"""Turn street decisions (data/research/streets.csv) into place rows (data/places_streets.csv).

match column:
  CUR:<name>   a current street, by exact name in the Paris register
  #<id>        a record in the vanished-streets register, by id; vanished records that say
               'Actuellement …', 'Dénommée …' or 'Voir : …' are followed to their successor
  DUP:<id>     this label duplicates another label
  (empty)      unresolved
Coordinates: for a current street, the point of the street nearest to the label's estimated
position (affine transform from data/gcps.csv). For a vanished street: the estimated position
itself, marked approx.
"""
import csv, json, re, sys, unicodedata
from pathlib import Path
import numpy as np
from rapidfuzz import fuzz
from shapely.geometry import shape, Point
from shapely.ops import nearest_points

root = Path(sys.argv[1])
ref = root / "work/ref"
OPENDATA = "https://opendata.paris.fr/explore/dataset/{ds}/table/?q=id%3D{id}"

cur = {str(v["id"]): v for v in json.load(open(ref / "voies_actuelles.json"))}
van = {str(v["id"]): v for v in json.load(open(ref / "voies_caduques.json"))}
cur_by_name = {}
for v in cur.values():
    cur_by_name.setdefault(v["typo_min"], []).append(v)
van_by_name = {}
for v in van.values():
    van_by_name.setdefault((v["typo_min"] or "").lower(), []).append(v)

g = list(csv.DictReader(open(root / "data/gcps.csv")))
A = np.array([[float(r["x"]), float(r["y"]), 1] for r in g])
c_lat = np.linalg.lstsq(A, np.array([float(r["lat"]) for r in g]), rcond=None)[0]
c_lon = np.linalg.lstsq(A, np.array([float(r["lon"]) for r in g]), rcond=None)[0]
def px2ll(x, y):
    return float(np.dot([x, y, 1], c_lat)), float(np.dot([x, y, 1], c_lon))

def nfd(s):
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()

SPECIAL = {"rue Madame de Sévigné": "Rue de Sévigné", "rue de La Reynie": "Rue de La Reynie",
           "rue Du Sommerard": "Rue Du Sommerard"}

def pretty(name):
    """Register names lack hyphens: 'rue du Petit Musc' -> 'Rue du Petit-Musc' (French usage)."""
    if name in SPECIAL:
        return SPECIAL[name]
    m = re.match(r"^(rue|ruelle|impasse|place|quai|boulevard|cour|passage|cul-de-sac|grand'rue)\s+((?:de la |de l'|du |des |de |d'|aux |au |à |la |le |les )?)(.*)$", name)
    if not m:
        return name[:1].upper() + name[1:]
    kind, art, rest = m.groups()
    small = {"de", "du", "des", "la", "le", "les", "l", "d", "et", "sur", "au", "aux", "à", "en"}
    words = re.split(r"(\s+)", rest)
    out, prev_word = [], None
    for w in words:
        if w.isspace():
            continue
        out.append(w)
    rest = "-".join(out).replace("'-", "'")
    return f"{kind[:1].upper()}{kind[1:]} {art}{rest}"

SUCC_RE = re.compile(r"(?:Actuellement|Dénommée?|Devenue|Englobée dans)\s+(?:d'abord\s+)?(?:une\s+)?(partie\s+(?:de\s+)?)?(?:la\s+|le\s+|l')?"
                     r"((?:rue|place|quai|boulevard|impasse|avenue|passage)\s+[^,.;(]+?)(?:\s*\(supprimée?\))?(?=\s*(?:par|,|\.|;| et |$))", re.I)
VOIR_RE = re.compile(r"Voir\s*:\s*([^()]+?)\s*\(([^)]+)\)")

def successor(v, depth=0):
    """Follow a vanished record to a current street. Returns (cur_record|None, is_part, chain)."""
    h = (v.get("historique") or "").replace("\r", " ").replace("\n", " ")
    m = VOIR_RE.search(h)
    if m and depth < 3:
        name = f"{m.group(2).strip().rstrip('.')} {m.group(1).strip()}".replace("  ", " ")
        name = re.sub(r"^(rue|imp|pas|place)\.?\s", lambda x: {"imp": "impasse ", "pas": "passage "}.get(x.group(1), x.group(1) + " "), name)
        for t in van_by_name.get(name.lower(), []):
            r = successor(t, depth + 1)
            if r[0] or r[2]:
                return r[0], r[1], [t["typo_min"]] + r[2]
        if name in cur_by_name:
            return cur_by_name[name][0], False, []
        return None, False, [name]
    for m in SUCC_RE.finditer(h):
        name = m.group(2).strip()
        # "Dénommée rue X (supprimée)": the successor was demolished too; a modern X is elsewhere.
        if "supprim" in (m.group(0) + h[m.end():m.end() + 14]).lower():
            continue
        for k in cur_by_name:
            if nfd(k) == nfd(name):
                return cur_by_name[k][0], bool(m.group(1)), []
    return None, False, []

def nearest_on(v, lat, lon):
    geom = shape(v["geo_shape"]["geometry"])
    p = nearest_points(geom, Point(lon, lat))[0]
    return round(p.y, 6), round(p.x, 6), geom.distance(Point(lon, lat)) * 85e3

def canon(s):
    """Normalise 16th-century and modern spellings so that the same name compares equal."""
    s = re.sub(r"[^a-z ]", " ", nfd(s).replace("-", " ").replace("'", " "))
    s = re.sub(r"\b(rue|r|la|le|les|de|du|des|d|l|au|aux|grant|grand|grande|saint|sainte|s|st)\b", " ", s)
    s = s.replace("y", "i").replace("v", "u").replace("j", "i").replace("th", "t").replace("ph", "f")
    s = re.sub(r"n(?=[bp])", "m", s)            # Lonbars ~ Lombards
    s = re.sub(r"(\w)\1", r"\1", s)            # doubled letters
    s = re.sub(r"[dt]\b", "t", s)               # Vaugirart ~ Vaugirard
    s = re.sub(r"(?<=\w)[sxz]\b", "", s)        # plural / silent endings
    s = re.sub(r"(?<=\w)e\b", "", s)
    return re.sub(r"\s+", " ", s).strip()

labels = {r["id"]: r for r in csv.DictReader(open(root / "data/labels_inventory.csv"))}
out = []
for d in csv.DictReader(open(root / "data/research/streets.csv")):
    L = labels[d["id"]]
    elat, elon = px2ll(int(L["x"]), int(L["y"]))
    row = {"id": d["id"], "old": L["text"], "modern": "", "status": "", "lat": "", "lon": "",
           "loc_confidence": "", "id_confidence": d["confidence"], "duplicate_of": "",
           "register": "", "history_fr": "", "sources": "", "note": d["note"], "check": ""}
    m = d["match"].strip()
    if m.startswith("DUP:"):
        row["duplicate_of"] = m[4:]
        out.append(row); continue
    if not m:
        row.update(lat=round(elat, 6), lon=round(elon, 6), loc_confidence="approx")
        out.append(row); continue
    if m.startswith("CUR:"):
        cands = cur_by_name.get(m[4:])
        if not cands:
            row["check"] = f"no current street named {m[4:]!r}"
            out.append(row); continue
        v, kind, part = cands[0], "CUR", None
    else:
        rid = m[1:]  # '#id' always refers to the vanished-streets register (ids overlap)
        v, kind = van.get(rid), "VAN"
        if v is None:
            row["check"] = f"no register record {rid}"
            out.append(row); continue
    src = [{"label": "Ville de Paris, street register (open data)",
            "url": OPENDATA.format(ds="denominations-emprises-voies-actuelles" if kind == "CUR" else "denominations-des-voies-caduques", id=v["id"])}]
    row["register"] = f"{kind}:{v['id']}"
    row["history_fr"] = (v.get("historique") or "").replace("\r", " ").replace("\n", " ").strip()
    if kind == "CUR":
        lat, lon, dist = nearest_on(v, elat, elon)
        same = fuzz.token_set_ratio(canon(L["text"]), canon(v["typo_min"])) >= 80
        row.update(modern=pretty(v["typo_min"]), status=d["status"] or ("standing" if same else "renamed"),
                   lat=lat, lon=lon, loc_confidence="exact")
        if dist > 450:
            row["check"] = f"street is {dist:.0f} m from the label's estimated position"
    else:
        succ, part, chain = successor(v)
        if succ is not None and d["status"] != "vanished":
            lat, lon, dist = nearest_on(succ, elat, elon)
            name = pretty(succ["typo_min"])
            row.update(modern=f"part of {name}" if part else name, status=d["status"] or "renamed",
                       lat=lat, lon=lon, loc_confidence="exact")
            src.append({"label": "Ville de Paris, street register (open data)",
                        "url": OPENDATA.format(ds="denominations-emprises-voies-actuelles", id=succ["id"])})
            if dist > 450:
                row["check"] = f"successor street is {dist:.0f} m from the label's estimated position"
        else:
            row.update(status=d["status"] or "vanished", lat=round(elat, 6), lon=round(elon, 6), loc_confidence="approx")
            if chain:
                row["note"] = (row["note"] + "; " if row["note"] else "") + "later " + " → ".join(chain)
    row["sources"] = json.dumps(src, ensure_ascii=False)
    out.append(row)

fields = list(out[0].keys())
with open(root / "data/places_streets.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(out)
from collections import Counter
print(Counter(r["status"] or ("duplicate" if r["duplicate_of"] else "unresolved") for r in out))
for r in out:
    if r["check"]:
        print("CHECK", r["id"], r["old"], "->", r["modern"], "|", r["check"])

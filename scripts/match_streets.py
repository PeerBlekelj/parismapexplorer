"""Suggest modern / vanished-street matches for every street label.

Sources (Paris open data, downloaded to work/ref/):
  voies_actuelles.json  current streets, with geometry and 'historique' (former names)
  voies_caduques.json   vanished streets, no geometry
Each label is compared with every name and former name (fuzzy, after 16th-century spelling
normalisation). Current streets far from the label's estimated position are penalised.
Output: work/street_candidates.csv, top candidates per label, for manual review.
"""
import csv, json, re, sys, unicodedata
from pathlib import Path
import numpy as np
from rapidfuzz import fuzz
from shapely.geometry import shape, Point

root = Path(sys.argv[1])
ref = root / "work/ref"

STOP = {"de", "la", "le", "les", "du", "des", "d", "l", "au", "aux", "en", "a", "et", "rue", "r",
        "ruelle", "grant", "grand", "grande", "petite", "cul", "sac"}

def canon(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = s.replace("'", " ").replace("’", " ").replace("-", " ").replace(".", " ")
    out = []
    for w in s.split():
        if w in ("s", "st", "ste", "saint", "sainte", "sainct"):
            out.append("st"); continue
        if w in STOP:
            continue
        w = w.replace("y", "i").replace("v", "u").replace("j", "i").replace("ph", "f")
        w = re.sub(r"c(?=[aou])", "k", w).replace("qu", "k")
        w = re.sub(r"h", "", w)
        w = re.sub(r"(.)\1", r"\1", w)
        w = re.sub(r"[sxz]$", "", w)
        w = re.sub(r"e$", "", w)
        out.append(w)
    return " ".join(out)

# Old-map pixel -> lat/lon, least-squares affine from the control points.
g = list(csv.DictReader(open(root / "data/gcps.csv")))
A = np.array([[float(r["x"]), float(r["y"]), 1] for r in g])
coef_lat = np.linalg.lstsq(A, np.array([float(r["lat"]) for r in g]), rcond=None)[0]
coef_lon = np.linalg.lstsq(A, np.array([float(r["lon"]) for r in g]), rcond=None)[0]
def px2ll(x, y):
    return float(np.dot([x, y, 1], coef_lat)), float(np.dot([x, y, 1], coef_lon))
res = [np.hypot((np.dot([float(r["x"]), float(r["y"]), 1], coef_lat) - float(r["lat"])) * 111e3,
                (np.dot([float(r["x"]), float(r["y"]), 1], coef_lon) - float(r["lon"])) * 73e3) for r in g]
print(f"affine residuals: median {np.median(res):.0f} m, max {max(res):.0f} m")

NAME_RE = re.compile(r"\b(?:rue|ruelle|cul-de-sac|impasse|place|carrefour|cour|passage|rue)\s+"
                     r"((?:(?:de la|de l'|du|des|de|d'|aux|au|la|le|les)\s*)?[A-ZÉÈÀÂÊÎÔÛÇ][\w'’\- ]{1,50}?)"
                     r"(?=\s*[,.;:()]|\s+(?:et|ou|qui|en|à|puis|dès|par|sur|entre|on|elle)\b|$)")
VARIANT_RE = re.compile(r"(?:écrit son nom|écrit|nommait|appelait|appelée?s?|dite?)\s*:?\s*((?:[A-ZÉ][\w'’\-]+(?:\s*\([^)]*\))?,?\s*)+)")

def names_from_history(h):
    if not h:
        return []
    out = [m.group(1).strip() for m in NAME_RE.finditer(h)]
    for m in VARIANT_RE.finditer(h):
        out += [re.sub(r"\(.*?\)", "", v).strip() for v in m.group(1).split(",") if v.strip()]
    return out

cands = []
for kind, fname in (("current", "voies_actuelles.json"), ("vanished", "voies_caduques.json")):
    for v in json.load(open(ref / fname)):
        if not v.get("typo_min"):
            continue
        geom = None
        if v.get("geo_shape"):
            try:
                geom = shape(v["geo_shape"]["geometry"])
            except Exception:
                geom = None
        names = [(v["typo_min"], "name")] + [(n, "former") for n in names_from_history(v.get("historique"))]
        for n, how in names:
            c = canon(n)
            if c:
                cands.append({"kind": kind, "rec": v["id"], "modern": v["typo_min"], "name": n, "how": how,
                              "c": c, "geom": geom, "hist": (v.get("historique") or "")[:240].replace("\n", " ")})
print(len(cands), "candidate names")

labels = [r for r in csv.DictReader(open(root / "data/labels_inventory.csv")) if r["type"] == "street"]
rows = []
for L in labels:
    lc = canon(L["text"])
    lat, lon = px2ll(int(L["x"]), int(L["y"]))
    pt = Point(lon, lat)
    scored = {}
    for c in cands:
        s = max(fuzz.token_sort_ratio(lc, c["c"]), fuzz.ratio(lc.replace(" ", ""), c["c"].replace(" ", "")))
        if s < 70:
            continue
        dist = c["geom"].distance(pt) * 85e3 if c["geom"] is not None else None
        adj = s - (min(30, (dist - 400) / 50) if dist and dist > 400 else 0)
        k = (c["kind"], c["rec"])
        if k not in scored or adj > scored[k]["adj"]:
            scored[k] = {**c, "score": s, "adj": adj, "dist": dist}
    top = sorted(scored.values(), key=lambda c: -c["adj"])[:4]
    for rank, c in enumerate(top, 1):
        rows.append([L["id"], L["text"], rank, round(c["adj"]), c["score"], c["kind"], c["rec"], c["modern"],
                     c["name"], c["how"], "" if c["dist"] is None else round(c["dist"]), c["hist"]])
    if not top:
        rows.append([L["id"], L["text"], 0, "", "", "", "", "", "", "", "", ""])

with open(root / "work/street_candidates.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "old", "rank", "adj", "score", "kind", "rec", "modern", "matched_name", "how", "dist_m", "historique"])
    w.writerows(rows)
n_hit = len({r[0] for r in rows if r[2] == 1})
n_strong = len({r[0] for r in rows if r[2] == 1 and r[3] != "" and r[3] >= 90})
print(f"{len(labels)} street labels: {n_hit} with a candidate, {n_strong} with a strong one (>=90)")

"""Build the app's data files (web/public/data/*.json) from data/.

Contract with the app (see web/DATA_CONTRACT.md). Fields that are not researched yet are null,
never empty strings or guesses: the app must show null as "not identified yet".
"""
import csv, json, re, sys, datetime
from pathlib import Path

root = Path(sys.argv[1])
out = root / "web/public/data"
out.mkdir(parents=True, exist_ok=True)

ident = {}
for p in sorted((root / "data").glob("places_*.csv")):  # research results per category, keyed by label id
    for r in csv.DictReader(open(p)):
        if r["id"] in ident:
            sys.exit(f"{r['id']} researched twice ({p.name})")
        ident[r["id"]] = r

def nn(v):
    return v if v not in ("", None) else None

# Bookkeeping left by the tile-by-tile transcription pass ("already recorded in the previous
# tile"); `seen_in` carries the same fact. Not something to show on a place's card.
INV_BOOKKEEPING = {"dup", "dupe", "duplicate"}

def inv_note(v):
    v = nn(v)
    return None if v and v.strip().lower() in INV_BOOKKEEPING else v

def read_summaries(name):
    out = {}
    p = root / "data/research" / name
    if p.exists():
        for r in csv.DictReader(open(p, encoding="utf-8")):
            if r["id"] in out:
                sys.exit(f"{r['id']} has two summaries in {name}")
            out[r["id"]] = r["summary"].strip()
    return out

# English summaries, and their French and Swedish translations (same ids; a missing one is null
# and the app falls back to English).
summaries = read_summaries("summaries.csv")
summaries_fr = read_summaries("summaries_fr.csv")
summaries_sv = read_summaries("summaries_sv.csv")
for lang, tr in (("fr", summaries_fr), ("sv", summaries_sv)):
    extra = sorted(set(tr) - set(summaries))
    if extra:
        sys.exit(f"summaries_{lang}.csv has ids with no English summary: {', '.join(extra[:10])}")

# Jules Cousin's 1875 table of the map's names (data/research/cousin.csv, from scripts/cousin_match.py):
# cited on every place it lists, linked to the page on Gallica (Gallica page = printed page + 8).
COUSIN = "https://gallica.bnf.fr/ark:/12148/bpt6k6310467r/f{f}.item"
SMALL = {"de", "du", "des", "la", "le", "les", "l", "d", "l'", "d'", "l’", "d’", "et", "ou", "en", "au", "aux", "sur", "sous", "a"}


def cousin_name(n):
    """Cousin's index form to a plain name, searchable as a variant: 'FÉCAMP (hôtel de)' -> 'Hôtel de Fécamp'."""
    m = re.match(r"^(.*?)\s*\(([^)]*)\)\s*(.*)$", n)
    head, pre, rest = (m.group(1), m.group(2).strip(), m.group(3).strip()) if m else (n, "", "")
    m2 = re.match(r"^([^a-z]+?)\s+(\S*[a-z].*)$", head)  # 'SAINT-MICHEL du Palais'
    if m2:
        head, rest = m2.group(1), (m2.group(2) + " " + rest).strip()
    if not head.isupper():
        return n
    words = re.split(r"([\s-]+|(?<=['’]))", head.lower())
    head = "".join(w if (w in SMALL and i) else w[:1].upper() + w[1:] for i, w in enumerate(words))
    if pre[:1].isupper() and pre != "L'":  # a qualifier, not a prefix: 'HÔPITAL (St-Médard)'
        out = f"{head} ({pre})"
    elif pre.startswith(("de ", "du ", "des ")):  # a complement: 'HÔPITAL (de Notre-Dame-des-Champs)'
        out = f"{head} {pre}"
    elif pre in ("le", "la", "les", "L'") or not pre or pre.startswith(("sans", "les —")):
        out = (pre.capitalize() + " " if pre in ("le", "la", "les") else "L'" if pre == "L'" else "") + head
    else:
        out = pre + ("" if pre.endswith(("'", "’")) else " ") + head
    if rest and not rest.startswith(","):
        out += " " + rest
    return out[:1].upper() + out[1:]


cousin = {}
p = root / "data/research/cousin.csv"
if p.exists():
    for r in csv.DictReader(open(p, encoding="utf-8")):
        cousin[r["id"]] = {"label": f"Cousin 1875, p. {r['page']}", "url": COUSIN.format(f=int(r["page"]) + 8),
                           "name": cousin_name(r["cousin_name"])}

# A label that repeats another (e.g. a second "LA VILLE NEUVE") is not a place of its own, but its
# position stays clickable on the old map: it is listed under the main place as `also_px`.
inv_rows = list(csv.DictReader(open(root / "data/labels_inventory.csv")))
also = {}
for r in inv_rows:
    dup = nn(ident.get(r["id"], {}).get("duplicate_of"))
    if dup:
        also.setdefault(dup, []).append([int(r["x"]), int(r["y"])])

places = []
for r in inv_rows:
    if r["type"] == "decoration":
        continue
    i = ident.get(r["id"], {})
    if nn(i.get("duplicate_of")):
        continue  # a second reading of the same label
    places.append({
        "id": r["id"],
        "old": r["text"],
        "type": r["type"],
        "px": [int(r["x"]), int(r["y"])],
        "also_px": also.get(r["id"], []),
        "orient": r["orient"],
        "flag": r["flag"],
        "note": nn(i.get("note")) or inv_note(r["note"]),
        "modern": nn(i.get("modern")),
        "status": nn(i.get("status")),
        "lat": float(i["lat"]) if nn(i.get("lat")) else None,
        "lon": float(i["lon"]) if nn(i.get("lon")) else None,
        "loc_confidence": nn(i.get("loc_confidence")),
        "summary": nn(summaries.get(r["id"])) or nn(i.get("summary")),
        "summary_fr": nn(summaries_fr.get(r["id"])),
        "summary_sv": nn(summaries_sv.get(r["id"])),
        "variants": [v for v in (i.get("variants") or "").split("|") if v]
                    + ([cousin[r["id"]]["name"]] if r["id"] in cousin else []),
        "sources": (json.loads(i["sources"]) if nn(i.get("sources")) else [])
                   + ([{k: cousin[r["id"]][k] for k in ("label", "url")}] if r["id"] in cousin else []),
    })

# --auto-gcps: use the larger set built by scripts/fit_transform.py (needs a TPS in the app).
if "--auto-gcps" in sys.argv:
    gcps = [{"id": g["id"], "name": g["name"], "px": [int(g["x"]), int(g["y"])],
             "lat": float(g["lat"]), "lon": float(g["lon"]), "quality": "label" if g["source"] == "hand" else "place"}
            for g in csv.DictReader(open(root / "data/gcps_auto.csv"))]
else:
    gcps = [{"id": g["id"], "name": g["name"], "px": [int(g["x"]), int(g["y"])],
             "lat": float(g["lat"]), "lon": float(g["lon"]), "quality": g["quality"]}
            for g in csv.DictReader(open(root / "data/gcps.csv"))]

meta = {"generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "image": {"width": 10890, "height": 7820, "orientation": "east-up"}}
json.dump({**meta, "places": places}, open(out / "places.json", "w"), ensure_ascii=False, indent=0)
json.dump({**meta, "gcps": gcps}, open(out / "gcps.json", "w"), ensure_ascii=False, indent=1)
print(len(places), "places,", len(gcps), "gcps")

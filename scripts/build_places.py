"""Build the app's data files (web/public/data/*.json) from data/.

Contract with the app (see web/DATA_CONTRACT.md). Fields that are not researched yet are null,
never empty strings or guesses: the app must show null as "not identified yet".
"""
import csv, json, sys, datetime
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

places = []
for r in csv.DictReader(open(root / "data/labels_inventory.csv")):
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
        "orient": r["orient"],
        "flag": r["flag"],
        "note": nn(i.get("note")) or nn(r["note"]),
        "modern": nn(i.get("modern")),
        "status": nn(i.get("status")),
        "lat": float(i["lat"]) if nn(i.get("lat")) else None,
        "lon": float(i["lon"]) if nn(i.get("lon")) else None,
        "loc_confidence": nn(i.get("loc_confidence")),
        "summary": nn(i.get("summary")),
        "variants": [v for v in (i.get("variants") or "").split("|") if v],
        "sources": json.loads(i["sources"]) if nn(i.get("sources")) else [],
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

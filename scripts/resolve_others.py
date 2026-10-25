"""Turn data/research/others.csv + work/wiki_cache.json into data/places_others.csv.

Coordinates, in order of preference: Wikipedia article coordinates, Wikidata P625, the
position estimated from the old map (affine transform from data/gcps.csv). Wikipedia/Wikidata
coordinates for a building that still stands count as exact; anything else as approx.
The 'coords' column overrides: "map" forces the map estimate (article coordinates describe a
different site, e.g. after a move), "lat,lon" sets a position by hand.
Rows whose source coordinates lie far from the map-estimated position are flagged for review.
"""
import csv, json, math, sys, time, urllib.parse, urllib.request
from pathlib import Path
import numpy as np

root = Path(sys.argv[1])
UA = "parismapexplorer/0.1 (https://github.com/PeerBlekelj/parismapexplorer)"
wiki = json.load(open(root / "work/wiki_cache.json"))["pages"]
wd_p = root / "work/wikidata_coords.json"
wd = json.load(open(wd_p)) if wd_p.exists() else {}

# Features whose article coordinates don't describe the spot on this map (rivers: their source).
USE_MAP_POSITION = {"L0185", "L0186"}
FAR_OK_TYPES = {"village_faubourg", "other"}  # large areas: article point may be far from the label

g = list(csv.DictReader(open(root / "data/gcps.csv")))
A = np.array([[float(r["x"]), float(r["y"]), 1] for r in g])
c_lat = np.linalg.lstsq(A, np.array([float(r["lat"]) for r in g]), rcond=None)[0]
c_lon = np.linalg.lstsq(A, np.array([float(r["lon"]) for r in g]), rcond=None)[0]
def px2ll(x, y):
    return float(np.dot([x, y, 1], c_lat)), float(np.dot([x, y, 1], c_lon))
def dist_m(a, b):
    return math.hypot((a[0] - b[0]) * 111.2e3, (a[1] - b[1]) * 111.2e3 * math.cos(math.radians(a[0])))

rows = list(csv.DictReader(open(root / "data/research/others.csv")))
need = sorted({wiki[r["wiki_fr"]]["qid"] for r in rows if r["wiki_fr"] and not wiki[r["wiki_fr"]].get("missing")
               and wiki[r["wiki_fr"]]["lat"] is None and wiki[r["wiki_fr"]].get("qid")} - set(wd))
for i in range(0, len(need), 40):
    ids = need[i:i + 40]
    u = "https://www.wikidata.org/w/api.php?" + urllib.parse.urlencode(
        {"action": "wbgetentities", "ids": "|".join(ids), "props": "claims", "format": "json"})
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=30))
    for q in ids:
        claims = d["entities"].get(q, {}).get("claims", {}).get("P625", [])
        v = claims[0]["mainsnak"].get("datavalue", {}).get("value") if claims else None
        wd[q] = [v["latitude"], v["longitude"]] if v else None
    time.sleep(0.5)
json.dump(wd, open(wd_p, "w"), indent=0)

labels = {r["id"]: r for r in csv.DictReader(open(root / "data/labels_inventory.csv"))}
out, flags = [], []
for r in rows:
    L = labels[r["id"]]
    est = px2ll(int(L["x"]), int(L["y"]))
    row = {"id": r["id"], "old": L["text"], "modern": r["modern"], "status": r["status"], "lat": "", "lon": "",
           "loc_confidence": "", "id_confidence": r["confidence"], "duplicate_of": r["dup_of"],
           "register": "", "history_fr": "", "sources": "", "note": r["note"], "check": ""}
    if r["dup_of"]:
        out.append(row); continue
    src, ll, how = [], None, "map"
    p = wiki.get(r["wiki_fr"]) if r["wiki_fr"] else None
    if p and not p.get("missing"):
        row["register"] = p.get("qid") or ""
        row["history_fr"] = p.get("extract", "").replace("\n", " ")
        src.append({"label": "Wikipédia (fr)", "url": p["url"]})
        if p.get("en"):
            src.append({"label": "Wikipedia (en)", "url": "https://en.wikipedia.org/wiki/" + urllib.parse.quote(p["en"].replace(" ", "_"))})
        if p.get("qid"):
            src.append({"label": "Wikidata", "url": f"https://www.wikidata.org/wiki/{p['qid']}"})
        if r["id"] not in USE_MAP_POSITION and r.get("coords") != "map":
            if p.get("lat") is not None:
                ll, how = (p["lat"], p["lon"]), "wikipedia"
            elif p.get("qid") and wd.get(p["qid"]):
                ll, how = tuple(wd[p["qid"]]), "wikidata"
    if r.get("coords") not in ("", "map", None):  # manual "lat,lon"
        ll, how = tuple(float(v) for v in r["coords"].split(",")), "manual"
    if ll is None:
        ll = est
    d = dist_m(ll, est)
    if how != "map" and d > 600 and L["type"] not in FAR_OK_TYPES:
        row["check"] = f"{how} position is {d:.0f} m from the map-estimated position"
    exact = how != "map" and r["status"] in ("standing", "rebuilt", "renamed")
    row.update(lat=round(ll[0], 6), lon=round(ll[1], 6),
               loc_confidence="exact" if exact else ("uncertain" if r["confidence"] == "low" and how == "map" else "approx"))
    row["sources"] = json.dumps(src, ensure_ascii=False) if src else ""
    out.append(row)

with open(root / "data/places_others.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
from collections import Counter
print(Counter(r["status"] or "dup" for r in out))
print("location from:", Counter(("wiki/wd" if r["sources"] and r["loc_confidence"] == "exact" else r["loc_confidence"]) for r in out if not r["duplicate_of"]))
for r in out:
    if r["check"]:
        print("CHECK", r["id"], r["old"], "|", r["check"])

"""Merge per-tile label readings into one deduplicated inventory.

Tiles overlap by 300 px, so the same label is often read twice. Two readings are the same
label when their normalised text matches and they lie within DUP_DIST px. Partial readings
(cut at a tile edge) are dropped when a full reading lies within PARTIAL_DIST px and starts
with or contains the fragment.
"""
import csv, math, re, sys, unicodedata
from pathlib import Path

root = Path(sys.argv[1])
DUP_DIST, PARTIAL_DIST = 200, 350

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().upper()
    return re.sub(r"[^A-Z ]", "", s.replace(".", " ")).split()

def key(s):
    return " ".join(norm(s))

rows = []
for f in sorted((root / "data/labels_raw").glob("r*.csv")):
    for r in csv.DictReader(open(f)):
        r["tile"], r["x"], r["y"] = f.stem, int(r["x"]), int(r["y"])
        rows.append(r)

full = [r for r in rows if r["flag"] != "partial"]
partial = [r for r in rows if r["flag"] == "partial"]

merged = []
for r in full:
    for m in merged:
        if key(m["text"]) == key(r["text"]) and math.dist((m["x"], m["y"]), (r["x"], r["y"])) < DUP_DIST:
            m["seen"].append(r["tile"])
            if not m["note"] and r["note"]:
                m["note"] = r["note"]
            if r["flag"] == "unsure":
                m["flag"] = "unsure"
            break
    else:
        merged.append({**r, "seen": [r["tile"]]})

orphans = []
for p in partial:
    frag = key(p["text"])
    if any(math.dist((m["x"], m["y"]), (p["x"], p["y"])) < PARTIAL_DIST and frag and
           (frag in key(m["text"]) or key(m["text"]).startswith(frag[:3])) for m in merged):
        continue
    orphans.append(p)

DECOR = {"SUBSOLANUS", "AUSTER", "FAVONIUS", "SEPTENTRIONES", "ORIENS", "OCCIDENS"}
VILLAGES = {"BELE VILE", "BANIOLET", "PROPINCOURT", "MONTREUIL SUR LE BOIS", "CONFLANS", "PERCI",
            "IVERI", "VITERI", "VILLE IUIVE", "BISSESTRE", "GENTILI", "CLINNIENCOURT", "MONMARTRE",
            "LA VILLE NEUVE", "LA VILLE LEVESQUE", "LE ROULLE", "CHALIOT", "AUTEUL", "REUILLI",
            "LES TORCHERONS", "LA COURTILLE", "LA GRANCHE BATELIERE", "LES MARES"}
COLLEGE_HINT = {"BON COURT", "NAVARRE", "LA MARCHE", "PRELLE", "BEAUVAIS", "CORNALLE", "ALBRET",
                "LONBARS", "COQUERET", "RAINS", "MONT EGU", "LEMAN", "LE PLESSI", "MARMOUTIERS",
                "LISIEUX", "CALVI", "CLUGNI", "NERBONNE", "BOURGONGNE", "C SORBONNE", "C DE IUSTICE",
                "C S BARBE", "LE CARDINAL LEMOINE", "COLEGE MAISTRE GERVAIS", "LA CHAPELLE MIGNON",
                "LE COLLEGE S GERMAIN", "LES BONS ENFANS", "LES DE BONS ENFANS", "LE GRANT DECRET",
                "LOTEL DE HEROCOURT", "LES CHOLES"}

# Labels without "R." that name streets (trade streets and the like), per the map's usage.
STREET_NAMES = {"LA VIELE R DU TAMPLE", "LA COURRERIE", "LA VIELLE CORRERIE", "LA COCHONNERIE",
                "LA HEAUMERIE", "LA VIEILLE PELETERIE", "LA SAVATERIE", "LA PARCHEMINERIE",
                "LA FRIPERIE", "LA LINGERIE", "LA TANNERIE", "LE MONT S GENEVIEVE", "LE CLOS BRUNEAU",
                "LA PIERRE AU LART", "LE PAVE"}
SQUARES = {"LA PLACE DE GREVE", "LA PLACE MAUBERT", "LA PLACE AU VIAUX", "LE CARFOUR GILORI",
           "LA CROIX DU TIROY", "LE PILORI", "LE MARCHE AUX POURCEAUX", "LA HALLE AU BLE",
           "LA GRANT BOUCHERIE", "LA BOUCHERIE DE BEAUVAIS", "LA FOIRE S GERMAIN", "LE PORT AU FIN"}

def classify(t, note):
    k = key(t)
    n = (note or "").lower()
    if k in STREET_NAMES:
        return "street"
    if k in SQUARES:
        return "square_market"
    if k in DECOR:
        return "decoration"
    if k in COLLEGE_HINT or "college" in n:
        return "college"
    if re.match(r"^(LA |LE )?(GRANT )?R |^RUE |^LA R |^LA GRANT R ", k + " ") or "rue " in n[:4] or k.startswith("CUDESAC"):
        return "street"
    if k.startswith("PORTE ") or "BASTILLON" in k or k in {"LA BASTILLE", "LA TOUR NELLE", "LA TOUR DU BOIS"}:
        return "gate_wall"
    if "PONT" in k.split():
        return "bridge"
    if k in VILLAGES or k.startswith("LES FAUBOURS"):
        return "village_faubourg"
    if re.match(r"^(S |NOSTRE|LES (CELESTINS|CORDELIERS|CORDELIERES|CARMES|MATURINS|IACOPINS|AUGUSTINS|BERNARDINS|BILLETTES|FILLES|CHARTEREUS|ENFANS|QUINSE|BONS HOMMES|AUDRIETTES)|LAVE MARIA|LEGLISE|LA CHAPELLE|LE SEPULCRE|LA MADELINNE|LES ESPERIT|LOPITAL|LOSPITAL|LOSTEL DIEU|LOTEL DIEU|CIMETIERE|LE CIMETIERE|CLOISTRE|LE CLOISTRE)", k):
        return "church_religious"
    if k.startswith(("LOSTEL", "LOTEL", "LOSTE")) or k in {"LE LOUVRE", "LE PALAYS", "LES TOURNELLES", "LA CONCIERGERIE", "CHATELET", "PETIT CHATELET", "LORLOGE", "LA CHAMBRE DES CONTES", "LA MONNOIE", "LE FOUR LEVESQUE"}:
        return "building"
    return "other"

for m in merged:
    m["type"] = classify(m["text"], m["note"])

merged.sort(key=lambda m: (m["type"], m["y"] // 500, m["x"]))
out = root / "data/labels_inventory.csv"
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "text", "type", "x", "y", "orient", "flag", "note", "seen_in"])
    for i, m in enumerate(merged, 1):
        w.writerow([f"L{i:04d}", m["text"], m["type"], m["x"], m["y"], m["orient"], m["flag"], m["note"], " ".join(m["seen"])])
with open(root / "data/labels_orphan_fragments.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["text", "x", "y", "tile", "note"])
    for p in orphans:
        w.writerow([p["text"], p["x"], p["y"], p["tile"], p["note"]])

from collections import Counter
c = Counter(m["type"] for m in merged)
print("raw readings:", len(rows), "| merged labels:", len(merged), "| orphan fragments:", len(orphans))
for t, n in c.most_common():
    print(f"  {t:18s}{n}")
print("unsure:", sum(m["flag"] == "unsure" for m in merged))

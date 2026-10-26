"""Match our label inventory against Jules Cousin's 1875 table of the map's names.

Input: data/research/cousin_1875_table.txt (transcribed: name | printed | refs | note), data/labels_inventory.csv.
1. Normalise both sides (accents, u/v, i/j, y/i, S. -> SAINT, articles, spacing) and score every
   label against every entry's printed form (or corrected name) with rapidfuzz.
2. Fit Cousin's sheet layout (8 sheets, each split 3x3, squares numbered row by row) from the
   confident matches: try every arrangement of the sheets over a 4x2 grid and keep the one under
   which most matches fall in a square Cousin gives.
3. Re-score every label with the position check folded in and write work/cousin/matches.csv.
Usage: .venv/bin/python scripts/cousin_match.py .
"""
import csv, itertools, re, sys, unicodedata
from pathlib import Path
from rapidfuzz import fuzz

root = Path(sys.argv[1])
W, H = 10890, 7820
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8}


def norm(s):
    s = unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().upper()
    s = re.sub(r"\([^)]*\)", lambda m: " " + m.group(0)[1:-1] + " ", s)
    s = s.replace("'", " ").replace("-", " ").replace(".", " ").replace(",", " ")
    s = re.sub(r"\bS\b|\bST\b|\bSTE\b", "SAINT", s)
    s = re.sub(r"\bR\b|\bRUE\b", "RUE", s)
    s = s.replace("V", "U").replace("J", "I").replace("Y", "I").replace("PH", "F")
    s = re.sub(r"\b(LE|LA|LES|DE|DES|DU|D|L|AU|AUX|EN|ET|OU|LOSTEL|LOTEL|HOTEL|GRANT|GRAND)\b", " ", s)
    s = re.sub(r"LOSTEL|LOTEL", "", s)
    return re.sub(r"\s+", " ", s).strip()


entries = []
for line in open(root / "data/research/cousin_1875_table.txt", encoding="utf-8"):
    if line.startswith("#") or not line.strip():
        continue
    name, printed, refs, note = [x.strip() for x in line.split("|")]
    if note.startswith("voy.") and not refs:
        continue  # cross-references only
    rr = []
    for r in filter(None, refs.split(";")):
        sh, _, sq = r.partition(",")
        rr.append((ROMAN[sh], int(sq) if sq else None))
    entries.append({"name": name, "printed": printed, "refs": rr, "note": note,
                    "keys": [k for k in {norm(printed), norm(name)} if k]})

labels = list(csv.DictReader(open(root / "data/labels_inventory.csv", encoding="utf-8")))


def best(lab):
    t = norm(lab["text"])
    sc = []
    for i, e in enumerate(entries):
        s = max(fuzz.token_sort_ratio(t, k) for k in e["keys"])
        sc.append((s, i))
    sc.sort(reverse=True)
    return t, sc[:8]


cand = {lab["id"]: best(lab) for lab in labels}

# ---------- fit the sheet layout ----------
def cell(x, y, pos_of_sheet, cols, rows):
    sw, sh = W / cols, H / rows
    c, r = min(int(x // sw), cols - 1), min(int(y // sh), rows - 1)
    p = r * cols + c
    sx, sy = min(int((x - c * sw) // (sw / 3)), 2), min(int((y - r * sh) // (sh / 3)), 2)
    return pos_of_sheet[p], sy * 3 + sx + 1


conf = [(lab, entries[cand[lab["id"]][1][0][1]]) for lab in labels if cand[lab["id"]][1][0][0] >= 92]
print(len(conf), "confident name matches used for the layout fit")
bestfit = None
for cols, rows in ((4, 2), (2, 4)):
    for perm in itertools.permutations(range(1, 9)):
        hits = sum(1 for lab, e in conf if any(
            s == a and (b is None or q == b) for (a, b) in e["refs"]
            for s, q in [cell(int(lab["x"]), int(lab["y"]), perm, cols, rows)]))
        if not bestfit or hits > bestfit[0]:
            bestfit = (hits, cols, rows, perm)
hits, cols, rows, perm = bestfit
print(f"layout {cols}x{rows}, sheet at each position (row by row): {perm}; {hits}/{len(conf)} matches in Cousin's square")
sheet_hits = sum(1 for lab, e in conf if any(a == cell(int(lab["x"]), int(lab["y"]), perm, cols, rows)[0] for a, _ in e["refs"]))
print(f"  ... {sheet_hits}/{len(conf)} at least on the right sheet")


def roman(n):
    return [k for k, v in ROMAN.items() if v == n][0]


def near(lab, e):
    """0: right square, 1: neighbouring square on the right sheet or an adjacent sheet edge, 2: elsewhere."""
    x, y = int(lab["x"]), int(lab["y"])
    if any(e2 for e2 in []):
        pass
    s, q = cell(x, y, perm, cols, rows)
    if any(a == s and (b is None or b == q) for a, b in e["refs"]):
        return 0
    for dx in (-350, 0, 350):
        for dy in (-350, 0, 350):
            s2, q2 = cell(min(max(x + dx, 0), W - 1), min(max(y + dy, 0), H - 1), perm, cols, rows)
            if any(a == s2 and (b is None or b == q2) for a, b in e["refs"]):
                return 1
    return 2


STREETY = re.compile(r"\((rue|place|carrefour)|\brue\b", re.I)


def kind_bonus(lab, e):
    """A street label prefers Cousin's street entry, a building label the building of the same name."""
    street = STREETY.search(e["name"]) is not None
    return 6 if (lab["type"] == "street") == street else 0


with open(root / "work/cousin/matches.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["id", "text", "cell", "score", "pos", "cousin_name", "cousin_printed", "cousin_refs", "cousin_note", "alt"])
    for lab in labels:
        t, sc = cand[lab["id"]]
        # rank by name score, with a bonus for being where Cousin says
        ranked = sorted(((s - 12 * near(lab, entries[i]) + kind_bonus(lab, entries[i]), s, i) for s, i in sc), reverse=True)
        adj, s, i = ranked[0]
        e = entries[i]
        sh, sq = cell(int(lab["x"]), int(lab["y"]), perm, cols, rows)
        alt = "; ".join(f"{entries[j]['name']} ({s2})" for _, s2, j in ranked[1:3])
        w.writerow([lab["id"], lab["text"], f"{roman(sh)},{sq}", s, near(lab, e), e["name"], e["printed"],
                    ";".join(f"{roman(a)},{b or ''}" for a, b in e["refs"]), e["note"], alt])
print("wrote work/cousin/matches.csv")

# ---------- data/research/cousin.csv: the reviewed pairing of each label with Cousin's entry ----------
# Hand review of the weaker matches: the matcher's pick replaced by the right entry (usually a convent
# paired with the street of the same name), or dropped where Cousin has no entry for the label.
OVERRIDE = {
    "L0040": "CORDELIÈRES (couvent des)", "L0062": "BERNARDINS (couvent des)", "L0064": "SAINT-ÉTIENNE-DU-MONT (église)",
    "L0084": "CARMES (couvent des)", "L0086": "SAINT-HILAIRE (église)", "L0090": "NOTRE-DAME-DES-CHAMPS (église et prieuré)",
    "L0106": "SAINT-MICHEL du Palais (chapelle)", "L0108": "MATHURINS (couvent des)", "L0112": "FILLES-DIEU (couvent des)",
    "L0113": "SAINT-SAUVEUR (église)", "L0116": "CORDELIERS (couvent des)", "L0121": "AUGUSTINS (couvent des)",
    "L0123": "SAINT-HONORÉ (église)", "L0126": "SAINT-THOMAS-DU-LOUVRE (église)", "L0155": "CALVI (collège de)",
    "L0159": "ÉCOLE SAINT GERMAIN-L'AUXERROIS (L')", "L0308": "CIMETIÈRE ST-NICOLAS (rue du)",
    "L0363": "PERCÉE-ST-ANDRÉ (rue)", "L0367": "FOIN-ST-JACQUES (rue du)", "L0386": "FOUR-ST-HONORÉ (rue du)",
    "L0403": "SERPENTE (rue)", "L0365": "SERPENTE (rue de la)", "L0429": "AUTRUCHE (rue de l'), ou rue d'Autriche",
    "L0470": "TIRON ou TISON (rue)", "L0199": "HARCOURT (collège d')", "L0151": "HARCOURT (hôtel d')",
    "L0311": "POTERIE (rue de la Vieille)", "L0339": "PALÉE (rue)", "L0250": "GARNIER-SUR-L'EAU (rue)",
}
DROP = {"L0067", "L0163", "L0404"}
page_of, cur_page = {}, None
for line in open(root / "data/research/cousin_1875_table.txt", encoding="utf-8"):
    m = re.match(r"# p\. (\d+)", line)
    if m:
        cur_page = int(m.group(1))
    elif line.strip() and not line.startswith("#"):
        page_of.setdefault(line.split("|")[0].strip(), cur_page)
by_name = {e["name"]: e for e in entries}
out = []
for r in csv.DictReader(open(root / "work/cousin/matches.csv", encoding="utf-8")):
    good = (float(r["score"]) >= 85 and r["pos"] != "2") or (float(r["score"]) >= 60 and r["pos"] == "0")
    if r["id"] in DROP or not (good or r["id"] in OVERRIDE):
        continue
    name = OVERRIDE.get(r["id"], r["cousin_name"])
    if name not in by_name:
        sys.exit(f"{r['id']}: no Cousin entry named {name!r}")
    e = by_name[name]
    out.append({"id": r["id"], "cousin_name": name, "printed": e["printed"],
                "refs": ";".join(f"{roman(a)},{b or ''}".rstrip(",") for a, b in e["refs"]),
                "page": page_of[name], "note": e["note"]})
with open(root / "data/research/cousin.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()), lineterminator="\n")
    w.writeheader(); w.writerows(out)
print(f"data/research/cousin.csv: {len(out)} labels paired with Cousin's entries")

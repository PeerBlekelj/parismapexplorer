"""Print Paris open-data street records whose name contains each argument (case/accent-insensitive)."""
import json, sys, unicodedata
from pathlib import Path
ref = Path(__file__).resolve().parent.parent / "work/ref"
def n(s): return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
data = [("CUR", v) for v in json.load(open(ref / "voies_actuelles.json"))] + \
       [("VAN", v) for v in json.load(open(ref / "voies_caduques.json"))]
for q in sys.argv[1:]:
    print(f"#### {q}")
    for k, v in data:
        if n(q) in n(v.get("typo_min")):
            h = (v.get("historique") or "").replace("\r", " ").replace("\n", " ")
            print(f"{k} {v['id']} {v['typo_min']} [{v.get('arrdt')}] :: {h[:330]}")

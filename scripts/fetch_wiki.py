"""Verify French Wikipedia titles in data/research/others.csv and fetch facts for each.

For every title: follows redirects, gets coordinates, Wikidata id, English sitelink and the
intro extract. Titles that don't exist, and rows without a title, get search suggestions.
Cache: work/wiki_cache.json (re-runs only fetch what's new). Report: work/wiki_report.txt.
"""
import csv, json, sys, time, urllib.parse, urllib.request
from pathlib import Path

root = Path(sys.argv[1])
UA = "parismapexplorer/0.1 (https://github.com/PeerBlekelj/parismapexplorer)"
API = "https://fr.wikipedia.org/w/api.php"
cache_p = root / "work/wiki_cache.json"
cache = json.load(open(cache_p)) if cache_p.exists() else {"pages": {}, "search": {}}

def get(params):
    params = {**params, "format": "json", "formatversion": "2"}
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(params), headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            return json.load(urllib.request.urlopen(req, timeout=30))
        except Exception as e:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"failed: {params}")

rows = list(csv.DictReader(open(root / "data/research/others.csv")))
titles = sorted({r["wiki_fr"] for r in rows if r["wiki_fr"] and r["wiki_fr"] not in cache["pages"]})
for i in range(0, len(titles), 20):
    batch = titles[i:i + 20]
    d = get({"action": "query", "titles": "|".join(batch), "redirects": 1,
             "prop": "coordinates|pageprops|langlinks|extracts|info", "inprop": "url",
             "lllang": "en", "exintro": 1, "explaintext": 1, "exlimit": "max", "ppprop": "wikibase_item|disambiguation"})
    q = d["query"]
    alias = {}
    for n in q.get("normalized", []):
        alias[n["from"]] = n["to"]
    for rd in q.get("redirects", []):
        alias[rd["from"]] = rd["to"]
    pages = {p["title"]: p for p in q["pages"]}
    for t in batch:
        final = t
        while final in alias:
            final = alias[final]
        p = pages.get(final, {"missing": True})
        if p.get("missing"):
            cache["pages"][t] = {"missing": True}
            continue
        c = (p.get("coordinates") or [{}])[0]
        cache["pages"][t] = {
            "title": p["title"], "url": p.get("fullurl"),
            "qid": p.get("pageprops", {}).get("wikibase_item"),
            "disambiguation": "disambiguation" in p.get("pageprops", {}),
            "lat": c.get("lat"), "lon": c.get("lon"),
            "en": (p.get("langlinks") or [{}])[0].get("title"),
            "extract": (p.get("extract") or "")[:1500],
        }
    time.sleep(0.5)

def search(q):
    if q not in cache["search"]:
        d = get({"action": "query", "list": "search", "srsearch": q, "srlimit": 5})
        cache["search"][q] = [s["title"] for s in d["query"]["search"]]
        time.sleep(0.3)
    return cache["search"][q]

labels = {r["id"]: r for r in csv.DictReader(open(root / "data/labels_inventory.csv"))}
lines = []
for r in rows:
    if r["dup_of"]:
        continue
    t = r["wiki_fr"]
    if t:
        p = cache["pages"][t]
        if p.get("missing"):
            lines.append(f"MISSING {r['id']} {t!r} -> search: {search(t + ' Paris')}")
        elif p["disambiguation"]:
            lines.append(f"DISAMBIG {r['id']} {t!r} -> search: {search(t + ' Paris')}")
        elif p["lat"] is None:
            lines.append(f"NOCOORD {r['id']} {p['title']}")
    else:
        q = (r["note"].split(";")[0] or labels[r["id"]]["text"]) + " Paris"
        lines.append(f"BLANK {r['id']} {labels[r['id']]['text']} | q={q!r} -> {search(q)}")

json.dump(cache, open(cache_p, "w"), ensure_ascii=False, indent=1)
open(root / "work/wiki_report.txt", "w").write("\n".join(lines) + "\n")
ok = sum(1 for r in rows if r["wiki_fr"] and not cache["pages"][r["wiki_fr"]].get("missing"))
print(f"{ok} titles found; report: {len(lines)} lines")

"""Build the batches to hand to Gemini for the longer place descriptions (option B).

    ../.venv/bin/python scripts/make_detail_batches.py .

Writes work/detail/batch-NN.json (gitignored), one per ~25 places, each carrying everything the
model is allowed to use: the label as printed, the modern name, the status, the short description
the site already shows, and the French source extract the project collected (`history_fr` in
data/places_*.csv). Nothing else may enter the text — see data/research/DETAIL_BRIEF.md.

Only places whose extract is 200 characters or more are included: below that the extract says no
more than the summary already does, and asking for a longer text invites invention.
"""
import csv, glob, json, sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
MIN_SOURCE = 200
PER_BATCH = 25

ident = {}
for f in sorted(glob.glob(str(root / 'data/places_*.csv'))):
    for r in csv.DictReader(open(f, encoding='utf-8')):
        ident[r['id']] = r

data = json.load(open(root / 'web/public/data/places.json', encoding='utf-8'))
places = [p for p in data['places'] if p['type'] != 'inscription']

jobs = []
for p in places:
    src = (ident.get(p['id'], {}).get('history_fr') or '').strip()
    if len(src) < MIN_SOURCE:
        continue
    jobs.append({
        'id': p['id'],
        'on_the_map': p['old'],
        'today': p['modern'],
        'status': p['status'],
        'type': p['type'],
        'summary_now': p['summary'],
        'source_fr': src,
        'sources': [s['label'] for s in p['sources']],
    })

# group by type so a batch reads as one kind of thing and keeps one voice
jobs.sort(key=lambda j: (j['type'], j['id']))
out = root / 'work/detail'
out.mkdir(parents=True, exist_ok=True)
for old in out.glob('batch-*.json'):
    old.unlink()

n = 0
for i in range(0, len(jobs), PER_BATCH):
    chunk = jobs[i:i + PER_BATCH]
    n += 1
    f = out / f'batch-{n:02d}.json'
    json.dump({'batch': n, 'count': len(chunk), 'places': chunk},
              open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    kinds = sorted({j['type'] for j in chunk})
    print(f'{f.name}: {len(chunk):2} places, {sum(len(j["source_fr"]) for j in chunk):6,} chars of source  ({", ".join(kinds)})')

print(f'\n{len(jobs)} places in {n} batches -> {out}')
print(f'Paste data/research/DETAIL_BRIEF.md and one batch file per conversation.')

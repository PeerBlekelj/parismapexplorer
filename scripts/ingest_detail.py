"""Check and ingest a batch of longer descriptions returned for data/research/DETAIL_BRIEF.md.

    ../.venv/bin/python scripts/ingest_detail.py . work/detail/returned-01.json
    ../.venv/bin/python scripts/ingest_detail.py . work/detail/returned-01.json --write

Reports every failure and ingests nothing unless --write is given and nothing failed. The point of
the checks is that a longer text written from a source can be held to that source mechanically:

  * every `used` span must appear verbatim in that place's source_fr (accents and all);
  * every four-digit year in the text must appear in the source;
  * `added_beyond_source` must be empty;
  * the detail must not restate the summary, and must be inside the length range.

With --write, appends to data/research/details.csv (id,detail), which build_places.py reads.
"""
import csv, difflib, glob, json, re, sys, unicodedata
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
returned = Path(sys.argv[2])
write = '--write' in sys.argv
MIN_WORDS, MAX_WORDS = 40, 200          # the brief asks for 80-160; refuse well outside it

def norm(s):
    """For span matching: collapse whitespace and the typographic variants a model may re-type."""
    s = unicodedata.normalize('NFC', s)
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'),
                 ('–', '-'), ('—', '-'), (' ', ' ')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()

ident = {}
for f in sorted(glob.glob(str(root / 'data/places_*.csv'))):
    for r in csv.DictReader(open(f, encoding='utf-8')):
        ident[r['id']] = r
data = json.load(open(root / 'web/public/data/places.json', encoding='utf-8'))
ps = {p['id']: p for p in data['places']}

try:
    got = json.load(open(returned, encoding='utf-8'))
except json.JSONDecodeError as e:
    sys.exit(f'{returned}: not valid JSON ({e}). The reply must be the array and nothing else.')
if isinstance(got, dict):                     # tolerate {"places": [...]} or {"results": [...]}
    for k in ('places', 'results', 'details', 'data'):
        if isinstance(got.get(k), list):
            got = got[k]
            break
if not isinstance(got, list):
    sys.exit(f'{returned}: expected a JSON array of objects, got {type(got).__name__}')

problems, ok = [], []
seen = set()
for i, r in enumerate(got):
    pid = (r or {}).get('id')
    def bad(msg):
        problems.append(f'{pid or f"item {i}"}: {msg}')
    if not pid or pid not in ps:
        bad('unknown id — it is not a place in this gazetteer')
        continue
    if pid in seen:
        bad('returned twice')
        continue
    seen.add(pid)
    src = norm((ident.get(pid, {}).get('history_fr') or ''))
    detail = r.get('detail_en')
    if detail is None:
        ok.append((pid, None, r.get('notes', '')))
        continue
    if not isinstance(detail, str) or not detail.strip():
        bad('detail_en is neither a string nor null')
        continue
    words = len(detail.split())
    if not MIN_WORDS <= words <= MAX_WORDS:
        bad(f'{words} words, outside {MIN_WORDS}-{MAX_WORDS}')
    extra = r.get('added_beyond_source') or []
    if extra:
        bad(f'{len(extra)} statement(s) not from the source: {extra[0][:90]!r}')
    used = r.get('used') or []
    if not used:
        bad('no `used` spans — nothing can be checked against the source')
    for span in used:
        if not isinstance(span, str) or norm(span) not in src:
            bad(f'span not found verbatim in the source: {str(span)[:80]!r}')
    for year in set(re.findall(r'\b(1[0-9]{3}|20[0-9]{2})\b', detail)):
        if year not in (ident.get(pid, {}).get('history_fr') or '') and year not in (ps[pid]['summary'] or ''):
            bad(f'the year {year} appears in neither the source nor the summary')
    summ = ps[pid]['summary'] or ''
    if summ and difflib.SequenceMatcher(None, norm(summ), norm(detail)).ratio() > 0.6:
        bad('reads as a restatement of the short description')
    if 'http' in detail:
        bad('contains a URL')
    if not any(p.startswith(pid) for p in problems):
        ok.append((pid, detail, r.get('notes', '')))

print(f'{returned.name}: {len(got)} returned, {len(ok)} clean, {len(problems)} problem(s)\n')
for p in problems:
    print('  FAIL', p)
notes = [(i, n) for i, _, n in ok if n]
if notes:
    print('\n  notes from the model:')
    for i, n in notes:
        print(f'    {i}: {n[:150]}')
nulls = [i for i, d, _ in ok if d is None]
if nulls:
    print(f'\n  {len(nulls)} returned null (source too thin): {", ".join(nulls)}')

if problems:
    sys.exit(f'\n{len(problems)} problem(s). Nothing written; send the failures back for another pass.')
if not write:
    print('\nAll clean. Re-run with --write to append to data/research/details.csv.')
    sys.exit(0)

out = root / 'data/research/details.csv'
have = set()
if out.exists():
    have = {r['id'] for r in csv.DictReader(open(out, encoding='utf-8'))}
else:
    with open(out, 'w', encoding='utf-8', newline='') as f:
        csv.DictWriter(f, fieldnames=['id', 'detail'], lineterminator='\n').writeheader()
added = 0
with open(out, 'a', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['id', 'detail'], lineterminator='\n')
    for pid, detail, _ in ok:
        if detail and pid not in have:
            w.writerow({'id': pid, 'detail': detail})
            added += 1
print(f'\nwrote {added} to {out}')

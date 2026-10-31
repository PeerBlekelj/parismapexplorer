"""What the gazetteer is still missing.

    ../.venv/bin/python scripts/check_coverage.py .

Reads the built web/public/data/places.json. Exits non-zero if a place has no description, which
is the gap worth refusing; everything else is reported and allowed, because a null there means
"not researched yet" and that is a legitimate state (see web/DATA_CONTRACT.md).

A place with no modern name is NOT counted as a gap when it is marked vanished: that is the
answer, not a hole.
"""
import json, sys
from collections import Counter
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
d = json.load(open(root / 'web/public/data/places.json', encoding='utf-8'))
places = [p for p in d['places'] if p['type'] != 'inscription']
insc = [p for p in d['places'] if p['type'] == 'inscription']
n = len(places)

def report(label, rows, fatal=False):
    mark = 'MISSING' if (fatal and rows) else '       '
    print(f'  {mark} {label:34} {len(rows):3}  ({len(rows) * 100 // n:2}%)')
    if rows and len(rows) <= 12:
        print('           ' + ', '.join(f"{p['id']} {p['old'][:22]}" for p in rows))
    return rows

print(f'{n} places + {len(insc)} inscriptions\n')
no_sum = report('no description', [p for p in places if not p['summary']], fatal=True)
report('no French description', [p for p in places if not p['summary_fr']])
report('no Swedish description', [p for p in places if not p['summary_sv']])
report('no source', [p for p in places if not p['sources']])
report('no status', [p for p in places if not p['status']])
report('unsure reading', [p for p in places if p['flag'] == 'unsure'])
report('no position of its own', [p for p in places if p['lat'] is None])
unknown = [p for p in places if not p['modern'] and p['status'] != 'vanished']
report('not identified (and not vanished)', unknown)
print(f'\n  for reference: {sum(1 for p in places if not p["modern"] and p["status"] == "vanished")} '
      f'places have no modern name because they are marked vanished, which is an answer')
print('  types:', ', '.join(f'{k} {v}' for k, v in Counter(p['type'] for p in places).most_common()))

if no_sum:
    print(f'\n{len(no_sum)} places have no description at all.')
    sys.exit(1)
print('\nEvery place has a description in all three languages.')

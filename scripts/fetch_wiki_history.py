"""Fetch the HISTORY sections of a French Wikipedia article, for places whose lead says nothing
about the period the map shows.

    ../.venv/bin/python scripts/fetch_wiki_history.py . data/research/sources_long_titles.csv

`history_fr` in data/places_*.csv is the article's **lead** (fetch_wiki.py asks for `exintro`).
For a church or a street the lead is usually the whole story. For a modern commune or an
administrative quarter it is today's population, today's politics and today's buildings, and a
longer description written from it is about the wrong century -- see the nine ids in
data/research/details-held.csv. This fetches the article's history sections instead and writes them
to data/research/sources_long.csv, which make_detail_batches.py and ingest_detail.py prefer over
`history_fr` when it exists.

The input is a small csv of `id,title` naming the article to read for each place. The title is
chosen by hand, because the right article is often not the one already cited: Bercy's card points
at `Quartier de Bercy`, whose history begins in the 19th century, while `Bercy (Seine)` is the
village that the map shows.
"""
import csv, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
titles_p = Path(sys.argv[2]) if len(sys.argv) > 2 else root / 'data/research/sources_long_titles.csv'
UA = 'parismapexplorer/0.1 (https://github.com/PeerBlekelj/parismapexplorer)'
API = 'https://fr.wikipedia.org/w/api.php'
MAX = 7000

# `histo` on purpose: it catches BOTH "Histoire" and "Historique", and an earlier pass that matched
# only "histoire" reported that Bercy and the faubourg Saint-Germain had no history at all.
WANTED = re.compile(r'histo|toponym|moyen|origine|antiquit|chasses|xvi+e|renaissance|ancien r', re.I)
# Sections that are history but not this map's history.
SKIP = re.compile(r'r[eé]volution|empire|restauration|r[eé]publique|contemporain|xix|xx|'
                  r'guerre mondiale|aujourd', re.I)


def get(params):
    params = {**params, 'format': 'json', 'formatversion': '2'}
    req = urllib.request.Request(API + '?' + urllib.parse.urlencode(params),
                                 headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            return json.load(urllib.request.urlopen(req, timeout=30))
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)


def plain(html):
    # Figures and tables first: a caption is a sentence fragment that reads like prose but is not,
    # and a model asked for verbatim spans will happily quote one.
    html = re.sub(r'<(script|style|sup|table|figure)[^>]*>.*?</\1>', ' ', html, flags=re.S | re.I)
    html = re.sub(r'<figcaption[^>]*>.*?</figcaption>', ' ', html, flags=re.S | re.I)
    html = re.sub(r'<div class="thumb.*?</div>\s*</div>', ' ', html, flags=re.S)
    html = re.sub(r'<span class="mw-editsection.*?</span>', ' ', html, flags=re.S)
    html = re.sub(r'<[^>]+>', ' ', html)
    html = html.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&quot;', '"')
    html = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), html)
    html = re.sub(r'\[\s*\d+\s*\]|\[\s*modifier[^\]]*\]', ' ', html)
    # whatever survived of the edit links, in either order
    html = re.sub(r'\|?\s*modifier(\s+le\s+code)?\s*\]?', ' ', html, flags=re.I)
    return re.sub(r'\s+', ' ', html).strip()


rows = list(csv.DictReader(open(titles_p, encoding='utf-8')))
out = []
for r in rows:
    pid, title = r['id'], r['title']
    secs = get({'action': 'parse', 'page': title, 'prop': 'sections'})['parse']['sections']
    keep = [s for s in secs
            if WANTED.search(re.sub(r'<[^>]+>', '', s['line']))
            and not SKIP.search(re.sub(r'<[^>]+>', '', s['line']))]
    text = ''
    used = []
    for s in keep:
        body = plain(get({'action': 'parse', 'page': title, 'prop': 'text',
                          'section': s['index']})['parse']['text'])
        if not body:
            continue
        used.append(re.sub(r'<[^>]+>', '', s['line']))
        text = (text + ' ' + body).strip()
        if len(text) >= MAX:
            text = text[:MAX].rsplit('. ', 1)[0] + '.'
            break
    early = len(re.findall(r'\b1[0-5][0-9]{2}\b|\b(?:X|XI|XII|XIII|XIV|XV|XVI)e si[eè]cle|'
                           r'moyen[- ]âge', text, re.I))
    print(f'{pid} {title[:34]:34} {len(text):5} chars  {early:2} pre-1600 refs  '
          f'[{", ".join(used[:4])}]')
    if not text:
        print(f'   SKIPPED: no history section matched in {title}')
        continue
    out.append({'id': pid, 'title': title,
                'url': 'https://fr.wikipedia.org/wiki/' + urllib.parse.quote(title.replace(' ', '_')),
                'pre1600_refs': early, 'source_fr': text})

dest = root / 'data/research/sources_long.csv'
tmp = dest.with_suffix('.csv.tmp')
with open(tmp, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['id', 'title', 'url', 'pre1600_refs', 'source_fr'],
                       lineterminator='\n')
    w.writeheader()
    w.writerows(out)
tmp.replace(dest)
print(f'\n{len(out)} of {len(rows)} written to {dest}')

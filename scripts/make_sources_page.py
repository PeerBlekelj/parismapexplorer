#!/usr/bin/env python3
"""web/sources/index.html, from data/library/sources-public.json.

    python3 scripts/make_sources_page.py [repo root]

The JSON is written by the library's export_sources.py (metadata only: title, author, date, link, page
count) and is regenerated whenever the library is reindexed, so this page follows the library. Run
this, read the diff, commit and deploy by hand. Plain Python, no dependencies.
"""
import html
import json
import sys
from pathlib import Path

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
data = json.loads((root / "data/library/sources-public.json").read_text(encoding="utf-8"))
e = html.escape

GROUPS = ["The map and other plans", "Guides to the city", "The city's own records", "Trades and printing", "Also in the library"]
QUEUE = {"A": "The city's own records", "B": "Chronicles, laws and guilds", "C": "Topography and urban history"}
QUEUE_ORDER = ["The city's own records", "Chronicles, laws and guilds", "Topography and urban history"]


def where(url: str) -> str:
    h = url.split("/")[2] if "//" in url else ""
    return {"gallica.bnf.fr": "Gallica (BnF)", "archive.org": "Internet Archive"}.get(h, h)


def entry(r: dict, held: bool) -> str:
    bits = [b for b in (r.get("author"), r.get("date")) if b]
    if held and r.get("pages"):
        bits.append(f"{r['pages']} pages")
    title = f'<a href="{e(r["url"])}">{e(r["title"])}</a>' if r.get("url") else e(r["title"])
    where_ = f' <span class="where">{e(where(r["url"]))}</span>' if r.get("url") else ""
    meta = f'<div class="meta">{e(" · ".join(bits))}{where_}</div>' if bits or where_ else ""
    blurb = f"<p>{e(r['blurb'])}</p>" if r.get("blurb") else ""
    return f"<li>{title}{meta}{blurb}</li>"


lib = data["library"]
parts = []
for g in GROUPS:
    rows = [r for r in lib if r["group"] == g]
    if rows:
        parts.append(f'<h3>{e(g)}</h3>\n<ul class="bib">\n' + "\n".join(entry(r, True) for r in rows) + "\n</ul>")
queued = data["queued"]
qparts = []
for g in QUEUE_ORDER:
    rows = [r for r in queued if QUEUE.get(r["category"]) == g]
    if rows:
        qparts.append(f'<h3>{e(g)}</h3>\n<ul class="bib">\n' + "\n".join(entry(r, False) for r in rows) + "\n</ul>")

page = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Sources · Paris 1550</title>
    <meta name="description" content="Everything the Paris 1550 project reads from: the open-source volumes held in its research library, and the ones queued next." />
    <link rel="canonical" href="%SITE%/sources/" />
    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="Paris 1550" />
    <meta property="og:title" content="Sources · Paris 1550" />
    <meta property="og:description" content="The open-source volumes behind the Paris 1550 map, and the ones queued next." />
    <meta property="og:url" content="%SITE%/sources/" />
    <meta property="og:image" content="%SITE%/og/site.jpg" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  </head>
  <body class="doc">
    <header class="doc-head">
      <div class="doc-top">
        <span class="home-links"><a class="back" href="/">← Paris 1550</a> · <a class="back" href="/map/">Open the map</a></span>
      </div>
      <h1>Sources</h1>
      <p class="lede">The books, records and plans this project reads from, in one place. Each place on the map is checked against them, and each link goes to the open copy.</p>
    </header>

    <main class="doc-body">
      <section id="library">
        <h2>In the library <span class="count">{len(lib)}</span></h2>
        <p>These volumes are held in the project's research library, where they can be searched page by page. Only open sources are listed, and only their details: the text stays in the library. The list is rebuilt whenever something is added. The sources cited for individual claims are on the <a href="/#sources">start page</a>.</p>
        {chr(10).join(parts)}
      </section>

      <section id="queued">
        <h2>Next in line <span class="count">{len(queued)}</span></h2>
        <p>Found and checked against their own title pages, not yet in the library.</p>
        {chr(10).join(qparts)}
      </section>

      <section id="help">
        <h2>Know a source we are missing?</h2>
        <p>Further reading, a better copy or a correction is welcome. <a href="/suggest/">Write to us</a>, no account needed.</p>
      </section>
    </main>
    <script type="module" src="/src/method.ts"></script>
  </body>
</html>
'''
out = root / "web/sources/index.html"
out.parent.mkdir(parents=True, exist_ok=True)
tmp = out.with_name("index.html.tmp")
tmp.write_text(page, encoding="utf-8")
tmp.replace(out)
print(f"sources page: {len(lib)} in the library, {len(queued)} queued")

# Contributing

Corrections and additions to Paris 1550 are very welcome — especially from people who know old Paris.

## The quickest way: open an issue

If you spot a wrong identification, a misread label, a misplaced pin or a mistake in a text,
click **Suggest a correction** at the bottom of the place's card on the site. It opens a new
GitHub issue with the place's id, its label as printed, today's name and status, and a link to the
place already filled in; you add what's wrong, the correction and, if you can, a source (book,
article, link, old map). You need a (free) GitHub account.

You can also [open an issue](https://github.com/PeerBlekelj/parismapexplorer/issues/new/choose)
directly, with the place id (e.g. `L0123`, shown in the place card, the table of places and the
page address `/place/L0123/`).

## Editing the data directly

All place data lives in plain CSV files under `data/research/`. Edit them and open a pull request.

| File | What it holds |
|---|---|
| `data/research/streets.csv` | How each street label is identified: `match` is `CUR:<current street name>` (as in the Paris street register), `#<id>` (a record in the register of vanished streets), `DUP:<id>` (duplicate label) or empty (unknown). `status` overrides the automatic standing/renamed decision. |
| `data/research/others.csv` | Churches, colleges, gates, buildings, villages, squares: `wiki_fr` is the French Wikipedia article title; `status` is `standing`, `rebuilt`, `renamed` or `vanished`; `modern` is what is there today; `coords` can force `map` (use the position on the old map) or a `lat,lon`. |
| `data/research/summaries.csv` | The short English text shown for each place. Keep it to 2–4 plain sentences, and only state what a source supports. |
| `data/research/OPEN_QUESTIONS.md` | Labels that are still unidentified or uncertain — the best place to start. |

`data/labels_inventory.csv` lists every label read from the map with its pixel position on the
scan. Ids are permanent: never renumber them.

Every identification should be traceable to a source: the Paris street registers (open data),
Wikipedia, or a printed reference such as Lazare (1844), Hillairet, or Jules Cousin's 1875 index
of this map's names.

## Building it yourself

```sh
scripts/fetch_source.sh                       # the 98 MB scan, public domain
python3 -m venv .venv && .venv/bin/pip install pillow numpy rapidfuzz shapely
# street matching needs the Paris open-data registers in work/ref/ (see scripts/match_streets.py)
.venv/bin/python scripts/resolve_streets.py .
.venv/bin/python scripts/resolve_others.py .
.venv/bin/python scripts/fit_transform.py .   # control points for the overlay
python3 scripts/build_places.py . --auto-gcps # writes web/public/data/*.json
.venv/bin/python scripts/make_old_tiles.py .
.venv/bin/python scripts/make_overlay_tiles.py .
.venv/bin/python scripts/make_og_images.py .       # link-preview images (web/public/og/)
.venv/bin/python scripts/make_method_figures.py .  # figures for the method page
cd web && npm install && npm run dev
```

`npm run build` also writes one page per place (`/place/L0123/`, for link previews), `sitemap.xml`
and `robots.txt`; see `web/vite.config.ts`.

## Licences

By contributing you agree that your contributions to the data and texts are released under
CC BY-SA 4.0, and to the code under MIT.

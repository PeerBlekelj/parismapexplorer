# Paris 1550: plan

A searchable website that pairs the Truschet & Hoyau plan of Paris (c. 1550, the "Basel plan")
with the modern city. Every place named on the old map can be found by its old or modern name,
located on both maps, and read about.

Live preview (noindex until launch): https://parismapexplorer.vercel.app

## Decisions

| Topic | Decision |
|---|---|
| Views | Side-by-side synced **and** overlay (old map bent to fit modern streets, swipe + opacity slider), plus "1550 only" / "today only" |
| Orientation | Default north-up (old map rotated). Toggle "original orientation": old map east-up as printed, modern map rotated to match |
| Layout | Mockup layout 1, "Atlas sidebar": search + filters + results + info card on the left, map on the right. Opacity slider only in overlay mode. A full **table of places** (from mockup 3) as an extra view |
| Scope | **Every** label on the map. The cartouche counts 287 streets and alleys, 104 churches and monasteries, 49 colleges; plus gates, bridges, mansions, fields, mills |
| Vanished places | Shown where they stood, marked as vanished, with a note on what is there now |
| Info cards | Distilled from Wikipedia / Wikidata (and other sources), with attribution |
| Languages | English first; French and Swedish later via a switch |
| Devices | Desktop first, then mobile |
| Contributions | Stage 1: GitHub pull requests to the data files. Stage 2: an in-site "suggest a correction" form with moderation |
| Search engines | Indexed at launch (noindex only on the placeholder) |
| Identity | Public under the alias **Peer Blekelj** (GitHub + Vercel). Never the real name in commits, pages or metadata |

## Source

- Scan: Wikimedia Commons, `File:Map of Paris by Truschet and Hoyau - Basel University Library.jpg`,
  10890 × 7820 px, public domain. Not committed (98 MB); `scripts/fetch_source.sh` downloads it.
- The map is **east-up** (ORIENS at top, OCCIDENS at bottom). North is on the left.

## Architecture

- `web/`: Vite + TypeScript + MapLibre GL. One MapLibre instance per pane, so both can rotate.
  - Old map: deep-zoom raster tiles of the scan, placed in a small pseudo-geographic box
    (pixel space mapped linearly), so rotation and zoom behave like any map.
  - Modern map: OpenFreeMap vector tiles (free, no key), OpenStreetMap data.
  - Overlay: old map warped (thin-plate spline through control points) into Web Mercator tiles.
  - Sync: TPS transform old-pixel ↔ lat/lon, fitted from the control points.
- `data/places.csv` (or YAML per place): the gazetteer. One row per label: id, old text as
  printed, normalised old name, modern name, type, status (standing / rebuilt / renamed /
  vanished), label pixel xy, feature pixel xy, lat/lon, location confidence, sources, notes.
- `data/gcps.csv`: control points (old pixel ↔ lat/lon). Mostly derived from places with exact
  modern locations (surviving churches, bridges, gate sites).
- `scripts/`: Python pipeline (tiling, label-extraction helpers, warping, building JSON for the web).

## Phases

1. **Label inventory**: cut the scan into overlapping tiles, read every label, record text +
   pixel position. Check counts against the cartouche.
2. **Identification**: match each label to a modern place or a documented vanished one. List
   the unsure ones and research each (French Wikipedia, Wikidata, ALPAGE/Vasserot, Lazare's
   *Dictionnaire des rues*, Hillairet).
3. **Control points + warp**: build the GCP set, fit the TPS, produce overlay tiles, check
   residuals.
4. **Info cards**: distil short English texts with sources.
5. **App**: layout 1 with all four views, search (accent-insensitive, fuzzy, old + modern
   names, variants), filters, deep links (`#place=...`).
6. **Launch**: drop noindex, README for contributors, CONTRIBUTING.md.
7. Later: FR/SV, mobile layout, suggestion form.

## Status (2026-10-26)

- Phases 1–5 done in a first version: 453 labels read, identified and described; 40 control
  points (drawn buildings + bridge ends), TPS overlay ~64 m median error; the app is live as a
  preview. 29 open items in `data/research/OPEN_QUESTIONS.md`.
- Deploy: local prebuilt build (tiles are not in git), see the memory notes / deploy commands.
- Next: the user's review of the preview; launch (drop noindex, link previews); Cousin's 1875
  index to check labels; more control points towards the edges; mobile layout; FR/SV.

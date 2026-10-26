# Log

Newest first. What was done, what was found, what is open.

## 2026-10-26 — launch + the method page

**Done**
- **Launched** (owner's go-ahead): noindex dropped; `robots.txt` + `sitemap.xml` (455 urls).
- **Place pages for link previews:** `npm run build` writes `/place/<id>/index.html` for all 453
  places (copies of the app's `index.html` with the `page-meta` block swapped; `web/vite.config.ts`).
  Each has its own title, description and `og:image` = a 800×420 crop of the woodcut round the
  label with a red ellipse (`scripts/make_og_images.py` → `web/public/og/`, gitignored, 35 MB;
  site card `og/site.jpg`). The app now reads the place from the path and writes `/place/<id>/`
  on selection; `#place=` links still open. Tab title follows the selection.
- **Method page** `/method/` ("How the map was bent"), linked from the sidebar footer and README.
  Four SVG figures from `scripts/make_method_figures.py` (`web/public/figures/`, committed):
  orientation, control points coloured by LOO error with the overlay edge, affine vs spline
  error arrows, and the sheet's grid after one stretch vs after the spline.
- Verified live: pages 200, `og:image` per place, app opens the place from the path, no errors.

**Findings (numbers now on the page)**
- Closest rotation: the top of the sheet points to 115°. The best affine is sheared: the sheet's
  right angles are 77° on the ground; 0.36 m/px across vs 0.44 m/px up the sheet.
- LOO: affine median 76 / p90 228 / worst 440 m; spline 64 / 155 / 427 m.
- Control points: 21 drawn buildings, 8 bridge ends, 11 at labels.

**Open / for the owner**
- The method page says the labels were "read tile by tile"; it doesn't mention that an AI model
  did the reading. Owner to decide whether to say so.
- Cousin 1875 (item 4 below) not started.

## NEXT SESSION — start here (owner's answers, 2026-10-26)

1. **Review:** "looks good for now". No changes requested to the preview.
2. **Launch: YES to indexing and YES to link previews.** Drop `noindex` from `web/index.html`, add
   `robots.txt` + `sitemap.xml`, an Open Graph / Twitter card (title, description, a share image cut from the
   map), and ideally per-place previews for `#place=` links. A hash isn't sent to the server, so per-place cards
   need a path form such as `/place/L0123` (see how ReadLater does OG previews with Vercel edge middleware).
   Grep the build for the real name before deploying.
3. **Vercel team slug** (`pelle-bjerke-s-projects`): the owner will look into it later. Do nothing.
4. **Cousin 1875:** the whole volume is in the owner's Google Drive, Claude folder:
   `Mémoires_de_la_Société_de_[...]Société_de_bpt6k6310467r.pdf`, 78 MB, Drive file id
   `1Zzn05jN2UiuI0cGC5sGuL_raEgG0ExI9`. The index of the map's names is pp. 58–70 (Gallica f66 on); Cousin's
   notice on the map starts around f52. Use it to settle `data/research/OPEN_QUESTIONS.md` and check the label list.
5. **NEW REQUEST: a page on the site explaining how the map was bent**, i.e. the method. Cover:
   - why a bird's-eye view can't be laid on a map with one stretch, and the ~115° rotation;
   - how the labels were read and identified (sources);
   - control points (drawn buildings, bridge ends), the thin-plate spline, the leave-one-out error (64 m
     median, 155 m p90) and why the edges are worse;
   - mistakes caught (Charenton, homonyms, old spellings);
   - figures: the control-point map, an error map, affine vs spline;
   - honest limits; credits and sources.
   Link it from the app (sidebar footer) and the README, and keep it in the site's style.

## 2026-10-25 → 26 — first session: from idea to live preview

**Done**
- Decisions taken with the owner (see PLAN.md): layout 1 "Atlas sidebar" + a table of places;
  side by side + overlay (opacity slider only in overlay); north-up with an "original orientation"
  toggle; every label; texts from Wikipedia-type sources; English first (FR/SV later); desktop
  first; contributions via GitHub first, an in-site form later; public under the alias Peer
  Blekelj; indexed at launch.
- Source: the Basel scan on Wikimedia Commons, 10890 × 7820 px, public domain. Printed east-up
  (the fitted "up" is actually ESE, ~115°).
- Label inventory: 88 gridded tiles read, then a 2× zoom pass on the dense areas with
  recorded labels marked → 468 labels (`data/labels_inventory.csv`), 453 places after removing
  duplicates and decoration. Ids are permanent.
- Identification: streets against the Ville de Paris registers of current and vanished street
  names; everything else against French Wikipedia (titles verified by script) and Wikidata.
  Result: 138 standing, 19 rebuilt, 77 renamed/absorbed, 212 vanished, 7 unresolved;
  29 open or low-confidence items in `data/research/OPEN_QUESTIONS.md`.
- English summaries for 422 places (`data/research/summaries.csv`).
- Overlay: thin-plate spline (λ 0.2) through 40 control points — 21 drawn buildings + 8 bridge
  ends from OSM + hand-picked landmarks. Leave-one-out error: median 64 m, p90 155 m.
  Warped tiles z11–17 (`scripts/make_overlay_tiles.py`).
- App (Vite + TS + MapLibre): synced maps, warped overlay with swipe/opacity, four modes, both
  orientations, tolerant search, info cards, table of places, `#place=` deep links, UI strings in
  `i18n.ts`. Live preview (noindex): https://parismapexplorer.vercel.app — deployed as a local
  prebuilt build because the tiles are not in git.
- README and CONTRIBUTING written.

**Findings**
- The cartouche counts 287 streets, 104 churches, 49 colleges; the map labels fewer (221 streets,
  ~91 churches, 33 colleges read even at 2× zoom) — many features are drawn but unnamed.
- Several labels were added by hand on the Basel copy (Sainte-Chapelle, rue Poupée, rue Percée,
  rue de la Serpente, rue des Deux-Portes).
- Printer's slips and corruptions: "HOSTRE DAME" (N cut as H), "rue de la Verrerie" for the
  Vieille-Draperie (as on Ducerceau 1555), "R. des Ras" = rue d'Arras, "Bribouche" = Aubry-le-
  Boucher, "Cochonnerie" = Cossonnerie, "Lostel de Tournai" = the Collège de Tournai. The Paris
  street register itself cites this map ("rue Bouquetonne (Truschet)").
- 1550 shorelines lie further out than today's quays (e.g. the quai de Gesvres was built in 1642),
  so the overlay's river edges don't — and shouldn't — match modern ones exactly.
- Pitfalls hit: Wikipedia homonyms (Popincourt → a commune in Oise 92 km away; now a hard stop
  for positions outside the map area); 16th-century spellings fooling the standing/renamed test
  (fixed with spelling normalisation + manual overrides); a lone control point far out
  (Charenton) wrecking the spline (dropped: p90 463 → 172 m); village anchors making the centre
  worse (left out); Python's csv writer emitting CRLF.

**Open**
- Owner's review of the preview; go-ahead to launch (drop noindex, link previews).
- Jules Cousin's 1875 index of the map's names (Gallica blocks scripted download) to settle the
  open items and check the label list.
- More control points towards the edges; mobile layout; French and Swedish; in-site suggestion
  form.
- The Vercel team slug contains the owner's real name (deployment-specific URLs only; they are
  login-protected; the production alias and pages are clean).

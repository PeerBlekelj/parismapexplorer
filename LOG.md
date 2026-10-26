# Log

Newest first. What was done, what was found, what is open.

## 2026-10-26 (evening) — FR/SV pages, texts on the map, start-over link: live; intro = suggestion

- Merged + deployed: `i18n-pages` (FR/SV place + home + method pages, hreflang, app follows /fr/ /sv/
  paths; UI strings moved to `web/src/strings.ts`, shared with the build), `texts` (/texts/ in
  en/fr/sv: the 108-line poem + the publishers' notice, transcription checked by the cloud session,
  16 fixes; full-res JPGs under /texts/full/), and from `intro` only commit 81eb0ff (the title =
  "Back to the start"; cherry-picked as 3bf7d72). Fixes during the merge: creditTexts/brandHome into
  strings.ts, footer links via langBase(), start-over keeps the language path (/fr/), texts/ in the
  sitemap paths, hreflang links inside the texts pages.
- Flying between places now always zooms out ≥1 level (flightPlan in maps.ts).
- Seen once: 8 "source image could not be decoded" console errors only during the start-over
  flight (MapLibre cancelling tile loads mid-zoom). Not reproduced in normal use.
- Owner decisions pending from the cloud summaries: a FR/SV browser on an English link is moved
  to /fr/ or /sv/ (shipped; owner may prefer unprefixed = always English); native-speaker read of
  the FR/SV method page; the texts' sources (Hofmann, Lepape, fr.wikipedia) were seen only via
  search extracts.
- `intro` branch (NOT merged): /about/ page (~2,350 words, 13 sources; Cousin's 1875 notice is in
  `data/research/cousin_1875_notice.txt`), footer link, first-visit welcome card (flag
  WELCOME_CARD in web/src/welcome.ts). I cut the 6 images from the scan (a862f12). Screenshots in
  mockups/intro/ on that branch. Waiting for the owner's verdict.
- ⚠ Never `pkill -f "...port..."` from a Bash call: it matches its own command line and kills it.

## 2026-10-26 (afternoon) — GitHub unlinked from Vercel; six edge control points

- Owner said yes: `vercel git disconnect` done. Deploys only from the mini (prebuilt).
- Edge control points from the cloud session's 15 candidates (`data/research/gcp_candidates.md`):
  today's positions from the junction of the two streets' areas in the Paris register
  (`work/corners.json`), the pixel from the drawn junction on the scan. Rejected on sight: C01
  (rue de la Cerisaie is drawn at right angles, Cousin), C08 (Porte Saint-Jacques sits on a sheet
  seam), C10/C11/C15 (the drawn junction isn't identifiable: the Saint-Germain fields are schematic;
  the Saint-Honoré grid near the Louvre is the engraver's shuffled block). Tried and dropped by the
  fit: G103 Sévigné×Francs-Bourgeois, G107 Coquillière×Coq-Héron, G108 Saint-Denis×Saint-Sauveur
  (each 120–220 m off and dragging neighbours; Saint-Laurent went 49→273 m with them).
  KEPT (G101, G102, G104, G105, G106 Tour de Nesle, G109) in `data/gcps_refined.csv`.
- Result, 46 points: LOO median 64→61 m, p90 155→136 m, worst 427→195 m. Saint-Médard 416→25 m,
  Bastille 427→190 m. Overlay tiles regenerated, method page + figures + README updated.

## 2026-10-26 (13:15) — all four cloud branches merged; live at paris1550.vercel.app

- The owner picked in the cloud sessions directly: favicon **A** ("15" over "50") and phone layout
  **A** (bottom sheet, stacked "Both" by default, compact cards for the table). Merged in order
  rename → corrections-research → i18n-fr-sv → mobile; conflicts only in i18n.ts/card.ts (added the
  FR/SV strings the other branches lacked: correction link, phone short labels).
- Research: L0007 Pont Arcans (bridge over the Grand Égout, ~rue de Provence × Chaussée-d'Antin) and
  L0421 rue Breneuse = rue Verdelet (#662) settled → **1 open question** (L0224). The session's
  quotes came from search extracts; `data/research/open_questions_research.md` flags them for checking.
  Edge control-point candidates in `data/research/gcp_candidates.md`: NOT yet checked on the scan.
- **New address https://paris1550.vercel.app**; the old address 308-redirects path-for-path (set as a
  Vercel project-domain redirect via the API; the host-conditioned redirect in web/vercel.json did
  not fire because the CDN served the old domain from cache; keep it anyway, harmless).
- ⚠ The Vercel project IS connected to GitHub: every push made a Vercel build (all failed: no
  tiles). A successful one would replace the live site with a tile-less one. Added
  `"git": {"deploymentEnabled": false}` in both vercel.json files (root = where git builds look).
  Disconnecting outright (`vercel git disconnect`) was refused by the safety check: owner's call.
- Known gaps: transcription notes, source labels, the per-place pages and the method page are
  English only; place pages in /fr/ /sv/ = owner to decide.

## 2026-10-26 (midday) — name chosen; work fanned out to cloud sessions

- **Name: "Paris 1550"** (owner). `paris1550.vercel.app` answered 404 = probably free; the domain move
  waits until the rename is merged (keep the old URL working, then switch canonical/sitemap).
- Owner: "hand over as much as possible to cloud". Four cloud sessions, each on its own branch, no
  merge/PR/deploy, told NOT to edit LOG.md (notes come in their final summaries):
  - `rename-paris-1550` (session_018QqnWXdEF3oW36FYV9yZHs): rename everywhere except URLs; favicon
    options in `mockups/favicons-1550/` with preview.png for the owner to view on GitHub.
  - `mobile` (session_01MPeK8UethfUobKsy54B5LS): 3 phone mockups in `mockups/mobile/`, then builds its pick
    behind a media query; owner to choose.
  - `i18n-fr-sv` (session_01PFTteGnqxqaJ2qRjHWxzod): FR/SV UI, language switch, all summaries translated.
  - `corrections-research` (session_019NbwEZ9EeMqc1U45jTQ5uW): "Suggest a correction" → prefilled GitHub
    issue form; research on the 3 open questions; edge control-point candidates.
- Merge order planned: rename → corrections → i18n → mobile (expect conflicts in i18n.ts, card.ts).
- The layout-A session (session_01PXG9oTDuoQGTs7niy7sh7R) is done and merged.

## 2026-10-26 (branch `layout-a`) — sidebar layout A, drill-in

**Done** (not merged, not deployed: for review on the machine with the tiles)
- **Compact header:** the title is on one line (18 px) with a 9 px subtitle under it, then one row:
  search, with "Filters ▾" at its right end, and the Map / Table toggle. The header is now 100 px
  (was ~350 px). The type chips, "All" and "Unsure reading" moved into a dropdown under the row;
  same state and behaviour. The button reads "Filters · N" in red when N filters are on. The
  dropdown closes on an outside click, on Esc or on the button.
- **Drill-in:** with a place selected, the count and list are hidden and the card fills the
  sidebar between header and credits (736 px of 900), scrolling on its own. "← Back to N places"
  at the top (N = current results), the × and Esc all return to the list at its old scroll
  position with the place highlighted (scrolled into view if it was picked on the map or a link).
- Typing a search, or changing a filter, while a card is open returns to the list with the new
  results. Enter in search still opens the first result.
- Search placeholder shortened to "Search…" (the field is ~90 px wide now); the full "Search old
  or modern names" is its title and aria-label.
- Files: `web/index.html`, `web/src/main.ts`, `web/src/card.ts`, `web/src/i18n.ts`, `web/src/style.css`.

**Verified** with `npm run build` and in Chromium (Playwright, 1600×900, no tiles in that
checkout, OpenFreeMap blocked by the sandbox network): `/place/L0029/` opens in the card (card
114–835 px, list hidden); Back, × and Esc return to the list (scroll 2000 → 2000, row
highlighted, URL back to `/`); selecting from the list, table, a map pick (via the `onPick`
callback) and `#place=L0029` all open the card; Filters → Bridges shows "Filters · 1", 7 results,
Back reads "Back to 7 places". No console errors apart from the missing tiles and the blocked
style. At 420 px wide nothing scrolls sideways.

**Open**
- Not checked with real tiles or real map clicks; a map label click was simulated through the
  callback.
- The subtitle at 9 px is small; on a font fallback it may wrap to two lines (it is allowed to).
- The "Search…" placeholder no longer hints at old vs modern names; the owner may prefer a
  narrower Map/Table toggle instead.
## 2026-10-26 (afternoon) — Cousin 1875 checked; layout A sent to a cloud session

**Cousin's table, done.** PDF on the mini (`source/cousin-1875-…pdf`, gitignored). It has an OCR layer, but
the table (printed pp. 60–70 = PDF pp. 70–80; Gallica page = printed + 8) was transcribed from the page
images: 480 entries in `data/research/cousin_1875_table.txt` (name | printed form | sheet,square | note).
- **His grid:** 8 sheets, 4 across × 2 down, I–IV on the top row of the scan, each split 3×3, squares
  numbered row by row. Fitted by brute force over sheet orders: 285/313 clear matches in the exact square.
- `scripts/cousin_match.py` pairs labels with entries (names + square); weak pairs reviewed by hand
  (`OVERRIDE`/`DROP` in the script) → `data/research/cousin.csv`, 424 labels. `build_places.py` now
  cites "Cousin 1875, p. N" (linked to Gallica) on each, and adds his corrected name as a searchable
  variant (e.g. "Hôtel de Fécamp" finds "Lostel de Tes").
- **Open questions 29 → 3** (L0007 Pont Arcans, L0224 a rue Neuve, L0421 rue Breneuse: he lists them only).
- **Corrections:** the engraver's chain of shifted names around the rue des Poulies (9 labels, L0413…
  L0435, now each on its real street); L0244 Paiens = rue des Juifs; L0391 Chats = Déchargeurs; L0398
  Battoir = Gît-le-Cœur; L0339 Pavée = rue Palée/Petit-Hurleur; L0294 = Renard-St-Merri; L0295 Courrerie
  = rue de la Verrerie; L0315 Platrière = the Corroierie; L0232 = rue des Lions; L0352, L0393, L0417,
  L0266, L0311. Collège d'Harcourt moved from L0151 to L0199 (L0151 = hôtel d'Harcourt).
- **Misreadings fixed:** L0311 VENERIE → POTERIE (damaged paper), L0159 → LECOLLE S. GERMAIN (l'École
  Saint-Germain, not a college; type other), L0199 → C. HERRO COUPT, L0203 → LE PRESOER DE LOTEL DIEU
  (a wine press, not a meadow), L0250 → R. GARNIER SVR IAN.
- **Two missed labels added:** L0469 HU LEU (rue du Grand-Hurleur), L0470 R. DEI SON (rue Tiron).
- Totals now: 470 labels, 455 places; 143 standing, 19 rebuilt, 76 renamed, 215 vanished, 2 unknown.
  Method page, README and open-questions footer updated.
- ⚠ `labels_inventory.csv`, `places_*.csv` are CRLF in git; `research/*.csv` LF; `summaries.csv`
  quotes every field. Keep that when rewriting them, or the diff is the whole file.

**Layout A** delegated to a cloud session (`session_01PXG9oTDuoQGTs7niy7sh7R`, branch `layout-a`, no
deploy, no PR). Review + merge + deploy from the mini (it has the tiles).

**Naming:** the owner wants a less generic name than "Paris Map Explorer"; suggestions given, waiting.
Favicons wait for the name.

## 2026-10-26 (later) — owner's feedback round

- Owner: **state that it was built with Claude Code** → DONE and live: section "How this was built"
  (`/method/#built`), the sidebar credit ("by Peer Blekelj, built with Claude Code") and the README.
- **Favicon:** the blue bolt is Vite's default. Four options drawn in `mockups/favicons/`
  (A serif P + red ring, B the ship of Paris shield, C Seine + ringed Cité, D Notre-Dame cut from
  the woodcut); sheet `favicon-options.png`. Waiting for the owner's pick.
- **Sidebar real estate:** the header (brand, tabs, search, 9 chips) eats ~350 px, so a selected
  place's card is squeezed at the bottom. Four layouts mocked over a real screenshot in
  `mockups/layout2/`: A drill-in (card replaces the list, ← Back, filters in a menu), B pop-up on
  the map, C card column between list and map, D card on top of the list. Recommended A. Waiting.
  All images for review together in `mockups/review/index.html` (not in git).
- **Cousin 1875: BLOCKED.** No Drive mount on the mini; the Drive connector returns an empty text
  layer for the PDF (scanned pages) and a base64 download of 78 MB is too big; Gallica answers
  403 to scripts (and a headless browser try was refused by the safety check — don't retry it).
  Needs the owner to copy the PDF (or just pp. 58–70) onto the mini.
  → **UNBLOCKED 2026-10-26 08:09:** owner scp'd it from p-ubuntu. Now at
  `source/cousin-1875-memoires-shp-bpt6k6310467r.pdf` (gitignored, 78,490,054 bytes, 302 pages,
  PDF 1.4, `%%EOF` present). Not read yet.

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

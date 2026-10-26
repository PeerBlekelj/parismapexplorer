# Log

Newest first. What was done, what was found, what is open.

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

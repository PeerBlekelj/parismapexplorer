# Log

Newest first. What was done, what was found, what is open.

## 2026-10-30 (19:10) — starred places and sharing, on branch `starred-places`

**Built, not deployed.** A visitor can keep their own list of places and send a place, a view or the
whole list to someone else — or to their own phone. The site stays static: no server, no accounts, no
cookies. A star lives in `localStorage` (guarded, as `lang` is) and a **link** is the only thing that
travels. Mockups and the reasoning: `mockups/favorites/` (four sheets + README).

What is there:
- **Star a place** from its card (☆ Star / ★ Starred) or from any row in the list. On a touch screen
  the row star is always visible — there is no hover to reveal it with.
- **The list**: `★ n starred` appears in the count line as soon as there is one, and as a chip in the
  Filters menu (owner's call: A + B, not a button in the top row, which has no width to spare on a
  phone). It filters the list and both maps through the `setFilter()` path that already existed.
  Starred places keep a gold ring at every zoom, where the catalogue's red dots fade out.
- **Share one place**: a button that copies `/place/L0006/` — which already had its own page, title
  and link-preview image in three languages — or opens the system share sheet on a phone.
- **Share a view**: `?m=overlay&c=48.8529,2.3463&z=15.4&o=62&s=50`, the thing that had no link at all
  before. Every part optional, so an older link still opens.
- **Share the list**: `?stars=…`, and **Open on another device**, which draws the same string as a QR
  code. Opening such a link shows the places with a banner — *add them* or *just look*. It **merges,
  never replaces**, so following a link twice changes nothing and nobody's list is overwritten.
- `?stars=` indexes by the **id number** (`L0017` → 17), never by a row's position in `places.json`,
  which shifts whenever a place is added. Two forms, whichever is shorter: the numbers written out, or
  a base64url bitmap with trailing zero bytes trimmed (22 characters for seven places, 79 for all 457).
  **The ids must therefore never be reused for a different place.**

**Two bugs the checks caught, worth remembering:**
1. Wrapping a zoom `interpolate` inside a `case` to make starred dots bigger made MapLibre reject the
   whole paint property and **never add the `dots` layer at all** — every place dot gone, reported only
   to the console. The per-place choice has to go inside each stop of the ramp (`starRamp` in maps.ts).
   The run passed until console errors were made to count as failures: a `pageerror` listener does not
   see this.
2. The row star was `visibility: hidden` until hover, which on a phone means unreachable. Now
   `@media (hover: none)` shows it always.

**Checking it**: `scripts/check_stars.py <base-url>` walks the whole thing in a real browser (39
assertions) and leaves screenshots in `work/stars-check/`. Run it against **both** the dev server and
`npm run preview`: the QR generator (`qrcode-generator`, the one new dependency) is a bundler question,
and `/fr/map/` and `/sv/map/` only exist in a build. Both green here.

**Open:**
- Not deployed and not merged — waiting on the owner's look.
- The French and Swedish wordings are drafted, not reviewed, like the rest of the translations.
- A `?stars=` or view link gets the generic site link-preview card: a query string never reaches a
  static file, so a custom one would need a serverless OG function — the first runtime on a site with
  none. Left out deliberately.
- No GPX export and no free-dropped pins (both the owner's call: only the 457 catalogued places).
- The starred list shows in the catalogue's order, not the order they were starred.

## 2026-10-30 (10:30) — 73 claims checked; three corrections live; the poem question answered

**The verification branch is merged and deployed** (main b102e3f). A cloud session opened and read the
sources behind the claims that had only ever been seen as search extracts: **73 claims — 57 confirmed,
9 partly, 4 contradicted, 3 unverified** (`data/research/quote_verification.md`). It stayed inside
`data/research/`, so the site edits below were made here.

**The four contradicted:**
1. **The Senat brochure quotation does not exist.** `corrozet.md` attributed to it a sentence about
   Corrozet patronising the plan's edition. All 12 pages carry a text layer and contain no "plan de
   Bale", no "patronne", no "annexe". Kept in the notes WITH the contradiction recorded, on the owner's
   call — a deleted bad citation gets re-added by the next person who finds the same extract. Not cited
   on the site.
2. **fr.wikipedia's 1553 sentence is not unsourced.** It carries two notes, one naming "Gilles
   Corrozet, editeur" outright, and cites Vergneault-Belmont 2008 p. 168. The site said "we have found
   no source for it". **Corrected in en/fr/sv** — it now names the study and says it is modern, not a
   document of the time.
3. Lazare's "actes de 1290, 1330, 1352 et 1406" are his **Verderet** entry, a different street 400 m
   from **Verdelet**.
4. Mathoniere was installed at the Corne de Daim in **1557**, not 1577 (fr.wikipedia's date is
   internally impossible — it also has him dying in 1572).

**Two more site corrections, deployed:**
- The poem is at **pp. 64-67** of Lacroix 1874, not 64-68; p. 68 opens the Epigramme and the Blason,
  which the texts page does not transcribe. Confirmed from a SECOND copy (Internet Archive
  `lafleurdesantiqu00corr`, whose OCR keeps the running heads), its edition checked on its own title page.
- **Truschet died about 1561-1564** (Lepape), not "by 1575". The 1575 date came from the archbishop's
  censier still carrying his name, which Grivel reads as an error. The page now says both.

**Two traps worth keeping:** fr.wikipedia's *Rue Verderet* article **conflates two Lazare entries**, so
do NOT "correct" L0421 to match it — Lazare and the Archives nationales support what we have. And
*History of Cartography* **disagrees with itself**: ch. 48 (Pelletier) dates the map 1550, ch. 53
(Hofmann) ca. 1553. Never cite "HOC" for a date without the chapter.

**The standing question is answered: the 1550 *Antiquitez* does NOT print the poem.** Vision OCR (458
of 459 pages, $0.69) took it from 2 pages of text to 439. The *Louenges de Paris* is absent — *propices*,
*gentillesse*, *singularite*, *instaurateur*, *descripture*, *exquise* all return nothing — as are the
acrostic and the Epigramme. The book prints only the **Blason des armes**, front matter, scan p. 21,
ending PLVS QVE MOINS. So the 14-gates/120-councillors question does not arise, and the updated figures
appear in neither book: not in the 1532 *Fleur* (old numbers), not here (no poem). **The updating was
done for the map.** Full note: `data/research/library_verification.md`.

Checked live after the deploy: 9 routes 200, all three corrections present in en/fr/sv, old wording gone.

## 2026-10-30 (09:00) — Cousin corrected on the live site; the 1550 Antiquitez is in the library

- **The about page overstated its own source.** It said "around 1572 the image-maker Nicolas Prevost
  printed there", cited to Cousin. Cousin 1875 (scan p. 61) says: "La maison du Chef Saint-Denis, sans
  doute liquidee apres la mort de Truschet, appartient alors a Nicolas Prevost." Ownership, not
  printing. Corrected in en/fr/sv and DEPLOYED (main 737923d, prebuilt, `--archive=tgz`); checked live
  on all three, old wording gone. Cousin's "toute une colonie d'imagiers" supports the other half of
  the sentence, so that stayed. Found by the cloud session, verified here against the library.
- **A flagged citation turned out to be right.** `web/texts/index.html` cites the poem in Lacroix 1874
  at pp. 64-68; this log said 102-106. Rendered the page: printed page number 64, running head LES
  ANTIQUITEZ. The site is right, 102-106 are Gallica VIEWER pages, offset 38. Cite printed pages.
- **The 1550 first edition of the Antiquitez is in the library** (ark bpt6k1527257k, 459 pages),
  confirmed from its own title page, not the catalogue: "LES ANTIQVITEZ ... 1550. A PARIS, Au Palais,
  en la boutique de Gilles Corrozet." Two things follow: Corrozet's shop at the Palais is now on a
  primary source (and is NOT the rue Montorgueil shop the open question is about); and the book is
  dedicated to "Claude Guiot ... preuost des marchans de la ville de Paris", the same man the
  Registres t. 3 show being sent to the King in Dec 1549 and reporting back 13 Jan 1550.
- The poem question is still open: the scan is image-only, so Vision OCR is running (459 pages, $0.69).
  The earlier "ends at FIN, no poem" was against the **1561** edition.
- Notes in `data/research/library_verification.md` — deliberately a new file, because the cloud session
  is editing `print_shop.md` and `corrozet.md` on `verify-research-quotes` at the same time.
- Open: "by 1575 Truschet was dead" (cited to [9], not Cousin) is still unverified; the cloud session
  is checking it. Cousin only infers Truschet's death, hedged with "sans doute", from the signatures
  vanishing by about 1572.

## 2026-10-29 (13:20) — the ten coordinates are live

- Merged `wrong-site-coordinates` into main (merge 61a73aa) and deployed. The 28 Oct fix had been
  pushed but never merged, so the live map still carried the ten wrong pins for a day.
- The LOG.md conflict was the badge entry against the coordinates entry; both kept, newest first.
- Verified the data build is reproducible before deploying: `build_places.py . --auto-gcps` on the
  merged tree reproduces the committed `places.json` and `gcps.json` byte for byte apart from the
  `generated` timestamp. 457 places, 46 gcps.
- Deployed prebuilt with `--archive=tgz` from the main checkout (so `web/public/og/`, 458 images, and
  `web/public/tiles/`, 49 MB, were both present). Production Ready.
- Checked live: `/` `/fr/` `/sv/` `/map/` `/fr/map/` `/place/L0017/` `/method/` `/texts/` 200;
  `/data/places.json`, `/sitemap.xml` (1383 urls), `/og/L0017.jpg`, `/tiles/old/7/64/64.webp`,
  `/tiles/overlay/15/16598/11271.webp` 200; the old domain still 308s path-for-path. The badge is in
  the HTML of the written pages and injected by `main.ts` on the map pages, as designed.
- Live coordinates confirmed moved: L0017 Petit Chatelet 48.852874, 2.346347; L0025 La Monnoie
  48.860307, 2.344764; L0080 Hostel Dieu 48.852981, 2.347932.

## 2026-10-29 (07:15) — the Simple Analytics badge; deployed main

- Simple Analytics' free plan requires a visible badge from 2026-11-01 (mail of 10-27): no badge means
  a reminder, then 14 days, then the dashboard is locked — the collected data is kept. Owner's call:
  tune the badge to each site's palette rather than take the stock grey one.
- `web/src/badge.ts` holds the markup in one place (`background`/`text`/`logo` query params = paper,
  sepia ink, the site's red). The written pages get it from the same vite plugin that injects the
  analytics script, under the colophon that ends the last section (`withBadge`, keyed on
  `<body class="doc">`); the map and place pages get it from `main.ts`, at the end of the sidebar
  credits. 9 static pages carry it in the HTML, which is what their detector reads.
- Deployed main 684cb07 (prebuilt, `--archive=tgz`). Checked live: `/` `/fr/` `/sv/` `/map/` `/fr/map/`
  `/place/L0017/` `/method/` `/texts/` 200, og images, tiles, sitemap, data, and the old-domain 308.
- The deploy must run from a tree that has `web/public/og/` and `web/public/tiles/` — both gitignored,
  so a fresh clone or worktree builds a site without OG images and without the 1550 tiles. They were
  hard-linked in from the main checkout for this one.
- The owner's `wrong-site-coordinates` work is NOT in this deploy; main had only the badge commit.

## 2026-10-28 (20:36) — ten coordinates pointed at the wrong site

- Owner asked whether "S. GERMAIN DE LOCERRAS" (L0120) -> Saint-Germain-l'Auxerrois is an error. It is
  not. The scan really reads that (a period spelling of l'Aucerrois, from Auxerre); the drawing is the
  church, and R. S. GERMAIN, LE COLLEGE S. GERMAIN and LA MONNOIE all sit around it. The pin looked off
  because the old-map marker sits on the label pixel (model.ts `oldLL`), which is below the building.
- Measured, for all 457: the TPS georef of the label pixel vs the stored coordinate. Inside the
  control-point hull, median 58 m against the transform's own leave-one-out error of 61 m - i.e. at the
  noise floor, no general accuracy problem. Outside the hull, median 205 m and up to 6 km: the outlying
  villages are drawn crammed into the margins and every control point is inside the city. That is the
  map, not the data. work/drift_map.png shows it.
- Ten places carried a Wikipedia/Wikidata coordinate describing a *different* site. `coords=map` in
  data/research/others.csv + re-ran resolve_others.py: L0017 PETIT CHATELET (had the Grand Chatelet's
  point, 519 m), L0025 LA MONNOIE (the quai de Conti building the mint moved to in 1775, 450 m),
  L0080 LOSTEL DIEU (the 1867 building north of the parvis, 199 m), L0084 LES CARMES, L0106 S. MICHEL,
  L0121 LES AUGUSTINS (459 m), L0461 LES FAUBOURS S. GERMAIN (a rounded district centroid, 2.32000,
  marked `exact`), and L0092 / L0095 / L0096 - the cimetiere de la Trinite, Saint-Magloire and the
  Saint-Sepulcre, which all three carry the SAME coordinate (48.864461, 2.350194) on fr.wikipedia.
- Rule, on the owner's word: a place that moved points at its 1550 site, not its later home. Checked all
  50 relocation-flavoured entries; only L0025 and L0080 needed moving. The rest (Quinze-Vingts,
  Cordelieres, Saint-Antoine, Nesle...) already pointed at the old site.
- Result: worst in-hull drift 1316 m -> 355 m, p90 145 -> 127 m. No two unrelated places share a
  coordinate any more (the two remaining pairs are the hotel de Nesle + its tower, and Saint-Jean + its
  own cemetery, both genuinely co-located). All ten are `approx` now, which is honest.
- build_places.py: the transcription pass's "dup" marker ("already recorded in the previous tile";
  `seen_in` carries the same fact) was surfacing as the card's Transcription line on 9 places. Filtered
  in the build (`inv_note`); labels_inventory.csv untouched. gcps.json diff is the timestamp only -
  none of the ten was a control point, so the georeference is unchanged.
- Open: resolve_others.py positions `coords=map` places with an *affine* fit while the app uses the TPS,
  so those ten sit 24-143 m from where the app's own transform would put them. Harmless at `approx`,
  but the two should use one transform.

## 2026-10-26 (23:00) — English by default

- Owner: default to English regardless of browser language — the Swedish translation is too weak for now.
  `detectLang()` in web/src/i18n.ts no longer reads navigator.language; FR/SV only via /fr/ /sv/ paths,
  ?lang=, or the visitor's own click on the switch (remembered). Tested with sv-SE and fr-FR browsers.
- TODO before re-enabling browser detection: a native-speaker review of the SV (and FR) texts.

## 2026-10-26 (22:30) — analytics; second labels clickable; two duplicates were separate places

- Simple Analytics on every page (vite transformIndexHtml); owner added paris1550.vercel.app in the
  dashboard (their browser sends Do Not Track, so their own visits don't count).
- Owner: the vertical "LA VILLE NEUVE" (L0456) wasn't clickable: duplicate labels were dropped from the
  places. Now `also_px` on the main place (build_places.py, DATA_CONTRACT, model/maps): extra dots on the
  old map, clicking one opens the main place. 7 places have one.
- Checking the 9 duplicate pairs against Cousin: two were NOT duplicates. L0171 "LE BASTILLON" = the
  Bastillon du Temple (Cousin I,5), not the Bastillon Saint-Antoine (L0167); L0251 "R. NONNAIN" = the
  rue du Fauconnier, misnamed by the engraver (Cousin). Both now places of their own → 457 places
  (143 standing, 19 rebuilt, 77 renamed, 217 vanished, 1 open). Counts updated on all pages (en/fr/sv).

## 2026-10-26 (21:40) — start page = about; map at /map/; Corrozet; the shop question

- Deployed main 705f725 (the print-shop cloud session merged both branches into main itself, on the
  owner's word in that session). `/` `/fr/` `/sv/` = the about page with "Open the map"; the app is at
  `/map/` (+ /fr/map/, /sv/map/); `/place/<id>/` unchanged; `#place=` on `/` forwards to `/map/`;
  `/about/` → `/` 308 (web/vercel.json). Welcome card removed. Tested 14 routing cases locally with
  tiles, all good; live routes and redirects verified.
- **Corrozet:** the map's poem is in his *Fleur des antiquitez* (1532 ed., Lacroix 1874 reprint,
  Gallica bpt6k6487221d, pp. 102–106) under « Le nom et surnom de l'aucteur »: the acrostic is his
  declared signature. Book 112 lines vs map 108 (4 dropped; explains the 2 unrhymed lines); map updates
  facts: 11 → 14 gates, 100 → 120 councillors, gros murs → haultz rampars. Line 98 translation fixed
  (par elles = the Muses). Notes in data/research/corrozet.md, data/research/fleur_1532_louenges.txt.
- **The shop:** new about-page section "Where was the shop?" (#shop): street extent in 1550 (north of
  rue Mauconseil, plus today's rue des Petits-Carreaux), house not located, how it could be (archbishop's
  censiers → Brette's parcel plans; deeds naming neighbours). data/research/print_shop.md; listed as
  a research question in OPEN_QUESTIONS.md.
- Drive sources: Taildrop to the mini works (receiving); p-ubuntu needs `sudo tailscale set
  --operator=pelle` to send. Owner's files on p-ubuntu ~/Downloads: Corrozet Antiquitez 1550 (141 MB,
  no text via Drive), 1549 royal entry (images only), Registres t.10, Lespinasse Métiers, Delamare Lutèce.
  Wanted next: the Antiquitez' closing pages (does it reprint the poem with the 1550 figures?) and
  Registres vol. 3 (1539–1552) for Henri II's order.

## 2026-10-26 (20:35) — intro page live; Corrozet + about FR/SV in the cloud

- Owner: intro page OK as is, translate after launch; keep both the welcome card and the footer link;
  keep the FR/SV language redirect. Merged `intro` (about page, card, footer link) and deployed.
  About links stay English-only until the translation lands (sitemap: one plain /about/ entry).
- ⚠ Vercel free plan: "more than 5000 file uploads per day" — deploy with `--archive=tgz` (one
  upload). A failed deploy can leave 404s cached for a few minutes.
- The acrostic GILLES CORROSET (lines 1–14) = the poet Gilles Corrozet, not the publishers; the about
  page already says so and credits Cousin 1875.
- Cloud session session_016hjei192GYZPbkfQvLFN7i, branch `corrozet-about-i18n`: investigate the acrostic
  (other acrostics, who noticed it first, shared verses in Corrozet's works, the 1553 "commission"),
  update the about + texts pages, then translate the about page to FR/SV.

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

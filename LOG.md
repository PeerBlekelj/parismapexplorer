# Log

Newest first. What was done, what was found, what is open.

## 2026-11-04 (late) — References vs Sources, wording fixes, LIVE

In-page lists are now "References" (method: "Credits and references"), the top bar carries a site-wide "Sources" link (to `/sources/`) on every page (on a phone it sits at the end of the Contents list), bar labels are shortened with `data-nav`. Wording fixes after reading the Gemini-shortened text against the original (garbled shop sentence, "No study connects" back to "We have found no study…", "about 1561–1564", Cousin "first to point out" the acrostic, "youth work" removed, the Wikipedia 1553 commission described as resting on a modern study). Corrections/"tell us" links go to `/suggest/`, not GitHub. **Resume:** see the library LOG top entry and the private to-do artifact https://claude.ai/artifact/5mrUz8pFY1PND1QpifPMfg. Open here: street/church/college counts differ between method (221/91/33) and texts (219/91/32) pages.

## 2026-11-04 (evening) — shortened pages, note, contact form, sources page, top bar: LIVE

Live on paris1550.vercel.app (main = `f6c0b48` + the plain-form-post fix): the Gemini-shortened start page and cloud-shortened method page (both ~18-19% shorter, headings merged), the owner's note + cabinet photo + contact form at the top of the start page, `/suggest/` (per-place correction form, linked from every card and from the 20 held-description cards), `/sources/` (generated; see library LOG), a top bar on every written page (built from each page's own `<h2>`s, `data-nav="…"` overrides a label), a footer `© 2026 Peer Blekelj` + links, the right-bank paragraph and Ville/Cité/Université labels on `orientation.svg`, longer place texts inline (no disclosure), French/Swedish parked (redirects). **Form:** Web3Forms free key in `web/src/suggest.ts` (public by design), mail goes to the owner's dummy address, subject starts `[1550]`; confirmed delivered by the owner 4 Nov 22:08. Web3Forms refuses server-side and headless calls, so delivery can only be tested from a real browser. **Backup of the replaced pages:** `~/dev/backups/paris-1550-pages-2026-11-04/` and tag `pages-before-tighten-2026-11-04`. Branches `suggest-form`, `tightened-pages`, `method-page-tighten` are merged or superseded. **Open:** street/church/college counts disagree between the method page (221/91/33) and the texts page (219/91/32); the Basel overflow of the old nav is moot after the rewrite.

## 2026-11-04 — French and Swedish parked

On the owner's word the /fr/ and /sv/ versions are off: `LANGS` in `web/src/strings.ts` lists English only, no link or hreflang points at them, the pages are not built, the sitemap and the served `places.json` carry English only, and /fr, /sv (with or without trailing slash, any depth) redirect 307 to the English page. The translations stay in the repo. **To bring them back:** list them in `LANGS`, unfilter `TEXTS`/inputs in `vite.config.ts` (they follow `LANGS`), take the four redirects per language out of `web/vercel.json`, set `ACTIVE` in `scripts/make_texts_page.py`, restore the loop in `scripts/check_inscriptions.py`. Live and checked. A `:path*` redirect does not match a trailing slash; it needs its own `/:path*/` rule (found live: /fr/ was a 404 on the first deploy).

## 2026-11-03 (night) — an independent reading of the 206 descriptions, and twenty pulled

**An independent second reading found twenty descriptions that should not have shipped, and they are pulled.**
A separate model read all 206 longer descriptions against their sources (`data/research/detail_review.md`,
`detail_review.csv`). It asks what the mechanical checks cannot: is the source itself right, is the text about
the century the map shows, does it claim more than its source, does it conflate two things, does it agree with the
card it sits on. Result: **20 hold, 135 edit, 51 ok**. Of the 135, about half want one sentence deleted. It says
plainly that only **61** were checked deeply (the Wikipedia article opened past the extract, its references read)
and 145 shallowly, and that accents are flattened in its CSV.

The twenty were real defects, and all twenty were live. L0025 LA MONNOIE described the **modern** Monnaie de Paris,
down to a 2007 finance law, on a card for a building pulled down after 1775. L0029 described the Petit-Bourbon
(the hôtel d'Alençon is only its neighbour). L0034 described the Tour de Nesle on the hôtel de Nesle's card, and
turned an antiquarian's opinion of 1853 into an established fact. The rest are a mix of those three kinds: a source
about the modern place, a neighbour described instead, an unattributed opinion.

**Pulled, not rewritten.** The twenty ids are removed from `details.csv` and recorded in `details-held.csv` with the
reviewer's reason, so `places.json` now carries 186 details and the cards for those twenty show only their short
description, which is accurate. Regenerated with `--auto-gcps` (46 control points held); the diff of `places.json`
is exactly twenty places, field `detail` only, plus the timestamp. All six check scripts are green against a local
preview before the deploy. The suggested edits are suggestions: nothing in the review was applied.

**Also merged:** `unresolved-places` (data/research/unresolved_places_2026-11.md and proposals/), a write-up of the
six places that still carried no source and two research questions. Proposals only; no data file changed. Its main
finding is the **moulin de la Gourdaine**: the King's letter of 9 May 1551 (Registres, t. III, pp. 247-248) asks for
"ung viel moullin... à la porte de nostre jardin du Palais de Paris, nommé la Gourdaine" to house the German coining
engines, so the mill the map labels LE MOULIN DE LA MONNOIE cannot predate spring 1551. That is a lower bound on the
state of the city the sheet shows, and it is incompatible with a city as of 1550; it does not by itself choose between
*History of Cartography* ch. 48 (1550) and ch. 53 (ca. 1553), and Berty and Tisserand date the map 1552. The write-up
read Internet Archive OCR and not page images, and says so on every quotation; its Corrozet 1550 folios (ff. 88, 193,
198) were read from the page image afterwards.

## 2026-11-02 (16:10) — the faubourg sweep, and the reading flag stops overclaiming

**The reading flag told a lie, and the data already knew.** The owner asked why L0419 says "the label
is hard to read" when R. DES AUGUSTINS is plainly legible on the crop and other sources tell us what
is printed. He was right. That card carried `id_confidence: high`, a register match (`VAN:542`) **and**
a citation to Cousin 1875 p. 60 — who printed his own reading of the same label. The site was
asserting a fact about the woodcut on the strength of our own transcription doubt, contradicted by a
source cited three lines further down the same card.

`flag == "unsure"` is a note the tile-by-tile pass left about **its own** doubt. Comparing our
reading against Cousin's transcription of the printed label settles most of them. Of the 24 flagged:

- **14 agree character for character** (case, accents and the `R.`/`S.` abbreviations aside), L0419
  at 1.00 — two readers a century apart, so the reading is settled.
- **2 genuinely differ**: we read `REUILLI` where Cousin read *Rueli*, `BAIEUS` where he read
  *Raieus*. The flag is earned, and what is worth showing is **both readings**, not "hard to read".
- **8 have no second reading.** Cousin's alphabetical index heading does **not** count — it is his
  name for the street, not his transcription of the ink. Treating it as corroboration would have
  "confirmed" four labels on no evidence at all; that distinction is the whole of this fix.

places.json now carries a derived `reading` (clear / confirmed / disputed / uncertain) plus
`reading_other`. The filter chip and the table column count the **10 still open**, not all 24.
`scripts/check_reading.py` guards it with 20 assertions — two of which were **vacuous when written**:
the badge sits in `.kicker`, which CSS uppercases, so comparing `innerText` against "Unsure reading"
made the presence and the absence assertion both pass. The same class of bug as the `histoire`
matcher and the `neighboring` spelling miss earlier the same day.

**The faubourg sweep.** 18 more village and quarter cards were still described from their Wikipedia
lead — **13 had never been batched at all**, because the lead fell under the 200-character gate, so
nothing had ever flagged them. 5 carried a detail written from the lead. All 18 now have a period
source and a new detail, and they are the best in the set:

- **Bagnolet** — its article alone carries 30 pre-1600 references. Queen Isabeau of Bavaria's château
  of 1412 with its windmill, winepress and dovecote; Charles VI granting the manor of Mallassis to his
  mistress Odette de Champdivers; the Bois de Bagnolet bought by John of Lancaster in 1422. The source
  states that the **plan de Truschet et Hoyau is the first known depiction of the village**, so the
  detail can say the church "appears on the 1550 map" and have it be true.
- **Conflans** — the Charenton bridge seized by Vikings in 865, taken by the dauphin in 1358, retaken
  from the English in 1436.
- **Le Roule** — the moneyers of the Paris mint buying land around 1200 to care for their own lepers.

**206 details.** Three check corrections: **1550 is the sheet's own date** and the brief tells the
model to use it, so the year check no longer demands it appear in the source (two entries failed on
exactly that); markdown italics round Latin etymologies are presentation and are stripped rather than
rejected (8 of 18 had them, from the Toponymie sections); and `labor`/`favor`/`vapor` joined
US_SPELLINGS after the check caught `baptized` and let `forced labor` through **in the same sentence**.

**A review surface for the owner's read**, since nothing on the site says which places have a detail:
a private artifact listing all 206 with label, modern name, status, the live short description, the
longer one, and links to the card and the source — markable Good / Reword / Cut with a note, saved in
the artifact's own store so the marks can be read back and acted on.
<https://claude.ai/artifact/5FQVA5bgi4FEw9rv2X1FwP>

**Open:**
- The read itself. The checks prove provenance; only a person can judge fit.
- French and Swedish translations, after that read.
- L0185 (the Marne) has no history section to draw on; L0018 still refused over the altered quotation.
- `L0447` (Bicêtre) and `L0467` (Auteuil) were probed and skipped: their articles' history sections
  carry no pre-1600 reference either.

## 2026-11-02 (13:40) — the held-back places were a source failure, and eight came back

Chased the nine held back this morning. **None of them was a model failure.** The cause is one
parameter: `fetch_wiki.py` asks French Wikipedia for **`exintro`**, so `history_fr` is the article's
**lead**. For a church or a street the lead is the whole story; for a modern commune it is today's
population, today's politics and today's buildings. The model wrote the only thing those sources
supported.

**`scripts/fetch_wiki_history.py`** fetches the article's *history sections* instead, into
`data/research/sources_long.csv`, which `make_detail_batches.py` and `ingest_detail.py` both now
prefer over `history_fr` — the same text in both, so a span is still checked against exactly what
the model was given.

**Two traps on the way, both about a pattern being too narrow:**

1. The section is normally called **"Historique"**, not "Histoire". A first pass matched only
   `histoire`, and reported that Bercy and the faubourg Saint-Germain had **no history at all**.
   Matching `histo` found 4,207 and 3,112 characters of it. Within the same hour the US-spelling
   check matched `neighborhood` and let `neighboring` through, then caught `baptized` and let
   `forced labor` through in the same sentence. A too-narrow pattern returns zero and reads exactly
   like a clean result.
2. **The right article is often not the one the card cites.** Bercy pointed at `Quartier de Bercy`,
   whose history begins in the 19th century. `Bercy (Seine)` is the village the map shows: 0
   pre-1600 references became 7. The article a place is *identified* by is not always the article it
   should be *described* from.

**Eight of the nine now have a detail**, and they are the best writing in the set. Clignancourt's
vineyards stripped of unripe grapes by Breton and Burgundian soldiers on 9 September 1465;
Belleville's medieval ploughland and vines on the "Mont chauve", and the 1543 chapel built to spare
residents the walk to Saint-Merry; Montreuil keeping its tax exemptions on condition it maintained
the fountains feeding the Vincennes fishpond. **Bercy is the find**: its source names *"plan de
Truschet et Hoyau"* outright and says the place is labelled **"Percy"** on it — which is exactly
what our sheet reads for L0441. An independent corroboration of that identification, arrived at
sideways.

**193 details**, live and checked on production.

**Only L0185 (the Marne) stays held**, and it is a final answer rather than a gap: that article has
no history section at all — hydronymy, flood records, water quality. The summary already says what
a reader needs.

**Period fit resisted mechanisation twice, so it is a warning, not a check.** Requiring an early
date in the text wherever the source has one would reject **33 of the 185 already shipped**, nearly
all of them good: "Joan of Navarre, wife of Philip the Fair" is plainly medieval and names no year.
Absence of a date is not evidence of the wrong century. `ingest_detail.py` prints it as `look`,
pointing a reader at entries worth a glance, and fails nothing.

The brief gained a **"Which century to write about"** section naming the exact failure: a
population in 2023, a quarter number, which party has held the town hall since 1925 are all true,
sourced, and wrong for this card.

**Open:**
- A read of the 193 by the owner; the checks prove provenance, not editorial fit.
- French and Swedish translations, after that read.
- The other `village_faubourg` and quarter cards still read from their leads. Eight were fixed
  because they had produced a bad detail; the rest were never asked. `sources_long_titles.csv` is
  where to add them.
- L0018 still has no detail (the altered quotation, refused — see 10-31).

## 2026-11-02 (11:20) — the longer descriptions on the card, and nine held back

The 7 rewrites blocked by the Gemini quota went through on the first pass once it reset, and
`detail` is now wired from `data/research/details.csv` through `build_places.py` into places.json
and onto the card, under the summary behind a **"More about this place"** disclosure. It continues
the summary, never replaces it. English only, so French and Swedish say "(en anglais)" / "(på
engelska)" and mark the text `lang="en"`. **185 places carry one.** Live and checked on production.

**The read found a failure the provenance checks cannot see, and it is a source problem, not a
model problem.** Nine details were written from a source that is long but **off-period** — a modern
commune or quarter article. Ivry and Vitry got the population in 2023, 1970s brutalism and the PCF
since 1925; Belleville and Clignancourt got their administrative quarter numbers; Bois de Vincennes
got its hectares back from its own summary; Saint-Nicolas-du-Chardonnet got the 1977 occupation as
its "notable recent history". Every one of them passes every check: the spans are verbatim, the
years are in the source. The source simply is not about the place the map shows.

`make_detail_batches.py` gates on **`len(source) >= 200`**, which measures bulk, not period. A
modern commune lead clears it easily. The nine are listed with their reason in
`data/research/details-held.csv`, waiting for a 16th-century source; the fix belongs upstream in
which sources enter a batch, not in another pass over the same text.

Four more were **trimmed by hand** to the part that is about the place on the map — Hôtel-Dieu
(keep the pilgrims' hostelry, the Augustinian nuns and doctors arriving in hospitals only in the
18th century; drop the 2019 retail plan), the Cordeliers, the Seine and Montmartre. Trimming only
removes claims, so nothing can enter that the source does not carry; each was re-checked for the
word floor, the summary-restatement ratio and the forbidden opener afterwards.

**A measurement worth keeping:** a first pass flagged 35 details as having "no date before 1700",
but it was over-firing — entries write "In the 13th century" in words, and a street's register
extract legitimately carries no dates at all. Counting written-out centuries as well brings it to
52 of 194, and most of those are fine. Period fit is not mechanisable; it took reading them.

**What was mechanisable, and is now a check:** British English. `ingest_detail.py` gained a
US-spelling table, which caught 3 in the shipped 194 (`practicing`, `neighborhood`). The first
version of the pattern missed `neighboring` — a reminder that a check with a too-narrow pattern
reports zero and looks like success.

**`scripts/check_details.py`** — 24 assertions, mostly absences: no empty disclosure where there is
no detail, the summary never moves aside, the body stays hidden until asked, and both other
languages say the text is English.

**Two process notes.** `build_places.py` must be run with **`--auto-gcps`** (CONTRIBUTING.md line
44): without it gcps.json silently drops from 46 control points to the 20 hand ones, and the diff
looks like an ordinary regeneration. And piping `vercel build` into `head` kills it with SIGPIPE
part-way, leaving `.vercel/output/` without `config.json`; the deploy then fails with a message
about the config file that says nothing about the real cause.

**Open:**
- The 9 held-back places want a 16th-century source. Lazare, Sauval and Berty cover most of them.
- French and Swedish translations of the 185, after the English has been read by the owner.
- L0018 still has no detail (the altered quotation, refused — see 10-31).

## 2026-10-31 (19:30) — 190 longer descriptions, written by Gemini through the gateway

The brief and the batches did not need a human in the middle: the mini's **LiteLLM gateway**
(`localhost:4000`, see the llm-gateway notes) takes them straight to Gemini.
`scripts/run_detail_gemini.py` sends the brief plus one batch and saves the reply;
`scripts/ingest_detail.py` checks it and writes the ones that pass.

**190 details in `data/research/details.csv`**, 40–141 words, median 72, out of 277 asked for.
**79 came back `null`** — the model's own judgement that the source adds nothing over the summary,
which is what the brief asks for and is the right answer for a street the register describes in one
line. Nothing is wired into the site yet.

**The checks did real work.** Two findings worth keeping:

1. **The model alters a quotation while asserting it is verbatim.** For L0018 it returned a `used`
   span reading *"l'édifice le plus **sinister** de Paris"*; the source reads *sinistre*. It did this
   **twice, in two independent passes**, after being told not to retype or correct spans. One letter
   — but a model that quietly anglicises a word inside a quotation will quietly move a date. The
   check stayed strict and **L0018 has no detail**; its summary is complete without one.
2. **A style rule in a prompt is a hope; a check is a guarantee.** The brief forbids opening with
   "Located in…". Ten of 197 did exactly that, and three leaked markdown into a plain-text field.
   Both are mechanically detectable, so both are now checks in `ingest_detail.py` rather than
   sentences in the brief.

**Model**: `gemini/gemini-3.5-flash`. `gemini-2.5-pro` is **retired** by Google ("no longer available
to new users"), `gemini-3.1-pro-preview` is over quota on this key, and `gemini-3.8-flash` and
`gemini-flash-latest` both answered **503**. The gateway advertises 88 Gemini models; several of them
the API will not serve.

**Cost**: **$3.17** for 29 calls — 152k tokens in, 330k out. The output is large because thinking
tokens are billed.

**Two gateway notes**: `litellm_session_id` works (these are tagged `paris1550-detail-batch-NN` in
`LiteLLM_SpendLogs`), but **`GET /spend/logs?start_date=…` returned 0 rows while Postgres held 123**
— its date filter is broken, not just `/global/spend/report`. Query the container's Postgres directly
(`docker exec litellm-postgres psql -U litellm -d litellm`).

**Open:**
- **7 details are pulled and awaiting a rewrite** (L0118, L0145, L0176, L0191, L0204, L0443, L0444):
  they opened with "Located…" and were removed from details.csv; the daily Gemini quota ran out
  mid-rewrite. Resume with
  `scripts/run_detail_gemini.py . work/detail/batch-NN.json --retry work/detail/failed-style-NN.json`
  for batches 03, 04, 05 and 11, then ingest.
- **The checks guarantee provenance, not editorial fit.** A spot-read found L0118 (Saint-Eustache)
  drifting into the life of the saint rather than the church on the map — sourced, but off the point.
  The 190 want a read before they are shown.
- Still to build: `detail` through `build_places.py` into places.json and the data contract, and the
  disclosure on the card. French and Swedish after the English is reviewed.

## 2026-10-31 (17:05) — a brief and a validator for the longer descriptions (option B)

Option B — a written `detail` behind a disclosure on the card, not the raw French extract — is the
owner's choice, for later. The handover package is ready now so the writing can be done elsewhere.

**`data/research/DETAIL_BRIEF.md`** is what goes to the model with each batch: what the site is,
the house voice with two worked examples, the 80–160 word range, and the rule the whole thing turns
on — *every factual statement must be supported by the `source_fr` supplied with that place*, with
`null` an explicitly welcome answer when the source is thin. It carries the four traps this project
has already fallen into (two streets with one name; the later building of the same name; an
administrative extract dressed up as a history; a year nobody read).

**`scripts/make_detail_batches.py`** writes `work/detail/batch-NN.json`: **277 places in 12 batches**
of 25, grouped by type so a batch keeps one voice. Only places whose French extract runs to 200
characters or more are included — below that the extract says no more than the summary already does,
and asking for a longer text would be asking for invention. (414 places have an extract at all; 137
of those are too short to be worth it.)

**The part that makes it checkable**: the model must return, with each text, `used` — short spans
**copied verbatim** from that place's source, one per factual claim. `scripts/ingest_detail.py` then
holds the text to the source mechanically: every span must appear verbatim (accents and typographic
variants normalised), **every four-digit year in the text must appear in the source or the summary**,
`added_beyond_source` must be empty, the length must be in range, and the text must not read as a
restatement of the summary. Nothing is ingested unless the whole batch is clean.

Tested against five deliberately broken returns — a fabricated year, a span that is not in the
source, context added from the model's own knowledge, an unknown id, and short texts — and all nine
expected failures fired; the one clean entry passed and wrote. The test rows were then removed, so
`data/research/details.csv` does not exist until real work lands.

**Still to build when the texts come back**: `detail` through `build_places.py` into places.json and
the data contract, and the disclosure on the card. French and Swedish are a separate pass after the
English is reviewed.

## 2026-10-31 (16:10) — every place has a description

**0 places without one**, in all three languages (was 20 without any description, and 22 without a
French or Swedish one). `scripts/check_coverage.py` reports the gaps and now **fails** if a place
has no description; the other gaps it reports and allows, because a null there means "not researched
yet", which is a legitimate state.

**What the 20 were**: mostly vanished mansions, hospitals and chapels — Lostel Dangoulesme, Lostel
Dargent, Lotel de Nevers, Lotel de Rims, Lopital S. Gerves, Les Audriettes, S. Bon, La Chapelle de
Braques — plus two colleges, two gates, a tennis court, a mill, a crossroads and two streets.

**Four of them turned out to be properly researchable** and now cite the article the words came
from: the **Haudriettes** (founded by Étienne Haudry and his wife Jeanne, chapel licensed by
Philippe le Bel in 1306, moved to the rue Saint-Honoré in 1622 as the Sisters of the Assumption);
**Saint-Bon** (on the site of an older Sainte-Colombe, suppressed 1790); the **Tour du Bois** (where
Charles V's wall met the Seine, by the present pont du Carrousel); and the **chapelle de Braque**
(Arnould de Braque, 1348, in the street that still carries the name). The **collège de Bayeux**
already had its article and now uses it.

**The rest say what is and is not known.** For a vanished hôtel that Cousin's table attests and
nothing else does, the description says so in as many words rather than inventing a history or
leaving a blank. Two conflation traps are written into the text so a later reader does not fall in:
L0009 is **not** the hôtel d'Angoulême-Lamoignon (begun 1584), L0027 is **not** the hôtel de Nevers
on the Monnaie site (1580s), L0196 is a different Braque from L0047, and L0421 is **not** the rue
Verderet that fr.wikipedia describes — the trap this log recorded on 2026-10-30.

**A lead worth chasing, in OPEN_QUESTIONS.md**: the map marks LE MOULIN DE LA MONNOIE on the Seine
just west of the Cité. Henri II sent to Augsburg for the screw press in **1550** and Aubin Olivier's
*Monnaie du Moulin des Étuves*, at the west end of the Cité, was authorised in **July 1553**. If the
mill on the sheet is that works it bears on the map's contested date — but nothing here establishes
it, and the place's own description says so.

**Still open**: 6 places carry no source at all (L0031, L0083, L0133, L0202, L0217, L0224 — none is
in Cousin's table under a name the pairing recognised); 24 labels have an unsure reading; 6 places
are not identified and not marked vanished. All listed by the coverage check.

**DEPLOYED** (main, prebuilt, `--archive=tgz`); all three browser suites green against
`https://paris1550.vercel.app`, and a filled entry checked live in its page metadata.

**Owner's call**: longer descriptions behind a disclosure on the card — a written `detail` field,
not the raw French source extract — are wanted, but **later**.

## 2026-10-31 (14:20) — the sheet's own inscriptions are on the map

The four quarter words, the two named winds, the title banderole, the two coats of arms, the king's
crescents, the poem, the publishers' notice and the Basel stamp: **13 inscriptions**, each with a mark
on the 1550 sheet, a card that explains it, and a link into the part of `/texts/` that covers it.

**Six of them were already read.** `labels_inventory.csv` had SUBSOLANUS, ORIENS, AUSTER,
SEPTENTRIONES, OCCIDENS and FAVONIUS as type `decoration` (L0161–L0166) and `build_places.py` then
threw them away. The other seven were found on `mockups/overview.jpg` (2400 px wide, 4.5375 scan px
per overview px) and their positions read off a grid drawn in scan coordinates; the mapping was
checked against SUBSOLANUS's known position before any of them were trusted. New ids L0471–L0478.

**They are a type, not a status.** `inscription` reaches the app as its own type, and the app treats
it as ink on paper rather than a place:
- `geoKind: 'sheet'` — no position on the ground, not even an estimated one. They are **not drawn on
  the modern map** and cannot be picked there; they never anchor the two maps to each other, and a
  shared list's fit ignores them.
- The card drops the rows that would otherwise be filled with placeholders: no "Today", no status
  badge, no "Position today". It keeps "Position (1550)" and adds **Read it on the texts page →**.
- The list and the table say **"Printed on the map"** where a place says what is there today — an
  inscription was never missing a modern name.
- `t.count` still says **457 places**; the 13 are counted separately in the same line ("457 places ·
  13 inscriptions"), so neither number is inflated. The back link quotes that same wording instead of
  counting "places" of a list that is not all places.
- The **poem is one thing in two panels**: the second is `also_px`, which was already the mechanism
  for a place labelled twice, so both panels are clickable and open the same card.

**Three of them carry no words at all** — the two coats of arms and the crescents. Their `old` is a
name, not a reading, so `printed: no` in the data; the card sets the title in italic rather than as
small-caps, says "A device, not a text: it carries no words", and the name is translated
(`deviceNames` in strings.ts, and in `vite.config.ts` so a shared link's title is right before the app
has run).

**Anchors**: `make_texts_page.py` now gives the four items of "Other words on the map" their own ids
(`title`, `winds`, `arms`, `basel`); `poem` and `notice` were already section ids. A `li:target` rule
marks the sentence you were sent to. The texts page is long and its images settle late, so the browser
corrects the jump over about a second — that is the browser, not the link.

**Checking**: `scripts/check_inscriptions.py <url>` (24 assertions, mostly absences — what must *not*
appear on an inscription's card or on the modern map).

**DEPLOYED** (main 62b7b8e, prebuilt, `--archive=tgz`). All three suites green against
`https://paris1550.vercel.app`; the routes, the data, the sitemap (1422 urls), the OG images (471,
regenerated for the new ids) and the old domain's 308 checked after the deploy.

**Open**: the French and Swedish summaries for the 13 are drafted here, not reviewed, like the rest of
the translations.

## 2026-10-31 (11:40) — the QR a camera can read; stronger marks with a switch; starred in the table

**The QR was never wrong — it was too small.** Reported as "the QR sharing isn't working". A decoder
reads the rendered symbol and returns exactly the link the panel shows, so the encoding was fine; it
was drawn at **92 css px**, which is where a scanner starts to lose it. Under any blur or distance the
capture falls below about 100 px of symbol and nothing decodes — there was no margin at all. Now 200 px,
stacked above the link instead of beside it, with the **4-module quiet zone** the spec asks for (it had
2) and **no border**, which was eating into the zone a camera looks for. `check_stars.py` fails if it is
ever drawn under 160 px. Deployed and re-scanned live.

**The top strip could not help overlapping.** The modes bar was centred absolutely and the controls
anchored absolutely to the right, with a `max-width: 1180px` media query meant to drop the controls
below. The query keys off the **viewport** while the bar is constrained by the **pane** — the viewport
minus the 380 px sidebar — so at 1400 px wide the pane is 1020 and they collided with no query firing.
Now one wrapping flex row (`.maptop`): the modes bar centres itself in what the controls leave, and
when they no longer fit the controls take their own line. The overlay note is in the same row, so its
hard-coded `top: 56px`/`96px` are gone too. Checked at twelve widths in both modes.

**The marks stand out, and can be switched off** (owner's pick, option B of `mockups/favorites/`):
a disc of the map's own paper under each mark, with the engraving showing through, rather than a
thin red ring lost among the red-orange roofs. A **Places** toggle beside the orientation switch hides
them; **starred places stay**, since there are few of them and they are the visitor's own. Clicking a
label still works with the marks hidden — picking is geometric, not a hit test on the layers. The
switch travels in a shared view link as `&d=0`.

**Starred is a column in the table**, sortable, and a star can be set from there. It shows only for a
starred row, under the pointer, or always where there is no pointer — as in the sidebar list.

**Checking**: `scripts/check_map_controls.py <url>` (the strip at twelve widths, the halo, the switch,
the column); `scripts/check_stars.py <url>` as before.

**All of it is DEPLOYED** (main 79f09b1, prebuilt, `--archive=tgz`). Both check scripts run green
against `https://paris1550.vercel.app`, and the nine routes, the data, the sitemap, the OG images, both
tile pyramids and the old domain's 308 were checked after the deploy.

**Open:** the direction banners (SEPTENTRIONES, ORIENS, the winds), the arms, the Basel stamp, the poem
and the publishers' notice are **not in the gazetteer** — 0 of 457 rows. Their explanations already
exist in all three languages in "Other words on the map" on the texts page; what is missing is a
pixel position, a dot, a card, and a link from that card into that section. Next piece of work.

## 2026-10-30 (22:45) — starred places and sharing: LIVE

**Deployed** (main 1d22a4b, prebuilt, `--archive=tgz`). A visitor can keep their own list of places and send a place, a view or the
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

**Checked live** after the deploy: all 39 assertions against `https://paris1550.vercel.app`, in
English, French and Swedish. Routes: `/` `/fr/` `/sv/` `/map/` `/fr/map/` `/sv/map/` `/place/L0017/`
`/method/` `/texts/` 200; `/data/places.json`, `/sitemap.xml`, `/og/L0017.jpg`, both tile pyramids 200;
the old domain still 308s path-for-path.

**Open:**
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

# Gilles Corrozet and the poem on the map

Research note, 26 October 2026 (cloud session). Question: what does the acrostic GILLES CORROSET in the
poem on the Truschet & Hoyau plan tell us, who noticed it, do the verses occur in Corrozet's own books,
and what was his part in the map?

**Access caveat** (superseded on 29 Oct 2026 — see the verification note below; the external sources
have since been opened). Direct page fetches were blocked in this session (gallica.bnf.fr, fr.wikipedia.org,
archive.org, press.uchicago.edu all refused by the network policy). Read **in full**: only the files in
this repository (Cousin's notice, `cousin_1875_notice.txt`, OCR; the poem as transcribed in
`scripts/make_texts_page.py`; the panel crops in `data/map_texts/`). Everything else below was **seen only
as search-engine extracts**, and is marked so.

**Update, same evening:** the owner put Lacroix's 1874 reprint of the *Fleur des antiquitez* (Gallica
PDF bpt6k6487221d) on Google Drive. The connector could not download the 35 MB PDF, but Drive's search
index returned its OCR text up to PDF page 132, which includes the whole poem (PDF pages 102–106). §2
and §3 are rewritten from that text; it is OCR, not checked against the page images.

**Verification pass, 29 October 2026 (branch `verify-research-quotes`).** The flagged claims below were
checked against the sources themselves. Results in full: `quote_verification.md`. In short, for this file:
the fr.wikipedia quotation is exact but **two of our remarks about it are wrong**; the **Sénat quotation
does not exist**; both *History of Cartography* chapters check out; and no source yet read mentions the
acrostic, so Cousin is still the only one.

## 1. Acrostics and other signatures: one, and only one

The poem has 108 printed lines (`POEM_1` lines 1–78, three columns of 26; `POEM_2` lines 79–108, two
columns of 15). Looking at the panel crops, there are exactly **two printer's ornaments** (fleurons), at
line 1 (“Gentilz lecteurs…”) and line 15 (“Noble cite…”). The second panel (lines 79–108) has none; it
continues the sentence begun at line 78 (catchword “Le sainct”). So the poem has an opening stanza of 14
lines and one long body of 94 lines.

Checked by script (first letter of each line, last letter, initial of the second word, second letter),
per stanza, per column and over the whole poem, forwards and backwards:

| Segment | First letters | Result |
|---|---|---|
| 1–14 (opening stanza) | `GILLESCORROSET` | **GILLES CORROSET** |
| 15–78 (rest of panel 1) | `NDPDDSOHDDOFCFMFQPEDEPEHTPPOEEPDDTALEEPMMCDPLCDPDQPDPCEPOPPDATEC` | nothing |
| 79–108 (panel 2) | `LNDDSATPAAEEDEPALFPDEADASVDEQQ` | nothing |
| column 2 (27–52) | `CFMFQPEDEPEHTPPOEEPDDTALEE` | nothing |
| column 3 (53–78) | `PMMCDPLCDPDQPDPCEPOPPDATEC` | nothing |
| panel 2, col. 1 / col. 2 | `LNDDSATPAAEEDEP` / `ALFPDEADASVDEQQ` | nothing |
| last letters, any segment | e.g. 1–14 `EENNEEÉÉSSEEÉÉ` | only the rhyme pairs; no telestich |
| second-word initials, second letters | — | nothing |

- **Negative:** no second acrostic, no telestich, no name of Truschet, Hoyau or anyone else. The line
  count (108 = 14 + 94; 78 + 30) has no evident meaning. Two lines lack a rhyme partner (21, 74; see
  the texts page), so the poem may once have had 110 lines.
- **Corrozet's motto** *Plus que moins*, which he put on his books, does not appear on the map (“Plus
  que iamais”, line 97, and “Plus qu'en nul lieu”, line 91, are ordinary phrases).
- **The publishers' notice** is prose in 9 printed lines; their initials (I, &, l, s, q, c, e; A, l)
  spell nothing. Its only signature is the open one: “A Paris, par Oliuier Truschet, & Germain Hoyau…”.
- The acrostic spells **CORROSET** with an *s*. Cousin reads it the same way and does not comment.
  The usual spelling in Corrozet's imprints is *Corrozet*; *s* for *z* is a common 16th-century
  variant (the acrostic needs an S-line: “Son hault estat”, line 12).
- The ornament at line 15 marks the end of the acrostic exactly: the stanza was built to carry it.

Confidence: high (the text is transcribed line by line from the scan and checked; the ornaments are
visible on the crops).

## 2. Who noticed it first

**Jules Cousin, 1875.** After transcribing the first 14 lines, he writes (OCR text of the Gallica scan,
`cousin_1875_notice.txt`, printed pp. 51–52; spelling of the OCR kept, obvious OCR slips such as
“i55o” and run-together words corrected):

> Rien à tirer de ce fastidieux dithyrambe farci de lieux communs et de fables mythologiques sur
> l'origine de Paris, alors si fort en honneur. Mais ce n'est pas sans raison que nous en avons transcrit
> ici les quatorze premiers vers. En isolant les lettres initiales, ils nous révéleront le nom de l'auteur
> GILLES CORROSET, le libraire historiographe de la ville de Paris, qui venait de faire paraître en 1550
> la première et la plus belle édition de ses Antiquités de Paris, succédant à l'ouvrage qu'il traite
> lui-même de « petit livret plein d'erreurs et de fables qu'il a supprimé et mis à néant », la Fleur des
> antiquités de Paris, publiée pour la première fois en 1532. […] C'est une chronique, fabuleuse pour
> toute la période antique, plus que succincte pour la période contemporaine, dont chaque chapitre se
> trouve ensuite résumé en quelques vers, que l'on peut qualifier, suivant la devise de l'auteur, de plus
> que moins médiocres. Or cet interminable poème qui remplit, en cinq colonnes, deux cartouches de notre
> plan est précisément le couronnement de l'édifice, le poème final qui termine et résume la Fleur des
> antiquités. Nous pouvons en conclure que c'est sous le patronage de Gilles Corrozet que fut édité ce
> grand plan et qu'il servait de complément à son livre des Antiquités de Paris. Ajoutons sans craindre
> de nous tromper que livre et plan se vendaient en sa boutique au Palais aussi bien que chez les
> éditeurs, car nous verrons plus loin que cet exemplaire du plan fut acheté alors à Paris et rapporté à
> Bâle en même temps qu'un magnifique exemplaire du livre de l'édition de 1550.

Translation:

> Nothing to be got from this tedious dithyramb stuffed with commonplaces and mythological fables on the
> origin of Paris, so much in favour at the time. But it is not without reason that we have transcribed
> its first fourteen lines here. Taking their initial letters on their own, they will reveal the name of
> the author, GILLES CORROSET, the bookseller and historiographer of the city of Paris, who had just
> brought out in 1550 the first and finest edition of his *Antiquités de Paris*, which replaced the work
> he himself calls “a little booklet full of errors and fables, which he has suppressed and brought to
> nothing”: the *Fleur des antiquités de Paris*, first published in 1532. […] It is a chronicle, fabulous
> for all of antiquity and more than brief for recent times, each chapter of which is then summed up in a
> few verses that one may call, after the author's motto, more rather than less mediocre [a pun on
> Corrozet's device *Plus que moins*]. Now this interminable poem, which fills two cartouches of our plan
> in five columns, is precisely the crowning of the building, the final poem that closes and sums up the
> *Fleur des antiquités*. We may conclude from this that this great plan was published under the
> patronage of Gilles Corrozet and served as a complement to his book of the *Antiquités de Paris*. Let
> us add, without fear of being wrong, that book and plan were sold in his shop at the Palais as well as
> at the publishers', for we shall see below that this copy of the plan was bought in Paris at the time
> and brought back to Basel together with a magnificent copy of the book in the 1550 edition.

And later (p. 58, OCR): Amerbach bought the plan “avec un bel exemplaire de l'édition des Antiquités de
Paris de 1550. C'était probablement le plan et le guide offerts alors aux étrangers […] et Corrozet paraît
en avoir eu sinon le monopole, du moins la spécialité” (“probably the plan and the guide then offered to
foreigners […] and Corrozet seems to have had, if not the monopoly, at least the speciality of them”).

**Before Cousin: Corrozet himself.** In the *Fleur des antiquitez* (second edition, 1532, as reprinted
by Lacroix in 1874) the same fourteen lines stand under the heading **“Le nom et surnom de laucteur.”**
(“The author's first name and surname”), followed by **“Louenges de Paris faictes par ledict aucteur.”**
(“Praises of Paris made by the said author”). The acrostic was announced in print in 1532; it is no
hidden signature. The map drops both headings and keeps only the printer's ornaments, so on the map
the name is hidden. Cousin, who knew the *Fleur* (“Nous connaissons tous ce rare petit livre”) and
wrote a year after Lacroix's reprint, presents it as a reveal (“ils nous révéleront”) without saying
the book labels it. Fair credit: Corrozet signed it; Cousin was the first to point it out **on the
map** (1875); the map itself was unknown before 1874.

Corrozet liked the device: right after the poem the *Fleur* prints an “Épigramme sur le nom de Paris”
whose five lines begin P(our), A(ccroissement), R(och), I(ustice), S(cauoir): an acrostic of PARIS.
The map does not print it.

**Later literature** (checked against the sources, 29 Oct 2026):
- **French Wikipedia**, “Plan de Truschet et Hoyau” — **quotation confirmed, our gloss on it wrong**:
  “Ce plan est une commande datée de 1553 d'un certain Corrozet adressée à deux artistes de la rue
  Montorgueil de Paris, le dessinateur Olivier Truschet et le graveur Germain Hoyau.” We said the
  sentence had no reference and that “un certain Corrozet” showed the writer had not identified him.
  **Both are false.** The sentence carries two footnotes: on “Corrozet”, « Gilles Corrozet, éditeur
  (cf. infra, p. 169) » — so Wikipedia does identify him — and at the end, « Françoise
  Vergneault-Belmont – *Lire l'espace penser la carte* – p. 168 » (L'Harmattan, 2008,
  ISBN 978-2-296-07831-4). The 1553 commission therefore has a named source, which we have not read.
  The article's infobox gives « 1552 (vue de Paris) / 1553 (édition) ». No acrostic anywhere in it.
- **Sénat library brochure** *Paris : représentations et plans anciens* (senat.fr, brochure-02.pdf) —
  **contradicted: the sentence is not in the brochure.** All 12 pages carry a text layer and contain no
  “plan de Bâle”, no “patronné”, no “1551”, no “annexe”. Its only mention of the map is a picture
  caption: « Plan de Paris sous le règne de Henri II, par Olivier Truschet et Germain Hoyau. Reproduit
  en fac-similé d'après l'exemplaire unique de la Bibliothèque de Bâle, par M. F. Hoffbauër (1877) ».
  Corrozet appears only as the author behind Bonfons's 1608 reissue. **Cite nothing to this brochure.**
- **History of Cartography vol. 3, ch. 48** (Monique Pelletier; the Fine-to-Postel section sits inside
  it) — **confirmed**, p. 1500: “The Paris map and *Les antiquitez* were sold together, as confirmed by
  their joined use by **Theodore Zwinger** in his *Methodus apodemica* (Basel, 1577).” The same page
  makes Hoyau the draughtsman and Truschet the engraver, after Dérens, and dates the map **1550**. No
  acrostic.
- **Hofmann, ch. 53** — **confirmed**, p. 1572, in two places: the plan was “published by Olivier
  Truschet and Germain Hoyau **ca. 1553**”, and, of Mathonière's 1598 inventory, “probably the one **cut
  in 1553** by Olivier Truschet and Germain Hoyau”. No Corrozet in the chapter. **Note that HOC's two
  chapters disagree: ch. 48 says 1550, ch. 53 ca. 1553.** Never cite “HOC” for a date without the
  chapter.
- **Boutier 2002**: not seen (dates c. 1553, as cited elsewhere). Unknown whether it discusses the
  acrostic.
- **Dérens 1980** (commentary to the Zürich facsimile): still not read, but HOC ch. 48 n. 80 gives the
  full citation — Jean Dérens, *Le plan de Paris par Truschet et Hoyau, 1550, dit plan de Bâle* (1980;
  reprinted Paris: Rotonde de la Villette, 1986) — and his argument: the 1550 *Antiquitez* is a **less**
  detailed guide than the 1543 *Fleur* “because, according to Dérens, the Truschet-Hoyau map, which came
  out that same year, rendered some information included in the late *Fleur des antiquitez* useless”.
  Note that Dérens's own title dates the plan **1550**.
- **Corrozet studies** (Chiron, Godet & Tran (eds.), *En lisant, en écrivant. Gilles Corrozet, un
  libraire-auteur au temps de la Renaissance*, colloquium, Toulouse; the Persée article on Corrozet and
  the fables): seen only as titles; nothing about the map surfaced in the extracts.

So: **no later source now read discusses the acrostic** — not fr.wikipedia, not en.wikipedia (which does
not mention the map at all), not the Sénat brochure, not HOC ch. 48 or ch. 53, not the Institut Paris
Région. Cousin remains the only writer known to point it out. Of those read, HOC ch. 48 supports the
sold-together claim from Zwinger; Wikipedia alone speaks of a dated “commission”, and does cite a source
for it (Vergneault-Belmont 2008, p. 168), which still needs reading.

## 3. Shared verses: the map's poem is Corrozet's “Louenges de Paris”, lightly revised

Compared line by line (script in the session; OCR of Lacroix 1874 against the map transcription in
`scripts/make_texts_page.py`, spelling normalised):

- **Same poem.** The *Fleur* has the 14-line acrostic stanza plus 98 lines of “Louenges de Paris”: 112
  lines. The map has 108: the same text in the same order, with **four lines left out** and about ten
  words changed. Everything else differs only in spelling (*beaulx/beaux*, *et/&*, *Luthesse/Lutece*…).
- **The four missing lines** (book numbering):
  - 21 “Soit dudict lieu qui fut de Gaulle roy” (whether Paris, founder of the place, was king of Gaul),
    the partner of “arroy”: this is why map line 21 has no rhyme;
  - 73–74 “Lequel encloz sep[t] lieues lors contient / Comme le bruyt tout commun le maintient” (the
    enclosure contains seven leagues, as common report has it): a whole couplet dropped;
  - 77 “Depuis la ville en la noble cite”, the partner of “De la cite en luniuersite”: this is why map
    line 74 has no rhyme.
  So the texts page's guess (“perhaps a line was dropped each time”) is confirmed.
- **Changed readings** (map / *Fleur* 1532):

| Map line | Map | *Fleur* (1532, Lacroix) |
|---|---|---|
| 2 | la stature | la structure (OCR; could be a misreading) |
| 15 | **Noble** cite | **Nostre** cite |
| 43 | la riuiere **propice** | la riuiere **rassise** (rhymes with *assise*; the map's word does not) |
| 45 | Puis est remplie de tres belle fonteine | Ou leau decourt clere plaisante et seine |
| 47 | boys, & **plantes** | boys, et **plaines** (rhymes with *tresplaines*) |
| 68 | Ceste ville à **quatorze** portes close | Ceste ville est de **unze** portes enclose |
| 69 | Et **haultz rampars**, qui n'est pas peu de chose | **Avecq gros murs** qui pas nest peu de chose |
| 77 | En tresgrand nombre | En tres gros nombre |
| 79 | **Le** sainct senat | **Et** sainct senat |
| 80 | Nombre **six vingtz** hommes | En nombre **cent** hommes |
| 83 | à la court | en la court |
| 96 | **Font** en ce lieu | **Sont** en ce lieu (long s / f: possibly OCR) |
| 106 | qu'il n'ya **peuple** au monde | quil ny a **ville** au monde |

- **Where the book helps read the map:** line 98, map “ou par elle semond / Estoit iadis maint homme”,
  book “ou par elles se mond”: *elles* are the Muses (subject of the sentence), so “where many a man
  was once summoned by them to learn”; the map's singular *elle* is most likely a dropped *s*. The
  texts page translated “she” (Pallas); changed to the Muses in all three languages. Line 96 *Font*
  (map) / *Sont* (book): *sont … tenantes* (“are holding [their dwelling]”) is the better grammar; the
  map's letter is a clear F on the scan, so the transcription stays, and the translation (“make their
  lasting home”) fits both.
- **What the changes look like:** the factual ones go one way, towards Paris around 1550: eleven gates
  become fourteen, “thick walls” become “high ramparts”, the hundred councillors of the Parlement become
  six score (120; Francis I had enlarged the court), and the seven-leagues claim goes. Two changes break
  a rhyme (43, 47), which looks like careless copying or resetting rather than the poet's own revision.
  Who revised it, Corrozet or the publishers, the text cannot tell.
- **Caveats.** (1) Only the second 1532 edition was compared. The *Fleur* was reprinted at least eight
  times to 1555 (Lacroix's preface lists 1532, 1532, 1533/34, 1534, 1535, 1543, 1555); the map's
  readings (fourteen gates, six score) may already be in a later edition. Lacroix's appendix of
  first-edition variants lies beyond the part of the OCR we could read. (2) The 1550 *Antiquitez*:
  the owner also uploaded a Gallica PDF of it (bpt6k1510886x, 141 MB), but it has no text layer the
  connector can read; not checked.
- **Placement in the book:** the acrostic stanza and the poem come after the prose chapters and before
  the epigram on the name of Paris, the “Blason des armes de la ville de Paris” (ending with Corrozet's
  motto “Plus que moins”) and the list of streets, churches and colleges. Cousin's “le poème final qui
  termine et résume la Fleur” is fair: it is the last long poem.
- **“Blason de Paris”**: no poem of that name. The *Fleur*'s own “Blason des armes de la ville de
  Paris” (10 lines, on the ship of the city's arms) is not on the map.

**Verdict.** Cousin was right: the map's poem is Corrozet's “Louenges de Paris” from the *Fleur des
antiquitez*, with its acrostic stanza. Confidence: high (whole text compared; OCR of a reprint).

**Still open:** which edition the map's text was taken from (the later *Fleur* editions, 1533–1555, and
the 1550 *Antiquitez*); the first edition's variants (Lacroix's appendix).

## 4. Corrozet's role

What the evidence supports, from strongest to weakest:

1. **He wrote the verses**: certain; the poem is in his own book under his name (“Le nom et surnom de
   laucteur”, “Louenges de Paris faictes par ledict aucteur”). But it was printed there in 1532, so the
   verses show authorship of the poem, not involvement in the map: the publishers could have reprinted
   them from his book. The revisions (fourteen gates, six score councillors) show someone updated the
   text for the map, or used a later edition; that someone may or may not be Corrozet.
2. **Map and book were sold together, or at least bought together**: Amerbach bought the map in Paris
   (1557 or 1558, per Cousin and Sieber) with a 1550 *Antiquités*; Zwinger's *Methodus apodemica*
   follows the map's names. Evidence for joint purchase by one buyer; “sold together as a pair” is an
   inference.
3. **Patronage / published under Corrozet's auspices, sold in his shop at the Palais**: Cousin's
   inference (“nous pouvons en conclure”, “sans craindre de nous tromper”), no document cited. Plausible,
   not proven. Corrozet's shop was indeed at the Palais (Cousin; his imprints), but no imprint, contract
   or inventory ties the map to it. The map itself names only Truschet and Hoyau as its publishers.
4. **A 1553 commission from Corrozet** (French Wikipedia): **a source is named, and we have not read
   it.** Wikipedia cites Françoise Vergneault-Belmont, *Lire l'espace penser la carte* (L'Harmattan,
   2008), p. 168, and a second footnote identifies the man as “Gilles Corrozet, éditeur”. No such
   document is mentioned by Cousin, nor in HOC ch. 48 or ch. 53, the Sénat brochure or the Institut
   Paris Région page — all now read in full. So the claim is **unverified, not unsourced**: it stands or
   falls on Vergneault-Belmont p. 168, which is the next thing to read. Note that Lepape independently
   dates the *publication* to 1553, also without giving a document, so the date itself is not
   Wikipedia's invention.

One tension — which Dérens, we now find, has already answered (see §2: on his account the 1550
*Antiquitez* is the thinner book precisely *because* the map took over what the *Fleur* used to carry,
which argues for the companion-piece reading rather than against it): Corrozet had disowned the
*Fleur* by 1550 as a “petit livret” full of “erreurs et fables” (his words, quoted by Lacroix and
Cousin), yet the map, supposedly a companion to the new *Antiquités*, prints the old book's poem. That fits a cheap reuse of available verses
by Truschet and Hoyau at least as well as a planned companion piece.

## Sources

Read in full (repository, the owner's Drive, and — 29 Oct 2026 — the Internet Archive):
- Gilles Corrozet, *La fleur des antiquitez de la noble et triumphante ville et cité de Paris*, second
  edition (Galiot du Pré, 1532), ed. P. Lacroix (“le bibliophile Jacob”), Paris, 1874; Gallica
  ark:/12148/bpt6k6487221d. OCR text from Google Drive's index, PDF pages 1–132 (preface, text, poem
  on PDF pp. 102–106, street list); not the appendix.
- The **same 1874 reprint on the Internet Archive**, `lafleurdesantiqu00corr`, whose OCR keeps the
  **printed** page numbers that the Gallica text layer lost (Gallica itself answers `403` to automated
  requests). Edition confirmed from its own title page. **The poem is at printed pp. 64–67**: p. 64
  carries “Le nom et surnom de lauctenr” and the acrostic stanza, p. 67 ends the *Louenges*, and p. 68
  opens with the “Épigramme sur le nom de Paris” and the “Blason des armes”. The texts page currently
  cites “pp. 64–68”, one page too many.
  https://archive.org/stream/lafleurdesantiqu00corr/lafleurdesantiqu00corr_djvu.txt
- Jules Cousin, “Notice sur un plan de Paris du XVIe siècle nouvellement découvert à Bâle”, *Mémoires
  de la Société de l'histoire de Paris et de l'Île-de-France*, t. I (1875), pp. 46–59, OCR in
  `data/research/cousin_1875_notice.txt` (Gallica ark:/12148/bpt6k6310467r, f54–f67).
- The poem and notice as transcribed in `scripts/make_texts_page.py`; panel crops `data/map_texts/`.

Opened and read, 29 Oct 2026 (previously search extracts only; see `quote_verification.md`):
- Wikipédia (fr), “Plan de Truschet et Hoyau” (and its mirror on wikimonde.com).
- Sénat, Bibliothèque, *Paris : représentations et plans anciens* (brochure-02.pdf).
- *History of Cartography* vol. 3, ch. 48 (“National Mapmaking from Oronce Fine to Guillaume Postel”)
  and ch. 53 (C. Hofmann, “Publishing and the Map Trade in France, 1470–1670”), press.uchicago.edu PDFs.
- English Wikipedia, “Gilles Corrozet” — the one fact the site takes from it, Corrozet's dates
  1510–1568, no longer depends on it: the BnF metadata page of the Gallica *Fleur* scan reads
  “Corrozet, Gilles (1510-1568). Auteur du texte.”
  (`data/research/sources/corrozet_fleur_des_antiquitez_bpt6k6487221d.txt`, line 27);
  Institut Paris Région page on the plan; WorldCat / AbeBooks
  records of Dérens 1980; fabula.org notice of *En lisant, en écrivant* (Corrozet colloquium); Scripta
  Manent (huma-num) record of “Blason des armes de la ville de Paris”.

Not seen at all: Boutier 2002; Dérens 1980; any original edition of the *Fleur* or the *Antiquitez*.

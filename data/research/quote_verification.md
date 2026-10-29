# Verification of the flagged quotes and search-extract claims

Verification pass, 29 October 2026 (cloud session, branch `verify-research-quotes`). Scope: the claims
flagged as unverified in `corrozet.md`, `print_shop.md` and `open_questions_research.md`.

Every source below was **opened and read**, not searched. Quotations are copied from the page, the PDF or
the wikitext. Where a source could not be opened, the claim stays unverified and says so.

## Summary

| Verdict | Claims |
|---|---|
| **Confirmed** | **57** |
| **Partly confirmed** | **8** |
| **Contradicted** | **4** |
| **Still unverified** | **4** |
| Total | 73 |

### The four contradicted claims

1. **The Sénat brochure quotation does not exist** (A2). `corrozet.md` attributes to the Sénat library
   brochure a sentence about the plan de Bâle "dont Gilles Corrozet a probablement patronné l'édition pour
   servir d'annexe à ses Antiquitez de 1550". The brochure is 12 pages, every page carries a text layer,
   and it contains no such sentence — no "plan de Bâle", no "patronné", no "1551", no "annexe". Its only
   mention of the map is a bare picture caption. **Nothing should be cited to this brochure.**
2. **French Wikipedia's 1553 sentence does carry a reference** (A1). `corrozet.md` says it has "no
   reference", and reads "un certain Corrozet" as showing the writer had not identified him. Both are
   wrong: the sentence carries two footnotes, one of which identifies him outright as "Gilles Corrozet,
   éditeur", and the other cites Vergneault-Belmont 2008, p. 168. **This is on the live site.**
3. **Lazare's "actes de 1290, 1330, 1352 et 1406" belong to a different street** (F11).
   `open_questions_research.md` presents them as an addition to the *Verdelet* entry. They are Lazare's
   separate ***Verderet*** entry — another street altogether, 400 m away.
4. **Alain de Mathonière was installed at the Corne de Daim in 1557, not 1577** (E7). French Wikipedia's
   1577 is internally impossible (it also has him dying in 1572); Lepape has 19 January 1557.

### The four still unverified

- **B10** the texts page's "pp. 64–68" for the poem in Lacroix 1874 — gallica.bnf.fr returns `403` to
  automated requests and no printed page numbers survive in the OCR.
- **A5** Boutier 2002 and **A7** the Corrozet colloquium volume — print only.
- **E20 (part)** Grivel 2015's issue and pagination; **F19** Lazare on the rue des
  Francs-Bourgeois-Saint-Marcel (not on Wikisource).
- **E1** the FranceArchives record itself sits behind a JavaScript/cookie wall. Its substance was
  nevertheless settled from Lepape, who gives the inventory's date: **2 November 1547**.

### Two traps worth recording

- **Near-identical titles, as with the tome-3/tome-10 mix-up.** French Wikipedia's *Rue Verderet
  (ancienne voie de Paris)* **conflates two distinct Lazare entries**: it takes *Verderet*'s situation
  (Grande-Truanderie → Mauconseil, 89 m, quartier Montorgueil) and *Verdelet*'s history (1311 Breneuse,
  Pagevin and Petit-Reposoir opposite). *Rue Merderet* and *Rue Verderet (ancienne, Paris)* both redirect
  to it, so there is no way to land on the right article by name. **Do not "correct" L0421 to match
  Wikipedia** — Lazare and the Archives nationales both support what the project already has.
- **Chapters of one book can disagree.** *History of Cartography* vol. 3 dates this map **1550** in
  chapter 48 (Pelletier, following Dérens) and **ca. 1553** in chapter 53 (Hofmann). Citing "HOC" for a
  date without the chapter is meaningless.

### Confirmed from its own title page (the wrong-volume check)

`data/research/sources/corrozet_fleur_des_antiquitez_bpt6k6487221d.txt` is Lacroix's 1874 reprint of the
1532 *Fleur*: `PAR / GILLES CORROZET (1532) / PUBLIÉE / PAR / LE / BIBLIOPHILE JACOB / PARIS /
LIBRAIRIES: LÉON WILLEM, 8 RUE DE VERNEUIL / PAUL DAFFIS, 7 RUE GUÉNÉGAUD / 1874` (Gallica viewer p. 9).
Both *History of Cartography* PDFs were likewise confirmed from their own first pages, not from the URL:
ch. 48 = "48 • National and Regional Mapping in France to About 1650", **Monique Pelletier**; ch. 53 =
"53 • Publishing and the Map Trade in France, 1470–1670", **Catherine Hofmann**.

---

## Group A — `corrozet.md`, "Later literature" (lines 116–140)

| # | Claim (file:line) | Verdict | What the source says | Read at |
|---|---|---|---|---|
| A1 | fr.wikipedia "Plan de Truschet et Hoyau": « Ce plan est une commande datée de 1553 d'un certain Corrozet… »; **and** that the sentence has no reference, and that "un certain Corrozet" shows the writer did not connect him with Gilles Corrozet — `corrozet.md:117–120` | **Partly confirmed / partly contradicted** | The quotation is **exact**. But the sentence carries **two footnotes**: on "Corrozet", `<ref>Gilles Corrozet, éditeur (cf. infra, p. 169)</ref>`; at the end, `<ref>Françoise Vergneault-Belmont – ''Lire l'espace penser la carte'' – p. 168</ref>` (L'Harmattan, 2008, ISBN 978-2-296-07831-4). So the reference exists, **and Wikipedia identifies him as Gilles Corrozet the publisher**. No acrostic anywhere in the article — that part holds. | fr.wikipedia.org/w/index.php?title=Plan_de_Truschet_et_Hoyau&action=raw |
| A2 | Sénat brochure: the plan de Bâle (c. 1551) « dont Gilles Corrozet a probablement patronné l'édition pour servir d'annexe à ses Antiquitez de 1550 » — `corrozet.md:121–124` | **Contradicted** | **No such sentence in the brochure.** All 12 pages carry a text layer (page 1 is the cover image). Searching the whole text for "patron", "1551", "annexe", "Bâle" returns nothing of the kind. The only mention of the map is the caption `Plan de Paris sous le règne de Henri II, par Olivier Truschet et Germain Hoyau. Reproduit en fac-similé d'après l'exemplaire unique de la Bibliothèque de Bâle, par M. F. Hoffbauër (1877)`. Corrozet appears only as the author of the 1532 *Fleur*, behind Bonfons's 1608 reissue. | senat.fr/fileadmin/import/files/fileadmin/Fichiers/Images/archives/brochures-bibliotheque/brochure-02.pdf |
| A3 | HOC vol. 3 ch. 48: the Paris map and *Les antiquitez* "were sold together, as confirmed by their joined use by Theodore…" — `corrozet.md:125–128` | **Confirmed** | « The Paris map and *Les antiquitez* were sold together, as confirmed by their joined use by **Theodore Zwinger** in his *Methodus apodemica* (Basel, 1577). » The guess "presumably Theodor Zwinger" was right. The chapter is **Monique Pelletier**'s (the Fine-to-Postel section heading sits inside it). | press.uchicago.edu/books/HOC/HOC_V3_Pt2/HOC_VOLUME3_Part2_chapter48.pdf, **p. 1500** |
| A4 | Hofmann, HOC ch. 53: the eight-sheet plan "was cut in 1553 by Olivier Truschet and Germain Hoyau"; no Corrozet — `corrozet.md:129–130` | **Confirmed** | Both halves are there, in two places: « Except for the famous eight-sheet plan of Paris, **published** by Olivier Truschet and Germain Hoyau **ca. 1553** », and, of the 1598 Mathonière inventory, « it was probably the one **cut in 1553** by Olivier Truschet and Germain Hoyau ». Corrozet does not appear in the chapter. | HOC ch. 53, **p. 1572** |
| A5 | Boutier 2002 dates the plan c. 1553; unknown whether it discusses the acrostic — `corrozet.md:131–132` | **Still unverified** | Print only; not online. | — |
| A6 | Dérens 1980 (Zürich facsimile commentary) links map and *Fleur* — `corrozet.md:133–134` | **Partly confirmed** | HOC ch. 48 n. 80 gives the full citation — « Jean Dérens, *Le plan de Paris par Truschet et Hoyau, 1550, dit plan de Bâle* (1980; reprinted Paris: Rotonde de la Villette, 1986) » — and summarises his argument: the 1550 *Antiquitez* is a **less** detailed guide than the 1543 *Fleur* « because, according to Dérens, the Truschet-Hoyau map, which came out that same year, rendered some information included in the late *Fleur des antiquitez* useless ». Note the title dates the plan **1550**. The commentary itself was not read. | HOC ch. 48, p. 1500 and n. 80 |
| A7 | Corrozet studies (Chiron, Godet & Tran; the Persée article) say nothing about the map — `corrozet.md:135–137` | **Still unverified** | Not opened. | — |
| A8 | "No later source found discusses the acrostic itself" — `corrozet.md:139–140` | **Confirmed for every source now read** | The acrostic appears in none of: fr.wikipedia "Plan de Truschet et Hoyau", en.wikipedia "Gilles Corrozet", the Sénat brochure, HOC ch. 48, HOC ch. 53, the Institut Paris Région page. Cousin remains the only writer known to point it out. | all of the above |

> **A6 bears on `corrozet.md` §4.** The note offers, as "our observation, not in the literature seen",
> the tension that Corrozet had disowned the *Fleur* by 1550 yet the map prints its poem. Dérens has a
> published account of exactly this relationship, reported by Pelletier: the 1550 *Antiquitez* is thinner
> **because the map took over** what the *Fleur* used to carry. That is an argument for the
> companion-piece reading, and the note should stop presenting the observation as unanswered.

---

## Group B — `corrozet.md`: the *Fleur* OCR and English Wikipedia

Quotations from `data/research/sources/corrozet_fleur_des_antiquitez_bpt6k6487221d.txt` (OCR of Lacroix
1874, Gallica ark:/12148/bpt6k6487221d), cited by the Gallica viewer page markers the file carries.

| # | Claim | Verdict | What was found | Where |
|---|---|---|---|---|
| B1 | Corrozet's dates are 1510–1568 (site `web/index.html:124`, `web/texts/index.html:160`) | **Confirmed twice** | BnF metadata: `Corrozet, Gilles (1510-1568). Auteur du texte.` English Wikipedia is sharper: « Gilles Corrozet (**4 January 1510 - 4 July 1568**, Paris) ». | OCR file line 27; en.wikipedia "Gilles Corrozet" |
| B2 | The OCR is Lacroix's 1874 reprint of the 1532 *Fleur* | **Confirmed from the title page** | See the quotation above. | Gallica viewer p. 9; file lines 134–156 |
| B3 | The fourteen acrostic lines stand under "Le nom et surnom de laucteur" | **Confirmed** | `Le nom et surnom de laucteur.` then 14 lines, `Gentilz lecteurs…` to `Totallement dire dune cite.`, initials G I L L E S C O R R O S E T. | viewer p. 102; file 7189–7211 |
| B4 | The poem is headed "Louenges de Paris faictes par ledict aucteur" | **Confirmed** | `Louenges deParisfaictesparledict` / `aueteur.` (OCR for *aucteur*). | viewer p. 102; file 7229–7233 |
| B5 | Book "Nostre cite" vs map "Noble cite" (line 15) | **Confirmed** | `Nostre cite et ville tantexquise` | viewer p. 102; file 7233 |
| B6 | Book "structure" vs map "stature" (line 2) | **Confirmed** | `Ioyeulx esprits regardez la structure` | viewer p. 102; file 7193 |
| B7 | Book "cent hommes" vs map "six vingtz" (line 80) | **Confirmed** | `Et sainct senat ou sont les conseillers` / `En nombre centhommes tressinguliers` | viewer p. 105; file 7419–7421 |
| B8 | The "Épigramme sur le nom de Paris" spells PARIS | **Confirmed** | `Pour pris dhonneur…` / `Accroissementde tout bien…` / `Roch de vertu…` / `Iustice vraye…` / `Scauoir de tout estude…`, closing `Cest de Paris le tiltre de noblesse.` | viewer p. 106; file 7497–7513 |
| B9 | The "Blason des armes" is 10 lines and ends with the motto *Plus que moins* | **Confirmed** | 10 verse lines, `La nef voguant dessus la mergallicque` → `Cest de Paris le beau blason des armes.`, then `Plusquemoins.` | viewer p. 106; file 7517–7545 |
| B10 | The texts page cites the poem as **"pp. 64–68"** of Lacroix 1874 (`web/texts/index.html:215`) | **Still unverified** | gallica.bnf.fr answers `403` to automated requests, and no printed page number survives anywhere in the OCR. The poem occupies viewer pp. 102–106 — five pages, as "64–68" is five pages, consistent with a constant offset of 38, but that is arithmetic, not a reading. | — |
| B11 | English Wikipedia "Gilles Corrozet" as a source on the map | **Note** | The article **never mentions the map, Truschet or Hoyau**. It is good for his life and trade only. It gives the *Fleur* 1532 as his first published work, and has his daughter marrying Nicholas Bonfons, who later reissued it. | en.wikipedia.org |

---

## Group C — `print_shop.md`, the †-marked facts

11 † characters: 9 on facts (the same three sentences in English, French and Swedish) and 2 in the prose
legend at lines 177 and 231. They cover six distinct claims. **All six are now confirmed**, one with a
correction.

| # | Claim (file:line) | Verdict | What the source says | Read at |
|---|---|---|---|---|
| C1 | Nicolas Prévost was "installé rue Montorgueil au Chef Saint-Denis, où il se trouvait en **1571**" — `print_shop.md:85–88`, 189/203/219 | **Confirmed** | « Nicolas Prévost (vers 1535/1540-vers 1599) … Les actes le désignent comme peintre en papier, imprimeur d'histoires et imagier. Il est **installé rue Montorgueil au Chef Saint-Denis, où il se trouvait en 1571** (taxé 60 sols au don de 300 000 livres, voir *Dictionnaire des éditeurs…*, p. 267-268). » The documentary basis is the 1571 Paris tax roll — firmer than Cousin's inference from undated prints. | books.openedition.org/editionsbnf/2414 ("Prévost") |
| C2 | Lepape: the house "était en **1553** le lieu d'édition de Truschet et Hoyau pour le Plan de Paris"; **and** a contents entry "Germain Hoyau au Chef Saint-Denis en 1553" — `print_shop.md:87–92` | **Confirmed / the contents entry contradicted** | The sentence is exact, and Lepape repeats the date three more times: Truschet's biography, « où il **publia en 1553** avec Germain Hoyau le fameux plan de Paris (cat. 228) »; Hoyau's, « un plan de Paris (aujourd'hui conservé à Bâle), **que l'on date de 1553** »; the signs list, « Germain Hoyau et Olivier Truschet y publièrent le Plan de Paris en 1553 ». **But the table of contents has no such entry** — only "Les Hoyau et Nicolas" and "Truschet". And in none of the readable parts does Lepape say *which document* carries the 1553 date; "que l'on date de 1553" reads as received opinion. | editionsbnf/2414, /2418 (p. 306-308), /2441 (p. 136-168), /2393 (p. 345), /2341 |
| C3 | Truschet, *Carte de la cité de Guînes*, **1559** — `print_shop.md:118`, 190/206/220 | **Confirmed** | « 1559 *Carte de la cité de Guînes*, par Olivier Truschet. » | editionsbnf/2395, p. 349-350 |
| C4 | Truschet, *Carte de France, d'Allemagne et d'Italie* after Jean Jolivet, **1560** — `print_shop.md:118–119`, 190/206/220 | **Confirmed** | « 1560 *Carte de France, d'Allemagne et d'Italie* **de Jean Jolivet, par Olivier Truschet**. *Monstre découvert dans le Berry*, par Olivier Truschet. » The title is exactly as the note has it. **A fourth Truschet work the note missed: *Monstre découvert dans le Berry*, 1560** (cat. 592), published with Richard Breton. Note HOC ch. 53 names a *different* 1560 Jolivet map published by Truschet, *Nouvelle description des Gaules*. | editionsbnf/2395; /2418 |
| C5 | Hoyau bought a share of the Bon Pasteur in **1563** and **1566** — `print_shop.md:99`, `122`, 192/207/222 | **Confirmed** | Signs list: « appartenait en copropriété à François Desprez, Olivier Truschet et Richard Breton jusqu'en 1563, date à laquelle **Germain Hoyau en acheta un sixième, puis un autre sixième en 1566** ». Hoyau's biography gives the act: propriétaire « **depuis le 25 octobre 1563 d'un sixième** … que lui vendirent François Desprez et sa veuve pour **180 livres tournois**. L'acte d'ensaisinement eut lieu le **17 avril 1564** (AN, S* 1214) ». | editionsbnf/2393; /2441 |
| C6 | Hoyau was still alive in **1572** — `print_shop.md:125–126`, 192/207/222 | **Confirmed** | « Germain, baptisé le **19 novembre 1572**, dont le parrain fut **Germain Hoyau, son grand-père maternel** » (Fichier Laborde Mss.; *Dictionnaire des éditeurs…*, p. 135-136). | editionsbnf/2423, p. 92-94 |

---

## Group D — `print_shop.md`: Cousin, from the repository

| # | Claim | Verdict | Quotation | Where |
|---|---|---|---|---|
| D1 | Cousin puts the Chef Saint-Denis in Prévost's hands c. 1572 | **Confirmed** | « Ces planches datent de 1572 ou environ; […] La maison du Chef Saint-Denis, sans doute liquidée après la mort de Truschet, **appartient alors à Nicolas Prévost**. » He says the house *belonged to* him, not that he printed there, and gives no year for Truschet's death. | Cousin p. 53; `cousin_1875_notice.txt:315–321` |
| D2 | The neighbouring signs c. 1572 | **Confirmed** | « la maison de l'Échiquier, à Marin Bonnemer et Clément Boussy; la Corne de Daim, à Denis de Mathonière; l'Espinette, à Jean Boussy; l'image Saint-Pierre, à Ch. Levigoureux; la Corne de Cerf, à Marin Boussy, etc., etc., toute une colonie d'imagiers. » | same, `:321–326` |
| D3 | Hoyau signed prints with Mathurin Nicolas at the Bon Pasteur; Truschet's signature gone | **Confirmed** | « nous n'y retrouvons plus la signature d'Olivier Truschet … mais Germain Hoyau en a signé plusieurs en compagnie de Mathurin Nicolas son nouvel associé à l'enseigne du Bon Pasteur. » | same, `:315–319` |
| D4 | They were not booksellers; Cousin checked Lottin | **Confirmed** | « Ce ne sont pas des libraires; je l'ai vérifié sur le catalogue de Lottin. » | Cousin p. 52; `:297–298` |
| D5 | Cousin's table has Comte-d'Artois as an entry distinct from Montorgueil | **Confirmed** | `COMTE-D'ARTOIS (rue au) \| R. Conte Dartois \| VI,1 \|` and `MONTORGUEIL (rue de) \| \| VI,1;V,3 \|` | `cousin_1875_table.txt:109`, `:256` |
| D6 | The map itself labels the southern stretch separately | **Confirmed** | `L0378,R. DE MONTORGUEIL,…,2870,4930` and `L0381,R. CONTE DARTOIS,…,3160,4930` | `data/labels_inventory.csv` |

---

## Group E — `print_shop.md`, the other extract-based facts

| # | Claim (file:line) | Verdict | What the source says | Read at |
|---|---|---|---|---|
| E1 | FranceArchives record of the Boussy/Clément inventory — **cote and date never seen** — `:43`, `:104` | **Partly confirmed** (record unreachable, substance settled) | The FranceArchives page is behind a JavaScript/cookie wall and was not opened. **Lepape supplies the facts**: « Le premier éditeur installé rue Montorgueil serait **Jean Ier Boussy ( ?-1547)**. Il épousa le **28 septembre 1542 Michèle Clément** (MC, CXXII, 1156). … En 1547, le couple est documenté rue Montorgueil, **à l'enseigne de la Cuillère. L'inventaire après décès de leurs biens, réalisé le 2 novembre 1547**… » **This also resolves the note's Cuillère/Espinette puzzle**: Lepape distinguishes Jean Ier (d. 1547), Jean II and Jean III Boussy. Cousin's c. 1572 Jean Boussy at the Espinette is Jean II — a different man. Grivel 2015 is not needed. | editionsbnf/2433, p. 40-57 |
| E2 | AN register: the rue des Petits-Carreaux was "until the early 17th century confused with the rue Montorgueil" — `:68–69` | **Confirmed** | « Elle existait au XIIIe siècle. **Jusqu'au début du XVIIe siècle, elle a été confondue avec la rue Montorgueil.** » | rdf.archives-nationales.culture.gouv.fr/place/FRAN_RI_025-d3nzchekdc-1oaf022uugsgq |
| E3 | "rue des Petitz Carneaulx" first in a manuscript of 1636 — `:70–71` | **Confirmed** | « Initialement partie de la rue Montorgueil, elle devient une rue à part entière au XVIIe siècle. Elle est citée sous le nom de « **rue des Petitz Carneaulx** » dans un manuscrit de **1636** » | fr.wikipedia "Rue des Petits-Carreaux" |
| E4 | AN register: in 1637 the stretch neighbouring the rue Poissonnière was the "rue des Boucheries" — `:71–72` | **Confirmed** | « **En 1637, la partie voisine de la rue Poissonnière était appelée rue des Boucheries.** » (fr.wikipedia describes the same stretch from the other end — the northern part, after the butchers' stalls at no. 43.) | same AN record |
| E5 | Porte au Comte d'Artois ordered demolished December 1498; street joined to the rue Montorgueil in 1792 — `:58–62`; **on the site** | **Confirmed, and sharpened** | Lazare, "Montorgueil (rue)": « La première partie de cette voie publique qui prend naissance à la Pointe-Saint-Eustache, et **se termine à la rue Mauconseil** … se nommait anciennement rue du *Comte-d'Artois* … Elle tirait ces dénominations de **Robert II, comte d'Artois**, neveu de saint Louis … la Ville ordonna, le **17 décembre 1498**, de la démolir. **En 1792 la rue Comtesse-d'Artois fut confondue avec la rue Montorgueil.** » This also confirms the **rue Mauconseil** as the southern limit — the structural claim of §1 and of the site's "Where was the shop?". | fr.wikisource, Lazare 1844 djvu **p. 470** |
| E6 | Charles V's wall had six original Right-Bank gates, none at Montorgueil — `:76–78` | **Confirmed** | « L'enceinte ne comprend à l'origine que **six portes** … » then Saint-Honoré, Montmartre, Saint-Denis, Saint-Martin, Temple, Saint-Antoine. (A seventh, the porte Neuve, opened in 1536.) | fr.wikipedia "Enceinte de Charles V" |
| E7 | Alain de Mathonière owner outright from 13 Oct. 1565, **installed from 19 Jan. 1577**; Denis's 1598 inventory lists two large presses and a typographic press — `:101` | **Contradicted on the date** | Lepape: « Alain de Mathonière (**vers 1525-1575**) … Il est installé rue Montorgueil, à la Corne de Daim, **depuis le 19 janvier 1557 au moins**. Il était alors en partie propriétaire et le devint complètement le **13 octobre 1565**. » French Wikipedia's "19 janvier 1577" is both wrong and self-contradictory (it has Alain dying in 1572). The 1598 inventory is **confirmed**: « deux grandes presses pour imprimer et une presse typographique avec cinq paires de casses », drawn up 2 April 1598. | editionsbnf/2452, p. 181-205; fr.wikipedia "Denis de Mathonière" |
| E8 | Fonteney/Fontenoy (d. 1583) given the Corne de Daim though his prints say only "près l'Échiquier" — `:101` | **Confirmed** | « Denis Fonteney ou Fontenoy ( ?-1583) … Il était établi rue Montorgueil, **à la Corne de Daim**, à la même enseigne que celle des Mathonière, mais les suites qu'il édita ne précisent pas son enseigne, se contentant de signaler qu'il est **près l'Échiquier**. On peut dès lors se demander s'il avait vraiment une boutique à cet endroit. » | editionsbnf/2434, p. 78-91 |
| E9 | Guillaume Saulce at the Espinette — `:103` | **Confirmed** | « Guillaume Saulce ( ?-1582) … Il est installé rue Montorgueil **à l'enseigne de l'Espinette**. » (HOC ch. 53 puts Nicolas Lefebvre there in 1555, Cousin puts Jean Boussy there c. 1572 — successive holders, not a conflict.) | editionsbnf/2417, p. 300-305 |
| E10 | Fonteney's daughter baptised at Saint-Eustache, 29 May 1579 — `:108–109` | **Confirmed** | « Il épousa Jeanne Valet, dont il eut au moins une fille, Jeanne, **baptisée à Saint-Eustache le 29 mai 1579**. » | editionsbnf/2434 |
| E11 | 24 Aug. 1564: Godet sells Hoyau, Desprez and Nicolas twelve Months woodblocks for 200 livres tournois — `:122–124` | **Confirmed, with the contract's words** | « Le **24 août 1564**, Gilles Godet vendit en effet à Germain Hoyau, François Desprez et Mathurin Nicolas "douze pl. de bois esquelles sont gravés les douze moys, servant pour l'imprimerie, **pour 200 livres tournois**. Godet pouvait imprimer à ses dépens ces planches à hauteur de soixante rames de papier, mais seulement celles dont l'escripture … faicte selon le vulgaire angloys…" » Godet was a Parisian imagier **settled in London**. | collections.louvre.fr/en/ark:/53355/cl020519735 |
| E12 | "La veuve de Germain Hoyau" died in 1585; Hoyau died between 1572 and 1585 — `:125–126` | **Confirmed, and superseded** | The widow's death is exact: « après la mort de **la veuve de Germain Hoyau, en 1585** ». But Hoyau's own death no longer needs a bracket: Lepape heads his biography « Germain Hoyau ( ?-**1583**) », the signs list says « mort en 1583 », the Louvre record credits « (vers 1518-1583) » after Lepape, and HOC gives « ca. 1525–83 ». | editionsbnf/2414, /2441, /2393; Louvre; HOC ch. 48 p. 1500 |
| E13 | Truschet was dead by 1575 — `:129`; **on the site** | **Confirmed, and superseded** | The 1575 statement is right and its basis is exact: « en 1575, dans le censier de l'archevêché de Paris, la maison du Bon Pasteur était toujours la propriété d'Hoyau, Desprez et Olivier Truschet (**Grivel 2008, p. 21**, signalant que le nom de Truschet est une erreur, car il était mort à cette époque) ». But Lepape dates his death far earlier: « **Olivier Truschet ( ?-vers 1561/1564)** », and the signs list « mort entre 1561 et 1564 ». His widow was Thomasse Laloze. | editionsbnf/2445, /2418, /2393 |
| E14 | HOC calls Hoyau "imagier en papier" and draughtsman, Truschet the engraver — the reverse of fr.wikipedia — `:115–117`; **on the site** | **Confirmed** | « In his study on the map of Paris **drafted by Germain Hoyau (ca. 1525–83), imagier en papier (producer of prints) and drawer, and engraved by Olivier Truschet**, Dérens establishes a clear relation between this map of 1550 … and the Paris guide written by Gilles Corrozet… » | HOC ch. 48, p. 1500 |
| E15 | HOC: Guînes copied from a Nicolas de Nicolay manuscript; Truschet linked to a *Description de la haulte et basse Picardye*, c. 1559–60 — `:119–121` | **Confirmed, and extended** | « in addition to **a map of the city of Guînes (ca. 1559) copied from a manuscript by Nicolas de Nicolay**, Truschet published ***Description de la haulte et basse Picardye* (ca. 1559–60), attributed to Jean Jolivet**, and *Nouvelle description des Gaules* (1560) by Jolivet. » (Karrow, *Mapmakers of the Sixteenth Century*, 438–39, 322.) | HOC ch. 53, p. 1572 |
| E16 | Jeanne Hoyau, Hoyau's sister, married François Gence — `:124–125` | **Confirmed, with a wrinkle** | « Un premier François Gence a épousé Jeanne Hoyau, **qui serait selon Marianne Grivel la sœur de Germain Hoyau** (Grivel 2008, p. 5). » **But the same paragraph calls Germain Hoyau the "grand-père maternel" of her son**, which would make her his daughter. Lepape is internally inconsistent here; the hedge "qui serait selon" suggests she knew it. | editionsbnf/2423 |
| E17 | Lepape's index: "Veuve de Mathurin Nicolas: voir Hoyau (Catherine)"; relationship not seen — `:127–128` | **Confirmed and resolved** | The index has « **Hoyau (Catherine), veuve de Mathurin Nicolas** : 14, 76, 119, 132, 137, 143, 160, 347 » and the cross-reference. The relationship is in the Prévost chapter: Roland Guérard « épousa **sa fille Catherine** et récupéra une partie du matériel de Hoyau ». So Catherine Hoyau was **Germain Hoyau's daughter**, widow of his partner Mathurin Nicolas (d. 1580), then wife of Guérard (d. 1599). | editionsbnf/2421, /2414, /2393 |
| E18 | **The two extracts disagree: a sixth or a third?** — `:99` | **Resolved — both are right** | Desprez's chapter: « Desprez était propriétaire **d'un tiers** de la maison, qu'il vendit **en deux fois** à Germain Hoyau, d'abord en 1563 puis en 1566. » The signs list and Hoyau's biography give the two instalments as **a sixth each**. A third sold in two halves = two sixths. No conflict. | editionsbnf/2445, /2393, /2441 |
| E19 | 1575 censier lists Hoyau, Desprez and Truschet; Grivel takes Truschet's name as an error — `:99`; the censive point is **on the site** | **Confirmed verbatim** | See E13. Hoyau's own sixth is recorded in the « **registres d'ensaisinement de l'évêché de Paris** » (AN, S* 1214) — precisely the kind of source the note's "where to look next" recommends, and already cited. | editionsbnf/2445, /2441 |
| E20 | Bibliographic metadata from extracts — `:40`, `:41`, `:42`, `:50` | **Partly confirmed** | **Grivel 2008 confirmed**: HAL metadata gives *Documents d'histoire parisienne*, n° 9, 2008, p. 15-47, Marianne Grivel (Centre André Chastel). **HOC ch. 53 pp. 1569–1588 confirmed** (last page header reads 1588). **Lepape's ISBN confirmed** (978-2-7177-2656-5 print; 978-2-7177-2658-9 digital) but the page count is **364, not 361**, published 20 October 2016. **Grivel 2015 still unverified.** | shs.hal.science/halshs-00602821; HOC ch. 53; editionsbnf/2341 |

---

## Group F — `open_questions_research.md`

### L0007 "LE PONT ARCANS"

| # | Claim (file:line) | Verdict | What the source says | Read at |
|---|---|---|---|---|
| F1 | fr.wikipedia, *Liste des ponts de Paris*: « Pont Arcans : jeté sur le Grand Égout, il était situé entre le château des Porcherons et la Ville l'Évêque. » — `:19–21` | **Confirmed verbatim** | Exactly that, in the list of destroyed bridges. **No reference is attached** to the line — the note's suspicion was right. | fr.wikipedia "Liste des ponts de Paris" |
| F2 | *Paris pittoresque*, "Chaussée-d'Antin", after Lurine 1844: a poor bridge called the Pont-Arcans, cracked, ugly, no railings — `:22–25` | **Confirmed, exact wording recovered** | « Pour aller de la ville à ce lieu de perdition … avaient tracé un chemin sinueux qui, **partant de la porte Gaillon, aboutissait aux Porcherons**. Ce chemin … **enjambait, à l'aide d'un mauvais pont, un affreux égout** … qui s'appelait le ruisseau de Ménilmontant. Cette sentine et ce ruisseau sont le père et la mère de la rue de Provence. **Le pont, qui était fort vilain et fort crevassé, avait nom le Pont-Arcans. On avait oublié d'y mettre des garde-fous**, et on le passait à la grâce de Dieu. » The page header confirms the attribution: "(D'après *Les rues de Paris. Paris ancien et moderne*…, sous la direction de Louis Lurine, paru en 1844)". | paris-pittoresque.com/rues/100.htm |
| F3 | An unidentified French source: « fit disparaître le pont d'Arcans enjambant l'égout au niveau approximatif de la rue de la Chaussée d'Antin actuelle » — `:26–29` | **Confirmed and the source identified** | It is fr.wikipedia ***Ruisseau de Ménilmontant***: « Dans les années 1760, la ville autorisa les riverains à recouvrir le Grand Égout … Sur la couverture … de nouvelles rues furent ouvertes, notamment **la rue de Provence qui fit disparaitre le pont d'Arcans enjambant l'égout au niveau approximatif de la rue de la Chaussée d'Antin actuelle**, la rue des Petites-Écuries, la rue Richer… » | fr.wikipedia "Ruisseau de Ménilmontant" |
| F4 | English Wikipedia, *Menilmontant brook*, says the same — `:30` | **Confirmed** | « It is notably the Rue de Provence with an East-West route that covers the Great Sewer and **makes disappear the small *pont d'Arcans* (Arcans bridge). This bridge allowed to cross the Grand Sewer at approximate level of the rue de la Chaussée-d'Antin today.** » | en.wikipedia "Menilmontant brook" |
| F5 | Duplomb, *Histoire générale des ponts de Paris* (1911–13), lists it among the forgotten bridges over sewers — `:31–34` | **Confirmed; date corrected** | « Et puis il y a **les ponts oubliés**, disparus de notre paysage urbain qui furent établis sur divers cours d'eau, **égouts**, canaux et rivières … **Pont Arcans (sur le Grand Egout, ancien lit du ruisseau de Ménilmontant, entre le château des Porcherons, rue Saint Lazare et la Ville-l'Evêque)** ». The work is **"Paris, 1911. Deux volumes in-8 … 376-75 pp."** — 1911, not 1911–13. The "rue Saint Lazare" locator for the château is new. | blog.paris-libris.com |
| F6 | BnF CCFr: a folio "Pont Arcans" in Charles Sellier's notes — `:35–36` | **Confirmed and expanded** | Record "Pont Arcans"; establishment **Bibliothèque historique de la Ville de Paris**; "Fonds Sellier, Charles (1844-1912), historien"; **cote MS-2765 à MS-2783**; date vers 1870–vers 1910; 19 volumes. The holding library is the **BHVP**, not the BnF (CCFr is only the union catalogue). | ccfr.bnf.fr/portailccfr/ark:/16871/004a1965928 |
| F7 | The rue de Provence × rue de la Chaussée-d'Antin crossing is at about **48.8745 N, 2.3330 E** ("from memory, ±50 m") — `:42–44` | **Confirmed by measurement** | From OpenStreetMap, the two ways share nodes at **48.874303, 2.332751** and 48.874299, 2.332712. The remembered figure is **28 m** from it — well inside its own ±50 m. **The live pin (48.8755, 2.338845) is 465 m away**, not "about 420 m" as the note says. | openstreetmap.org API 0.6, bbox 2.3290,48.8720,2.3380,48.8780 |
| F8 | Label distances: L0007 is 641 px from L0462 and 1300 px from L0464 — `:38–40` | **Confirmed** | 641 px and 1301 px. | `data/labels_inventory.csv` |

### L0421 "R. BRENEUSE"

| # | Claim (file:line) | Verdict | What the source says | Read at |
|---|---|---|---|---|
| F9 | Lazare, "Verdelet (rue)": « En 1295, ce n'était qu'une ruelle étroite et puante hors des murs de l'enceinte de Philippe-Auguste. Elle se nommait alors rue Merderet. […] Plus tard, par altération, elle fut appelée rue Verderet, puis Verdelet. » — `:62–67` | **Confirmed verbatim** | Exactly so. And the entry's head settles the street: « Verdelet, rue. **Commence à la rue Jean-Jacques-Rousseau, n° 11 ; finit aux rues Coq-Héron et de la Jussienne, n° 2.** … Sa longueur est de **77 m**. — 3e arrondissement, quartier Saint-Eustache. » **That is exactly the junction the label sits in**, so the project's identification is right and now directly sourced. | fr.wikisource, Lazare 1844 djvu **p. 671** |
| F10 | The 1311 *rôle de la taille* calls it « rue Breneuse » — `:67–68` | **Partly confirmed** | Lazare: « **En 1311, on la trouve sous le nom de *Breneuse*, c'est-à-dire rue malpropre.** » The 1311 attestation holds. But Lazare **does not name the *rôle de la taille***; that attribution remains unsourced. | same |
| F11 | "A reprint of the same entry adds « Des actes de 1290, 1330, 1352 et 1406 l'indiquent sous les noms de Merderiau, Merderai, Merderel et Merderet »" — `:68–69` | **Contradicted as attributed** | The sentence is real but it is **Lazare's separate "Verderet (rue)" entry**, immediately after Verdelet on the same page: « Verderet, rue. **Commence à la rue de la Grande-Truanderie, nos 42 et 44 ; finit à la rue Mauconseil, nos 17 et 19.** … **89 m.** — 5e arrondissement, quartier Montorgueil. Des actes de 1290, 1330, 1352 et 1406, l'indiquent sous les noms de *Merderiau*, *Merderai*, *Merderel* et *Merderet*… » **A different street, ~400 m away.** Not a reprint variant. | same |
| F12 | AN register: « La rue Verdelet, qui était comprise entre les rues Jean-Jacques Rousseau et de la Jussienne, avait porté les noms de rue Mardelet ou Marderet (XIIIe siècle), Breneuse et enfin de rue Verderet ou Verdelet. » — and the note could not say which record — `:70–73` | **Confirmed verbatim; the record identified** | The quotation is exact, and it sits in record **vdp-3149, which is the *rue Pagevin* record** (vdp-3953 returns 404). Its full history note also reads: « Supprimé par l'ouverture de la rue Etienne Marcel et par l'agrandissement de l'Hôtel des Postes. Elle avait été formée, en 1849, par la réunion des rues Verdelet, Pagevin et du Petit Reposoir. … La rue Pagevin commençait rue de la Jussienne et finissait rue d'Argout. … La rue du Petit Reposoir était comprise entre la rue d'Argout et la place des Victoires ; elle avait aussi anciennement été dénommée rue Breneuse. » | rdf.archives-nationales.culture.gouv.fr/place/FRAN_RI_025-d3nzcc8smx--w2i8uceiz29c-vdp-3149 |
| F13 | fr.wikipedia has *Rue Verderet (ancienne voie de Paris)* and a separate *Rue Merderet*, sometimes confused — `:75–78` | **Contradicted, and the real problem is worse** | *Rue Merderet* and *Rue Verderet (ancienne, Paris)* are both **redirects** to one article. That article **conflates Lazare's two entries**: it takes *Verderet*'s situation (Grande-Truanderie → Mauconseil, 89 m, quartier Montorgueil, gone in 1866 with the rue Étienne-Marcel) and *Verdelet*'s history (1311 Breneuse; « Les rues Pagevin et du Petit-Reposoir **qui étaient en face** »). Those cannot both describe one street, and *Rue Pagevin* links to it for the street at Coq-Héron/Jussienne. **Wikipedia is wrong here; Lazare and the Archives nationales agree with the project.** | fr.wikipedia, four articles |
| F14 | *Nouvelle revue d'onomastique*, citing Lock 1867, puts "Orde rue" in 1311 and Breneuse after — `:79–81` | **Confirmed verbatim** | « à Paris, **la rue Merderel en 1295 prit le nom d'Orde rue en 1311 puis celui de rue Breneuse**, avant que Merderet ne se transforme en Verderet puis en Verdelet (**Lock 1867 : 292**). » The disagreement with Lazare is real and now documented on both sides; it does not affect the identification. | journals.openedition.org/nda/3928 |
| F15 | AN register gives Breneuse as an old name of the rue du Petit-Reposoir, renamed by a court ruling of 1582; it lay further west, towards the place des Victoires — `:84–86` | **Partly confirmed** | The register confirms the street and its position exactly (see F12): Petit-Reposoir ran from the rue d'Argout to the place des Victoires and was also called Breneuse. The three streets formed one chain — Verdelet, then Pagevin, then Petit-Reposoir — which is why all three carried the name. **The 1582 court ruling is not in the record**: still unsourced. | same AN record |
| F16 | AN register: the 1849 rue Pagevin vanished under the rue Étienne-Marcel and the Hôtel des Postes, so L0422's `CUR:rue d'Argout` may be wrong — `:98–102` | **Confirmed, but the inference needs care** | The disappearance is verbatim (F12). **However** the same record adds: « Cette dénomination correspond à **2 voies : actuelles rue Herold et rue d'Argout**. Voie supprimée. » So the register itself chains Pagevin forward to the rue d'Argout, which makes the project's match defensible. The real problem is the duplicate: L0419 (Vieux-Augustins) also lands on the rue d'Argout. fr.wikipedia adds that the merged street disappeared in **1880** and that the rue d'Argout is the former rue des Vieux-Augustins. | same; fr.wikipedia "Rue d'Argout", "Rue Pagevin" |
| F17 | Label distances for L0421 — `:86–89` | **Confirmed** | 186, 149, 197 and 220 px. | `data/labels_inventory.csv` |

### L0224 "R. NEUVE"

| # | Claim (file:line) | Verdict | What the source says | Where |
|---|---|---|---|---|
| F18 | Cousin: « NEUVE (rue), sans autre désignation \| IV,2 \| donnant dans la rue de la Barre au faub. St-Marcel » — `:106–107` | **Confirmed** | Exact; the note elides only the empty map-label column. Beware the neighbouring entry: `NEUVE (rue) \| R. Neueve \| VIII,4 \| à l'entrée du faubourg St-Germain` — a different street. | `cousin_1875_table.txt:266`, `:265` |
| F19 | fr.wikipedia: « rue Scipion (ancienne *rue de la Barre*, ouverte en 1540) » — `:114–115` | **Confirmed verbatim** | And a useful addition: the hôtel Scipion was built in 1565 for Scipion Sardini « dans le faubourg Saint-Marcel **rue de la Barre à l'angle de l'actuelle rue du Fer à Moulin** » — which is the corner the label sits beside. | fr.wikipedia "Faubourg Saint-Marcel (quartier de Paris)" |
| F20 | The *séjour d'Orléans* was divided into plots in **1541/1545**, opening the rues Censier and de la Clef — `:118–121` | **Partly confirmed** | « le séjour d'Orléans fut **loti en 1541** (ouverture des rues Censier et de la Clef) ». 1541 is right; **1545 does not appear in the source** and should be dropped. | paris-atlas-historique.fr/32.html |
| F21 | The rue des Francs-Bourgeois-Saint-Marcel's name dates from 1296 — `:122–125` | **Still unverified** | Not on Wikisource (404). | — |
| F22 | Lazare gives the rue du Fer-à-Moulin the earlier names « rue Richebourg » and « rue des Morts » — `:130–131` | **Confirmed, and it weakens the hypothesis** | « Selon Sauval, elle a pris aussi la dénomination de rue de ***Richebourg*** … En 1713, cette rue divisée en deux parties avait deux dénominations : la première partie … se nommait rue ***des Morts***, parce qu'elle longeait le cimetière de Clamart ; la deuxième partie s'appelait rue *Permoulin* ». It also carried *Comte-de-Boulogne*. **None of its documented names is "Neuve"**, so hypothesis 2 is weaker than the note allows. | fr.wikisource, Lazare 1844 djvu **p. 220** |
| F23 | Label distances for L0224 — `:109–111` | **Confirmed** | 168, 209 and 285 px. | `data/labels_inventory.csv` |

---

## Sources opened in this pass

fr.wikipedia (Plan de Truschet et Hoyau; Liste des ponts de Paris; Ruisseau de Ménilmontant; Rue des
Petits-Carreaux; Enceinte de Charles V; Denis de Mathonière; Rue Verderet (ancienne voie de Paris); Rue
Verderet; Rue Merderet; Rue Pagevin; Rue d'Argout; Faubourg Saint-Marcel) · en.wikipedia (Gilles
Corrozet; Menilmontant brook) · Sénat, *Paris : représentations et plans anciens*, brochure-02.pdf ·
*History of Cartography* vol. 3 ch. 48 (Pelletier) and ch. 53 (Hofmann), press.uchicago.edu PDFs ·
Lepape, *Gravures de la rue Montorgueil*, OpenEdition chapters 2341, 2393, 2394, 2395, 2414, 2417, 2418,
2421, 2423, 2433, 2434, 2441, 2445, 2452 · Archives nationales street register, records
d3nzchekdc-1oaf022uugsgq and vdp-3149 · Lazare 1844 on fr.wikisource, djvu pp. 220, 470, 518, 671 ·
Institut Paris Région · Louvre collections cl020519735 · HAL halshs-00602821 ·
journals.openedition.org/nda/3928 · paris-pittoresque.com/rues/100.htm · blog.paris-libris.com ·
ccfr.bnf.fr · OpenStreetMap API · and, in the repository, Cousin's notice and table and the *Fleur* OCR.

**Could not be opened:** gallica.bnf.fr (`403` to automated requests — its own anti-bot, not the network
policy); francearchives.gouv.fr (JavaScript/cookie wall); api.archives-ouvertes.fr (not in the allowed
domains; the HAL page itself served the metadata).

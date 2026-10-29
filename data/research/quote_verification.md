# Verification of the flagged quotes and search-extract claims

Verification pass, 29 October 2026 (cloud session, branch `verify-research-quotes`). Scope: the claims
flagged as unverified in `corrozet.md`, `print_shop.md` and `open_questions_research.md`.

## Summary

| Verdict | Claims |
|---|---|
| **Confirmed** (source opened and quoted) | **16** |
| **Partly confirmed** | **1** |
| **Contradicted** | **0** |
| **Still unverified** | **53** |
| Total | 70 |

**The external sources could not be opened: this session's network policy blocks every one of them.**
Outbound HTTPS is limited to GitHub and package registries. Each of the hosts below answered the proxy
with `403 Forbidden` on `CONNECT`, which is a policy denial, not a server error or a transient failure:

```
fr.wikipedia.org            en.wikipedia.org          gallica.bnf.fr
archive.org                 web.archive.org           books.openedition.org
journals.openedition.org    shs.hal.science           francearchives.gouv.fr
rdf.archives-nationales.culture.gouv.fr                www.senat.fr
press.uchicago.edu          www.institutparisregion.fr www.paris-pittoresque.com
fr.wikisource.org           collections.louvre.fr      opendata.paris.fr
heurist.huma-num.fr         ccfr.bnf.fr                catalogue.bnf.fr
```

`WebFetch` fails the same way (`getaddrinfo ENOTFOUND`) for all of them, and works normally against the
allowed hosts, so the tool is fine and the policy is the obstacle. **Nothing in this file was upgraded on
the strength of a search extract.** A web search still returns extracts in this session, but a second
extract is not verification, so none was used to resolve a claim; re-deriving them would only have added
a second layer of paraphrase to the record.

**So 53 claims remain exactly as unverified as they were.** What this pass did add:

- **16 claims verified against primary sources that are in the checkout** — Cousin's 1875 notice and
  table, and the OCR of Lacroix's 1874 reprint of the *Fleur* in `data/research/sources/`. Several of
  these were being carried on the site under a *different*, unread citation; the quotations and locations
  are below, so the site can now cite what was actually read.
- **One wrong-volume check passed.** `corrozet_fleur_des_antiquitez_bpt6k6487221d.txt` really is Lacroix's
  1874 reprint of the 1532 *Fleur*, confirmed from the reprint's own **title page** (Gallica viewer p. 9),
  not from the catalogue entry or the URL: `PAR / GILLES CORROZET (1532) / PUBLIÉE / PAR / LE /
  BIBLIOPHILE JACOB / PARIS / LIBRAIRIES: LÉON WILLEM, 8 RUE DE VERNEUIL / PAUL DAFFIS, 7 RUE GUÉNÉGAUD /
  1874`.
- **One correction to the notes' own bookkeeping.** `print_shop.md` is described as carrying 11 †-marked
  facts. It carries 11 **† characters**: 9 on facts (the same three sentences in English, French and
  Swedish) and 2 in the prose that explains the mark. Those 9 markers cover **four** distinct factual
  claims (five if the last sentence is split), not eleven. See group D.
- **One claim downgraded to partly confirmed** (D1): the Cousin half of it is confirmed in the repo; the
  Lepape half is not.

### To finish this job

Add these hosts under **Allowed domains** in the environment's network settings (cloud environment menu
in the session title bar → Edit), leaving *Allow package managers* ticked, and the 53 claims become
checkable in one more pass: `press.uchicago.edu`, `fr.wikipedia.org`, `en.wikipedia.org`, `www.senat.fr`,
`www.institutparisregion.fr`, `books.openedition.org`, `journals.openedition.org`, `shs.hal.science`,
`francearchives.gouv.fr`, `rdf.archives-nationales.culture.gouv.fr`, `fr.wikisource.org`,
`www.paris-pittoresque.com`, `gallica.bnf.fr`, `collections.louvre.fr`, `archive.org`.
The steps: https://code.claude.com/docs/en/cloud-environments#network-access

### How to read the verdicts

- **Confirmed** — a source was opened and the quotation below was copied from it.
- **Partly confirmed** — one component verified, another not.
- **Still unverified — source unreachable** — the claim may well be right; nobody has looked.
  It is *not* evidence against the claim.

---

## Group A — `corrozet.md`, "Later literature (all search extracts only)" (lines 116–140)

| # | Claim (file:line) | Verdict | Found | Source URL (not reachable this session) |
|---|---|---|---|---|
| A1 | fr.wikipedia "Plan de Truschet et Hoyau": « Ce plan est une commande datée de 1553 d'un certain Corrozet adressée à deux artistes de la rue Montorgueil… », and that no reference is attached to it — `corrozet.md:117–120` | Still unverified — source unreachable | — | https://fr.wikipedia.org/wiki/Plan_de_Truschet_et_Hoyau |
| A2 | Sénat brochure *Paris : représentations et plans anciens*: the plan de Bâle (c. 1551) « dont Gilles Corrozet a probablement patronné l'édition pour servir d'annexe à ses Antiquitez de 1550 » — `corrozet.md:121–124` | Still unverified — source unreachable | — | https://www.senat.fr/fileadmin/import/files/fileadmin/Fichiers/Images/archives/brochures-bibliotheque/brochure-02.pdf |
| A3 | *History of Cartography* vol. 3, ch. 48 (Fine to Postel): the Paris map and *Les antiquitez* "were sold together, as confirmed by their joined use by Theodore…", citing Dérens 1980 and the *Fleur* — `corrozet.md:125–128` | Still unverified — source unreachable | — | https://press.uchicago.edu (HOC vol. 3 free chapter PDFs) |
| A4 | Hofmann, HOC vol. 3 ch. 53: the eight-sheet plan "was cut in 1553 by Olivier Truschet and Germain Hoyau" — `corrozet.md:129–130` | Still unverified — source unreachable | — | https://press.uchicago.edu (HOC vol. 3 ch. 53 PDF) |
| A5 | Boutier 2002 dates the plan c. 1553; unknown whether it discusses the acrostic — `corrozet.md:131–132` | Still unverified — not seen | — | — |
| A6 | Dérens 1980 (commentary to the Zürich facsimile) links map and *Fleur* — `corrozet.md:133–134` | Still unverified — not seen | — | — |
| A7 | The Corrozet studies (Chiron, Godet & Tran, *En lisant, en écrivant*; the Persée article) say nothing about the map — `corrozet.md:135–137` | Still unverified — titles only | — | — |
| A8 | "No later source found discusses the acrostic itself" — `corrozet.md:139–140` | Still unverified | A negative claim resting on A1–A7, none of which was opened. It is a statement about what the *extracts* showed, not about what the sources say. | — |

> **Note on A1 and the site.** `corrozet.md:224–227` and the about page both rest on A1 when they say
> French Wikipedia asserts a 1553 commission and that no source for it exists. The about page *also*
> attributes a different formula to the same unread article — "1552 for the view, 1553 for the edition"
> (`web/index.html:209–210`). Both are characterisations of an article nobody has opened. See the live-site
> list below.

### Sources listed at `corrozet.md:246–253` ("Seen only as search extracts")

Source-level roster rather than individual claims; none could be opened, so none moves.

| Source | Status | URL |
|---|---|---|
| Wikipédia (fr), "Plan de Truschet et Hoyau" (+ wikimonde mirror) | Not opened — host blocked | https://fr.wikipedia.org/wiki/Plan_de_Truschet_et_Hoyau |
| Sénat, *Paris : représentations et plans anciens* (brochure-02.pdf) | Not opened — host blocked | https://www.senat.fr/.../brochure-02.pdf |
| HOC vol. 3, ch. 48 and ch. 53 (press.uchicago.edu PDFs) | Not opened — host blocked | https://press.uchicago.edu |
| English Wikipedia, "Gilles Corrozet" | Not opened — host blocked | https://en.wikipedia.org/wiki/Gilles_Corrozet |
| Institut Paris Région page on the plan | Not opened — host blocked | https://www.institutparisregion.fr |
| WorldCat / AbeBooks records of Dérens 1980 | Not opened | — |
| fabula.org notice of *En lisant, en écrivant* | Not opened | — |
| Scripta Manent (huma-num), "Blason des armes de la ville de Paris" | Not opened — host blocked | https://heurist.huma-num.fr/ScriptaManent/ |

---

## Group B — `corrozet.md` claims checkable against primary material in the checkout

All quotations below are copied from `data/research/sources/corrozet_fleur_des_antiquitez_bpt6k6487221d.txt`
(OCR of Lacroix's 1874 reprint, Gallica ark:/12148/bpt6k6487221d), cited by the **Gallica viewer page**
markers the file carries. OCR spelling and run-together words are kept as they stand.

| # | Claim | Verdict | Quotation found | Where |
|---|---|---|---|---|
| B1 | Corrozet's dates are 1510–1568 (on the site at `web/index.html:124` and `web/texts/index.html:160`, previously resting on English Wikipedia) | **Confirmed** | `Corrozet, Gilles (1510-1568). Auteur du texte. La fleur des antiquitez de la noble et triumphante ville et cité de Paris / par Gilles Corrozet (1532) ; publiée par le bibliophile Jacob [Paul Lacroix]. 1874.` | BnF metadata page, Gallica viewer p. 2; file line 27 |
| B2 | The file is Lacroix's 1874 reprint of the 1532 *Fleur* (wrong-volume check) | **Confirmed from the title page** | `PAR / GILLES CORROZET (1532) / PUBLIÉE / PAR / LE / BIBLIOPHILE JACOB / PARIS / LIBRAIRIES: LÉON WILLEM, 8 RUE DE VERNEUIL / PAUL DAFFIS, 7 RUE GUÉNÉGAUD / 1874` | Title page, Gallica viewer p. 9; file lines 134–156 |
| B3 | In the *Fleur* the fourteen acrostic lines stand under the heading "Le nom et surnom de laucteur" (`corrozet.md:102–104`; site `web/index.html:128–129`, `web/texts/index.html:160`) | **Confirmed** | `Le nom et surnom de laucteur.` immediately followed by `Gentilz lecteursamateursdescripture.` / `Ioyeulx esprits regardez la structure` / … / `Son hault estat sa doulce gentillesse` / `Et tous les biens quonpeult en verite` / `Totallement dire dune cite.` — 14 lines, initials G I L L E S C O R R O S E T | Gallica viewer p. 102; file lines 7189–7211 |
| B4 | The poem that follows is headed "Louenges de Paris faictes par ledict aucteur" (`corrozet.md:104–105`) | **Confirmed** | `Louenges deParisfaictesparledict` / `aueteur.` (OCR; *aucteur*), followed by `Nostre cite et ville tantexquise` | Gallica viewer p. 102; file lines 7229–7233 |
| B5 | Map line 15 reads "Noble cite" where the book reads "Nostre cite" (`corrozet.md:163`) | **Confirmed** (book side) | `Nostre cite et ville tantexquise` | Gallica viewer p. 102; file line 7233 |
| B6 | Map line 2 reads "la stature" where the book reads "la structure" (`corrozet.md:162`) | **Confirmed** (book side) | `Ioyeulx esprits regardez la structure` | Gallica viewer p. 102; file line 7193 |
| B7 | The book has a hundred councillors where the map has six score (`corrozet.md:171`; site `web/index.html:137`, `web/texts/index.html:164`) | **Confirmed** (book side) | `Et sainct senat ou sont les conseillers` / `En nombre centhommes tressinguliers` | Gallica viewer p. 105; file lines 7419–7421 |
| B8 | Right after the poem the *Fleur* prints an "Épigramme sur le nom de Paris" whose five lines spell PARIS: P(our), A(ccroissement), R(och), I(ustice), S(cauoir) (`corrozet.md:112–113`) | **Confirmed** | `Épigramme / sur le / nom / de Paris.` then `Pour pris dhonneur precieuse maison` / `Accroissementde tout bien et richesse` / `Roch de vertu et repos de raison` / `Iustice vraye en tout temps et saison` / `Scauoir de tout estude desagesse` / `Cest de Paris le tiltre de noblesse.` | Gallica viewer p. 106; file lines 7497–7513 |
| B9 | The "Blason des armes de la ville de Paris" is 10 lines on the ship of the city's arms and ends with Corrozet's motto *Plus que moins* (`corrozet.md:196–199`, `43–44`) | **Confirmed** | 10 verse lines from `La nef voguant dessus la mergallicque` to `Cest de Paris le beau blason des armes.`, followed by `Plusquemoins.` | Gallica viewer p. 106; file lines 7517–7545 |
| B10 | The texts page cites the poem in Lacroix 1874 as **"pp. 64–68"** (`web/texts/index.html:215`) | **Still unverified** | The OCR carries only Gallica viewer page markers; the poem runs over viewer pp. 102–106. No printed page number appears anywhere in the OCR, so the printed range cannot be checked from this file. Five viewer pages and five printed pages is consistent with a constant offset of 38, but that is arithmetic, not a reading. | — |

---

## Group C — `print_shop.md`, the †-marked facts

11 † characters: 9 on facts, 2 in the prose legend at lines 177 and 231. The 9 cover four distinct claims.

| # | Claim (file:line) | Verdict | Found | Source URL (not reachable this session) |
|---|---|---|---|---|
| C1 | Nicolas Prévost was "installé rue Montorgueil au Chef Saint-Denis, où il se trouvait en **1571**" (Lepape, chapter "Prévost") — `print_shop.md:85–88`, 189/203/219 | **Partly confirmed** | The **Cousin** half is confirmed in the checkout (see D1): Cousin puts the house in Prévost's hands around 1572. Lepape's **1571**, and the claim that this "refines Cousin", are unverified: the chapter could not be opened. | https://books.openedition.org/editionsbnf/2414 |
| C2 | Lepape: the house "était en **1553** le lieu d'édition de Truschet et Hoyau pour le Plan de Paris", and a contents entry "Germain Hoyau au Chef Saint-Denis en 1553" — `print_shop.md:87–92` | Still unverified — source unreachable | Not checked. This is the hinge the note proposes for French Wikipedia's 1553 date, so it matters more than its length suggests. | https://books.openedition.org/editionsbnf/2341 (contents), /2414 |
| C3 | Truschet published a *Carte de la cité de Guînes*, **1559** — `print_shop.md:118`, 190/206/220 | Still unverified — source unreachable | — | https://books.openedition.org/editionsbnf/2395 (dated prints) |
| C4 | Truschet published a *Carte de France, d'Allemagne et d'Italie* after Jean Jolivet, **1560** — `print_shop.md:118–119`, 190/206/220 | Still unverified — source unreachable | — | https://books.openedition.org/editionsbnf/2395 |
| C5 | Hoyau bought a share of the Bon Pasteur house in **1563** and **1566** — `print_shop.md:99`, `122`, 192/207/222 | Still unverified — source unreachable | — | https://books.openedition.org/editionsbnf/2445 |
| C6 | Hoyau was still alive in **1572** (godfather to a grandchild) — `print_shop.md:125–126`, 192/207/222 | Still unverified — source unreachable | Cousin independently has Hoyau signing prints "de 1572 ou environ" (D3), which is consistent, but is a different fact from the godparenthood. | https://books.openedition.org/editionsbnf/2341 |

---

## Group D — `print_shop.md` claims checkable against Cousin in the checkout

Quotations from `data/research/cousin_1875_notice.txt` (OCR of Gallica ark:/12148/bpt6k6310467r) and
`data/research/cousin_1875_table.txt` (project transcription). OCR spelling kept.

| # | Claim | Verdict | Quotation found | Where |
|---|---|---|---|---|
| D1 | Cousin puts the Chef Saint-Denis in Nicolas Prévost's hands around 1572 (`print_shop.md:88` "who says c. 1572"; site `web/index.html:118`, `156`) | **Confirmed** | `Ces planches datent de 1572 ou environ; […] La maison du Chef Saint-Denis, sans doute liquidée après la mort de Truschet, appartient alors à Nicolas Prévost.` | Cousin, printed p. 53; `cousin_1875_notice.txt:315–321` |
| D2 | The neighbouring signs and their holders c. 1572 (`print_shop.md:101–106`; site `web/index.html:118–119`) | **Confirmed** | `Elle a pour voisines—toujours dans la même rue Montorgueil: la maison de l'Échiquier, à Marin Bonnemer et Clément Boussy; la Corne de Daim, à Denis de Mathonière; l'Espinette, à Jean Boussy; l'image Saint-Pierre, à Ch. Levigoureux; la Corne de Cerf, à Marin Boussy, etc., etc., toute une colonie d'imagiers.` | Cousin, printed p. 53; `cousin_1875_notice.txt:321–326` |
| D3 | Hoyau signed prints with his new partner Mathurin Nicolas at the Bon Pasteur, c. 1572; Truschet's signature is gone (site `web/index.html:116–118`) | **Confirmed** | `nous n'y retrouvons plus la signature d'Olivier Truschet, le premier inscrit et probablement le plus ancien des deux associés, mais Germain Hoyau en a signé plusieurs en compagnie de Mathurin Nicolas son nouvel associé à l'enseigne du Bon Pasteur.` | Cousin, printed p. 53; `cousin_1875_notice.txt:315–319` |
| D4 | Truschet and Hoyau were not booksellers; Cousin checked Lottin (`print_shop.md:114–115`; site `web/index.html:105–106`) | **Confirmed** | `Ces éditeurs qui sont-ils? Ce ne sont pas des libraires; je l'ai vérifié sur le catalogue de Lottin.` | Cousin, printed p. 52; `cousin_1875_notice.txt:297–298` |
| D5 | Cousin's table has "COMTE-D'ARTOIS (rue au)" as an entry distinct from "MONTORGUEIL (rue de)" (`print_shop.md:62–66`; site `web/index.html:149–151`) | **Confirmed** | `COMTE-D'ARTOIS (rue au) \| R. Conte Dartois \| VI,1 \|` and `MONTORGUEIL (rue de) \| \| VI,1;V,3 \|` | `cousin_1875_table.txt:109` and `:256` |
| D6 | The map itself labels the southern stretch separately (`streets.csv` L0378 vs L0381) | **Confirmed** | `L0378,R. DE MONTORGUEIL,street,2870,4930` and `L0381,R. CONTE DARTOIS,street,3160,4930` | `data/labels_inventory.csv` |

---

## Group E — `print_shop.md`, the other extract-based facts

All of these are marked "Extract" in the note's own source table. None could be opened.

| # | Claim (file:line) | Verdict | Source URL (not reachable this session) |
|---|---|---|---|
| E1 | FranceArchives record of the inventory after death of Jean Boucy/Boussy and Michèle Clément, at the sign of the Cuillère — **cote and date were never seen** — `print_shop.md:43`, `104` | Still unverified — source unreachable. The record's cote and date remain unknown; nothing should cite a date for it. | https://francearchives.gouv.fr/fr/facomponent/475b5a6d350cc3068d5ac68fcb13baa802a679b0 |
| E2 | AN street register: the rue des Petits-Carreaux was "until the early 17th century confused with the rue Montorgueil" — `print_shop.md:68–69` | Still unverified — source unreachable | https://rdf.archives-nationales.culture.gouv.fr/place/FRAN_RI_025-d3nzchekdc-1oaf022uugsgq |
| E3 | fr.wikipedia: the form "rue des Petitz Carneaulx" first appears in a manuscript of 1636 — `print_shop.md:70–71` | Still unverified — source unreachable | https://fr.wikipedia.org/wiki/Rue_des_Petits-Carreaux |
| E4 | AN register: in 1637 the neighbouring stretch of the rue Poissonnière was the "rue des Boucheries" — `print_shop.md:71–72` | Still unverified — source unreachable | as E2 |
| E5 | The porte au Comte d'Artois was ordered demolished in **December 1498**; the street was joined to the rue Montorgueil in **1792** — `print_shop.md:58–62` | Still unverified — source unreachable. (Cousin confirms only that the map names the two streets separately, D5; he gives neither date.) | https://fr.wikisource.org (Lazare, "Montorgueil (rue)"); AN register |
| E6 | fr.wikipedia: the Charles V wall had six original Right-Bank gates, none at Montorgueil — `print_shop.md:76–78` | Still unverified — source unreachable | https://fr.wikipedia.org/wiki/Enceinte_de_Charles_V |
| E7 | Alain de Mathonière owned the Corne de Daim outright from **13 Oct. 1565**, installed from **19 Jan. 1577**; Denis de Mathonière's 1598 inventory lists two large presses and a typographic press — `print_shop.md:101` | Still unverified — source unreachable | https://fr.wikipedia.org/wiki/Denis_de_Mathonière |
| E8 | Denis Fonteney/Fontenoy (d. 1583) is given the Corne de Daim though his prints say only "près l'Échiquier" — `print_shop.md:101` | Still unverified — source unreachable | https://books.openedition.org/editionsbnf/2434 |
| E9 | Guillaume Saulce at the Espinette — `print_shop.md:103` | Still unverified — source unreachable | https://books.openedition.org/editionsbnf/2417 |
| E10 | Fonteney's daughter was baptised at Saint-Eustache on **29 May 1579** — `print_shop.md:108–109` | Still unverified — source unreachable | https://books.openedition.org/editionsbnf/2434 |
| E11 | **24 Aug. 1564**: Gilles Godet sells Hoyau, François Desprez and Mathurin Nicolas twelve woodblocks of the Months for 200 livres tournois — `print_shop.md:122–124` | Still unverified — source unreachable | https://collections.louvre.fr/en/ark:/53355/cl020519735 |
| E12 | "La veuve de Germain Hoyau" died in **1585**; Hoyau therefore died between 1572 and 1585 — `print_shop.md:125–126` | Still unverified — source unreachable | https://books.openedition.org/editionsbnf/2341 |
| E13 | Truschet was dead by **1575** (Grivel 2008 via Lepape) — `print_shop.md:129`; **on the site** at `web/index.html:120–121` | Still unverified — source unreachable. Cousin supports only the weaker statement that Truschet's signature is absent from the c. 1572 prints (D3) and that the house was liquidated "sans doute après la mort de Truschet" (D1) — he gives no year. | https://shs.hal.science/halshs-00602821 |
| E14 | HOC calls Hoyau "imagier en papier" and draughtsman, with Truschet the engraver — the reverse of French Wikipedia — `print_shop.md:115–117`; **on the site** at `web/index.html:112–114` | Still unverified — source unreachable | https://press.uchicago.edu (HOC vol. 3 ch. 53) |
| E15 | HOC: the Guînes map was copied from a manuscript by Nicolas de Nicolay; Truschet is linked to a *Description de la haulte et basse Picardye*, c. 1559–60 — `print_shop.md:119–121` | Still unverified — source unreachable | as E14 |
| E16 | Hoyau's sister Jeanne Hoyau married François Gence — `print_shop.md:124–125` | Still unverified — source unreachable | https://books.openedition.org/editionsbnf/2423 |
| E17 | Lepape's index: "Veuve de Mathurin Nicolas: voir Hoyau (Catherine)" — `print_shop.md:127–128` | Still unverified — source unreachable | https://books.openedition.org/editionsbnf/2421 |
| E18 | **The two Lepape extracts contradict each other**: Hoyau buys a *sixth* in 1563 and another *sixth* in 1566, or Desprez sells his *third* in two parts — `print_shop.md:99` | Still unverified — unresolved. Both readings come from extracts of chapters that could not be opened, so the conflict cannot be settled here. The site's wording "a share" (`web/index.html:120`) sidesteps it correctly and should stay that way. | https://books.openedition.org/editionsbnf/2445 |
| E19 | In 1575 the archbishopric's censier still lists Hoyau, Desprez and Olivier Truschet as owners of the Bon Pasteur; Grivel takes Truschet's name as an error since he was dead — `print_shop.md:99`; the censive point is **on the site** at `web/index.html:162` | Still unverified — source unreachable | https://shs.hal.science/halshs-00602821 |
| E20 | Bibliographic metadata taken from extracts: Lepape 2016, 361 p., ISBN 978-2-7177-2656-5, DL 2015 (`:40`); Grivel 2008, *Documents d'histoire parisienne* n° 9, pp. 15–47 (`:41`); Grivel 2015, n° 17, pp. 5–16 (`:42`); HOC ch. 53, pp. 1569–1588 (`:50`) | Still unverified — catalogues unreachable. These appear in the site's source list, so they are worth a catalogue check before the next publish. | — |

---

## Group F — `open_questions_research.md`, the quotes

The file's own header says its quotes come from search extracts of the Paris street registers and other
pages rather than from the pages themselves. That header stands: none of the pages could be opened.

### L0007 "LE PONT ARCANS"

| # | Claim (file:line) | Verdict | Found | Source URL (not reachable this session) |
|---|---|---|---|---|
| F1 | fr.wikipedia, *Liste des ponts de Paris*: « Pont Arcans : jeté sur le Grand Égout, il était situé entre le château des Porcherons et la Ville l'Évêque. » — `:19–21` | Still unverified — source unreachable | — | https://fr.wikipedia.org/wiki/Liste_des_ponts_de_Paris |
| F2 | *Paris pittoresque*, "Chaussée-d'Antin", quoting Lurine 1844: the road from the Porte Gaillon to the Porcherons crossed the sewer on a poor bridge called the Pont-Arcans, cracked, ugly, without railings — `:22–25` | Still unverified — source unreachable. The note already says this is "the gist from search extracts, not the exact wording"; no wording has been recovered. | — | https://www.paris-pittoresque.com/rues/100.htm |
| F3 | An unidentified French source: building the rue de Provence « fit disparaître le pont d'Arcans enjambant l'égout au niveau approximatif de la rue de la Chaussée d'Antin actuelle » — `:26–29` | Still unverified — **source not even identified** (the note guesses fr.wikipedia *Rue de Provence* or *Ruisseau de Ménilmontant*). An unattributed quotation should not be cited anywhere until its page is found. | — | — |
| F4 | English Wikipedia, *Menilmontant brook*, says the same in English — `:30` | Still unverified — source unreachable | — | https://en.wikipedia.org/wiki/Menilmontant_brook |
| F5 | Duplomb, *Histoire générale des ponts de Paris* (1911–13), lists it among the "forgotten" bridges over sewers; seen only in a bookseller's description — `:31–34` | Still unverified — source unreachable | — | https://blog.paris-libris.com/duplomb-charles-histoire-generale-des-ponts-de-paris/ |
| F6 | BnF CCFr: a folio titled "Pont Arcans" in Charles Sellier's notes — `:35–36` | Still unverified — source unreachable | — | https://ccfr.bnf.fr/portailccfr/ark:/16871/004a1965928 |
| F7 | The rue de Provence × rue de la Chaussée-d'Antin crossing is at about **48.8745 N, 2.3330 E** — `:42–44` | Still unverified. The note itself says this is **"from memory, ±50 m"**, with OpenStreetMap unreachable; it is still unreachable (`opendata.paris.fr` and the map services are blocked). **Nothing should be moved onto this coordinate until it is checked.** `others.csv` L0007 correctly leaves `coords` empty, so the live pin is the overlay estimate (48.8755, 2.338845) and is unaffected. | — | — |
| F8 | Label-position reasoning: L0007 is 641 px from LES TORCHERONS (L0462) and 1300 px from LA VILLE LEVESQUE (L0464) — `:38–40` | **Confirmed** | Computed from `data/labels_inventory.csv`: L0007 (1100, 7150) → L0462 (770, 6600) = **641 px**; → L0464 (2400, 7100) = **1301 px** (note says 1300; rounding). | `data/labels_inventory.csv` |

### L0421 "R. BRENEUSE"

| # | Claim (file:line) | Verdict | Found | Source URL (not reachable this session) |
|---|---|---|---|---|
| F9 | Lazare, "Verdelet (rue)", Wikisource: « En 1295, ce n'était qu'une ruelle étroite et puante hors des murs de l'enceinte de Philippe-Auguste. Elle se nommait alors rue Merderet. […] Plus tard, par altération, elle fut appelée rue Verderet, puis Verdelet. » — `:62–67` | Still unverified — source unreachable | — | https://fr.wikisource.org/wiki/Dictionnaire_administratif_et_historique_des_rues_de_Paris_et_de_ses_monuments/Verdelet_(rue) |
| F10 | The 1311 *rôle de la taille* calls it « rue Breneuse » — `:67–68` | Still unverified — source unreachable. This is the load-bearing link between the map's label and the identification. | — | as F9 |
| F11 | A reprint adds « Des actes de 1290, 1330, 1352 et 1406 l'indiquent sous les noms de Merderiau, Merderai, Merderel et Merderet » — `:68–69` | Still unverified — source unreachable | — | as F9 |
| F12 | AN register: « La rue Verdelet, qui était comprise entre les rues Jean-Jacques Rousseau et de la Jussienne, avait porté les noms de rue Mardelet ou Marderet (XIIIe siècle), Breneuse et enfin de rue Verderet ou Verdelet. » — `:70–73`. The note also cannot say **which of two records** the quote belongs to. | Still unverified — source unreachable; the record-id ambiguity is also unresolved | — | https://rdf.archives-nationales.culture.gouv.fr/place/FRAN_RI_025-d3nzcc8smx--w2i8uceiz29c-vdp-3149 (and …-vdp-3953) |
| F13 | fr.wikipedia has both *Rue Verderet (ancienne voie de Paris)* and *Rue Merderet*, noting the two are sometimes confused — `:75–78` | Still unverified — source unreachable | — | https://fr.wikipedia.org |
| F14 | *Nouvelle revue d'onomastique* (OpenEdition), citing Lock 1867, puts "Orde rue" in 1311 and "Breneuse" after it — a disagreement with F10 — `:79–81` | Still unverified — source unreachable; the disagreement with F10 therefore stands unresolved | — | https://journals.openedition.org/nda/3928 |
| F15 | AN register gives "Breneuse" also as an old name of the rue du Petit-Reposoir, renamed by a court ruling of 1582 — `:84–86` | Still unverified — source unreachable | — | https://rdf.archives-nationales.culture.gouv.fr |
| F16 | AN register: the rue Pagevin of 1849 disappeared under the rue Étienne-Marcel and the Hôtel des Postes, so L0422's match to `CUR:rue d'Argout` may be wrong — `:98–102` | Still unverified — source unreachable. The flagged possible inconsistency in `streets.csv` stays open. | — | https://rdf.archives-nationales.culture.gouv.fr |
| F17 | Label-position reasoning: L0421 is 186 px from L0408, 148 px from L0423, 197 px from L0420, and L0422 is 220 px further — `:86–89` | **Confirmed** | From `data/labels_inventory.csv`: L0421 (3150, 5600) → L0408 = **186 px**, → L0423 = **149 px** (note says 148), → L0420 = **197 px**, → L0422 = **220 px**. | `data/labels_inventory.csv` |

### L0224 "R. NEUVE"

| # | Claim (file:line) | Verdict | Found | Source URL |
|---|---|---|---|---|
| F18 | Cousin: « NEUVE (rue), sans autre désignation \| IV,2 \| donnant dans la rue de la Barre au faub. St-Marcel » — `:106–107` | **Confirmed** | `NEUVE (rue), sans autre désignation \| \| IV,2 \| donnant dans la rue de la Barre au faub. St-Marcel` — the quotation is exact; the note simply elides the empty map-label column. Cousin's table also has a *different* `NEUVE (rue) \| R. Neueve \| VIII,4` entry for the faubourg Saint-Germain, so the two must not be confused. | `cousin_1875_table.txt:266` (and `:265` for the other) |
| F19 | fr.wikipedia: « rue Scipion (ancienne rue de la Barre, ouverte en 1540) » — `:114–115` | Still unverified — source unreachable | — | https://fr.wikipedia.org/wiki/Faubourg_Saint-Marcel_(quartier_de_Paris) |
| F20 | The *séjour d'Orléans* was divided into plots in 1541/1545, opening the rues Censier and de la Clef — `:118–121` | Still unverified — source unreachable | — | https://paris-atlas-historique.fr/32.html |
| F21 | The rue des Francs-Bourgeois-Saint-Marcel ran from the rue des Fossés-Saint-Marcel to the place de la Collégiale, is now under the boulevard Saint-Marcel, and its name dates from 1296 — `:122–125` | Still unverified — sources unreachable | — | Lazare 1844; Carnavalet; INHA |
| F22 | Lazare gives the rue du Fer-à-Moulin the earlier names « rue Richebourg » and « rue des Morts » — `:130–131` | Still unverified — source unreachable | — | https://fr.wikisource.org |
| F23 | Label-position reasoning: L0224 is 168 px from L0037, 208 px from L0223, 284 px from L0222 — `:109–111` | **Confirmed** | From `data/labels_inventory.csv`: L0224 (9520, 1140) → L0037 = **168 px**, → L0223 = **209 px** (note says 208), → L0222 = **285 px** (note says 284). Rounding only. | `data/labels_inventory.csv` |

---

## What this pass did *not* do

- It opened none of the external sources, so no claim about French Wikipedia, the Sénat brochure, the
  *History of Cartography* chapters, Lepape, Grivel, the Archives nationales registers, Lazare on
  Wikisource, paris-pittoresque or FranceArchives has been checked.
- It did not touch the research library on the owner's machine (Cousin 1875 in facsimile, the *Antiquitez*
  1561, the *Fleur* 1532 originals, Lespinasse, the *Registres des délibérations*) — out of scope here.
- It did not check the printed page range "pp. 64–68" cited for the poem on the texts page (B10).
- It did not edit any page of the site.

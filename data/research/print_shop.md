# The print shop "au Chef Sainct-Denys", rue Montorgueil

Research note, 2026-10-26 (cloud session, branch `print-shop-research`).

**Status: open** — listed in `OPEN_QUESTIONS.md` ("Research questions"); summary on the site at https://paris1550.vercel.app/#shop (section "Where was the shop?"). Add new findings here.

## Question

The publishers' notice on the map reads: *"A Paris, par Olivier Truschet, & Germain Hoyau, demourans en
la Rue de Montorgueil, au Chef sainct Denys."* Where was the house at the sign of the Chef Saint-Denis,
in terms of today's rue Montorgueil?

## Short answer

**House not found.** No source I could reach places the Chef Saint-Denis at a present-day street
number, block, side of the street or cross-street. What can be said:

1. The map itself names the southern stretch separately ("R. Conte Dartois", Cousin's table), so on the
   publishers' own sheet "rue de Montorgueil" meant the street **north of the rue Mauconseil**. The shop
   was somewhere on today's rue Montorgueil between the rue Mauconseil and the rue Saint-Sauveur, or on
   today's rue des Petits-Carreaux, which was still counted as part of the rue Montorgueil until the early
   17th century. (Medium confidence: it assumes the notice uses the same street names as the map.)
2. The house is well attested as a print shop over about twenty years: Truschet and Hoyau there c. 1550–53,
   Nicolas Prévost there in 1571 (Lepape, extract). It was one of a cluster of image-makers' houses
   (Bon Pasteur, Corne de Daim, Échiquier, Espinette, Cuillère…), none of which I found matched to a
   modern address either.

## Sources and how they were read

Network policy blocked all direct fetches (curl: proxy 403; WebFetch: DNS failure for
books.openedition.org, gallica.bnf.fr, fr.wikisource.org, centrechastel…). **Everything below except
Cousin 1875 and the project's own data comes from search-engine extracts**, not from reading the
source. Extracts are a search model's summary of a page, sometimes with quoted fragments; wording and
page numbers must be checked against the source before they are quoted on the site.

| Key | Source | How read |
|---|---|---|
| COUSIN | Jules Cousin, "Notice sur un plan de Paris du XVIe siècle nouvellement découvert à Bâle", *Mémoires de la Société de l'histoire de Paris et de l'Île-de-France*, t. I (1875), pp. 46–59, here pp. 52–53. `data/research/cousin_1875_notice.txt` | **Read in full** (OCR) |
| COUSIN-T | Cousin, "Table des noms des rues…", same volume, pp. 60–70. `data/research/cousin_1875_table.txt` | **Read in full** (project transcription) |
| LEPAPE | Séverine Lepape, *Gravures de la rue Montorgueil*, Paris, Bibliothèque nationale de France, 2016 (DL 2015), 361 p., ISBN 978-2-7177-2656-5; online at OpenEdition Books, https://books.openedition.org/editionsbnf/2341 (table of contents). Chapters used: "Prévost" (editionsbnf/2414), "Les Desprez" (editionsbnf/2445, already source [9] on the about page), "Les Gence et Leroy" (2423), "Fonteney ou Fontenoy" (2434), "Saulce" (2417), "Gravures… datées" (2395), index (2421) | Extracts only |
| GRIVEL08 | Marianne Grivel, "Au Bon Pasteur, rue Montorgueil : une famille d'imagiers parisiens dans la seconde moitié du XVIe siècle", *Documents d'histoire parisienne*, n° 9, 2008, pp. 15–47; HAL: https://shs.hal.science/halshs-00602821 | Bibliographic record only; content known only as cited by LEPAPE |
| GRIVEL15 | Marianne Grivel, "Une famille d'imagiers de la rue Montorgueil au XVIe siècle : les Boussy. Réseau familial, méthodes de travail et alliances commerciales", *Documents d'histoire parisienne*, n° 17, 2015, pp. 5–16 | Bibliographic record only (title, issue, pages from extract) |
| BOUSSY-IAD | Inventaire après décès de Jean Boucy (ou Boussy), maître imagier en papier, et de Michèle Clément, sa femme, rue Montorgueil, à l'enseigne de la Cuillère; FranceArchives, https://francearchives.gouv.fr/fr/facomponent/475b5a6d350cc3068d5ac68fcb13baa802a679b0 (Archives nationales, Minutier central) | Search title only; **date and cote still not seen** (29 Oct 2026: francearchives.gouv.fr blocked by the session's network policy). Cite no date for this act. |
| AN-PC | Archives nationales, street register entry "rue des Petits Carreaux", https://rdf.archives-nationales.culture.gouv.fr/place/FRAN_RI_025-d3nzchekdc-1oaf022uugsgq | Extract |
| AN-CA | Archives nationales, street register entries for the rue au Comte-d'Artois / de la Porte au Comte (part of rue Montorgueil) | Extract |
| LAZARE | Félix et Louis Lazare, *Dictionnaire administratif et historique des rues de Paris et de ses monuments* (1844; 2nd ed. 1855), "Montorgueil (rue)", Wikisource | Extract |
| WP-PC | "Rue des Petits-Carreaux", Wikipédia (fr) | Extract |
| WP-C5 | "Enceinte de Charles V", Wikipédia (fr) | Extract |
| WP-MAT | "Denis de Mathonière", Wikipédia (fr) | Extract |
| HOC | Catherine Hofmann, "Publishing and the Map Trade in France, 1470–1670", in D. Woodward (ed.), *The History of Cartography*, vol. 3, part 2, University of Chicago Press, 2007, ch. 53, pp. 1569–1588 (PDF at press.uchicago.edu) | Extract |
| BEAUREPAIRE | Edmond Beaurepaire, *Vieux Paris, vieux plans*, Gallica ark:/12148/bpt6k64563829 | Extract |
| BRETTE | Armand Brette (ed.), *Atlas de la censive de l'Archevêché dans Paris*, Paris, Imprimerie nationale, 1906 (Histoire générale de Paris); archive.org `atlasdelacensive00bret` | Bibliographic record only |

**Verification pass, 29 October 2026 (branch `verify-research-quotes`).** Every extract-based fact in
this note was put to a check; the result is in `quote_verification.md`. **The external sources still
could not be opened** — books.openedition.org, francearchives.gouv.fr,
rdf.archives-nationales.culture.gouv.fr, fr.wikipedia.org, fr.wikisource.org, press.uchicago.edu,
collections.louvre.fr and shs.hal.science are all refused by the session's network policy — so the
extract markings below stand. Two things did change:

- The **Cousin** half of the Prévost finding is now confirmed from the OCR in this repository (see §2);
  Lepape's 1571 is not. That † is downgraded to "partly confirmed", not removed.
- The daggers: this note carries **11 † characters**, but 9 of them are on facts (the same three
  sentences in English, French and Swedish) and 2 are in the prose that explains the mark. They cover
  **four** distinct claims — Prévost 1571; Guînes 1559; France/Germany/Italy 1560; Hoyau's Bon Pasteur
  shares 1563/1566 and his being alive in 1572 — not eleven.

## Findings

### 1. Where "rue Montorgueil" ran in 1550

**Southern end — confirmed.** The stretch from the rue Montmartre (Pointe Saint-Eustache) to the rue
Mauconseil was the rue au Comte-d'Artois (also rue de la Comtesse-d'Artois, de la Porte au Comte),
named after the counts of Artois' hôtel and the "porte au Comte d'Artois", a postern of the Philippe
Auguste wall; the gate was ordered demolished in December 1498; the street was joined to the rue
Montorgueil in 1792 (LAZARE, AN-CA, extracts). **New, and stronger than the register:** the 1550 map
itself labels it separately: Cousin's table has "COMTE-D'ARTOIS (rue au) | R. Conte Dartois | VI,1" as
a distinct entry from "MONTORGUEIL (rue de) | VI,1; V,3" (COUSIN-T, read in full; project data:
`streets.csv` L0378 vs L0381). So on the publishers' own sheet the shop's street began at the rue
Mauconseil.

**Northern end — mostly settled.** The Archives nationales register says the rue des Petits-Carreaux was
"until the early 17th century confused with the rue Montorgueil" (AN-PC, extract); French Wikipedia says it
was at first part of the rue Montorgueil and became a separate street only in the 17th century, with the
form "rue des Petitz Carneaulx" first found in a manuscript of 1636 (WP-PC, extract). In 1637 the
neighbouring stretch of the rue Poissonnière was the "rue des Boucheries" (AN-PC, extract). So in 1550 the
name very probably covered today's rue des Petits-Carreaux as well, i.e. it ran up to the Charles V wall,
whose ditch is followed by today's rue d'Aboukir (WP, extract).

**No Porte Montorgueil in the Charles V wall.** French Wikipedia lists six original gates on the Right
Bank (Saint-Honoré, Montmartre, Saint-Denis, Saint-Martin, Temple, Saint-Antoine), none at Montorgueil
(WP-C5, extract). The only "Montorgueil" gate in the sources is the 13th-century postern of the
Philippe Auguste wall at the *southern* end (= porte au Comte d'Artois). I did not establish whether the
street ended blind at the wall in 1550 or passed it by a minor opening; not found.

### 2. The house at the Chef Saint-Denis

- 1550s: Truschet and Hoyau "demourans en la rue de Montorgueil, au chef Sainct-Denys" (the map; COUSIN).
- **Cousin, printed p. 53 — confirmed, read in this repository** (`cousin_1875_notice.txt:315–321`):
  "Ces planches datent de 1572 ou environ; [...] La maison du Chef Saint-Denis, sans doute liquidée après
  la mort de Truschet, appartient alors à Nicolas Prévost." Note what Cousin actually claims: the house
  **belonged to** Prévost around 1572. He does not say Prévost printed there, and he gives no year for
  Truschet's death.
- LEPAPE, chapter "Prévost" (extract, **still unverified 29 Oct 2026**): Nicolas Prévost, "peintre en
  papier, imprimeur d'histoires et imagier", was "installé rue Montorgueil au Chef Saint-Denis, où il se
  trouvait en 1571", and the house "était en 1553 le lieu d'édition de Truschet et Hoyau pour le Plan de
  Paris". This would **refine Cousin** (who says c. 1572, now confirmed above) to 1571 and give a modern
  scholarly confirmation of the house's continuity — if the chapter can be opened.
  The table of contents (extract) has an entry like "Germain Hoyau au Chef Saint-Denis en 1553".
  → Note that Lepape apparently dates the plan **1553**. That may be where French Wikipedia's
  "commande… datée de 1553" comes from (the about page says its source is not given). Unverified:
  the extract does not say what document carries the 1553 date. Worth passing to the Corrozet session.
- No source located the house more closely than "rue Montorgueil". **Not found.**

### 3. The neighbouring signs

| Sign | Who, when | Source | Location found? |
|---|---|---|---|
| Bon Pasteur | François Desprez, Richard Breton, Olivier Truschet co-owners until 1563; Germain Hoyau buys a sixth in 1563 and another sixth in 1566 (one LEPAPE extract) — or Desprez sells his *third* in two parts to Hoyau, 1563 and 1566 (chapter "Les Desprez", extract): **the extracts disagree, sixth vs third**. Later Breton and Marc Duchesne; Simon Douget by marriage to Geneviève Desprez. In 1575 the **archbishopric's censier** still lists Hoyau, Desprez and Olivier Truschet as owners; Grivel (2008) takes Truschet's name as an error, since he was dead | LEPAPE (extracts) citing GRIVEL08 | No |
| Chef Saint-Denis | Truschet & Hoyau (1550s); Nicolas Prévost (1571) | Map; COUSIN; LEPAPE | No |
| Corne de Daim | Alain de Mathonière owner outright from 13 Oct. 1565, installed from 19 Jan. 1577; Denis de Mathonière (inventory 1598: two large presses and a typographic press); Denis Fonteney/Fontenoy (d. 1583) also given this sign, though his prints say only "près l'Échiquier" | WP-MAT, LEPAPE "Fonteney" (extracts) | No; only "near the Échiquier" |
| Échiquier | Marin Bonnemer, Clément Boussy (c. 1572) | COUSIN | No; it was close to the Corne de Daim (Fonteney's "près l'Échiquier") |
| Espinette | Jean Boussy (COUSIN); Guillaume Saulce (LEPAPE "Saulce", extract) | | No |
| Cuillère | Jean Boucy/Boussy, maître imagier en papier, and his wife Michèle Clément | BOUSSY-IAD (title) | No. Cousin puts Jean Boussy at the Espinette: either two Jean Boussys, a move, or an error — GRIVEL15 should settle it |
| Image Saint-Pierre | Ch. Levigoureux | COUSIN | No |
| Corne de Cerf | Marin Boussy | COUSIN | No |

The image-makers were parishioners of **Saint-Eustache** (e.g. Fonteney's daughter baptised there,
29 May 1579: LEPAPE, extract).

### 4. Truschet and Hoyau: other solid facts

- **Trades.** LEPAPE (extract) calls Truschet an imprimeur-imagier, "peintre en papier" and dominotier
  at the Chef Saint-Denis, also named among the owners of the Bon Pasteur. Cousin (read in full) found
  they were not booksellers (checked against Lottin). HOC/vol. 3 (extract) calls Hoyau "imagier en papier"
  and draughtsman with Truschet the engraver — the reverse of French Wikipedia (this is probably the
  "other way round" source the about page mentions; still an extract, page not seen).
- **Other works by Truschet** (LEPAPE, dated-prints list, extract): *Carte de la cité de Guînes*, 1559, and
  *Carte de France, d'Allemagne et d'Italie* after Jean Jolivet, 1560. HOC (extract): the Guînes map was
  copied from a manuscript by Nicolas de Nicolay, and Truschet is linked to a *Description de la haulte et
  basse Picardye* (c. 1559–60). So Truschet was a map publisher beyond the Paris plan, active at least to 1560.
- **Hoyau.** 24 Aug. 1564: Gilles Godet sells Hoyau, François Desprez and Mathurin Nicolas twelve woodblocks
  of the Months for 200 livres tournois (LEPAPE, extract; Louvre collections, "Mois de novembre",
  https://collections.louvre.fr/en/ark:/53355/cl020519735, citing Lepape no. 164). His sister Jeanne Hoyau
  married François Gence (Grivel, cited by LEPAPE, extract). He was godfather to a grandchild in 1572, so
  alive then; "la veuve de Germain Hoyau" died in 1585 (LEPAPE, extracts). So Hoyau died between 1572 and
  1585. The index also has "Veuve de Mathurin Nicolas: voir Hoyau (Catherine)" — a Hoyau woman married to
  Hoyau's partner Nicolas; relationship not seen.
- **Truschet** was dead by 1575 (GRIVEL08 via LEPAPE, extract) and is absent from the c. 1572 prints
  (COUSIN). Dates of life: BnF authority "Truschet, Olivier (15..-15..)".

## Confidence

- Southern limit (rue Mauconseil) of the 1550 rue Montorgueil: **high** (register + the map's own label).
- Petits-Carreaux included in 1550: **medium-high** (two independent extracts agree; not read).
- Chef Saint-Denis = a print shop continuously from the 1550s to 1571: **high** (Cousin read; Lepape extract).
- Present-day location of the Chef Saint-Denis: **not found**. No street number should be published.

## Not found

- Any modern address, block, side of street or cross-street for the Chef Saint-Denis or any neighbour.
- Lefeuve, *Histoire de Paris rue par rue* (rue Montorgueil): no passage surfaced.
- Berty/Tisserand, *Topographie historique du vieux Paris*: the published volumes found are Louvre/
  Tuileries, Bourg/Faubourg Saint-Germain, Université regions; I found no published Halles/Saint-Eustache
  volume covering the rue Montorgueil.
- Préaud et al., *Dictionnaire des éditeurs d'estampes à Paris sous l'Ancien Régime* (1987);
  Renouard; Grodecki; Wildenstein; Weigert; Jaillot; Hillairet: no relevant extract surfaced.
- The full text of Grivel 2008 and 2015.

## Where to look next (archive access needed)

1. **Read Lepape 2016 in full** (OpenEdition Books, open access in parts): chapters "Prévost",
   "Truschet" (if separate), "Hoyau", "Les Boussy", "Bonnemer", and the introduction. Check whether Lepape
   gives the document for "1553" and whether any notarial act locates a house by its neighbours
   ("tenant d'une part à… aboutissant à…").
2. **Grivel 2008 and 2015** (*Documents d'histoire parisienne* 9 and 17; HAL halshs-00602821). Notarial
   sales of shares of the Bon Pasteur (1563, 1566) normally give abutments, which would place the Bon
   Pasteur relative to its neighbours and possibly to the Chef Saint-Denis.
3. **The archbishop's censiers.** The 1575 entry for the Bon Pasteur shows these houses were in the
   *censive de l'archevêché*. The archbishopric's censiers and terriers (Archives nationales, series S,
   archevêché de Paris; cote not identified here) list houses in street order with signs and
   owners, and can be chained forward to the 1786 terrier whose parcel plans Brette published (BRETTE,
   1906). That chain is the standard way (Berty's method) to put a 16th-century sign on a modern parcel.
4. **Minutier central** (AN, MC): the Jean Boussy inventory (BOUSSY-IAD) and the Mathonière acts
   (1565, 1577, 1598) — inventories après décès describe the house room by room and often its abutments.
   Catherine Grodecki, *Documents du Minutier central des notaires de Paris. Histoire de l'art au XVIe
   siècle (1540–1600)*, 2 vols (1985–86) indexes such acts by name; look up Truschet, Hoyau, Prévost,
   Boussy, Mathonière, Bonnemer.
5. **Saint-Eustache parish registers**: the originals burned in 1871; Lepape's baptisms presumably come
   from the Laborde index (BnF, fichier Laborde) — worth a name search for Truschet.

## Ready-to-paste text for "Who made it"

Source numbers: `[1]` = Cousin 1875 notice (existing), `[2]` = Cousin's table (existing), `[9]` = Lepape,
"Les Desprez" (existing). New: `[A]` Lepape 2016 (whole book / "Prévost" chapter), `[B]` Grivel 2008,
`[C]` Archives nationales street register (rue des Petits-Carreaux; rue au Comte-d'Artois). Full entries
below. Facts marked † are from search extracts only; the main session should check them in Lepape
before publishing (Lepape is open on OpenEdition and was reachable from the owner's own machine before).

### English

The address on the map is "in the rue Montorgueil, at the sign of the Head of Saint Denis". In 1550 that
name did not cover the whole of today's street: the stretch south of the rue Mauconseil was the rue au
Comte-d'Artois, and the map labels it so; it joined the rue Montorgueil only in 1792
[2][C]. To the north the name still took in today's rue des Petits-Carreaux, a separate street only in the
17th century [C]. The shop stood somewhere on that stretch, between the rue Mauconseil and the city wall. Exactly where is not known: no study we found ties the sign to a present-day house.

The house stayed in the trade. By 1571 the image-maker Nicolas Prévost was printing at the Head of Saint
Denis† [A], and the neighbours were image-makers too: the Chessboard, the Deer's Horn, the Spinet, the Stag's
Horn [1]. Truschet also published maps of Guînes (1559) and of France, Germany and Italy (1560)† [A];
he was dead by 1575 [9][B]. Hoyau bought into the house of the Good Shepherd in the same street in 1563
and 1566 and was still alive in 1572† [9][A].

### Français

L'adresse portée sur le plan est « en la rue de Montorgueil, au Chef Saint-Denis ». En 1550 ce nom ne
couvrait pas toute la rue actuelle : au sud de la rue Mauconseil, c'était la rue au Comte-d'Artois, que le
plan nomme ainsi, réunie à la rue Montorgueil seulement en 1792 [2][C]. Au nord, en revanche, le nom
englobait encore l'actuelle rue des Petits-Carreaux, qui n'est devenue une rue distincte qu'au XVIIe siècle
[C]. La boutique se trouvait quelque part sur ce tronçon, entre la rue Mauconseil et l'enceinte. On ne sait pas où exactement : aucune étude que nous ayons trouvée ne rattache l'enseigne à une
maison d'aujourd'hui.

La maison resta dans le métier. En 1571 l'imagier Nicolas Prévost y travaillait, au Chef Saint-Denis†
[A], et les voisins étaient eux aussi imagiers : l'Échiquier, la Corne de Daim, l'Espinette, la Corne de
Cerf [1]. Truschet a aussi publié une carte de Guînes (1559) et une carte de France, d'Allemagne et d'Italie
(1560)† [A] ; il était mort en 1575 [9][B]. Hoyau acheta des parts de la maison du Bon Pasteur, dans
la même rue, en 1563 et 1566, et vivait encore en 1572† [9][A].

### Svenska

Adressen på kartan är ”i rue de Montorgueil, vid skylten Sankt Denis huvud”. År 1550 gällde namnet inte
hela dagens gata: sträckan söder om rue Mauconseil hette rue au Comte-d'Artois, och kartan kallar den så;
den slogs ihop med rue Montorgueil först 1792 [2][C]. Norrut omfattade namnet däremot fortfarande
dagens rue des Petits-Carreaux, som blev en egen gata först på 1600-talet [C]. Någonstans på den
sträckan, mellan rue Mauconseil och stadsmuren, låg verkstaden. Exakt var vet man inte:
ingen undersökning vi har hittat knyter skylten till ett hus som står i dag.

Huset förblev en bildtryckarverkstad. År 1571 tryckte bildmakaren Nicolas Prévost där, vid Sankt Denis
huvud† [A], och grannarna var också bildmakare: Schackbrädet, Dovhjortshornet, Spinetten, Kronhjortshornet
[1]. Truschet gav också ut kartor över Guînes (1559) och över Frankrike, Tyskland och Italien (1560)† [A];
han var död 1575 [9][B]. Hoyau köpte andelar i huset Den gode herden på samma gata 1563 och
1566 och levde ännu 1572† [9][A].

Notes on the wording:
- The sources say only that the Bon Pasteur was in the *same street*; don't write "next door" or
  "a few doors away".
- No length is given for the stretch Mauconseil → city wall; measure it on the project's street
  geometry before adding a figure.
- "Spinet" for *l'Espinette*: an *espinette* is a small spinet (keyboard instrument), but it could also be
  a thorn-bush (*épine*). If Lepape or Grivel don't explain it, leave the name in French.
- Nicolas Prévost's 1571 date and Truschet's 1559/1560 maps are marked † (search extract only). As of
  29 Oct 2026 they are **still unverified**; Cousin's own "c. 1572, the house belonged to Prévost" is
  confirmed and is the safe form to publish until Lepape can be read.

### New source entries

- **[A]** Séverine Lepape, *Gravures de la rue Montorgueil*, Paris, Bibliothèque nationale de France,
  2016, ISBN 978-2-7177-2656-5; OpenEdition Books, https://books.openedition.org/editionsbnf/2341
  (chapter "Prévost": https://books.openedition.org/editionsbnf/2414).
- **[B]** Marianne Grivel, « Au Bon Pasteur, rue Montorgueil : une famille d'imagiers parisiens dans la
  seconde moitié du XVIe siècle », *Documents d'histoire parisienne*, n° 9, 2008, pp. 15–47;
  https://shs.hal.science/halshs-00602821 (cited after Lepape [9]).
- **[C]** Archives nationales, *Dénominations des voies de Paris* (street register), entries « rue des
  Petits Carreaux » (https://rdf.archives-nationales.culture.gouv.fr/place/FRAN_RI_025-d3nzchekdc-1oaf022uugsgq)
  and « rue au Comte d'Artois » — or, if the project prefers, the Ville de Paris register it already
  uses (same facts).

# A second reading of the 206 longer descriptions

Reviewed 3 November 2026, branch `detail-review`. One row per id in
`data/research/detail_review.csv`; this file is the same material arranged for a reader,
worst first. Nothing in `details.csv` or any other data file has been changed — every
`suggested_edit` is a suggestion.

One mechanical caveat before anything else: in `detail_review.csv`, and therefore in the
`issues` and `evidence` quoted below, **French accents are flattened to ASCII** — *Bievre*,
*siecle*, *prevot*. That is a limitation of how the rows were written, not of the sources.
Any quotation here should be re-copied from the source before it is used anywhere, which is
the rule this project already applies to its own quotations.

The mechanical checks in `scripts/ingest_detail.py` already prove each description against
the text it was written from. This pass asks the five things they cannot: is the source
itself right, is the text about the century the map shows, does it claim more than its
source does, does it conflate two things, and does it agree with the card it sits on.

## Counts

| verdict | shallow | deep | total |
|---|---:|---:|---:|
| `hold` | 4 | 16 | 20 |
| `edit` | 91 | 44 | 135 |
| `ok` | 50 | 1 | 51 |
| **total** | **145** | **61** | **206** |

`hold` means I can show the text is wrong, or that it is about something other than the
place on the card and no sentence-level change fixes that. `edit` means a named change makes
it publishable — for about half of these that change is deleting one sentence. `ok` means
I found nothing. **61 of the 206 were taken deep**: the Wikipedia article opened past the
extract the writer was given, its references read, and at least one further source
consulted. The other 145 had the shallow pass only — the description read against its
source text and its short description. Why that is short of the 70 asked for is under
*What I could not reach*.

A word on the proportion, because 155 of 206 marked `hold` or `edit` reads worse than it is.
20 are serious. About 35 more want a real rewrite. The remaining hundred are one-line
trims: a closing sentence about a 1972 street naming, a dropped *aurait*, a forename the
source does not give. They are grouped at the end rather than written out, because a
pattern is worth telling the author once.

---

## The twenty held back

These should not ship as they stand.

### 1. **L0450 — REUILLI** (Reuilly; village_faubourg, standing)

> Toponymists derive the name either from rubus, referring to brambles, or from the personal name
> Regullus. According to tradition, a Merovingian castle stood here where King Dagobert repudiated
> his wife Gomatrude in 629. In 1359, King John the Good promised the royal castle of Reuilly to
> Humbert II de Viennois, Patriarch of Alexandria, and in the 16th century it belonged to Humbert
> de la Tour-du-Pin. The Knights Templar established a domain here in 1152, granted by Mathieu de
> Beaumont, grand chamberlain to the king; the property passed to the Hospitallers after the
> suppression of the Templar order. Despite the presence of the castle, most of the land remained
> open wasteland until the early 17th century.

- source: the detail makes Humbert II de Viennois, patriarch of Alexandria, the man John the Good promised the castle to in 1359, and then "Humbert de la Tour-du-Pin" the owner in the 16th century - two owners two centuries apart. They are one man, and he died in 1355. The register's own entry is impossible on both counts and the detail passes it on, split in two; this is the Mathoniere case again (quote_verification.md, contradicted claim 4).

**Evidence.** fr.wikipedia, "Humbert II de Viennois" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Humbert_II_de_Viennois&action=raw: the article's subject is "Humbert de la Tour-du-Pin", known "sous le nom de Humbert II de Viennois", "le dernier dauphin de Viennois", born 1312 at La Tour-du-Pin, "Nomme patriarche d'Alexandrie le 31 janvier 1351", died "22 mai 1355" at Clermont. One man, dead four years before the 1359 promise and two centuries before the 16th-century ownership.

**Suggested.** Delete both sentences until the source is replaced. The Templar grant of 1152 by Mathieu de Beaumont, the passage to the Hospitallers, and Dagobert's repudiation of Gomatrude in 629 - which the detail rightly hedges as tradition - carry this card without them.

### 2. **L0145 — C. S. BARBE** (Collège Sainte-Barbe; college, rebuilt)

> The school stood in the rue Valette. Following its closure in June 1999, its buildings were
> remodelled by Louis-Ernest Lheureux (1827–1898) and later rehabilitated by Antoine Stinco. In
> addition to housing the interuniversity Bibliothèque Sainte-Barbe, the premises now accommodate
> one of the university centres of Panthéon-Assas University.

- source: "Following its closure in June 1999, its buildings were remodelled by Louis-Ernest Lheureux (1827-1898)" is impossible on its own face - the detail gives the architect's death year in the same sentence. The source attaches the remodelling to the buildings, not to the closure ("Ses batiments, reamenages par Louis-Ernest Lheureux (1827-1898) et rehabilites par Antoine Stinco, accueillent la bibliotheque"); the author turned a relative clause into a sequence.
- period: all four statements are 1881 or later, on a card about a school founded in 1460.
- consistency: the summary already gives the 1999 closure and the Bibliotheque Sainte-Barbe.

**Evidence.** fr.wikipedia, "College Sainte-Barbe (Paris)" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Coll%C3%A8ge_Sainte-Barbe_(Paris)&action=raw: for the Lheureux rebuilding, "Les demolitions commencent en 1881", with the new buildings opened about two years later - a century before the closure. The same article has the college in the map's own decade: Robert Dugast, head of the University and principal in 1553, bought the college and left it his fortune, gave it statutes on 19 November 1556, founded seven scholarships and "rebuilt and enlarged the premises"; the long Hubert-Lenormand dispute ended when the hotel des Coulons was annexed in 1556; the king of Portugal entrusted it with fifty pupils; Andre de Gouvea (1497-1548) was among its principals. Cited there to Jules Quicherat, Histoire de Sainte-Barbe, college, communaute, institution, Hachette, 1860-1864, 3 vols.

**Suggested.** Delete the whole text and write the 1550s from the article's body: "Robert Dugast, head of the University, bought the college and was its principal in 1553; he gave it statutes in 1556, founded seven scholarships and rebuilt the premises. The same year a long quarrel over the hotel des Coulons was settled and the house annexed. The king of Portugal sent fifty pupils."

### 3. **L0374 — R. DU RENART** (Rue Greneta; street, renamed)

> By an order of 2 April 1868, the rue du Renard Saint-Sauveur was combined with the rue
> Beaurepaire and the rue Greneta into a single street. The middle section, formerly the rue
> Beaurepaire between the rue Dussoubs and the rue Montorgueil, was recorded in 1255 as Bellus
> Locus, in 1258 as Bellus Reditus, and in 1313 as Beaurepaire. Meanwhile, the eastern section
> (rue Greneta) between the rue Saint-Martin and the rue Saint-Denis had older forms such as rue
> d'Arnetal, Darnetal, or Darnestat, and was also known as the rue de la Trinité.

- source: "The middle section, formerly the rue Beaurepaire between the rue Dussoubs and the rue Montorgueil" is wrong - Beaurepaire is the western end, and the middle section is the rue du Renard-Saint-Sauveur, which is this card's own street.
- consistency: the card is the rue du Renard-Saint-Sauveur and the detail never says what that street was; its 1313 rue Percee and 1383 rue du Renard appear only in the short description.
- period: the text opens on the 1868 merger.

**Evidence.** fr.wikipedia, "Rue Greneta" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Rue_Greneta&action=raw: the street "commence au 241, rue Saint-Martin et se termine au 72, rue Montorgueil", and its cross streets are listed "d'Est en Ouest" as boulevard de Sebastopol, rue de Palestro, rue Saint-Denis, rue Dussoubs. With the register's own three ranges - Greneta Saint-Martin to Saint-Denis, Renard-Saint-Sauveur Saint-Denis to Dussoubs, Beaurepaire Dussoubs to Montorgueil - the order east to west is Greneta, Renard, Beaurepaire, so the card's street is the middle one. Article cites Felix et Louis Lazare, Dictionnaire administratif et historique des rues de Paris, and Jean de La Tynna, Dictionnaire topographique... des rues de Paris, 1817.

**Suggested.** Put the card's own street first and fix the position: "Between the rue Saint-Denis and the rue Dussoubs, the street existed in 1313 as the rue Percee, then Perciee, and was the rue du Renard by 1383. In 1868 it became the middle section of the rue Greneta, with the rue Beaurepaire to the west and the old rue Greneta to the east."

### 4. **L0463 — LES FAUBOURS S. HONORE** (Rue du Faubourg-Saint-Honoré; village_faubourg, standing)

> In the Middle Ages, the road extended west from the original church of Saint-Honoré towards the
> Roule bridge. Following the construction of a new city gate in 1631, the name faubourg Saint-
> Honoré was applied to the stretch outside the wall as far as the Grand Égout. Urban development
> expanded rapidly from the late seventeenth century as wealthy financiers constructed townhouses
> along the road. Royal decrees in 1724 and 1726 attempted to curb building speculation by banning
> new streets and carriage gates in the suburbs, but local resistance and the city's outward
> expansion forced the crown to extend the building limits in 1740 and 1765. Later in the
> nineteenth century, Empress Eugénie had the house number 13 permanently removed from the street.

- source: "the name faubourg Saint-Honore was applied to the stretch outside the wall as far as the Grand Egout" reverses the source, which has the street running as far as the faubourg du Roule AFTER crossing the Grand Egout.
- overclaim: "local resistance and the city's outward expansion forced the crown to extend the building limits in 1740 and 1765" supplies a cause the source does not state - it reports the protest and the moved limits as separate facts.
- overclaim: the name was restricted from 1633, not 1631; 1631 is the gate's rebuilding, and the detail merges the two and loses 1633.
- period: only the first sentence is before 1550, and the text closes on Empress Eugenie and a missing house number 13.

**Evidence.** The supplied source_fr (fr.wikipedia, "Rue du Faubourg-Saint-Honore", Historique) reads: "A partir de 1633, cette appellation est reservee a la rue situee a l'ouest de la nouvelle porte Saint-Honore reconstruite en 1631 ... et qui va jusqu'au faubourg du Roule apres avoir traverse le Grand Egout, qui se situait approximativement au carrefour avec la rue du Colisee", and "les habitants du faubourg Saint-Honore s'insurgent et reclament un traitement privilegie" followed separately by "La limite d'interdiction de batir est reportee en 1740 ... et, le 10 fevrier 1765, jusqu'a la rue de Chaillot". The article's references for this stretch are E.-T. Lemaire, "Le developpement du faubourg Saint-Honore au XVIIIe siecle", Bulletin de la Societe historique de Paris et de l'Ile-de-France, 1957-1959, and Arch. nat., K 982.

**Suggested.** Fix the course - "as far as the faubourg du Roule, beyond the Grand Egout" - give 1633 for the name and 1631 for the gate, drop "forced", and cut the Eugenie sentence. Then the card still needs a pre-1550 source: all this source has for the map's century is the medieval road from the church of Saint-Honore to the pont du Roule.

### 5. **L0464 — LA VILLE LEVESQUE** (Rue de la Ville-l'Évêque; village_faubourg, vanished)

> Settled as early as the sixth century, the estate (Villa Episcopi) was granted to the bishop of
> Paris by King Dagobert I in the seventh century. It comprised agricultural land, a manor house,
> farms, and a river port. By the thirteenth century, the settlement had grown into an independent
> parish with a church dedicated to Saint Mary Magdalene, which was rebuilt in 1429. In 1613,
> Catherine and Marguerite d'Orléans-Longueville founded the Benedictine priory of Notre-Dame de
> Grâce within the village. The parish expanded significantly in the seventeenth century, and in
> 1659 Anne-Marie-Louise d'Orléans, known as the Grande Mademoiselle, laid the foundation stone of
> a larger church. The village was formally annexed to Paris in 1722.

- source: "a church dedicated to Saint Mary Magdalene, which was rebuilt in 1429" rests on a date that appears in this article and nowhere else the project holds - the article devoted to that church gives 1238, 1366 and 1492 and never 1429, and the Le Roule article in this same corpus says 1492 and 1660. One of the three is wrong and the detail picked the uncorroborated one.
- period: the back half is 1613, 1659 and 1722, while the article's 14th-century material - the bishop's couture in two parts, the Port-l'Eveque, the comparison with Saint-Germain-des-Pres - goes unused.

**Evidence.** fr.wikipedia, "Ancienne eglise de la Madeleine" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Ancienne_%C3%A9glise_de_la_Madeleine&action=raw: a chapel "attestee depuis 1238" (Antoine Krieger, La Madeleine, 1937, p. 28), "restauree en 1366" by Jean Le Coq (Krieger, p. 27), a new chapel to sainte Madeleine "adjointe en 1492 a l'eglise existante" with its first stone laid by Charles VIII (Krieger, p. 39), and the new building's first stone laid "le 7 juillet 1659" (Krieger, p. 37). No 1429 anywhere. Within this project's own corpus, the Le Roule source (L0465) says the church was "reconstruite en 1492 et 1660", and the Ville l'Eveque source says "reconstruite en 1429" - and the dedicated article dates the 1492 work as an addition to the existing church, not a rebuilding.

**Suggested.** Drop "which was rebuilt in 1429" until one of the three dates is settled from Krieger or Lazare. Replace the 1613 and 1659 sentences with the 14th-century couture: the bishop's land in two parts, one along the Seine served by the Port-l'Eveque, the other north of the chemin du Roule between the portes Saint-Honore and Montmartre - the Right Bank's answer to the faubourg Saint-Germain-des-Pres.

### 6. **L0174 — PORTE S. MARTIN** (Porte Saint-Martin (the triumphal arch of 1674 stands near the site); gate_wall, vanished)

> The replacement gate was erected in 1674 by order of Louis XIV to celebrate his victories on the
> Rhine and in Franche-Comté. Designed by the architect Pierre Bullet—a pupil of François Blondel,
> who built the nearby Porte Saint-Denis—it stands where the adjacent walls were later destroyed.
> The monument was listed as a historic monument in 1862, and restoration work was carried out in
> 1988.

- period: the whole text is the triumphal arch of 1674, not the medieval gate the card is about, and the card's own note says so.
- source: history_fr holds only the article's lead, which is about the arch; the article's Historique describes the gate on the map.
- voice: "it stands where the adjacent walls were later destroyed" fuses two unrelated source sentences into one that says nothing.

**Evidence.** fr.wikipedia, "Porte Saint-Martin", section Historique (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Porte_Saint-Martin&action=raw: the third gate, of the XIVe siecle, was "defendue par toute une bastide", belonged to the "Enceinte de Charles V", stood about 60 m south of the present arch at the crossing of the rue Saint-Martin with the rue Blondel and the rue Sainte-Apolline, and its bastide was "detruite en 1673". Cited there to Renaud Gagneux and Denis Prouvost, Sur les traces des enceintes de Paris, Parigramme, 2004, pp. 20, 36, 107, and to paris-atlas-historique.fr, "L'enceinte de Charles V vers 1450".

**Suggested.** Rewrite from the article's Historique, not its lead. Suggestion: "The gate on the map was the third of the name: a 14th-century gate of the wall of Charles V, defended by a bastide, standing about 60 metres south of the present arch where the rue Saint-Martin meets the rue Blondel. The bastide was pulled down in 1673, and the arch went up the next year." Delete the 1862 listing and the 1988 restoration.

### 7. **L0176 — PORTE S. DENIS** (Porte Saint-Denis (the triumphal arch of 1672 stands near the site); gate_wall, vanished)

> Designed by the architect François Blondel, the triumphal arch was built in 1673 to celebrate
> Louis XIV. It stands in today’s 10th arrondissement on the site of the former Paris gate in the
> ancient wall of Charles V, whose adjacent walls have since been destroyed. Regarded as one of
> the most representative monuments of the official art of its era.

- period: the whole text is the triumphal arch of 1673, not the medieval gate the card is about, and the card's own note says so.
- source: history_fr holds only the article's lead; the article's Historique describes the gate the map shows.
- consistency: the summary already says Louis XIV replaced the gate in 1672-1673, so the detail restates it and adds only the arch.
- voice: the last sentence has no main verb ("Regarded as one of the most representative monuments...").

**Evidence.** fr.wikipedia, "Porte Saint-Denis", section Historique (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Porte_Saint-Denis&action=raw: "La troisieme porte Saint-Denis, ou << bastide Saint-Denis >>, du [XIVe siecle], se trouvait 60 metres au sud de l'actuel arc de triomphe", and of the fourth, "a l'emplacement d'une porte medievale dans l'enceinte de Charles V". The same article dates the arch 1673 in its lead and "erigee en 1672" in its Historique, so the source contradicts itself on the year. Cited there to Gagneux and Prouvost, Sur les traces des enceintes de Paris, Parigramme, 2004, and to Perouse de Montclos, Histoire de l'architecture francaise, vol. II, pp. 317-318.

**Suggested.** Rewrite from the Historique: "The gate on the map was the third of the name, a 14th-century bastide of the wall of Charles V standing some 60 metres south of where the arch now is." Delete the whole of the present text, which is about the arch.

### 8. **L0025 — LA MONNOIE** ((gone); building, vanished)

> Created on 25 June 864 under King Charles II through the Edict of Pîtres, the Monnaie de Paris
> is the national minting institution of France. It is one of the oldest operating companies in
> the world and the oldest surviving French institution. Responsible for producing the nation's
> coinage, it functioned for centuries under direct government oversight as part of the Ministry
> of Economy, Finance and Industry. It gained full administrative autonomy and legal status as a
> public industrial and commercial establishment under a 2007 finance law.

- period: the detail is about the Monnaie de Paris as an institution today - "is the national minting institution of France", the Ministry of Economy, the 2007 finance law - on a card marked vanished for a building pulled down after 1775.
- source: the article never describes the old mint by the rue de la Monnaie at all, so no faithful detail from it can be about the thing on the map.
- overclaim: "one of the oldest operating companies in the world and the oldest surviving French institution" is a superlative about the modern body, not the building.
- voice: "King Charles II" will read to an English reader as the Stuart; the source means Charles le Chauve.

**Evidence.** fr.wikipedia, "Monnaie de Paris" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Monnaie_de_Paris&action=raw: the article does not mention the rue de la Monnaie, names no medieval or 16th-century premises for the Paris mint, and the only Paris site it gives before 1770 is a different one - "Olivier fonde ensuite la Monnaie du Moulin des Etuves sur l'extremite ouest de l'ile de la Cite a Paris" - while its only building is "un nouveau siege central a Paris" of 1770. The card's own note places the mint "by the rue de la Monnaie" until 1775, i.e. not that site.

**Suggested.** Return null for this source, or find one about the building: the card's neighbour L0394 (rue de la Monnaie) already carries the 1387 attestation of the street's name from the register, which is better evidence about this site than the institution's article is. If anything is kept, it is the 864 edit de Pitres and nothing after it.

### 9. **L0197 — LES MOULINS DES GOBELLIN** (Manufacture des Gobelins; other, rebuilt)

> The tapestry workshop was established in April 1601 under Henri IV, acting on the advice of his
> commerce advisor Barthélemy de Laffemas. Officially named the Manufacture nationale des Gobelins
> and located in the 13th arrondissement, its gallery was renovated starting in the late 1970s and
> reopened to the public on 12 May 2007 to mark its 400th anniversary. The complex and its grounds
> are classified as historical monuments.

- period: the detail is the Manufacture nationale des Gobelins as it is run today - its official name, its arrondissement, a gallery reopened on 12 May 2007, its monument listing - on a card labelled LES MOULINS DES GOBELLIN.
- source: and the article DOES carry the dye works, including the mill the map names, so the material was there and was passed over: Jehan Gobelin taking a house in the rue Mouffetard at the sign of the swan in 1443, his dyeing shop on the open Bievre, his reputation for scarlet reds, and the mill that took the family's name.
- consistency: the 1601 foundation under Henri IV is in the summary.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Manufacture des Gobelins", https://fr.wikipedia.org/w/index.php?title=Manufacture_des_Gobelins&action=raw: Jehan Gobelin "prit a loyer une maison rue Mouffetard a l'enseigne du cygne" (1443) and "etablit sur les bords de la Bievre, coulant en ce temps-la a ciel ouvert, un atelier de teinture"; he was "un teinturier de laine repute pour ses rouges a l'ecarlate, installe pres d'un moulin sur la Bievre"; "Ce moulin fut nomme << Moulin des Gobelins >>"; "la reputation des Gobelins eclipsa des lors celle des autres teinturiers"; the family, "alliee aux Le Peultre et aux Canaye", went on "pendant un siecle et demi a y perfectionner l'industrie tinctoriale"; and the family "paradoxalement ne fabriqua aucune tapisserie". Philibert Gobelin is cited to Guiffrey 1886, p. 338, Jehan's will of 1476 to Guiffrey 1904, and the site to Belhoste 1994, pp. 464-475.

**Suggested.** Delete the present text and write the dyers from the same article: Jehan Gobelin took a house in the rue Mouffetard at the sign of the swan in 1443 and set up a dye works on the Bievre, then still an open stream; his scarlets made the family's name, the mill beside them took it too, and they went on perfecting the trade for a century and a half - without ever weaving a tapestry.

### 10. **L0186 — RIVIERE DE SAINE** (Seine; other, standing)

> The river flows for 774.76 kilometres across the Paris Basin, rising at an altitude of 446
> metres at Source-Seine in Côte-d'Or on the Langres plateau. Following a general course from
> south-east to north-west, it passes through Troyes, Paris, Rouen, and Le Havre before emptying
> into the English Channel between Le Havre and Honfleur. Its drainage basin covers 79,000 square
> kilometres.

- period: the detail is a gazetteer entry for the river - 774.76 kilometres, a source at 446 metres, Troyes, Rouen, Le Havre, a 79,000 square kilometre basin - on a card whose subject is the Seine as this woodcut draws it. Nothing in it bears on Paris in 1550, and the article has nothing to put in its place: it is hydrographic and modern, with no medieval Paris navigation, no marchands de l'eau and no ports.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Seine", https://fr.wikipedia.org/w/index.php?title=Seine&action=raw: the article's pre-1600 content is the floods of 358 and 582, the Viking ascents from 841 and the treaty of Saint-Clair-sur-Epte of 911, and the building of the port of Le Havre in 1517 - nothing about the river at Paris, its watermen or its ports. Its mid-16th-century material is the floating of firewood down the Yonne and the Seine from the Morvan.

**Suggested.** Return null. The summary already says the one thing worth saying - that the river runs from the top of the sheet to the bottom because the map is printed east-up.

### 11. **L0118 — S. EUSTACE** (Église Saint-Eustache; church_religious, rebuilt)

> The church is dedicated to Saint Eustace, originally named Placidus or Placidas, a Roman general
> and hunting enthusiast who converted to Christianity. His symbols and attributes can be seen on
> both the interior and the exterior of the building. Intertwined letters S and E, hunting horns,
> and a stag bearing a cross between its antlers appear on pedestals inside the church as well as
> on the gables of the two transepts outside.

- period: all four sentences are about Saint Eustace the martyr - Placidus the Roman general, the monogram, the hunting horn, the stag with the cross - and none about the church. The card's own note says the map still shows the older church, replaced from 1532; the detail does not mention a building at all. This is the same failure as L0097, where the detail retold the Massacre of the Innocents instead of describing the cemetery.
- voice: "hunting enthusiast" for "amateur de chasse".

**Suggested.** Return null: the supplied lead carries only the dedication and the "third largest in Paris" that the summary has already used. A detail here needs a source about the fabric - the 1532 start, the older church it replaced - not about the saint.

### 12. **L0015 — LOSTEL DE LA VILE** (Hôtel de Ville; building, rebuilt)

> Commonly called the Hôtel de Ville, this building has housed the municipal institutions of Paris
> since 1357. Because Paris has experienced various insurrections throughout its history, the
> municipal building frequently became a rallying point for rioters, insurgents, and
> revolutionaries. It stands as a location deeply marked by history, witnessing moments from the
> time of Étienne Marcel to the Fronde, from the French Revolution to the revolutionary days of
> July 1830 and February 1848, and from the Commune to the Liberation of Paris. After being
> totally burned down at the end of the Paris Commune, it was rebuilt identically in the following
> years.

- period: the detail is the source's lead translated whole - a sweep of insurrections from Etienne Marcel to the Liberation - and says nothing about the building the map shows, although the article has it in detail.
- voice: "It stands as a location deeply marked by history, witnessing moments from..." is the brochure register the brief forbids.
- consistency: the 1357 date and the burning and identical rebuilding are both in the summary, so cutting the off-period material leaves nothing.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Hotel de ville de Paris", https://fr.wikipedia.org/w/index.php?title=H%C3%B4tel_de_ville_de_Paris&action=raw: the municipal officers obtained from Francois I in 1529 that the ruinous Maison aux Piliers "soit remplacee par un veritable palais de style Renaissance", "dessine par l'architecte italien Boccador"; "Sa construction debute en 1533", the first stone laid on 15 July by the prevot des marchands Pierre Violle; and "La partie sud est edifiee sous Francois Ier et Henri II de 1533 a 1551", the Wars of Religion then interrupting the work, the north part waiting for 1605-1628. Cited to Henri Stein, Boccador et l'Hotel de ville de Paris, Societe de l'Histoire de Paris, 1904, and Pierre Casselle and Francoise Masson, L'Hotel de ville de Paris, Imprimerie nationale, 1998, p. 19.

**Suggested.** Replace the whole text: "The officers of the city got leave from Francois I in 1529 to pull down the ruinous Maison aux Piliers and put up a Renaissance palace in its place, to the design of the Italian known as Boccador. The first stone was laid on 15 July 1533 by the prevot des marchands, Pierre Violle. On this sheet only the south range was rising; it was finished in 1551, and the Wars of Religion then stopped the work for half a century."

### 13. **L0029 — LOSTEL DALANCON** ((gone); building, vanished)

> The hôtel d'Alençon adjoined the hôtel du Petit-Bourbon, which stood opposite the drawbridge of
> the east gate of the medieval Louvre. The site lay between the fossé Saint-Germain-l'Auxerrois,
> now the southern section of the rue de l'Amiral-de-Coligny, and the former rue d'Autriche,
> bounded on one side by the Right Bank of the Seine.

- conflation: the source is the article on the hotel du Petit-Bourbon, which names the hotel d'Alencon only as its neighbour; the detail describes the Petit-Bourbon and then gives the Petit-Bourbon's boundaries as those of "the site" on this card.
- source: nothing in the supplied text is about the hotel d'Alencon itself, so per the brief's trap 2 this should have been null.

**Evidence.** The supplied source_fr is the lead of fr.wikipedia, "Hotel du Petit-Bourbon", which reads "attenant d'un cote a l'ancien hotel d'Alencon et de l'autre a la rive droite de la Seine" - the Seine frontage and the two boundary streets are the Petit-Bourbon's, and the hotel d'Alencon is the thing on the far side. No independent source on the hotel d'Alencon was opened, so this is a reading of the supplied text, not a verification of the building.

**Suggested.** Return null, or keep only what the source says of this house: "The hotel d'Alencon stood next to the hotel du Petit-Bourbon, on the side away from the river." Delete the second sentence, whose boundaries belong to the neighbour.

### 14. **L0328 — R. DES NOERS** (Boulevard Saint-Germain; street, renamed)

> The creation of the boulevard Saint-Germain led to the absorption or destruction of dozens of
> ancient Left Bank streets and alleys. A section of the rue des Noyers was initially taken over
> by the main thoroughfare, and the remaining portion of the street was officially incorporated
> into the boulevard by a prefectoral decree issued on 26 December 1893.

- source: the extract supplied is the register entry for the BOULEVARD SAINT-GERMAIN - a list of the twenty-odd streets the boulevard swallowed - and the card is the rue des Noyers. The detail is therefore wholly about the 19th-century boulevard that destroyed the street, and nothing in it can be trimmed to leave anything about the street the map shows.
- overclaim: "dozens of ancient Left Bank streets and alleys" is a count the register does not give; it names about twenty-five items.

**Suggested.** Return null for this source, and source the rue des Noyers from its own entry. The register's boulevard Saint-Germain entry is the wrong document for any of the streets it lists.

### 15. **L0413 — R. DES DEUS ESCUS** (Rue du Louvre; street, renamed)

> The creation of the rue du Louvre led to the suppression of the rue des Poulies between the rue
> de Rivoli and the rue Saint-Honoré, as well as the rue d'Orléans between the rue Saint-Honoré
> and the place des Deux Écus. In 1972, the section located between the quai du Louvre and the rue
> de Rivoli was renamed the rue de l'Amiral de Coligny.

- source: the extract is the register entry for the RUE DU LOUVRE, which lists what its opening suppressed, and the card is the rue des Poulies. The detail is the rue du Louvre's creation plus a 1972 renaming to rue de l'Amiral-de-Coligny; the rue des Poulies' own 1205 record and its name from a cloth-working device are in the short description and the detail never reaches them. Same case as L0328.

**Suggested.** Return null for this source. If the rue des Poulies is to have a detail it must come from its own register entry, or from Lazare, who has it under Poulies.

### 16. **L0447 — BISSESTRE** (Hôpital Bicêtre; village_faubourg, rebuilt)

> The university hospital is located at 78 rue du Général-Leclerc in the commune of Le Kremlin-
> Bicêtre, in Val-de-Marne. It forms part of the Assistance publique – Hôpitaux de Paris (AP-HP),
> occupying the site of the former hospice founded in the 17th century.

- period: the detail is the present-day university hospital - its street number, its commune, its departement, and its place in the AP-HP - on a card about the ruined castle of Bicetre on a 1550 sheet.
- source: LOG.md records that this card was "probed and skipped" because the article's history sections carry no pre-1600 reference, yet a detail written from its lead is live on the card.

**Evidence.** LOG.md, entry of 2026-11-02 (16:10), read 3 Nov 2026: "L0447 (Bicetre) and L0467 (Auteuil) were probed and skipped: their articles' history sections carry no pre-1600 reference either." The project had already judged this source unusable for this card.

**Suggested.** Return null. The summary already says what the map shows - a ruined castle, and Louis XIII's hospital for invalid soldiers on its site.

### 17. **L0138 — LE GRANT DECRET** ((gone); college, vanished)

> Tracing its origin back to the twelfth century, the faculty was one of the four main faculties
> of the old University of Paris. In 1679, it became the faculty of civil and canon law. Following
> its closure during the French Revolution in 1793, it was refounded in 1802 and became the new
> law faculty of Paris in 1808. The historic building constructed in 1771 on the place du Panthéon
> to house it is today shared between the universities of Paris I and Paris II.

- period: five of the six facts are 1679, 1771, 1793, 1802 and 1808, and the last sentence is about who occupies a 1771 building today; cutting them leaves about twenty words.
- source: history_fr is the article's lead, which runs from the 12th century straight to 1808; the article's body carries the medieval story the card wants.
- consistency: the card is marked vanished with no modern name, and the detail ends on a building that is "today shared between the universities of Paris I and Paris II".

**Evidence.** fr.wikipedia, "Faculte de droit de Paris" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Facult%C3%A9_de_droit_de_Paris&action=raw: the faculty "remonte son origine a 1170 au moins", and the 1679 edict restored the teaching of Roman law at Paris, "interdit depuis la decretale Super Specula d'Honorius III" - which is why the map's label reads LE GRANT DECRET and the school taught canon law alone. Cited there to Edouard Fournier, "L'enseignement des Decretales a l'universite de Paris au Moyen Age", Revue d'histoire de l'Eglise de France, vol. 26, 1940, pp. 58-59.

**Suggested.** Replace with the pre-1550 story the article supports: the schools go back to at least 1170; civil law had been barred at Paris since Honorius III's Super specula, so the faculty on the map taught canon law only, which is what "decret" means. Delete everything from "Following its closure" onwards.

### 18. **L0111 — LES IACOPINS** ((gone); church_religious, vanished)

> The convent was located at the site of present-day 158 rue Saint-Jacques. The name Jacobins
> derived from Saint-Jacques, as Jacques is Jacobus in Latin. Its teaching activity formed the
> Collège des Jacobins, a college within the former University of Paris. Suppressed in 1790 during
> the French Revolution, the convent buildings were demolished between 1800 and 1849. In 1849,
> Father Lacordaire re-established the Dominicans of the Saint-Jacques convent at a new site,
> located today at 20 rue des Tanneries in the 13th arrondissement.

- period: after the address and the etymology, everything is 1790, 1800-1849 and Lacordaire's refoundation of 1849; cutting those leaves about twenty usable words.
- source: history_fr is the lead; the article's body has the convent as it stood in the map's century.
- consistency: the summary says "It has disappeared", and the detail closes on a present-day address in the 13th arrondissement.
- overclaim: "Suppressed in 1790" - the source says the college was suppressed ("Supprime en 1790, ses batiments"), and the detail applies it to the convent.

**Evidence.** fr.wikipedia, "Couvent des Jacobins (rue Saint-Jacques)" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Couvent_des_Jacobins_(rue_Saint-Jacques)&action=raw: "En 1556, le don d'un riche bourgeois nomme Hennequin permet de reconstruire le cloitre de ces religieux" and "La salle des exercices, connue sous le nom d'ecoles Saint-Thomas, est quant a elle reconstruite en 1563"; under Louis XII the friars received "l'ancien parloir aux bourgeois", letting them spread beyond the wall of Philip Augustus; the church was "divisee en deux nefs par une colonnade centrale", about 20 m by 83 m, and "Saint Louis comble les Jacobins de ses bienfaits : il fait achever l'eglise". Cited there to Abbe Eugene Bernard, Les Dominicains dans l'universite de Paris, ou le grand couvent des Jacobins de la rue Saint-Jacques, 1883, and to Archives nationales, carton S 4229.

**Suggested.** Rewrite from the convent's own century: the two-naved church of about 20 by 83 metres finished under Saint Louis, the ground gained beyond Philip Augustus's wall under Louis XII, and the cloister rebuilt in 1556 on a bourgeois's gift - the map's sheet shows it a few years before that work. Delete the 1849 refoundation.

### 19. **L0461 — LES FAUBOURS S. GERMAIN** (Faubourg Saint-Germain; village_faubourg, standing)

> Urbanization of the faubourg beyond the medieval abbey settlement began in 1622 with the
> subdivision of the former estate of Marguerite de Valois, Queen Margot, between the Seine, the
> rue de l'Université, and the rue du Bac. During the mid-seventeenth century, the southern
> section was occupied mainly by religious houses, including the Novitiate of the Dominicans in
> 1632, the Carmelite convent in 1656, and the Missions Étrangères in 1663.  Following the
> construction of the Pont Royal in 1685–1689 and the court's move to Versailles, aristocratic
> townhouses rapidly replaced the Marais as the city's most fashionable quarter.

- period: every date in the text is 1622-1689; the map shows the faubourg in 1550 and nothing in the detail is about it.
- source: the article has no content at all before 1600 - its Historique opens "Le faubourg Saint-Germain s'urbanise au cours des XVIIe et XVIIIe siecles" - so no faithful detail from this source can be about the map's century.
- overclaim: the source dates the faubourg's rise to the fashionable quarter to the early 18th century and the Regence, not to the Pont Royal; the detail moves it some thirty years earlier and adds "rapidly".

**Evidence.** fr.wikipedia, "Faubourg Saint-Germain" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Faubourg_Saint-Germain&action=raw: the earliest date in the article is 1622, and on the Marais it says "Cette tendance se renforce au debut du XVIIIe siecle, notamment durant la Regence" ... "devient le quartier a la mode, le << noble faubourg >>, alors que le quartier du Marais amorce son declin" - a different moment from the 1685-1689 Pont Royal the detail ties it to.

**Suggested.** Return null for this source, or source the card afresh (the abbey's bourg, the Pre-aux-Clercs, the foire Saint-Germain) - the article behind it begins in the 17th century. If it must ship, at minimum: "...favoured building along the rue de l'Universite and the rue de Grenelle; the faubourg became the fashionable quarter in the early 18th century, as the Marais began to decline."

### 20. **L0034 — LOSTEL DE NELLE** (Institut de France and Monnaie de Paris (on its site); building, vanished)

> Constructed at the beginning of the 13th century, the Tour de Nesle formed one of the corner
> towers of the city wall built by Philip Augustus. The vanished tower stood at the exact site now
> occupied by the eastern pavilion of the Institut de France. It was described historically as
> unquestionably the most famous of all the towers in old Paris.

- conflation: the card is the hotel de Nesle and the detail is about the Tour de Nesle throughout; the card's own note says the article covers the tower.
- overclaim: "It was described historically as unquestionably the most famous of all the towers in old Paris" turns a named antiquarian's opinion of 1853 into an established historical description, and strips both the attribution and the date.
- source: the same article carries the house's own 1550s story, which the detail does not use.

**Evidence.** fr.wikipedia, "Tour de Nesle" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Tour_de_Nesle&action=raw: the sentence is a block quotation attributed to Alfred Bonnardot, footnoted to his Dissertations archeologiques sur les anciennes enceintes de Paris, J.-B. Dumoulin, Paris, 1853, p. 37. The same article on the house: in 1523 Francois I installed the bailli de Paris in the hotel to judge cases touching the University's privileges; the post was abolished in 1526 and "L'hotel resta inoccupe"; in 1552 Henri II decided to sell the property in lots, a sale not carried out, Charles IX renewing the letters patent in 1570; and in 1582 the hotel de Nevers was built on the site, keeping the duc de Berry's grande galerie.

**Suggested.** Write the house, not the tower: "Francois I put the bailli de Paris in the hotel in 1523 to hear cases touching the University's privileges; the post went in 1526 and the house stood empty. In 1552 Henri II decided to sell it off in lots - the sale this map's Paris was waiting for - and it did not go through. The hotel de Nevers replaced it in 1582." If Bonnardot's line is kept, attribute it: "Alfred Bonnardot called it, in 1853, the best known of all the towers of old Paris."
---

## The edits that matter, worst first

63 of the 135 `edit` rows are written out here. The rest follow in tables,
and every row is in the CSV in full.

### 1. **L0058 — S. MARI** (Église Saint-Merri; church_religious, standing)  — *deep*

- consistency: the detail says the church was "built between 1500 and 1565" while the short description directly above it says 1500-1550 "so it was brand new when this map was made". One of the two is wrong and the card prints both.
- period: the closing sentence is the present-day organ and picture collection.
- overclaim: "is regarded as one of the four daughters of Notre-Dame" is fine, but the detail opens on Saint Medericus's death in 700 and his relics rather than on the church.

**Evidence.** fr.wikipedia, "Eglise Saint-Merri" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=%C3%89glise_Saint-Merri&action=raw: the lead and the infobox both give "Construite de 1500 a 1565", and the architecture section breaks it down as "la nef entre 1500 et 1515, le transept entre 1525 et 1535, le choeur entre 1535 et 1565", cited to Agnes Bos, Les eglises flamboyantes de Paris : XVe-XVIe s, Picard, 2003, p. 239. The same article also says in its own choir section "Le choeur, acheve en 1552", so the article contradicts itself; the only 1550 in it is the date of the Truschet and Hoyau plan.

**Suggested.** Settle the date against Bos 2003, p. 239 and make the summary and the detail agree. If 1565 stands, the summary's "brand new when this map was made" needs rewording - on this sheet the nave and transept were up and the choir was still going. Cut the organ sentence.

### 2. **L0156 — CLUGNI** ((gone); college, vanished)  — *deep*

- overclaim: the source is in the conditional - "Son emplacement se situerait de nos jours", "s'etendrait approximativement" - and the detail states it flatly. This is the brief's own case of a hedge the source made and the description dropped.
- period: the detail is a modern street-by-street location and the present Hotel des 3 Colleges, where the article has the college itself, built in one campaign in the 1270s and 1280s and standing unchanged until the 19th century.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "College de Cluny", https://fr.wikipedia.org/w/index.php?title=Coll%C3%A8ge_de_Cluny&action=raw: the college was "fonde en 1269 par Yves de Vergy dit de Beaumont, abbe de Cluny" for Cluniac novices studying at Paris; he walled the site and built refectory, kitchen, dormitory and cloister, half the cloister standing at his death in 1275; his nephew Yves de Chasant (1275-1289) finished the cloister and built the chapel, chapter house and library; the building went up "d'une traite" and stayed in its original state until the 19th century; Jacques d'Amboise, abbot of Cluny, later had repairs made. Cited to Aubert de la Chesnaye des Bois, Dictionnaire de la noblesse, 1771, p. 197, Emile Raunie, Epitaphier du vieux Paris, vol. 3, 1901, pp. 117-142, and Dulaure, Histoire physique, civile et morale de Paris, 1837, vol. 2, p. 301.

**Suggested.** Replace with the college: Yves de Vergy, abbot of Cluny, walled the ground and raised refectory, kitchen, dormitory and cloister; his nephew finished the cloister and added chapel, chapter house and library. It was built in one campaign and stood unaltered until the 19th century - so what the map shows is the house of 1269 almost untouched. Restore the conditional on the site.

### 3. **L0449 — BANIOLET** (Bagnolet; village_faubourg, standing)

- overclaim: "Charles VI also granted the nearby manor of Mallassis to his mistress Odette de Champdivers" drops the source's hedge - "Cette propriete a vraisemblablement ete donnee par Charles VI a sa maitresse". The grant is probable, not recorded.

**Suggested.** "The manor of Mallassis close by was probably given by Charles VI to his mistress Odette de Champdivers." Everything else here is exact, including "Les Brieres sur le plan", which the source itself supplies - this is the strongest entry in the village set.

### 4. **L0458 — CLINNIENCOURT** (Clignancourt; village_faubourg, standing)

- overclaim: "The hamlet's name comes from Clenini Curtis, named after a Gallo-Roman villa owner" drops both the attribution and the conditional - the source reads "D'apres l'Abbe Lebeuf, son nom PROVIENDRAIT de Clenini Curtis ... du nom d'un certain Cleninus, proprietaire d'une villa gallo-romaine, decouverte en 1738".

**Suggested.** "The Abbe Lebeuf derived the name from Clenini Curtis, after a Cleninus whose Gallo-Roman villa was found here in 1738." The 9 September 1465 vintage, taken from Jean de Roye's chronicle, is the best sentence in the whole village set.

### 5. **L0044 — S. MEDART** (Église Saint-Médard; church_religious, standing)

- overclaim: two of the source's hedges are dropped. The source has "sans doute deja un oratoire" at the 6th or 7th century and "une chapelle dediee a saint Medard AURAIT ETE construite" in the 9th; the detail states both flatly ("A Christian cemetery and chapel existed on this site", "a chapel dedicated to Saint Medard stood along the Roman road").

**Suggested.** "A Christian cemetery and probably an oratory were here by the sixth or seventh century, and a chapel to Saint Medard is said to have stood by the ninth...". The December 1561 Tumulte de Saint-Medard, which interrupted the building work, is exactly the right thing for a card about this church in 1550 and is well handled.

### 6. **L0349 — R. DES LONBARS** (Rue des Lombards; street, standing)

- overclaim: the register hedges the Pourpointerie - "une partie de cette voie AURAIT ETE denommee rue de la Pourpointerie en 1612 et 1636" - and the detail states it flatly ("A portion of it is recorded as"). The second hedge, on rue Alain de Dampierre, is kept, so the two are treated differently in one sentence.
- overclaim: "Henri Sauval" for the register's "Sauval".

**Suggested.** "A part of it is said to have been called the rue de la Pourpointerie in 1612 and 1636", and "Sauval".

### 7. **L0392 — R. DES BOURDONNOIS** (Rue des Bourdonnais; street, standing)

- overclaim: "the section called the rue des Bourdonnais was named after Adam Bourdon and Guillaume Bourdon" turns two attested street names into an etymology. The register says only that at the end of the 13th century it was called "rue Adam Bourdon, rue Guillaume Bourdon et rue Sire Guillaume Bourdon"; the card's own summary hedges the question - "whose name may come from a family called Bourdon" - and the detail answers it.

**Suggested.** "At the end of the 13th century it appears as the rue Adam Bourdon, the rue Guillaume Bourdon and the rue Sire Guillaume Bourdon, and as the rue des Bourdonnais from the early 14th." The 1530 rue des Etuves aux Femmes is the best fact here and should not be buried.

### 8. **L0441 — PERCI** (Bercy; village_faubourg, standing)

- overclaim: "Bercy is shown as a feudal fortress with a donjon" drops two hedges at once - the source says the old plans show "une sorte de forteresse d'aspect feodal", a sort of fortress of feudal appearance. What the map shows is how the place looked, which is not the same as what it was.

**Suggested.** "On this map and other plans of the same years Bercy appears as a kind of fortress, feudal in look, with a keep inside a walled enclosure and a fortified gate near the Seine." Everything else in this entry is exact, including the forty horsemen and the windmill, and it is one of the best in the set.

### 9. **L0451 — PROPINCOURT** (Rue Popincourt (11th arrondissement); village_faubourg, standing)

- overclaim: "By 1550, a cluster of about fifteen houses had formed the hamlet" - the source says "Cent cinquante ans plus tard, le carrefour s'est garni d'une quinzaine de maisons", a hundred and fifty years after the manor of about 1400. The date is the author's arithmetic presented as a record, and it lands on the one year ingest_detail.py's year check waives as the sheet's own date, so nothing would have caught it.

**Suggested.** "A century and a half later the crossroads had gathered some fifteen houses, the first hamlet of Popincourt, just outside the wall of Charles V." The 1561 Reformed temple and its destruction the next year are exact and are the best thing in the entry.

### 10. **L0262 — R. COURAULAIN** (Rue de Montmorency; street, renamed)  — *deep*

- overclaim: "The mapmaker Lacaille" - the source says only "Lacaille", and Jean de La Caille was a printer-bookseller who published a plan, not a mapmaker; the trade is the detail's own addition.
- period: six of the seven dates are 1768, 1793, 1806 and 1808; the 14th-century name and the 1328 ruelle au Villain, which are the map-relevant part, get one clause each.

**Evidence.** data.bnf.fr, authority record for Jean de La Caille (1645-1723), https://data.bnf.fr/12192872/jean_de_la_caille/fr.pdf: he is recorded as an imprimeur-libraire who succeeded Denis II Thierry as printer-bookseller to the police in 1712, and the Description de la ville et des fauxbourgs de Paris en vingt planches (1714) is listed under him in that capacity. So "Lacaille" in the street register is an authority who published a plan in twenty plates, which is not the same as being its maker.

**Suggested.** "Lacaille writes rue Courtauvillain, and rue or ruelle Auvillain" - give him no trade. Lead on the 1328 ruelle au Villain and the rue du Seigneur de Montmorency, and compress the 1768-1808 renamings into one clause.

### 11. **L0309 — R. MONT MORANCI** (Rue de Montmorency; street, standing)  — *deep*

- consistency: the card is the western stretch - its summary is the lord of Montmorency's street and Flamel's house - and the detail is entirely about the eastern stretch between the rue Beaubourg and the rue du Temple, which is the neighbouring card L0262; a reader is told "This eastern segment adopted the name rue de Montmorency in 1768" on a card whose own street carried that name from the 14th century.
- overclaim: "the entire street was renamed the rue de la Reunion" - the source's "elle" is the eastern part under discussion, and the register does not say the whole street took the name.
- overclaim: "The cartographer Lacaille", as at L0262.

**Evidence.** data.bnf.fr, authority record for Jean de La Caille (1645-1723), https://data.bnf.fr/12192872/jean_de_la_caille/fr.pdf: imprimeur-libraire, printer-bookseller to the police from 1712, under whom the Description de la ville et des fauxbourgs de Paris en vingt planches (1714) is listed. The register's "Lacaille" is a published authority, not a cartographer. The split of the street is the register's own: "La partie situee entre les rues Saint-Martin et Beaubourg... rue du Seigneur de Montmorency. La partie situee entre les rues Beaubourg et du Temple... la ruelle au Villain."

**Suggested.** Write this card from its own stretch: "From the 14th century the part between the rue Saint-Martin and the rue Beaubourg was the rue du Seigneur de Montmorency, after the lord whose house stood on it." Then, if the eastern stretch is mentioned at all, say plainly that it is the neighbouring section. Cut "the entire street" and Lacaille's trade.

### 12. **L0221 — R. DES CELLESTINS** (Rue du Petit-Musc; street, renamed)

- overclaim: "the historian Corrozet" - the register says only "Corrozet", and he was a bookseller and author, not a historian. He is also not a stranger to this project: the 1532 book in which he calls the street the rue de la Petite Pusse is the Fleur des antiquitez, whose poem is printed on this very map, and the site's own pages say so. L0401 gets this right ("Gilles Corrozet's 1532 guide"); L0398 writes bare "Corrozet"; this card invents a trade. Three cards, three treatments.

**Evidence.** data/research/library_verification.md §1-2 and §6 of this repository, read 3 Nov 2026: Corrozet's own 1550 imprint reads "A PARIS, Au Palais, en la boutique de Gilles Corrozet", and he describes the 1532 Fleur as "vn petit liuret ainsi intitule, lequel i'ay supprime & mis a neant" - an author and bookseller writing about his own earlier book. The project's own notes already establish him as "bookseller at the Palais".

**Suggested.** "Corrozet, in his Fleur des antiquitez of 1532, calls it the rue de la Petite Pusse" - and note for the reader that this is the same Corrozet whose verses are printed on the map.

### 13. **L0229 — R. VERCEE** (Rue du Prévôt; street, renamed)

- overclaim: three additions the register does not make - "the historian La Tynna", "Felix Lazare" (the 1844 dictionary is by the brothers Felix and Louis Lazare), and, worse, "Later sources distinguished it from other streets of the same name", which invents the reason the saints' names were added. Streets of the same name are the project's known trap, and a guess about why one was distinguished from another is exactly what should not be written.

**Evidence.** The attribution is settled from fr.wikipedia, "Rue Greneta" (read 3 Nov 2026), which cites "Felix et Louis Lazare, Dictionnaire administratif et historique des rues de Paris et de ses monuments" and refers to "Les freres Lazare"; the same two-author form is used in the references of fr.wikipedia, "Ville l'Eveque" (edition de 1844, p. 403), which is a source this project already holds.

**Suggested.** "La Tynna has it as the rue Percee Saint-Paul in 1816; the Lazare brothers' dictionary of 1844 as the rue Percee Saint-Antoine." Drop the sentence about distinguishing it from other streets.

### 14. **L0313 — R. QUI QUEN POIX** (Rue Quincampoix; street, standing)  — *deep*

- overclaim: "Quiquenpoit by Jacques Androuet du Cerceau, and Quinquempoix by Jean-Baptiste-Michel Jaillot" - the register writes only "(Ducerceau)" and "(Jaillot)". Both expansions turn out to be right, and both are corroborated inside this project's own corpus, so the fault is not the identification but the silent supplying of it: the brief asks for additions to be declared, not slipped in.

**Evidence.** Both names are confirmed from sources this project already holds. For du Cerceau: data/places_streets.csv, note for L0356, "as on Ducerceau's plan of 1555", and the sources_long extracts for L0441 and L0442, "plan de Truschet et Hoyau et plan de Jacques Androuet du Cerceau dessines vers 1550". For Jaillot: the fr.wikipedia article "Couvent des Cordelieres (Paris)" (read 3 Nov 2026) cites "J.B.M. Renou de Chauvigne Jaillot, Recherches critiques : historiques et topographiques sur la ville de Paris, vol. 4, Lottin, 1779", and the "Filles-Dieu" article cites the same work as by "Jean-Baptiste Michel Jaillot" - the authority the street register means.

**Suggested.** Write "Ducerceau" and "Jaillot" as the register does, and put the full names in the card's sources, where a reader can see where they come from.

### 15. **L0319 — R. IEHAN PIN MOLET** ((gone); street, vanished)

- overclaim: three additions the source does not make - "Henri" Sauval (the register says only "Sauval"), "the 16th-century map of the Tapisserie" (the register gives no date, and published datings of the plan de la Tapisserie range over c. 1540, 1547 and c. 1550, with the tapestry itself about 1571), and "briefly" of the 1851 designation.
- voice: the street is called "the passage" in the third sentence, a word the source does not use.

**Evidence.** No page on the plan de la Tapisserie was opened and read, so its dating is reported from catalogue descriptions seen in search results only (Princeton's facsimile record labels it 1547, a Merian caption c. 1540 with the tapestry c. 1571, a dealer listing c. 1550). The finding is that the source gives no date, not that 16th-century is wrong. Marked shallow for that reason.

**Suggested.** "Sauval claims it was once called the rue du Croc; the plan de la Tapisserie gives it the name la Radrerie." Drop "Henri", "16th-century", "briefly" and "passage".

### 16. **L0323 — LA TANNERIE** ((gone); street, vanished)

- overclaim: "the 17th-century historian Henri Sauval" - the register says only "Sauval dit". Both the forename and the century are supplied, as at L0319 and L0349; the site does assert them elsewhere (L0410's summary calls him "Henri Sauval, a 17th-century historian of Paris"), but not in this source.
- period: the place is called "place de l'Hotel-de-Ville" where the card's own summary uses its 1550 name, the place de Greve, and the same slip is at L0322.
- consistency: the clearance for the avenue Victoria is in the summary.

**Suggested.** "Sauval says it was once called the ruelle de la Planche aux Teinturiers." Use "place de Greve" on a card about 1550, and cut the closing sentence.

### 17. **L0339 — R. PAVEE** ((gone); street, vanished)

- overclaim: "the 17th-century plan of Blondel" - the register says only "Sur le plan de Blondel"; the century is supplied.
- consistency: the summary gives the later name as the rue du Petit-Hurleur, on Cousin's authority, and the detail gives "rue du Petit Leu" from the register, with nothing to tell a reader that these are two sources differing about the same street.

**Suggested.** "On Blondel's plan it is the rue du Petit Leu." And say that Cousin's rue du Petit-Hurleur and the register's rue du Petit Leu are two readings of the same street, which is worth more than either on its own.

### 18. **L0352 — R. DE LA SERPENTE** ((gone); street, vanished)

- overclaim: "the 16th-century plan of Jacques Androuet du Cerceau" and "the adjoining rue du Chevalier-du-Guet" - the register says only "d'apres le plan de Ducerceau" and does not say the two streets adjoin. The identification is sound within this project, which dates that plan 1555 on the neighbouring card L0356, but it is not in this source.

**Suggested.** "On Ducerceau's plan this street and the rue du Chevalier-du-Guet both carry the name rue de la Serpente."

### 19. **L0355 — LA VIEILLE PELETERIE** ((gone); street, vanished)

- overclaim: "The cartographer Lacaille" adds a trade the register does not give (see L0262); "it was originally called the rue Macra Madiana" hardens the source's conditional "elle se serait appelee", and adds "originally"; "later recorded it as" adds a sequence the register does not give.
- period: the closing two clauses are the 1806 and 1814 renamings, and the 1786 edict on the riverside houses - the one thing here about the street as a place - is left to the summary.

**Suggested.** "Older deeds are said to have called it the rue Macra Madiana; Lacaille names it the rue de la Vieille Pelleterie, a name it already bore in 1183." Cut the Desaix renaming.

### 20. **L0438 — R. DE SEINE** (Rue de Seine; street, standing)

- overclaim: "According to the historian Sauval" adds a trade the register does not give, and "temporarily named it rue du Senat" adds a judgement the register does not make.
- voice: "prefectural decree", as at L0367.

**Suggested.** "Sauval has it that it also bore the name rue Dauphine. A prefectoral decree of 26 February 1867 named it rue du Senat." The 1489 rue de Seine is the fact that matters.

### 21. **L0188 — LILE DE LOUVIERS** (Boulevard Morland (the island was joined to the bank in 1843); other, vanished)  — *deep*

- voice: four sentences of alternative names and nothing about the island, when the article has its owner, its use and the one building this very map shows.
- overclaim: "the historian Jacques-Antoine Dulaure" adds a trade the source does not give.
- consistency: the summary says the island was "used for storing timber and hay", and the article dates the timber-merchants' lease to 1700, so a post-1550 use is being given as the island's character on a card about 1550.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Ile Louviers", https://fr.wikipedia.org/w/index.php?title=%C3%8Ele_Louviers&action=raw: "Cette ile appartenait en 1408 a Nicolas de Louviers", prevot des marchands, who gave it his name, and "a l'origine, elle etait couverte de paturages" (Theophile Lavallee, Histoire de Paris depuis le temps des Gaulois jusqu'a nos jours, 2nd ed., 1857, vol. II, ch. 2, p. 8); "Elle fut longtemps un terrain d'exercice pour les arbaletriers"; and it carried "un petit fort et d'une espece de havre pour donner au roi Henri II un spectacle de siege et de combat naval" (Dictionnaire historique des rues de Paris, 1997, vol. 1, p. 43) - which the article identifies as "la seule construction figuree sur le plan de Truschet et Hoyau, vers 1550". The timber-merchants' lease it dates to 1700.

**Suggested.** Replace the name list: "The island belonged in 1408 to Nicolas de Louviers, prevot des marchands, who gave it his name. It was pasture, and long a shooting ground for the crossbowmen. The one building on it here is probably the small fort and harbour put up so that Henri II could be given a mock siege and a naval battle."

### 22. **L0446 — GENTILI** (Gentilly; village_faubourg, standing)  — *deep*

- overclaim: "King Louis IX founded a Carthusian monastery here in the 13th century" - the source says only "Saint Louis y batit un monastere pour les chartreux" and gives no date; the century is supplied. The claim is also uncited in the article, and the Carthusian house Saint Louis endowed outside Paris is normally the Chartreuse de Vauvert, on the ground now under the Jardin du Luxembourg, so it is worth a second source before it is stated flatly.
- voice: the source has a motte and a ROUND tower, then a square tower inside an enclosure; the detail keeps only "a fortified square tower".

**Evidence.** On Vauvert: the Senat's own history of the Luxembourg garden and the Chartreuse's own site both place Saint Louis's Carthusian foundation at Vauvert, on the site of today's Jardin du Luxembourg, in 1257-1258 (jardin.senat.fr/en/history-heritage/history-of-the-garden.html; chartreuse.fr/en/paris-vauvert-chartreuse-site). Neither was read as a page on Gentilly, and one popular account does connect a prior of Gentilly with the Vauvert community, so this is recorded as a claim needing corroboration, NOT as a refutation.

**Suggested.** "Saint Louis built a house for the Carthusians here" - no century, until the claim is checked against Lebeuf or Lazare. And restore the round tower that preceded the square one.

### 23. **L0442 — CONFLANS** (Conflans (Charenton-le-Pont); village_faubourg, standing)

- overclaim: "the village dominates the confluence of the Seine and Marne" is the detail's own reading of the sheet; the source says only what the old plans show the village to have consisted of - the church of Saint-Pierre and the remains of the Sejour de Bourgogne - and that they depict the territory schematically.

**Suggested.** "On this map the village is little more than the church of Saint-Pierre and the remains of the 14th-century Sejour de Bourgogne." The rest - 865, 1358, 11 January 1436, the Sejour du Roi with stables for fifty horses, Gillette Hennequin in 1481 - is exact and is among the best writing in the set.

### 24. **L0444 — VITERI** (Vitry-sur-Seine; village_faubourg, standing)

- overclaim: "a parish survey recorded 47 households, or about 211 inhabitants" - the source says an archdeacon's visitation found the TWO parishes counting "environ 47 feux"; the detail drops "environ" from the households while keeping "about" for the inhabitants, and turns a visitation into a survey.

**Suggested.** "In 1462 an archdeacon's visitation put the two parishes at about 47 households, some 211 people." The hedge on the battle of Lutetia is well kept and the rest is exact.

### 25. **L0112 — LES FILLES DIEU** ((gone); church_religious, vanished)  — *deep*

- conflation: the source given to the writer is about the Filles-Dieu as a congregation and the card is their house on the rue Saint-Denis; the detail is wholly about the order - its habit, its houses in Orleans, Beauvais and Abbeville - and never reaches the convent the map shows.
- source: "Beyond their foundation in Paris, the order held its principal houses in Orleans, Beauvais, and Abbeville" misreads the source, which lists Paris as one of the four.
- period: the article on the house has its own 16th century in full and none of it is used.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Filles-Dieu", https://fr.wikipedia.org/w/index.php?title=Filles-Dieu&action=raw: the convent stood on the rue Saint-Denis with its garden running to the wall of Charles V; by letters patent of 27 December 1483 Charles VIII ordered the house to be held in future by reformed nuns of Fontevraud, carried out about 1495 by Jean-Simon de Champigny with nuns from the Madeleine priory near Orleans and from Fontaine near Meaux; Charles VIII laid the first stone of the church in 1495 and it was finished in 1508; and condemned prisoners on their way to the gibbet of Montfaucon kissed a crucifix before the church and were given bread and wine by the sisters, "le dernier morceau du Patient". Cited to Jean-Baptiste Michel Jaillot, Recherches critiques, historiques et topographiques sur la ville de Paris, pp. 26, 29ff, Raunie, Epitaphier du vieux Paris, t. IV, pp. 334-35, 342, Lazare p. 243 and Dulaure, Histoire de Paris, p. 123.

**Suggested.** Write the house: the church this sheet shows was begun in 1495, Charles VIII laying the first stone, and finished in 1508, twelve years after he had turned the house over to reformed nuns of Fontevraud. And the sisters' office that no reader will forget: the condemned on their way to Montfaucon stopped at the church door for a crucifix and a last piece of bread and wine.

### 26. **L0245 — R. DU ROI DE CECILE** (Rue du Roi-de-Sicile; street, standing)

- source: "rue Bouquetonne" is listed among the street's 14th-century names, but the register gives it as "rue Bouquetonne (Truschet)" - a citation of THIS map, which the card's own short description correctly reports as "this map labels [it] separately as the rue Bouquetonne". The detail drops the attribution, so a reading taken off this woodcut is presented as a medieval attestation.
- voice: 141 words, the longest entry in the set, consisting of nothing but name variants.

**Suggested.** "...rue du Hoqueton or Hoqueton le Faucheur in the 14th century, and rue Bouquetonne on this map." Then cut the Croix Blanche list to two or three names: at 141 words the entry has room for something that is not a name.

### 27. **L0021 — LE PALAYS** (Palais de Justice; building, rebuilt)  — *deep*

- consistency: the summary says the palace is still the seat of the highest courts and the detail says the courts left in the spring of 2018.
- period: the Terror and 2018 take three of five statements, while the article has the Palais in the map's own years - the Grand-Chambre renovated by Fra Giocondo and renamed the Chambre doree, Louis XII's new Chambre des comptes with its 1504 facade finished under Henri II, and Francois I's wedding at the marble table in 1530.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Palais de la Cite", https://fr.wikipedia.org/w/index.php?title=Palais_de_la_Cit%C3%A9&action=raw, throughout cited to Herveline Delhumeau, Le palais de la Cite, Du Palais des rois de France au Palais de Justice, Actes Sud, 2011, pp. 64, 75, 88, 90: Louis XII "fit edifier un escalier monumental couvert de voutes rampantes" and had a new Chambre des comptes built, its 1504 facade by Giovanni Giocondo, completed only under Henri II (p. 88); the Grand-Chambre renovated by Fra Giocondo, which gave it the name Chambre doree; Francois I "celebra autour de la table de marbre de la Grand-Salle ses noces avec Eleonore de Habsbourg" and received Charles Quint there in 1540. The article dates the Grand-Chambre's carved ceiling 1499 in one place and 1491 in another.

**Suggested.** Cut the last sentence and the Terror. "Louis XII had the Grand-Chambre done over by Fra Giocondo, which is how it came to be called the Chambre doree, and built a new Chambre des comptes whose facade of 1504 was finished only under Henri II. Francois I married Eleonore de Habsbourg at the marble table of the Grand-Salle."

### 28. **L0022 — LA CHAMBRE DES CONTES** ((gone); building, vanished)  — *deep*

- consistency: the detail opens with the summary's own first sentence and then defines what a chambre des comptes was; nothing in it is about the building the map labels.
- source: "la plus ancienne des Chambres des comptes apres l'Echiquier de Normandie" carries no reference in the article.
- period: the building on this sheet is Giocondo's of 1504-1511, and Henri II added an archive store across the rue de Nazareth in 1553, three years after the map - none of which is in the detail.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Chambre des comptes de Paris", https://fr.wikipedia.org/w/index.php?title=Chambre_des_comptes_de_Paris&action=raw: the chamber's building "occupe tout le cote ouest de la cour de la Sainte-Chapelle"; Giovanni Giocondo "a construit les nouveaux batiments de la Chambre des comptes a partir de 1504 jusqu'en 1511"; in 1553 Henri II added an archive depot across the rue de Nazareth; and "L'incendie du 27 octobre 1737 a detruit une grande partie des archives". No footnote is attached to the Exchequer-of-Normandy claim. Corroborated for 1504 by the Palais de la Cite article, citing Delhumeau 2011, p. 88.

**Suggested.** Write the building: "The chamber's new buildings, on the west side of the Sainte-Chapelle courtyard, were put up by Giovanni Giocondo between 1504 and 1511, and are the ones on this sheet; Henri II added an archive store across the rue de Nazareth in 1553."

### 29. **L0105 — S. CHAPPELLE** (Sainte-Chapelle; church_religious, standing)  — *deep*

- period: half the text is 1787-1797 - the canons, the closure, the Club de la Sainte-Chapelle, the archive store - while the article has the chapel exactly as the map shows it: the third spire begun about 1460, Charles VIII's Flamboyant rose on the west front, and Louis XII's staircase along the south wall.
- overclaim: "Designed as the first of the 'saintes chapelles'" reads as intent; the source says only that it was the first one built, and that sentence carries no reference.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Sainte-Chapelle", https://fr.wikipedia.org/w/index.php?title=Sainte-Chapelle&action=raw: "Vers 1460, la troisieme fleche de la Sainte-Chapelle avait ete entamee, peu avant la mort de Charles VII"; "Charles VIII fait poser une rose de style flamboyant sur la facade occidentale"; "Louis XII fait entamer la construction d'un escalier d'acces longeant la muraille sud". A caption notes that the 1630 fire destroyed the spire of 1460. No reference is attached to "Elle est la premiere construite des saintes chapelles".

**Suggested.** Cut from "A college of canons" onwards and put the late-medieval work in: the spire begun about 1460, Charles VIII's Flamboyant rose on the west front, Louis XII's staircase up the south wall - the chapel this sheet draws. And "the first of the saintes chapelles to be built".

### 30. **L0049 — S. VITOR** (Jussieu university campus (on its site); church_religious, vanished)  — *deep*

- period: the second half of the text is 1790, 1811, the halle aux vins, the 20th-century science faculty and the Jussieu campus, which the summary has already covered; the abbey as the map shows it gets nothing, although the article's 16th-century material is the best on the card.
- voice: "famous masters such as Hugh, Adam, Andrew, Richard, and Thomas Gallus" names four men by first name only.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Abbaye Saint-Victor de Paris", https://fr.wikipedia.org/w/index.php?title=Abbaye_Saint-Victor_de_Paris&action=raw: the abbey's library was "une des plus riches de France", its manuscripts chained in the reading room, and Rabelais sends Pantagruel to it in chapter VII - "Et trouva la librairie de sainct Victor fort magnifique" - with its catalogue of 139 invented titles. The article's bibliography cites a catalogue of the library based on Claude de Grandrue's repertory of 1514, and dates the abbey's foundation to 1113, when Louis VI turned the hermitage into an abbey. The masters are Hugh, Adam, Andrew and Richard of Saint-Victor (Ricossa 1999 p. 247 for Adam; Dahan 1990 p. 301 for Andrew).

**Suggested.** Cut everything from "Following its suppression" and put the library in: by the time of this map Saint-Victor's was among the richest libraries in France, its manuscripts chained to the desks, catalogued by Claude de Grandrue in 1514 - and mocked by Rabelais, who sends Pantagruel there to find it "fort magnifique". Name the masters "of Saint-Victor".

### 31. **L0091 — S. LADRE** ((gone); church_religious, vanished)  — *deep*

- period: the middle of the text is four modern street names and "parts of the former 3rd and 5th arrondissements" - the administrative-locator failure the brief and the log both name - while the article has the leper house itself, and the label on the map is S. LADRE, which the article explains.
- voice: "The recorded history of Saint-Lazare contains many gaps" is the best line here and is buried last.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Enclos Saint-Lazare", https://fr.wikipedia.org/w/index.php?title=Enclos_Saint-Lazare&action=raw: the enclosure is first mentioned in 1110 as "un hopital de lepreux, sous l'invocation de Saint-Ladre ou Saint-Lazare", covering about 92 arpents, some 32 hectares (Felix and Louis Lazare, Dictionnaire administratif et historique des rues de Paris, 1844-49, pp. 369-370); from about 1147 the "logiz du roy" at Saint-Lazare was a required halt for sovereigns on their accession, where kings and queens received the Parisians' oath of loyalty (Francois-Olivier Touati, Maladie et societe au Moyen Age, p. 223; Dulaure, Histoire physique, civile et morale de Paris, 1837, t. 1, p. 421), and sovereigns' bodies were shown there after death until Louis XV.

**Suggested.** Cut the street boundaries and the arrondissement numbers. "The house of Saint-Ladre, as the map calls it, is first named in 1110, a leper hospital of some 92 arpents. From about 1147 it was the king's halt: a sovereign coming to the throne stopped at Saint-Lazare to receive the Parisians' oath, and after death was shown there before burial." Keep the destroyed archives as the close.

### 32. **L0107 — S. SEVERIN** (Église Saint-Séverin; church_religious, standing)  — *deep*

- period: one of the three sentences is the 1789-90 confiscation and one a present-day property description, while the article has the church this sheet draws: burned in 1448, the spire finished in 1487, the chevet built 1489-1495, the nave's side chapels 1498-1520, five naves across, and the famous twisted pillar in the ambulatory.
- consistency: the summary already says the cloister survives and that it is still a parish church.
- source: of all those dates only the 1487 spire has a source in the article, a Paris history street panel.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Eglise Saint-Severin de Paris", https://fr.wikipedia.org/w/index.php?title=%C3%89glise_Saint-S%C3%A9verin_de_Paris&action=raw: the church was "partiellement detruite par un incendie" in 1448 and rebuilt "de la seconde moitie du XVe pour le reste"; "achevement de la fleche de la tour" in 1487 (cited to the Panneau Histoire de Paris); "construction du chevet" 1489-1495; "realisation des chapelles laterales de la nef" 1498-1520; the nave has "collateraux doubles", making "cinq nefs en largeur"; the ambulatory has "dix doubles travees de piliers originaux en forme de palmier", one of them "une colonne torsadee, ou colonne salomonique". All but the 1487 spire are uncited.

**Suggested.** Cut the last sentence and the 1789 parish count. "Fire took the church in 1448; the tower's spire was finished in 1487, the chevet built between 1489 and 1495, the nave's side chapels between 1498 and 1520 - so the church on this sheet was barely a generation old. Its ambulatory turns on palm-like piers, one of them twisted like a column of Solomon."

### 33. **L0119 — LES FILLES REPENTIS** ((gone); church_religious, vanished)  — *deep*

- period: the detail gives the order's later names and its popular nickname, where the article has the house in 1550 itself - kept under strict enclosure, its doors walled up, entry allowed only to workmen, a surgeon, royalty and bishops - and the church of 1495-1508 that the map draws.
- source: the article contradicts itself on who moved them to Saint-Magloire in 1572, saying Marie de Medicis in one place and Catherine de Medicis in another, and the detail passes the move on without the clash.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Augustines de l'ordre de la Penitence de la Madeleine", https://fr.wikipedia.org/w/index.php?title=Augustines_de_l%27ordre_de_la_P%C3%A9nitence_de_la_Madeleine&action=raw: founded 1492, 1493 or 1494 after two years of Lent and Advent preaching by Jean Tisserand at Notre-Dame, with about 200 women converted (Nicole Gilles, Les Annales et Chroniques de France); authorised by Charles VIII's letters patent of 14 September 1496, given the Rule of Saint Augustine by Alexander VI in October 1497, their statutes issued by Jean-Simon de Champigny; housed from 1498 in part of the hotel du Bouchage, also called the hotel d'Orleans, the whole bought back for 2,000 gold ecus, after which "Il fallut murer les portes a cause de la cloture"; in 1550 "obligees de garder la cloture", entry restricted to workers, a surgeon, royalty and bishops; moved by letters of 17 September 1572 to the chapel of Saint-Georges at Saint-Magloire. The article's own reference list includes "Plan de Truchet et Hoyau (c. 1550, publie 1553)".

**Suggested.** Write 1550: "By the middle of the century the house was held to strict enclosure - its doors walled up, and no one admitted but workmen, a surgeon, royalty and bishops. Charles VIII had authorised the community in 1496 and Alexander VI gave it the Rule of Saint Augustine the year after." And flag the Medicis contradiction.

### 34. **L0154 — C. SORBONNE** (Sorbonne; college, rebuilt)  — *deep*

- period: the closing sentence lists four present-day universities, which the brief names as a failure outright, and the 1257 foundation and Robert de Sorbon are in the summary, leaving Rabelais as the only pre-1600 content. The article meanwhile has the first printing press in the kingdom of France, set up in the college's own cloister in 1469 - which is the thing this project cares about most.
- source: the 15th- and 16th-century section has no inline citations and the article is tagged "a sourcer".

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "College de Sorbonne", https://fr.wikipedia.org/w/index.php?title=Coll%C3%A8ge_de_Sorbonne&action=raw: in 1469 Jean Heynlin, as rector, set up a printing workshop in the Saint-Benoit cloister, "le premier dans le royaume de France", with Guillaume Fichet; the first book printed in 1470 was the Epistolae of Gasparin de Bergame; and a lectureship was founded in 1532 by Ulrich Gering, one of the printers of that first press. The section carries no inline citation and the article is tagged "a sourcer" (November 2012).

**Suggested.** Cut the four universities. "The first printing press in the kingdom was set up in the college's own cloister in 1469 by its rector, Jean Heynlin, and printed its first book the next year; one of its printers, Ulrich Gering, endowed a lectureship here in 1532." Keep Rabelais.

### 35. **L0169 — LA BASTILLE** (Place de la Bastille; gate_wall, vanished)  — *deep*

- consistency: the only fact in the detail that the summary does not already carry is the old name; the 14th-century building, the position, the prison, the symbol of royal despotism and the destruction are all in the summary, restated in 50 words.
- period: the article has the Bastille of the map - the first stone laid by the prevot Hugues Aubriot on 22 April 1370, eight towers, one of them damaged by an exploding powder barrel about 1430, a fort guarding the road between the king's lodging and the Hotel Saint-Pol, and under Francois I a place of reception - and the detail has none of it.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Bastille", https://fr.wikipedia.org/w/index.php?title=Bastille&action=raw: built 1370-1383 "sous la direction du prevot de Paris Hugues Aubriot qui posa la premiere pierre le 22 avril 1370" (Roland Delachenal, Histoire de Charles V, vol. 4, 1928, p. 317; Frantz Funck-Brentano, Bibliotheque de l'ecole des chartes, 1894, p. 362); eight towers, the Puits tower damaged by a powder barrel about 1430 (Jacques Hillairet, La rue Saint-Antoine, 1970, p. 83); the first captain-governor Jehan de La Personne, named by Charles VI in 1386 (Fernand Bournon, La Bastille, 1893, pp. 76-78); the fort protected the route between the king's residence and the Hotel Saint-Pol and under Francois I served as a place of reception; it surrendered on 13 May 1588 and held out four days against Henri IV in 1594.

**Suggested.** Replace the restatement: "The prevot of Paris, Hugues Aubriot, laid the first stone on 22 April 1370; the work took to 1383 and gave it eight towers, one of them cracked by an exploding powder barrel about 1430. It guarded the road between the king's lodging and the Hotel Saint-Pol, and under Francois I the king received there."

### 36. **L0020 — LA CONCIERGERIE** (Conciergerie; building, standing)  — *deep*

- period: two of the four sentences are the Revolution and the present-day Centre des monuments nationaux, and the summary has already given the Revolution. The article has the Conciergerie as it worked in the map's century: the concierge's office, the salle des Gens d'Armes as hall and refectory for the guards and servants, the kitchen pavilion of about 1353, and two classes of cell - the rich and influential in their own rooms, the poorest in dark, damp, vermin-ridden holes.
- consistency: "It originally formed part of the old royal residence" repeats the summary.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Conciergerie de Paris", https://fr.wikipedia.org/w/index.php?title=Conciergerie_de_Paris&action=raw, cited throughout to Beatrice de Parseval and Guillaume Mazeau, La Conciergerie - Palais de la Cite, 2019, pp. 8, 14-15, 52-53, 65, and Monique Delon, same title, 2000: a concierge was appointed "pour superviser l'administration du palais" (p. 8); the salle des Gens d'Armes "servait de salle a manger et de lieu de rassemblement pour les gardes armes et les serviteurs" (pp. 52-53); "Le pavillon des cuisines a ete ajoute vers 1353" (pp. 14-15); and "Les prisonniers riches ou influents avaient generalement leurs propres cellules" while "Les plus pauvres etaient confines dans des cellules sombres, humides et infestees de vermine" (p. 65).

**Suggested.** Cut the Revolution and the monuments-nationaux sentences. "A concierge kept the palace for the king; the hall of the men-at-arms fed and mustered the guards and servants, with a kitchen pavilion added about 1353. Prisoners who could pay had rooms of their own, and the rest the dark and the damp below."

### 37. **L0024 — LOTEL DE CLUNI** (Musée de Cluny; building, standing)  — *deep*

- period: the closing sentence is the state's purchase in 1843, and the museum is in the summary; the article meanwhile has the house's own 16th century, which the detail passes over.
- voice: "the reluctance of Parisian architects" - the source says Parisian architecture.
- consistency: the detail says "the abbots of Cluny" where the article names the man who rebuilt it, Jacques d'Amboise, abbot 1485-1510, who is also the abbot who had repairs made at the college de Cluny on card L0156.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Hotel de Cluny", https://fr.wikipedia.org/w/index.php?title=H%C3%B4tel_de_Cluny&action=raw: the house was begun by Jean de Bourbon and "a ete agrandi par Jacques d'Amboise, abbe de Cluny (1485-1510)"; Mary Tudor "y est enfermee pendant 40 jours en janvier 1515" and there "epouse secretement et sans le consentement de son frere le roi Henri VIII" Charles Brandon; James V of Scotland "sejourna ainsi dans l'hotel durant les grandes festes et joutes donnees pour l'occasion" in 1536. The rebuilding date and the style claim are cited to Robert Ducher, Caracteristiques des styles, Flammarion, 1963, p. 80; the Mary Tudor and James V passages are uncited.

**Suggested.** Cut the 1843 sentence, write "Parisian architecture", and name the builder: Jacques d'Amboise, abbot of Cluny, enlarged the house between 1485 and 1510. If there is room, the English queen dowager shut up here for forty days in January 1515, who married Charles Brandon in it without her brother's leave, is the house's best story.

### 38. **L0033 — LE LOUVRE** (Louvre; building, rebuilt)  — *deep*

- period: the closing sentence lists the palace's present tenants.
- consistency: the card's whole point - the medieval castle being rebuilt, Lescot's wing begun in 1546 - is in the summary, and the detail jumps from Charles V to Henri IV, leaving out Francois I although the article is specific about him.
- source: "Over an 800-year construction history, the medieval castle and its keep were gradually demolished" welds two separate statements.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Palais du Louvre", https://fr.wikipedia.org/w/index.php?title=Palais_du_Louvre&action=raw: "En 1528 a lieu la destruction du donjon central"; "C'est le 2 aout 1546 que le projet de l'architecte Pierre Lescot" was adopted; "la mort de Francois Ier (en 1547) interrompt les travaux" with "le chantier est a peine commence"; and at Henri II's death in 1559 the castle was still "encore tres medieval" with "une seule aile de style Renaissance". Cited to Julie Degageux, "Le palais du Louvre au XVIe siecle", Documents d'histoire parisienne, no. 7, 2007, p. 31, Henri Zerner, "Lescot, Goujon et le Louvre", in L'Art de la Renaissance en France, Flammarion, 2002, pp. 155, 184, and Frederic Morvan, Louvre : les 300 chefs-d'oeuvre, Hazan, 2006, p. 9.

**Suggested.** Cut the last sentence and put the 1550s in: the great central keep came down in 1528, Lescot's design was adopted on 2 August 1546, Francois I's death the next year stopped the work almost as it started - so what this sheet shows is a castle still largely medieval with a single Renaissance wing.

### 39. **L0008 — LES TOURNELLES** (Place des Vosges (built on part of its site); building, vanished)  — *deep*

- overclaim: "temporarily converted into a powder magazine" - "temporarily" is added; "because she considered it outdated" turns the source's impersonal "ce palais juge demode" into Catherine de' Medici's own judgement.
- consistency: the abandonment and the sale for the Tuileries are both in the summary.
- period: the article has the Tournelles of the map - two parks of trees, six kitchen gardens and a ploughed field; Francois I lodging his mother Louise de Savoie and then Anne de Pisseleu there; Henri II feasting his coronation there in 1547 - and the detail has none of it.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Hotel des Tournelles", https://fr.wikipedia.org/w/index.php?title=H%C3%B4tel_des_Tournelles&action=raw: "Francois Ier ne l'habita pas, lui preferant le chateau de Fontainebleau" but lodged there "sa mere, Louise de Savoie, puis sa maitresse Anne de Pisseleu"; "Henri II y feta son sacre en 1547, puis la signature des traites du Cateau-Cambresis en 1559"; the domain held "deux parcs plantes d'arbres, six jardins potagers et un champ laboure"; after the joust in the rue Saint-Antoine, "la plus large rue de Paris a l'epoque", "Transporte a l'hotel des Tournelles, le roi y mourut le 10 juillet 1559"; and letters patent of 28 January 1563 ordered the demolition (Archives du royaume, section domaniale, serie 9, no. 1234). The article dates the tournament 29 June where the Porte Saint-Antoine article has 30 June.

**Suggested.** Replace with the place as it stood: two parks of trees, six kitchen gardens and a ploughed field; Francois I would not live there but kept his mother and then his mistress in it; Henri II feasted his coronation there in 1547 and was carried there to die in July 1559.

### 40. **L0132 — NAVARRE** ((gone); college, vanished)  — *deep*

- consistency: the card dates the foundation to 1304, but the article's own archival caption dates the founding act to 25 March 1305 (Archives nationales AE/II/308a-b), its external link gives a codicil of 31 March 1305, and the scholarly reference it cites is titled "de sa fondation (1305)". The 1304 in the lead has no footnote.
- consistency: the article lists Ronsard among the college's students, where card L0140 has him taught at Coqueret - both may be true but the site now says both without a word.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "College de Navarre", https://fr.wikipedia.org/w/index.php?title=Coll%C3%A8ge_de_Navarre&action=raw: the lead's "fonde en 1304" carries no footnote; the image caption cites "Archives nationales AE/II/308a et AE/II/308b" and dates the founding act 25 March 1305; the external link is to "Actes royaux, actes 2945 et 2946 : 31 mars 1305. Codicille du testament relatif au college de Navarre"; and the bibliography cites Nathalie Gorochov, "Le college de Navarre de sa fondation (1305) au debut du XVe (1418)", 1997. Among its students the article lists "Jacques Amyot (1513-1593)", "Pierre de La Ramee (1515-1572)", "Jacques Peletier du Mans (1517-1582)" and "Pierre de Ronsard (1524-1585)"; among its grands maitres "Pierre Duval ou de Vale (1509)", "Olivier de Lyon (1518)", "Pierre Loret (1525)" and "Mathurin Cordier (1528-15??)".

**Suggested.** Settle 1304 against 1305 from Gorochov or the Archives nationales act, and make the summary agree. The detail itself would be better spent on the college in the map's own years: Pierre Loret and Mathurin Cordier as grands maitres in the 1520s, and Amyot, La Ramee, Peletier du Mans and Ronsard passing through.

### 41. **L0127 — S. GERMAIN DES PRES** (Église Saint-Germain-des-Prés; church_religious, standing)  — *deep*

- period: the detail is excellent to 1163 and stops there, so the abbey the map actually draws - a monastery fortified and moated, which is what the woodcut shows - is absent. The article has it: Charles V required the abbey in 1368 to dig a ditch like the city's, fed by a channel called the Petite Seine, and an earlier abbot "fait reparer l'eglise et fortifier le monastere". It also has the 1533 quarrel with the scholars, put down on the Pre-aux-Clercs on 20 March 1557.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Abbaye de Saint-Germain-des-Pres", https://fr.wikipedia.org/w/index.php?title=Abbaye_de_Saint-Germain-des-Pr%C3%A9s&action=raw: "L'abbe Richard de Laitre fait reparer l'eglise et fortifier le monastere" (Bouillart, Histoire de l'abbaye royale de Saint-Germain-des-Prez, 1724, p. 164); in 1368 Charles V required the abbey to dig a moat on the model of the city's fortifications, fed by a canal called the "Petite Seine" (ALPAGE); "Une nouvelle dissension avec les ecolatres en 1533 fut durement reprimee, le 20 mars 1557 sur le Pre-aux-Clercs" (Bouillart 1724, p. 189); and in 1586 the cardinal-abbot Charles de Bourbon had Guillaume Marchant build the abbatial palace. A caption in the article reads "L'abbaye de Saint-Germain-des-Pres en 1550", its image file named for the Truschet and Hoyau plan.

**Suggested.** Keep the 558 consecration and the Morard rebuilding, cut the Alexander III sentence to a clause, and close on what the sheet shows: a fortified abbey, its moat dug on the city's model after 1368 and fed by the channel they called the Petite Seine, with the Pre-aux-Clercs outside it where the scholars and the monks came to blows.

### 42. **L0141 — LE PLESSI** ((gone); college, vanished)  — *deep*

- period: all three of the detail's new facts are modern locators - the street number, the neighbouring college, and the cours Moliere of the present lycee - and the rue Saint-Jacques position and the 1864 demolition are in the summary. The article's body has what the card lacks: the college was founded in 1322 by Geoffroy du Plessis, protonotary of France, for poor scholars of six named dioceses. The extract given to the writer was the article's lead, which has the address and not the founder.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "College du Plessis", https://fr.wikipedia.org/w/index.php?title=Coll%C3%A8ge_du_Plessis&action=raw: "fonde par Geoffroy du Plessis, protonotaire de France, rue Saint-Jacques en 1322", "pour les ecoliers pauvres des dioceses de Tours, Saint-Malo, Evreux, Rouen, Sens, Reims". The address is cited to Dulaure, Histoire physique, civile et morale de Paris, 1823.

**Suggested.** Replace the whole text: "Geoffroy du Plessis, protonotary of France, founded the college in 1322 for poor scholars from the dioceses of Tours, Saint-Malo, Evreux, Rouen, Sens and Reims." That is the college on the map, and it is not on the card at all.

### 43. **L0040 — LES CORDELIERES** (Hôpital Broca (on its site); church_religious, vanished)  — *deep*

- consistency: two of the three sentences restate the summary - the 1289 foundation, the faubourg Saint-Marcel, Marguerite de Provence's request and the three streets cut across the enclosure are all in it - and the one new fact is the founder's name.
- source: the article gives two foundation dates, 1289 for the Paris house and 1270 for the order, with the nuns "transferees de Troyes ... en 1289", and the card states 1289 alone.
- period: the article has the convent the map shows - eight hectares along the rue de Lourcine, exposed to the Bievre's floods - and the detail gives its full Latinate name instead.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Couvent des Cordelieres (Paris)", https://fr.wikipedia.org/w/index.php?title=Couvent_des_Cordeli%C3%A8res_(Paris)&action=raw: "fonde en 1289 par Gallien de Poix" "a la demande de Marguerite de Provence" (J.B.M. Renou de Chauvigne Jaillot, Recherches critiques : historiques et topographiques sur la ville de Paris, vol. 4, Lottin, 1779, p. 76), against "dont la fondation remonte a 1270" and the nuns "transferees de Troyes" "au faubourg Saint-Marcel, en 1289" (Panayota Volti, "Le choeur des Cordelieres de la rue de Lourcine, a Paris", in Spaces for friars and nuns, EFR, 2022, pp. 301-316); "Les batiments s'etendent alors le long de la rue de Lourcine sur huit hectares" and "Ils sont tres exposes aux crues de la riviere"; they were "largement endommages lors du siege de Paris par Henri IV en 1589-1590" (Hillairet, Dictionnaire historique des rues de Paris, 1985, p. 36); and the abbesses are listed from Gillette de Sens (1270-1286) to Denise Bourdereul (1592-1608).

**Suggested.** "The nuns came from Troyes in 1289, the order itself dating from 1270. Their buildings ran eight hectares along the rue de Lourcine and were badly exposed to the floods of the Bievre; Henri IV's siege of 1589-90 wrecked much of them." Drop the full Latinate name.

### 44. **L0216 — LA FOIRE S. GERMAIN** (Marché Saint-Germain (on its site); square_market, vanished)  — *deep*

- source: "The 15th-century fair buildings were destroyed by fire in 1762" - the article says a hall was built in 1512 by Guillaume Briconnet, abbot of Saint-Germain, able to hold several hundred merchants, so the buildings that burned were not simply 15th-century, and the 1512 hall is the fair the map shows.
- source: the article dates the fair's refoundation two ways and does not reconcile them - the lead has it running yearly "depuis le 3 fevrier 1486", the history section says Louis XI granted the right in 1482.
- period: half the text is 1762-1811.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Foire Saint-Germain", https://fr.wikipedia.org/w/index.php?title=Foire_Saint-Germain&action=raw: "Une halle fut construite en 1512 sous l'impulsion de Guillaume Briconnet, abbe de Saint-Germain, pouvant accueillir plusieurs centaines de marchands" and "En 1482, le roi Louis XI accorda aux religieux de l'abbaye le droit de tenir une foire franche chaque annee", against the lead's "chaque annee depuis le 3 fevrier 1486"; the "plus de 120 espaces de vente, nommes loges" figure is tied to no period. Both the lead and the 1512 hall are cited to Julien Philippe de Gaulle, Nouvelle histoire de Paris et de ses environs, P.M. Pourrat, 1842.

**Suggested.** "A hall for several hundred merchants went up in 1512 under Guillaume Briconnet, abbot of Saint-Germain; it was those buildings that burned in 1762." And flag the 1482/1486 clash rather than printing one of them.

### 45. **L0191 — MON FAUCON** ((gone); other, vanished)  — *deep*

- overclaim: "Montfaucon was transformed shortly after 1303 into a monument" is stated as fact, where the article calls the story "peut-etre un peu romancee" and rests it on a 1596 antiquarian.
- period: the gallows' busiest years were the Wars of Religion, with up to eighty hanged at once in the mid-16th century - the map's own moment - and the detail goes straight from 1416 to Henri IV's accession.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Gibet de Montfaucon", https://fr.wikipedia.org/w/index.php?title=Gibet_de_Montfaucon&action=raw: the 1303 transformation is given as a history "peut-etre un peu romancee" attributing it to Enguerrand de Marigny, sourced to Etienne Pasquier, Les Recherches de la France, livre XXXVIII, fol. 330v, 1596; the 1027 date is sourced to Expilly, Dictionnaire geographique... des Gaules et de France, V, p. 567, 1768; the sixteen pillars to Viollet-le-Duc, Dictionnaire raisonne, t. V, p. 562, 1861, which adds that Tanneguy du Chastel had them made "un par quartier de Paris". A caption states that on the plan de Truschet et Hoyau of about 1550 the gibbet "est alors a l'exterieur de l'enceinte de Paris", and the Wars of Religion made it "un lieu d'execution de masse", with a "pendaison simultanee de jusque quatre-vingts huguenots ou presumes tels" (F. Maillard, Le gibet de Montfaucon, p. 15, 1863).

**Suggested.** "One account, from Pasquier in 1596, has Enguerrand de Marigny turn the gallows into a monument of stone." Add the sixteen pillars' meaning - one for each quarter of Paris - and the mass hangings of the Wars of Religion, which are what the gibbet was for in the years around this sheet.

### 46. **L0012 — LOSTEL DE LA REINE** ((gone); building, vanished)  — *deep*

- consistency: the card is LOSTEL DE LA REINE, the queen's lodging, and the detail never mentions it, although the article describes it - the hotel of the comte d'Etampes bought in 1361 "qui constitua la residence de la reine", behind the king's, entered from the rue Saint-Paul through a portal with stone lions.
- period: the estate's break-up under Francois I is left as a clause at the end, where the article has the queen's hotel auctioned in 36 lots, the rue Beautreillis cut through it, and the buyers using the ground to stack timber - the years this map was drawn.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Hotel Saint-Pol", https://fr.wikipedia.org/w/index.php?title=H%C3%B4tel_Saint-Pol&action=raw: "L'adjudication sous forme de 36 lots de l'hotel de la Reine s'accompagna du percement de la rue Beautreillis", the buyers Claude Girard and Jehan Bocquet using the lots mainly to store timber, cited to Leon Mirot, "Formation et demantelement de l'hotel Saint-Pol", La Cite, t. III, 1906-07, pp. 232-35; the 1544 subdivision to Louis Bergeron, Paris : genese d'un paysage, Picard, 1989, p. 102. A caption shows the "Hotel de la reine vers 1530" after the Braun and Hogenberg plan.

**Suggested.** Give the card its own building: the hotel of the comte d'Etampes, bought in 1361, became the queen's residence, entered from the rue Saint-Paul under a portal of stone lions. Then the end: the queen's hotel was sold off in 36 lots, the rue Beautreillis was cut through it, and the buyers stacked timber on the ground.

### 47. **L0017 — PETIT CHATELET** ((gone); building, vanished)  — *deep*

- period: the closing sentence is a note on present-day Parisian usage of the word "Chatelet"; the second restates the summary. The article has the building the map shows: rebuilt by Charles V in 1369, and named by Charles VI in 1382 as the prevot of Paris's own residence, its prisons - never used until then - serving as an overflow for the Grand Chatelet's.
- voice: "the far end of the Petit-Pont" loses the source's "a l'extremite meridionale".

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Petit Chatelet", https://fr.wikipedia.org/w/index.php?title=Petit_Ch%C3%A2telet&action=raw: "ce dernier fut reconstruit par Charles V, en 1369, et servit plus tard de prison d'Etat" (uncited); by his letters of 27 January 1382 Charles VI made it the prevot's residence and ordered that "les prisons de cette forteresse, qui n'avaient jamais ete utilisees, servent de supplement a celle du Grand Chatelet" (Ordonnances du Louvre, t. VIII, p. 309); the demolition of 1782 is cited to Felix and Louis Lazare, Dictionnaire administratif et historique des rues de Paris, 1855, pp. 560-61.

**Suggested.** Cut the last sentence. "The fort the map shows was rebuilt by Charles V in 1369 at the southern end of the Petit-Pont, and in 1382 Charles VI made it the prevot of Paris's own house, its prisons - until then unused - taking the overflow from the Grand Chatelet."

### 48. **L0062 — LES BERNARDINS** (Collège des Bernardins; church_religious, standing)  — *deep*

- period: three of the four sentences are 1859, 1887, 2008 and 2009; the summary already says the hall survives as a cultural centre.
- source: the 1248 foundation date carries no reference in the article, whose foundation paragraph is cited only to a 2008 newspaper piece about the restoration, and the article is tagged "a sourcer".
- period: the article says a church was begun in 1338 "et cette derniere reste inachevee" - the college on this map had an unfinished church, which is a better fact than the ones the detail chose.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "College des Bernardins", https://fr.wikipedia.org/w/index.php?title=Coll%C3%A8ge_des_Bernardins&action=raw: "la construction d'une sacristie et d'une eglise a partir de 1338 ; cette derniere reste inachevee"; "Prevu a l'origine pour accueillir une vingtaine d'etudiants, le College formera, entre le XIIIe et le XVe, plusieurs milliers de jeunes moines cisterciens". The only citation in the foundation paragraph is Annick Colybes, "La resurrection du college des Bernadins", Les Echos, 3 September 2008, and no source is attached to the 1248 date.

**Suggested.** Cut from "Designated a historical monument" to the end. Put in the church begun in 1338 and never finished, and the thousands of young Cistercians the house trained between the 13th and the 15th century.

### 49. **L0066 — S. LAURENS** (Église Saint-Laurent; church_religious, standing)  — *deep*

- source: the Roman road is dated "the middle of the first century BC", following an uncited sentence in the article; the Musee Carnavalet puts the founding of the Roman town under Augustus, in the last quarter of the first century BC, so a mid-first-century-BC Roman layout predates the town.
- period: two of the three sentences are modern - the 10th arrondissement and the 1945 and 2016 monument listings - and nothing is about the church on the map.
- source: history_fr is the lead; the article's body has the pre-1600 church.

**Evidence.** fr.wikipedia, "Eglise Saint-Laurent de Paris" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=%C3%89glise_Saint-Laurent_de_Paris&action=raw: the sentence "qui fut trace par les Romains au cours de la moitie du Ier siecle av. J.-C." carries no footnote, while the same article has the church founded "a la fin du Ve" siecle, the basilica named in a charter of 710, Gregory of Tours on its monks, a fire in 547, destruction by the Normans in 885, a charter of Louis VI of 1122, a new parish church attested in 1180, and the present church's choir "consacre le 14 juin 1429". On the date: Musee Carnavalet's Paris Antiquite teaching dossier places the founding of Lutetia under Augustus, in the last quarter of the first century BC - but carnavalet.paris.fr does not resolve from this session, so that is taken from the search summary of it and not from the page, and the claim is reported as uncited rather than as refuted.

**Suggested.** Cut the last sentence. Replace the Roman date with the source's own hedge or drop it, and use the church's own history instead: the parish church attested in 1180, rebuilt in the 15th century with its choir consecrated in 1429 - the building the map shows.

### 50. **L0079 — NOSTRE DAME DE PARIS** (Cathédrale Notre-Dame; church_religious, standing)  — *deep*

- period: "Seat of the Archdiocese of Paris" is anachronistic on a card about 1550 - Paris was a bishopric, suffragan of Sens, until 1622.
- period: the second half of the text (Viollet-le-Duc 1845-1867, Napoleon 1804, the 1821 baptism, presidential funerals) is the modern end of the source.
- overclaim: the source hedges the completion date ("au milieu du XIVe siecle vers 1345"); the detail gives "finishing around 1345" alone, which is the lesser of the two problems.

**Evidence.** Diocese de Paris, "Paris, archidiocese depuis 400 ans", https://dioceseparis.fr/paris-archidiocese-depuis-400-ans.html: on 20 October 1622 Gregory XV, by the bull Universi orbis, raised the bishopric of Paris, until then suffragan of Sens, to a metropolitan archbishopric, with Meaux, Chartres and Orleans detached from Sens as its suffragans; the diocese's own list of archbishops begins with Jean-Francois de Gondi (1622-1654). Corroborated by en.wikipedia, "Archdiocese of Paris".

**Suggested.** Cut "Seat of the Archdiocese of Paris," and the final sentence. If the bishop is wanted: in 1550 Notre-Dame was the cathedral of the bishop of Paris, who was still a suffragan of the archbishop of Sens.

### 51. **L0080 — LOSTEL DIEU** (Hôtel-Dieu (rebuilt north of the parvis 1867–1878); church_religious, rebuilt)  — *deep*

- voice: the text begins "Te hospital" - a plain typing error, live on the card, which the mechanical checks do not look for.
- period: the article has the hospital growing in the map's own years - a council of eight lay governors created in 1505, and a salle du Legat added near the Petit-Pont in 1531, which is the building reaching across the small arm of the Seine that the card's own note describes.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Hotel-Dieu de Paris", https://fr.wikipedia.org/w/index.php?title=H%C3%B4tel-Dieu_de_Paris&action=raw: in 1505 a council of eight lay governors was created, and in 1531 a "salle du Legat" was added near the Petit-Pont; the hospital "connait une crise financiere car il est finance uniquement par les aides, les subsides ou les privileges". Cited to Jacques Hillairet, L'ile de la Cite, Editions de Minuit, 1969, pp. 152-53, and Dictionnaire historique des rues de Paris, t. 2, 1997, p. 235.

**Suggested.** "The hospital originally functioned as a hostelry...". Then, if there is room, the salle du Legat of 1531 by the Petit-Pont, which is the range the card's note has reaching over the small arm of the Seine.

### 52. **L0116 — LES CORDELIERS** (Couvent des Cordeliers (only the refectory survives); church_religious, vanished)  — *deep*

- period: all three sentences are after 1789 - the Cordeliers club, the Empire's Ecole pratique, a 20th-century restoration - on a card about the great Franciscan convent of the Latin Quarter, and the Cordeliers club and the refectory are both in the summary. The article has the convent itself: an old vineyard lent by Saint-Germain-des-Pres, a convent with two cloisters, a refectory, gardens and a chapel, the Franciscans growing there through the 15th and 16th centuries, and a great fire in the chapel and cloister in 1580.
- source: that material is cited to a housing-authority video and a blog.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Couvent des Cordeliers de Paris", https://fr.wikipedia.org/w/index.php?title=Couvent_des_Cordeliers_de_Paris&action=raw: "l'abbaye Saint-Germain-des-Pres preta un ancien champ de vigne aux Franciscains de France"; "Les Cordeliers y batirent un couvent, deux cloitres, un refectoire" with gardens and a chapel; "Au cours des XVe et XVIe siecles, les franciscains s'y developpent"; "un grand incendie toucha la chapelle et le cloitre en 1580", with rebuilding from 1582 finished in 1606. Cited to an RIVP video on the Refectoire des Cordeliers and to Alain Foucaut's patrimoine-urbain blog (2014); Laure Beaumont-Maillet, "Le grand couvent des Cordeliers de Paris", Annuaires de l'EPHE, 1973, is cited for the demolition dates.

**Suggested.** Replace the text: the friars had an old vineyard of Saint-Germain-des-Pres and built on it a convent with two cloisters and a refectory, gardens and a chapel; they went on growing through the 15th and 16th centuries, and the fire of 1580 took the chapel and the cloister thirty years after this sheet.

### 53. **L0153 — NERBONNE** ((gone); college, vanished)  — *deep*

- source: the entry's most specific fact, the sixteen bursars in 1544, carries no reference in the article, and the 1481 printing rests on a 2002 exhibition page at the Musee Conde. Both are stated flatly. The 1544 figure is the one number on this card from the map's own generation, so it is the one that most wants a second source.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "College de Narbonne (Paris)", https://fr.wikipedia.org/w/index.php?title=Coll%C3%A8ge_de_Narbonne_(Paris)&action=raw: "On y denombrait seize boursiers en 1544" has no footnote; the paragraph's only reference is Jean-Loup Abbe, Histoire de Limoux, Privat, 2009, p. 124. The Maillard printing - "Le musee Conde de Chantilly possede un ouvrage d'Olivier Maillard, La Confession, imprime en 1481" ... "A Paris, au college de Narbonne" - and the statement that no other book is known from the press are both footnoted to an exhibition shown in the Cabinet des livres at Chantilly in 2002 (bibliotheque-conde.fr).

**Suggested.** No change to the text is needed; the maintainer should know that "sixteen bursars in 1544" is uncited, and that the 1481 press rests on an exhibition page. Lazare has the college under Narbonne and would settle both.

### 54. **L0184 — LE BOIS DE VINCIENNE** (Bois de Vincennes; other, standing)  — *deep*

- source: "a twelve-kilometre wall that stood for six centuries" is the entry's most striking fact and it carries no citation in the article; the Derex references nearby support the 1274 and 1375 extensions, not the 1183 enclosure. The 848 charter, by contrast, is sourced.

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Bois de Vincennes", https://fr.wikipedia.org/w/index.php?title=Bois_de_Vincennes&action=raw: "En 1183, sous Philippe Auguste, il est enclos par une enceinte de douze kilometres de long" has no inline citation, while "Le document le plus ancien mentionnant la foret de Vincennes est la confirmation par Charles le Chauve" is footnoted to Derex, Histoire du bois de Vincennes, p. 38. The article's history also runs straight from Philippe Auguste to Louis XIV's enlargement of 1659, so it carries nothing about the wood in the map's own century.

**Suggested.** Hedge the enclosure - "a wall said to have run twelve kilometres" - or cite it properly. There is nothing to add about 1550 from this source, and the detail is right not to invent any.

### 55. **L0045 — LEGLISE DU TEMPLE** (Square du Temple (on its site); church_religious, vanished)  — *deep*

- consistency: the card is the church of the Temple and the detail never mentions a church - it describes the priory and the enclosure's franchise, which the summary has already given ("kept its own jurisdiction inside Paris").
- source: "the largest Templar commandery in France" carries no footnote in the article.
- period: the one dated thing is "Until the Revolution".

**Evidence.** fr.wikipedia, "Prieure hospitalier du Temple" (read as wikitext, 3 Nov 2026; "Enclos du Temple" is a redirect to it), https://fr.wikipedia.org/w/index.php?title=Prieur%C3%A9_hospitalier_du_Temple&action=raw: no footnote is attached to "la plus grande commanderie templiere de France". The same article describes the church: in the 12th century the rotunda was the whole of it, modelled on the Holy Sepulchre; by the 13th, with choir and porch finished, the rotunda was 10 toises across (about 19.50 m), the nave 4 toises (about 7.80 m) and each aisle 3 toises (about 5.85 m), on six columns and five arcades under a "voute en ombrelle"; it was razed in 1796. A caption in the same article states that the Maison du Temple and its porte du Temple appear on the plan de Truschet et Hoyau, c. 1550.

**Suggested.** Write the church: the rotunda modelled on the Holy Sepulchre, about 19.50 m across, with a nave of some 7.80 m and aisles of 5.85 m on six columns, standing until 1796. Hedge or drop "the largest Templar commandery in France", and cut the franchise sentences, which the summary already carries.

### 56. **L0097 — S. INOCENS** (Place Joachim-du-Bellay (the Fontaine des Innocents survives); church_religious, vanished)  — *deep*

- period: of three sentences, one is the church's position, one retells the Massacre of the Innocents, and one the reclusoirs; nothing is about the largest cemetery in Paris as the map shows it.
- source: "the most famous of all those in Paris" rests on a sentence that carries no citation in the article, while the article's own cited 15th-century material goes unused.
- voice: "possessed up to two reclusories" is a word-for-word rendering of "posseda jusqu'a deux reclusoirs" and does not read as English; the source means it had as many as two at one time.

**Evidence.** fr.wikipedia, "Cimetiere des Innocents" (read as wikitext, 3 Nov 2026), https://fr.wikipedia.org/w/index.php?title=Cimeti%C3%A8re_des_Innocents&action=raw: the reclusoir sentences carry no footnote ("posseda jusqu'a deux reclusoirs a la fois, le premier entre l'eglise et la fontaine et le second du cote oppose"), whereas the charniers "s'elevaient sur plus de quatre-vingts arcades" with the bones "au-dessus d'arcades, entre la voute et la toiture", and the Charnier des Lingeres "etait orne d'une fresque intitulee Danse Macabre peinte en 1424", cited to the Journal d'un bourgeois de Paris, with Guillebert de Metz quoted: "Illec sont paintures notables de la dance macabre."

**Suggested.** Drop the Herod sentence, which is about the feast and not the place, and use the cemetery the map shows: the charniers on more than eighty arcades with the bones stacked between vault and roof, and the Danse Macabre painted in the Charnier des Lingeres in 1424.

### 57. **L0405 — R. DES CORDELIERS** (Rue de l'École-de-Médecine; street, renamed)

- consistency: the detail's chronology contradicts the short description above it - the summary has Guillot calling it the rue des Cordeles in 1300, the detail says it was the rue Saint-Germain before 1672 and the rue des Cordeliers only from 1672 to 1690. The register carries both and the author should have flagged the clash rather than presenting the later sequence flatly.
- period: of seven dated statements, one is before 1550.

**Suggested.** Say what the register actually leaves unresolved: "Guillot already called it the rue des Cordeles in 1300, after the Franciscan convent, and in 1304 deeds name it for Saint-Come and Saint-Damien; the register then has it as the rue Saint-Germain before 1672 and the rue des Cordeliers only from 1672 to 1690." Cut the Revolution renamings and the boulevard Saint-Germain absorption.

### 58. **L0168 — PORTE S. ANTHOINE** (Place de la Bastille; gate_wall, vanished)  — *deep*

- period: the detail is the two gates' dates and nothing else, while the article has the gate the map shows - two flanking towers that became the Tresor and Comte towers of the Bastille, the bastions 11 and 12 the 16th century put beside it, and the tournament of 1559 in front of it in which Henri II took his death wound.
- source: the article contradicts itself, dating the gate to the mid-14th century and also saying it was built under Henri II to bring the Bastille inside Paris; the detail passes the mid-14th-century date on without the clash.
- voice: "the more famous gate" for "la plus connue".

**Evidence.** fr.wikipedia (read as wikitext, 3 Nov 2026), "Porte Saint-Antoine", https://fr.wikipedia.org/w/index.php?title=Porte_Saint-Antoine&action=raw: the second gate belonged to the wall Charles V ordered in 1356, "elevee a la hate et protegee par deux tours" which later became the Bastille's Tresor and Comte towers; the Charles V wall became a bastioned enceinte with bastions 11 and 12 flanking the gate; "Henri II participa, le 30 juin 1559, a un tournoi durant lequel il fut mortellement blesse" at the old Porte Saint-Antoine, by the hotel des Tournelles; and in 1585 the city set a screen wall "en forme d'arc de triomphe, a trois travees separees par des pilastres" by Thibault Metezeau in front of it, with sculpture by Germain Pilon. Cited to Gagneux and Prouvost, Sur les traces des enceintes de Paris, 2004, pp. 39, 85, 122-26, and Hillairet, Connaissance du vieux Paris, Rive droite, 1993, pp. 9, 18, 346-47. Note: the hotel des Tournelles article dates the same tournament 29 June, so two sources in this corpus differ by a day.

**Suggested.** "The gate the map shows was hastily raised in the wall Charles V began in 1356, with two towers that ended as the Tresor and the Comte of the Bastille. It was in the lists before it, in the rue Saint-Antoine, that Henri II took his death wound in June 1559."

### 59. **L0288 — R. TRASENONNAIN** (Rue Beaubourg; street, renamed)

- source: the detail copies the register's bowdlerised entry as a street name - "rue Trace put...", ellipsis and all - which reads on the card as a broken word rather than a name.
- source: the list of the rue Transnonain's names stops one short and never reaches "rue Transnonnain", the card's own name, which the source gives as the last of the series ("et enfin, rue Transnonnain").
- period: the closing sentence is the 1972 clearance for the Centre national d'art contemporain.

**Suggested.** Drop "rue Trace put..." rather than print a truncation, and close the series properly: "...rue Trousse Nonnain, rue Tasse Nonnain and at last rue Transnonnain." Cut the 1972 sentence. The opening - a street of the late 11th century crossing the city wall, called rue de la Poterne inside it and rue outre la Poterne Nicolas Hydron outside - is the best material here and should lead.

### 60. **L0426 — LA GRANT R. S. HONORE** (Rue Saint-Honoré; street, standing)

- period: the closing sentence is a 1966 naming of the place Colette, on a card whose body is a good 13th-to-17th-century chain of names.

**Suggested.** Cut the 1966 sentence.

### 61. **L0433 — R. DE VAUGIRART** (Rue de Vaugirard; street, standing)

- period: the closing sentence is a 1965 naming of the place Paul Claudel. The body - rue de Vaulgirard 1523, chemin des Carrieres 1529, rue des Vaches 1543, chemin de Bel Ayr 1547, rue de Bel Air 1559 - is exactly the map's own decades and is the best dated series in the street set.

**Suggested.** Cut the 1965 sentence and nothing else.

### 62. **L0410 — R. DES ETUVE** (Rue Sauval; street, renamed)

- period: "The section between the rue Berger and the rue de Viarmes was named rue Marie de France by municipal decision in April 2025" - a street naming from this year, 24 of the entry's 54 words, on a card about a 16th-century bathhouse street. It is the most recent fact in the whole set.

**Suggested.** Cut the 2025 sentence. What is left - rue des Etuves, rue des Estuves, and earlier the rue du Pressoir du Bret, attested in 1300 - is short but it is about the street the map shows.

### 63. **L0389 — LA LINGERIE** (Rue de la Lingerie; street, standing)

- period: 36 of the entry's 50 words are a 1972 declassification for the Forum des Halles, which the summary has already covered as "the rebuilding of the Halles in the 1970s". The one new fact is the former name rue de la Ganterie.

**Suggested.** Return null, or keep one line: "It was earlier the rue de la Ganterie, the glovers' street, beside the linen market."

---

## The remaining edits, in brief

Each is in `detail_review.csv` in full, with its evidence and its suggested change.
They are grouped by what is wrong with them.

### A sentence of the wrong century, nearly always the last one (`period:`) — 18

| id | on the map | now | what to change |
|---|---|---|---|
| L0002 | LE PONT NOSTRE DAME | Pont Notre-Dame | Cut the last sentence and the opening quais. |
| L0030 | LOSTEL DE BOURBON | — | Cut the last sentence. |
| L0137 | BEAUVAIS | Chapelle Saint-Jean-de-Beauvais (its chapel survives) | The source's lead has only the Jansenism and the listing, so this is a card for null until a source about the 14th-century foundation is found. |
| L0238 | LA VIELE R. DU TAMPLE | Rue Vieille-du-Temple | Cut the 1885 sentence and keep the names that are not in the summary, with what they mean: the Culture and Cloture du Temple from the Templars' ground it ran to, the Pote… |
| L0239 | R. DE POULISE | Rue des Francs-Bourgeois | Cut the 1868 and 1893 sentences, which the summary covers, and give the room to the Poulies names and what they meant. |
| L0240 | R. DU TAMPLE | Rue Vieille-du-Temple | Return null. |
| L0243 | R. DES ECOUFLES | Rue des Écouffes | Cut the 2017 sentence and keep the dated series, which is the new part. |
| L0244 | R. DES PAIENS | Rue Ferdinand-Duval | Cut the 2019 sentence. |
| L0281 | R. DES RAS | Rue d'Arras | Keep the first sentence and cut the other two. |
| L0292 | LA PIERRE AU LART | Rue Pierre-au-Lard | Cut the last sentence and the 1817 decree. |
| L0301 | LA GRANT R. S. VITOR | Rue Saint-Victor | Keep the course from the rue Copeau to the place Maubert and the rue du Faubourg Saint-Victor name, cut the 1865 and 1869 sentences, and flag the 11th/12th-century clash… |
| L0322 | R. DE LA VANNERIE | — | "From the place de Greve to the rue Saint-Martin..." |
| L0332 | LA GRANT R. S. IAQUES | Rue Saint-Jacques | Cut the 1974 clause, write "this great Left Bank street", and close the list where the source does: "...grand'rue vers Saint-Matelin, grand'rue Saint-Benoit, and at last… |
| L0370 | R. DE SORBONNE | Rue de la Sorbonne | Return null. |
| L0386 | R. DU FOUR | Rue Vauvilliers | Replace the 1936 sentence with the oven: "The bishop's communal oven that gave the street its name stood at the Saint-Eustache end and was in use from 1137 until about 14… |
| L0396 | R. S. GERMAIN | Rue Saint-Germain-l'Auxerrois | "In 1300 it was the rue Saint-Germain a Couroiers, later simply the rue Saint-Germain or the grande rue Saint-Germain." |
| L0434 | R. DES PETIS CHANS | Rue Croix-des-Petits-Champs | Lead on what the card is about: "The street was already there in the 14th century as the rue des Petits-Champs; the stretch between the rue Coquilliere and the place des… |
| L0437 | R. S. THOMAS | — | Lead on the two medieval names and cut the pre-1808 course: "In 1212 it was the rue des Chanoines; from 1242 it took the name of the collegiate church of Saint-Thomas-du-… |

### Adds little or nothing the short description has not already said (`consistency:`) — 26

| id | on the map | now | what to change |
|---|---|---|---|
| L0026 | LE FOUR LEVESQUE | — | Return null, or drop the spelling sentence and give the two dates the summary lacks in one line: "It served the bishops until 1674 and then the crown, as one of the royal… |
| L0041 | S. CATERINE DU VAL DES ESCOLIERS | Place du Marché-Sainte-Catherine (on its site) | "Its outbuildings later served as a cemetery." |
| L0129 | LE CARDINAL LEMOINE | — | Return null, or keep the one fact that gives the man a reason to be here: "The cardinal had been sent to Paris as papal legate to end the fighting between France and Engl… |
| L0167 | LE BASTILLON | — | Cut the last sentence and the western-section sentence, which is about the other end of the wall, and say where the bastion stood and what a bastillon was for. |
| L0171 | LE BASTILLON | — | Either distinguish the two bastions - the card's own note does, citing Cousin 1875 - or return null for both. |
| L0178 | PORTE DE BUCI | — | Keep "Also recorded under the spelling Bussy, it was one of the two gates called the portes Saint-Germain, the other being the porte des Cordeliers" |
| L0179 | PORTE S. GERMAIN | — | Return null. |
| L0228 | LA R. S. CATERINE | Rue de Sévigné | Return null, or add the rue de la Couture variant and the rue du Val to the summary and drop the detail. |
| L0269 | R. DES HOMES ARMES | Rue des Archives | Give the card's street the body of the text, and name the others only as the neighbouring sections they are: "The rue de l'Homme-Arme ran between the rue Sainte-Croix-de-… |
| L0286 | R. DU VERBOIS | Rue du Vertbois | "The street existed in 1546 and was also called the rue Gaillardbois." |
| L0300 | R. DES BERNARDINS | Rue des Bernardins | Cut the last sentence. |
| L0326 | LE PAVE | Rue Frédéric-Sauton | Return null. |
| L0336 | R. DE GARNETAL | Rue Greneta | Open on the card's own street: "Earlier forms of the name run rue d'Arnetal, Darnetal, Dernetat, Drenetat and Darnestat, and it was also called the rue de la Trinite." |
| L0341 | R. AUX OURS | Rue aux Ours | "It appears as the rue As Oues, aux Oues and aux Oes." |
| L0351 | R. DE LA SAVONNERIE | — | Return null. |
| L0354 | R. DES LAVANDIERE | Rue des Lavandières-Sainte-Opportune | Return null. |
| L0364 | R. DU BOUT DE BRIE | Rue Boutebrie | Keep the Latin Eremburgis de Bria and two or three spellings, and let the rest go. |
| L0378 | R. DE MONTORGUEIL | Rue Montorgueil | Say at the start that this is the stretch joined to the rue Montorgueil, not the rue Montorgueil itself, and drop "permanently". |
| L0379 | R. PAVEE | Rue Tiquetonne | Lead with the card's street: "Between the rue Dussoubs and the rue Montorgueil the street was the rue Pavee from 1313, and kept that name until 1851, when it was joined t… |
| L0380 | R. DE BOURGONGNE | Rue Française | Return null, or keep the two new forms in a single clause and let the summary carry the rest. |
| L0381 | R. CONTE DARTOIS | Rue Montorgueil | Drop "briefly" |
| L0387 | R. DES PROUVELLES | Rue des Prouvaires | Return null, or cut to the three or four spellings that differ most and say nothing else. |
| L0403 | R. DE LA SER PANTE | Rue Serpente | Return null, or keep only the rue Serpente: the 1263 Vicus Tortuosus and the 16th-century plans that write it rue Serpente. |
| L0416 | R. DU PAN | — | Return null. |
| L0425 | R. DE GERNELLE | Rue Jean-Jacques-Rousseau | Return null, or write the card's own stretch: "Running as far as the rue Coquilliere, the street appears as rue de Guernelles, Guarnelle, Guarnales and Garnelles before s… |
| L0435 | R. DE BEAUVAIS | — | Keep "First documented as the rue des Chanoines in 1212, it took the name rue Saint-Thomas du Louvre in 1242" |

### Something supplied that the source does not give (`overclaim:`) — 11

| id | on the map | now | what to change |
|---|---|---|---|
| L0140 | COQUERET | — | "It was here that the scholastic jargon of Thomist and Aristotelian philosophy was given up, which one account makes the reason for the college's closure during the troub… |
| L0226 | R. DES CORDELIERES | Rue Broca | Write "Dheulland", and keep the 12th century the source states: "Created in the 12th century, the street was part of the old rue de Lourcine, written Loursine, l'Oursine,… |
| L0306 | LE MONT S. GENEVIEVE | Rue de la Montagne-Sainte-Geneviève | "It was simply the rue de la Montagne from 1793 to 1815." |
| L0333 | R. DES CHOLES | — | Write "Boisseau". |
| L0350 | LA HEAUMERIE | — | "A prefectoral order of 11 March 1851 made it part of the rue des Ecrivains." |
| L0367 | R. DU FOIN | — | "Made part of the rue des Noyers by a prefectoral decree of 10 May 1851, it was destroyed soon after by the boulevard Saint-Germain." |
| L0382 | R. DE MAUCONSEIL | Rue Mauconseil | Drop "eastern" |
| L0406 | LA R. QUIQUETONNE | Rue Tiquetonne | Write "Sauval" |
| L0408 | R. DE LA PLATRIERE | Rue Jean-Jacques-Rousseau | Write "Ducerceau". |
| L0443 | IVERI | Ivry-sur-Seine | "A plan of the 1550s shows the church and spells the village Iveri" |
| L0452 | LA COURTILLE | — | "...and La Courtille became a quarter of amusements." |

### A list of former names and nothing else, or an English slip (`voice:`) — 11

| id | on the map | now | what to change |
|---|---|---|---|
| L0180 | PORTE MONMARTRE | — | Drop the first sentence and lead on the reason, which is the only new thing here: "Each was pulled down in turn to ease the traffic and the city's supply of provisions." |
| L0287 | R. AU MERE | Rue au Maire | Return null. |
| L0311 | R. DE LA POTERIE | — | Cut to the names that carry something - the 1313 tax roll's Jehan Palee, and the Poterne and Fausse Poterne that explain the engraver's slip the card's own note describes… |
| L0321 | R. DE LA COTELLERIE | Rue de la Coutellerie | "Widened in 1564, the cutlers' street had been the rue des Recommanderesses, the rue de la Vieille Oreille or Guigne Oreille, and the rue Guillori." |
| L0325 | LA R. NEUVE | — | "...until it was taken into the enlarged parvis." |
| L0365 | R. DE LA SERPENTE | Rue Serpente | Lead on the map: "Several 16th-century plans, this one among them, write it rue Serpente; a deed of 1263 has the Latin Vicus Tortuosus, the winding street." |
| L0368 | LA GRANT R. DE LA HERPE | Rue de la Harpe | "Between the rue Saint-Severin and the rue de l'Ecole-de-Medecine it was the rue de la Juiverie, vicus Cithare in Judearia in 1247 and vicus Harpe in 1270." |
| L0411 | R. DORLEANS | part of Rue Berger | "...later Behaigne, from Bohemia, recorded in 1328, and Vieille Behaigne." |
| L0412 | R. DES POULLIES | — | "...Autheriche, then d'Autruche, de l'Autruche and d'Autruche dite du Louvre." |
| L0420 | R. MARIE EGIPCIENNE | Rue de la Jussienne | "In the 16th century it was also the rue du Coq Heron, and the rue du Coq Heron dite l'Egyptienne." |
| L0457 | LA VILLE NEUVE | Bonne-Nouvelle | "levelled". |

### Something inherited from the source that wants a second look (`source:`) — 5

| id | on the map | now | what to change |
|---|---|---|---|
| L0331 | LE CLOS BRUNEAU | — | Either say plainly that what remains is the impasse du Clos-Bruneau, if that can be confirmed, or stop after the 1243 name. |
| L0358 | R. DE LA CALANDRE | — | "By 1280 it was the rue de la Calande; the register connects the name with a house of Jean de la Kalendre, though it dates that house to 1343, after the name." |
| L0371 | R. DE POIREES | — | "An imperial decree of 24 August 1864 divided it into the rue Gerson and the rue Restaut." |
| L0445 | VILLE IUIVE | Villejuif | Not an edit to the text so much as a re-fetch: data/research/sources_long.csv L0445 holds 6,892 characters that end inside the sentence "L'histoire de Villejuif dans l'An… |
| L0459 | MONMARTRE | Montmartre | Either hedge - "in the 1680s the nuns left the upper convent" |

### Two things run together (`conflation:`) — 1

| id | on the map | now | what to change |
|---|---|---|---|
| L0460 | LA GRANCHE BATELIERE | Rue de la Grange-Batelière | Split the two: "The fief ran to 58 hectares, from the Champs-Elysees to the chemin de Montmartre. |
---

## What the pattern is

Counted across all 206, the criteria fall out like this: `period:` 80, `consistency:` 71,
`overclaim:` 58, `source:` 46, `voice:` 44, `conflation:` 4. Six things are behind nearly
all of them.

### 1. The extract, not the writer, is the first cause

`fetch_wiki.py` asks French Wikipedia for `exintro`, so `history_fr` is the article's **lead**.
The log already found that this ruins a modern commune. It ruins more than that. For a street
or a small church the lead *is* the story. For a gate, a mint, a manufactory, a cathedral, a
town hall, a hospital or a college the lead is a definition plus the modern end — and the
article's `Historique`, two screens further down, has exactly what the card wants.

**16 of the 20 held-back cards are on `history_fr`.** The sharpest cases:

| id | the lead gave | the same article's body has |
|---|---|---|
| L0174, L0176 | the triumphal arches of 1673-74 | the 14th-century bastide gates the map shows, 60 m from the arches |
| L0025 | the Monnaie de Paris as an institution today | nothing about this site — the mint it names is on the Île de la Cité |
| L0197 | the Manufacture nationale and a 2007 reopening | Jehan Gobelin's dye works of 1443 and the mill the map is named after |
| L0015 | a sweep of riots from Étienne Marcel to the Liberation | Boccador's palace, begun 1533, its south range finished 1551 |
| L0138 | the law faculty's institutional history to 1808 | the ban on civil law since *Super specula*, which is what "décret" means |
| L0111 | an address and the 1849 refoundation | the cloister rebuilt in 1556, the schools in 1563 |
| L0141 | a street number | Geoffroy du Plessis, protonotary of France, 1322, and six dioceses |
| L0118 | the attributes of Saint Eustace | — (this one really has nothing; the card wants another source) |
| L0066 | an arrondissement and two monument listings | the parish church of 1180, the choir consecrated 14 June 1429 |

The cheapest improvement available to this project is not another pass over the same text.
It is running `fetch_wiki_history.py` over the **church, college, building, gate and bridge**
cards as well as the villages, and asking again. On the evidence of the nine above, that would
turn most of the twenty holds into good cards.

### 2. `sources_long` is capped, and the toponymy eats the budget

Of the 26 `sources_long` entries, **11 stop at about 6,900 characters, mid-sentence** (L0465's
breaks off at "les Fermiers généraux obtiendront de Louis XVI le"), and **12 open with
`Toponymie` or `Origine du nom`** rather than the history. Usually the history survives
further down. Once it does not: L0445 (Villejuif) is 5,100 characters of etymology, then the
opening of a prehistory section, and it ends inside the sentence "L'histoire de Villejuif dans
l'Antiquité et le haut Moyen Âge est longtemps restée mal connue, et le demeure." The card
therefore carries seven sentences of name etymology and nothing about the village — and the
writer could not have done anything else. That one is a fetch to redo, not a text to fix.

### 3. One habit, repeated: supplying what a bare surname leaves out

The register names its authorities by surname. The descriptions give them trades, forenames
and centuries the register does not:

- *Lacaille* → "the mapmaker Lacaille" (L0262), "the cartographer Lacaille" (L0309, L0355)
- *Sauval* → "Henri Sauval" (L0349), "the 17th-century historian Henri Sauval" (L0323),
  "the historian Sauval" (L0438), "Henri Sauval" (L0319)
- *Ducerceau* → "Jacques Androuet du Cerceau" (L0313, L0352, L0406, L0408)
- *Jaillot* → "Jean-Baptiste-Michel Jaillot" (L0313)
- *Boisseau* → "Jean Boisseau" (L0333); *Dulaure* → "the historian Jacques-Antoine Dulaure"
  (L0188); *Dheulland* → "the cartographer Dheulland" (L0226); *Lazare* → "Felix Lazare" (L0229)
- undated plans given centuries: "the 16th-century map of the Tapisserie" (L0319), "the
  17th-century plan of Blondel" (L0339), "the 16th-century plan of Jacques Androuet du
  Cerceau" (L0352)

**Most of these are right.** Du Cerceau and Jaillot are both confirmed from sources this
project already holds, and the site itself calls Sauval "a 17th-century historian of Paris" on
L0410. The fault is that they are supplied silently, which the brief forbids for exactly the
reason this project knows best — a plausible addition is how the Verderet and the Sénat
brochure went wrong. Two of them are also loose on the facts: **Jean de La Caille was a
printer-bookseller** who published a plan in twenty plates, which is not a mapmaker, and
**"Felix Lazare" should be the brothers Félix and Louis Lazare**.

And one inconsistency worth fixing for its own sake: Gilles Corrozet, whose verses are printed
on this very map, appears as "the historian Corrozet" (L0221), as bare "Corrozet" (L0398), and
— correctly — as "Gilles Corrozet's 1532 guide" (L0401). Three cards, three treatments of the
one author the site has a whole page about.

### 4. Hedges kept, then dropped, inside the same habit of mind

Fourteen entries drop a conditional or an attribution the source made: L0156 (*se situerait*,
*s'étendrait approximativement*), L0449 (*vraisemblablement*), L0458 (*d'après l'Abbé Lebeuf*,
*proviendrait*), L0044 (*sans doute* and *aurait été construite*, both in one entry), L0349
(*aurait été dénommée*), L0441 (*une sorte de forteresse d'aspect féodal* becomes "a feudal
fortress"), L0392 (two attested street names become an etymology the summary hedges), L0191
(a story the article calls *peut-être un peu romancée*), L0034 (a named 1853 opinion becomes
"described historically as unquestionably"), L0444 (*environ* 47 households), L0355, L0105,
L0446, L0112.

This is not carelessness, which makes it more interesting. The same writer keeps "According to
tradition" at L0450, "reportedly" at L0228, "is said to have" at L0333 and L0414, "likely" and
"remains debated" through the whole of L0445, and preserves Sauval's *prétend* as "claimed" at
L0319. L0349 keeps one hedge and drops the other **in the same sentence**. A single line in the
brief — *if the source says* aurait, *write "is said to"* — would catch most of them.

### 5. The last sentence

**68 of the 206 end on a sentence carrying a date of 1700 or later; 23 name a year after 1900.**
Street namings (L0410, April 2025; L0244, June 2019; L0243, March 2017), Forum des Halles
declassifications (L0389, L0392), Centre Pompidou clearances (L0288, L0292), square namings
(L0426, 1966; L0433, 1965), monument listings (L0066, L0174), renovations (L0062, L0197),
today's tenants (L0033, L0138, L0154). **Deleting the final sentence would fix about a third of
the `edit` rows outright** and would cost almost nothing, because in nearly every case the
summary has already said what became of the place.

### 6. Where two labels share one register entry, one of the pair gets the other's street

Twelve ids share a source text with a neighbour: L0262/L0309, L0378/L0381, L0340/L0379/L0406,
L0365/L0403, L0336/L0374, L0234/L0269, L0408/L0425, L0238/L0240, L0167/L0171, L0178/L0179,
L0029/L0030, L0437/L0435. In nine of the twelve, the card whose own stretch is *not* the
register entry's lead subject gets a description of the neighbouring stretch, sometimes without
a word to say so. L0309's reader is told "This eastern segment adopted the name rue de
Montmorency in 1768" on a card whose own stretch had borne that name since the 14th century;
L0374's reader is told the rue Beaurepaire was "the middle section" when the middle section is
the card's own street. The register's own three ranges prove it.

### And the trap the project already named: shared street names, stated flatly

The brief says to look twice at any shared name. There are more than the brief expects, and no
detail flags one of them:

- **three** rues des Deux-Portes (L0234/L0269 in the Marais, L0363 off the rue Hautefeuille,
  L0370 by the Sorbonne)
- two rues de la Fausse-Poterne (L0288, L0311), two rues des Recommanderesses (L0321, L0322),
  two rues de la Vieille-Plâtrière (L0365, L0402), two rues de la Barre (L0402, L0414), two
  rues du Pet (L0401, L0469), two rues de Richebourg (L0223, L0233)
- the **rue des Rosiers** as the former name of the street next door (L0242 is the rue des
  Rosiers; L0244's register entry says that street was "antérieurement, rue des Rosiers")
- a rue de la Pelleterie on the Cité (L0355) and the same name given to the rue du
  Vieux-Colombier on Merian's plan of 1615 (L0432) — a name transferred between two streets on
  opposite banks, which is the same kind of slip Cousin found on this woodcut

### Eight sources in this corpus cite this map — and date it three ways

A by-product worth keeping. The sources the project collected mention the Truschet and Hoyau
plan eight times, and they do not agree on its date:

| source for | wording |
|---|---|
| L0465 Le Roule | "porté pour la première fois sur le plan de Truschet et Hoyau en **1552**" |
| L0449 Bagnolet | "la première représentation connue date de **1552** (plan de Truschet et Hoyau)" |
| L0441 Bercy, L0442 Conflans | "plan de Truschet et Hoyau et plan de Jacques Androuet du Cerceau dessinés **vers 1550**" |
| L0444 Vitry | "plan dit plan de Bâle (de Truschet et Hoyau), publication datée **1553**" |
| L0119 Filles Pénitentes | reference list: "Plan de Truchet et Hoyau (**c. 1550, publié 1553**)" |
| L0191 Montfaucon | caption: on the plan "d'environ **1550**" the gibbet is outside the wall |
| L0188 Île Louviers | "la seule construction figurée sur le plan de Truschet et Hoyau, **vers 1550**" |
| L0127 Saint-Germain-des-Prés | caption "L'abbaye ... en **1550**", file named for the plan |

That bears on the project's own open question, where *History of Cartography* ch. 48 says 1550
and ch. 53 says c. 1553: five of these eight sources are independent of each other and three of
them say 1552 or 1553. The descriptions handle the map references well at L0441, L0442, L0449
and L0465. At **L0443** they do not: the source says only "un plan des années 1550" and the
detail makes it this map.

The L0188 citation is the best of the eight and is unused: the article says the island's **one
building on this sheet** is probably the small fort and harbour put up so that Henri II could be
given a mock siege and a naval battle.

---

## Six things wrong outside the longer descriptions

Found while checking, out of this review's scope, and each on a live card:

1. **L0386** — the short description calls Vauvilliers "the architect". He was a Hellenist
   scholar who handled Paris's food supply in 1789 (fr.wikipedia, *Rue Vauvilliers*: "le savant
   helléniste Jean-François Vauvilliers (1737-1801)").
2. **L0058** — the summary says Saint-Merri was built 1500–1550 "so it was brand new when this
   map was made"; the detail says 1500–1565; the source says 1565, broken down by Agnès Bos
   (*Les églises flamboyantes de Paris*, Picard, 2003, p. 239) as nave 1500–1515, transept
   1525–1535, choir 1535–1565. One of the two is wrong and the card prints both.
3. **L0064** — the card's note says Saint-Étienne-du-Mont was "built 1494–1624"; the source says
   the work began in **1491**.
4. **L0132** — the card dates the collège de Navarre to 1304. The article's own archival caption
   dates the founding act to **25 March 1305** (Archives nationales AE/II/308a-b), its external
   link to a codicil of 31 March 1305, and the scholarly reference it cites is titled "de sa
   fondation (**1305**)". The 1304 in the lead has no footnote.
5. **L0188** — the summary says the Île Louviers was "used for storing timber and hay". The
   article dates the timber-merchants' lease to **1700**; before 1600 it gives pasture, a
   crossbowmen's range and Henri II's mock siege.
6. **L0301** — the register dates the foundation of the abbey of Saint-Victor to the **11th**
   century, where the site's own summary and card L0049 say the 12th. The detail wisely writes
   neither, but the clash should be in notes.

## Three gaps in the mechanical checks, each demonstrated

1. **L0080's detail begins "Te hospital".** Live on the card. No check looks at the first word.
2. **L0457 contains "leveled".** `US_SPELLINGS` in `scripts/ingest_detail.py` catches `labeled`
   and `canceled` but has no entry for `leveled`/`levelled` — the same too-narrow-pattern
   failure the log records twice for `neighboring` and `forced labor`.
3. **L0451's "By 1550" is arithmetic, not a record.** The source says "Cent cinquante ans plus
   tard", a hundred and fifty years after a manor of about 1400. The author did the sum and
   wrote the answer as a date — and 1550 is the single year the year check waives by design, as
   the sheet's own date. Nothing could have caught it.

## What held up

Worth saying, because 155 rows marked `hold` or `edit` does not describe the whole set. The
**village and faubourg cards written from the `sources_long` extracts are the best writing
here**, and the ones the log singles out survive checking almost claim for claim: Bercy, Conflans,
Bagnolet, Le Roule, Belleville, Clignancourt, Montreuil, Les Porcherons, Chaillot, Vitry. I
checked their specific claims against their sources phrase by phrase — the forty horsemen at La
Grange aux Merciers, the stables for fifty horses at the Séjour du Roi, 11 January 1436, the
9 September 1465 vintage out of Jean de Roye's chronicle, "Les Brières sur le plan" — and found
one fault between them all: a dropped *vraisemblablement* at L0449. Among the streets, L0432
(rue du Vieux-Colombier), L0433 (Vaugirard), L0439 (rue du Four) and L0392's 1530 rue des Étuves
aux Femmes put the reader in the right decade without being asked to.

---

## What I could not reach

**Depth.** 61 of 206 were taken deep, against the brief's "roughly 70", and I should say why
rather than round up. 75 of the 206 cards are streets drawn from the Ville de Paris register,
which is an administrative extract with no article behind it and no references to follow, so a
deep pass as the brief defines it does not exist for them. Where a named authority or a datable
plan made an outside check possible I made it — Jean de La Caille through data.bnf.fr, du
Cerceau and Jaillot through this project's own corpus, the east-to-west order of the rue
Greneta's three merged sections through fr.wikipedia. For the 70 non-street cards I opened the
article past the supplied extract in all but a handful, and those handful are where the article
turned out to be a redirect to the page the extract already came from (L0041, L0042, L0137).
**Every one of the 206 had the shallow pass. None is marked `unchecked`.**

**Hosts that refused me.** `www.carnavalet.paris.fr` does not resolve from this session, so the
Musée Carnavalet's dating of the founding of Lutetia — which bears on L0066's "middle of the
first century BC" — is reported from a search summary and not from the page. That is why L0066's
Roman date is recorded as **uncited** rather than refuted; somebody with the page in front of
them should finish it. Lazare's dictionary is transcribed on fr.wikisource, but only as
letter pages of about half a million characters each, returned in 100,000-character slices; I
did not page through them, so **no street claim in this review was checked against Lazare
directly**, which is the single biggest hole in it. Gallica was not attempted
(`quote_verification.md` records it answering 403 to automated requests).

**Out of scope and untouched.** The French and Swedish summaries, the identifications, the
label readings, and the question of whether each place is in the right spot on the map.

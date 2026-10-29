# Research on the last 3 open questions (2026-10-26)

Web research only, for the three labels Cousin (1875) lists without identifying. The sandbox
could run web searches but could not open Gallica, Wikisource, Wikipedia or the Paris open-data
registers directly. So the quotes below come from search-engine extracts of those pages, not from
pages read in full. **Check each quote against the page before citing it on the site.**

**Verification pass, 29 October 2026 (branch `verify-research-quotes`).** Every quote below was checked
against the page itself; full results in `quote_verification.md`, group F. Most are exact. Four things
changed, and they are marked in place below:

- **L0007's coordinate is now measured, not remembered**: the rue de Provence × rue de la
  Chaussée-d'Antin crossing is at **48.87430, 2.33275** (OpenStreetMap). The remembered figure was 28 m
  out — good — but the live pin is **465 m** away, not the “about 420 m” stated here.
- **The unattributed “pont d'Arcans” quote is fr.wikipedia *Ruisseau de Ménilmontant*.**
- **L0421 is confirmed** by Lazare and the Archives nationales, independently of each other — but one of
  the Lazare sentences quoted here belongs to a **different street**, and French Wikipedia has the two
  streets conflated. See the warning in that section.
- **The séjour d'Orléans was divided in 1541**; the “/1545” has no source.

Positions on the scan: x grows southwards, y grows westwards (the map is east-up).

## L0007 "LE PONT ARCANS": the Pont Arcans over the Grand Égout. Confidence: medium–high

**Finding.** A small bridge where the road from Paris to the Porcherons crossed the Grand Égout
(the old bed of the Ménilmontant brook, the open sewer that ran round the north of the city to
the Seine at Chaillot). The road later became the rue de la Chaussée-d'Antin, and the sewer was
covered by the rue de Provence (finished 1771). So the site is roughly where the rue de Provence
meets the rue de la Chaussée-d'Antin, in the 9th arrondissement.

**Sources**
- French Wikipedia, *Liste des ponts de Paris*, section on destroyed bridges:
  « Pont Arcans : jeté sur le Grand Égout, il était situé entre le château des Porcherons et la
  Ville l'Évêque. » https://fr.wikipedia.org/wiki/Liste_des_ponts_de_Paris
- *Paris pittoresque*, « Chaussée-d'Antin » (**read 29 Oct 2026**; the page's own header gives the
  source as « D'après *Les rues de Paris. Paris ancien et moderne*…, sous la direction de Louis
  Lurine, paru en 1844 »). Exact wording: « … avaient tracé un chemin sinueux qui, partant de la
  porte Gaillon, aboutissait aux Porcherons. Ce chemin … enjambait, à l'aide d'un mauvais pont, un
  affreux égout … qui s'appelait le ruisseau de Ménilmontant. Cette sentine et ce ruisseau sont le
  père et la mère de la rue de Provence. Le pont, qui était fort vilain et fort crevassé, avait nom
  le Pont-Arcans. On avait oublié d'y mettre des garde-fous, et on le passait à la grâce de Dieu. »
  https://www.paris-pittoresque.com/rues/100.htm
- **The source of the « fit disparaître le pont d'Arcans » quote is identified**: fr.wikipedia,
  *Ruisseau de Ménilmontant* (**read**), on the covering of the Grand Égout in the 1760s — « … de
  nouvelles rues furent ouvertes, notamment la rue de Provence qui fit disparaitre le pont d'Arcans
  enjambant l'égout au niveau approximatif de la rue de la Chaussée d'Antin actuelle ». English
  Wikipedia, *Menilmontant brook* (**read**), says the same in English.
- Charles Duplomb, *Histoire générale des ponts de Paris*, **Paris, 1911**, 2 vols (not 1911–13),
  lists it among « les ponts oubliés » over sewers: « Pont Arcans (sur le Grand Egout, ancien lit du
  ruisseau de Ménilmontant, entre le château des Porcherons, **rue Saint Lazare**, et la
  Ville-l'Evêque) » — bookseller's description, **read**:
  https://blog.paris-libris.com/duplomb-charles-histoire-generale-des-ponts-de-paris/
- CCFr (**read**): a folio "Pont Arcans" in the **Fonds Sellier** — held not by the BnF but by the
  **Bibliothèque historique de la Ville de Paris**, « Fonds Sellier, Charles (1844-1912), historien »,
  **cote MS-2765 à MS-2783**, vers 1870–vers 1910, 19 volumes.
  https://ccfr.bnf.fr/portailccfr/ark:/16871/004a1965928

**Does it fit the map?** Yes. The label (1100, 7150) sits between LES TORCHERONS (the
Porcherons, L0462, 641 px away) and LA VILLE LEVESQUE (L0464, 1300 px), which is exactly where
Wikipedia puts the bridge. Cousin's square V,7–8 is the same area.
(The distances are **confirmed** against `data/labels_inventory.csv`, 29 Oct 2026: 641 px and 1301 px.
The Wikipedia half of the sentence is still unverified.)

**Position.** The rue de Provence × rue de la Chaussée-d'Antin crossing is at about
**48.87430 N, 2.33275 E** — **measured from OpenStreetMap, 29 Oct 2026** (the two ways share nodes at
48.874303/2.332751 and 48.874299/2.332712). The earlier from-memory figure, 48.8745 / 2.3330, was 28 m
out, inside its own ±50 m. The
current map estimate (48.8755, 2.3389) is **465 m** east-north-east of that (the note said about 420 m). That error is
typical for this edge of the overlay, so I left `coords` empty. Setting it after a check on OSM
would put the pin on the site.

**Changed:** `others.csv` row L0007: `modern`, `note`, confidence low → medium. I didn't use
"high" because neither the Wikipedia list nor Lurine gives a primary source, and the exact
crossing is "approximatif".

## L0421 "R. BRENEUSE": rue Verdelet (Merderet, Verderet). Confidence: high on the street; the register id is still to add

**Finding.** In this quarter, "rue Breneuse" (French *bren*, filth) was a medieval name of the
lane later called rue Verderet / Verdelet, earlier Merderet. It ran from the rue Plâtrière (now
rue Jean-Jacques-Rousseau) to the corner of the rue Coq-Héron and the rue de la Jussienne
(Sainte-Marie-l'Égyptienne). In 1849 it was merged with the rue Pagevin and the rue du
Petit-Reposoir. The merged street later disappeared under the rue Étienne-Marcel and the
extension of the Hôtel des Postes.

**Sources**
- **Lazare 1844, « Verdelet (rue) » — read on Wikisource (djvu p. 671), confirmed verbatim.** The
  entry's head settles the street: « **Commence à la rue Jean-Jacques-Rousseau, n° 11 ; finit aux
  rues Coq-Héron et de la Jussienne, n° 2.** … Sa longueur est de **77 m**. — 3e arrondissement,
  quartier Saint-Eustache. » Then: « En 1295, ce n'était qu'une ruelle étroite et puante hors des
  murs de l'enceinte de Philippe-Auguste. Elle se nommait alors rue *Merderet*. **En 1311, on la
  trouve sous le nom de *Breneuse***, c'est-à-dire rue malpropre. Plus tard, par altération, elle fut
  appelée rue *Verderet*, puis *Verdelet*. » **That extent is exactly where the label sits.**
  (Lazare does *not* mention the *rôle de la taille*; that attribution is still unsourced.)
  https://fr.wikisource.org/wiki/Dictionnaire_administratif_et_historique_des_rues_de_Paris_et_de_ses_monuments/Verdelet_(rue)
- **CORRECTION.** « Des actes de 1290, 1330, 1352 et 1406… » is **not** a variant of that entry. It is
  Lazare's **separate « Verderet (rue) » entry**, immediately below on the same page, describing a
  **different street**: « Commence à la rue de la Grande-Truanderie, nos 42 et 44 ; finit à la rue
  Mauconseil, nos 17 et 19. … 89 m. — 5e arrondissement, quartier Montorgueil. » About 400 m away,
  on the far side of the Halles. Do not cite it for this label.
- **Archives nationales — read, confirmed verbatim, and the record identified.** The quote is in
  record **vdp-3149, which is the *rue Pagevin* record** (vdp-3953 returns 404): « Supprimé par
  l'ouverture de la rue Etienne Marcel et par l'agrandissement de l'Hôtel des Postes. Elle avait été
  formée, en 1849, par la réunion des rues Verdelet, Pagevin et du Petit Reposoir. **La rue Verdelet,
  qui était comprise entre les rues Jean-Jacques Rousseau et de la Jussienne, avait porté les noms de
  la rue Mardelet ou Marderet (XIIIe siècle), Breneuse et enfin de rue Verderet ou Verdelet.** La rue
  Pagevin commençait rue de la Jussienne et finissait rue d'Argout. … La rue du Petit Reposoir était
  comprise entre la rue d'Argout et la place des Victoires ; elle avait aussi anciennement été
  dénommée rue Breneuse. » So the three Breneuses were one continuous chain, east to west.
  https://rdf.archives-nationales.culture.gouv.fr/place/FRAN_RI_025-d3nzcc8smx--w2i8uceiz29c-vdp-3149
- **⚠ Do not "correct" this identification to match French Wikipedia.** *Rue Merderet* and *Rue
  Verderet (ancienne, Paris)* are both redirects to one article, *Rue Verderet (ancienne voie de
  Paris)*, and **that article conflates Lazare's two entries**: it takes *Verderet*'s situation
  (Grande-Truanderie → Mauconseil, 89 m, quartier Montorgueil) and *Verdelet*'s history (1311
  Breneuse; « les rues Pagevin et du Petit-Reposoir qui étaient en face »). Those cannot both be one
  street, and *Rue Pagevin* links to it for the street at Coq-Héron/Jussienne. Lazare and the
  Archives nationales agree with each other, and with this project.
- Disagreement, **read and confirmed**: *Nouvelle revue d'onomastique*
  (https://journals.openedition.org/nda/3928) — « à Paris, la rue Merderel en 1295 prit le nom
  d'Orde rue en 1311 puis celui de rue Breneuse, avant que Merderet ne se transforme en Verderet puis
  en Verdelet (**Lock 1867 : 292**) ». So Lock puts « Orde rue » at 1311 and Breneuse after; Lazare
  puts Breneuse at 1311. Either way the name belongs to this street.

**Why this one, and not the other "rues Breneuses".** The Archives nationales register also
gives "Breneuse" as an old name of the rue du Petit-Reposoir. **Confirmed**: it ran from the rue
d'Argout to the place des Victoires — further west, beyond the rue Pagevin, exactly as supposed.
(The “renamed by a court ruling of 1582” detail is **not** in the record and remains unsourced.)
Lazare gives Breneuse for the rue Pagevin too (« Plus tard on la nomma rue *Breneuse* »; its name
comes from Jean Pagevin, huissier du parlement). The label (3150, 5600) sits between R. DE LA PLATRIERE (L0408, 186 px),
R. QUOQUEHERON (L0423, 148 px) and R. MARIE EGIPCIENNE (L0420, 197 px), so it marks the lane
joining those three. That is Verdelet's exact extent. R. PAGEVIN (L0422) has its own label
220 px further west.
(The distances are **confirmed** against `data/labels_inventory.csv`, 29 Oct 2026: 186, 149, 197 and
220 px. The register and Lazare quotes above are still unverified.)

**Changed:** `streets.csv` row L0421: the note only. `match` stays empty and confidence stays
low, because `resolve_streets.py` needs the id of rue Verdelet in the vanished-streets register
(`work/ref/voies_caduques.json`), which isn't in this checkout. To close it: look up "rue
Verdelet" (or "Verderet") there, set `match` to `#<id>`, `status` to `vanished`, confidence
`high`. Use `vanished`, or the resolver would follow the register's "Voir : rue Pagevin" chain
to a successor.

**Possible inconsistency — checked, and it is real but subtler than it looked.** L0422 (R. PAGEVIN)
is matched to `CUR:rue d'Argout`. The Archives nationales register (**read**) does say the 1849 rue
Pagevin « Supprimé par l'ouverture de la rue Etienne Marcel et par l'agrandissement de l'Hôtel des
Postes » — **but the same record adds** « Cette dénomination correspond à 2 voies : actuelles rue
Herold et rue d'Argout. Voie supprimée. » So the register itself chains Pagevin forward to the rue
d'Argout, which makes the project's match defensible. The genuine problem is the **duplicate**:
L0419 (Vieux-Augustins) also lands on the rue d'Argout, and the rue d'Argout *is* the former rue des
Vieux-Augustins. French Wikipedia adds that the merged street disappeared in **1880** (not 1866) and
that the 1849 merger was by ministerial decision of **28 August 1849**. Someone should decide
whether L0422 is better marked `vanished`.

## L0224 "R. NEUVE" (faubourg Saint-Marcel): not resolved. Confidence: low

**What Cousin says:** « NEUVE (rue), sans autre désignation | IV,2 | donnant dans la rue de la
Barre au faub. St-Marcel ».
**Confirmed** 29 Oct 2026 against the project transcription, `data/research/cousin_1875_table.txt:266`:
`NEUVE (rue), sans autre désignation | | IV,2 | donnant dans la rue de la Barre au faub. St-Marcel`
(the quote above simply elides the empty map-label column). Beware the neighbouring entry at line 265,
`NEUVE (rue) | R. Neueve | VIII,4 | à l'entrée du faubourg St-Germain; se rapporte à la rue Garancière`
— a different street, and not this label.

**On the map:** the label (9520, 1140) is 168 px from S. MARCEAU (the collegiate church of
Saint-Marcel, L0037), 208 px from R. DU FER DE MOULAIN (L0223) and 284 px from R. DE LA BARRE
(L0222, now rue Scipion).
(The distances are **confirmed** against `data/labels_inventory.csv`, 29 Oct 2026: 168, 209 and 285 px.)

**What I found**
- The rue de la Barre was itself a new street: « rue Scipion (ancienne *rue de la Barre*, ouverte
  en 1540) » (fr.wikipedia, *Faubourg Saint-Marcel (quartier de Paris)*, **read, verbatim**). The
  same article puts the hôtel Scipion, built 1565 for Scipion Sardini, « rue de la Barre **à l'angle
  de l'actuelle rue du Fer à Moulin** » — which is the corner this label sits beside. So a "rue
  Neuve" opening onto it c. 1550 is plausible: a street from the same years, still known only as
  "the new street".
- Other streets were laid out here at the same time: the *séjour d'Orléans* « fut **loti en 1541**
  (ouverture des rues Censier et de la Clef) » (Atlas historique de Paris,
  https://paris-atlas-historique.fr/32.html, **read**; the “/1545” in the earlier draft has no
  source and is dropped). Neither street is next to the label, though.
- The rue des Francs-Bourgeois-Saint-Marcel ran from the rue des Fossés-Saint-Marcel to the
  place de la Collégiale, and is now under the boulevard Saint-Marcel (Lazare 1844; Carnavalet;
  INHA). It does meet the rue de la Barre, but its name dates from 1296 (Lazare), so it was not
  "new" in 1550. Unlikely.

**Hypotheses for someone with the books:**
1. A street opened with the rue de la Barre in 1540–1550 between the collegiate church and the
   rue de la Barre, known later under another name. I found no source naming it.
2. A first name of a street that the map also labels under another name. **The rue du Fer-à-Moulin is
   now checked and looks unlikely**: Lazare (djvu p. 220, **read**) gives it *Comte-de-Boulogne*,
   *Richebourg* (after Sauval), and, from 1713, *des Morts* for the stretch along the Clamart
   cemetery and *Permoulin* for the rest — **not one of its documented names is “Neuve”**. The rue
   Pierre-Assis is still unchecked.

Search next in Jaillot, *Recherches critiques… sur la ville de Paris* (1772–1775), quartier de
la Place-Maubert / Saint-Marcel, which lists the faubourg's streets with their 16th-century
names; and in Berty and Tisserand, *Topographie historique du vieux Paris*, the volume on the
Saint-Marcel area (or Friedmann's ALPAGE parcel data). **No change made** to `streets.csv`.

# Research on the last 3 open questions (2026-10-26)

Web research only, for the three labels Cousin (1875) lists without identifying. The sandbox
could run web searches but could not open Gallica, Wikisource, Wikipedia or the Paris open-data
registers directly. So the quotes below come from search-engine extracts of those pages, not from
pages read in full. **Check each quote against the page before citing it on the site.**

**Verification pass, 29 October 2026 (branch `verify-research-quotes`).** The quotes were put to a check.
**The pages still could not be opened** — fr.wikipedia.org, en.wikipedia.org, fr.wikisource.org,
rdf.archives-nationales.culture.gouv.fr, journals.openedition.org, paris-pittoresque.com, ccfr.bnf.fr and
paris-atlas-historique.fr are all refused by the session's network policy — so every quote taken from them
stands unverified. Two kinds of claim were confirmed, from material in this repository: the Cousin
quotation for L0224, and all nine label-distance figures. Details in `quote_verification.md`, group F.

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
- *Paris pittoresque*, « Chaussée-d'Antin », quoting Louis Lurine (ed.), *Les rues de Paris :
  Paris ancien et moderne* (1844): the road from the Porte Gaillon to the Porcherons crossed the
  sewer on a poor bridge called the Pont-Arcans, which was cracked, ugly and had no railings.
  https://www.paris-pittoresque.com/rues/100.htm (I have the gist from search extracts, not the
  exact wording.)
- A French source in the search results (probably fr.wikipedia, *Rue de Provence*, or
  *Ruisseau de Ménilmontant*) says that building the rue de Provence « fit disparaître le pont
  d'Arcans enjambant l'égout au niveau approximatif de la rue de la Chaussée d'Antin actuelle ».
  English Wikipedia, *Menilmontant brook*, says the same in English. Neither article was opened
  in full.
- Charles Duplomb, *Histoire générale des ponts de Paris* (1911–1913), lists it among the
  "forgotten" bridges, over sewers. Seen only in a bookseller's description:
  https://blog.paris-libris.com/duplomb-charles-histoire-generale-des-ponts-de-paris/
- BnF, Catalogue collectif de France: a folio titled "Pont Arcans" in Charles Sellier's notes on
  old Paris. https://ccfr.bnf.fr/portailccfr/ark:/16871/004a1965928 (not opened).

**Does it fit the map?** Yes. The label (1100, 7150) sits between LES TORCHERONS (the
Porcherons, L0462, 641 px away) and LA VILLE LEVESQUE (L0464, 1300 px), which is exactly where
Wikipedia puts the bridge. Cousin's square V,7–8 is the same area.
(The distances are **confirmed** against `data/labels_inventory.csv`, 29 Oct 2026: 641 px and 1301 px.
The Wikipedia half of the sentence is still unverified.)

**Position.** The rue de Provence × rue de la Chaussée-d'Antin crossing is at about
48.8745 N, 2.3330 E (from memory, ±50 m; OpenStreetMap could not be reached to check it).
**Still unchecked on 29 Oct 2026** (the map services are blocked too). This figure rests on no source at
all: do not move a pin onto it until it has been read off a map. The
current map estimate (48.8755, 2.3389) is about 420 m east-north-east of that. That error is
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
- Félix and Louis Lazare, *Dictionnaire administratif et historique des rues de Paris et de ses
  monuments* (1844), entry « Verdelet (rue) », Wikisource:
  https://fr.wikisource.org/wiki/Dictionnaire_administratif_et_historique_des_rues_de_Paris_et_de_ses_monuments/Verdelet_(rue)
  « En 1295, ce n'était qu'une ruelle étroite et puante hors des murs de l'enceinte de
  Philippe-Auguste. Elle se nommait alors rue Merderet. […] Plus tard, par altération, elle fut
  appelée rue Verderet, puis Verdelet. » The search extract also says that the 1311 *rôle de la
  taille* calls it « rue Breneuse ». A reprint of the same entry adds « Des actes de 1290, 1330,
  1352 et 1406 l'indiquent sous les noms de Merderiau, Merderai, Merderel et Merderet ».
- Archives nationales, register of Paris streets (*Voies de Paris*): « La rue Verdelet, qui était
  comprise entre les rues Jean-Jacques Rousseau et de la Jussienne, avait porté les noms de rue
  Mardelet ou Marderet (XIIIe siècle), Breneuse et enfin de rue Verderet ou Verdelet. »
  https://rdf.archives-nationales.culture.gouv.fr/place/FRAN_RI_025-d3nzcc8smx--w2i8uceiz29c-vdp-3149
  (the search engine tied the quote to one of this record and …-vdp-3953; I could not open them
  to check which.)
- French Wikipedia has *Rue Verderet (ancienne voie de Paris)* and a separate *Rue Merderet*,
  and notes the two are sometimes confused. Both lie on the same few metres, so this doesn't
  change the identification.
- Disagreement: an article on scatological street names (*Nouvelle revue d'onomastique* /
  OpenEdition, https://journals.openedition.org/nda/3928, citing Lock 1867) puts "Orde rue" in 1311
  and "Breneuse" after it. Either way the name belongs to this street.

**Why this one, and not the other "rues Breneuses".** The Archives nationales register also
gives "Breneuse" as an old name of the rue du Petit-Reposoir (renamed by a court ruling of
1582). That street lay further west, towards the later place des Victoires, beyond the rue
Pagevin. The label (3150, 5600) sits between R. DE LA PLATRIERE (L0408, 186 px),
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

**Possible inconsistency to check.** L0422 (R. PAGEVIN) is matched to `CUR:rue d'Argout`. The
Archives nationales register says the rue Pagevin of 1849 (Verdelet + Pagevin + Petit-Reposoir)
disappeared under the rue Étienne-Marcel and the Hôtel des Postes. If that's right, Pagevin is
vanished, not today's rue d'Argout. The rue d'Argout is the former rue des Vieux-Augustins, which
L0419 already covers. Worth a look in the register.

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
- The rue de la Barre was itself a new street: « rue Scipion (ancienne rue de la Barre, ouverte
  en 1540) » (fr.wikipedia, *Faubourg Saint-Marcel (quartier de Paris)*). Its name comes from a
  barrier near the rue des Francs-Bourgeois-Saint-Marcel. So a "rue Neuve" opening onto it in
  c. 1550 is plausible: a street from the same years, still known only as "the new street".
- Other streets were laid out here at the same time: the *séjour d'Orléans* was divided into
  plots in 1541/1545, opening the rues Censier and de la Clef (Atlas historique de Paris,
  https://paris-atlas-historique.fr/32.html; urbanisation-paris.com, « Le développement des
  faubourgs 1450-1600 »). Neither is next to the label, though.
- The rue des Francs-Bourgeois-Saint-Marcel ran from the rue des Fossés-Saint-Marcel to the
  place de la Collégiale, and is now under the boulevard Saint-Marcel (Lazare 1844; Carnavalet;
  INHA). It does meet the rue de la Barre, but its name dates from 1296 (Lazare), so it was not
  "new" in 1550. Unlikely.

**Hypotheses for someone with the books:**
1. A street opened with the rue de la Barre in 1540–1550 between the collegiate church and the
   rue de la Barre, known later under another name. I found no source naming it.
2. A first name of a street that the map also labels under another name. Check the rue du Fer-à-Moulin (Lazare: « rue
   Richebourg », « rue des Morts ») and the rue Pierre-Assis.

Search next in Jaillot, *Recherches critiques… sur la ville de Paris* (1772–1775), quartier de
la Place-Maubert / Saint-Marcel, which lists the faubourg's streets with their 16th-century
names; and in Berty and Tisserand, *Topographie historique du vieux Paris*, the volume on the
Saint-Marcel area (or Friedmann's ALPAGE parcel data). **No change made** to `streets.csv`.

# Control-point candidates for the edges of the map (2026-10-26)

The overlay is weakest where one control point carries a whole quarter. Leave-one-out errors in
`data/gcps_auto.csv` are 427 m at the Bastille (G006), 416 m at Saint-Médard (G015) and 221 m at
Saint-Germain-des-Prés (G003). Other gaps: the Tour de Nesle and rue de Seine are 1,370–1,540 px
from any control point, and the Marais north of the rue Saint-Antoine and the Montorgueil /
Coq-Héron quarter are about 1,000 px from one. At this scale 1,000 px is about 390 m (Notre-Dame
to Saint-Eustache is 3,090 px for 1,200 m).

Below are 15 candidates, ordered by the gap each one fills. Each is a point whose position
**today** is known to within about 10–20 m and which the woodcut should show: a standing
building, a street corner that hasn't moved since the 16th century, or a gate or tower site
fixed by a plaque or a later building.

**On the coordinates.** The sandbox could not reach OpenStreetMap, Wikipedia or the Paris
open-data registers. The "≈" coordinates below are my estimates, good to about ±50 m, given so
each point can be found. **Don't use them as control-point coordinates.** For street corners,
take the intersection of the two streets' centre lines in the Paris register geometry
(`work/ref/voies_actuelles.json`, the same source `resolve_streets.py` uses) or OSM. For
buildings, use the coordinates of the named building in OSM or Wikidata. The pixel position
must come from the drawn feature on the scan, not from the label, as was done for the existing
points. The "label" positions below only show where to look.

Columns: label position (x, y) on the scan; distance to the nearest current control point.

## East: the Bastille gap (G006, 427 m)

1. **Corner of rue de la Cerisaie and rue du Petit-Musc.** L0220 R. DE LA CERISEE (4930, 1165;
   358 px from G006) and L0221 R. DES CELLESTINS (5030, 1385; the rue du Petit-Musc's
   16th-century name in this stretch). The rue de la Cerisaie is drawn on this map. Both streets keep their medieval lines, and the rue
   du Petit-Musc was not widened. ≈ 48.8523, 2.3637. Sources: Paris street register (current
   streets) for both; Lazare (1844), « Cerisaie (rue de la) » and « Petit-Musc (rue du) ».
   *Best single candidate for this gap.*
2. **Corner of rue Saint-Antoine and rue Saint-Paul.** L0219 LA GRANT R. S. ANTHOINE
   (4660, 1480; 528 px) and L0230 R. S. POL (5070, 1725). Both are medieval streets on their old
   lines. The rue Saint-Antoine was widened on its south side in places, so put the point on the
   corner's centre line, not a building edge. ≈ 48.8541, 2.3621. Sources: the register; Lazare,
   « Saint-Antoine (rue) », « Saint-Paul (rue) ».
3. **Corner of rue Saint-Paul and rue des Lions-Saint-Paul.** L0232 R. NEUVE S. POL
   (5340, 1550; 919 px). Cousin (1875, entry « SAINT-PAUL (rue Neuve) ») places this label on
   the line of today's rue des Lions-Saint-Paul, laid out on the former Hôtel Saint-Pol lands.
   ≈ 48.8527, 2.3613. Sources: Cousin 1875 (in `cousin_1875_table.txt`); the register.
4. **Hôtel de Sens** (unlabelled on the map; standing; built 1475–1519; 1 rue du Figuier). The
   only standing great house of the period on this side. If the woodcut draws it next to the
   Ave-Maria (L0043, 5120, 1965; 824 px from Saint-Gervais), take its corner tower on the rue du
   Figuier. ≈ 48.8534, 2.3590. Sources: fr.wikipedia « Hôtel de Sens »; its Mérimée
   listing. *Only if it can be recognised on the scan.*
5. **Corner of rue de Sévigné and rue des Francs-Bourgeois.** L0228 LA R. S. CATERINE
   (3840, 1880; 1,036 px) and L0239 R. DE POULISE (3610, 2010). The rue Culture-Sainte-Catherine
   (now de Sévigné) met the rue des Francs-Bourgeois (here the rue des Poulies) at the corner
   where the Hôtel Carnavalet was being built, from 1548. Check it against the Poulies relabelling
   noted in LOG.md, where L0413…L0435 were shifted by the engraver. ≈ 48.8572, 2.3627. Sources:
   the register; fr.wikipedia « Hôtel Carnavalet » (begun 1548).

## South-east: the Saint-Médard gap (G015, 416 m)

6. **Corner of rue Mouffetard and rue Daubenton.** L0233 R. DORLEANS (9090, 1650; 444 px). The
   rue d'Orléans-Saint-Marcel (now rue Daubenton) meets the rue Mouffetard just north of
   Saint-Médard. A second point next to G015 would steady it more than anything else.
   ≈ 48.8404, 2.3502. Sources: the register (history of the current rue Daubenton); Lazare,
   « Orléans-Saint-Marcel (rue d') ».
7. **Corner of rue Scipion and rue du Fer-à-Moulin.** L0222 R. DE LA BARRE (9250, 1050; 657 px)
   and L0223 R. DU FER DE MOULAIN (9320, 1200; 491 px). The rue de la Barre was opened in 1540.
   The Hôtel Scipion (1565) stands at this corner: « rue de la Barre à l'angle de l'actuelle rue
   du Fer à Moulin » (fr.wikipedia, « Faubourg Saint-Marcel (quartier de Paris) »). The house
   postdates the map, but the corner doesn't. ≈ 48.8391, 2.3548. Sources: that article; the
   register (history of the rue Scipion).

## South: between Saint-Jacques-du-Haut-Pas and the Sorbonne

8. **Porte Saint-Jacques (site).** L0175 PORTE S. IAQUES (9250, 3840; 735 px from the nearest
   point). The Philippe Auguste gate across the rue Saint-Jacques, demolished in 1684; « une
   plaque commémorative rappelle son emplacement sur l'immeuble situé au 172, rue Saint-Jacques »,
   and it stood between nos. 151 bis and 172 (fr.wikipedia « Porte Saint-Jacques », via a
   mirror: https://franco.wiki/fr/Porte_Saint-Jacques.html; Ville de Paris, « Sur la piste de
   l'enceinte Philippe-Auguste, rive gauche »,
   https://www.paris.fr/pages/sur-la-piste-de-l-enceinte-medievale-philippe-auguste-rive-gauche-episode-2-2-21081).
   Point: the rue Saint-Jacques centre line at no. 172, at the rue Soufflot. ≈ 48.8466, 2.3437.
   The gate is drawn as a building across the street, so its middle is a clean pixel target.

## South-west and west: Saint-Germain-des-Prés (G003, 221 m) and the empty band along the Seine

9. **Tour de Nesle (site).** L0181 LA TOUR NELLE (6470, 5860; 1,366 px from the nearest point,
   the largest gap in the city). Demolished in 1665; « Elle était située à l'emplacement actuel
   du pavillon ouest de la bibliothèque Mazarine » (fr.wikipedia « Tour de Nesle », via
   Structurae). The English Wikipedia (« Bibliothèque Mazarine ») says the library was built on
   « the exact site » of the tower. Point: the river corner of the Mazarine's west pavilion, quai
   de Conti. ≈ 48.8577, 2.3366. A round tower on the bank is a sharp target on the woodcut.
   Caveat: Techno-Science puts it « à peu près à l'angle gauche du palais de l'Institut », about
   30 m away. Medium precision.
10. **Carrefour de Buci (corner of rue de Seine and rue de Buci).** L0438 R. DE SEINE
    (6540, 6300; 1,542 px). The rue de Seine and the rue de Buci, the old road out of the Porte de
    Buci (L0178), both keep their 16th-century lines. ≈ 48.8538, 2.3369. Sources: the register;
    Lazare, « Seine-Saint-Germain (rue de) », « Bussy (rue de) ». Check on the scan that the
    drawn junction is the rue de Seine and not the rue Mazarine (des Fossés).
11. **Carrefour de la Croix-Rouge (rue du Four, rue du Vieux-Colombier, rue du Cherche-Midi).**
    L0439 R. DU FOUR (9130, 6150; 587 px from Saint-Sulpice) and L0432 R. S. SURPLICE, now rue du
    Vieux-Colombier (9030, 5950). It's a medieval crossroads west of the abbey, and the obvious
    second anchor for G003. ≈ 48.8514, 2.3296. Sources: the register; fr.wikipedia « Carrefour de
    la Croix-Rouge ».

## North and north-west: Montorgueil, Coq-Héron, the upper Marais

12. **Corner of rue Coquillière and rue Coq-Héron.** L0424 R. COQUILLIERE (3530, 5780; 868 px)
    and L0423 R. QUOQUEHERON (3260, 5700; 916 px). Both are medieval streets on their lines.
    The rue Coquillière lost its west end to the Halles works, but not at this corner.
    ≈ 48.8645, 2.3424. Sources: the register; Lazare, « Coquillière (rue) », « Coq-Héron (rue) ».
13. **Corner of rue Saint-Denis and rue Saint-Sauveur.** L0373 R. S. SAUVEUR (2550, 4800;
    1,029 px). Both are 13th-century streets. The rue Saint-Denis is the map's main north–south
    axis, so its corners are reliable. ≈ 48.8660, 2.3500. Sources: the register; Lazare,
    « Saint-Sauveur (rue) ».
14. **Corner of rue du Temple and rue Pastourelle.** L0261 LA GRANT R. DU TAMPLE (3080, 2705;
    956 px) and L0259 R. PATOURELLE (2950, 2560; 991 px). The rue Pastourelle (13th century) is
    unchanged. ≈ 48.8630, 2.3591. Sources: the register; Lazare, « Pastourelle (rue) ».
15. **Corner of rue Croix-des-Petits-Champs and rue Saint-Honoré.** L0434 R. DES PETIS CHANS
    (3590, 6000; 1,068 px). This fills the north-west, between Saint-Eustache and the Louvre. The
    street's south end at the rue Saint-Honoré hasn't moved. Its north end was rebuilt with the
    Banque de France and the place des Victoires, so take only the Saint-Honoré corner.
    ≈ 48.8625, 2.3404. Sources: the register; Lazare, « Croix-des-Petits-Champs (rue) ».

## Considered and left out

- **The Charles V gates** (Saint-Denis, Saint-Martin, du Temple, Saint-Honoré, Montmartre):
  sources disagree on their sites. For the Porte Saint-Denis, one source gives no. 248 rue
  Saint-Denis at the rue Blondel, while others mix it up with the Philippe Auguste gate at the
  rue Étienne-Marcel or with the 1672 arch. The Charles V Porte Saint-Honoré stood at the vanished
  rue du Rempart, not a fixed point today. Worth a second look with Hillairet or plaques in
  hand: they are exactly where the map is weakest (north).
- **The Bastille itself:** G006 is already there. The stones in square Henri-Galli were moved
  in 1899 and are **not** in situ; only the outline in the paving of the place de la Bastille
  is.
- **The far villages and bridges** (Charenton, Vincennes, Montmartre, Belleville…): drawn in
  shortened perspective at the sheet's margin, not to scale. Pinning the spline to them would
  bend the city edge to fit a schematic drawing.
- **The Philippe Auguste wall remnants** (rue des Jardins-Saint-Paul, rue Clovis, cour du
  Commerce-Saint-André): exactly placed today, but on the right bank the map draws the later
  Charles V wall, and the rue Clovis stretch is next to G005 anyway.

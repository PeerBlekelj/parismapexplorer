# Paris Map Explorer

The Truschet & Hoyau plan of Paris (*La ville, cité et université de Paris*, c. 1550, known as the
Basel plan) side by side with the city today. Search any place named on the old map by its old or
modern name and see where it was and what is there now.

**Site:** https://parismapexplorer.vercel.app

- 453 places named on the map, each identified with today's place (or marked as vanished, shown
  where it stood), with a short description and sources.
- The 1550 map and modern Paris side by side and synced, or overlaid: the woodcut is warped onto
  modern streets with a thin-plate spline through 40 control points (typical error about 60 m).
  How that works, how accurate it is and where it fails:
  [How the map was bent](https://parismapexplorer.vercel.app/method/).
- Search by old or modern name, tolerant of 16th-century spellings.
- Every place has its own link, e.g. https://parismapexplorer.vercel.app/place/L0006/

Corrections are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) and the list of
[open questions](data/research/OPEN_QUESTIONS.md). Project notes: [PLAN.md](PLAN.md).

## Sources

- The map: *La ville, cité et université de Paris*, Olivier Truschet and Germain Hoyau, c. 1550
  (the "Basel plan"), Basel University Library, via Wikimedia Commons.
- Street identifications: Ville de Paris open data, registers of current and vanished street names
  (*Dénominations des emprises des voies actuelles* / *des voies caduques*).
- Buildings and places: Wikipedia (French and English) and Wikidata.

## Licences

- Code: MIT.
- Place data and texts: CC BY-SA 4.0 (texts draw on Wikipedia).
- The 1550 map: public domain (scan: Basel University Library, via Wikimedia Commons).
- Modern map data: © OpenStreetMap contributors.

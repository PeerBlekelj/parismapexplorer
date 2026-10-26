# Paris 1550

The Truschet & Hoyau plan of Paris (*La ville, cité et université de Paris*, c. 1550, known as the
Basel plan) side by side with the city today. Search any place named on the old map by its old or
modern name and see where it was and what is there now.

**Site:** https://paris1550.vercel.app: the start page tells the map's story (who made it, how it is
dated, how its only copy turned up in Basel; also in [French](https://paris1550.vercel.app/fr/) and
[Swedish](https://paris1550.vercel.app/sv/)). The map itself: https://paris1550.vercel.app/map/

- 455 places named on the map, each identified with today's place (or marked as vanished, shown
  where it stood), with a short description and sources.
- The 1550 map and modern Paris side by side and synced, or overlaid: the woodcut is warped onto
  modern streets with a thin-plate spline through 46 control points (typical error about 60 m).
  How that works, how accurate it is and where it fails:
  [How the map was bent](https://paris1550.vercel.app/method/).
- Search by old or modern name, tolerant of 16th-century spellings.
- Every place has its own link, e.g. https://paris1550.vercel.app/place/L0006/
- The texts printed on the map (a 108-line poem in praise of Paris and the publishers' notice),
  transcribed and translated line by line into English, modern French and Swedish:
  [The texts on the map](https://paris1550.vercel.app/texts/) (built by `scripts/make_texts_page.py`).

Corrections are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) and the list of
[open questions](data/research/OPEN_QUESTIONS.md). Project notes: [PLAN.md](PLAN.md).

Built with [Claude Code](https://claude.com/claude-code): the labels were read off the scan,
identified, and the site written by Claude, directed and reviewed by the project's editor. See
[How the map was bent](https://paris1550.vercel.app/method/#built).

## Sources

- The map: *La ville, cité et université de Paris*, Olivier Truschet and Germain Hoyau, c. 1550
  (the "Basel plan"), Basel University Library, via Wikimedia Commons.
- Street identifications: Ville de Paris open data, registers of current and vanished street names
  (*Dénominations des emprises des voies actuelles* / *des voies caduques*).
- Buildings and places: Wikipedia (French and English) and Wikidata.
- Checked against Jules Cousin's table of the map's names, *Mémoires de la Société de l'histoire de
  Paris et de l'Île-de-France*, t. I (1875), pp. 60–70 (source gallica.bnf.fr / BnF); transcription in
  `data/research/cousin_1875_table.txt`, pairing per label in `data/research/cousin.csv`.

## Licences

- Code: MIT.
- Place data and texts: CC BY-SA 4.0 (texts draw on Wikipedia).
- The 1550 map: public domain (scan: Basel University Library, via Wikimedia Commons).
- Modern map data: © OpenStreetMap contributors.

# Favicon options for "Paris 1550"

See `preview.png`: each option at 64, 32 and 16 px, the 16 px rendering blown up 4×, and in a
dark and a light browser tab. Letters are EB Garamond Bold converted to paths (fonts don't load
inside favicons). Palette: ink #2b2118, paper #f4ecdc, red #a63a1f, blue #3d5a78.
`sheet.html` rebuilds the preview (open it next to the SVGs).

- **A** `a-1550-stacked.svg`: "15" over "50", ink and red on paper. Clear at 32 px; at 16 px each
  digit is about 5 px tall and the "50" blurs.
- **B** `b-p-red-ring.svg`: a serif P with the red ring the app draws round a selected place.
- **C** `c-ship-arms.svg`: the arms of Paris cut down to blocks: ship on red, three lozenges for the
  fleurs-de-lis on blue. At 16 px it reads as a red-and-blue flag, the ship as a white blob.
- **D** `d-seine-cite.svg`: the Seine's bend with the Île de la Cité ringed in red. The island
  vanishes at 16 px; what's left is a ring on a blue line.
- **E** `e-compass.svg`: an eight-point compass rose, the red point at the top. Since the 1550 map
  is printed east-up, the red point stands for east (ORIENS), not north.

**Chosen: A** (by the owner, 2026-10-26), now `web/public/favicon.svg`.

Recommended at the time: B. It is the only one with a single large shape plus one accent, so it stays
sharp at 16 px on both dark and light tabs. The ring ties it to the app (it is the selected-place marker),
and the P is in the site's type. E comes second (just as legible, but a compass rose is
what any map or travel site would use). C is the most "Paris" but is the weakest at 16 px, and it looks
like the city's official arms, which the site has no business borrowing as a logo.

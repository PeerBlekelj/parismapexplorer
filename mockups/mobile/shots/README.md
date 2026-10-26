# Screenshots of the built phone layout (option A)

Chromium via Playwright, touch emulation (`hasTouch`, `isMobile`), in a checkout without the map
tiles and with OpenFreeMap blocked, so both maps are blank paper here; the pink banner is the
"tiles missing" notice that only shows without tiles.

- `phone-390-*` (390 × 844) and `phone-360-*` (360 × 740): 1 peek, 2 half (grip tapped),
  3 search "pont", 4 a place opened from the list, 5 the card dragged up to full, 6 after the
  browser's Back (list, place highlighted), 7 overlay with the swipe dragged by touch, 8 the table,
  9 a table row opened, 10 opened from `/place/L0029/`.
- `desktop-1600-*-before/after` (1600 × 900): home, a place, overlay, table, on `main` and on
  this branch. The pairs are pixel-identical.

# Data contract: app ↔ place data

The app reads two static files. They are **generated** by `scripts/build_places.py` from
`data/` — never edit them by hand, and the app must never depend on anything else in `data/`.

## `public/data/places.json`

```jsonc
{
  "generated": "2026-10-25T18:50:02+00:00",
  "image": { "width": 10890, "height": 7820, "orientation": "east-up" },
  "places": [
    {
      "id": "L0123",              // permanent; safe for URLs (#place=L0123)
      "old": "S. CHRISTOFLE",     // label as printed (normalised spelling of letters, not modernised)
      "type": "church_religious", // street | church_religious | college | building | gate_wall |
                                  // bridge | square_market | village_faubourg | other |
                                  // inscription (see below)
      "px": [6430, 3665],         // label position in source-image pixels (x right, y down)
      "also_px": [[6420, 3900]],  // other labels naming the same place (duplicates); [] if none
      "orient": "h",              // label direction on the map: h | v | d (diagonal)
      "flag": "ok",               // ok | unsure  (reading of the label itself is uncertain)
      "note": "…" | null,         // working note from the transcription
      "modern": "Saint-Christophe" | null,
      "status": "standing" | "rebuilt" | "renamed" | "vanished" | null,
      "lat": 48.853 | null, "lon": 2.348 | null,
      "loc_confidence": "exact" | "approx" | "uncertain" | null,
      "summary": "2–4 sentences, English" | null,
      "summary_fr": "the same in French" | null,   // null: not translated yet; show `summary`
      "summary_sv": "the same in Swedish" | null,
      "detail": "a longer description, English" | null,
      "reading": "clear" | "confirmed" | "disputed" | "uncertain",
      "reading_other": "Rueli" | null,          // the other reading, when "disputed"
      "variants": ["Saint-Christofle", "…"],
      "sources": [{ "label": "Wikipedia (fr)", "url": "https://…" }]
    }
  ]
}
```

### `type: "inscription"`

The sheet's own words and devices: the title banderole, the quarter and wind names, the two coats
of arms, the king's crescents, the poem, the publishers' notice, the Basel library stamp. They are
ink on the paper, not somewhere you can stand, and they carry two extra fields:

```jsonc
"printed": true,   // false for a device with no text: `old` is then a NAME we give it, not a
                   // reading, and the app translates it (deviceNames in src/strings.ts)
"texts": "winds"   // which part of /texts/ explains it: title | winds | arms | basel |
                   // poem | notice
```

An inscription has `modern`, `status`, `lat`, `lon` and `loc_confidence` all null, and the app must
**not** estimate a modern position for it, show it on the modern map, or describe it as "not
identified yet": there is nothing to identify. The app counts them apart from the 457 places.

`summary_fr` / `summary_sv` are translations of `summary` from `data/research/summaries_fr.csv` and
`summaries_sv.csv`; show the one for the current language and fall back to `summary`.

### `reading`

How well attested our reading of `old` is. `flag` is the raw note the tile-by-tile transcription
pass left about **its own** doubt; `reading` is what became of that doubt once Jules Cousin's 1875
reading of the same label was compared against ours.

- **`clear`** — the transcription pass had no doubt.
- **`confirmed`** — it had doubt, and Cousin printed the same reading, character for character
  (case, accents and the `R.`/`S.` abbreviations aside). Two readers a century apart agree, so the
  reading is settled and the card must **not** call the label hard to read.
- **`disputed`** — it had doubt, and Cousin read something else. `reading_other` carries his
  reading; show both and prefer neither.
- **`uncertain`** — it had doubt and there is no second reading. Cousin's alphabetical index
  heading does not count: it is his name for the street, not his transcription of the ink.

Of 24 labels the transcription pass flagged, 14 are `confirmed`, 2 are `disputed`
(`REUILLI`/*Rueli*, `BAIEUS`/*Raieus*) and 8 are `uncertain`. The "unsure reading" filter and the
table column count the 10 that are still open, not all 24.

### `detail`

A longer description, 40–160 words, from `data/research/details.csv`. It **continues** the summary
rather than replacing it, so the app shows it under the summary behind a disclosure and never
instead of it. English only: there is no `detail_fr`/`detail_sv` yet, so in French and Swedish the
card shows the English text and says so.

`detail` is `null` for most places, and that is a normal, final answer as often as it is a gap.
Each one is written from that place’s French source extract (`history_fr` in `data/places_*.csv`)
and checked against it by `scripts/ingest_detail.py`: every factual claim must be carried by a span
copied verbatim from the source, and every year in the text must appear in the source. Three reasons
a place has none, and the app must not distinguish them:

- the source is too thin to say more than the summary already does;
- the source is long but **off-period** — a modern commune or quarter article that describes
  today’s administration, not the place on the map. Those ids are listed with their reason in
  `data/research/details-held.csv`, waiting for a 16th-century source;
- the text failed a check and has not been rewritten.

**`null` means "not researched yet", never "nothing there".** Show it as "Not identified yet" /
"Location estimated from the map", never as an empty or negative state.

When `lat`/`lon` are null, the app may *estimate* a modern position from `px` with the
transform below, but must mark it visibly as estimated.

## `public/data/gcps.json`

Ground control points pairing old-map pixels with real coordinates:

```jsonc
{ "gcps": [ { "id": "G001", "name": "Notre-Dame", "px": [6490, 3585], "lat": 48.85296, "lon": 2.34903, "quality": "label" } ] }
```

`quality: "label"` = the pixel is the label's position, not the building itself (rough).
The set will grow from 20 to 100+ and become more precise; the app must fit its transform at
load time from whatever is in the file (no hard-coded coefficients).

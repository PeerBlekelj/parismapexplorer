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
                                  // bridge | square_market | village_faubourg | other
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
      "variants": ["Saint-Christofle", "…"],
      "sources": [{ "label": "Wikipedia (fr)", "url": "https://…" }]
    }
  ]
}
```

`summary_fr` / `summary_sv` are translations of `summary` from `data/research/summaries_fr.csv` and
`summaries_sv.csv`; show the one for the current language and fall back to `summary`.

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

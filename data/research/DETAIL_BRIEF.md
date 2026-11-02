# Brief: the longer place descriptions

Paste this whole file, then one `work/detail/batch-NN.json`, into a fresh conversation. One batch
per conversation. Return the JSON described under **What to return** and nothing else.

## What this is for

Paris 1550 (<https://paris1550.vercel.app>) pairs the Truschet & Hoyau plan of Paris, c. 1550, with
the city today. Every place named on the woodcut has a card with a **short description** of two to
four sentences, which is all a reader sees now. We want a **longer description** underneath it, shown
when the reader asks for more.

The short one stays exactly as it is. You are writing the *continuation*, not a replacement.

## The one rule that matters

**Every factual statement you write must be supported by the `source_fr` text supplied with that
place.** Not by what you know about Paris. Not by what is probably true of a street of that name.
Not by a reasonable inference about a family, a parish or a date.

This project has already had to undo claims that were plausible and wrong — a quotation attributed
to a brochure that does not contain it, a street "corrected" to match a Wikipedia article that had
conflated two different streets, a date that was internally impossible. A detail that cannot be
traced to the source is worse than no detail at all.

If the source is thin, **return a short detail, or `null`**. `null` is a correct and welcome answer.
Padding is not.

## Voice

Match the short descriptions you are given in `summary_now`. They are the house style:

> The oldest hospital in Paris, traditionally founded by bishop Saint Landry around 650. In 1878 it
> was rebuilt on the north side of the parvis of Notre-Dame.

> A small fortress guarding the Left Bank end of the Petit-Pont, the counterpart of the Grand
> Châtelet on the Right Bank. It served as a prison and was demolished in 1782.

- Plain British English. Concrete nouns, ordinary words, short sentences.
- Write for a curious reader looking at a 16th-century map, not for a tourist brochure and not for
  an encyclopaedia. No "nestled", "iconic", "rich history", "bustling", no rhetorical questions, no
  opening with "Located in…".
- French street and building names stay in French (*rue du Temple*, *hôtel de Nevers*). Do not
  translate them.
- Say "the map" for the 1550 sheet. The map is printed east-up; do not describe directions on it
  unless the source does.
- Dates and numbers exactly as the source gives them. If the source hedges, hedge.
- **Do not repeat the short description.** Start where it stops. Overlap of a phrase or two is
  unavoidable; a restatement is not.

## Which century to write about

The reader is looking at a woodcut of Paris made around 1550, and has clicked a place **on that
sheet**. Write about that place: what it was, who held it, what stood there, what it was for.

Some sources run from antiquity to last year. Take from them the part that bears on the map's own
century and the centuries before it, and let the modern end go. A commune's population in 2023, its
administrative quarter number, which party has held the town hall since 1925, the architects of a
1970s renovation and the tenants of a building today are all **true, sourced and wrong for this
card**. This is the single most common way a detail has failed here: nine were written entirely
from the modern end of their source and had to be thrown away.

Later history earns its place when it is the fate of the thing on the map — a gate demolished, a
convent turned into a medical school, a village swallowed by the city in 1860. That is the
continuation of the story. The population of the commune in 2023 is a different story.

If the source only has the modern end, say so in `notes` and return `null`.

## Length

**80 to 160 words.** Below 80, it is not worth a disclosure; above 160, it stops being a map card.
A place whose source supports only 50 words gets 50 words — do not stretch it.

## What to return

A single JSON array. One object per place in the batch, in the same order, every id present:

```json
[
  {
    "id": "L0080",
    "detail_en": "The hospital stood on the south side of the parvis … ",
    "used": [
      "fondé en 651 par saint Landry",
      "reconstruit de 1867 à 1878 au nord du parvis"
    ],
    "added_beyond_source": [],
    "notes": ""
  }
]
```

- **`detail_en`** — the longer description, or `null` if the source does not support one.
- **`used`** — short spans **copied verbatim** from that place's `source_fr`, one for each factual
  claim you make. These are checked mechanically against the source text: a span that is not found
  verbatim fails the batch. Copy, do not paraphrase, and keep the original accents.
- **`added_beyond_source`** — anything in `detail_en` that is *not* from the source. This should
  normally be empty. If you believe a piece of context is worth adding, put the sentence here as
  well as in the text so a human can check it. Do not add it silently.
- **`notes`** — free text for anything the next reader should know: a contradiction inside the
  source, an ambiguity, a name that might be two different places. Empty string if none.

Nothing else. No prose before or after the JSON, no code fence commentary, no markdown.

## Traps this project has already fallen into

Read these before you start; they are the shape of the mistakes that happen here.

1. **Two streets, one name.** French Wikipedia's *rue Verderet* article conflates two separate
   entries in Lazare's dictionary. If a source describes a street in two places at once, say so in
   `notes` and write nothing that depends on it.
2. **The later building with the same name.** The *hôtel d'Angoulême-Lamoignon* was begun in 1584,
   the *hôtel de Nevers* on the Monnaie site in the 1580s — a generation after this map. A source
   about those is not a source about what the map shows. If the `source_fr` is plainly about a later
   building, write `null` and say why in `notes`.
3. **An administrative extract is not a history.** Many of the street sources are register text
   ("Tronçon A : précédemment partie de la rue du Chaume…"). You may draw the street's course and
   its former names from it. Do not dress it up as a story.
4. **A number you did not read.** Every four-digit year in `detail_en` is checked against the source.
   If the year is not in the source, do not write it.

## Fields you are given

| field | meaning |
|---|---|
| `id` | the place's permanent id — return it unchanged |
| `on_the_map` | the label as printed on the woodcut, in 16th-century spelling |
| `today` | the modern name, or `null` if the place is gone or unidentified |
| `status` | standing, rebuilt, renamed, vanished, or `null` for not researched |
| `type` | street, church_religious, college, building, gate_wall, bridge, square_market, village_faubourg, other |
| `summary_now` | the short description the site already shows — do not repeat it |
| `source_fr` | **the only material you may draw facts from**: French Wikipedia and the Ville de Paris street register, as collected by this project |
| `sources` | the labels of the sources already cited on the card, for context |

## After you return it

On our side: `scripts/ingest_detail.py` checks that every id is present and known, that every `used`
span appears verbatim in that place's source, that every year in the text appears in the source,
that the length is in range, that `added_beyond_source` is empty, and that the detail is not a
restatement of the summary. Whatever fails comes back for another pass.

French and Swedish translations are a separate job, after the English is reviewed.

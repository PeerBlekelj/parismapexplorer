// All UI strings live here so French and Swedish can be added later: add an object with the
// same shape as `en` and pick it in `t`.

const en = {
  siteName: 'Paris 1550',
  brandTitle: 'La Ville, Cité et Université de Paris',
  brandSub: 'the Truschet & Hoyau map, with Paris today',

  viewMap: 'Map',
  viewTable: 'Table of places',

  searchPlaceholder: 'Search…',
  searchLabel: 'Search old or modern names',
  searchClear: 'Clear search',
  chipAll: 'All',
  chipUnsure: 'Unsure reading',
  filters: 'Filters',
  filtersActive: (n: number) => `Filters · ${n}`,
  filtersTitle: 'Filter by type or reading',
  count: (n: number, total: number) => (n === total ? `${total} places` : `${n} of ${total} places`),
  noResults: 'No places match. Try fewer letters, or another spelling.',

  // map area
  modeSide: 'Side by side',
  modeOverlay: 'Overlay',
  modeOld: '1550 only',
  modeMod: 'Today only',
  orientNorth: 'North up',
  orientOriginal: 'Original orientation',
  orientTitle: 'Orientation',
  tagOldNorth: 'Truschet & Hoyau, c. 1550 (rotated north-up)',
  tagOldOriginal: 'Truschet & Hoyau, c. 1550 (as printed, east at top)',
  tagMod: 'Today: © OpenStreetMap contributors',
  overlayOpacity: 'Old map',
  overlayOpacityUnit: 'opacity',
  overlaySwipeHint: 'drag ⇆ to swipe',
  overlayLeft: '1550',
  overlayRight: 'Today',
  overlayNoteWarped: (n: number | null, median: number | null) =>
    `Alignment is approximate: the old map is warped to fit modern streets${n ? ` through ${n} control points` : ''}` +
    `${median ? ` (typical error about ${roundTo(median, 10)} m)` : ''}. It fits best in the centre and less well towards the edges.`,
  overlayNote: (n: number, rms: number) =>
    `Alignment is approximate: the old map is placed with a simple fit through ${n} control points (typical error about ${roundTo(rms, 10)} m).`,
  tilesMissing: 'The old-map tiles are missing. Run scripts/make_old_tiles.py.',

  // card
  cardClose: 'Close',
  backToList: (n: number) => `← Back to ${n} ${n === 1 ? 'place' : 'places'}`,
  intro: 'Search for a place, pick one from the list, or click a label on either map.',
  introNote: 'Every name printed on the 1550 map is listed. Identifications and descriptions are still being added and checked.',
  notIdentified: 'Not identified yet',
  noLongerExists: 'No longer exists',
  formerSite: 'former site',
  pinTags: {
    approx: 'approximate',
    uncertain: 'uncertain',
    unassessed: '',
    estimated: 'estimated',
    exact: '',
  } as Record<string, string>,
  today: 'Today',
  noSummary: 'No description yet.',
  noSources: 'No sources yet.',
  sources: 'Sources',
  onMapAs: 'On the map as',
  transcription: 'Transcription note',
  reading: 'Reading',
  readingOk: 'Clear',
  readingUnsure: 'Unsure: the label is hard to read',
  variants: 'Spelling variants',
  noVariants: 'None recorded yet',
  pos1550: 'Position (1550)',
  posToday: 'Position today',
  pxFmt: (x: number, y: number) => `x ${Math.round(x)}, y ${Math.round(y)} px on the scan`,
  estimated: 'Location estimated from the map',
  estimatedHow: (n: number, rms: number) =>
    `Fitted through ${n} control points; typical error about ${roundTo(rms, 10)} m.`,
  confidence: 'confidence',
  confidenceUnknown: 'confidence not assessed yet',
  confidenceLabels: { exact: 'exact', approx: 'approximate', uncertain: 'uncertain' } as Record<string, string>,
  link: 'Link to this place',
  id: 'Id',
  cropCaption: 'As printed on the 1550 map (east at top)',
  unsureBadge: 'Unsure reading',

  statusLabels: {
    standing: 'Still standing',
    rebuilt: 'Rebuilt',
    renamed: 'Renamed',
    vanished: 'Vanished',
  } as Record<string, string>,
  statusUnknown: 'Not researched yet',

  typeLabels: {
    street: 'Street',
    church_religious: 'Church or religious house',
    college: 'College',
    building: 'Building',
    gate_wall: 'Gate or wall',
    bridge: 'Bridge',
    square_market: 'Square or market',
    village_faubourg: 'Village or faubourg',
    other: 'Other',
  } as Record<string, string>,
  typeChips: {
    church_religious: 'Churches',
    college: 'Colleges',
    street: 'Streets',
    gate_wall: 'Gates & walls',
    bridge: 'Bridges',
    building: 'Buildings',
    square_market: 'Squares & markets',
    village_faubourg: 'Villages',
    other: 'Other',
  } as Record<string, string>,

  // table
  colId: 'Id',
  colOld: 'On the map (1550)',
  colModern: 'Today',
  colType: 'Type',
  colStatus: 'Status',
  colReading: 'Reading',
  tableHint: 'Click a row to show the place on the map.',

  // credits
  creditMap: 'Map: Truschet & Hoyau, c. 1550, Basel University Library (public domain)',
  creditOsm: '© OpenStreetMap contributors',
  creditBy: 'by Peer Blekelj, built with Claude Code',
  creditMethod: 'How the map was bent',
  oldAttribution: 'Truschet &amp; Hoyau, c. 1550 · Basel University Library (public domain)',

  loadError: 'Could not load the place data.',

  // correction link (opens a pre-filled GitHub issue)
  suggestCorrection: 'Suggest a correction',
  suggestCorrectionHint: 'Opens a pre-filled issue on GitHub (needs a GitHub account)',
};

function roundTo(v: number, step: number): number {
  return Math.max(step, Math.round(v / step) * step);
}

export type Strings = typeof en;
export const t: Strings = en;

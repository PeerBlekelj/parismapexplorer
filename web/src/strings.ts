// All UI strings, one object per language with the same shape as `en`. Pure data, no DOM: the
// build (vite.config.ts) reads it too, for the static per-language pages. The runtime side
// (which language is on, switching it) is i18n.ts.

const en = {
  siteName: 'Paris 1550',

  // the static pages' <head> (vite.config.ts): home page, and the lead of each place's description
  ogLocale: 'en_GB',
  siteTitle: 'Paris 1550 · the Truschet & Hoyau map and the city today',
  siteDesc: 'Every place named on the Truschet & Hoyau plan of Paris, c. 1550, found on the map and in the city today.',
  siteImageAlt: 'The Île de la Cité and both banks on the Truschet & Hoyau plan of Paris',
  placeLead: (old: string, status: string | null, modern: string | null) =>
    `“${old}” on the Truschet & Hoyau plan of Paris, c. 1550` +
    (status === 'standing' ? ': still standing' : status === 'rebuilt' ? ': rebuilt' : status === 'vanished' ? ': vanished'
      : status === 'renamed' ? `: renamed${modern ? ` as ${modern}` : ''}` : '') + '.',
  placeImageAlt: (old: string) => `The label “${old}” on the 1550 map`,
  brandTitle: 'La Ville, Cité et Université de Paris',
  brandSub: 'the Truschet & Hoyau map, with Paris today',
  brandHome: 'Back to the start',

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
  creditTexts: 'Texts on the map',
  creditAbout: 'About the map',
  welcomeTitle: 'New here?',
  welcomeText: 'Who made this map of Paris around 1550, how it is dated, and how its only copy turned up in Basel.',
  welcomeLink: 'Read about the map →',
  welcomeDismiss: 'Dismiss',
  oldAttribution: 'Truschet &amp; Hoyau, c. 1550 · Basel University Library (public domain)',

  loadError: 'Could not load the place data.',

  // correction link (opens a pre-filled GitHub issue)
  suggestCorrection: 'Suggest a correction',
  suggestCorrectionHint: 'Opens a pre-filled issue on GitHub (needs a GitHub account)',

  langLabel: 'Language',
  colon: ': ',
  quote: (s: string) => `“${s}”`,

  // The modern names in the data are English where they describe (see localModern in model.ts).
  partOf: (name: string) => `part of ${name}`,
  and: ' and ',
  modernNames: {} as Record<string, string>,
  modernNotes: {} as Record<string, string>,
  compass: { N: 'N', S: 'S', E: 'E', W: 'W' } as Record<string, string>,

  // phone layout: short labels for the narrow bars, and the sheet's grip
  viewTableShort: 'Table',
  modeSideShort: 'Both',
  modeOverlayShort: 'Overlay',
  modeOldShort: '1550',
  modeModShort: 'Today',
  orientOriginalShort: 'As printed',
  sheetGrip: 'Show more or less',
  sortLabel: 'Sort',
  sortDefault: 'Best match',
};

function roundTo(v: number, step: number): number {
  return Math.max(step, Math.round(v / step) * step);
}


export type Strings = typeof en;

// French typography: a no-break space before : ; ? ! and inside « ».
const NB = ' ';

const fr: Strings = {
  siteName: 'Paris 1550',

  ogLocale: 'fr_FR',
  siteTitle: 'Paris 1550 · le plan de Truschet et Hoyau et la ville d’aujourd’hui',
  siteDesc: 'Tous les lieux nommés sur le plan de Paris de Truschet et Hoyau, vers 1550, retrouvés sur le plan et dans la ville d’aujourd’hui.',
  siteImageAlt: 'L’île de la Cité et les deux rives sur le plan de Paris de Truschet et Hoyau',
  // The status words agree with « lieu », as the badges do.
  placeLead: (old: string, status: string | null, modern: string | null) =>
    `«${NB}${old}${NB}» sur le plan de Paris de Truschet et Hoyau, vers 1550` +
    (status === 'standing' ? `${NB}: existe encore` : status === 'rebuilt' ? `${NB}: reconstruit` : status === 'vanished' ? `${NB}: disparu`
      : status === 'renamed' ? `${NB}: renommé${modern ? `, aujourd’hui ${modern}` : ''}` : '') + '.',
  placeImageAlt: (old: string) => `Le nom «${NB}${old}${NB}» sur le plan de 1550`,
  brandTitle: 'La Ville, Cité et Université de Paris',
  brandSub: 'la carte de Truschet & Hoyau, avec Paris aujourd’hui',
  brandHome: 'Revenir au début',

  viewMap: 'Carte',
  viewTable: 'Tableau',

  searchPlaceholder: 'Chercher…',
  searchLabel: 'Chercher un nom ancien ou actuel',
  searchClear: 'Effacer la recherche',
  chipAll: 'Tous',
  chipUnsure: 'Lecture incertaine',
  filters: 'Filtres',
  filtersActive: (n: number) => `Filtres · ${n}`,
  filtersTitle: 'Filtrer par type ou par lecture',
  count: (n: number, total: number) => (n === total ? `${total} lieux` : `${n} ${n > 1 ? 'lieux' : 'lieu'} sur ${total}`),
  noResults: 'Aucun lieu ne correspond. Essayez avec moins de lettres, ou une autre graphie.',

  modeSide: 'Côte à côte',
  modeOverlay: 'Superposition',
  modeOld: 'Plan de 1550',
  modeMod: 'Aujourd’hui',
  orientNorth: 'Nord en haut',
  orientOriginal: 'Orientation d’origine',
  orientTitle: 'Orientation',
  tagOldNorth: 'Truschet & Hoyau, vers 1550 (pivoté, nord en haut)',
  tagOldOriginal: 'Truschet & Hoyau, vers 1550 (tel qu’imprimé, est en haut)',
  tagMod: `Aujourd’hui${NB}: © les contributeurs d’OpenStreetMap`,
  overlayOpacity: 'Plan ancien',
  overlayOpacityUnit: 'opacité',
  overlaySwipeHint: 'faire glisser ⇆ pour comparer',
  overlayLeft: '1550',
  overlayRight: 'Aujourd’hui',
  overlayNoteWarped: (n: number | null, median: number | null) =>
    `Le calage est approximatif${NB}: le plan ancien est déformé pour épouser les rues actuelles${n ? ` à l’aide de ${n} points de calage` : ''}` +
    `${median ? ` (erreur typique d’environ ${roundTo(median, 10)} m)` : ''}. Il est plus juste au centre que vers les bords.`,
  overlayNote: (n: number, rms: number) =>
    `Le calage est approximatif${NB}: le plan ancien est placé par un ajustement simple sur ${n} points de calage (erreur typique d’environ ${roundTo(rms, 10)} m).`,
  tilesMissing: 'Les tuiles du plan ancien sont absentes. Lancez scripts/make_old_tiles.py.',

  cardClose: 'Fermer',
  backToList: (n: number) => (n > 1 ? `← Retour aux ${n} lieux` : '← Retour à la liste'),
  intro: 'Cherchez un lieu, choisissez-en un dans la liste, ou cliquez sur un nom sur l’une des deux cartes.',
  introNote: 'Tous les noms imprimés sur le plan de 1550 sont répertoriés. Les identifications et les descriptions sont encore en cours d’ajout et de vérification.',
  notIdentified: 'Pas encore identifié',
  noLongerExists: 'N’existe plus',
  formerSite: 'ancien emplacement',
  pinTags: {
    approx: 'approximatif',
    uncertain: 'incertain',
    unassessed: '',
    estimated: 'estimé',
    exact: '',
  } as Record<string, string>,
  today: 'Aujourd’hui',
  noSummary: 'Pas encore de description.',
  noSources: 'Pas encore de sources.',
  sources: 'Sources',
  onMapAs: 'Sur le plan',
  transcription: 'Note de transcription',
  reading: 'Lecture',
  readingOk: 'Sûre',
  readingUnsure: `Incertaine${NB}: le nom est difficile à lire`,
  variants: 'Variantes orthographiques',
  noVariants: 'Aucune relevée pour l’instant',
  pos1550: 'Position (1550)',
  posToday: 'Position actuelle',
  pxFmt: (x: number, y: number) => `x ${Math.round(x)}, y ${Math.round(y)} px sur la numérisation`,
  estimated: 'Emplacement estimé d’après le plan',
  estimatedHow: (n: number, rms: number) =>
    `Calculé à partir de ${n} points de calage${NB}; erreur typique d’environ ${roundTo(rms, 10)} m.`,
  confidence: 'précision',
  confidenceUnknown: 'précision non encore évaluée',
  confidenceLabels: { exact: 'exacte', approx: 'approximative', uncertain: 'incertaine' } as Record<string, string>,
  link: 'Lien vers ce lieu',
  id: 'Id',
  cropCaption: 'Tel qu’imprimé sur le plan de 1550 (est en haut)',
  unsureBadge: 'Lecture incertaine',

  // Masculine, agreeing with « lieu ».
  statusLabels: {
    standing: 'Existe encore',
    rebuilt: 'Reconstruit',
    renamed: 'Renommé',
    vanished: 'Disparu',
  } as Record<string, string>,
  statusUnknown: 'Pas encore étudié',

  typeLabels: {
    street: 'Rue',
    church_religious: 'Église ou maison religieuse',
    college: 'Collège',
    building: 'Édifice',
    gate_wall: 'Porte ou enceinte',
    bridge: 'Pont',
    square_market: 'Place ou marché',
    village_faubourg: 'Village ou faubourg',
    other: 'Autre',
  } as Record<string, string>,
  typeChips: {
    church_religious: 'Églises',
    college: 'Collèges',
    street: 'Rues',
    gate_wall: 'Portes et enceinte',
    bridge: 'Ponts',
    building: 'Édifices',
    square_market: 'Places et marchés',
    village_faubourg: 'Villages',
    other: 'Autres',
  } as Record<string, string>,

  colId: 'Id',
  colOld: 'Sur le plan (1550)',
  colModern: 'Aujourd’hui',
  colType: 'Type',
  colStatus: 'Statut',
  colReading: 'Lecture',
  tableHint: 'Cliquez sur une ligne pour voir le lieu sur la carte.',

  creditMap: `Plan${NB}: Truschet & Hoyau, vers 1550, bibliothèque universitaire de Bâle (domaine public)`,
  creditOsm: '© les contributeurs d’OpenStreetMap',
  creditBy: 'par Peer Blekelj, réalisé avec Claude Code',
  creditMethod: 'Comment le plan a été déformé',
  creditTexts: 'Les textes du plan',
  creditAbout: 'À propos du plan (en anglais)',
  welcomeTitle: `Première visite${NB}?`,
  welcomeText: 'Qui a fait ce plan de Paris vers 1550, comment on le date, et comment son unique exemplaire a resurgi à Bâle.',
  welcomeLink: 'Lire la présentation (en anglais) →',
  welcomeDismiss: 'Fermer',
  oldAttribution: 'Truschet &amp; Hoyau, vers 1550 · bibliothèque universitaire de Bâle (domaine public)',

  suggestCorrection: 'Proposer une correction',
  suggestCorrectionHint: 'Ouvre un ticket prérempli sur GitHub (compte GitHub nécessaire)',
  viewTableShort: 'Tableau',
  modeSideShort: 'Les deux',
  modeOverlayShort: 'Superposé',
  modeOldShort: '1550',
  modeModShort: 'Aujourd’hui',
  orientOriginalShort: 'Tel qu’imprimé',
  sheetGrip: 'Afficher plus ou moins',
  sortLabel: 'Trier',
  sortDefault: 'Pertinence',
  loadError: 'Impossible de charger les données des lieux.',

  langLabel: 'Langue',
  colon: `${NB}: `,
  quote: (s: string) => `«${NB}${s}${NB}»`,

  partOf: (name: string) => (name.startsWith('Rue ') ? `partie de la rue ${name.slice(4)}` : `partie de ${name}`),
  and: ' et ',
  modernNames: {
    'Jussieu university campus': 'Campus universitaire de Jussieu',
  } as Record<string, string>,
  modernNotes: {
    'on its site': 'à son emplacement',
    'built on part of its site': 'sur une partie de son emplacement',
    'part of its site': 'sur une partie de son emplacement',
    'near the site': 'près de l’emplacement',
    'on its site; the Tour Clovis survives': `à son emplacement${NB}; la tour Clovis subsiste`,
    'its bell tower survives': 'son clocher subsiste',
    'its chapel survives': 'sa chapelle subsiste',
    'only the refectory survives': 'seul le réfectoire subsiste',
    'the Fontaine des Innocents survives': 'la fontaine des Innocents subsiste',
    'rebuilt north of the parvis 1867–1878': 'reconstruit au nord du parvis en 1867–1878',
    'rebuilt 1776, on the site': 'reconstruite en 1776, à l’emplacement',
    'the triumphal arch of 1674 stands near the site': 'l’arc de triomphe de 1674 se dresse près de l’emplacement',
    'the triumphal arch of 1672 stands near the site': 'l’arc de triomphe de 1672 se dresse près de l’emplacement',
    'the island was joined to the bank in 1843': 'l’île fut rattachée à la rive en 1843',
    "formerly quai de l'École": 'anciennement quai de l’École',
    '11th arrondissement': 'XIe arrondissement',
  } as Record<string, string>,
  compass: { N: 'N', S: 'S', E: 'E', W: 'O' } as Record<string, string>,
};

const sv: Strings = {
  siteName: 'Paris 1550',

  ogLocale: 'sv_SE',
  siteTitle: 'Paris 1550 · Truschet & Hoyaus karta och staden i dag',
  siteDesc: 'Alla platser som namnges på Truschet & Hoyaus karta över Paris från omkring 1550, återfunna på kartan och i dagens stad.',
  siteImageAlt: 'Île de la Cité och båda stränderna på Truschet & Hoyaus karta över Paris',
  placeLead: (old: string, status: string | null, modern: string | null) =>
    `”${old}” på Truschet & Hoyaus karta över Paris, ca 1550` +
    (status === 'standing' ? ': finns kvar' : status === 'rebuilt' ? ': återuppbyggd' : status === 'vanished' ? ': försvunnen'
      : status === 'renamed' ? `: har bytt namn${modern ? ` till ${modern}` : ''}` : '') + '.',
  placeImageAlt: (old: string) => `Namnet ”${old}” på kartan från 1550`,
  brandTitle: 'La Ville, Cité et Université de Paris',
  brandSub: 'Truschet & Hoyaus karta, med Paris i dag',
  brandHome: 'Tillbaka till början',

  viewMap: 'Karta',
  viewTable: 'Tabell över platser',

  searchPlaceholder: 'Sök…',
  searchLabel: 'Sök på gamla eller nutida namn',
  searchClear: 'Rensa sökningen',
  chipAll: 'Alla',
  chipUnsure: 'Osäker läsning',
  filters: 'Filter',
  filtersActive: (n: number) => `Filter · ${n}`,
  filtersTitle: 'Filtrera på typ eller läsning',
  count: (n: number, total: number) => (n === total ? `${total} platser` : `${n} av ${total} platser`),
  noResults: 'Inga platser hittades. Prova med färre bokstäver eller en annan stavning.',

  modeSide: 'Sida vid sida',
  modeOverlay: 'Överlägg',
  modeOld: 'Bara 1550',
  modeMod: 'Bara i dag',
  orientNorth: 'Norr uppåt',
  orientOriginal: 'Ursprunglig orientering',
  orientTitle: 'Orientering',
  tagOldNorth: 'Truschet & Hoyau, ca 1550 (vriden med norr uppåt)',
  tagOldOriginal: 'Truschet & Hoyau, ca 1550 (som tryckt, med öster uppåt)',
  tagMod: 'I dag: © OpenStreetMap-bidragsgivare',
  overlayOpacity: 'Gamla kartan',
  overlayOpacityUnit: 'opacitet',
  overlaySwipeHint: 'dra ⇆ för att jämföra',
  overlayLeft: '1550',
  overlayRight: 'I dag',
  overlayNoteWarped: (n: number | null, median: number | null) =>
    `Passningen är ungefärlig: den gamla kartan har böjts för att passa dagens gator${n ? ` med hjälp av ${n} kontrollpunkter` : ''}` +
    `${median ? ` (typiskt fel omkring ${roundTo(median, 10)} m)` : ''}. Den stämmer bäst i mitten och sämre mot kanterna.`,
  overlayNote: (n: number, rms: number) =>
    `Passningen är ungefärlig: den gamla kartan är placerad med en enkel anpassning till ${n} kontrollpunkter (typiskt fel omkring ${roundTo(rms, 10)} m).`,
  tilesMissing: 'Kartrutorna för den gamla kartan saknas. Kör scripts/make_old_tiles.py.',

  cardClose: 'Stäng',
  backToList: (n: number) => `← Tillbaka till ${n} ${n === 1 ? 'plats' : 'platser'}`,
  intro: 'Sök efter en plats, välj en i listan eller klicka på ett namn på någon av kartorna.',
  introNote: 'Alla namn som är tryckta på kartan från 1550 finns med. Identifieringar och beskrivningar håller fortfarande på att läggas till och kontrolleras.',
  notIdentified: 'Ännu inte identifierad',
  noLongerExists: 'Finns inte längre',
  formerSite: 'tidigare läge',
  pinTags: {
    approx: 'ungefärligt',
    uncertain: 'osäkert',
    unassessed: '',
    estimated: 'uppskattat',
    exact: '',
  } as Record<string, string>,
  today: 'I dag',
  noSummary: 'Ingen beskrivning ännu.',
  noSources: 'Inga källor ännu.',
  sources: 'Källor',
  onMapAs: 'På kartan',
  transcription: 'Anteckning om läsningen',
  reading: 'Läsning',
  readingOk: 'Säker',
  readingUnsure: 'Osäker: namnet är svårläst',
  variants: 'Stavningar',
  noVariants: 'Inga noterade ännu',
  pos1550: 'Läge (1550)',
  posToday: 'Läge i dag',
  pxFmt: (x: number, y: number) => `x ${Math.round(x)}, y ${Math.round(y)} px på skanningen`,
  estimated: 'Läget är uppskattat utifrån kartan',
  estimatedHow: (n: number, rms: number) =>
    `Beräknat från ${n} kontrollpunkter; typiskt fel omkring ${roundTo(rms, 10)} m.`,
  confidence: 'noggrannhet',
  confidenceUnknown: 'noggrannheten är ännu inte bedömd',
  confidenceLabels: { exact: 'exakt', approx: 'ungefärlig', uncertain: 'osäker' } as Record<string, string>,
  link: 'Länk till platsen',
  id: 'Id',
  cropCaption: 'Som det står tryckt på kartan från 1550 (öster uppåt)',
  unsureBadge: 'Osäker läsning',

  // Common gender, agreeing with "plats".
  statusLabels: {
    standing: 'Finns kvar',
    rebuilt: 'Återuppbyggd',
    renamed: 'Nytt namn',
    vanished: 'Försvunnen',
  } as Record<string, string>,
  statusUnknown: 'Ännu inte utrett',

  typeLabels: {
    street: 'Gata',
    church_religious: 'Kyrka eller kloster',
    college: 'Kollegium',
    building: 'Byggnad',
    gate_wall: 'Port eller stadsmur',
    bridge: 'Bro',
    square_market: 'Torg eller marknad',
    village_faubourg: 'By eller förstad',
    other: 'Övrigt',
  } as Record<string, string>,
  typeChips: {
    church_religious: 'Kyrkor',
    college: 'Kollegier',
    street: 'Gator',
    gate_wall: 'Portar och murar',
    bridge: 'Broar',
    building: 'Byggnader',
    square_market: 'Torg och marknader',
    village_faubourg: 'Byar',
    other: 'Övrigt',
  } as Record<string, string>,

  colId: 'Id',
  colOld: 'På kartan (1550)',
  colModern: 'I dag',
  colType: 'Typ',
  colStatus: 'Status',
  colReading: 'Läsning',
  tableHint: 'Klicka på en rad för att visa platsen på kartan.',

  creditMap: 'Karta: Truschet & Hoyau, ca 1550, Basels universitetsbibliotek (fri från upphovsrätt)',
  creditOsm: '© OpenStreetMap-bidragsgivare',
  creditBy: 'av Peer Blekelj, byggd med Claude Code',
  creditMethod: 'Hur kartan böjdes',
  creditTexts: 'Texterna på kartan',
  creditAbout: 'Om kartan (på engelska)',
  welcomeTitle: 'Ny här?',
  welcomeText: 'Vem som gjorde den här kartan över Paris runt 1550, hur den dateras och hur det enda exemplaret dök upp i Basel.',
  welcomeLink: 'Läs om kartan (på engelska) →',
  welcomeDismiss: 'Stäng',
  oldAttribution: 'Truschet &amp; Hoyau, ca 1550 · Basels universitetsbibliotek (fri från upphovsrätt)',

  suggestCorrection: 'Föreslå en rättelse',
  suggestCorrectionHint: 'Öppnar ett ifyllt ärende på GitHub (kräver ett GitHub-konto)',
  viewTableShort: 'Tabell',
  modeSideShort: 'Båda',
  modeOverlayShort: 'Överlagrad',
  modeOldShort: '1550',
  modeModShort: 'I dag',
  orientOriginalShort: 'Som tryckt',
  sheetGrip: 'Visa mer eller mindre',
  sortLabel: 'Sortera',
  sortDefault: 'Bästa träff',
  loadError: 'Kunde inte läsa in platsdata.',

  langLabel: 'Språk',
  colon: ': ',
  quote: (s: string) => `”${s}”`,

  partOf: (name: string) => `del av ${name.startsWith('Rue ') ? `rue ${name.slice(4)}` : name}`,
  and: ' och ',
  modernNames: {
    'Jussieu university campus': 'Universitetsområdet Jussieu',
  } as Record<string, string>,
  modernNotes: {
    'on its site': 'på platsen',
    'built on part of its site': 'anlagd på en del av platsen',
    'part of its site': 'på en del av platsen',
    'near the site': 'nära platsen',
    'on its site; the Tour Clovis survives': 'på platsen; Tour Clovis finns kvar',
    'its bell tower survives': 'klocktornet finns kvar',
    'its chapel survives': 'kapellet finns kvar',
    'only the refectory survives': 'bara refektoriet finns kvar',
    'the Fontaine des Innocents survives': 'Fontaine des Innocents finns kvar',
    'rebuilt north of the parvis 1867–1878': 'återuppbyggt norr om parvisen 1867–1878',
    'rebuilt 1776, on the site': 'återuppbyggd 1776, på platsen',
    'the triumphal arch of 1674 stands near the site': 'triumfbågen från 1674 står nära platsen',
    'the triumphal arch of 1672 stands near the site': 'triumfbågen från 1672 står nära platsen',
    'the island was joined to the bank in 1843': 'ön förenades med stranden 1843',
    "formerly quai de l'École": "tidigare quai de l'École",
    '11th arrondissement': '11:e arrondissementet',
  } as Record<string, string>,
  compass: { N: 'N', S: 'S', E: 'Ö', W: 'V' } as Record<string, string>,
};

export const LANGS = ['en', 'fr', 'sv'] as const;
export type Lang = (typeof LANGS)[number];
export const STRINGS: Record<Lang, Strings> = { en, fr, sv };

export const isLang = (v: unknown): v is Lang => typeof v === 'string' && (LANGS as readonly string[]).includes(v);

/** The modern name in language `s`. The names are French already; what is translated is the
 *  English around them: "part of …", " and ", and a trailing note in parentheses. */
export function localModernIn(m: string, s: Strings): string {
  if (s === en) return m;
  const paren = / \(([^()]*)\)$/.exec(m);
  let name = paren ? m.slice(0, paren.index) : m;
  const part = /^part of (.+)$/.exec(name);
  name = part ? s.partOf(part[1]) : s.modernNames[name] ?? name.replace(/ and /g, s.and);
  return paren ? `${name} (${s.modernNotes[paren[1]] ?? paren[1]})` : name;
}

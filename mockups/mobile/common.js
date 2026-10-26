// Shared bits for the phone mockups: a few real places and helpers that draw the real components.
const PLACES = [
  ['L0006', 'Le Pont S. Michel', 'Pont Saint-Michel', 'rebuilt', ''],
  ['L0002', 'Le Pont Nostre Dame', 'Pont Notre-Dame', 'rebuilt', ''],
  ['L0003', 'Petit Pont', 'Petit-Pont', 'rebuilt', ''],
  ['L0004', 'Le Pont au Change', 'Pont au Change', 'rebuilt', ''],
  ['L0005', 'Le Pont au Muniers', null, 'vanished', 'vanished'],
  ['L0007', 'Le Pont Arcans', null, 'vanished', 'vanished'],
  ['L0001', 'Le Pont de Chalanton', 'Pont de Charenton', 'rebuilt', ''],
  ['L0008', 'Les Tournelles', 'Place des Vosges', 'vanished', 'vanished'],
];
const STATUS = { rebuilt: 'Rebuilt', vanished: 'Vanished', standing: 'Still standing', renamed: 'Renamed' };
function results(n, sel) {
  return PLACES.slice(0, n).map(([id, o, m, s, cls], i) =>
    `<div class="result${i === sel ? ' sel' : ''}"><span class="dot ${cls}"></span><span class="old">${o}</span>` +
    `<span class="mod"><span class="${m ? '' : 'placeholder'}">${m ?? 'No longer exists'}</span> · ${STATUS[s].toLowerCase()}</span></div>`).join('');
}
function card() {
  return `<article class="card">
    <button class="card-back" type="button">← Back to 17 places</button>
    <button class="card-close" type="button">×</button>
    <div class="kicker">Bridge <span class="badge rebuilt">Rebuilt</span></div>
    <h2>Le Pont S. Michel</h2>
    <div class="modname">Today: <span>Pont Saint-Michel</span></div>
    <figure class="snip"><div class="crop"></div><figcaption>As printed on the 1550 map (east at top)</figcaption></figure>
    <dl>
      <dt>On the map as</dt><dd>“LE PONT S. MICHEL”</dd>
      <dt>Transcription note</dt><dd>rebuilt 1857</dd>
      <dt>Reading</dt><dd>Clear</dd>
      <dt>Spelling variants</dt><dd>Pont Saint-Michel</dd>
      <dt>Position today</dt><dd>48.8542° N, 2.3447° E<small>confidence: exact</small></dd>
      <dt>Id</dt><dd><a href="#">L0006</a> · <span class="muted">Link to this place</span></dd>
    </dl>
    <p class="summary">Links the Left Bank (place Saint-Michel) to the Île de la Cité. The bridge on the map was lined with houses; the present bridge was built in 1857.</p>
    <div class="src">Sources: <a href="#">Wikipédia (fr)</a> · <a href="#">Wikipedia (en)</a> · <a href="#">Wikidata</a> · <a href="#">Cousin 1875, p. 66</a></div>
  </article>`;
}
const SEARCH_ICON = '<svg viewBox="0 0 20 20" width="17" height="17"><circle cx="8.5" cy="8.5" r="5.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M13 13l4.5 4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>';
// An old-map pane centred on the Pont Saint-Michel (scan at 2× the overview).
function oldPane(style, h) { return `<div class="omap" style="${style};background-position:${195 - 2780}px ${h / 2 - 1590}px"></div>`; }
function modPane(style, h) { return `<div class="mmap" style="${style};background-position:-215px ${h / 2 - 390}px"></div>`; }
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-fill]').forEach((el) => { el.innerHTML = eval(el.dataset.fill); });
  document.querySelectorAll('i.ico').forEach((el) => { el.outerHTML = SEARCH_ICON; });
});
// The card as a page of its own (B): the page header has Back and the map strip shows the place.
function cardPage() { return card().replace('<figure', '<figure hidden').replace('<button class="card-back"', '<button hidden class="card-back"').replace('<button class="card-close"', '<button hidden class="card-close"'); }

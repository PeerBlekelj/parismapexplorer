// Result rows for the mockups: [old label, today, second line, status class, star state]
function rows(list) {
  return list.map(([old, mod, second, st, star]) => {
    const starCls = star === 'on' ? 'star on' : star === 'shared' ? 'star shared-only' : 'star';
    const glyph = star === 'on' ? '★' : '☆';
    const modCls = mod ? '' : ' class="placeholder"';
    const modTxt = mod || 'No longer exists';
    return `<div class="result">` +
      `<span class="dot ${st}"></span>` +
      `<span class="old">${old}</span>` +
      `<button type="button" class="${starCls}" title="Starred">${glyph}</button>` +
      `<span class="mod"><span${modCls}>${modTxt}</span> · ${second}</span>` +
      `</div>`;
  }).join('');
}
// The seven starred places used throughout (real records from data/places.json).
const SEVEN = [
  ['Le Pont S. Michel', 'Pont Saint-Michel', 'rebuilt', 'rebuilt'],
  ['Le Pont Nostre Dame', 'Pont Notre-Dame', 'rebuilt', 'rebuilt'],
  ['Lostel de la Vile', 'Hôtel de Ville', 'rebuilt', 'rebuilt'],
  ['Petit Chatelet', null, 'vanished', 'vanished'],
  ['La Monnoie', null, 'vanished', 'vanished'],
  ['Lostel Dieu', 'Hôtel-Dieu', 'rebuilt', 'rebuilt'],
  ['S. Germain de Locerras', 'Église Saint-Germain-l’Auxerrois', 'standing', 'standing'],
];
const UNSTARRED = [
  ['Le Petit Pont', 'Petit-Pont', 'rebuilt', 'rebuilt'],
  ['Le Pont au Change', 'Pont au Change', 'rebuilt', 'rebuilt'],
  ['Le Palais', 'Palais de la Cité', 'rebuilt', 'rebuilt'],
];
const sev = (star) => SEVEN.map((r) => [r[0], r[1], r[2], r[3], star]);

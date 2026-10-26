// The info card for the selected place. Null handling follows DATA_CONTRACT.md: a null field is
// "not researched yet" and is shown with a neutral placeholder, never as absent or negative.

import { drawCrop } from './crop';
import { esc, fmtLat, fmtLon, safeUrl, statusClass, statusLabel, typeLabel } from './format';
import { t } from './i18n';
import { modernText, type Entry } from './model';
import type { PixelGeoTransform } from './transform';

// `backCount` is the number of places in the list the card was opened over; the back link and
// the × both call `onClose`, which returns to that list.
export function renderCard(el: HTMLElement, e: Entry, T: PixelGeoTransform, backCount: number, onClose: () => void): void {
  const p = e.place;
  const m = modernText(p);
  const unsure = p.flag === 'unsure';
  const gone = p.status === 'vanished';

  let posToday: string;
  if (e.geoKind === 'estimated') {
    posToday =
      `≈ ${fmtLat(e.geo[1], 3)}, ${fmtLon(e.geo[0], 3)}` +
      `<span class="est-note">${esc(t.estimated)}</span>` +
      `<small>${esc(t.estimatedHow(T.n, T.errorMeters))}</small>`;
  } else {
    const conf = e.geoKind === 'unassessed' ? t.confidenceUnknown : `${t.confidence}: ${t.confidenceLabels[e.geoKind] ?? e.geoKind}`;
    posToday = `${fmtLat(e.geo[1], 4)}, ${fmtLon(e.geo[0], 4)}<small>${esc(conf)}${gone ? ` · ${esc(t.formerSite)}` : ''}</small>`;
  }

  const variants = p.variants.length
    ? p.variants.map(esc).join(', ')
    : `<span class="placeholder">${esc(t.noVariants)}</span>`;

  const links = p.sources
    .map((s) => {
      const url = safeUrl(s.url);
      const label = esc(s.label || s.url);
      return url ? `<a href="${esc(url)}" target="_blank" rel="noopener">${label}</a>` : label;
    })
    .join(' · ');

  const orient = p.orient === 'v' ? 'v' : p.orient === 'd' ? 'd' : 'h';

  el.innerHTML = `
    <article class="card">
      <button class="card-back" type="button">${esc(t.backToList(backCount))}</button>
      <button class="card-close" type="button" aria-label="${esc(t.cardClose)}" title="${esc(t.cardClose)}">×</button>
      <div class="kicker">${esc(typeLabel(p.type))}
        <span class="badge ${statusClass(p.status)}">${esc(statusLabel(p.status))}</span>
        ${unsure ? `<span class="badge unsure">${esc(t.unsureBadge)}</span>` : ''}
      </div>
      <h2>${esc(e.title)}</h2>
      <div class="modname">${esc(t.today)}: <span class="${m.placeholder ? 'placeholder' : ''}">${esc(m.text)}</span></div>
      <figure class="snip snip-${orient}">
        <canvas aria-label="${esc(t.cropCaption)}"></canvas>
        <figcaption>${esc(t.cropCaption)}</figcaption>
      </figure>
      <dl>
        <dt>${esc(t.onMapAs)}</dt><dd>“${esc(p.old)}”</dd>
        ${p.note ? `<dt>${esc(t.transcription)}</dt><dd>${esc(p.note)}</dd>` : ''}
        <dt>${esc(t.reading)}</dt><dd>${esc(unsure ? t.readingUnsure : t.readingOk)}</dd>
        <dt>${esc(t.variants)}</dt><dd>${variants}</dd>
        <dt>${esc(t.pos1550)}</dt><dd>${esc(t.pxFmt(e.px[0], e.px[1]))}</dd>
        <dt>${esc(t.posToday)}</dt><dd class="pos">${posToday}</dd>
        <dt>${esc(t.id)}</dt><dd><a href="${import.meta.env.BASE_URL}place/${encodeURIComponent(p.id)}/" class="permalink">${esc(p.id)}</a> · <span class="muted">${esc(t.link)}</span></dd>
      </dl>
      ${p.summary ? `<p class="summary">${esc(p.summary)}</p>` : `<p class="summary placeholder">${esc(t.noSummary)}</p>`}
      <div class="src">${esc(t.sources)}: ${links || `<span class="placeholder">${esc(t.noSources)}</span>`}</div>
    </article>`;

  el.querySelector('.card-close')?.addEventListener('click', onClose);
  el.querySelector('.card-back')?.addEventListener('click', onClose);
  // The address bar already shows this link; a plain click shouldn't reload the app.
  el.querySelector('.permalink')?.addEventListener('click', (ev) => ev.preventDefault());
  el.scrollTop = 0;

  const fig = el.querySelector('figure') as HTMLElement;
  const canvas = el.querySelector('canvas') as HTMLCanvasElement;
  const w = Math.min(440, Math.max(200, Math.floor(fig.clientWidth || 340)));
  const h = orient === 'h' ? Math.round(w * 0.55) : orient === 'v' ? Math.round(w * 0.85) : Math.round(w * 0.7);
  const scale = orient === 'h' ? 2.2 : 2.4;
  void drawCrop(canvas, e.px, w, h, scale);
}

export function renderIntro(el: HTMLElement): void {
  el.innerHTML = `
    <div class="intro">
      <p>${esc(t.intro)}</p>
      <p class="muted">${esc(t.introNote)}</p>
    </div>`;
}

import '@fontsource/eb-garamond/latin-400.css';
import '@fontsource/eb-garamond/latin-500.css';
import '@fontsource/eb-garamond/latin-400-italic.css';
import '@fontsource/inter/latin-400.css';
import '@fontsource/inter/latin-500.css';
import '@fontsource/inter/latin-600.css';
import './style.css';

import { renderCard, renderIntro } from './card';
import { esc, statusClass, statusLabel, typeLabel } from './format';
import { lang, langBase, LANGS, setLang, t, type Lang } from './i18n';
import { loadOverlayTiles, MapView, type Mode, type Orientation } from './maps';
import { initMobile } from './mobile';
import { renderWelcome } from './welcome';
import { buildEntries, modernText, type Entry } from './model';
import { IMAGE_H, IMAGE_W } from './oldPlane';
import { SearchIndex } from './search';
import { PlaceTable } from './table';
import { createTransform } from './transform';
import type { GcpsFile, PlacesFile } from './types';

const BASE = import.meta.env.BASE_URL;
const TYPE_ORDER = ['church_religious', 'college', 'street', 'gate_wall', 'bridge', 'building', 'square_market', 'village_faubourg', 'other'];

const $ = <T extends HTMLElement = HTMLElement>(sel: string) => document.querySelector(sel) as T;

async function loadJson<T>(path: string): Promise<T> {
  const r = await fetch(`${BASE}${path}`, { cache: 'no-cache' });
  if (!r.ok) throw new Error(`${path}: HTTP ${r.status}`);
  return (await r.json()) as T;
}

// A place link is /place/L0123/ or /fr/place/L0123/ (a real page, so link previews work); the
// older #place= form still opens.
function placeIdFromUrl(): string | null {
  const m = /\/place\/([A-Za-z0-9_-]+)\/?$/.exec(location.pathname) ?? /(?:^#|&)place=([A-Za-z0-9_-]+)/.exec(location.hash);
  return m ? m[1] : null;
}

/** The start page, keeping ?lang= if the address has it. */
function homeUrl(): string {
  const l = new URLSearchParams(location.search).get('lang');
  return `${langBase()}${l ? `?lang=${encodeURIComponent(l)}` : ''}`;
}

function fillStaticText(): void {
  $('#brand-title').textContent = t.brandTitle;
  $('#brand-sub').textContent = `${t.siteName} · ${t.brandSub}`;
  $('#brand').title = t.brandHome;
  $('#brand').setAttribute('aria-label', `${t.brandTitle}. ${t.brandHome}`);
  $<HTMLAnchorElement>('#brand').href = homeUrl();
  renderWelcome($('#welcome'));
  $('.viewtabs [data-view=map]').textContent = t.viewMap;
  $('.viewtabs [data-view=table]').textContent = t.viewTable;
  $<HTMLInputElement>('#q').placeholder = t.searchPlaceholder;
  $('#q').title = t.searchLabel;
  $('#q').setAttribute('aria-label', t.searchLabel);
  $('#q-clear').title = t.searchClear;
  $('#q-clear').setAttribute('aria-label', t.searchClear);
  $('#filters-btn').title = t.filtersTitle;
  const modes: Record<string, string> = { side: t.modeSide, overlay: t.modeOverlay, old: t.modeOld, mod: t.modeMod };
  document.querySelectorAll<HTMLButtonElement>('#modes button').forEach((b) => (b.textContent = modes[b.dataset.m ?? ''] ?? ''));
  $('#orient .lbl').textContent = t.orientOriginal;
  $('#tag-mod').textContent = t.tagMod;
  $('#op-label').textContent = t.overlayOpacity;
  $('#op-unit').textContent = t.overlayOpacityUnit;
  $('#swipe-hint').textContent = t.overlaySwipeHint;
  $('.swipe-l').textContent = t.overlayLeft;
  $('.swipe-r').textContent = t.overlayRight;
  const langs = LANGS.map((l) =>
    `<button type="button" data-lang="${l}" lang="${l}" aria-pressed="${l === lang}">${l.toUpperCase()}</button>`).join(' · ');
  $('#credits').innerHTML = `<span class="langs" role="group" aria-label="${esc(t.langLabel)}">${langs}</span>` +
    `<a href="${langBase()}about/">${esc(t.creditAbout)}</a> · <a href="${langBase()}method/">${esc(t.creditMethod)}</a> · ` +
    `<a href="${langBase()}texts/">${esc(t.creditTexts)}</a> · ` + [t.creditMap, t.creditOsm, t.creditBy].map(esc).join(' · ');
}

// Re-renders everything that shows text; replaced by the full version once the data is loaded.
let rerender = (): void => {
  fillStaticText();
  renderIntro($('#card'));
};

$('#credits').addEventListener('click', (ev) => {
  const b = (ev.target as HTMLElement).closest('button[data-lang]') as HTMLButtonElement | null;
  const l = b?.dataset.lang as Lang | undefined;
  if (!l || l === lang) return;
  setLang(l);
  rerender();
});

async function main(): Promise<void> {
  fillStaticText();
  renderIntro($('#card'));

  let placesFile: PlacesFile, gcpsFile: GcpsFile;
  const overlayTilesP = loadOverlayTiles();
  try {
    [placesFile, gcpsFile] = await Promise.all([
      loadJson<PlacesFile>('data/places.json'),
      loadJson<GcpsFile>('data/gcps.json'),
    ]);
  } catch (err) {
    console.error(err);
    $('#card').innerHTML = `<div class="intro"><p>${esc(t.loadError)}</p></div>`;
    return;
  }
  if (placesFile.image && (placesFile.image.width !== IMAGE_W || placesFile.image.height !== IMAGE_H)) {
    console.warn('places.json image size differs from the tiled image', placesFile.image);
  }

  const T = createTransform(gcpsFile.gcps ?? []);
  const entries = buildEntries(placesFile.places ?? [], T);
  const byId = new Map(entries.map((e) => [e.place.id, e]));
  const index = new SearchIndex(entries.map((e) => e.place));
  const total = entries.length;

  // ---------- state ----------
  const state = {
    query: '',
    types: new Set<string>(),
    unsure: false,
    selected: null as Entry | null,
    lastSelected: null as Entry | null, // stays highlighted in the list after Back
    listScroll: 0,                      // list scroll position when the card opened
    view: 'map' as 'map' | 'table',
    mode: 'side' as Mode,
    orientation: 'north' as Orientation,
    results: entries as Entry[],
  };
  const app = $('.app');
  const mapArea = $('#map-area');
  const listEl = $('#list');
  const cardEl = $('#card');

  const initial = byId.get(placeIdFromUrl() ?? '') ?? null;
  const overlayTiles = await overlayTilesP;
  const maps = new MapView(
    { old: $('#map-old'), mod: $('#map-mod'), ovl: $('#map-ovl'), tooltip: $('#tooltip') },
    T, entries,
    { onPick: (id, source) => select(id, { fly: false, source }) },
    initial,
    overlayTiles,
  );
  // Expose for debugging in the console and for the screenshot script.
  (window as unknown as { pme: unknown }).pme = { maps, T, entries };

  const table = new PlaceTable($('#table'), (id) => select(id, { fly: true, fromTable: true }));
  const mobile = initMobile({ back: () => closeCard(true), resize: () => maps.resize() });
  mobile.foldAttribution([maps.old, maps.mod]);

  // ---------- chips ----------
  const counts = new Map<string, number>();
  for (const e of entries) counts.set(e.place.type, (counts.get(e.place.type) ?? 0) + 1);
  const unsureCount = entries.filter((e) => e.place.flag === 'unsure').length;
  const chipTypes = TYPE_ORDER.filter((k) => counts.has(k));
  for (const k of counts.keys()) if (!chipTypes.includes(k)) chipTypes.push(k);
  const chipsEl = $('#chips');
  function renderChips(): void {
    chipsEl.innerHTML =
      `<button type="button" class="chip" data-chip="all">${esc(t.chipAll)}</button>` +
      chipTypes.map((k) => `<button type="button" class="chip" data-chip="type" data-type="${esc(k)}">${esc(t.typeChips[k] ?? typeLabel(k))} <span class="n">${counts.get(k)}</span></button>`).join('') +
      (unsureCount ? `<button type="button" class="chip chip-unsure" data-chip="unsure">${esc(t.chipUnsure)} <span class="n">${unsureCount}</span></button>` : '');
    markChips();
  }
  function markChips(): void {
    chipsEl.querySelectorAll<HTMLButtonElement>('button.chip').forEach((c) => {
      const on = c.dataset.chip === 'all' ? state.types.size === 0
        : c.dataset.chip === 'type' ? state.types.has(c.dataset.type ?? '')
        : state.unsure;
      c.classList.toggle('on', on);
    });
  }
  renderChips();
  chipsEl.addEventListener('click', (ev) => {
    const b = (ev.target as HTMLElement).closest('button.chip') as HTMLButtonElement | null;
    if (!b) return;
    if (b.dataset.chip === 'all') state.types.clear();
    else if (b.dataset.chip === 'type') {
      const k = b.dataset.type ?? '';
      if (state.types.has(k)) state.types.delete(k);
      else state.types.add(k);
    } else if (b.dataset.chip === 'unsure') state.unsure = !state.unsure;
    markChips();
    updateFiltersBtn();
    if (state.selected) closeCard(false);
    refresh();
  });

  // ---------- filters menu ----------
  const filtersBtn = $<HTMLButtonElement>('#filters-btn');
  const filtersEl = $('#filters');
  function updateFiltersBtn(): void {
    const n = state.types.size + (state.unsure ? 1 : 0);
    filtersBtn.innerHTML = `${esc(n ? t.filtersActive(n) : t.filters)} <span class="caret" aria-hidden="true">▾</span>`;
    filtersBtn.classList.toggle('active', n > 0);
  }
  let filtersOpen = false;
  function setFiltersOpen(open: boolean): void {
    filtersOpen = open;
    filtersEl.hidden = !open;
    filtersBtn.setAttribute('aria-expanded', String(open));
    filtersBtn.classList.toggle('open', open);
  }
  filtersBtn.addEventListener('click', () => setFiltersOpen(!filtersOpen));
  document.addEventListener('pointerdown', (ev) => {
    const target = ev.target as Node;
    if (filtersOpen && !filtersEl.contains(target) && !filtersBtn.contains(target)) setFiltersOpen(false);
  });
  updateFiltersBtn();

  // ---------- results ----------
  function filterActive(): boolean {
    return !!state.query.trim() || state.types.size > 0 || state.unsure;
  }

  function resultHtml(e: Entry): string {
    const p = e.place;
    const m = modernText(p);
    const second = p.status ? statusLabel(p.status).toLowerCase() : typeLabel(p.type);
    return `<div class="result${(state.selected ?? state.lastSelected) === e ? ' sel' : ''}" data-id="${esc(p.id)}" role="option">` +
      `<span class="dot ${statusClass(p.status)}"></span>` +
      `<span class="old">${esc(e.title)}${p.flag === 'unsure' ? ' <span class="q" title="' + esc(t.unsureBadge) + '">?</span>' : ''}</span>` +
      `<span class="mod"><span class="${m.placeholder ? 'placeholder' : ''}">${esc(m.text)}</span> · ${esc(second)}</span></div>`;
  }

  /** `keepScroll`: same results, new language; leave the list where it is. */
  function refresh(keepScroll = false): void {
    const filter = (p: Entry['place']) =>
      (state.types.size === 0 || state.types.has(p.type)) && (!state.unsure || p.flag === 'unsure');
    state.results = index.search(state.query, filter).map((r) => byId.get(r.place.id) as Entry);
    const countText = t.count(state.results.length, total);
    $('#count').textContent = countText;
    listEl.innerHTML = state.results.length
      ? state.results.map(resultHtml).join('')
      : `<p class="empty">${esc(t.noResults)}</p>`;
    if (!keepScroll) listEl.scrollTop = 0;
    maps.setFilter(state.results, filterActive());
    if (state.view === 'table') table.update(state.results, state.selected?.place.id ?? null, countText);
  }

  listEl.addEventListener('click', (ev) => {
    const r = (ev.target as HTMLElement).closest('.result') as HTMLElement | null;
    if (r?.dataset.id) select(r.dataset.id, { fly: true });
  });

  // ---------- search box ----------
  const q = $<HTMLInputElement>('#q');
  let timer = 0;
  q.addEventListener('input', () => {
    $('#q-clear').hidden = !q.value;
    clearTimeout(timer);
    timer = window.setTimeout(() => {
      if (q.value === state.query) return;
      state.query = q.value;
      if (state.selected) closeCard(false);
      refresh();
    }, 70);
  });
  q.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter') {
      clearTimeout(timer);
      if (q.value !== state.query) {
        state.query = q.value;
        refresh();
      }
      if (state.results[0]) select(state.results[0].place.id, { fly: true });
    } else if (ev.key === 'Escape' && q.value) {
      // With text in the box, Esc clears it; with an empty box it falls through to the
      // document handler (close the filters menu or the card).
      ev.stopPropagation();
      q.value = '';
      q.dispatchEvent(new Event('input'));
    }
  });
  $('#q-clear').addEventListener('click', () => {
    q.value = '';
    q.dispatchEvent(new Event('input'));
    q.focus();
  });

  // ---------- selection ----------
  // A selected place opens as a card that replaces the list (drill-in); Back, × and Esc
  // return to the list, scrolled to where it was, with the place still highlighted.
  function select(id: string | null, opts: { fly: boolean; source?: 'old' | 'mod'; fromTable?: boolean; instant?: boolean }): void {
    const e = id ? byId.get(id) ?? null : null;
    const wasOpen = !!state.selected;
    if (e && !state.selected) state.listScroll = listEl.scrollTop;
    state.selected = e;
    if (e) state.lastSelected = e;
    if (opts.fromTable) setView('map');
    listEl.querySelectorAll('.result.sel').forEach((n) => n.classList.remove('sel'));
    const item = state.lastSelected
      ? listEl.querySelector(`.result[data-id="${CSS.escape(state.lastSelected.place.id)}"]`)
      : null;
    item?.classList.add('sel');
    app.classList.toggle('has-sel', !!e);
    if (e) {
      renderCard(cardEl, e, T, state.results.length, () => closeCard(true));
      if (!wasOpen) mobile.cardOpened();
      history.replaceState(null, '', `${langBase()}place/${encodeURIComponent(e.place.id)}/${location.search}`);
      document.title = `${e.place.modern ?? e.place.old} · Paris 1550`;
    } else {
      renderIntro(cardEl);
      history.replaceState(null, '', `${langBase()}${location.search}`);
      if (wasOpen) mobile.cardClosed();
      document.title = t.siteTitle;
    }
    maps.select(e, opts);
    if (state.view === 'table') table.update(state.results, e?.place.id ?? null, t.count(state.results.length, total));
  }

  /** Back to the list. `restore` puts the list back where it was (false when the results are
   *  about to change anyway, e.g. a new search). */
  function closeCard(restore: boolean): void {
    select(null, { fly: false });
    if (!restore) return;
    listEl.scrollTop = state.listScroll;
    const item = listEl.querySelector<HTMLElement>('.result.sel');
    if (item) {
      // Opened from the map or a link: the row may be outside the remembered view.
      const lr = listEl.getBoundingClientRect(), ir = item.getBoundingClientRect();
      if (ir.top < lr.top || ir.bottom > lr.bottom) item.scrollIntoView({ block: 'center' });
    }
  }

  document.addEventListener('keydown', (ev) => {
    if (ev.key !== 'Escape' || ev.defaultPrevented) return;
    if (filtersOpen) {
      setFiltersOpen(false);
      filtersBtn.focus();
    } else if (state.selected) {
      closeCard(true);
    }
  });

  window.addEventListener('hashchange', () => {
    const id = placeIdFromUrl();
    if (id && id !== state.selected?.place.id && byId.has(id)) select(id, { fly: true });
  });

  // ---------- views ----------
  function setView(view: 'map' | 'table'): void {
    if (state.view === view) return;
    state.view = view;
    app.dataset.view = view;
    document.querySelectorAll<HTMLButtonElement>('.viewtabs button').forEach((b) => {
      const on = b.dataset.view === view;
      b.classList.toggle('on', on);
      b.setAttribute('aria-selected', String(on));
    });
    if (view === 'table') table.update(state.results, state.selected?.place.id ?? null, t.count(state.results.length, total));
    else maps.resize();
  }
  document.querySelectorAll<HTMLButtonElement>('.viewtabs button').forEach((b) =>
    b.addEventListener('click', () => setView(b.dataset.view as 'map' | 'table')));

  // ---------- modes / orientation ----------
  function updateTags(): void {
    $('#tag-old').textContent = state.orientation === 'north' ? t.tagOldNorth : t.tagOldOriginal;
  }
  function setMode(mode: Mode): void {
    if (mode === state.mode) return;
    state.mode = mode;
    mapArea.dataset.mode = mode;
    document.querySelectorAll<HTMLButtonElement>('#modes button').forEach((x) => x.classList.toggle('on', x.dataset.m === mode));
    maps.setMode(mode);
  }
  document.querySelectorAll<HTMLButtonElement>('#modes button').forEach((b) =>
    b.addEventListener('click', () => setMode(b.dataset.m as Mode)));
  const orientBtn = $('#orient');
  orientBtn.title = t.orientTitle;
  function markOrientation(): void {
    orientBtn.setAttribute('aria-pressed', String(state.orientation === 'original'));
    updateTags();
  }
  orientBtn.addEventListener('click', () => {
    state.orientation = state.orientation === 'north' ? 'original' : 'north';
    markOrientation();
    maps.setOrientation(state.orientation);
  });
  updateTags();

  // ---------- start over ----------
  // The title returns to the standard view: list, no search or filters, side by side, north up,
  // the whole city, the address back to / (keeping ?lang=). A modified click (new tab) is left alone.
  function startOver(): void {
    setFiltersOpen(false);
    q.value = '';
    $('#q-clear').hidden = true;
    clearTimeout(timer);
    state.query = '';
    state.types.clear();
    state.unsure = false;
    markChips();
    updateFiltersBtn();
    setView('map');
    mobile.home(); // first: the sheet sets the map's size, and the camera fits that size
    setMode('side');
    state.orientation = 'north';
    markOrientation();
    if (state.selected) select(null, { fly: false });
    state.lastSelected = null;
    state.listScroll = 0;
    refresh();
    maps.home();
    history.replaceState(null, '', homeUrl());
    document.title = t.siteTitle;
  }
  $('#brand').addEventListener('click', (ev) => {
    if (ev.button !== 0 || ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey) return;
    ev.preventDefault();
    startOver();
  });

  // ---------- overlay controls ----------
  $('#warn').textContent = overlayTiles
    ? t.overlayNoteWarped(overlayTiles.controlPoints, overlayTiles.medianErrorM)
    : t.overlayNote(T.n, T.affineErrorMeters);
  const op = $<HTMLInputElement>('#op');
  op.addEventListener('input', () => maps.setOpacity(Number(op.value) / 100));
  const swipe = $('#swipe');
  const modPane = $('.modp');
  let dragging = false;
  const setSwipe = (pct: number) => {
    swipe.style.left = `${pct}%`;
    maps.setSwipe(pct);
  };
  swipe.addEventListener('pointerdown', (ev) => {
    dragging = true;
    swipe.setPointerCapture(ev.pointerId);
    ev.preventDefault();
  });
  swipe.addEventListener('pointermove', (ev) => {
    if (!dragging) return;
    const r = modPane.getBoundingClientRect();
    setSwipe(Math.max(0, Math.min(100, ((ev.clientX - r.left) / r.width) * 100)));
  });
  const endDrag = () => (dragging = false);
  swipe.addEventListener('pointerup', endDrag);
  swipe.addEventListener('pointercancel', endDrag);
  setSwipe(50);

  // ---------- language ----------
  // Text only: the selection, list scroll, card scroll and map cameras stay as they are.
  rerender = () => {
    fillStaticText();
    renderChips();
    updateFiltersBtn();
    const listScroll = listEl.scrollTop;
    refresh(true);
    listEl.scrollTop = listScroll;
    const e = state.selected;
    if (e) {
      const cardScroll = cardEl.scrollTop;
      renderCard(cardEl, e, T, state.results.length, () => closeCard(true));
      cardEl.scrollTop = cardScroll;
    } else {
      renderIntro(cardEl);
      document.title = t.siteTitle;
    }
    orientBtn.title = t.orientTitle;
    updateTags();
    $('#warn').textContent = overlayTiles
      ? t.overlayNoteWarped(overlayTiles.controlPoints, overlayTiles.medianErrorM)
      : t.overlayNote(T.n, T.affineErrorMeters);
    if (!$('#banner').hidden) $('#banner').textContent = t.tilesMissing;
    maps.relabel();
  };

  // ---------- go ----------
  refresh();
  if (initial) select(initial.place.id, { fly: true, instant: true });

  // Warn (once) when the tile pyramid has not been generated.
  fetch(`${BASE}tiles/old/meta.json`, { cache: 'no-cache' })
    .then((r) => (r.ok && (r.headers.get('content-type') ?? '').includes('json') ? null : Promise.reject()))
    .catch(() => {
      const b = $('#banner');
      b.textContent = t.tilesMissing;
      b.hidden = false;
    });
}

void main();

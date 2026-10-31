import '@fontsource/eb-garamond/latin-400.css';
import '@fontsource/eb-garamond/latin-500.css';
import '@fontsource/eb-garamond/latin-400-italic.css';
import '@fontsource/inter/latin-400.css';
import '@fontsource/inter/latin-500.css';
import '@fontsource/inter/latin-600.css';
import './style.css';

import { renderCard, renderIntro } from './card';
import { badge } from './badge';
import { esc, statusClass, statusLabel, typeLabel } from './format';
import { lang, langBase, LANGS, mapBase, setLang, t, type Lang } from './i18n';
import { loadOverlayTiles, MapView, type Mode, type Orientation } from './maps';
import { initMobile } from './mobile';
import { buildEntries, modernText, type Entry } from './model';
import { IMAGE_H, IMAGE_W } from './oldPlane';
import { SearchIndex } from './search';
import { copyText, flash, qrSvg, shareLink } from './share';
import { decodeIds, Stars } from './stars';
import { PlaceTable } from './table';
import { createTransform } from './transform';
import type { GcpsFile, PlacesFile } from './types';
import { hasCamera, readViewState, viewQuery, withoutView } from './viewstate';

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

/** The map's standard view (/map/, /fr/map/…), keeping ?lang= if the address has it. */
function homeUrl(): string {
  const l = new URLSearchParams(location.search).get('lang');
  return `${mapBase()}${l ? `?lang=${encodeURIComponent(l)}` : ''}`;
}

function fillStaticText(): void {
  $('#brand-title').textContent = t.brandTitle;
  $('#brand-sub').textContent = `${t.siteName} · ${t.brandSub}`;
  $('#brand').title = t.brandHome;
  $('#brand').setAttribute('aria-label', `${t.brandTitle}. ${t.brandHome}`);
  $<HTMLAnchorElement>('#brand').href = homeUrl();
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
  $('#share-view .lbl').textContent = t.shareView;
  $('#share-view').title = t.shareViewHint;
  $('#share-view').setAttribute('aria-label', t.shareView);
  $('#tag-mod').textContent = t.tagMod;
  $('#op-label').textContent = t.overlayOpacity;
  $('#op-unit').textContent = t.overlayOpacityUnit;
  $('#swipe-hint').textContent = t.overlaySwipeHint;
  $('.swipe-l').textContent = t.overlayLeft;
  $('.swipe-r').textContent = t.overlayRight;
  const langs = LANGS.map((l) =>
    `<button type="button" data-lang="${l}" lang="${l}" aria-pressed="${l === lang}">${l.toUpperCase()}</button>`).join(' · ');
  $('#credits').innerHTML = `<span class="langs" role="group" aria-label="${esc(t.langLabel)}">${langs}</span>` +
    `<a href="${langBase()}">${esc(t.creditAbout)}</a> · <a href="${langBase()}method/">${esc(t.creditMethod)}</a> · ` +
    `<a href="${langBase()}texts/">${esc(t.creditTexts)}</a> · ` + [t.creditMap, t.creditOsm, t.creditBy].map(esc).join(' · ') + badge('sa-badge');
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

  // What the address asks for, read before anything rewrites it: a view to open at, and a list
  // of places someone shared. Both are then taken off the address, so that a reload does not ask
  // again and the replaceState that follows every selection (which keeps the query) stays clean.
  const wantedView = readViewState();
  const sharedIds = decodeIds(new URLSearchParams(location.search).get('stars') ?? '');
  if (sharedIds.length || Object.keys(wantedView).length) {
    history.replaceState(null, '', `${location.pathname}${withoutView()}`);
  }

  const stars = new Stars();

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
    /** Showing only the visitor's own starred places. */
    starred: false,
    /** Places a link shared, while they are being shown. Never merged into the visitor's own
     *  list without being asked: `null` once the question has been answered either way. */
    shared: null as { set: Set<string>; ids: string[]; unknown: number } | null,
    sharedBanner: false,
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
      (unsureCount ? `<button type="button" class="chip chip-unsure" data-chip="unsure">${esc(t.chipUnsure)} <span class="n">${unsureCount}</span></button>` : '') +
      // Starred is a filter like any other; it appears here as well as in the count line, and
      // only once there is something to filter by.
      (stars.size ? `<button type="button" class="chip chip-starred" data-chip="starred">★ ${esc(t.chipStarred)} <span class="n">${stars.size}</span></button>` : '');
    markChips();
  }
  function markChips(): void {
    chipsEl.querySelectorAll<HTMLButtonElement>('button.chip').forEach((c) => {
      const on = c.dataset.chip === 'all' ? state.types.size === 0
        : c.dataset.chip === 'type' ? state.types.has(c.dataset.type ?? '')
        : c.dataset.chip === 'starred' ? state.starred
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
    else if (b.dataset.chip === 'starred') setStarredView(!state.starred);
    markChips();
    updateFiltersBtn();
    if (state.selected) closeCard(false);
    refresh();
  });

  // ---------- filters menu ----------
  const filtersBtn = $<HTMLButtonElement>('#filters-btn');
  const filtersEl = $('#filters');
  function updateFiltersBtn(): void {
    const n = state.types.size + (state.unsure ? 1 : 0) + (state.starred ? 1 : 0);
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
    return !!state.query.trim() || state.types.size > 0 || state.unsure || state.starred || !!state.shared?.ids.length;
  }

  function resultHtml(e: Entry): string {
    const p = e.place;
    const m = modernText(p);
    const second = p.status ? statusLabel(p.status).toLowerCase() : typeLabel(p.type);
    const on = stars.has(p.id);
    // A place from someone else's link is not yours until you say so: its star is drawn hollow,
    // in the paler gold, and only a click makes it yours.
    const fromLink = !on && !!state.shared?.set.has(p.id);
    return `<div class="result${(state.selected ?? state.lastSelected) === e ? ' sel' : ''}" data-id="${esc(p.id)}" role="option">` +
      `<span class="dot ${statusClass(p.status)}"></span>` +
      `<span class="old">${esc(e.title)}${p.flag === 'unsure' ? ' <span class="q" title="' + esc(t.unsureBadge) + '">?</span>' : ''}</span>` +
      `<button type="button" class="star${on ? ' on' : fromLink ? ' from-link' : ''}" aria-pressed="${on}" ` +
      `aria-label="${esc(on ? t.unstarRow(e.title) : t.starRow(e.title))}">${on ? '★' : '☆'}</button>` +
      `<span class="mod"><span class="${m.placeholder ? 'placeholder' : ''}">${esc(m.text)}</span> · ${esc(second)}</span></div>`;
  }

  /** `keepScroll`: same results, new language; leave the list where it is. */
  function refresh(keepScroll = false): void {
    const shared = state.shared;
    const filter = (p: Entry['place']) =>
      (state.types.size === 0 || state.types.has(p.type)) && (!state.unsure || p.flag === 'unsure') &&
      (!state.starred || stars.has(p.id)) && (!shared?.ids.length || shared.set.has(p.id));
    state.results = index.search(state.query, filter).map((r) => byId.get(r.place.id) as Entry);
    const countText = shared?.ids.length ? t.sharedCount(state.results.length) : t.count(state.results.length, total);
    renderCount(countText);
    listEl.innerHTML = state.results.length
      ? state.results.map(resultHtml).join('')
      : `<p class="empty">${esc(state.starred ? t.starsEmpty : t.noResults)}</p>`;
    if (!keepScroll) listEl.scrollTop = 0;
    renderStarsBar();
    maps.setFilter(state.results, filterActive());
    if (state.view === 'table') table.update(state.results, state.selected?.place.id ?? null, countText);
  }

  listEl.addEventListener('click', (ev) => {
    const target = ev.target as HTMLElement;
    const r = target.closest('.result') as HTMLElement | null;
    if (!r?.dataset.id) return;
    // The star belongs to the row but is not a way into it.
    if (target.closest('.star')) {
      toggleStar(r.dataset.id);
      return;
    }
    select(r.dataset.id, { fly: true });
  });

  // ---------- starred places ----------
  // The list itself lives in stars.ts (this browser's own storage). Here is everything that
  // shows it: the way in from the count line, the bar under the list, and the banner a shared
  // link opens with. Nothing is sent anywhere; a link is the only thing that travels.

  const countEl = $('#count');
  const starsBarEl = $('#stars-bar');
  const sharedEl = $('#shared');
  let qrOpen = false;
  let confirmingClear = false;

  function renderCount(text: string): void {
    countEl.innerHTML = esc(text) +
      (stars.size
        ? `<span class="starsw"><button type="button" class="stars-link${state.starred ? ' on' : ''}" ` +
          `aria-pressed="${state.starred}" title="${esc(t.starsFilterHint)}">${esc(t.starsFilter(stars.size))}</button></span>`
        : '');
  }

  /** Show only the visitor's own places, or go back to all of them. A shared list is a different
   *  question, so it is put down first. */
  function setStarredView(on: boolean): void {
    state.starred = on;
    qrOpen = false;
    confirmingClear = false;
    if (on) {
      state.shared = null;
      state.sharedBanner = false;
      renderSharedBanner();
    }
  }

  function starsView(on: boolean): void {
    setStarredView(on);
    markChips();
    updateFiltersBtn();
    if (state.selected) closeCard(false);
    refresh();
  }

  countEl.addEventListener('click', (ev) => {
    if ((ev.target as HTMLElement).closest('.stars-link')) starsView(!state.starred);
  });

  /** The link to the starred list, in the language the visitor is reading. */
  function starsUrl(): string {
    const q = new URLSearchParams(withoutView().replace(/^\?/, ''));
    const code = stars.code();
    if (code) q.set('stars', code);
    const s = q.toString();
    return `${location.origin}${mapBase()}${s ? `?${s}` : ''}`;
  }

  function renderStarsBar(): void {
    const show = state.starred && stars.size > 0;
    starsBarEl.hidden = !show;
    if (!show) {
      starsBarEl.innerHTML = '';
      return;
    }
    const n = stars.size;
    const url = starsUrl();
    let qr = '';
    if (qrOpen) {
      let svg = '';
      try {
        svg = qrSvg(url, t.starsQrAlt);
      } catch {
        // A list too long for a symbol: the link itself still works, so show only that.
      }
      qr = '<div class="handoff">' +
        (svg ? `<span class="lbl">${esc(t.starsQrLead)}</span>${svg}` : '') +
        `<div class="side2"><span class="urlbox">${esc(url)}</span>` +
        `<span>${esc(t.starsPrivacy(n))}</span></div></div>`;
    }
    starsBarEl.innerHTML =
      '<div class="acts">' +
      `<button type="button" class="act" data-act="copy"><span class="ic" aria-hidden="true">⤴</span><span>${esc(t.starsCopy(n))}</span></button>` +
      `<button type="button" class="act${qrOpen ? ' starred' : ''}" data-act="qr" aria-expanded="${qrOpen}">` +
      `<span class="ic" aria-hidden="true">▣</span><span>${esc(qrOpen ? t.starsHandoffHide : t.starsHandoff)}</span></button>` +
      (confirmingClear
        ? `<span class="ask">${esc(t.starsClearAsk(n))}` +
          ` <button type="button" class="act danger" data-act="clear-yes">${esc(t.starsClearYes)}</button>` +
          ` <button type="button" class="act" data-act="clear-no">${esc(t.starsClearNo)}</button></span>`
        : `<button type="button" class="act danger" data-act="clear">${esc(t.starsClear)}</button>`) +
      '</div>' + qr +
      `<p class="note">${esc(stars.blocked ? t.starsBlocked : t.starsNote)}</p>`;
  }

  starsBarEl.addEventListener('click', async (ev) => {
    const b = (ev.target as HTMLElement).closest('[data-act]') as HTMLElement | null;
    if (!b) return;
    const act = b.dataset.act;
    if (act === 'copy') {
      flash(b, (await copyText(starsUrl())) ? t.copied : t.copyFailed);
    } else if (act === 'qr') {
      qrOpen = !qrOpen;
      renderStarsBar();
    } else if (act === 'clear') {
      confirmingClear = true;
      renderStarsBar();
    } else if (act === 'clear-no') {
      confirmingClear = false;
      renderStarsBar();
    } else if (act === 'clear-yes') {
      confirmingClear = false;
      stars.clear();
      starsView(false);
    }
  });

  function renderSharedBanner(): void {
    const sh = state.shared;
    const show = !!sh && state.sharedBanner;
    sharedEl.hidden = !show;
    if (!show || !sh) {
      sharedEl.innerHTML = '';
      return;
    }
    const n = sh.ids.length;
    // A link whose places are all unknown here says so and offers nothing: an id that cannot be
    // resolved must not be made to look resolved.
    sharedEl.innerHTML =
      `<button type="button" class="x" data-act="dismiss" aria-label="${esc(t.sharedDismiss)}" title="${esc(t.sharedDismiss)}">×</button>` +
      (n ? `<strong>${esc(t.sharedTitle(n))}</strong> ${esc(t.sharedAsk(n))}` : `<strong>${esc(t.sharedNone(sh.unknown))}</strong>`) +
      (n && sh.unknown ? ` <span class="muted">${esc(t.sharedUnknown(sh.unknown))}</span>` : '') +
      (n
        ? '<div class="acts">' +
          `<button type="button" class="act primary" data-act="add">${esc(t.sharedAdd(n))}</button>` +
          `<button type="button" class="act" data-act="look">${esc(t.sharedLook)}</button>` +
          '</div>'
        : '');
  }

  sharedEl.addEventListener('click', (ev) => {
    const b = (ev.target as HTMLElement).closest('[data-act]') as HTMLElement | null;
    const sh = state.shared;
    if (!b || !sh) return;
    if (b.dataset.act === 'add') {
      // Merge, never replace: what is already starred here stays starred, so following the same
      // link twice changes nothing and nobody's list is overwritten by someone else's.
      state.shared = null;
      state.sharedBanner = false;
      state.starred = true;
      const added = stars.addAll(sh.ids);
      flash(b, added ? t.sharedAdded(added) : t.sharedAlready);
      renderSharedBanner();
      markChips();
      updateFiltersBtn();
      refresh();
    } else if (b.dataset.act === 'look') {
      state.sharedBanner = false;
      renderSharedBanner();
    } else {
      state.shared = null;
      state.sharedBanner = false;
      renderSharedBanner();
      updateFiltersBtn();
      refresh();
    }
  });

  // One place decides what a change to the list redraws: the dots on both maps, the chips, the
  // count line, the list and the bar under it.
  stars.onChange(() => {
    maps.setStarred((id) => stars.has(id));
    renderChips();
    updateFiltersBtn();
    refresh(true);
  });
  maps.setStarred((id) => stars.has(id));

  function toggleStar(id: string): void {
    stars.toggle(id);
  }

  // ---------- sharing ----------

  $('#share-view').addEventListener('click', (ev) => {
    const b = ev.currentTarget as HTMLElement;
    const q = viewQuery(maps.getView());
    void shareLink({
      url: `${location.origin}${mapBase()}${q ? `?${q}` : ''}`,
      title: t.siteTitle,
      anchor: b,
      copied: t.copied,
      failed: t.copyFailed,
    });
  });

  function sharePlace(e: Entry, anchor: HTMLElement): void {
    void shareLink({
      url: `${location.origin}${langBase()}place/${encodeURIComponent(e.place.id)}/`,
      title: `${e.place.modern ?? e.place.old} · ${t.siteName}`,
      anchor,
      copied: t.copied,
      failed: t.copyFailed,
    });
  }

  /** What the card's two buttons do for a place. */
  function cardActions(e: Entry) {
    return {
      onClose: () => closeCard(true),
      onStar: () => stars.toggle(e.place.id),
      onShare: (btn: HTMLElement) => sharePlace(e, btn),
      starred: stars.has(e.place.id),
    };
  }

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
      renderCard(cardEl, e, T, state.results.length, cardActions(e));
      if (!wasOpen) mobile.cardOpened();
      history.replaceState(null, '', `${langBase()}place/${encodeURIComponent(e.place.id)}/${location.search}`);
      document.title = `${e.place.modern ?? e.place.old} · Paris 1550`;
    } else {
      renderIntro(cardEl);
      history.replaceState(null, '', `${mapBase()}${location.search}`);
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
  // the whole city, the address back to /map/ (keeping the language and ?lang=). A modified click
  // (new tab) is left alone.
  function startOver(): void {
    setFiltersOpen(false);
    q.value = '';
    $('#q-clear').hidden = true;
    clearTimeout(timer);
    state.query = '';
    state.types.clear();
    state.unsure = false;
    setStarredView(false);
    state.shared = null;
    state.sharedBanner = false;
    renderSharedBanner();
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
    renderSharedBanner();
    const listScroll = listEl.scrollTop;
    refresh(true);
    listEl.scrollTop = listScroll;
    const e = state.selected;
    if (e) {
      const cardScroll = cardEl.scrollTop;
      renderCard(cardEl, e, T, state.results.length, cardActions(e));
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

  // ---------- what the address asked for ----------

  /** A shared view: the mode, which way up, where and how far in. Each part is optional. */
  function applyWantedView(): void {
    const v = wantedView;
    const camera = hasCamera(v) && !initial; // a place in the address decides the camera itself
    if (v.mode) setMode(v.mode);
    if (v.orientation === 'original') {
      state.orientation = 'original';
      markOrientation();
      maps.setOrientation('original', !camera);
    }
    if (v.opacity !== undefined) {
      op.value = String(Math.round(v.opacity));
      maps.setOpacity(v.opacity / 100);
    }
    if (v.swipe !== undefined) setSwipe(v.swipe);
    if (camera && v.center && v.zoom !== undefined) maps.jumpToView(v.center, v.zoom, v.bearing ?? 0);
  }

  /** A shared list: shown, and offered — never merged into this browser's own list unasked. */
  function applySharedLink(): void {
    if (!sharedIds.length) return;
    const known = sharedIds.filter((id) => byId.has(id));
    state.shared = { set: new Set(known), ids: known, unknown: sharedIds.length - known.length };
    state.sharedBanner = true;
    renderSharedBanner();
    updateFiltersBtn();
  }

  // ---------- go ----------
  applyWantedView();
  applySharedLink();
  refresh();
  if (initial) select(initial.place.id, { fly: true, instant: true });
  else if (state.shared?.ids.length) maps.fitTo(state.results);

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

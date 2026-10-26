// Phone layout (mockups/mobile, option A): the sidebar is a bottom sheet over a full-screen map.
// The layout itself is mobile.css; this adds the sheet's grip (drag or tap: peek / half / full),
// short labels for the narrow bars, and a history entry while a place is open so the phone's
// Back button closes the card. Above 760 px it does nothing beyond adding hidden elements.

import './mobile.css';
import type { Map as MlMap } from 'maplibre-gl';
import { t } from './i18n';

type Sheet = 'peek' | 'half' | 'full';
const ORDER: Sheet[] = ['peek', 'half', 'full'];

export interface MobileHooks {
  /** Close the card and return to the list (as ← Back does). */
  back(): void;
  /** The map area changed size. */
  resize(): void;
}

export interface Mobile {
  /** A card is about to open over the list (call before the URL is replaced). */
  cardOpened(): void;
  /** The card was closed (call after the URL is replaced). */
  cardClosed(): void;
  /** Start the maps' attribution folded (the ⓘ button opens it), as it covers a third of a
   *  small pane otherwise. MapLibre unfolds it on load and folds it on the first drag. */
  foldAttribution(maps: MlMap[]): void;
  /** Back to the start: the sheet down to peek. */
  home(): void;
}

const mq = window.matchMedia('(max-width: 760px)');

export function initMobile(hooks: MobileHooks): Mobile {
  const app = document.querySelector('.app') as HTMLElement;
  const side = document.querySelector('.side') as HTMLElement;

  addShortLabels();

  // ---------- the sheet ----------
  const grip = document.createElement('button');
  grip.type = 'button';
  grip.className = 'sheet-grip';
  grip.title = t.sheetGrip;
  grip.setAttribute('aria-label', t.sheetGrip);
  side.prepend(grip);
  // The snap heights are CSS (vh, safe-area insets): read them off hidden probes.
  const probes = {} as Record<Sheet, HTMLElement>;
  for (const s of ORDER) {
    probes[s] = document.createElement('div');
    probes[s].className = 'sheet-probe';
    probes[s].style.height = `var(--${s}-h)`;
    document.body.append(probes[s]);
  }

  let sheet: Sheet = 'peek';
  function setSheet(s: Sheet): void {
    if (s === sheet && app.dataset.sheet === s) return;
    const mapChanges = (s === 'peek') !== (sheet === 'peek');
    sheet = s;
    app.dataset.sheet = s;
    grip.setAttribute('aria-expanded', String(s !== 'peek'));
    // The map area follows at once (it is not animated), so the map keeps its centre in view.
    if (mapChanges && mq.matches) hooks.resize();
  }
  setSheet('peek');

  let drag: { y: number; h: number; moved: boolean } | null = null;
  grip.addEventListener('pointerdown', (ev) => {
    if (!mq.matches || app.dataset.view === 'table') return;
    drag = { y: ev.clientY, h: side.offsetHeight, moved: false };
    grip.setPointerCapture(ev.pointerId);
    app.classList.add('dragging');
  });
  grip.addEventListener('pointermove', (ev) => {
    if (!drag) return;
    const dy = ev.clientY - drag.y;
    if (Math.abs(dy) > 6) drag.moved = true;
    if (!drag.moved) return;
    const h = Math.max(probes.peek.offsetHeight, Math.min(probes.full.offsetHeight, drag.h - dy));
    side.style.height = `${h}px`;
  });
  const endDrag = (ev: PointerEvent) => {
    if (!drag) return;
    const d = drag;
    drag = null;
    app.classList.remove('dragging');
    side.style.height = '';
    if (ev.type === 'pointercancel') return;
    if (!d.moved) {
      // A tap steps up, and from full back down to peek.
      setSheet(ORDER[(ORDER.indexOf(sheet) + 1) % ORDER.length]);
      return;
    }
    // Snap to the nearest height, leaning the way the finger moved.
    const h = d.h - (ev.clientY - d.y) + Math.sign(d.y - ev.clientY) * 40;
    let best: Sheet = 'peek';
    for (const s of ORDER) {
      if (Math.abs(probes[s].offsetHeight - h) < Math.abs(probes[best].offsetHeight - h)) best = s;
    }
    setSheet(best);
  };
  grip.addEventListener('pointerup', endDrag);
  grip.addEventListener('pointercancel', endDrag);

  // Searching or filtering needs room for the results.
  const lift = () => {
    if (mq.matches && sheet === 'peek' && app.dataset.view !== 'table') setSheet('half');
  };
  document.querySelector('#q')?.addEventListener('focus', lift);
  document.querySelector('#filters-btn')?.addEventListener('click', lift);

  mq.addEventListener('change', () => hooks.resize());

  // ---------- Back button ----------
  // Opening a card from the list pushes one history entry; the phone's Back pops it and closes
  // the card. Closing the card any other way pops it too, quietly, so Back is never a no-op.
  let pushed = false;
  let quietPop = false;
  window.addEventListener('popstate', () => {
    if (quietPop) {
      quietPop = false;
      // The entry we landed on may be a /place/ link the app was opened with.
      history.replaceState(null, '', `${import.meta.env.BASE_URL}${location.search}`);
      return;
    }
    if (!pushed) return;
    pushed = false;
    hooks.back();
  });

  return {
    cardOpened() {
      if (!mq.matches) return;
      if (!pushed) {
        history.pushState(null, '', location.href);
        pushed = true;
      }
      if (sheet === 'peek') setSheet('half');
    },
    cardClosed() {
      if (!pushed) return;
      pushed = false;
      quietPop = true;
      history.back();
    },
    home() {
      setSheet('peek');
    },
    foldAttribution(maps) {
      for (const m of maps) {
        m.once('load', () => {
          if (mq.matches) m.getContainer().querySelector('.maplibregl-ctrl-attrib')?.classList.remove('maplibregl-compact-show');
        });
      }
    },
  };
}

/** Wrap a label so CSS can show a shorter one on a phone. */
function addShortLabels(): void {
  const pairs: [string, string][] = [
    ['.viewtabs [data-view=table]', t.viewTableShort],
    ['#modes [data-m=side]', t.modeSideShort],
    ['#modes [data-m=overlay]', t.modeOverlayShort],
    ['#modes [data-m=old]', t.modeOldShort],
    ['#modes [data-m=mod]', t.modeModShort],
    ['#orient .lbl', t.orientOriginalShort],
  ];
  for (const [sel, short] of pairs) {
    const el = document.querySelector(sel);
    if (!el) continue;
    const long = document.createElement('span');
    long.className = 'lbl-long';
    long.textContent = el.textContent;
    const s = document.createElement('span');
    s.className = 'lbl-short';
    s.textContent = short;
    el.replaceChildren(long, s);
  }
}

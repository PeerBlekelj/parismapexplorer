// "Look at the overlay here" as an address.
//
// The app's own state — which mode, which way up, where the cameras are, how far in, the
// overlay's opacity and the swipe — written into the query string and read back. Every part is
// optional, so a link made before a new one was added still opens, and one with nothing it
// recognises simply opens the standard view.
//
// The address is only rewritten when the visitor asks for the link (the Share view button): the
// app already rewrites the path for /place/ links, and a second writer following every map move
// would fight it.

import type { Mode, Orientation } from './maps';
import type { Vec2 } from './types';

export interface ViewState {
  mode?: Mode;
  orientation?: Orientation;
  center?: Vec2; // [lng, lat]
  zoom?: number;
  bearing?: number;
  opacity?: number; // 0–100, overlay only
  swipe?: number; // 0–100, overlay only
  dots?: boolean; // the place marks; false when they have been switched off
}

const MODES: Mode[] = ['side', 'overlay', 'old', 'mod'];

function num(v: string | null, lo: number, hi: number): number | undefined {
  if (v === null) return undefined;
  const n = Number(v);
  return Number.isFinite(n) && n >= lo && n <= hi ? n : undefined;
}

const round = (v: number, digits: number): string => String(Number(v.toFixed(digits)));

/** What the address asks for. Anything unreadable is left out rather than guessed at. */
export function readViewState(search = location.search): ViewState {
  const q = new URLSearchParams(search);
  const v: ViewState = {};
  const m = q.get('m');
  if (m && (MODES as string[]).includes(m)) v.mode = m as Mode;
  if (q.get('or') === '1') v.orientation = 'original';
  const c = q.get('c');
  if (c) {
    const [lat, lng] = c.split(',').map(Number);
    // Paris, not the whole globe, but the bounds stay generous: the point is to reject nonsense.
    if (Number.isFinite(lat) && Number.isFinite(lng) && Math.abs(lat) <= 85 && Math.abs(lng) <= 180) {
      v.center = [lng, lat];
    }
  }
  const z = num(q.get('z'), 0, 24);
  if (z !== undefined) v.zoom = z;
  const b = num(q.get('b'), -360, 360);
  if (b !== undefined) v.bearing = b;
  const o = num(q.get('o'), 0, 100);
  if (o !== undefined) v.opacity = o;
  const s = num(q.get('s'), 0, 100);
  if (s !== undefined) v.swipe = s;
  if (q.get('d') === '0') v.dots = false;
  return v;
}

/** True when the address carries a camera (as opposed to only a mode or an orientation). */
export function hasCamera(v: ViewState): boolean {
  return !!v.center && v.zoom !== undefined;
}

/**
 * The query string for a view. `lang` is carried over from the current address, because a link
 * someone sends should open in the language they were reading. Defaults are left out: a link to
 * the plain side-by-side view is just `/map/`.
 */
export function viewQuery(v: ViewState, search = location.search): string {
  const q = new URLSearchParams();
  const lang = new URLSearchParams(search).get('lang');
  if (lang) q.set('lang', lang);
  if (v.mode && v.mode !== 'side') q.set('m', v.mode);
  if (v.orientation === 'original') q.set('or', '1');
  if (v.center) q.set('c', `${round(v.center[1], 5)},${round(v.center[0], 5)}`);
  if (v.zoom !== undefined) q.set('z', round(v.zoom, 2));
  if (v.bearing) q.set('b', round(v.bearing, 1));
  if (v.mode === 'overlay') {
    if (v.opacity !== undefined) q.set('o', round(v.opacity, 0));
    if (v.swipe !== undefined) q.set('s', round(v.swipe, 0));
  }
  if (v.dots === false) q.set('d', '0');
  // A comma is safe in a query and these links get pasted into messages, so it stays a
  // comma rather than %2C. Everything else keeps the standard encoding.
  return q.toString().replace(/%2C/g, ',');
}

/** Strip the view parameters from an address, keeping anything else (`lang`) it carries. */
export function withoutView(search = location.search): string {
  const q = new URLSearchParams(search);
  for (const k of ['m', 'or', 'c', 'z', 'b', 'o', 's', 'd', 'stars']) q.delete(k);
  const s = q.toString();
  return s ? `?${s}` : '';
}

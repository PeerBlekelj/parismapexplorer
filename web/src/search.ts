// Search tolerant of 16th-century spelling.
//
//  norm:   lower case, accents stripped, œ→oe, u/v → u, i/j/y → i, punctuation → space
//  loose:  norm plus "silent" spellings folded: s before a consonant (nostre → notre,
//          hostel → hotel), ct → t (sainct → saint), ph → f, th → t, doubled letters single
//  core:   loose tokens minus S./R./Saint/Rue and articles, for a secondary match
//          ("pont saint michel" ↔ "LE PONT S. MICHEL")
//  fuzzy:  tokens may differ by 1 edit (≥ 4 letters) or 2 edits (≥ 8 letters), and the last
//          query token may be a prefix.

import type { Place } from './types';

const STOP = new Set([
  's', 'st', 'ste', 'saint', 'sainte', 'sainct', 'saincte', 'sanct', 'r', 'rue',
  'le', 'la', 'les', 'l', 'de', 'du', 'des', 'd', 'au', 'aux', 'a', 'en', 'et', 'lo',
  'the', 'of',
]);

export function norm(s: string): string {
  return s
    .toLowerCase()
    .replace(/œ/g, 'oe').replace(/æ/g, 'ae').replace(/ß/g, 'ss')
    .normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/v/g, 'u').replace(/[jy]/g, 'i')
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();
}

function looseToken(w: string): string {
  return w
    .replace(/ph/g, 'f')
    .replace(/th/g, 't')
    .replace(/ct/g, 't')
    .replace(/(?<=.)s(?=[bcdfghklmnpqrtxz])/g, '')
    .replace(/(.)\1+/g, '$1');
}

interface Indexed {
  n: string;        // normalised full string
  loose: string;    // loose full string
  tokens: string[]; // loose tokens
  core: string[];   // loose tokens without stop words
}

function index(s: string): Indexed {
  const n = norm(s);
  const raw = n ? n.split(' ') : [];
  const tokens = raw.map(looseToken);
  const core = raw.filter((w) => !STOP.has(w)).map(looseToken);
  return { n, loose: tokens.join(' '), tokens, core };
}

/** Optimal-string-alignment distance with an early exit above `max`. */
function editDistance(a: string, b: string, max: number): number {
  if (Math.abs(a.length - b.length) > max) return max + 1;
  const m = a.length, n = b.length;
  let prev2: number[] = [];
  let prev = Array.from({ length: n + 1 }, (_, j) => j);
  for (let i = 1; i <= m; i++) {
    const cur = [i];
    let rowMin = i;
    for (let j = 1; j <= n; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      let v = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost);
      if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) v = Math.min(v, prev2[j - 2] + 1);
      cur.push(v);
      if (v < rowMin) rowMin = v;
    }
    if (rowMin > max) return max + 1;
    prev2 = prev;
    prev = cur;
  }
  return prev[n];
}

/** Cost of matching query token q against field token f, or null when they don't match. */
function tokenCost(q: string, f: string, allowPrefix: boolean): number | null {
  if (q === f) return 0;
  if (allowPrefix && q.length >= 2 && f.startsWith(q)) return 0.25;
  const tol = q.length >= 8 ? 2 : q.length >= 4 ? 1 : 0;
  if (tol === 0) return null;
  const d = editDistance(q, f, tol);
  if (d <= tol) return d;
  if (allowPrefix && f.length > q.length) {
    for (let L = q.length - 1; L <= q.length + 1; L++) {
      if (L < 3 || L > f.length) continue;
      const dp = editDistance(q, f.slice(0, L), tol);
      if (dp <= tol) return dp + 0.25;
    }
  }
  return null;
}

function tokensScore(qt: string[], ft: string[]): number | null {
  if (!qt.length || !ft.length) return null;
  let cost = 0;
  for (let i = 0; i < qt.length; i++) {
    const last = i === qt.length - 1;
    let best: number | null = null;
    for (const f of ft) {
      const c = tokenCost(qt[i], f, last || qt[i].length >= 3);
      if (c !== null && (best === null || c < best)) best = c;
      if (best === 0) break;
    }
    if (best === null) return null;
    cost += best;
  }
  return Math.max(10, 70 - 9 * cost);
}

function fieldScore(q: Indexed, f: Indexed): number | null {
  if (!f.n) return null;
  let s: number | null = null;
  const at = f.n.indexOf(q.n);
  if (at >= 0) {
    s = 100 + (at === 0 ? 15 : 0) + (at === 0 || f.n[at - 1] === ' ' ? 5 : 0);
  } else {
    const la = f.loose.indexOf(q.loose);
    if (la >= 0) s = 85 + (la === 0 ? 10 : 0);
  }
  if (s !== null) return s;
  // secondary: drop S./R./articles on both sides when the query has a real word left
  if (q.core.length) {
    const sc = tokensScore(q.core, f.core.length ? f.core : f.tokens);
    if (sc !== null) return sc;
  }
  return tokensScore(q.tokens, f.tokens);
}

interface PlaceIndex { place: Place; fields: { idx: Indexed; w: number }[]; sortKey: string }

export class SearchIndex {
  private items: PlaceIndex[];

  constructor(places: Place[]) {
    this.items = places.map((place) => {
      const fields = [
        { idx: index(place.old), w: 1 },
        ...(place.variants ?? []).map((v) => ({ idx: index(v), w: 0.95 })),
        ...(place.modern ? [{ idx: index(place.modern), w: 0.9 }] : []),
        ...(place.note ? [{ idx: index(place.note), w: 0.55 }] : []),
      ];
      return { place, fields, sortKey: norm(place.old) };
    });
  }

  /** Places matching the query, best first. An empty query returns all, alphabetically. */
  search(query: string, filter: (p: Place) => boolean): { place: Place; score: number }[] {
    const q = index(query);
    const out: { place: Place; score: number; key: string }[] = [];
    for (const it of this.items) {
      if (!filter(it.place)) continue;
      if (!q.n) {
        out.push({ place: it.place, score: 0, key: it.sortKey });
        continue;
      }
      let best: number | null = null;
      for (const f of it.fields) {
        const s = fieldScore(q, f.idx);
        if (s !== null && (best === null || s * f.w > best)) best = s * f.w;
      }
      if (best !== null) out.push({ place: it.place, score: best, key: it.sortKey });
    }
    out.sort((a, b) => b.score - a.score || a.key.length - b.key.length || a.key.localeCompare(b.key));
    if (!q.n) out.sort((a, b) => a.key.localeCompare(b.key));
    return out;
  }
}

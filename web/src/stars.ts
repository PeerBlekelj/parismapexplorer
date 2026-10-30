// The visitor's own starred places.
//
// Two rules shape this file. The list is kept in THIS browser (localStorage, which a private
// window or blocked site data can refuse, so every access is guarded), and it travels only by a
// link the visitor chooses to copy — nothing here is ever sent anywhere. A link carries the
// numeric part of the ids and nothing else: no name, no history, no identifier of the visitor.

const KEY = 'starred';
/** A list longer than this is a bug or a bored visitor; either way, stop growing the store. */
const MAX = 2000;

/**
 * The stable numeric part of a place id: L0017 → 17. Share links are indexed by this number and
 * never by a row's position in places.json, which shifts whenever a place is added or removed.
 * The ids must therefore never be reused for a different place.
 */
export function idNum(id: string): number | null {
  const m = /^L(\d{1,6})$/.exec(id);
  if (!m) return null;
  const n = Number(m[1]);
  return Number.isInteger(n) ? n : null;
}

/** The id form of a number: 17 → L0017 (four digits, as the data files write them). */
export function numId(n: number): string {
  return `L${String(n).padStart(4, '0')}`;
}

function toBase64url(bytes: Uint8Array): string {
  let s = '';
  for (const b of bytes) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function fromBase64url(v: string): Uint8Array | null {
  try {
    const s = atob(v.replace(/-/g, '+').replace(/_/g, '/'));
    const out = new Uint8Array(s.length);
    for (let i = 0; i < s.length; i++) out[i] = s.charCodeAt(i);
    return out;
  } catch {
    return null;
  }
}

/**
 * The value of `?stars=`: whichever of the two forms is shorter.
 *
 * The readable one is the id numbers joined by dots (`2.6.15`); the compact one is a bitmap of
 * the ids in base64url, with trailing zero bytes trimmed, so it grows only as far as the highest
 * starred id — 79 characters for all 457 places, however many of them are starred. A short value
 * also makes a QR code a phone camera reads at arm's length.
 */
export function encodeIds(ids: readonly string[]): string {
  const nums = [...new Set(ids.map(idNum).filter((n): n is number => n !== null))].sort((a, b) => a - b);
  if (!nums.length) return '';
  const list = nums.join('.');
  const bytes = new Uint8Array((nums[nums.length - 1] >> 3) + 1);
  for (const n of nums) bytes[n >> 3] |= 1 << (7 - (n & 7));
  const packed = toBase64url(bytes);
  return packed.length < list.length ? packed : list;
}

/** Read either form back. Returns ids in ascending order; an unreadable value gives none. */
export function decodeIds(v: string): string[] {
  const s = v.trim();
  if (!s) return [];
  if (/^\d+(\.\d+)*$/.test(s)) {
    return [...new Set(s.split('.').map(Number))].filter((n) => Number.isInteger(n) && n >= 0).sort((a, b) => a - b).map(numId);
  }
  const bytes = fromBase64url(s);
  if (!bytes) return [];
  const out: string[] = [];
  for (let i = 0; i < bytes.length * 8; i++) {
    if (bytes[i >> 3] & (1 << (7 - (i & 7)))) out.push(numId(i));
  }
  return out;
}

/**
 * The list itself, in the order the places were starred. `blocked` is true when the browser
 * refused storage: the list then works for this visit only, and the UI says so rather than
 * letting someone believe a star is safe.
 */
export class Stars {
  private ids: string[] = [];
  private set = new Set<string>();
  private listeners: (() => void)[] = [];
  readonly blocked: boolean;

  constructor() {
    let blocked = false;
    try {
      const raw = localStorage.getItem(KEY);
      if (raw) {
        for (const id of raw.split(',')) {
          const t = id.trim();
          if (idNum(t) !== null && !this.set.has(t) && this.ids.length < MAX) {
            this.ids.push(t);
            this.set.add(t);
          }
        }
      }
      // A read can succeed where a write is refused (Safari's private mode used to do exactly
      // that), so prove the write too rather than discover it at the first star.
      localStorage.setItem(KEY, this.ids.join(','));
    } catch {
      blocked = true;
    }
    this.blocked = blocked;
  }

  get size(): number {
    return this.ids.length;
  }

  /** The starred ids, oldest first. A copy: callers may sort or filter it. */
  list(): string[] {
    return [...this.ids];
  }

  has(id: string): boolean {
    return this.set.has(id);
  }

  add(id: string): void {
    if (this.set.has(id) || idNum(id) === null || this.ids.length >= MAX) return;
    this.ids.push(id);
    this.set.add(id);
    this.save();
  }

  remove(id: string): void {
    if (!this.set.delete(id)) return;
    this.ids = this.ids.filter((x) => x !== id);
    this.save();
  }

  toggle(id: string): boolean {
    if (this.set.has(id)) {
      this.remove(id);
      return false;
    }
    this.add(id);
    return true;
  }

  /** Merge, never replace: returns how many were not already starred. Following the same link
   *  twice therefore changes nothing, and no star is ever lost to someone else's list. */
  addAll(ids: readonly string[]): number {
    let added = 0;
    for (const id of ids) {
      if (!this.set.has(id) && idNum(id) !== null && this.ids.length < MAX) {
        this.ids.push(id);
        this.set.add(id);
        added++;
      }
    }
    if (added) this.save();
    return added;
  }

  clear(): void {
    if (!this.ids.length) return;
    this.ids = [];
    this.set.clear();
    this.save();
  }

  /** The value for `?stars=`, or '' when nothing is starred. */
  code(): string {
    return encodeIds(this.ids);
  }

  onChange(fn: () => void): void {
    this.listeners.push(fn);
  }

  private save(): void {
    try {
      localStorage.setItem(KEY, this.ids.join(','));
    } catch {
      /* storage refused; the list still works for this visit */
    }
    for (const fn of this.listeners) fn();
  }
}

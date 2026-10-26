import { fmtNum, lang, t } from './i18n';
import type { Place } from './types';

const SMALL = new Set(['de', 'du', 'des', 'la', 'le', 'les', 'au', 'aux', 'et', 'en', 'a', 'sur', 'lez', 'sus', 'dela', 'del']);

function cap(w: string): string {
  return w ? w[0].toUpperCase() + w.slice(1) : w;
}

/**
 * Display form of a label printed in capitals: "LE PONT NOSTRE DAME" → "Le Pont Nostre Dame".
 * Spelling is kept; only the case changes (rendered in small caps, as in the mockup).
 */
export function displayOld(old: string): string {
  const parts = old.toLowerCase().split(/(\s+|-)/);
  let wordIndex = 0;
  return parts
    .map((part) => {
      if (/^\s+$/.test(part) || part === '-' || part === '') return part;
      const first = wordIndex++ === 0;
      // apostrophes: l'hostel → L'Hostel / l'Hostel
      if (part.includes("'") || part.includes('’')) {
        const [pre, ...rest] = part.split(/(['’])/);
        const tail = rest.map((r, i) => (i % 2 === 1 ? cap(r) : r)).join('');
        return (first ? cap(pre) : pre) + tail;
      }
      if (!first && SMALL.has(part)) return part;
      return cap(part);
    })
    .join('');
}

export function typeLabel(type: string): string {
  return t.typeLabels[type] ?? t.typeLabels.other;
}

export function statusLabel(status: string | null): string {
  return status ? t.statusLabels[status] ?? status : t.statusUnknown;
}

/** CSS class used for the status dot/badge: 'unknown' for null, never a negative style. */
export function statusClass(status: string | null): string {
  if (!status) return 'unknown';
  return ['standing', 'rebuilt', 'renamed', 'vanished'].includes(status) ? status : 'unknown';
}

export function hasKnownPosition(p: Place): boolean {
  return typeof p.lat === 'number' && typeof p.lon === 'number' && Number.isFinite(p.lat) && Number.isFinite(p.lon);
}

export function fmtLat(lat: number, digits: number): string {
  return `${fmtNum(Math.abs(lat), digits)}° ${t.compass[lat >= 0 ? 'N' : 'S']}`;
}

export function fmtLon(lon: number, digits: number): string {
  return `${fmtNum(Math.abs(lon), digits)}° ${t.compass[lon >= 0 ? 'E' : 'W']}`;
}

/** The summary in the current language, falling back to English. `lang` is set on the element
 *  when the text is not in the page's language. */
export function summaryFor(p: Place): { text: string; lang: string | null } | null {
  const own = lang === 'fr' ? p.summary_fr : lang === 'sv' ? p.summary_sv : null;
  if (own) return { text: own, lang: null };
  if (p.summary) return { text: p.summary, lang: lang === 'en' ? null : 'en' };
  return null;
}

const ESC: Record<string, string> = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
export function esc(s: unknown): string {
  return String(s ?? '').replace(/[&<>"']/g, (c) => ESC[c]);
}

/** Only http(s) links from the data are turned into anchors. */
export function safeUrl(u: string): string | null {
  try {
    const url = new URL(u);
    return url.protocol === 'https:' || url.protocol === 'http:' ? url.href : null;
  } catch {
    return null;
  }
}

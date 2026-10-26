// The current language: `t` holds its strings (strings.ts), `setLang` switches it (callers then
// re-render). French and Swedish live under /fr/ and /sv/; English is unprefixed.

import { isLang, LANGS, STRINGS, type Lang, type Strings } from './strings';

export { LANGS, type Lang, type Strings };
const STORE_KEY = 'lang';
const BASE = import.meta.env.BASE_URL;
const PREFIX = new RegExp(`^${BASE.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(fr|sv)(?:/|$)`);

/** The language a /fr/… or /sv/… address names, or null for the unprefixed (English) paths. */
function pathLang(): Lang | null {
  const m = PREFIX.exec(location.pathname);
  return m && isLang(m[1]) ? m[1] : null;
}

/** ?lang= in the address, then the /fr/ or /sv/ path, then the visitor's earlier choice, then
 *  the browser's language. An unprefixed path says nothing: it is also where old links point. */
function detectLang(): Lang {
  const q = new URLSearchParams(location.search).get('lang');
  if (isLang(q)) return q;
  const p = pathLang();
  if (p) return p;
  try {
    const s = localStorage.getItem(STORE_KEY);
    if (isLang(s)) return s;
  } catch { /* storage blocked */ }
  const nav = (navigator.language || '').toLowerCase();
  return nav.startsWith('fr') ? 'fr' : nav.startsWith('sv') ? 'sv' : 'en';
}

// Live bindings: modules that import `t` and `lang` see the new values after `setLang`.
export let lang: Lang = detectLang();
export let t: Strings = STRINGS[lang];
document.documentElement.lang = lang;

/** The site root in language `l`: "/" for English, "/fr/", "/sv/". The start page (about the
 *  map) lives there; the app and the other pages hang off it. */
export function langBase(l: Lang = lang): string {
  return l === 'en' ? BASE : `${BASE}${l}/`;
}

/** The map app's own address in language `l`: "/map/", "/fr/map/", "/sv/map/". */
export function mapBase(l: Lang = lang): string {
  return `${langBase(l)}map/`;
}

/** Put the address on the current language's path (/fr/place/L0123/ ↔ /place/L0123/), keeping
 *  the rest of it; ?lang= is updated if the address has one. */
function syncPath(): void {
  const params = new URLSearchParams(location.search);
  if (params.has('lang')) params.set('lang', lang);
  const from = pathLang();
  const rest = location.pathname.slice(langBase(from ?? 'en').length);
  const url = `${langBase()}${rest}${params.size ? `?${params}` : ''}${location.hash}`;
  if (url !== `${location.pathname}${location.search}${location.hash}`) history.replaceState(history.state, '', url);
}
syncPath();

/** Switch language (a visitor's choice: remembered, and the address moves to the same page in
 *  the new language, with ?lang= updated if it has one). */
export function setLang(l: Lang): void {
  lang = l;
  t = STRINGS[l];
  document.documentElement.lang = l;
  try {
    localStorage.setItem(STORE_KEY, l);
  } catch { /* storage blocked */ }
  syncPath();
}

/** Format a number with the language's decimal comma or point. */
export function fmtNum(v: number, digits: number): string {
  return v.toLocaleString(lang === 'en' ? 'en-GB' : lang, { minimumFractionDigits: digits, maximumFractionDigits: digits, useGrouping: false });
}

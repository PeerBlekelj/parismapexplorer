// Per-place data derived once at load: display name, old-map position, modern position
// (real when the data has lat/lon, otherwise estimated with the transform).

import { displayOld, hasKnownPosition, inscriptionTitle } from './format';
import { t } from './i18n';
import { pxToLngLat } from './oldPlane';
import { localModernIn } from './strings';
import type { PixelGeoTransform } from './transform';
import type { Place, Vec2 } from './types';

/** How the modern position was obtained. 'unassessed' = lat/lon given, loc_confidence null. */
/** 'sheet': the thing exists only as ink on the printed sheet, so it has no position on the
 *  ground at all -- not even an estimated one to show. */
export type GeoKind = 'exact' | 'approx' | 'uncertain' | 'unassessed' | 'estimated' | 'sheet';

export interface Entry {
  place: Place;
  title: string;   // display form of the old name
  px: Vec2;        // label position on the scan
  oldLL: Vec2;     // pseudo-lnglat on the old-map plane
  alsoLL: Vec2[];  // other labels for the same place, on the old-map plane
  geo: Vec2;       // [lng, lat] on the modern map
  geoKind: GeoKind;
}

export function buildEntries(places: Place[], T: PixelGeoTransform): Entry[] {
  return places
    .filter((p) => p && typeof p.id === 'string' && Array.isArray(p.px))
    .map((raw) => {
      const place: Place = { ...raw, variants: raw.variants ?? [], sources: raw.sources ?? [] };
      const px: Vec2 = [place.px[0], place.px[1]];
      let geo: Vec2;
      let geoKind: GeoKind;
      if (hasKnownPosition(place)) {
        geo = [place.lon as number, place.lat as number];
        const c = place.loc_confidence;
        geoKind = c === 'exact' || c === 'approx' || c === 'uncertain' ? c : 'unassessed';
      } else {
        // The camera still needs somewhere to look, so an inscription gets the transform's guess
        // like any unlocated label; 'sheet' is what stops it being shown as a position.
        geo = T.pxToLngLat(px);
        geoKind = place.type === 'inscription' ? 'sheet' : 'estimated';
      }
      const alsoLL = (place.also_px ?? []).map((q) => pxToLngLat([q[0], q[1]]));
      return { place, title: displayOld(place.old), px, oldLL: pxToLngLat(px), alsoLL, geo, geoKind };
    });
}

/**
 * What to call an entry on screen. `Entry.title` is fixed when the data loads, but a wordless
 * device is named rather than transcribed, and that name follows the language.
 */
export function displayTitle(e: Entry): string {
  return e.place.type === 'inscription' ? inscriptionTitle(e.place) : e.title;
}

/** What to show for "today": the modern name, or a neutral placeholder (never a blank). */
export function modernText(p: Place): { text: string; placeholder: boolean } {
  // An inscription has no "today": saying "not identified yet" of the map's own title would be
  // a placeholder for something that was never missing.
  if (p.type === 'inscription') return { text: t.onTheSheet, placeholder: true };
  if (p.modern) return { text: localModern(p.modern), placeholder: false };
  if (p.status === 'vanished') return { text: t.noLongerExists, placeholder: true };
  return { text: t.notIdentified, placeholder: true };
}

/** The modern name in the current language (see localModernIn). */
export function localModern(m: string): string {
  return localModernIn(m, t);
}

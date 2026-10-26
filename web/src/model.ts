// Per-place data derived once at load: display name, old-map position, modern position
// (real when the data has lat/lon, otherwise estimated with the transform).

import { displayOld, hasKnownPosition } from './format';
import { t } from './i18n';
import { pxToLngLat } from './oldPlane';
import type { PixelGeoTransform } from './transform';
import type { Place, Vec2 } from './types';

/** How the modern position was obtained. 'unassessed' = lat/lon given, loc_confidence null. */
export type GeoKind = 'exact' | 'approx' | 'uncertain' | 'unassessed' | 'estimated';

export interface Entry {
  place: Place;
  title: string;   // display form of the old name
  px: Vec2;        // label position on the scan
  oldLL: Vec2;     // pseudo-lnglat on the old-map plane
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
        geo = T.pxToLngLat(px);
        geoKind = 'estimated';
      }
      return { place, title: displayOld(place.old), px, oldLL: pxToLngLat(px), geo, geoKind };
    });
}

/** What to show for "today": the modern name, or a neutral placeholder (never a blank). */
export function modernText(p: Place): { text: string; placeholder: boolean } {
  if (p.modern) return { text: p.modern, placeholder: false };
  if (p.status === 'vanished') return { text: t.noLongerExists, placeholder: true };
  return { text: t.notIdentified, placeholder: true };
}

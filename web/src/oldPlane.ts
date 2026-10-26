// The scan as a flat plane in Web Mercator ("pseudo-lnglat").
//
// scripts/make_old_tiles.py places the image's top-left corner at lng/lat (0, 0) (the centre
// of the Mercator world), image x running east and image y running south, with one image
// pixel = one tile pixel at tile zoom TILE_MAX_ZOOM. MapLibre at bearing 0 therefore shows the
// map exactly as printed (east-up). These constants MUST match the script.

import type { Vec2 } from './types';

export const IMAGE_W = 10890;
export const IMAGE_H = 7820;
export const TILE_SIZE = 256;
export const TILE_MIN_ZOOM = 7;
export const TILE_MAX_ZOOM = 14;

/** Size of the Mercator world in image pixels. */
const WORLD_PX = TILE_SIZE * 2 ** TILE_MAX_ZOOM;
/** EPSG:3857 circumference in metres. */
export const MERC_WORLD_M = 40075016.68557849;
/** EPSG:3857 metres per image pixel inside the pseudo plane. */
export const PLANE_MERC_M_PER_PX = MERC_WORLD_M / WORLD_PX;

const D2R = Math.PI / 180;

/** Image pixel (x right, y down) → pseudo [lng, lat] of the old-map plane. */
export function pxToLngLat(p: Vec2): Vec2 {
  const lng = (p[0] / WORLD_PX) * 360;
  const my = 0.5 + p[1] / WORLD_PX; // normalised Mercator y, 0 at the top of the world
  const lat = (360 / Math.PI) * Math.atan(Math.exp((180 - my * 360) * D2R)) - 90;
  return [lng, lat];
}

/** Pseudo [lng, lat] of the old-map plane → image pixel. */
export function lngLatToPx(ll: Vec2): Vec2 {
  const x = (ll[0] / 360) * WORLD_PX;
  const my = (180 - Math.log(Math.tan(Math.PI / 4 + (ll[1] * D2R) / 2)) / D2R) / 360;
  return [x, (my - 0.5) * WORLD_PX];
}

/**
 * MapLibre's world is 512·2^zoom CSS px wide, the plane is WORLD_PX image px wide, so at
 * map zoom z one image pixel is 2^(z - TILE_MAX_ZOOM + 1) CSS px.
 */
export function oldZoomForScale(cssPxPerImagePx: number): number {
  return TILE_MAX_ZOOM - 1 + Math.log2(cssPxPerImagePx);
}

export const IMAGE_SW = pxToLngLat([0, IMAGE_H]);
export const IMAGE_NE = pxToLngLat([IMAGE_W, 0]);
/** [west, south, east, north] in pseudo-lnglat, for the raster source's `bounds`. */
export const IMAGE_BOUNDS: [number, number, number, number] =
  [IMAGE_SW[0], IMAGE_SW[1], IMAGE_NE[0], IMAGE_NE[1]];

/** Is an image pixel inside the scan? */
export function insideImage(p: Vec2, margin = 0): boolean {
  return p[0] >= -margin && p[1] >= -margin && p[0] <= IMAGE_W + margin && p[1] <= IMAGE_H + margin;
}

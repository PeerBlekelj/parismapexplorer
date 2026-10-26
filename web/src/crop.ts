// A crop of the old map around a label, drawn on a canvas from the tile pyramid (as printed,
// east at top, so the label reads the way it was cut).

import { IMAGE_H, IMAGE_W, TILE_MAX_ZOOM, TILE_MIN_ZOOM, TILE_SIZE } from './oldPlane';
import type { Vec2 } from './types';

const BASE = `${location.origin}${import.meta.env.BASE_URL}`;
const cache = new Map<string, Promise<HTMLImageElement | null>>();

function loadTile(z: number, x: number, y: number): Promise<HTMLImageElement | null> {
  const url = `${BASE}tiles/old/${z}/${x}/${y}.webp`;
  let p = cache.get(url);
  if (!p) {
    p = new Promise((resolve) => {
      const img = new Image();
      img.onload = () => resolve(img);
      img.onerror = () => resolve(null);
      img.src = url;
    });
    cache.set(url, p);
  }
  return p;
}

let seq = 0;

/**
 * Draw the area around `px` into `canvas`, `cssW`×`cssH` CSS px at `imgPerCss` image px per
 * CSS px. Returns false when no tile could be loaded.
 */
export async function drawCrop(canvas: HTMLCanvasElement, px: Vec2, cssW: number, cssH: number, imgPerCss: number): Promise<boolean> {
  const token = String(++seq);
  canvas.dataset.token = token;
  const dpr = Math.min(2, window.devicePixelRatio || 1);
  canvas.width = Math.round(cssW * dpr);
  canvas.height = Math.round(cssH * dpr);
  canvas.style.width = `${cssW}px`;
  canvas.style.height = `${cssH}px`;
  const ctx = canvas.getContext('2d');
  if (!ctx) return false;
  ctx.fillStyle = '#d6c9ad';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  const imgPerDev = imgPerCss / dpr;
  const down = Math.max(0, Math.floor(Math.log2(imgPerDev)));
  const z = Math.max(TILE_MIN_ZOOM, TILE_MAX_ZOOM - down);
  const span = TILE_SIZE * 2 ** (TILE_MAX_ZOOM - z); // image px per tile
  const origin = 2 ** (z - 1);
  const x0 = px[0] - (cssW / 2) * imgPerCss, y0 = px[1] - (cssH / 2) * imgPerCss;
  const x1 = px[0] + (cssW / 2) * imgPerCss, y1 = px[1] + (cssH / 2) * imgPerCss;
  const nTx = Math.ceil(IMAGE_W / span), nTy = Math.ceil(IMAGE_H / span);
  const k = dpr / imgPerCss; // device px per image px

  const jobs: Promise<boolean>[] = [];
  for (let ty = Math.max(0, Math.floor(y0 / span)); ty <= Math.min(nTy - 1, Math.floor(y1 / span)); ty++) {
    for (let tx = Math.max(0, Math.floor(x0 / span)); tx <= Math.min(nTx - 1, Math.floor(x1 / span)); tx++) {
      jobs.push(loadTile(z, origin + tx, origin + ty).then((img) => {
        if (!img || canvas.dataset.token !== token) return false;
        // Round both edges so neighbouring tiles meet without hairline seams.
        const dx0 = Math.round((tx * span - x0) * k), dx1 = Math.round(((tx + 1) * span - x0) * k);
        const dy0 = Math.round((ty * span - y0) * k), dy1 = Math.round(((ty + 1) * span - y0) * k);
        ctx.drawImage(img, dx0, dy0, dx1 - dx0, dy1 - dy0);
        return true;
      }));
    }
  }
  const done = await Promise.all(jobs);
  return done.some(Boolean);
}

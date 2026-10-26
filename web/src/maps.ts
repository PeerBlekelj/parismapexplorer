// The map area: an old-map MapLibre instance (tiles of the scan on a pseudo plane), a modern
// map (OpenFreeMap), and, for overlay mode, a third non-interactive map stacked on the modern
// one that shows the scan as an image source placed with the transform (clipped for the swipe).
//
// Old ↔ modern sync goes through the transform at the view centre: position via px ↔ merc,
// zoom via the local scale, bearing via the local rotation. `anchor` is a Mercator offset that
// makes the selected place line up exactly when its real position is known.

import {
  AttributionControl, Map as MlMap, Marker, NavigationControl, setWorkerUrl,
  type GeoJSONSource, type JumpToOptions, type MapMouseEvent, type StyleSpecification,
} from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';
// MapLibre v6 loads its worker from a separate module; let Vite emit it and tell MapLibre where.
import maplibreWorkerUrl from 'maplibre-gl/dist/maplibre-gl-worker.mjs?url';
import type { FeatureCollection } from 'geojson';

import { esc, statusClass } from './format';
import { t } from './i18n';
import { modernText, type Entry } from './model';
import {
  IMAGE_BOUNDS, IMAGE_H, IMAGE_W, PLANE_MERC_M_PER_PX, TILE_MAX_ZOOM, TILE_MIN_ZOOM,
  lngLatToPx, oldZoomForScale, pxToLngLat,
} from './oldPlane';
import { lngLatToMerc, mercToLngLat, type PixelGeoTransform } from './transform';
import type { Vec2 } from './types';

export type Mode = 'side' | 'overlay' | 'old' | 'mod';
export type Orientation = 'north' | 'original';
type Which = 'old' | 'mod';

setWorkerUrl(maplibreWorkerUrl);

export const MODERN_STYLE = 'https://tiles.openfreemap.org/styles/liberty';
const BASE = `${location.origin}${import.meta.env.BASE_URL}`;
export const TILE_URL = `${BASE}tiles/old/{z}/{x}/{y}.webp`;
/** Fallback overlay: one downscaled image placed by its 4 corners with the affine fit. */
const OVERLAY_URL = `${BASE}tiles/old-overlay.webp`;

/**
 * Warped overlay tiles (Web Mercator XYZ, made by scripts/make_overlay_tiles.py), described by
 * tiles/overlay/meta.json. When that file is missing, overlay mode falls back to OVERLAY_URL.
 */
export interface OverlayTiles {
  tiles: string;
  bounds: [number, number, number, number];
  minzoom: number;
  maxzoom: number;
  controlPoints: number | null;
  medianErrorM: number | null;
}

export async function loadOverlayTiles(): Promise<OverlayTiles | null> {
  try {
    const r = await fetch(`${BASE}tiles/overlay/meta.json`, { cache: 'no-cache' });
    if (!r.ok || !(r.headers.get('content-type') ?? '').includes('json')) return null;
    const m = await r.json();
    const b = m.bounds;
    if (!Array.isArray(b) || b.length !== 4 || !b.every((v: unknown) => Number.isFinite(v))) return null;
    const num = (v: unknown, d: number) => (Number.isFinite(v) ? (v as number) : d);
    const rel = typeof m.tiles === 'string' && m.tiles.includes('{z}') ? m.tiles.replace(/^\/+/, '') : 'tiles/overlay/{z}/{x}/{y}.webp';
    return {
      tiles: `${BASE}${rel}`,
      bounds: [b[0], b[1], b[2], b[3]],
      minzoom: num(m.minzoom, 13),
      maxzoom: num(m.maxzoom, 17),
      controlPoints: Number.isFinite(m.control_points) ? m.control_points : null,
      medianErrorM: Number.isFinite(m.median_error_m) ? m.median_error_m : null,
    };
  } catch {
    return null;
  }
}

/** CSS px per image px when flying to a place. */
const SELECT_SCALE = 0.5;
const PAPER = '#d6c9ad';
const OLD_MIN_ZOOM = 7.6;
const OLD_MAX_ZOOM = TILE_MAX_ZOOM + 0.8;
/** Zoom (old map) from which all places are drawn as small rings. */
const OLD_DOTS_ZOOM = 11.2;
const MOD_DOTS_ZOOM = 15.3;

export interface MapCallbacks {
  onPick(id: string, source: Which): void;
}

export class MapView {
  readonly old: MlMap;
  readonly mod: MlMap;
  ovl: MlMap | null = null;
  mode: Mode = 'side';
  orientation: Orientation = 'north';

  private T: PixelGeoTransform;
  private entries: Entry[];
  private candidates: Entry[];
  private filterActive = false;
  private selected: Entry | null = null;
  private syncing = false;
  private anchor: Vec2 = [0, 0];
  private opacity = 0.8;
  private swipe = 50;
  private zoomOffset: number; // modern zoom − old zoom at the image centre
  private ovlEl: HTMLElement;
  private overlayTiles: OverlayTiles | null;
  private tooltip: HTMLElement;
  private cb: MapCallbacks;
  private pins: Record<'old' | 'mod' | 'ovl', Marker>;

  constructor(
    els: { old: HTMLElement; mod: HTMLElement; ovl: HTMLElement; tooltip: HTMLElement },
    T: PixelGeoTransform,
    entries: Entry[],
    cb: MapCallbacks,
    initial: Entry | null,
    overlayTiles: OverlayTiles | null,
  ) {
    this.overlayTiles = overlayTiles;
    this.T = T;
    this.entries = entries;
    this.candidates = entries;
    this.cb = cb;
    this.ovlEl = els.ovl;
    this.tooltip = els.tooltip;
    const centre: Vec2 = [IMAGE_W / 2, IMAGE_H / 2];
    const z0 = Math.log2(PLANE_MERC_M_PER_PX / T.local(centre).scale);
    this.zoomOffset = Number.isFinite(z0) ? z0 : 4;

    if (initial) this.setAnchorFor(initial);
    const oldCam = initial
      ? { center: initial.oldLL, zoom: oldZoomForScale(SELECT_SCALE), bearing: this.targetOldBearing() }
      : this.fitOldCamera(els.old);

    const oldStyle: StyleSpecification = {
      version: 8,
      sources: {
        old: {
          type: 'raster', tiles: [TILE_URL], tileSize: 256,
          minzoom: TILE_MIN_ZOOM, maxzoom: TILE_MAX_ZOOM, bounds: IMAGE_BOUNDS,
          attribution: t.oldAttribution,
        },
      },
      layers: [
        { id: 'paper', type: 'background', paint: { 'background-color': PAPER } },
        { id: 'old', type: 'raster', source: 'old', paint: { 'raster-fade-duration': 120 } },
      ],
    };
    this.old = new MlMap({
      container: els.old,
      style: oldStyle,
      ...oldCam,
      renderWorldCopies: false,
      trackResize: false,
      minZoom: OLD_MIN_ZOOM,
      maxZoom: OLD_MAX_ZOOM,
      attributionControl: false,
      dragRotate: false,
      pitchWithRotate: false,
      touchPitch: false,
      maxPitch: 0,
    });
    this.mod = new MlMap({
      container: els.mod,
      style: MODERN_STYLE,
      trackResize: false,
      ...this.camOldToMod(oldCam.center, oldCam.zoom, oldCam.bearing),
      maxZoom: 19.5,
      attributionControl: false,
      dragRotate: false,
      pitchWithRotate: false,
      touchPitch: false,
      maxPitch: 0,
    });
    for (const m of [this.old, this.mod]) {
      m.touchZoomRotate.disableRotation();
      m.keyboard.disableRotation();
      m.addControl(new NavigationControl({ showCompass: false }), 'bottom-right');
      m.addControl(new AttributionControl({ compact: true }), 'bottom-right');
    }

    this.pins = { old: this.makePin('old'), mod: this.makePin('mod'), ovl: this.makePin('mod') };

    this.old.on('move', () => this.syncFrom('old'));
    this.mod.on('move', () => this.syncFrom('mod'));
    this.old.on('load', () => this.addDots('old'));
    this.mod.on('load', () => this.addDots('mod'));
    this.bindPointer(this.old, 'old');
    this.bindPointer(this.mod, 'mod');
    let raf = 0;
    window.addEventListener('resize', () => {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => this.resize());
    });
  }

  // ---------- camera maths ----------

  /**
   * Modern zoom − old zoom at an image point: matches ground scale using the local scale of
   * the transform, clamped so a spline extrapolating far off the map cannot run away.
   */
  private zoomDelta(px: Vec2): number {
    const d = Math.log2(PLANE_MERC_M_PER_PX / this.T.local(px).scale);
    return Number.isFinite(d) ? Math.max(this.zoomOffset - 1, Math.min(this.zoomOffset + 1, d)) : this.zoomOffset;
  }

  // Rotation is synced with ONE overall bearing (T.bearing), not the spline's local rotation,
  // so neither map turns while the other is panned.
  private camOldToMod(centre: Vec2, zoom: number, bearing: number): JumpToOptions {
    const px = lngLatToPx(centre);
    const m = this.T.pxToMerc(px);
    return {
      center: mercToLngLat([m[0] + this.anchor[0], m[1] + this.anchor[1]]),
      zoom: zoom + this.zoomDelta(px),
      bearing: bearing + this.T.bearing,
      pitch: 0,
    };
  }

  private camModToOld(centre: Vec2, zoom: number, bearing: number): JumpToOptions {
    const m = lngLatToMerc(centre);
    const px = this.T.mercToPx([m[0] - this.anchor[0], m[1] - this.anchor[1]]);
    return {
      center: pxToLngLat(px),
      zoom: zoom - this.zoomDelta(px),
      bearing: bearing - this.T.bearing,
      pitch: 0,
    };
  }

  private targetOldBearing(): number {
    return this.orientation === 'north' ? -this.T.bearing : 0;
  }

  private targetModBearing(): number {
    return this.orientation === 'north' ? 0 : this.T.bearing;
  }

  /** Fit the whole sheet in a container, rotated for the current orientation. */
  private fitOldCamera(el: HTMLElement): { center: Vec2; zoom: number; bearing: number } {
    const c: Vec2 = [IMAGE_W / 2, IMAGE_H / 2];
    const bearing = this.targetOldBearing();
    const b = (bearing * Math.PI) / 180;
    const bw = Math.abs(IMAGE_W * Math.cos(b)) + Math.abs(IMAGE_H * Math.sin(b));
    const bh = Math.abs(IMAGE_W * Math.sin(b)) + Math.abs(IMAGE_H * Math.cos(b));
    const w = Math.max(200, el.clientWidth - 40), h = Math.max(200, el.clientHeight - 100);
    // The rotated sheet leaves empty corners; zoom in a little past the exact fit.
    const zoom = oldZoomForScale(Math.min(w / bw, h / bh)) + 0.8;
    return { center: pxToLngLat(c), zoom: Math.max(OLD_MIN_ZOOM, zoom), bearing };
  }

  private primary(): Which {
    return this.mode === 'side' || this.mode === 'old' ? 'old' : 'mod';
  }

  /** Make the other map(s) follow `src`. */
  private syncFrom(src: Which): void {
    if (this.syncing) return;
    this.syncing = true;
    try {
      if (src === 'old') {
        const c = this.old.getCenter();
        this.mod.jumpTo(this.camOldToMod([c.lng, c.lat], this.old.getZoom(), this.old.getBearing()));
      } else {
        const c = this.mod.getCenter();
        this.old.jumpTo(this.camModToOld([c.lng, c.lat], this.mod.getZoom(), this.mod.getBearing()));
      }
      if (this.ovl) {
        this.ovl.jumpTo({ center: this.mod.getCenter(), zoom: this.mod.getZoom(), bearing: this.mod.getBearing(), pitch: 0 });
      }
    } finally {
      this.syncing = false;
    }
  }

  private setAnchorFor(e: Entry | null): void {
    if (e && e.geoKind !== 'estimated') {
      const real = lngLatToMerc(e.geo), fit = this.T.pxToMerc(e.px);
      this.anchor = [real[0] - fit[0], real[1] - fit[1]];
    } else {
      this.anchor = [0, 0];
    }
  }

  // ---------- modes and orientation ----------

  setMode(mode: Mode): void {
    const from = this.primary();
    this.mode = mode;
    if (mode === 'overlay') this.ensureOverlay();
    // Warped tiles start at tile zoom `minzoom` (= map zoom minzoom − 1 for 256-px tiles); don't
    // let the modern map zoom out past that in overlay mode, or the old map would vanish.
    this.mod.setMinZoom(mode === 'overlay' && this.overlayTiles ? this.overlayTiles.minzoom - 1 : null);
    // The caller has already switched the CSS; containers have their new sizes now.
    this.resizeVisible();
    this.syncFrom(from);
    this.updatePins();
    this.hideTooltip();
  }

  setOrientation(o: Orientation): void {
    this.orientation = o;
    const p = this.primary();
    if (p === 'old') this.old.easeTo({ bearing: this.targetOldBearing(), duration: 700 });
    else this.mod.easeTo({ bearing: this.targetModBearing(), duration: 700 });
  }

  /** Called after the map area becomes visible again (e.g. back from the table view). */
  resize(): void {
    this.resizeVisible();
    this.syncFrom(this.primary());
  }

  /**
   * Resize only maps whose container is visible: resizing a hidden (0×0) map shifts its
   * centre, which then drifts the other map on the next sync.
   */
  private resizeVisible(): void {
    // resize() fires 'move'; don't let that sync through the spline's inverse (the forward and
    // inverse fits are not exact inverses, so a round trip would shift the view a little).
    const was = this.syncing;
    this.syncing = true;
    try {
      for (const m of [this.old, this.mod, this.ovl]) {
        if (m && m.getContainer().offsetWidth > 0) m.resize();
      }
    } finally {
      this.syncing = was;
    }
  }

  // ---------- overlay ----------

  private ensureOverlay(): void {
    if (this.ovl) return;
    const corners = ([[0, 0], [IMAGE_W, 0], [IMAGE_W, IMAGE_H], [0, IMAGE_H]] as Vec2[])
      .map((p) => this.T.affinePxToLngLat(p)) as [Vec2, Vec2, Vec2, Vec2];
    const ot = this.overlayTiles;
    const source: StyleSpecification['sources'][string] = ot
      ? { type: 'raster', tiles: [ot.tiles], tileSize: 256, minzoom: ot.minzoom, maxzoom: ot.maxzoom, bounds: ot.bounds }
      : { type: 'image', url: OVERLAY_URL, coordinates: corners };
    this.ovl = new MlMap({
      container: this.ovlEl,
      interactive: false,
      trackResize: false,
      attributionControl: false,
      renderWorldCopies: false,
      maxZoom: 24,
      center: this.mod.getCenter(),
      zoom: this.mod.getZoom(),
      bearing: this.mod.getBearing(),
      style: {
        version: 8,
        sources: { img: source },
        layers: [{ id: 'img', type: 'raster', source: 'img', paint: { 'raster-opacity': this.opacity, 'raster-fade-duration': 0 } }],
      },
    });
    this.setSwipe(this.swipe);
  }

  setOpacity(v: number): void {
    this.opacity = v;
    if (this.ovl?.isStyleLoaded()) this.ovl.setPaintProperty('img', 'raster-opacity', v);
    else this.ovl?.once('load', () => this.ovl?.setPaintProperty('img', 'raster-opacity', this.opacity));
  }

  /** Percentage of the width (from the left) where the old map stops. */
  setSwipe(pct: number): void {
    this.swipe = pct;
    this.ovlEl.style.clipPath = `inset(0 ${100 - pct}% 0 0)`;
  }

  // ---------- selection and pins ----------

  private makePin(kind: 'old' | 'mod'): Marker {
    const el = document.createElement('div');
    el.className = kind === 'old' ? 'pin pin-old' : 'pin pin-mod';
    el.innerHTML = '<span class="pin-halo"></span><span class="pin-dot"></span><span class="pin-tag"></span>';
    return new Marker({ element: el, anchor: 'center' });
  }

  private updatePins(): void {
    const e = this.selected;
    if (!e) {
      Object.values(this.pins).forEach((m) => m.remove());
      return;
    }
    const gone = e.place.status === 'vanished';
    // On the 1550 map every place existed: always a solid ring there.
    this.pins.old.setLngLat(e.oldLL).addTo(this.old);
    const modPins: [Marker, MlMap | null][] = [[this.pins.mod, this.mod], [this.pins.ovl, this.ovl]];
    for (const [pin, map] of modPins) {
      if (!map) continue;
      const el = pin.getElement();
      el.classList.toggle('gone', gone);
      el.classList.toggle('halo', e.geoKind !== 'exact');
      el.classList.toggle('est', e.geoKind === 'estimated');
      const tag = t.pinTags[e.geoKind] ?? '';
      const tagEl = el.querySelector('.pin-tag') as HTMLElement;
      tagEl.textContent = tag;
      tagEl.hidden = !tag;
      pin.setLngLat(e.geo).addTo(map);
    }
  }

  /** Select a place. `fly` moves the camera; `source` = the map that was clicked, if any. */
  select(e: Entry | null, opts: { fly: boolean; source?: Which; instant?: boolean }): void {
    this.selected = e;
    this.setAnchorFor(e);
    this.updatePins();
    if (!e) return;
    if (!opts.fly) {
      this.syncFrom(opts.source ?? this.primary());
      return;
    }
    const p = this.primary();
    const selZoomOld = oldZoomForScale(SELECT_SCALE);
    if (p === 'old') {
      const cam = { center: e.oldLL, zoom: Math.max(this.old.getZoom(), selZoomOld), bearing: this.targetOldBearing() };
      if (opts.instant) this.old.jumpTo(cam);
      else this.old.flyTo({ ...cam, maxDuration: 2500 });
    } else {
      const cam = {
        center: e.geo,
        zoom: Math.max(this.mod.getZoom(), selZoomOld + this.zoomDelta(e.px)),
        bearing: this.targetModBearing(),
      };
      if (opts.instant) this.mod.jumpTo(cam);
      else this.mod.flyTo({ ...cam, maxDuration: 2500 });
    }
  }

  // ---------- dots for places ----------

  setFilter(results: Entry[], active: boolean): void {
    this.filterActive = active;
    this.candidates = active ? results : this.entries;
    this.refreshDots('old');
    this.refreshDots('mod');
  }

  private dotsData(which: Which): FeatureCollection {
    return {
      type: 'FeatureCollection',
      features: this.candidates.map((e) => ({
        type: 'Feature',
        geometry: { type: 'Point', coordinates: which === 'old' ? e.oldLL : e.geo },
        properties: { id: e.place.id, status: statusClass(e.place.status), kind: e.geoKind },
      })),
    };
  }

  private addDots(which: Which): void {
    const map = which === 'old' ? this.old : this.mod;
    if (map.getSource('places')) return;
    map.addSource('places', { type: 'geojson', data: this.dotsData(which) });
    const colour = ['match', ['get', 'status'], 'vanished', '#8a6d4a', 'unknown', '#6b5a48', '#a63a1f'];
    if (which === 'old') {
      map.addLayer({
        id: 'dots', type: 'circle', source: 'places',
        paint: {
          'circle-radius': ['interpolate', ['linear'], ['zoom'], 9, 3, 12, 5, 14, 7],
          'circle-color': 'rgba(0,0,0,0)',
          'circle-stroke-color': colour as never,
          'circle-stroke-width': ['interpolate', ['linear'], ['zoom'], 9, 1.5, 13, 2.5],
        },
      });
    } else {
      map.addLayer({
        id: 'dots', type: 'circle', source: 'places',
        paint: {
          'circle-radius': ['interpolate', ['linear'], ['zoom'], 12, 3, 17, 6],
          'circle-color': ['case', ['==', ['get', 'kind'], 'estimated'], 'rgba(255,250,240,0.6)', colour] as never,
          'circle-stroke-color': colour as never,
          'circle-stroke-width': 1.5,
        },
      });
    }
    this.refreshDots(which);
  }

  private refreshDots(which: Which): void {
    const map = which === 'old' ? this.old : this.mod;
    const src = map.getSource('places') as GeoJSONSource | undefined;
    if (!src) return;
    src.setData(this.dotsData(which));
    const z0 = which === 'old' ? OLD_DOTS_ZOOM : MOD_DOTS_ZOOM;
    const op = this.filterActive ? 0.9 : ['interpolate', ['linear'], ['zoom'], z0 - 0.6, 0, z0, 0.85];
    map.setPaintProperty('dots', 'circle-stroke-opacity', op as never);
    map.setPaintProperty('dots', 'circle-opacity', op as never);
  }

  // ---------- picking places by pointer ----------

  private pickRadius(which: Which): number {
    if (which === 'mod') return 26;
    // Labels are long: allow more slack as one zooms in on the scan.
    const scale = 2 ** (this.old.getZoom() - TILE_MAX_ZOOM + 1);
    return Math.max(24, Math.min(140, 150 * scale));
  }

  private nearest(which: Which, x: number, y: number): Entry | null {
    const map = which === 'old' ? this.old : this.mod;
    const r = this.pickRadius(which);
    let best: Entry | null = null;
    let bd = r * r;
    for (const e of this.candidates) {
      const p = map.project(which === 'old' ? e.oldLL : e.geo);
      const d = (p.x - x) ** 2 + (p.y - y) ** 2;
      if (d < bd) {
        bd = d;
        best = e;
      }
    }
    return best;
  }

  private bindPointer(map: MlMap, which: Which): void {
    let raf = 0;
    map.on('mousemove', (ev: MapMouseEvent) => {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        const e = this.nearest(which, ev.point.x, ev.point.y);
        map.getCanvas().style.cursor = e ? 'pointer' : '';
        if (e) this.showTooltip(e, ev.originalEvent);
        else this.hideTooltip();
      });
    });
    map.on('mouseout', () => {
      cancelAnimationFrame(raf);
      this.hideTooltip();
    });
    map.on('movestart', () => this.hideTooltip());
    map.on('click', (ev: MapMouseEvent) => {
      const e = this.nearest(which, ev.point.x, ev.point.y);
      if (e) this.cb.onPick(e.place.id, which);
    });
  }

  private showTooltip(e: Entry, me: MouseEvent): void {
    const m = modernText(e.place);
    this.tooltip.innerHTML =
      `<span class="tt-old">${esc(e.title)}</span><span class="tt-mod${m.placeholder ? ' placeholder' : ''}">${esc(m.text)}</span>`;
    this.tooltip.style.transform = `translate(${me.clientX + 14}px, ${me.clientY + 12}px)`;
    this.tooltip.hidden = false;
  }

  private hideTooltip(): void {
    this.tooltip.hidden = true;
  }
}

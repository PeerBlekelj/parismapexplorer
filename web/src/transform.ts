// Old-map pixel ↔ real-world transform, fitted at load time from gcps.json.
//
// Main transform: a thin-plate spline (TPS), mirroring `tps_fit` in scripts/fit_transform.py:
//   - inputs normalised by subtracting the mean and dividing by ONE overall standard deviation
//   - kernel U(r) = r² log r plus an affine term, λ = 0.2 added to the kernel diagonal
//   - two independent fits: pixel → (lat, lon), and (lat, lon·cos φ0) → pixel
// With fewer than MIN_TPS_POINTS control points it falls back to a least-squares affine.
//
// An affine fit in EPSG:3857 metres is always kept as well: it places the four corners of the
// overlay image (an image source needs a quadrilateral) and gives a stable overall rotation.
//
// The rest of the app only sees `PixelGeoTransform`.

import type { Gcp, Vec2 } from './types';

export interface Mapping { apply(p: Vec2): Vec2 }

export interface Residual { id: string; name: string; meters: number }

export interface LocalFrame {
  /** EPSG:3857 metres per image pixel (geometric mean of the two axes). */
  scale: number;
  /** Geographic bearing (degrees clockwise from north) of "up" on the printed map, here. */
  bearing: number;
}

export interface PixelGeoTransform {
  kind: 'affine' | 'tps';
  /** Number of control points used. */
  n: number;
  /** Typical ground error of this transform: median leave-one-out error, metres. */
  errorMeters: number;
  /** The same for the affine that places the overlay image. */
  affineErrorMeters: number;
  /** In-sample residuals (smaller than the real error for a spline). */
  residuals: Residual[];
  /** Overall bearing of "up" on the print (from the affine): stable for syncing rotation. */
  bearing: number;
  pxToMerc(p: Vec2): Vec2;
  mercToPx(m: Vec2): Vec2;
  pxToLngLat(p: Vec2): Vec2;
  lngLatToPx(ll: Vec2): Vec2;
  /** Affine placement, for the four corners of the overlay image. */
  affinePxToLngLat(p: Vec2): Vec2;
  local(p: Vec2): LocalFrame;
}

export const TPS_LAMBDA = 0.2;
export const MIN_TPS_POINTS = 6;
/** Leave-one-out is computed for at most this many points (evenly spread), to keep load fast. */
const MAX_LOO = 40;

// ---------- Web Mercator helpers ----------

const R = 6378137;
const D2R = Math.PI / 180;
const M_PER_DEG = 111195; // metres per degree of latitude (mean Earth radius)

export function lngLatToMerc(ll: Vec2): Vec2 {
  return [ll[0] * D2R * R, R * Math.log(Math.tan(Math.PI / 4 + (ll[1] * D2R) / 2))];
}

export function mercToLngLat(m: Vec2): Vec2 {
  return [m[0] / R / D2R, (2 * Math.atan(Math.exp(m[1] / R)) - Math.PI / 2) / D2R];
}

/** Ground distance in metres between two [lng, lat] points (equirectangular, fine at city scale). */
function groundDist(a: Vec2, b: Vec2): number {
  const cos = Math.cos(((a[1] + b[1]) / 2) * D2R);
  return Math.hypot((a[0] - b[0]) * M_PER_DEG * cos, (a[1] - b[1]) * M_PER_DEG);
}

// ---------- linear algebra ----------

/** Solve A·X = B (A n×n, B n×k) by Gaussian elimination with partial pivoting. A and B are consumed. */
function solve(A: Float64Array[], B: Float64Array[]): Float64Array[] {
  const n = A.length, k = B[0].length;
  for (let i = 0; i < n; i++) {
    let piv = i;
    for (let r = i + 1; r < n; r++) if (Math.abs(A[r][i]) > Math.abs(A[piv][i])) piv = r;
    if (Math.abs(A[piv][i]) < 1e-12) throw new Error('Singular system: control points collinear or duplicated');
    if (piv !== i) {
      [A[i], A[piv]] = [A[piv], A[i]];
      [B[i], B[piv]] = [B[piv], B[i]];
    }
    const ai = A[i], bi = B[i], d = ai[i];
    for (let r = i + 1; r < n; r++) {
      const ar = A[r];
      const f = ar[i] / d;
      if (f === 0) continue;
      for (let c = i; c < n; c++) ar[c] -= f * ai[c];
      for (let c = 0; c < k; c++) B[r][c] -= f * bi[c];
    }
  }
  const X = Array.from({ length: n }, () => new Float64Array(k));
  for (let i = n - 1; i >= 0; i--) {
    for (let c = 0; c < k; c++) {
      let s = B[i][c];
      for (let j = i + 1; j < n; j++) s -= A[i][j] * X[j][c];
      X[i][c] = s / A[i][i];
    }
  }
  return X;
}

// ---------- affine (least squares) ----------

class AffineMapping implements Mapping {
  // dst = [a0 + a1*x + a2*y, b0 + b1*x + b2*y]
  readonly a: [number, number, number];
  readonly b: [number, number, number];
  constructor(a: [number, number, number], b: [number, number, number]) {
    this.a = a;
    this.b = b;
  }

  apply(p: Vec2): Vec2 {
    const [a0, a1, a2] = this.a, [b0, b1, b2] = this.b;
    return [a0 + a1 * p[0] + a2 * p[1], b0 + b1 * p[0] + b2 * p[1]];
  }

  inverse(): AffineMapping {
    const [a0, a1, a2] = this.a, [b0, b1, b2] = this.b;
    const det = a1 * b2 - a2 * b1;
    if (Math.abs(det) < 1e-300) throw new Error('Degenerate affine transform');
    const i11 = b2 / det, i12 = -a2 / det, i21 = -b1 / det, i22 = a1 / det;
    return new AffineMapping([-(i11 * a0 + i12 * b0), i11, i12], [-(i21 * a0 + i22 * b0), i21, i22]);
  }
}

/** Least-squares affine src → dst. Data are centred and scaled for conditioning. */
export function fitAffine(src: Vec2[], dst: Vec2[]): AffineMapping {
  const n = src.length;
  if (n < 3) throw new Error(`Need at least 3 control points, got ${n}`);
  const mean = (v: Vec2[], k: 0 | 1) => v.reduce((s, p) => s + p[k], 0) / n;
  const sx = mean(src, 0), sy = mean(src, 1), dx = mean(dst, 0), dy = mean(dst, 1);
  const k = 1000;
  const rows = src.map((p) => [1, (p[0] - sx) / k, (p[1] - sy) / k]);
  const AtA = [0, 1, 2].map((i) => Float64Array.from([0, 1, 2], (j) => rows.reduce((s, r) => s + r[i] * r[j], 0)));
  const AtB = [0, 1, 2].map((i) => Float64Array.from([0, 1], (c) =>
    rows.reduce((s, r, idx) => s + r[i] * (dst[idx][c] - (c === 0 ? dx : dy)), 0)));
  const X = solve(AtA, AtB);
  const un = (c: number, d: number): [number, number, number] => {
    const c1 = X[1][c] / k, c2 = X[2][c] / k;
    return [d + X[0][c] - c1 * sx - c2 * sy, c1, c2];
  };
  return new AffineMapping(un(0, dx), un(1, dy));
}

// ---------- thin-plate spline ----------

function tpsU(d: number): number {
  return d > 0 ? d * d * Math.log(d + 1e-12) : 0;
}

/** Thin-plate spline from points P (n×2) to values V (n×2). Mirrors `tps_fit` in fit_transform.py. */
export function fitTps(P: Vec2[], V: Vec2[], lam: number = TPS_LAMBDA): Mapping {
  const n = P.length;
  // One overall standard deviation over all 2n coordinates (numpy's P.std()).
  let gm = 0;
  for (const p of P) gm += p[0] + p[1];
  gm /= 2 * n;
  let ss = 0;
  for (const p of P) ss += (p[0] - gm) ** 2 + (p[1] - gm) ** 2;
  const s = Math.sqrt(ss / (2 * n)) || 1;
  const mx = P.reduce((a, p) => a + p[0], 0) / n;
  const my = P.reduce((a, p) => a + p[1], 0) / n;
  const Q = P.map((p) => [(p[0] - mx) / s, (p[1] - my) / s] as Vec2);

  const N = n + 3;
  const A = Array.from({ length: N }, () => new Float64Array(N));
  const B = Array.from({ length: N }, () => new Float64Array(2));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      A[i][j] = tpsU(Math.hypot(Q[i][0] - Q[j][0], Q[i][1] - Q[j][1])) + (i === j ? lam : 0);
    }
    A[i][n] = 1; A[i][n + 1] = Q[i][0]; A[i][n + 2] = Q[i][1];
    A[n][i] = 1; A[n + 1][i] = Q[i][0]; A[n + 2][i] = Q[i][1];
    B[i][0] = V[i][0]; B[i][1] = V[i][1];
  }
  const W = solve(A, B);

  return {
    apply(p: Vec2): Vec2 {
      const zx = (p[0] - mx) / s, zy = (p[1] - my) / s;
      let o0 = W[n][0] + W[n + 1][0] * zx + W[n + 2][0] * zy;
      let o1 = W[n][1] + W[n + 1][1] * zx + W[n + 2][1] * zy;
      for (let i = 0; i < n; i++) {
        const u = tpsU(Math.hypot(zx - Q[i][0], zy - Q[i][1]));
        o0 += u * W[i][0];
        o1 += u * W[i][1];
      }
      return [o0, o1];
    },
  };
}

// ---------- the transform ----------

interface Fitted { pxToLngLat(p: Vec2): Vec2; lngLatToPx(ll: Vec2): Vec2 }

function fitAffineLL(px: Vec2[], ll: Vec2[]): Fitted & { fwd: AffineMapping } {
  const fwd = fitAffine(px, ll.map(lngLatToMerc));
  const inv = fwd.inverse();
  return {
    fwd,
    pxToLngLat: (p) => mercToLngLat(fwd.apply(p)),
    lngLatToPx: (l) => inv.apply(lngLatToMerc(l)),
  };
}

function fitTpsLL(px: Vec2[], ll: Vec2[]): Fitted {
  const lat0 = ll.reduce((a, l) => a + l[1], 0) / ll.length;
  const c = Math.cos(lat0 * D2R); // equalise lon and lat units for the inverse fit
  const fwd = fitTps(px, ll.map((l) => [l[1], l[0]] as Vec2));           // px → (lat, lon)
  const inv = fitTps(ll.map((l) => [l[1], l[0] * c] as Vec2), px);       // (lat, lon·c) → px

  // The two regularised splines are not exact inverses of each other (≈ 50 m apart with 20
  // points), so syncing old → modern → old would creep. The inverse spline gives the starting
  // point; a few Newton steps on the forward spline make the round trip exact.
  const lngLatToPx = (l: Vec2): Vec2 => {
    const p0 = inv.apply([l[1], l[0] * c]);
    let p: Vec2 = [p0[0], p0[1]];
    const resid = (q: Vec2): Vec2 => {
      const v = fwd.apply(q);
      return [(v[1] - l[0]) * c, v[0] - l[1]]; // (east, north) in degrees of latitude
    };
    let r = resid(p);
    for (let k = 0; k < 8 && Math.hypot(r[0], r[1]) > 1e-9; k++) {
      const h = 1;
      const rx = resid([p[0] + h, p[1]]), ry = resid([p[0], p[1] + h]);
      const a = (rx[0] - r[0]) / h, b = (ry[0] - r[0]) / h, cc = (rx[1] - r[1]) / h, d = (ry[1] - r[1]) / h;
      const det = a * d - b * cc;
      if (!Number.isFinite(det) || Math.abs(det) < 1e-24) return p0;
      p = [p[0] - (d * r[0] - b * r[1]) / det, p[1] - (-cc * r[0] + a * r[1]) / det];
      r = resid(p);
    }
    return Number.isFinite(p[0]) && Number.isFinite(p[1]) && Math.hypot(r[0], r[1]) < 1e-6 ? p : p0;
  };

  return {
    pxToLngLat: (p) => {
      const v = fwd.apply(p);
      return [v[1], v[0]];
    },
    lngLatToPx,
  };
}

/** Median leave-one-out ground error (metres) for a fitting method. */
function looMedian(px: Vec2[], ll: Vec2[], fit: (px: Vec2[], ll: Vec2[]) => Fitted): number {
  const n = px.length;
  if (n < 4) return NaN;
  const m = Math.min(n, MAX_LOO);
  const errs: number[] = [];
  for (let k = 0; k < m; k++) {
    const i = Math.floor((k * n) / m);
    try {
      const f = fit(px.filter((_, j) => j !== i), ll.filter((_, j) => j !== i));
      errs.push(groundDist(f.pxToLngLat(px[i]), ll[i]));
    } catch {
      /* a degenerate subset: skip */
    }
  }
  errs.sort((a, b) => a - b);
  return errs.length ? errs[Math.floor(errs.length / 2)] : NaN;
}

export function createTransform(gcps: Gcp[]): PixelGeoTransform {
  // quality "label" and "place" are treated the same.
  const usable = gcps.filter((g) =>
    Array.isArray(g.px) && Number.isFinite(g.px[0]) && Number.isFinite(g.px[1]) &&
    Number.isFinite(g.lat) && Number.isFinite(g.lon));
  const px = usable.map((g) => [g.px[0], g.px[1]] as Vec2);
  const ll = usable.map((g) => [g.lon, g.lat] as Vec2);

  const affine = fitAffineLL(px, ll);
  const kind: 'affine' | 'tps' = usable.length >= MIN_TPS_POINTS ? 'tps' : 'affine';
  const main: Fitted = kind === 'tps' ? fitTpsLL(px, ll) : affine;

  const residuals: Residual[] = usable.map((g, i) => ({
    id: g.id, name: g.name, meters: groundDist(main.pxToLngLat(px[i]), ll[i]),
  }));
  const affineErrorMeters = looMedian(px, ll, fitAffineLL);
  const errorMeters = kind === 'tps' ? looMedian(px, ll, fitTpsLL) : affineErrorMeters;

  const pxToMerc = (p: Vec2) => lngLatToMerc(main.pxToLngLat(p));

  const frame = (f: (p: Vec2) => Vec2, p: Vec2): LocalFrame => {
    const h = 20;
    const ex0 = f([p[0] - h, p[1]]), ex1 = f([p[0] + h, p[1]]);
    const ey0 = f([p[0], p[1] - h]), ey1 = f([p[0], p[1] + h]);
    // Jacobian in "plane" axes: (image right, image up) → (merc east, merc north)
    const a = (ex1[0] - ex0[0]) / (2 * h), c = (ex1[1] - ex0[1]) / (2 * h);
    const b = -(ey1[0] - ey0[0]) / (2 * h), d = -(ey1[1] - ey0[1]) / (2 * h);
    const scale = Math.sqrt(Math.abs(a * d - b * c));
    const phi = Math.atan2(c - b, a + d) / D2R; // closest rotation (polar decomposition), CCW
    return { scale, bearing: -phi };
  };
  const bearing = frame((p) => affine.fwd.apply(p), [0, 0]).bearing;

  if (kind === 'tps') console.info(`transform: TPS through ${usable.length} points, median LOO error ${Math.round(errorMeters)} m (affine ${Math.round(affineErrorMeters)} m)`);
  else console.info(`transform: affine through ${usable.length} points (fewer than ${MIN_TPS_POINTS} for a spline)`);

  return {
    kind,
    n: usable.length,
    errorMeters: Number.isFinite(errorMeters) ? errorMeters : 0,
    affineErrorMeters: Number.isFinite(affineErrorMeters) ? affineErrorMeters : 0,
    residuals,
    bearing,
    pxToMerc,
    mercToPx: (m) => main.lngLatToPx(mercToLngLat(m)),
    pxToLngLat: (p) => main.pxToLngLat(p),
    lngLatToPx: (l) => main.lngLatToPx(l),
    affinePxToLngLat: (p) => affine.pxToLngLat(p),
    local: (p) => frame(pxToMerc, p),
  };
}

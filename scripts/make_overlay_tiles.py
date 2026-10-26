"""Warp the old map onto Web Mercator raster tiles with a thin-plate spline.

For every output pixel: tile pixel -> lat/lon -> (inverse TPS) -> source-image pixel -> bilinear
sample. Control points: data/gcps_auto.csv. The overlay is clipped to the convex hull of the
control points (grown by HULL_GROW px): outside it the spline only extrapolates.
Output: web/public/tiles/overlay/{z}/{x}/{y}.webp (transparent outside the clip), plus
web/public/tiles/overlay/meta.json with the bounds and zoom range.
"""
import csv, json, math, sys
from pathlib import Path
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
root = Path(sys.argv[1])
ZMIN, ZMAX, LAM, HULL_GROW = 11, 17, 0.2, 900
out_dir = root / "web/public/tiles/overlay"

g = list(csv.DictReader(open(root / "data/gcps_auto.csv")))
P = np.array([[float(r["x"]), float(r["y"])] for r in g])
LL = np.array([[float(r["lat"]), float(r["lon"])] for r in g])
COS = math.cos(math.radians(LL[:, 0].mean()))

def tps(src, dst, lam):
    mu, s = src.mean(0), src.std()
    Q = (src - mu) / s
    n = len(Q)
    d = np.linalg.norm(Q[:, None] - Q[None], axis=2)
    K = np.where(d > 0, d ** 2 * np.log(d + 1e-12), 0) + lam * np.eye(n)
    Pm = np.hstack([np.ones((n, 1)), Q])
    A = np.zeros((n + 3, n + 3)); A[:n, :n] = K; A[:n, n:] = Pm; A[n:, :n] = Pm.T
    b = np.zeros((n + 3, dst.shape[1])); b[:n] = dst
    w = np.linalg.solve(A, b)
    def f(X):
        Z = (X - mu) / s
        out = np.hstack([np.ones((len(Z), 1)), Z]) @ w[n:]
        for i in range(n):  # loop over control points keeps memory small
            r = np.linalg.norm(Z - Q[i], axis=1)
            out += np.where(r > 0, r ** 2 * np.log(r + 1e-12), 0)[:, None] * w[i]
        return out
    return f

# inverse: (lat, lon*cos) -> pixel
ll2px = tps(np.c_[LL[:, 0], LL[:, 1] * COS], P, LAM)

# clip polygon: convex hull of the control-point pixels, grown outward
def hull(pts):
    pts = sorted(map(tuple, pts))
    def half(seq):
        h = []
        for p in seq:
            while len(h) >= 2 and (h[-1][0] - h[-2][0]) * (p[1] - h[-2][1]) - (h[-1][1] - h[-2][1]) * (p[0] - h[-2][0]) <= 0:
                h.pop()
            h.append(p)
        return h
    return np.array(half(pts)[:-1] + half(pts[::-1])[:-1])
H = hull(P)
c = H.mean(0)
H = c + (H - c) * (1 + HULL_GROW / np.linalg.norm(H - c, axis=1, keepdims=True))

def inside(X, poly):
    x, y = X[:, 0], X[:, 1]
    res = np.zeros(len(X), bool)
    j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i]; xj, yj = poly[j]
        cross = ((yi > y) != (yj > y)) & (x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi)
        res ^= cross
        j = i
    return res

# lat/lon bounds of the clip region (forward map of the hull, via a dense sample)
px2ll = tps(P, np.c_[LL[:, 0], LL[:, 1] * COS], LAM)
edge = np.vstack([np.linspace(H[i], H[(i + 1) % len(H)], 50) for i in range(len(H))])
E = px2ll(edge)
lat_min, lat_max = E[:, 0].min(), E[:, 0].max()
lon_min, lon_max = E[:, 1].min() / COS, E[:, 1].max() / COS

img = np.asarray(Image.open(root / "source/basel.jpg").convert("RGB"))
IH, IW = img.shape[:2]

def tile_xy(lat, lon, z):
    n = 2 ** z
    return (lon + 180) / 360 * n, (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n

count = 0
for z in range(ZMIN, ZMAX + 1):
    x0, y0 = map(int, tile_xy(lat_max, lon_min, z))
    x1, y1 = map(int, tile_xy(lat_min, lon_max, z))
    n = 2 ** z
    for tx in range(x0, x1 + 1):
        for ty in range(y0, y1 + 1):
            u, v = np.meshgrid(np.arange(256) + 0.5, np.arange(256) + 0.5)
            gx, gy = (tx + u / 256).ravel(), (ty + v / 256).ravel()
            lon = gx / n * 360 - 180
            lat = np.degrees(np.arctan(np.sinh(math.pi * (1 - 2 * gy / n))))
            src = ll2px(np.c_[lat, lon * COS])
            ok = inside(src, H) & (src[:, 0] >= 0) & (src[:, 0] < IW - 1) & (src[:, 1] >= 0) & (src[:, 1] < IH - 1)
            if not ok.any():
                continue
            rgba = np.zeros((256 * 256, 4), np.uint8)
            sx, sy = src[ok, 0], src[ok, 1]
            ix, iy = sx.astype(int), sy.astype(int)
            fx, fy = (sx - ix)[:, None], (sy - iy)[:, None]
            pix = (img[iy, ix] * (1 - fx) * (1 - fy) + img[iy, ix + 1] * fx * (1 - fy)
                   + img[iy + 1, ix] * (1 - fx) * fy + img[iy + 1, ix + 1] * fx * fy)
            rgba[ok, :3] = pix.astype(np.uint8)
            rgba[ok, 3] = 255
            d = out_dir / str(z) / str(tx)
            d.mkdir(parents=True, exist_ok=True)
            Image.fromarray(rgba.reshape(256, 256, 4), "RGBA").save(d / f"{ty}.webp", quality=78, method=4)
            count += 1
    print(f"z{z}: done ({count} tiles so far)", flush=True)

json.dump({"minzoom": ZMIN, "maxzoom": ZMAX, "bounds": [lon_min, lat_min, lon_max, lat_max],
           "tiles": "tiles/overlay/{z}/{x}/{y}.webp", "control_points": len(g), "lambda": LAM,
           "median_error_m": int(np.median([float(r["loo_error_m"]) for r in g]))},
          open(out_dir / "meta.json", "w"), indent=1)
print("bounds", [round(v, 5) for v in (lon_min, lat_min, lon_max, lat_max)])

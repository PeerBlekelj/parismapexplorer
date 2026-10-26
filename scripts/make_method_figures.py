"""Figures for the "How the map was bent" page (web/method/), as SVG in web/public/figures/.

1. orientation.svg   the whole map as printed, with true north from the fit
2. control-points.svg the 40 control points, coloured by leave-one-out error, and the overlay clip
3. affine-vs-spline.svg leave-one-out errors of one stretch (affine) and of the spline, as arrows
4. bend.svg          the old map's square grid after one stretch and after the spline, north up

Reads data/gcps_auto.csv (written by fit_transform.py) and source/basel.jpg. Also prints the
numbers the page quotes. Usage: .venv/bin/python scripts/make_method_figures.py .
"""
import base64, csv, io, json, math, sys
from pathlib import Path
import numpy as np
from PIL import Image

root = Path(sys.argv[1])
out = root / "web/public/figures"
out.mkdir(parents=True, exist_ok=True)
Image.MAX_IMAGE_PIXELS = None
KX, KY = 111.2e3, 73.2e3  # metres per degree of latitude / longitude at Paris (as fit_transform.py)
LAM, HULL_GROW = 0.2, 900  # as make_overlay_tiles.py

INK, INK2, PAPER, RULE, RED, BLUE = "#2b2118", "#6b5a48", "#f4ecdc", "#d3c3a3", "#a63a1f", "#3d5a78"
GOOD, MID, BAD = "#4f7a3a", "#c58a1b", "#a63a1f"
SERIF = "EB Garamond, Iowan Old Style, Georgia, serif"
SANS = "Inter, system-ui, sans-serif"

g = list(csv.DictReader(open(root / "data/gcps_auto.csv")))
P = np.array([[float(r["x"]), float(r["y"])] for r in g])
LL = np.array([[float(r["lat"]), float(r["lon"])] for r in g])
# gcps.csv was typed without accents
ACCENTS = {"Saint-Medard": "Saint-Médard", "Saint-Germain-des-Pres": "Saint-Germain-des-Prés",
           "Saint-Etienne-du-Mont": "Saint-Étienne-du-Mont", "Bastille (site)": "Bastille"}
names = [ACCENTS.get(r["name"], r["name"]) for r in g]
lat0, lon0 = LL[:, 0].mean(), LL[:, 1].mean()


def to_m(ll):
    """lat/lon -> metres east, north of the centre."""
    return np.c_[(ll[:, 1] - lon0) * KY, (ll[:, 0] - lat0) * KX]


M = to_m(LL)


def tps_fit(src, dst, lam):
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
        Z = (np.asarray(X, float) - mu) / s
        dd = np.linalg.norm(Z[:, None] - Q[None], axis=2)
        U = np.where(dd > 0, dd ** 2 * np.log(dd + 1e-12), 0)
        return U @ w[:n] + np.hstack([np.ones((len(Z), 1)), Z]) @ w[n:]
    return f


def affine_fit(src, dst):
    X = np.hstack([src, np.ones((len(src), 1))])
    c = np.linalg.lstsq(X, dst, rcond=None)[0]
    return lambda Y: np.hstack([np.asarray(Y, float), np.ones((len(Y), 1))]) @ c


def loo(make):
    pred = np.zeros_like(M)
    for i in range(len(P)):
        m = np.ones(len(P), bool); m[i] = False
        pred[i] = make(P[m], M[m])(P[i:i + 1])[0]
    return pred


tps = tps_fit(P, M, LAM)
aff = affine_fit(P, M)
pred_aff, pred_tps = loo(affine_fit), loo(lambda a, b: tps_fit(a, b, LAM))
err_aff = np.hypot(*(pred_aff - M).T)
err_tps = np.hypot(*(pred_tps - M).T)

# North in the scan: the direction in which the affine fit's "north" grows.
c = np.linalg.lstsq(np.hstack([P, np.ones((len(P), 1))]), M, rcond=None)[0]
C = c[:2]  # [dx, dy] @ C = [d east, d north] in metres; y grows down the sheet
A = np.array([[C[0, 0], -C[1, 0]], [C[0, 1], -C[1, 1]]])  # sheet (right, up) -> (east, north), column vectors
U, _, Vt = np.linalg.svd(A)
R = U @ Vt  # the closest pure rotation (polar decomposition), as the app uses for syncing
top_e, top_n = R @ np.array([0.0, 1.0])
top_bearing = math.degrees(math.atan2(top_e, top_n)) % 360  # compass bearing of the sheet's top
nr, nu = R.T @ np.array([0.0, 1.0])  # due north, in sheet (right, up)
north_deg = math.degrees(math.atan2(nr, nu)) % 360  # clockwise from the sheet's top
ax, ay = A[:, 0], A[:, 1]
axes_angle = math.degrees(math.acos(ax @ ay / np.linalg.norm(ax) / np.linalg.norm(ay)))  # 90 on a true plan
m_per_px = math.sqrt(abs(np.linalg.det(c[:2])))
sx, sy = np.linalg.norm(c[:2], axis=1)  # metres per pixel along the sheet's x and y


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
hc = H.mean(0)
H = hc + (H - hc) * (1 + HULL_GROW / np.linalg.norm(H - hc, axis=1, keepdims=True))

numbers = {
    "n": len(P),
    "north_deg": round(north_deg), "top_bearing": round(top_bearing), "axes_angle": round(axes_angle),
    "m_per_px": round(m_per_px, 2),
    "m_per_px_x": round(float(sx), 2), "m_per_px_y": round(float(sy), 2),
    "affine_median": round(float(np.median(err_aff))), "affine_p90": round(float(np.percentile(err_aff, 90))),
    "tps_median": round(float(np.median(err_tps))), "tps_p90": round(float(np.percentile(err_tps, 90))),
    "tps_max": round(float(err_tps.max())),
    "worst": [(names[i], round(float(err_tps[i]))) for i in np.argsort(-err_tps)[:4]],
    "affine_worst": round(float(err_aff.max())),
    "sources": {s: sum(1 for r in g if r["source"] == s) for s in sorted({r["source"] for r in g})},
}
print(json.dumps(numbers, ensure_ascii=False, indent=1))

# ---------- helpers ----------
scan = Image.open(root / "source/basel.jpg").convert("RGB")
W, Hh = scan.size


def bg_image(width):
    k = width / W
    im = scan.resize((width, round(Hh * k)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=70, optimize=True, progressive=True)
    return k, im.size, "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="{SANS}" role="img"><title>{title}</title>\n{body}\n</svg>\n')


def err_colour(e):
    return GOOD if e < 75 else MID if e < 150 else BAD


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


# ---------- 1. orientation ----------
k, (bw, bh), href = bg_image(1400)
cx, cy, L = bw * 0.9, bh * 0.16, 75
ang = math.radians(north_deg)
ux, uy = math.sin(ang), -math.cos(ang)
tip = (cx + ux * L, cy + uy * L); tail = (cx - ux * L * 0.6, cy - uy * L * 0.6)
body = [f'<image href="{href}" width="{bw}" height="{bh}"/>',
        f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{L + 22}" fill="{PAPER}" fill-opacity=".88" stroke="{INK}" stroke-width="1.5"/>',
        f'<line x1="{tail[0]:.1f}" y1="{tail[1]:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>']
# arrow head
hx, hy = -uy, ux
body.append(f'<path d="M{tip[0] + ux * 6:.1f},{tip[1] + uy * 6:.1f} L{tip[0] - ux * 18 + hx * 11:.1f},{tip[1] - uy * 18 + hy * 11:.1f} '
            f'L{tip[0] - ux * 18 - hx * 11:.1f},{tip[1] - uy * 18 - hy * 11:.1f} Z" fill="{RED}"/>')
lx, ly = cx + ux * (L + 6) * 0.55 + hx * 24, cy + uy * (L + 6) * 0.55 + hy * 24
body.append(f'<text x="{lx:.0f}" y="{ly + 9:.0f}" font-family="{SERIF}" font-size="30" font-weight="500" fill="{INK}" text-anchor="middle">N</text>')
(out / "orientation.svg").write_text(svg(bw, bh, "\n".join(body), "The whole map as printed, with the direction of north"), encoding="utf-8")

# ---------- 2. control points ----------
body = [f'<image href="{href}" width="{bw}" height="{bh}"/>',
        f'<rect width="{bw}" height="{bh}" fill="{PAPER}" fill-opacity=".35"/>',
        '<polygon points="' + " ".join(f"{x * k:.1f},{y * k:.1f}" for x, y in H) +
        f'" fill="none" stroke="{INK}" stroke-width="2.5" stroke-dasharray="9 6"/>']
for (x, y), e, nm in zip(P, err_tps, names):
    body.append(f'<circle cx="{x * k:.1f}" cy="{y * k:.1f}" r="9" fill="{err_colour(e)}" stroke="#fff" stroke-width="2.5"><title>{esc(nm)}: {e:.0f} m</title></circle>')
for i in np.argsort(-err_tps)[:3]:
    x, y = P[i] * k
    right = x > bw * 0.7
    body.append(f'<text x="{x - 14 if right else x + 14:.0f}" y="{y + 5:.0f}" font-size="16" font-weight="600" fill="{INK}" '
                f'text-anchor="{"end" if right else "start"}" paint-order="stroke" stroke="{PAPER}" stroke-width="5">'
                f'{esc(names[i])} · {err_tps[i]:.0f} m</text>')
# legend
lx, ly = 24, bh - 130
body.append(f'<rect x="{lx - 12}" y="{ly - 28}" width="330" height="134" rx="8" fill="{PAPER}" fill-opacity=".94" stroke="{RULE}"/>')
for j, (col, lab) in enumerate([(GOOD, "under 75 m"), (MID, "75–150 m"), (BAD, "150 m or more")]):
    body.append(f'<circle cx="{lx + 8}" cy="{ly + j * 26}" r="8" fill="{col}" stroke="#fff" stroke-width="2"/>'
                f'<text x="{lx + 26}" y="{ly + j * 26 + 6}" font-size="16" fill="{INK}">{lab}</text>')
body.append(f'<line x1="{lx}" y1="{ly + 82}" x2="{lx + 18}" y2="{ly + 82}" stroke="{INK}" stroke-width="2.5" stroke-dasharray="6 4"/>'
            f'<text x="{lx + 26}" y="{ly + 88}" font-size="16" fill="{INK}">edge of the overlay</text>')
body.append(f'<text x="{lx - 2}" y="{ly - 8}" font-size="13" fill="{INK2}" letter-spacing="1">LEAVE-ONE-OUT ERROR</text>')
(out / "control-points.svg").write_text(svg(bw, bh, "\n".join(body), "Control points on the map, coloured by leave-one-out error"), encoding="utf-8")

# ---------- metre-frame panels (north up) ----------
GRID_STEP, SAMPLE = 500, 60


def grid_lines():
    """The sheet's square grid, kept to the overlay area, as polylines in pixel space."""
    from shapely.geometry import LineString, Polygon
    poly = Polygon(H)
    x0, y0, x1, y1 = poly.bounds
    lines = []
    for x in np.arange(math.ceil(x0 / GRID_STEP) * GRID_STEP, x1, GRID_STEP):
        lines.append(LineString([(x, y0), (x, y1)]))
    for y in np.arange(math.ceil(y0 / GRID_STEP) * GRID_STEP, y1, GRID_STEP):
        lines.append(LineString([(x0, y), (x1, y)]))
    res = []
    for ln in lines:
        cut = ln.intersection(poly)
        for part in getattr(cut, "geoms", [cut]):
            if part.is_empty or part.length < 1:
                continue
            n = max(2, int(part.length / SAMPLE))
            res.append(np.array([part.interpolate(t, normalized=True).coords[0] for t in np.linspace(0, 1, n)]))
    return res


lines = grid_lines()
outline = np.vstack([H, H[:1]])
all_m = np.vstack([tps(np.vstack(lines)), aff(np.vstack(lines)), M])
mx0, my0 = all_m.min(0) - 150
mx1, my1 = all_m.max(0) + 150


def frame(pw, ox=0, oy=0):
    s = pw / (mx1 - mx0)
    ph = (my1 - my0) * s
    return s, ph, (lambda m: np.c_[ox + (m[:, 0] - mx0) * s, oy + (my1 - m[:, 1]) * s])


def path(pts):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


def scalebar(x, y, s, metres=1000):
    return (f'<line x1="{x}" y1="{y}" x2="{x + metres * s:.1f}" y2="{y}" stroke="{INK}" stroke-width="3"/>'
            f'<line x1="{x}" y1="{y - 6}" x2="{x}" y2="{y + 6}" stroke="{INK}" stroke-width="2"/>'
            f'<line x1="{x + metres * s:.1f}" y1="{y - 6}" x2="{x + metres * s:.1f}" y2="{y + 6}" stroke="{INK}" stroke-width="2"/>'
            f'<text x="{x + metres * s / 2:.1f}" y="{y - 10}" font-size="14" fill="{INK}" text-anchor="middle">{metres / 1000:g} km</text>')


def north(x, y):
    return (f'<path d="M{x},{y - 22} L{x - 8},{y + 4} L{x},{y - 2} L{x + 8},{y + 4} Z" fill="{INK}"/>'
            f'<text x="{x}" y="{y + 24}" font-family="{SERIF}" font-size="18" text-anchor="middle" fill="{INK}">N</text>')


# ---------- 3. affine vs spline ----------
EXAG = 4
PW, GAP, TOP = 560, 40, 70
s, ph, f0 = frame(PW, 0, TOP)
_, _, f1 = frame(PW, PW + GAP, TOP)
body = [f'<rect width="{2 * PW + GAP}" height="{ph + TOP + 40}" fill="{PAPER}"/>']
for j, (f, pred, err, title) in enumerate([(f0, pred_aff, err_aff, "One stretch (affine)"), (f1, pred_tps, err_tps, "Thin-plate spline")]):
    ox = f(M[:1])[0, 0] - (M[0, 0] - mx0) * s
    body.append(f'<clipPath id="c{j}"><rect x="{ox:.0f}" y="{TOP}" width="{PW}" height="{ph:.0f}"/></clipPath>')
    body.append(f'<rect x="{ox:.0f}" y="{TOP}" width="{PW}" height="{ph:.0f}" fill="#fffaf0" stroke="{RULE}"/>')
    body.append(f'<g clip-path="url(#c{j})">')
    body.append(f'<path d="{path(f(tps(outline)))}" fill="none" stroke="{RULE}" stroke-width="2" stroke-dasharray="6 5"/>')
    for m, pr, e in zip(M, pred, err):
        a = f(m[None])[0]
        b = f((m + (pr - m) * EXAG)[None])[0]
        body.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{err_colour(e)}" stroke-width="2.5"/>')
        body.append(f'<circle cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="4" fill="{INK}"/>')
    body.append('</g>')
    body.append(f'<text x="{ox:.0f}" y="{TOP - 36}" font-family="{SERIF}" font-size="24" fill="{INK}">{title}</text>')
    body.append(f'<text x="{ox:.0f}" y="{TOP - 12}" font-size="15" fill="{INK2}">median {np.median(err):.0f} m · 90% within {np.percentile(err, 90):.0f} m · worst {err.max():.0f} m</text>')
    body.append(scalebar(ox + 20, TOP + ph - 22, s))
    body.append(north(ox + PW - 30, TOP + 36))
body.append(f'<text x="0" y="{TOP + ph + 28:.0f}" font-size="14" fill="{INK2}">Dot: true position today. Line: where the fit puts it when that point is left out, drawn {EXAG}× longer than it is.</text>')
(out / "affine-vs-spline.svg").write_text(svg(2 * PW + GAP, round(ph + TOP + 40), "\n".join(body), "Leave-one-out errors: affine vs thin-plate spline"), encoding="utf-8")

# ---------- 4. the bend ----------
PW4, TOP4 = 900, 20
s4, ph4, f4 = frame(PW4, 0, TOP4)
body = [f'<rect width="{PW4}" height="{ph4 + TOP4 + 70:.0f}" fill="#fffaf0"/>']
for ln in lines:
    body.append(f'<path d="{path(f4(aff(ln)))}" fill="none" stroke="{INK2}" stroke-opacity=".45" stroke-width="1.3"/>')
for ln in lines:
    body.append(f'<path d="{path(f4(tps(ln)))}" fill="none" stroke="{RED}" stroke-width="1.8"/>')
for m in f4(M):
    body.append(f'<circle cx="{m[0]:.1f}" cy="{m[1]:.1f}" r="4.5" fill="{BLUE}" stroke="#fff" stroke-width="1.5"/>')
for key, lab in [("G001", "Notre-Dame"), ("G006", "Bastille"), ("G003", "Saint-Germain-des-Prés"), ("G002", "Saint-Eustache")]:
    i = next((j for j, r in enumerate(g) if r["id"] == key), None)
    if i is None:
        continue
    x, y = f4(M[i:i + 1])[0]
    body.append(f'<text x="{x + 9:.0f}" y="{y - 8:.0f}" font-size="15" font-weight="600" fill="{INK}" paint-order="stroke" stroke="#fffaf0" stroke-width="4">{lab}</text>')
body.append(scalebar(24, TOP4 + ph4 - 20, s4))
body.append(north(PW4 - 34, TOP4 + 34))
ly = TOP4 + ph4 + 26
body.append(f'<line x1="0" y1="{ly:.0f}" x2="26" y2="{ly:.0f}" stroke="{INK2}" stroke-opacity=".6" stroke-width="2"/>'
            f'<text x="34" y="{ly + 5:.0f}" font-size="15" fill="{INK}">one stretch: the sheet\'s grid stays straight and evenly spaced</text>')
body.append(f'<line x1="0" y1="{ly + 26:.0f}" x2="26" y2="{ly + 26:.0f}" stroke="{RED}" stroke-width="2.5"/>'
            f'<text x="34" y="{ly + 31:.0f}" font-size="15" fill="{INK}">the spline: the same grid bent to pass through the control points (blue)</text>')
(out / "bend.svg").write_text(svg(PW4, round(ph4 + TOP4 + 70), "\n".join(body), "The old map's grid after one stretch and after the spline, north up"), encoding="utf-8")

(out / "numbers.json").write_text(json.dumps(numbers, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for p in sorted(out.iterdir()):
    print(f"{p.name:24s} {p.stat().st_size / 1e3:7.0f} kB")

"""Build the control-point set and compare affine vs thin-plate-spline transforms.

Control points = hand-picked GCPs (data/gcps.csv, quality=label) + identified places with
exact coordinates whose label sits on a building (churches, colleges, gates, bridges,
buildings). Duplicates within 150 px are merged (hand-picked wins).
Writes data/gcps_auto.csv and prints leave-one-out errors for each method.
"""
import csv, sys
from pathlib import Path
import numpy as np

root = Path(sys.argv[1])
KX, KY = 111.2e3, 73.2e3  # metres per degree at Paris

def tps_fit(P, V, lam):
    """Thin-plate spline from pixel points P (n,2) to values V (n,k). Returns a predictor."""
    s = P.std()
    Q = (P - P.mean(0)) / s
    n = len(Q)
    d = np.linalg.norm(Q[:, None] - Q[None], axis=2)
    K = np.where(d > 0, d ** 2 * np.log(d + 1e-12), 0) + lam * np.eye(n)
    Pm = np.hstack([np.ones((n, 1)), Q])
    A = np.zeros((n + 3, n + 3)); A[:n, :n] = K; A[:n, n:] = Pm; A[n:, :n] = Pm.T
    b = np.zeros((n + 3, V.shape[1])); b[:n] = V
    w = np.linalg.solve(A, b)
    mu = P.mean(0)
    def pred(X):
        Z = (X - mu) / s
        dd = np.linalg.norm(Z[:, None] - Q[None], axis=2)
        U = np.where(dd > 0, dd ** 2 * np.log(dd + 1e-12), 0)
        return U @ w[:n] + np.hstack([np.ones((len(Z), 1)), Z]) @ w[n:]
    return pred

def affine_fit(P, V):
    X = np.hstack([P, np.ones((len(P), 1))])
    c = np.linalg.lstsq(X, V, rcond=None)[0]
    return lambda Y: np.hstack([Y, np.ones((len(Y), 1))]) @ c

def err_m(a, b):
    return np.hypot((a[:, 0] - b[:, 0]) * KX, (a[:, 1] - b[:, 1]) * KY)

pts = []
for g in csv.DictReader(open(root / "data/gcps.csv")):
    pts.append({"id": g["id"], "name": g["name"], "x": int(g["x"]), "y": int(g["y"]),
                "lat": float(g["lat"]), "lon": float(g["lon"]), "src": "hand"})
inv = {r["id"]: r for r in csv.DictReader(open(root / "data/labels_inventory.csv"))}
# Correct coordinates, but harmful as control points: the only point in a large, heavily
# compressed area of the bird's-eye view, so the spline stretches everything around it.
EXCLUDE = {"L0001": "Pont de Charenton: lone point 3 km beyond the city edge"}
for r in csv.DictReader(open(root / "data/places_others.csv")):
    L = inv[r["id"]]
    if r["loc_confidence"] != "exact" or r["duplicate_of"] or L["type"] in ("village_faubourg", "other"):
        continue
    if r["id"] in EXCLUDE:
        continue
    x, y = int(L["x"]), int(L["y"])
    if any(abs(p["x"] - x) < 150 and abs(p["y"] - y) < 150 for p in pts):
        continue
    pts.append({"id": r["id"], "name": r["modern"] or r["old"], "x": x, "y": y,
                "lat": float(r["lat"]), "lon": float(r["lon"]), "src": "place"})

# Refinements (data/gcps_refined.csv): move a point from its label to the drawn feature, or add
# precise new points (bridge ends). Bridge labels are dropped when their ends are present.
REPLACED_BY_ENDS = {"L0002", "L0003", "L0004", "L0006"}
ref = {r["id"]: r for r in csv.DictReader(open(root / "data/gcps_refined.csv"))} if "--labels-only" not in sys.argv else {}
if ref:
    pts = [p for p in pts if p["id"] not in REPLACED_BY_ENDS]
    for p in pts:
        r = ref.get(p["id"])
        if r:
            p["x"], p["y"], p["src"] = int(r["x"]), int(r["y"]), p["src"] + "+feature"
            if r["lat"]:
                p["lat"], p["lon"] = float(r["lat"]), float(r["lon"])
    have = {p["id"] for p in pts}
    for r in ref.values():
        if r["id"] not in have:
            pts.append({"id": r["id"], "name": r["name"], "x": int(r["x"]), "y": int(r["y"]),
                        "lat": float(r["lat"]), "lon": float(r["lon"]), "src": "feature"})

# Villages at the edge: coarse (a village is an area), but the only anchors out there.
WITH_VILLAGES = "--villages" in sys.argv
if WITH_VILLAGES:
    for r in csv.DictReader(open(root / "data/places_others.csv")):
        L = inv[r["id"]]
        if L["type"] != "village_faubourg" or r["duplicate_of"] or r["loc_confidence"] != "exact":
            continue
        if L["text"].startswith("LES FAUBOURS"):  # a faubourg is a whole district: too vague
            continue
        x, y = int(L["x"]), int(L["y"])
        pts.append({"id": r["id"], "name": r["modern"] or r["old"], "x": x, "y": y,
                    "lat": float(r["lat"]), "lon": float(r["lon"]), "src": "village"})

P = np.array([[p["x"], p["y"]] for p in pts], float)
V = np.array([[p["lat"], p["lon"]] for p in pts])
print(len(pts), "control points")

def loo(make):
    out = np.zeros_like(V)
    for i in range(len(P)):
        m = np.ones(len(P), bool); m[i] = False
        out[i] = make(P[m], V[m])(P[i:i + 1])[0]
    return err_m(out, V)

results = {"affine": loo(affine_fit)}
for lam in (0.0, 0.01, 0.05, 0.2):
    results[f"tps λ={lam}"] = loo(lambda A, B, lam=lam: tps_fit(A, B, lam))
central = np.array([p["src"] != "village" for p in pts])
for k, e in results.items():
    c = e[central]
    print(f"{k:12s} leave-one-out, city points: median {np.median(c):4.0f} m  p90 {np.percentile(c, 90):5.0f} m"
          f"  | all: median {np.median(e):5.0f} m")

best = "tps λ=0.2"  # the setting the app and make_overlay_tiles.py use; report its errors
e = results[best]
print(f"\nworst points under {best}:")
for i in np.argsort(-e)[:8]:
    print(f"  {pts[i]['id']} {pts[i]['name'][:40]:40s} {e[i]:5.0f} m  ({pts[i]['src']})")

with open(root / "data/gcps_auto.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "name", "x", "y", "lat", "lon", "source", "loo_error_m"])
    for p, ee in zip(pts, e):
        w.writerow([p["id"], p["name"], p["x"], p["y"], p["lat"], p["lon"], p["src"], round(float(ee))])

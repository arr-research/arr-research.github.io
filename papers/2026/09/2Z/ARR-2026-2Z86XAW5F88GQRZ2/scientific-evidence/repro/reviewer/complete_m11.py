"""Chamber-vertex completeness of the predicted set at m=11, z=1 (d=15): for each predicted form g, enumerate the vertices of
C_g (qhull HalfspaceIntersection in the 12-dim affine chart) and check kappa(v) = g(v) by the own hive LP.  With the validity of all
forms (extra_checks.py) and convexity of kappa - g, this is a floating-point proof of kappa_15 = max pred on the whole stratum."""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, time, numpy as np
from scipy.optimize import linprog
from scipy.spatial import HalfspaceIntersection
sys.path.insert(0, AUTHOR_DIR)
from horn_own import Hive, spec, form_val
from families2 import gen2
m = int(sys.argv[1]) if len(sys.argv) > 1 else 11; z = 1; d = m + z + 3
pred = sorted(gen2(m)); Hv = Hive(d); n = m + 1; t0 = time.time()
def lift(x):
    a = np.concatenate([x[:m - 1], [1 - x[:m - 1].sum()]]); b = np.array([x[m - 1], x[m], 1 - x[m - 1] - x[m]]); return a, b
def lin(ca, cb):
    row = np.zeros(n); row[:m - 1] = ca[:m - 1] - ca[m - 1]; row[m - 1] = cb[0] - cb[2]; row[m] = cb[1] - cb[2]; return row, ca[m - 1] + cb[2]
tot_v = 0; worst = 0; nfail = 0
for g in pred:
    g = np.array(g, float); ineq = []
    for h in pred:
        h = np.array(h, float)
        if np.array_equal(h, g): continue
        ineq.append(lin(g[:m] - h[:m], np.array([g[m] - h[m], g[m + 1] - h[m + 1], 0.0])))
    for j in range(m - 1):
        ca = np.zeros(m); ca[j] = 1; ca[j + 1] = -1; ineq.append(lin(ca, np.zeros(3)))
    ca = np.zeros(m); ca[m - 1] = 1; ineq.append(lin(ca, np.zeros(3)))
    for j in range(2):
        cb = np.zeros(3); cb[j] = 1; cb[j + 1] = -1; ineq.append(lin(np.zeros(m), cb))
    cb = np.zeros(3); cb[2] = 1; ineq.append(lin(np.zeros(m), cb))
    A = np.array([r for r, c in ineq]); C = np.array([c for r, c in ineq])
    norms = np.linalg.norm(A, axis=1); cc = np.zeros(n + 1); cc[-1] = -1
    res = linprog(cc, A_ub=np.hstack([-A, norms[:, None]]), b_ub=C, bounds=[(None, None)] * n + [(0, None)], method='highs')
    if res.status != 0 or res.x[-1] < 1e-9: print("  empty/degenerate chamber", g); nfail += 1; continue
    hs = HalfspaceIntersection(np.hstack([-A, -C[:, None]]), res.x[:n])
    verts = []
    for x in hs.intersections:
        if not any(np.linalg.norm(x - v) < 1e-7 for v in verts): verts.append(x)
    tot_v += len(verts); wg = 0
    for x in verts:
        a, b = lift(x); k = Hv.solve(spec(a, b, z))['val']; wg = max(wg, abs(k - form_val(g, a, b)))
    worst = max(worst, wg)
    if wg > 1e-9: print(f"  form {g}: {len(verts)} vertices, max|kappa - g| = {wg:.2e}  <-- GAP"); nfail += 1
print(f"m={m} z={z} d={d}: {len(pred)} predicted chambers, {tot_v} vertices (qhull), max|kappa - g| at vertices = {worst:.2e}, chambers with a gap: {nfail}  ({time.time()-t0:.0f}s)")

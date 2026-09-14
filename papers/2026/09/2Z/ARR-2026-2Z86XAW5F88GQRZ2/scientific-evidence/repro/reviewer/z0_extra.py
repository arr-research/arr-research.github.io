"""The z=0-only form: (a) m=10, 11: validity of the reported extra form at z=0 (joint LP: min kappa - g over the stratum), its
invalidity at z=1, and its exposedness relative to the predicted set; (b) m=12 (3 | m), z=0, d=15: sample 600 points vs the
predicted set -- is there any point with kappa_15 > max pred (which would reveal an extra z=0 form)?"""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, time, numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, csr_matrix
sys.path.insert(0, AUTHOR_DIR)
sys.path.insert(0, REVIEWER_DIR)
from horn_own import Hive, spec, rand_point, form_val
from exposed_m5 import radius
from families2 import gen2

def joint_min(m, z, g):
    d = m + z + 3; Hv = Hive(d); nv = Hv.nv; H = Hv.H; nx = nv + m + 3
    A = lil_matrix((Hv.A.shape[0] + (m - 1) + 2, nx)); A[:Hv.A.shape[0], :nv] = Hv.A; r = Hv.A.shape[0]
    for j in range(m - 1): A[r, nv + j] = -1; A[r, nv + j + 1] = 1; r += 1
    for j in range(2): A[r, nv + m + j] = -1; A[r, nv + m + j + 1] = 1; r += 1
    E = lil_matrix((Hv.neq + 2, nx)); E[:Hv.neq, :nv] = Hv.E
    for t, row in enumerate(Hv.lam_rows):
        if t < m: E[row, nv + t] = -1.0
        elif t >= m + z: E[row, nv + m + (2 - (t - m - z))] = 1.0
    E[Hv.neq, nv:nv + m] = 1; E[Hv.neq + 1, nv + m:nv + m + 3] = 1
    beq = np.zeros(Hv.neq + 2); beq[-2:] = 1
    c = np.zeros(nx); c[H:nv] = 1
    for j in range(m): c[nv + j] = -g[j]
    c[nv + m] = -g[m]; c[nv + m + 1] = -g[m + 1]
    res = linprog(c, A_ub=csr_matrix(A), b_ub=np.zeros(A.shape[0]), A_eq=csr_matrix(E), b_eq=beq, bounds=[(None, None)] * H + [(0, None)] * d + [(0, None)] * (m + 3),
                  method='highs', options=dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10))
    return res.fun, res.x[nv:nv + m], res.x[nv + m:nv + m + 3]

for m, g0 in ((10, (1, 2, 2, 3, 3, 3, 4, 4, 5, 6, -2, -1)), (11, (1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, -2, -1))):
    pred = sorted(gen2(m)); t0 = time.time()
    v0, a, b = joint_min(m, 0, g0); v1, a1, b1 = joint_min(m, 1, g0)
    t, ac, bc = radius(g0, pred, m); k0 = Hive(m + 3).solve(spec(ac, bc, 0))['val']
    print(f"m={m}: extra z=0 form {g0}: min(kappa_(m+3) - g0) over stratum = {v0:.2e} (valid at z=0: {v0 > -1e-9}); "
          f"min(kappa_(m+4) - g0) = {v1:.4e} (invalid at z=1: {v1 < -1e-9}); radius vs predicted set {t:.3e}, kappa_(m+3) - g0 at centre = {k0 - form_val(g0, ac, bc):.1e}  ({time.time()-t0:.0f}s)", flush=True)
m = 12; pred = sorted(gen2(m)); d = m + 3; Hv = Hive(d); rng = np.random.default_rng(12); worst = 0; t0 = time.time()
for i in range(600):
    a, b = rand_point(m, rng, law=i % 6); v = Hv.solve(spec(a, b, 0))['val']; worst = max(worst, v - max(form_val(g, a, b) for g in pred))
print(f"m=12 z=0 d=15: 600 points, max(kappa - max pred) = {worst:.2e} (no extra z=0 form detected: {worst < 1e-9})  ({time.time()-t0:.0f}s)")
# and m=13 z=0 (3 does not divide 13): expect an extra form
m = 13; pred = sorted(gen2(m)); d = m + 3; Hv = Hive(d); worst = 0; t0 = time.time(); found = {}
for i in range(600):
    a, b = rand_point(m, rng, law=i % 6); r = Hv.solve(spec(a, b, 0)); v = r['val']; gap = v - max(form_val(g, a, b) for g in pred); worst = max(worst, gap)
    if gap > 1e-9:
        gr = r['grad']; t3 = -(-gr[d - 3]); al = gr[:m] + gr[d - 3]; be = (-gr[d - 1] - gr[d - 3], -gr[d - 2] - gr[d - 3])
        key = tuple(np.round(np.concatenate([al, be]), 3)); found[key] = found.get(key, 0) + 1
print(f"m=13 z=0 d=16: 600 points, max(kappa - max pred) = {worst:.2e}; extra forms seen: {found}  ({time.time()-t0:.0f}s)")

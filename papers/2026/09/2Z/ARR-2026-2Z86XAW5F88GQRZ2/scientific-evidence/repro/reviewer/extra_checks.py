"""Extra checks: (i) formula at (7,2),(8,2),(9,2) (d=12..14) with own hive LP, tight; (ii) rank forcing on the 'new part' for
m=5 (Horn LP d=9, cap 5) and m=7 (hive d=11, cap 7); (iii) m=11 z=1: validity LP (joint hive LP with lambda as variables) and
exposedness (radius LP) for all 103 predicted forms."""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, time, numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, csr_matrix, hstack, vstack
sys.path.insert(0, AUTHOR_DIR)
sys.path.insert(0, REVIEWER_DIR)
from horn_own import Hive, horn_rows, kappa_horn, spec, rand_point, form_val
from exposed_m5 import radius
from families2 import gen2
W = AUTHOR_DIR
rng = np.random.default_rng(99)

print("--- (i) formula check at d = 12..14")
for m, z in ((7, 2), (8, 2), (9, 2)):
    d = m + z + 3; S = [tuple(f) for f in json.load(open(f"{W}/closed_m{m}_z1.json"))]; Hv = Hive(d); worst = 0; t0 = time.time()
    for i in range(250):
        a, b = rand_point(m, rng, law=i % 6); v = Hv.solve(spec(a, b, z))['val']; mx = max(form_val(g, a, b) for g in S); worst = max(worst, abs(v - mx))
    print(f"m={m} z={z} d={d}: 250 points, max|hive - maxS| = {worst:.2e}  ({time.time()-t0:.0f}s)", flush=True)

print("--- (ii) rank forcing on the new part (g0 > max S(m,1)) after padding")
for m, g0 in ((5, (1, 2, 3, 3, 4, -2, -1)), (7, (1, 2, 2, 3, 3, 4, 5, -2, -1))):
    S1 = [tuple(f) for f in json.load(open(f"{W}/closed_m{m}_z1.json"))]; d = m + 4
    Hv = Hive(d); n_new = forced = capk = 0; tries = 0
    # sample near the chamber centre of g0 at z=0 to hit the new part
    S0 = [tuple(f) for f in json.load(open(f"{W}/closed_m{m}_z0.json"))]
    t, ac, bc = radius(g0, [h for h in S0 if h != g0], m)
    while n_new < 40 and tries < 5000:
        tries += 1
        a = np.sort(np.abs(ac + 0.5 * t * rng.normal(size=m)))[::-1]; b = np.sort(np.abs(bc + 0.5 * t * rng.normal(size=3)))[::-1]; a /= a.sum(); b /= b.sum()
        if form_val(g0, a, b) - max(form_val(h, a, b) for h in S1) < 1e-6: continue
        n_new += 1
        k = Hv.solve(spec(a, b, 1))['val']; kc = Hv.solve(spec(a, b, 1), cap=m)['val']; k0 = Hive(d - 1).solve(spec(a, b, 0))['val']
        if kc - k > 1e-9: forced += 1
        if abs(kc - k0) < 1e-9: capk += 1
    print(f"m={m}: {n_new} points in the new part (of {tries} tries): rank m+1 forced at z=1 at {forced}; rank-m-capped value == kappa_(m+3) at {capk}", flush=True)

print("--- (iii) m=11 z=1: validity and exposedness of the 103 predicted forms")
m, z = 11, 1; d = m + z + 3; pred = sorted(gen2(m)); Hv = Hive(d); nv = Hv.nv; H = Hv.H
# joint LP: variables (h, s, a_1..a_m, b_1..b_3); min sum s - g(a,b) over the P=1 stratum
nx = nv + m + 3
A = lil_matrix((Hv.A.shape[0] + (m - 1) + 2, nx)); A[:Hv.A.shape[0], :nv] = Hv.A; r = Hv.A.shape[0]
for j in range(m - 1): A[r, nv + j] = -1; A[r, nv + j + 1] = 1; r += 1
for j in range(2): A[r, nv + m + j] = -1; A[r, nv + m + j + 1] = 1; r += 1
A = csr_matrix(A); bub = np.zeros(A.shape[0])
E = lil_matrix((Hv.neq + 2, nx)); E[:Hv.neq, :nv] = Hv.E
for t, row in enumerate(Hv.lam_rows):
    if t < m: E[row, nv + t] = -1.0
    elif t >= m + z: E[row, nv + m + (2 - (t - m - z))] = 1.0
E[Hv.neq, nv:nv + m] = 1; E[Hv.neq + 1, nv + m:nv + m + 3] = 1
E = csr_matrix(E); beq = np.zeros(Hv.neq + 2); beq[-2:] = 1
bounds = [(None, None)] * H + [(0, None)] * d + [(0, None)] * (m + 3)
t0 = time.time(); minval = 1; nvalid = 0; nexp = 0; minrad = 1
for g in pred:
    c = np.zeros(nx); c[H:nv] = 1
    for j in range(m): c[nv + j] = -g[j]
    c[nv + m] = -g[m]; c[nv + m + 1] = -g[m + 1]
    res = linprog(c, A_ub=A, b_ub=bub, A_eq=E, b_eq=beq, bounds=bounds, method='highs', options=dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10))
    v = res.fun; minval = min(minval, v)
    if v > -1e-9: nvalid += 1
    else: print(f"   INVALID predicted form {g}: min(kappa - g) = {v:.3e} at a={np.round(res.x[nv:nv+m],4)} b={np.round(res.x[nv+m:nv+m+3],4)}")
    t, a, b = radius(g, [h for h in pred if h != g], m); minrad = min(minrad, t)
    if t > 1e-9:
        k = Hv.solve(spec(a, b, z))['val']
        if abs(k - form_val(g, a, b)) < 1e-9: nexp += 1
        else: print(f"   form {g}: radius {t:.2e} but kappa - g = {k - form_val(g, a, b):.2e} at the centre")
    else: print(f"   NOT exposed among predicted: {g} (radius {t:.2e})")
print(f"m=11 z=1: valid (min over stratum of kappa - g >= -1e-9): {nvalid}/{len(pred)} (min value {minval:.2e}); exposed with kappa = g at centre: {nexp}/{len(pred)}; min radius {minrad:.2e}  ({time.time()-t0:.0f}s)")

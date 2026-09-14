"""Test the predicted form set pred_m{m}.json (rules v2, z>=1 family) against the hive LP at fresh random points, tight tolerances.
At points where kappa_LP > max pred + 1e-9 the LP dual form is printed (canonical integer coords) to identify missing forms.
Usage: python test_pred.py m z N"""
import sys, json, time, numpy as np
from scipy.optimize import linprog
from hive_core import HiveLP, rat
from m3_forms import spec_m3, canon
from m3_gather import rand_m3x, LAWS
m, z, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); d = m + z + 3
S = np.array(json.load(open(f"pred_m{m}.json")), float); M = HiveLP(d)
def solve_tight(lam):
    beq = np.zeros(M.neq)
    for t, r in enumerate(M.lam_rows): beq[r] = lam[t]
    res = linprog(M.c, A_ub=M.Aub, b_ub=M.bub, A_eq=M.Aeq, b_eq=beq, bounds=M.bounds, method='highs',
                  options=dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10))
    if res.status != 0: return None, None
    return res.fun, np.array([res.eqlin.marginals[r] for r in M.lam_rows])
rng = np.random.default_rng(77 + m + 10 * z); t0 = time.time(); gp = gm = 0; missing = {}
for i in range(N):
    a, b = rand_m3x(m, rng, LAWS[i % len(LAWS)]); lam = spec_m3(a, b, z)
    val, grad = solve_tight(lam)
    if val is None: continue
    v = np.max(S[:, :m] @ a + S[:, m] * b[0] + S[:, m + 1] * b[1]); g = val - v
    gp = max(gp, g); gm = max(gm, -g)
    if g > 1e-9:
        f = tuple(int(rat(x, 2000)) for x in canon(grad, m, z)); missing[f] = missing.get(f, 0) + 1
print(f"m={m} z={z} d={d} |pred|={len(S)}: N={N}: max(kappa-maxpred)={gp:.2e}, max(maxpred-kappa)={gm:.2e}; dual forms at gap points: {missing}  ({time.time()-t0:.0f}s)", flush=True)

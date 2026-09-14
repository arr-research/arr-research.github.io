"""The d=8 inertia-(4,4) example of [RankOnset] Theorem 4.1: lambda = (4c-3b, b, b, b, -c, -c, -c, -c), here (5,1,1,1,-2^4)
(c=2, b=1): kappa_8 = 13 and every optimizer has rank 5 > 4 = max(n_+, n_-).  We identify the exposed form at this point,
its level layering, the block-shift chain feasibility and rank bound, the minimal rank on the optimal face, and scan the
one-parameter family in c."""
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix
from mn_tools import *
from horn_lp import HornLP
from chain_lp import feasible, numeric_layers
m, n, z = 4, 4, 0; d = 8; H = HornLP(8); M = HiveLP(8)

import json
S = [tuple(json.loads(k)) for k in json.load(open("forms_m4_n4_z0.json")) if not k.startswith('_')]

def analyse(lam, verbose=True):
    lam = np.sort(np.asarray(lam, float))[::-1]
    r = M.solve(lam); kap = r['val']
    a = lam[:4]; b = -lam[4:][::-1]
    tied = [f for f in S if abs(form_val(np.array(f, float), a, b) - kap) < 1e-9]
    key = tied[0]
    L = level_layering(key, m, n)
    s = H.solve(lam)['s']
    A = np.vstack([-H.A, H.ord]); ub = np.concatenate([-(H.B @ lam), np.zeros(d - 2)])
    A2 = np.vstack([A, np.ones(d - 1)]); ub2 = np.concatenate([ub, [kap + 1e-9]])
    mins = []
    for k in range(4, d - 1):
        c = np.zeros(d - 1); c[k] = 1
        res = linprog(c, A_ub=csr_matrix(A2), b_ub=ub2, bounds=[(0, None)] * (d - 1), method='highs'); mins.append(res.fun)
    ok = feasible(numeric_layers(L, a, b), max(len(x) for x in L)) if not any(len(x) == 0 for x in L) else None
    caps = sum(min(len(L[t - 1]), len(L[t])) for t in range(1, len(L)))
    if verbose:
        print(f"lambda={lam}: kappa={kap:.6f}; raw hive dual gradient {np.round(r['grad'], 4)}; exposed forms of S(4,4,0) attaining kappa here: {len(tied)}")
        for f in tied:
            LL = level_layering(f, m, n); okf = feasible(numeric_layers(LL, a, b), max(len(x) for x in LL)) if not any(len(x) == 0 for x in LL) else None
            print(f"      {list(f)}  {show(LL)}  chain feasible: {okf}; chain rank bound {sum(min(len(LL[t - 1]), len(LL[t])) for t in range(1, len(LL)))}")
        print(f"   optimal s = {s.round(6)}; min s_5..s_7 on the optimal face = {np.round(mins, 6)} -> minimal optimal rank = {4 + sum(1 for x in mins if x > 1e-9)}")
        print(f"   chain (block shift of the level layering) feasible: {ok}; rank bound of that chain sum_t min(|L_(t-1)|,|L_t|) = {caps}")
    return key, mins, kap

analyse(np.array([5, 1, 1, 1, -2, -2, -2, -2.]))
print("one-parameter family (4c-3b, b, b, b, -c^4), b=1:")
for c in [0.8, 0.9, 1.0, 1.1, 1.25, 1.5, 2.0, 3.0]:
    lam = np.array([4 * c - 3, 1, 1, 1, -c, -c, -c, -c])
    key, mins, kap = analyse(lam, verbose=False)
    print(f"   c={c}: kappa={kap:.4f} first tied form {list(key)} min s_5 on the optimal face {mins[0]:.4f} -> r_* = {4 + sum(1 for x in mins if x > 1e-9)}")

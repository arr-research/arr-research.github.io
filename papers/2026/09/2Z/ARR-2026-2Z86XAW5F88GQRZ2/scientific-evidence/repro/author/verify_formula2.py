"""Fresh-sample verification with signed gaps and tight-tolerance re-solves.
gap_plus = kappa_LP - maxS (formula too LOW if > tol: a missing form), gap_minus = maxS - kappa_LP (LP tolerance artefact if the
certificates hold).  Points with |gap| > 1e-10 are re-solved with HiGHS primal/dual feasibility tolerances 1e-10 (default 1e-7).
Usage: python verify_formula2.py m_min m_max N zlist seed"""
import sys, json, time, numpy as np
from scipy.optimize import linprog
from hive_core import HiveLP
from m3_forms import spec_m3
from m3_gather import rand_m3x, LAWS

def solve_tight(M, lam):
    beq = np.zeros(M.neq)
    for t, r in enumerate(M.lam_rows): beq[r] = lam[t]
    res = linprog(M.c, A_ub=M.Aub, b_ub=M.bub, A_eq=M.Aeq, b_eq=beq, bounds=M.bounds, method='highs',
                  options=dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10))
    return res.fun if res.status == 0 else None

m0, m1, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
zs = [int(x) for x in sys.argv[4].split(',')]; seed = int(sys.argv[5]) if len(sys.argv) > 5 else 2026
for m in range(m0, m1 + 1):
    for z in zs:
        d = m + z + 3
        if d > 14: print(f"m={m} z={z}: d={d} > 14, skipped"); continue
        S = np.array(json.load(open(f"closed_m{m}_z{0 if z == 0 else 1}.json")), float)
        M = HiveLP(d); rng = np.random.default_rng(seed + 100 * m + z); t0 = time.time()
        gp = gm = 0; susp = []; gp2 = gm2 = 0; nre = 0
        for i in range(N):
            law = LAWS[i % len(LAWS)]; a, b = rand_m3x(m, rng, law); lam = spec_m3(a, b, z)
            r = M.solve(lam)
            if r is None: print("  LP failure"); continue
            v = np.max(S[:, :m] @ a + S[:, m] * b[0] + S[:, m + 1] * b[1]); g = r['val'] - v
            gp = max(gp, g); gm = max(gm, -g)
            if abs(g) > 1e-10:
                v2 = solve_tight(M, lam); nre += 1
                if v2 is None: print("  tight LP failure"); continue
                g2 = v2 - v; gp2 = max(gp2, g2); gm2 = max(gm2, -g2)
                if abs(g2) > 1e-9: susp.append((law, np.round(a, 6).tolist(), np.round(b, 6).tolist(), v, v2))
        print(f"m={m} z={z} d={d} |S|={len(S)}: N={N}; default tol: max(kappa-maxS)={gp:.2e}, max(maxS-kappa)={gm:.2e}; "
              f"{nre} points re-solved at tol 1e-10: max(kappa-maxS)={gp2:.2e}, max(maxS-kappa)={gm2:.2e}; {len(susp)} points with |gap|>1e-9 after re-solve ({time.time()-t0:.0f}s)", flush=True)
        for s_ in susp[:5]: print("    ", s_)

"""Optimal-rank scan on the (m,3) stratum: for random points (and the padding example), compute kappa (hive LP), then
(i) max of s_{m+1}+s_{m+2}+... over the optimal face (max rank of optimizers' common spectrum support beyond m),
(ii) min rank r such that the rank-capped LP still attains kappa.
Usage: python rank_scan.py m z N"""
import sys, numpy as np
from scipy.optimize import linprog
from hive_core import HiveLP
from m3_forms import spec_m3, rand_m3

def max_tail(M, lam, val, m):
    # maximize sum_{t>m} s_t subject to hive constraints and sum s <= val + 1e-9
    c = np.zeros(M.nv); c[M.H + m:] = -1.0
    beq = np.zeros(M.neq)
    for t, r in enumerate(M.lam_rows): beq[r] = lam[t]
    from scipy.sparse import vstack, csr_matrix
    row = np.zeros(M.nv); row[M.H:] = 1.0
    Aub = vstack([M.Aub, csr_matrix(row)]); bub = np.concatenate([M.bub, [val + 1e-9]])
    res = linprog(c, A_ub=Aub, b_ub=bub, A_eq=M.Aeq, b_eq=beq, bounds=M.bounds, method='highs')
    return -res.fun, res.x[M.H:]

if __name__ == "__main__":
    m, z, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); d = m + z + 3
    M = HiveLP(d); caps = {r: HiveLP(d, rank_cap=r) for r in range(m, m + 3)}
    rng = np.random.default_rng(5)
    pts = []
    if m == 4:
        pts.append((np.array([17, 17, 17, 10]) / 61, np.array([25, 18, 18]) / 61))
    for i in range(N):
        pts.append(rand_m3(m, rng, law=['exp', 'unif', 'sq'][i % 3]))
    hist = {}
    for a, b in pts:
        lam = spec_m3(a, b, z); r = M.solve(lam); val = r['val']
        tail, s = max_tail(M, lam, val, m)
        nz = int(np.sum(s > 1e-7))          # rank of the tail-maximising optimizer
        rmin = None
        for rr in range(m, m + 3):
            rc = caps[rr].solve(lam)
            if rc is not None and rc['val'] < val + 1e-9: rmin = rr; break
        key = (rmin, nz); hist[key] = hist.get(key, 0) + 1
        if a[0] == 17 / 61: print("padding example: kappa*61 =", val * 61, "min rank", rmin, "max-tail optimizer s =", np.round(s * 61, 4), "rank", nz)
    print(f"m={m} z={z} d={d}: histogram of (min optimal rank, rank of tail-maximising optimizer): {dict(sorted(hist.items()))}")

"""Restricted Horn LP using only catalogue tiles, compared with the hive LP at random points.
Usage: python restricted.py m z N [umax]"""
import sys, time, numpy as np
from scipy.optimize import linprog
from catalogue import tile_rows
from hive_core import HiveLP
from m3_gather import rand_m3x, LAWS
from m3_forms import spec_m3

def restricted_lp(lam, rows):
    d = len(lam); A = [-a for a, b, _ in rows]; ub = [-(b @ lam) for a, b, _ in rows]
    for j in range(d - 2):
        e = np.zeros(d - 1); e[j] = -1; e[j + 1] = 1; A.append(e); ub.append(0.0)
    res = linprog(np.ones(d - 1), A_ub=np.array(A), b_ub=np.array(ub), bounds=[(0, None)] * (d - 1), method='highs')
    return res.fun, res.x, -res.ineqlin.marginals

if __name__ == "__main__":
    m, z, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); umax = int(sys.argv[4]) if len(sys.argv) > 4 else None
    maxholes = int(sys.argv[5]) if len(sys.argv) > 5 else 2; maxN = int(sys.argv[6]) if len(sys.argv) > 6 else 2
    d = m + z + 3; t0 = time.time(); rows = tile_rows(m, z, umax, maxholes, maxN); M = HiveLP(d)
    print(f"m={m} z={z} d={d}: {len(rows)} catalogue tiles ({time.time()-t0:.0f}s)", flush=True)
    rng = np.random.default_rng(3); worst = 0; wpt = None; used = {}
    for i in range(N):
        a, b = rand_m3x(m, rng, LAWS[i % len(LAWS)]); lam = spec_m3(a, b, z)
        v, s, y = restricted_lp(lam, rows); h = M.solve(lam)['val']
        gap = h - v
        if gap > worst: worst, wpt = gap, (a, b)
        for r, (A_, B_, info) in enumerate(rows):
            if y[r] > 1e-7: used[info] = used.get(info, 0) + 1
    print(f"  max (hiveLP - restrictedLP) over {N} points = {worst:.2e}; tiles used in some certificate: {len(used)}  ({time.time()-t0:.0f}s)")
    if worst > 1e-7: print("  worst point a=", np.round(wpt[0], 4), "b=", np.round(wpt[1], 4))
    for info, n in sorted(used.items(), key=lambda kv: -kv[1]):
        K, U, Nn, I, J = info
        Ka = [k for k in K if k <= m]; Kb = [{d: 1, d - 1: 2, d - 2: 3}[k] for k in K if k >= d - 2]
        print(f"    {n:5d}  +s{list(U)} -s{[f'd-{d-t}' for t in Nn]} >= {'+'.join('a%d'%k for k in Ka)}{''.join('-b%d'%i for i in Kb)}   I={I} J={J} K={K}")

"""Fresh-sample verification of kappa_d = max S(m,z) on inertia (m,3), S from closed_m{m}_z{0|1}.json.
Usage: python verify_formula.py m_min m_max N zlist seed   (d = m+z+3 <= 14 enforced)"""
import sys, json, time, numpy as np
from hive_core import HiveLP
from m3_forms import spec_m3
from m3_gather import rand_m3x, LAWS
m0, m1, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
zs = [int(x) for x in sys.argv[4].split(',')]; seed = int(sys.argv[5]) if len(sys.argv) > 5 else 2026
for m in range(m0, m1 + 1):
    for z in zs:
        d = m + z + 3
        if d > 14: print(f"m={m} z={z}: d={d} > 14, skipped"); continue
        S = np.array(json.load(open(f"closed_m{m}_z{0 if z == 0 else 1}.json")), float)
        M = HiveLP(d); rng = np.random.default_rng(seed + 100 * m + z); t0 = time.time(); worst = 0; wpt = None; nlaw = {}
        for i in range(N):
            law = LAWS[i % len(LAWS)]; a, b = rand_m3x(m, rng, law); lam = spec_m3(a, b, z)
            r = M.solve(lam)
            if r is None: print("  LP failure at", a, b); continue
            v = np.max(S[:, :m] @ a + S[:, m] * b[0] + S[:, m + 1] * b[1]); gap = abs(v - r['val'])
            if gap > worst: worst, wpt = gap, (law, a.copy(), b.copy(), v, r['val'])
        print(f"m={m} z={z} d={d} |S|={len(S)}: N={N} fresh points, max|kappa_LP - max S| = {worst:.2e}  ({time.time()-t0:.0f}s)", flush=True)
        if worst > 1e-9: print("   worst:", wpt)

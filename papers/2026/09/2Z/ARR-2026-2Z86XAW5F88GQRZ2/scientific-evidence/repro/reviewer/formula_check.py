"""Task (c): max-of-forms (closed_m{m}_z{0|1}.json) vs the reviewer's own Horn LP (d<=9, all Fulton triples) and own hive LP,
m = 3..9, z = 0,1 (and z=2 for m<=6), >= 250 random points per (m,z), six sampling laws, tight LP tolerances."""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, time, numpy as np
sys.path.insert(0, AUTHOR_DIR)
from horn_own import horn_rows, kappa_horn, Hive, spec, rand_point, form_val
W = AUTHOR_DIR
N = int(sys.argv[1]) if len(sys.argv) > 1 else 250
rng = np.random.default_rng(20260913)
rows = {}
for m in range(3, 10):
    for z in (0, 1, 2):
        d = m + z + 3
        if d > 14 or (z == 2 and m > 6): continue
        S = [tuple(f) for f in json.load(open(f"{W}/closed_m{m}_z{0 if z == 0 else 1}.json"))]
        Hv = Hive(d); t0 = time.time()
        if d <= 9 and d not in rows: rows[d] = horn_rows(d)
        wh = wH = 0.0; nbig = 0; worst_pt = None
        for i in range(N):
            a, b = rand_point(m, rng, law=i % 6); lam = spec(a, b, z)
            mx = max(form_val(g, a, b) for g in S)
            v = Hv.solve(lam)['val']; gap = v - mx
            if abs(gap) > wh: wh = abs(gap); worst_pt = (a, b, gap)
            if d <= 9:
                v2 = kappa_horn(lam, rows[d]).fun; wH = max(wH, abs(v2 - mx))
            if abs(gap) > 1e-12: nbig += 1
        print(f"m={m} z={z} d={d} |S|={len(S)}: N={N}: max|hive-maxS|={wh:.2e}" + (f", max|Horn-maxS|={wH:.2e}" if d <= 9 else "") +
              f", points with |gap|>1e-12: {nbig}  ({time.time()-t0:.0f}s)", flush=True)
        if nbig: print("   worst point:", np.round(worst_pt[0], 5), np.round(worst_pt[1], 5), worst_pt[2])

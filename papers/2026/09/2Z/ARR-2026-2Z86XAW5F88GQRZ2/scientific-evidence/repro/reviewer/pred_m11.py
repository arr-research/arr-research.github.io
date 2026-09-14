"""Task (f): out-of-sample test of the conjectured families A-F: m=11, z=1 (d=15), 300 random points, own hive LP (tight);
also m=10 z=1 (d=14) and m=12 z=1 (d=16) as extra; prediction regenerated from families2.gen2 and compared with pred_m11.json."""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, time, numpy as np
sys.path.insert(0, AUTHOR_DIR)
from horn_own import Hive, spec, rand_point, form_val
from families2 import gen2
W = AUTHOR_DIR
for m, N in ((11, 300), (10, 200), (12, 200)):
    G = gen2(m); pred = sorted(G); fam = {}
    for f, v in G.items(): fam[v[0][0]] = fam.get(v[0][0], 0) + 1
    try:
        saved = sorted(tuple(f) for f in json.load(open(f"{W}/pred_m{m}.json")))
        same = saved == pred
    except FileNotFoundError: same = None
    z = 1; d = m + z + 3; Hv = Hive(d); rng = np.random.default_rng(1100 + m); t0 = time.time()
    worst_lo = worst_hi = 0; missing = {}
    for i in range(N):
        a, b = rand_point(m, rng, law=i % 6); lam = spec(a, b, z)
        r = Hv.solve(lam); v = r['val']; mx = max(form_val(f, a, b) for f in pred)
        worst_lo = max(worst_lo, v - mx); worst_hi = max(worst_hi, mx - v)
        if v - mx > 1e-9:
            gr = r['grad']; key = tuple(np.round(gr, 6)); missing[key] = missing.get(key, 0) + 1
    print(f"m={m} z={z} d={d}: predicted forms {len(pred)} {dict(sorted(fam.items()))} (matches pred_m{m}.json: {same}); N={N}: "
          f"max(kappa - maxpred)={worst_lo:.2e}, max(maxpred - kappa)={worst_hi:.2e}; points with kappa > maxpred + 1e-9: {sum(missing.values())}  ({time.time()-t0:.0f}s)", flush=True)
    for k, n in missing.items(): print("   missing form (dual gradient):", k, n)

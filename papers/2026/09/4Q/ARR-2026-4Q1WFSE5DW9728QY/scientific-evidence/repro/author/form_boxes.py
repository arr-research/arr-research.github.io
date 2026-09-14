"""Experiment 3b: per-form minimal box count.  For every exposed form g of (m,n,z) (file forms_m{m}_n{n}_z{z}.json, d <= 9),
take an interior point of its chamber (strict radius-LP centre, interior to the stratum as well; any restricted-LP certificate attaining kappa there certifies g
itself, because a valid linear form h <= kappa = g near the point with h = g at the point equals g) and compute
B_min(g) = least B such that the Horn LP restricted to triples with box = min(|lambda(I)|,|lambda(J)|) <= B attains kappa.
Also records the max box over the tiles of the full-LP dual certificate returned at that point.
Usage: python form_boxes.py m n z"""
import sys, json, time, numpy as np
from collections import Counter
from mn_tools import *
from joint_lp import radius
from horn_lp import HornLP

if __name__ == "__main__":
    m, n, z = [int(x) for x in sys.argv[1:4]]; d = m + n + z; t0 = time.time()
    data = json.load(open(f"forms_m{m}_n{n}_z{z}.json")); S = [tuple(json.loads(k)) for k in data if not k.startswith('_')]
    H = HornLP(d); M = HiveLP(d); rows = []
    for f in S:
        rr, (a, b) = radius(f, [g for g in S if g != f], m, n, strict=True)
        assert rr > 1e-9, (f, rr)
        lam = spec(a, b, z); B, full = H.bmin(lam)
        kap = M.solve(lam)['val']; assert abs(kap - form_val(np.array(f, float), a, b)) < 1e-7 and abs(kap - full) < 1e-7
        r = H.solve(lam, want_dual=True); mb = max(H.info[k]['box'] for k, y in r['active'])
        c = data[str(list(f))]
        rows.append((B, mb, f, c['layering'], c['sched'], c['binv'], c['maxsize'], c['ordered'], c['full']))
    hist = Counter(r[0] for r in rows)
    print(f"(m,n,z)=({m},{n},{z}) d={d}: {len(S)} exposed forms; B_min histogram {dict(sorted(hist.items()))}; "
          f"max B_min = {max(r[0] for r in rows)}; max box in returned LP certificates = {max(r[1] for r in rows)}; {time.time()-t0:.0f}s")
    for r in sorted(rows, key=lambda r: (-r[0], r[2])):
        B, mb, f, lay, sched, binv, ms, o, fu = r
        tag = 'ORD-full' if (o and fu) else ('ord-a' if o else '')
        print(f"   B_min={B} (LP cert max box {mb}) {list(f)} sched={tuple(sched)} binv={binv} maxsize={ms} {tag}  {lay}")

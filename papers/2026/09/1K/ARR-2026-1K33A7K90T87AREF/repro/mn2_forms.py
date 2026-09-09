"""Collect exposed linear forms of kappa_d on the inertia-(m,2) stratum via hive-LP duals.
Usage: python mn2_forms.py m_min m_max n_samples pads(comma) [seed]
Form canonical coords: kappa = sum alpha_j a_j + beta_1 b_1 (beta_2 := 0 using sum a = sum b).
Output: forms_m{m}_pad{pad}.json with the rationalized forms and counts; also optimal s spectra sample.
"""
import sys, json, time, numpy as np
from fractions import Fraction as Q
from hive_core import HiveLP, spec_mn2, rand_mn2, canon_form, rat

m0, m1, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
pads = [int(x) for x in sys.argv[4].split(',')]
seed = int(sys.argv[5]) if len(sys.argv) > 5 else 0
for m in range(m0, m1 + 1):
    for pad in pads:
        d = m + 2 + pad; M = HiveLP(d); rng = np.random.default_rng(seed + 1000 * m + pad)
        found = {}; t0 = time.time(); bad = 0
        for i in range(N):
            a, b = rand_mn2(m, rng, law=['exp', 'unif', 'sq'][i % 3])
            lam = spec_mn2(a, b, pad); r = M.solve(lam)
            f = canon_form(r['grad'], m, pad)
            key = tuple(rat(x, 2000) for x in f)
            val = float(sum(float(k) * x for k, x in zip(key[:m], a))) + float(key[m]) * b[0]
            if abs(val - r['val']) > 1e-7: bad += 1; continue
            e = found.setdefault(key, dict(n=0, s=None, lam=None))
            e['n'] += 1
            if e['s'] is None: e['s'] = [float(x) for x in r['s']]; e['lam'] = [float(x) for x in lam]
        # completeness check on fresh samples
        forms = [np.array([float(x) for x in k]) for k in found]
        rng2 = np.random.default_rng(999 + m); err = 0
        for i in range(300):
            a, b = rand_mn2(m, rng2, law=['exp', 'unif', 'sq'][i % 3]); lam = spec_mn2(a, b, pad); r = M.solve(lam)
            v = max(f[:m] @ a + f[m] * b[0] for f in forms); err = max(err, abs(v - r['val']))
        print(f"m={m} pad={pad} d={d}: {len(found)} forms from {N} samples ({bad} unrationalizable), "
              f"max|maxforms-LP| on 300 fresh = {err:.1e}, {time.time()-t0:.0f}s", flush=True)
        out = {str([str(x) for x in k]): dict(n=v['n'], s=v['s'], lam=v['lam']) for k, v in found.items()}
        json.dump(out, open(f"forms_m{m}_pad{pad}.json", "w"), indent=1)
        for k, v in sorted(found.items(), key=lambda kv: -kv[1]['n']):
            print("   ", [str(x) for x in k], v['n'])

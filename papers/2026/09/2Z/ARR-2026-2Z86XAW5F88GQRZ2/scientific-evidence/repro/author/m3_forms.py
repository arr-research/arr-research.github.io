"""Collect exposed linear forms of kappa_d on the inertia-(m,3) stratum via hive-LP duals.
Usage: python m3_forms.py m_min m_max n_samples pads(comma) [seed]
lambda = (a_1..a_m, 0^z, -b_3, -b_2, -b_1).  Canonical coords: kappa = sum alpha_j a_j + beta_1 b_1 + beta_2 b_2 (beta_3 := 0).
Output: forms_m{m}_z{z}.json (rationalized forms, counts, sample points), and a summary line per (m,z)."""
import sys, json, time, numpy as np
from fractions import Fraction as Q
from hive_core import HiveLP, rat

def spec_m3(a, b, z=0):
    return np.array(list(a) + [0.0] * z + [-b[2], -b[1], -b[0]])

def rand_m3(m, rng, law='exp'):
    if law == 'exp':
        a = rng.exponential(size=m); b = rng.exponential(size=3)
    elif law == 'unif':
        a = rng.uniform(size=m); b = rng.uniform(size=3)
    else:
        a = rng.normal(size=m) ** 2; b = rng.normal(size=3) ** 2
    a = np.sort(a)[::-1]; b = np.sort(b)[::-1]
    return a / a.sum(), b / b.sum()

def canon(grad, m, z):
    d = m + z + 3
    alpha = grad[:m].copy(); beta3 = -grad[d - 3]; beta2 = -grad[d - 2]; beta1 = -grad[d - 1]
    t = -beta3   # shift so that beta3 -> 0: alpha - t, beta + t
    return np.concatenate([alpha - t, [beta1 + t, beta2 + t]])

if __name__ == "__main__":
    m0, m1, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    pads = [int(x) for x in sys.argv[4].split(',')]
    seed = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    for m in range(m0, m1 + 1):
        for z in pads:
            d = m + 3 + z; M = HiveLP(d); rng = np.random.default_rng(seed + 1000 * m + z)
            found = {}; t0 = time.time(); bad = 0
            for i in range(N):
                a, b = rand_m3(m, rng, law=['exp', 'unif', 'sq'][i % 3])
                lam = spec_m3(a, b, z); r = M.solve(lam)
                if r is None: bad += 1; continue
                f = canon(r['grad'], m, z)
                key = tuple(rat(x, 2000) for x in f)
                val = float(sum(float(k) * x for k, x in zip(key[:m], a))) + float(key[m]) * b[0] + float(key[m + 1]) * b[1]
                if abs(val - r['val']) > 1e-7: bad += 1; continue
                e = found.setdefault(key, dict(n=0, s=None, lam=None))
                e['n'] += 1
                if e['s'] is None: e['s'] = [float(x) for x in r['s']]; e['lam'] = [float(x) for x in lam]
            forms = [np.array([float(x) for x in k]) for k in found]
            rng2 = np.random.default_rng(999 + m); err = 0
            for i in range(300):
                a, b = rand_m3(m, rng2, law=['exp', 'unif', 'sq'][i % 3]); lam = spec_m3(a, b, z); r = M.solve(lam)
                v = max(f[:m] @ a + f[m] * b[0] + f[m + 1] * b[1] for f in forms); err = max(err, abs(v - r['val']))
            print(f"m={m} z={z} d={d}: {len(found)} forms from {N} samples ({bad} bad), max|maxforms-LP| on 300 fresh = {err:.1e}, {time.time()-t0:.0f}s", flush=True)
            out = {str([str(x) for x in k]): dict(n=v['n'], s=v['s'], lam=v['lam']) for k, v in found.items()}
            json.dump(out, open(f"forms_m{m}_z{z}.json", "w"), indent=1)
            for k, v in sorted(found.items(), key=lambda kv: -kv[1]['n']):
                print("   ", [str(x) for x in k], v['n'])

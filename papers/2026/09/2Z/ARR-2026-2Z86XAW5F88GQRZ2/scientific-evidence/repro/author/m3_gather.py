"""Heavier candidate-form gathering for inertia (m,3), with tie-heavy sampling laws.
Usage: python m3_gather.py m_min m_max N pads seed -> cand_m{m}_z{z}.json  {form: {n, lam}}"""
import sys, json, time, numpy as np
from fractions import Fraction as Q
from hive_core import HiveLP, rat
from m3_forms import spec_m3, canon

def rand_m3x(m, rng, law):
    if law == 'exp':   a = rng.exponential(size=m); b = rng.exponential(size=3)
    elif law == 'unif': a = rng.uniform(size=m); b = rng.uniform(size=3)
    elif law == 'sq':  a = rng.normal(size=m) ** 2; b = rng.normal(size=3) ** 2
    elif law == 'tie':   # blocks of equal a's, b with possible ties, then small noise
        k = rng.integers(1, m + 1); vals = np.sort(rng.exponential(size=k))[::-1]
        a = vals[np.sort(rng.integers(0, k, size=m))]; a = a * (1 + 1e-3 * rng.normal(size=m))
        b = np.sort(rng.exponential(size=3))[::-1]
        r = rng.integers(3)
        if r == 0: b[2] = b[1]
        elif r == 1: b[1] = b[0]
        b = b * (1 + 1e-3 * rng.normal(size=3))
    elif law == 'dom':   # one dominant a or geometric decay
        q = rng.uniform(0.1, 0.9); a = q ** np.arange(m) * rng.uniform(0.5, 1.5, size=m)
        b = rng.exponential(size=3) ** rng.uniform(0.5, 2)
    elif law == 'flatb': # nearly flat b, a spread
        a = rng.exponential(size=m); b = 1 + 0.05 * rng.normal(size=3)
    elif law == 'ex':    # neighbourhood of the padding example (17,17,17,10)/7, (25,18,18)/7 scaled up to length m
        a = np.concatenate([np.full(3, 17.0), np.full(m - 3, 10.0)])[:m] if m >= 3 else np.array([17.0, 10.0])[:m]
        a = a * (1 + 0.05 * rng.normal(size=m)); b = np.array([25.0, 18.0, 18.0]) * (1 + 0.05 * rng.normal(size=3))
    a = np.abs(a); b = np.abs(b)
    a = np.sort(a)[::-1]; b = np.sort(b)[::-1]
    return a / a.sum(), b / b.sum()

LAWS = ['exp', 'unif', 'sq', 'tie', 'dom', 'flatb', 'ex', 'tie', 'tie']
if __name__ == "__main__":
    m0, m1, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    pads = [int(x) for x in sys.argv[4].split(',')]
    seed = int(sys.argv[5]) if len(sys.argv) > 5 else 7
    for m in range(m0, m1 + 1):
        for z in pads:
            d = m + 3 + z; M = HiveLP(d); rng = np.random.default_rng(seed + 1000 * m + z)
            found = {}; t0 = time.time(); bad = 0
            for i in range(N):
                a, b = rand_m3x(m, rng, LAWS[i % len(LAWS)])
                lam = spec_m3(a, b, z); r = M.solve(lam)
                if r is None: bad += 1; continue
                f = canon(r['grad'], m, z); key = tuple(rat(x, 2000) for x in f)
                val = float(sum(float(k) * x for k, x in zip(key[:m], a))) + float(key[m]) * b[0] + float(key[m + 1]) * b[1]
                if abs(val - r['val']) > 1e-7 or any(k.denominator > 1 for k in key): bad += 1; continue
                e = found.setdefault(key, dict(n=0, lam=None)); e['n'] += 1
                if e['lam'] is None: e['lam'] = [float(x) for x in lam]
            print(f"m={m} z={z} d={d}: {len(found)} candidate forms from {N} samples ({bad} bad/nonintegral), {time.time()-t0:.0f}s", flush=True)
            json.dump({str([str(x) for x in k]): v for k, v in found.items()}, open(f"cand_m{m}_z{z}.json", "w"), indent=1)

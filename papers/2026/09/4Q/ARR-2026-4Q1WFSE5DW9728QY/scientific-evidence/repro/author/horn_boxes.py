"""Experiment 3: how many boxes do the certificates need?  For random points of (m,n,z) strata with d <= 9:
B_min(lambda) = least B such that the Horn LP restricted to triples with box = min(|lambda(I)|,|lambda(J)|) <= B attains kappa.
Also lists, for the full-LP dual certificate at each point, the shapes (lambda(I), lambda(J), lambda(K)) of the active
non-Lidskii triples, whether lambda(K) is a rectangle, and the max |lambda(J)|.
Usage: python horn_boxes.py "m,n,z;..." N [seed]"""
import sys, time, numpy as np
from collections import Counter
from mn_tools import *
from horn_lp import HornLP

if __name__ == "__main__":
    cases = [tuple(int(x) for x in c.split(',')) for c in sys.argv[1].split(';')]
    N = int(sys.argv[2]); seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    for (m, n, z) in cases:
        d = m + n + z; t0 = time.time(); H = HornLP(d); M = HiveLP(d)
        rng = np.random.default_rng(seed + 100 * m + 10 * n + z)
        bhist = Counter(); shapes = Counter(); rectK = Counter(); maxJ = Counter(); dev = 0.0; bylaw = {}
        for i in range(N):
            law = LAWS[i % len(LAWS)]
            a, b = rand_ab(m, n, rng, law); lam = spec(a, b, z)
            B, full = H.bmin(lam); bhist[B] += 1
            bylaw.setdefault(law, Counter())[B] += 1
            dev = max(dev, abs(full - M.solve(lam)['val']))
            r = H.solve(lam, want_dual=True)
            mj = 0
            for (k, y) in r['active']:
                inf = H.info[k]
                if inf['box'] > 0:
                    shapes[(inf['lI'], inf['lJ'], inf['lK'])] += 1
                    rectK[inf['rectK']] += 1
                mj = max(mj, inf['box'])
            maxJ[mj] += 1
        print(f"(m,n,z)=({m},{n},{z}) d={d}: {len(H.triples)} triples; N={N}; max|HornLP-hive|={dev:.1e}; "
              f"B_min histogram {dict(sorted(bhist.items()))}; by law {{{', '.join(f'{k}:{dict(sorted(v.items()))}' for k, v in bylaw.items())}}}; "
              f"max box in the returned dual certificate: {dict(sorted(maxJ.items()))}; "
              f"lambda(K) rectangle among active non-LW tiles: {dict(rectK)}; {time.time()-t0:.0f}s", flush=True)
        print("   most frequent active non-LW shapes (lI, lJ, lK): count")
        for sh, c in shapes.most_common(12): print("     ", sh, c)

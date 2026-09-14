"""Experiment 4b: how much of the (m,n) stratum is covered by the Theorem-2B regions R_k = {tau_i(k) <= b_i <= tau_{i-1}(k)}
(union over k = 1..m), and by the aligned-spike cone (measure zero, not sampled)?  Also: the fraction of points where the
argmax is a single-mixed-layer form (the cost of some L_k), i.e. the chamber union of the L_k, for comparison.
Usage: python region_coverage.py "m,n;..." N [seed]"""
import sys, numpy as np
from mn_tools import *
from interlace_test import tau, layering_Lk

if __name__ == "__main__":
    cases = [tuple(int(x) for x in c.split(',')) for c in sys.argv[1].split(';')]
    N = int(sys.argv[2]); seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    for (m, n) in cases:
        d = m + n; M = HiveLP(d); rng = np.random.default_rng(seed + 100 * m + 10 * n)
        forms_k = {k: form_of_layering(layering_Lk(m, n, k), m, n) for k in range(1, m + 1)}
        inR = 0; argLk = 0; both = 0; tot = 0
        for i in range(N):
            law = LAWS[i % 4]     # exclude 'dom' (never in an ordered chamber)
            a, b = rand_ab(m, n, rng, law); lam = spec(a, b, 0); kap = M.solve(lam)['val']; tot += 1
            r = any(all(tau(a, k, n)[i - 1] - 1e-12 <= b[i - 1] <= tau(a, k, n)[i - 2] + 1e-12 for i in range(2, n + 1)) for k in range(1, m + 1))
            g = any(abs(form_val(np.array(f, float), a, b) - kap) < 1e-9 for f in forms_k.values())
            inR += r; argLk += g; both += (r and g)
        print(f"(m,n)=({m},{n}): N={tot} (laws exp/unif/sq/tie): in some R_k: {inR} ({100*inR/tot:.1f}%); some L_k is an argmax: {argLk} ({100*argLk/tot:.1f}%); "
              f"R_k points where L_k is argmax: {both}/{inR}")

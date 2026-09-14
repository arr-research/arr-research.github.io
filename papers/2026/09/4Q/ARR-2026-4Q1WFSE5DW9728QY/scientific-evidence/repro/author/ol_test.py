"""Experiment 1: kappa (hive LP) versus the ordered-layering bound OL = max over full-capacity ordered layerings
(any b-schedule) and OL_A (nondecreasing schedules = family A proper), on random (m,n,z) spectra.
Checks: (i) OL <= kappa always (Theorem 1 sanity), (ii) fraction of points with kappa = OL / OL_A,
(iii) the "at most c_u" version: max over under-filled ordered layerings can exceed kappa.
Usage: python ol_test.py "m,n,z;m,n,z;..." N seed"""
import sys, time, itertools, numpy as np
from mn_tools import *

def underfilled_forms(m, n):
    """Ordered a's, arbitrary schedule, layer u holds q_u <= c_u a's (at least one a in every layer >= 1 that has capacity,
    to keep it finite) -- enumerate for small m: choose the sequence q_u."""
    out = {}
    for u in all_schedules(m, n):
        T = max(u)
        caps = []
        t = 1
        while True:
            c = sum(1 for ui in u if ui < t)
            caps.append(c);
            if sum(caps) >= m and t >= T: break
            t += 1
            if t > m + T + 2: break
        # choose q_t in 1..cap_t (0 allowed only if cap = 0) with sum = m
        rngs = [range(0, 1) if c == 0 else range(1, c + 1) for c in caps]
        for q in itertools.product(*rngs):
            if sum(q) != m: continue
            layers = [[] for _ in range(max(T, len(q)) + 1)]
            for i, ui in enumerate(u): layers[ui].append(('b', i + 1))
            j = 1
            for t, qt in enumerate(q, start=1):
                for _ in range(qt): layers[t].append(('a', j)); j += 1
            if not any(k == 'a' for k, _ in layers[-1]): continue
            f = form_of_layering(layers, m, n)
            out.setdefault(f, (u, layers))
    return out

if __name__ == "__main__":
    cases = [tuple(int(x) for x in c.split(',')) for c in sys.argv[1].split(';')]
    N = int(sys.argv[2]); seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    for (m, n, z) in cases:
        d = m + n + z; t0 = time.time()
        M = HiveLP(d); rng = np.random.default_rng(seed + 100 * m + 10 * n + z)
        F_all = ordered_forms(m, n); F_A = ordered_forms(m, n, nondecreasing=True)
        F_under = underfilled_forms(m, n) if m <= 6 else {}
        eq_all = eq_A = 0; worst_viol = -np.inf; under_viol = 0; under_max = 0.0; gaps = []
        bylaw = {law: [0, 0] for law in LAWS}
        for i in range(N):
            law = LAWS[i % len(LAWS)]
            a, b = rand_ab(m, n, rng, law); lam = spec(a, b, z); r = M.solve(lam)
            if r is None: continue
            kap = r['val']
            v_all, _ = max_ordered(F_all, a, b); v_A, _ = max_ordered(F_A, a, b)
            worst_viol = max(worst_viol, v_all - kap)
            gaps.append(kap - v_all)
            bylaw[law][1] += 1
            if abs(kap - v_all) < 1e-8: eq_all += 1; bylaw[law][0] += 1
            if abs(kap - v_A) < 1e-8: eq_A += 1
            if F_under:
                v_u, _ = max_ordered(F_under, a, b)
                if v_u > kap + 1e-8: under_viol += 1; under_max = max(under_max, v_u - kap)
        gaps = np.array(gaps)
        print(f"(m,n,z)=({m},{n},{z}) d={d}: {len(F_all)} ordered forms ({len(F_A)} family-A); N={N}: "
              f"max(OL-kappa)={worst_viol:.1e} [must be <=0]; kappa=OL at {eq_all}/{N} ({100*eq_all/N:.1f}%), "
              f"kappa=OL_A at {eq_A}/{N} ({100*eq_A/N:.1f}%); mean gap {gaps.mean():.4f}, max gap {gaps.max():.4f}; "
              f"by law {{{', '.join(f'{k}:{v[0]}/{v[1]}' for k, v in bylaw.items())}}}; "
              f"under-filled forms ({len(F_under)}) exceed kappa at {under_viol} points (max excess {under_max:.4f}); {time.time()-t0:.0f}s", flush=True)

"""Conjectured closed formula for inertia (m,2):
lambda = (a_1>=...>=a_m>0, 0^z, -b_2, -b_1), b_1>=b_2>0, sum a = b_1+b_2 = P.
Family I  (k = 0..m-1):  F_k = k b_1 + sum_j c_k(j) a_j,  c_k(j) = j-k (j<=k), ceil((j-k)/2) (j>=k).
Family II (j odd, 1<=j<=m): G_j = b_2 + sum_i floor(i/2) a_i + (a_j - a_{j+1})  [a_{m+1} := 0].
kappa = max of all these.
"""
import math
from fractions import Fraction as Q

def forms_mn2(m):
    """Return list of (name, alpha (len m), beta1, beta2) with kappa >= alpha.a + beta1 b1 + beta2 b2."""
    out = []
    for k in range(m):
        alpha = [(j - k) if j <= k else math.ceil((j - k) / 2) for j in range(1, m + 1)]
        out.append((f"F{k}", alpha, k, 0))
    for j in range(1, m + 1, 2):
        alpha = [i // 2 for i in range(1, m + 1)]
        alpha[j - 1] += 1
        if j + 1 <= m: alpha[j] -= 1
        out.append((f"G{j}", alpha, 0, 1))
    return out

def kappa_conj(a, b, with_argmax=False):
    m = len(a); best = None
    for name, alpha, b1c, b2c in forms_mn2(m):
        v = sum(x * y for x, y in zip(alpha, a)) + b1c * b[0] + b2c * b[1]
        if best is None or v > best[0]: best = (v, name)
    return best if with_argmax else best[0]

if __name__ == "__main__":
    import sys, time, numpy as np
    from hive_core import HiveLP, spec_mn2, rand_mn2
    rng = np.random.default_rng(2024)
    for m in range(2, 13):
        for pad in (0, 1, 3):
            d = m + 2 + pad; M = HiveLP(d); err = 0; t0 = time.time()
            n = 400 if m <= 8 else 150
            for i in range(n):
                a, b = rand_mn2(m, rng, law=['exp', 'unif', 'sq'][i % 3])
                if i % 5 == 4:   # degenerate cases
                    r = rng.integers(4)
                    if r == 0: b = np.array([1.0, 0.0])            # one-spike limit
                    elif r == 1: b = np.array([0.5, 0.5])          # b1=b2
                    elif r == 2: a = np.ones(m) / m               # flat a
                    else: a[1:] = a[1:].mean(); a = a / a.sum()   # A_N-type
                r = M.solve(spec_mn2(a, b, pad))
                err = max(err, abs(r['val'] - kappa_conj(list(a), list(b))))
            print(f"m={m} pad={pad} d={d}: max|LP - conj| = {err:.1e} over {n} ({time.time()-t0:.0f}s)", flush=True)

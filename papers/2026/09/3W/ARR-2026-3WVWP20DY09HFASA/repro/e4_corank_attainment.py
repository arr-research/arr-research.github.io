"""E4: every corank k in {0,...,l-1} is attained by a matrix of EXACT Weyl sparsity l (l <= p) with collinear support:
f(z) = prod_{i<k} (z - omega^i) * prod_{j<l-1-k} (z - alpha_j) with random alpha_j; check exactly l nonzero coefficients
(numerically, |coeff| > 1e-9) and exactly k zeros among p-th roots of unity, hence nullity k for C = f(Z)."""
import numpy as np, sys
rng = np.random.default_rng(3)
for p in [5, 7, 11, 13]:
    ok = True
    for l in range(1, p+1):
        for k in range(0, l):
            w = np.exp(2j*np.pi/p)
            roots = [w**i for i in range(k)] + list(rng.normal(size=l-1-k) + 1j*rng.normal(size=l-1-k))
            coeffs = np.poly(roots) if roots else np.array([1.0])
            nz = np.sum(np.abs(coeffs) > 1e-9)
            vals = np.polyval(coeffs, w**np.arange(p))
            zeros = np.sum(np.abs(vals) < 1e-9)
            if nz != l or zeros != k: ok = False; print("FAIL", p, l, k, nz, zeros)
    print(f"p={p}: all pairs (l,k), 1<=l<=p, 0<=k<=l-1: exact sparsity l and corank k attained: {ok}")

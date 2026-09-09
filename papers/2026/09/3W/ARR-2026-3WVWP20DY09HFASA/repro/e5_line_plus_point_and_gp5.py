"""E5: (i) exact check of the 'line + one point' lemma: for S = {(0,b): b in B} u {(a,b')}, a != 0, all coefficients
nonzero in Z[omega], rank C >= p-1 (nullity <= 1); random instances p = 5, 7, 11, exact rank over Q(omega).
(ii) numerical minimiser for the general-position 5-set in p = 5 reaching nullity 2: print |c_g| to confirm all
coefficients are bounded away from zero (i.e. the point is not on a sub-support)."""
import random, numpy as np, sys
sys.path.insert(0, '.')
from e2_exact_padic_checks import make_ring, build, rank_Qomega
random.seed(11)
for p in [5, 7, 11]:
    R = make_ring(p); worst = p
    for trial in range(30 if p < 11 else 8):
        l = random.randint(2, min(6, p-1))
        B = random.sample(range(p), l-1); a = random.randrange(1, p); b2 = random.randrange(p)
        S = [(0, b) for b in B] + [(a, b2)]
        coeffs = []
        for _ in S:
            while True:
                c = R['canon'](tuple(random.randint(-2, 2) for _ in range(p)))
                if not R['iszero'](c): break
            coeffs.append(c)
        rk = rank_Qomega(R, p, build(R, p, S, coeffs))
        assert rk >= p-1, (p, S, rk)
        worst = min(worst, rk)
    print(f"(i) p={p}: line+point supports, exact rank >= p-1 in all instances (min rank seen {worst})")
from e1_orbits_numeric import weyl_np, min_sigma
p = 5; S = [(0,0),(1,0),(0,1),(1,1),(2,3)]
Ws = [weyl_np(p, a, b) for a, b in S]
v, c = min_sigma(Ws, p, 2, 60, np.random.default_rng(1))
print(f"(ii) p=5 general-position 5-set {S}: min sigma_4 = {v:.2e}, |c| = {np.round(np.abs(c),4)}")

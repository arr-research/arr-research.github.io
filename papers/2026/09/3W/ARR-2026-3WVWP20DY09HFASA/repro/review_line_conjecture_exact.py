"""EXACT certificate (Z[omega_5], rank via regular representation over Q) that the 'line conjecture'
(nullity <= maxcollinear - 1) is false in p = 5:
   S = parabola {(t, t^2)} (no three collinear, checked), C_k = sum_t omega^{f_k(t)} W_{(t,t^2)},
   f_k(t) = sum_{i<t} (i^2 + i - k)  (eigenvectors of Phi(C) = W_(1,1) Q_2 C Q_2^{-1}, eigenvalue omega^k).
Claim: rank C_k = 3 (nullity 2) for all k = 0..4, all five coefficients nonzero (roots of unity).
Also: numerical identification attempt for the author's orbit-6000 candidate.
"""
import sys, itertools
sys.path.insert(0, '.')
from fractions import Fraction
from review_check_proof import Cyc, weyl, rank_Q

p = 5; R = Cyc(p)
S = [(t, t*t % p) for t in range(p)]
for A, B, Cc in itertools.combinations(S, 3):
    assert ((B[0]-A[0])*(Cc[1]-A[1]) - (B[1]-A[1])*(Cc[0]-A[0])) % p != 0
print("parabola", S, ": no three points collinear (exact)")

def rank_Qomega(C):
    n = p - 1
    def regrep(u):
        cols = [list(R.mul(u, R.om(j))[:n]) for j in range(n)]
        return [[cols[j][i] for j in range(n)] for i in range(n)]
    N = p*n
    big = [[Fraction(0)]*N for _ in range(N)]
    for i in range(p):
        for j in range(p):
            m = regrep(C[i][j])
            for r in range(n):
                for c in range(n):
                    big[i*n+r][j*n+c] = Fraction(m[r][c])
    rk = rank_Q(big); assert rk % n == 0
    return rk // n

for k in range(p):
    f = []; acc = 0
    for t in range(p):
        f.append(acc % p); acc += t*t + t - k
    C = [[R.zero() for _ in range(p)] for _ in range(p)]
    for (a, b), e in zip(S, f):
        W = weyl(R, p, a, b)
        for i in range(p):
            for j in range(p):
                C[i][j] = R.add(C[i][j], R.mul(R.om(e), W[i][j]))
    rk = rank_Qomega(C)
    print(f"k={k}: C = sum_t omega^f(t) W_(t,t^2) with f = {f}; exact rank over Q(omega_5) = {rk}, nullity = {p-rk}")
    assert rk == 3

# Also verify by an explicit exact kernel: solve C v = 0 over Q(omega) via the regular representation is implicit in the rank.
print("EXACT: nullity 2 on a general-position 5-set in p = 5 (five distinct coefficient vectors, all coefficients nonzero).")
print("Line conjecture (nullity <= maxcollinear - 1 = 1) is FALSE; Theorem 1 (nullity <= l - 1 = 4) is respected.")

# numerical identification attempt for the author's candidate (orbit of size 6000)
try:
    import mpmath, numpy as np
    from review_line_conjecture import search, W
    rng = np.random.default_rng(5)
    S2 = [(0,0),(1,0),(0,1),(1,1),(2,3)]
    val, c = search(S2, 2, 40, rng, iters=2000)
    r = np.abs(c/c[0])**2
    print(f"\nauthor's candidate {S2}: sigma_4 = {val:.1e}; |c_i/c_0|^2 = {np.round(r, 10)}")
    for i in range(1, 5):
        pol = mpmath.findpoly(mpmath.mpf(float(r[i])), 4, maxcoeff=200, tol=1e-7)
        print(f"   |c_{i}/c_0|^2 ~ {r[i]:.10f}: findpoly(deg<=4, coeffs<=200) -> {pol}")
except Exception as ex:
    print("identification skipped:", ex)

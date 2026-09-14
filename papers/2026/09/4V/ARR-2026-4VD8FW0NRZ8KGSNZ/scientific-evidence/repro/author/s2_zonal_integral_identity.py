# s2: exact symbolic verification of the K-average (Laplace/Koornwinder-type) representation
#     Q_{n,d}(t) = E[ (t - (1-t) u + 2 i sqrt(t(1-t)) sqrt(u) cos(phi))^n ],   u ~ Beta(1, d-2),  phi ~ Uniform[0, pi]  (independent)
# against the Jacobi definition  Q_{n,d}(t) = P_n^{(d-2,0)}(2t-1) / C(n+d-2, n),  as polynomials in t, for n <= NMAX, d in {3,4,5,6}.
# Moments used: E[cos^j phi] = 0 (j odd), C(j, j/2)/2^j (j even);  E[u^m] = 1 / C(m+d-2, m).
# Also validates the exact Fraction recurrence of s1 against sympy.jacobi.
import sympy as sp, sys, time
from math import comb
from fractions import Fraction as Fr
sys.path.insert(0, '.')
from s1_exact_simplex_spectra import Q_seq

t = sp.symbols('t')
def Ez_pow(n, d):
    tot = sp.Integer(0)
    for j in range(0, n + 1, 2):           # even powers of the imaginary term only
        cj = sp.binomial(n, j) * (2 * sp.I) ** j * (t * (1 - t)) ** (j // 2) * sp.Rational(comb(j, j // 2), 2 ** j)
        inner = sp.Integer(0)
        for i in range(0, n - j + 1):      # (t - (1-t) u)^{n-j} expanded, u^{i + j/2} averaged
            m = i + j // 2
            inner += sp.binomial(n - j, i) * t ** (n - j - i) * (-(1 - t)) ** i * sp.Rational(1, comb(m + d - 2, m))
        tot += cj * inner
    return sp.expand(tot)

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 40
t0 = time.time()
for d in (3, 4, 5, 6):
    for n in range(0, NMAX + 1):
        lhs = Ez_pow(n, d)
        rhs = sp.expand(sp.jacobi(n, d - 2, 0, 2 * t - 1) / sp.binomial(n + d - 2, n))
        assert sp.expand(lhs - rhs) == 0, (d, n)
    print(f"d={d}: identity E[z^n] = P_n^{{({d-2},0)}}(2t-1)/C(n+{d-2},n) holds exactly as polynomials in t for 0<=n<={NMAX}  [OK]")
# recurrence (s1) vs sympy at the two overlaps used
for d, tv in ((4, Fr(1, 16)), (3, Fr(1, 9)), (3, Fr(4, 9)), (5, Fr(1, 25))):
    Q = Q_seq(d, tv, NMAX)
    for n in range(NMAX + 1):
        ref = sp.Rational(sp.jacobi(n, d - 2, 0, 2 * sp.Rational(tv) - 1)) / sp.binomial(n + d - 2, n)
        assert sp.Rational(Q[n].numerator, Q[n].denominator) == ref, (d, tv, n)
    print(f"d={d}, t={tv}: Fraction recurrence == sympy.jacobi for n<={NMAX}  [OK]")
print(f"runtime {time.time()-t0:.1f}s")

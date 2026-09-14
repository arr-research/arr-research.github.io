"""Exact check (Z[omega_d]) of the Theorem Z lower-bound construction
   f_r(z) = prod_{j=1}^k prod_{i=1}^{r_{j-1}} (z^{p^{j-1}} - omega_p^i),  omega_p = omega_d^{p^{k-1}}.
For every r < d: number of nonzero coefficients == w_p(r) and number of zeros in mu_d == r (exactly).
usage: python thmZ_construction.py d [d ...]
"""
import sys
from cyclo import Cyclo

def factor_pk(d):
    p = 2
    while d % p: p += 1
    k = 0
    while d % p == 0: d //= p; k += 1
    assert d == 1
    return p, k

def digit_weight(r, p):
    w = 1
    while r: w *= (r % p) + 1; r //= p
    return w

def polymul(F, a, b):
    """polynomials in z with coefficients in Z[omega] (lists of F-elements, low->high)"""
    c = [F.zero() for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        if F.is_zero(x): continue
        for j, y in enumerate(b):
            if F.is_zero(y): continue
            c[i+j] = F.add(c[i+j], F.mul(x, y))
    return c

def run(d):
    p, k = factor_pk(d)
    F = Cyclo(d)
    bad = 0
    for r in range(d):
        digits = []
        rr = r
        for j in range(k): digits.append(rr % p); rr //= p
        f = [F.one()]
        for j in range(1, k+1):
            for i in range(1, digits[j-1]+1):
                # z^{p^{j-1}} - omega_p^i
                g = [F.zero() for _ in range(p**(j-1)+1)]
                g[0] = F.neg(F.root_pow(i * p**(k-1)))
                g[-1] = F.one()
                f = polymul(F, f, g)
        nterms = sum(1 for c in f if not F.is_zero(c))
        # zeros in mu_d: evaluate at omega^t
        zeros = 0
        for t in range(d):
            val = F.zero()
            for e, c in enumerate(f):
                if not F.is_zero(c):
                    val = F.add(val, F.mul(c, F.root_pow(e*t)))
            if F.is_zero(val): zeros += 1
        deg = max(e for e, c in enumerate(f) if not F.is_zero(c))
        if nterms != digit_weight(r, p) or zeros != r or deg != r:
            bad += 1
            print(f"  d={d} r={r}: terms={nterms} (w_p={digit_weight(r,p)}), zeros={zeros}, deg={deg}  <-- MISMATCH")
    print(f"d={d} (p={p},k={k}): all r<d checked exactly in Z[omega_{d}]; mismatches={bad}")

for a in sys.argv[1:]:
    run(int(a))

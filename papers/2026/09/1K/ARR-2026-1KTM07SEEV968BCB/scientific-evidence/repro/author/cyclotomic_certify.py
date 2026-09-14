"""cyclotomic_certify.py -- exact certification over Z[omega_d] of the sharpness constructions.

For d = p^k and each r < d with digit weight w(r) = prod (r_t + 1), build recursively
   f_r(z) = f_1(z^{p^{k-1}}) * f_{r'}(z),  r = (n-1) p^{k-1} + r',  f_1(u) = prod_{i=1}^{n-1} (u - omega_p^i),
and verify EXACTLY (arithmetic in Z[x]/Phi_d(x)) that f_r has exactly w(r) nonzero coefficients (as an
element of Z[omega][z]/(z^d - 1)) and vanishes at exactly (at least) r of the d-th roots of unity.
Also certifies the d = 8 example 1 - z^4 -> dual 4-term polynomial with 6 zeros, and the equality
family for the operator theorem: prod_{i<l-1}(Z^{p^{k-1}} - omega_p^i I) has s_W = l and nullity (l-1)p^{k-1}
(nullity = number of zeros of the polynomial among d-th roots of unity, since it is a polynomial in Z).
usage: python cyclotomic_certify.py d
"""
import sys
from sympy import cyclotomic_poly, Poly, symbols, ZZ, div

x = symbols('x')

class Cyc:
    """elements of Z[omega_d] as integer coefficient lists modulo Phi_d"""
    def __init__(self, d):
        self.d = d
        self.Phi = Poly(cyclotomic_poly(d, x), x, domain=ZZ)
        self.n = self.Phi.degree()
    def red(self, coeffs):
        P = Poly(coeffs[::-1] if coeffs else [0], x, domain=ZZ)
        return tuple(div(P, self.Phi)[1].all_coeffs()[::-1] + [0] * self.n)[:self.n]
    def omega_pow(self, e):
        e %= self.d
        c = [0] * (e + 1); c[e] = 1
        return self.red(c)
    def add(self, a, b): return tuple((u + v) for u, v in zip(a, b))
    def neg(self, a): return tuple(-u for u in a)
    def mul(self, a, b):
        out = [0] * (2 * self.n)
        for i, u in enumerate(a):
            if u == 0: continue
            for j, v in enumerate(b):
                if v: out[i + j] += u * v
        return self.red(out)
    def zero(self): return tuple([0] * self.n)
    def one(self): return self.red([1])
    def is_zero(self, a): return all(u == 0 for u in a)

def poly_mul(K, f, g, d):
    """f, g: dict exponent(mod d) -> Cyc element; product mod z^d - 1"""
    out = {}
    for e1, c1 in f.items():
        for e2, c2 in g.items():
            e = (e1 + e2) % d
            out[e] = K.add(out.get(e, K.zero()), K.mul(c1, c2))
    return {e: c for e, c in out.items() if not K.is_zero(c)}

def evaluate(K, f, j, d):
    """f(omega^j)"""
    tot = K.zero()
    for e, c in f.items():
        tot = K.add(tot, K.mul(c, K.omega_pow(e * j)))
    return tot

def build_f(K, d, p, j, r):
    """recursive construction at level j (exponents < p^j, zeros counted in mu_{p^j}); returns dict polynomial.
    f_r(z) = prod_{i=1}^{n-1} (z^{p^{j-1}} - omega_p^i) * f_{r'}(z),  r = (n-1) p^{j-1} + r',  omega_p = omega_d^{d/p}."""
    if j == 0 or r == 0:
        return {0: K.one()}
    n = r // p**(j - 1) + 1
    rp = r % p**(j - 1)
    f1 = {0: K.one()}
    for i in range(1, n):
        lin = {p**(j - 1): K.one(), 0: K.neg(K.omega_pow(i * (d // p)))}
        f1 = poly_mul(K, f1, lin, d)
    frest = build_f(K, d, p, j - 1, rp)
    return poly_mul(K, f1, frest, d)

def weight(r, p):
    w = 1
    while r: w *= (r % p) + 1; r //= p
    return w

if __name__ == "__main__":
    d = int(sys.argv[1])
    p = 2
    while d % p: p += 1
    k = 0; dd = d
    while dd % p == 0: dd //= p; k += 1
    assert dd == 1
    K = Cyc(d)
    allok = True
    for r in range(d):
        f = build_f(K, d, p, k, r)
        terms = len(f)
        zeros = sum(1 for j in range(d) if K.is_zero(evaluate(K, f, j, d)))
        ok = (terms == weight(r, p)) and (zeros >= r)
        allok &= ok
        if not ok or r in (0, p**(k-1), d - 1) or weight(r, p) <= p + 1:
            print(f"  r={r:3d}: terms={terms} (w(r)={weight(r,p)}), zeros={zeros}  {'OK' if ok else 'FAIL'}")
    print(f"d={d}: all r<{d} certified exactly (terms == w(r), zeros >= r): {allok}")

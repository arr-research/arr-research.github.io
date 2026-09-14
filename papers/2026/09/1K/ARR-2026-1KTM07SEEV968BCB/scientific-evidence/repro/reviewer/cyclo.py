"""Minimal exact arithmetic in Z[omega_n] = Z[x]/(Phi_n(x)). Elements are integer lists of length phi(n)."""
from sympy import cyclotomic_poly, Poly, symbols
_x = symbols('x')

class Cyclo:
    def __init__(self, n):
        self.n = n
        P = Poly(cyclotomic_poly(n, _x), _x)
        self.phi = [int(c) for c in P.all_coeffs()[::-1]]  # low -> high, monic
        self.deg = P.degree()
    def zero(self): return [0]*self.deg
    def one(self):
        v = [0]*self.deg; v[0] = 1; return v
    def reduce(self, coeffs):
        c = list(coeffs)
        D = self.deg
        for i in range(len(c)-1, D-1, -1):
            if c[i]:
                f = c[i]
                for j in range(D+1):
                    c[i-D+j] -= f*self.phi[j]
        c = c[:D] + [0]*(D-len(c)) if len(c) < D else c[:D]
        return c
    def root_pow(self, t):
        """omega^t"""
        t %= self.n
        v = [0]*(t+1); v[t] = 1
        return self.reduce(v)
    def add(self, a, b): return [x+y for x, y in zip(a, b)]
    def sub(self, a, b): return [x-y for x, y in zip(a, b)]
    def neg(self, a): return [-x for x in a]
    def mul(self, a, b):
        D = self.deg
        c = [0]*(2*D-1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y: c[i+j] += x*y
        return self.reduce(c)
    def scal(self, k, a): return [k*x for x in a]
    def is_zero(self, a): return not any(a)
    def eq(self, a, b): return all(x == y for x, y in zip(a, b))
    def conj(self, a):
        """complex conjugate: omega -> omega^{-1}"""
        out = self.zero()
        for t, x in enumerate(a):
            if x: out = self.add(out, self.scal(x, self.root_pow(-t)))
        return out

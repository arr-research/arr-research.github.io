# s4: exact lower-bound certificate for gamma(F) of an N = 5 equal-trace frame in C^3 given by 5 unit Bloch vectors
#     n1, n2, n3 rational (unit), s = n1+n2+n3, n4 = -s/2 + v, n5 = -s/2 - v, v = sqrt(q) * w  with w rational, w.s = 0,
#     q = (1 - |s|^2/4)/|w|^2 rational.  Then all overlaps t_ij = (2/9)(1 + n_i.n_j) lie in Q(sqrt q).
#     g_k = (9/25)[5 + 2 sum_{i<j} Q_{k,3}(t_ij)] computed EXACTLY in Q(sqrt q) for 2 <= k <= K0 (three-term recurrence),
#     then bounded below by a rational using a rational enclosure [l,u] of sqrt(q) (checked l^2 <= q <= u^2).
#     Tail k > K0: Lemma T, |Q_{k,3}(t)| <= (1-t)^{-1}/(k+1)  =>  g_k >= (9/25)[5 - 2 S/(K0+2)],  S = sum_{i<j} (1-t_ij)^{-1} (upper bound).
# Output: certified rational lower bound gamma_cert with  gamma(F) >= gamma_cert, and the exact minimising degree(s).
from fractions import Fraction as Fr
import sys, json, time
from math import isqrt

class Qs:
    """a + b*sqrt(q) with a, b Fractions; q a global Fraction."""
    __slots__ = ('a', 'b')
    q = Fr(0)
    def __init__(self, a, b=Fr(0)): self.a = Fr(a); self.b = Fr(b)
    def __add__(self, o): o = o if isinstance(o, Qs) else Qs(o); return Qs(self.a + o.a, self.b + o.b)
    __radd__ = __add__
    def __sub__(self, o): o = o if isinstance(o, Qs) else Qs(o); return Qs(self.a - o.a, self.b - o.b)
    def __rsub__(self, o): return Qs(o) - self
    def __mul__(self, o):
        if not isinstance(o, Qs): return Qs(self.a * o, self.b * o)
        return Qs(self.a * o.a + self.b * o.b * Qs.q, self.a * o.b + self.b * o.a)
    __rmul__ = __mul__
    def __truediv__(self, o):
        if not isinstance(o, Qs): return Qs(self.a / o, self.b / o)
        den = o.a * o.a - o.b * o.b * Qs.q
        return Qs((self.a * o.a - self.b * o.b * Qs.q) / den, (self.b * o.a - self.a * o.b) / den)
    def bounds(self, l, u):
        """rational [lo, hi] given l <= sqrt(q) <= u"""
        lo = self.a + (self.b * l if self.b >= 0 else self.b * u)
        hi = self.a + (self.b * u if self.b >= 0 else self.b * l)
        return lo, hi
    def __float__(self): return float(self.a) + float(self.b) * float(Qs.q) ** 0.5

def sqrt_enclosure(q, digits=60):
    """rational l, u with l^2 <= q <= u^2, |u-l| ~ 10^-digits"""
    D = 10 ** digits
    n = q.numerator * D * D // q.denominator
    r = isqrt(n)
    l = Fr(r, D); u = Fr(r + 1, D)
    assert l * l <= q <= u * u
    return l, u

def dot(x, y): return sum(a * b for a, b in zip(x, y))

def build(n123, w):
    n1, n2, n3 = [[Fr(c) for c in v] for v in n123]
    for v in (n1, n2, n3): assert dot(v, v) == 1, "not a unit vector"
    s = [n1[i] + n2[i] + n3[i] for i in range(3)]
    w = [Fr(c) for c in w]; assert dot(w, s) == 0, "w not orthogonal to s"
    s2 = dot(s, s); assert s2 <= 4
    q = (1 - s2 / 4) / dot(w, w); Qs.q = q
    sq = Qs(0, 1)
    n4 = [Qs(-s[i] / 2) + sq * w[i] for i in range(3)]
    n5 = [Qs(-s[i] / 2) - sq * w[i] for i in range(3)]
    n = [[Qs(c) for c in n1], [Qs(c) for c in n2], [Qs(c) for c in n3], n4, n5]
    # sanity: unit norms and zero sum
    for v in n:
        nn = sum((c * c for c in v), Qs(0)); assert nn.a == 1 and nn.b == 0
    for i in range(3):
        tot = sum((v[i] for v in n), Qs(0)); assert tot.a == 0 and tot.b == 0
    return n, q

def certify(n123, w, K0=1000, verbose=True):
    t0 = time.time()
    n, q = build(n123, w)
    l, u = sqrt_enclosure(q)
    pairs = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    tv = [Fr(2, 9) * (1 + sum((a * b for a, b in zip(n[i], n[j])), Qs(0))) for i, j in pairs]
    x = [2 * t - 1 for t in tv]
    # recurrence for P_k^{(1,0)}(x): a=1,b=0
    a, b = 1, 0
    Pm = [Qs(1)] * 10; Pc = [Qs(a + 1) + Fr(a + b + 2, 2) * (xi - 1) for xi in x]
    Qk = {1: [Pc[p] / 2 for p in range(10)]}
    lower = {}
    for nn in range(1, K0):
        c1 = 2 * (nn + 1) * (nn + a + b + 1) * (2 * nn + a + b)
        c2 = (2 * nn + a + b + 1) * (a * a - b * b)
        c3 = (2 * nn + a + b) * (2 * nn + a + b + 1) * (2 * nn + a + b + 2)
        c4 = 2 * (nn + a) * (nn + b) * (2 * nn + a + b + 2)
        Pn = [((Fr(c2) + Fr(c3) * x[p]) * Pc[p] - Fr(c4) * Pm[p]) / c1 for p in range(10)]
        Pm, Pc = Pc, Pn
        k = nn + 1
        g = Fr(9, 25) * (5 + 2 * sum((Pc[p] / (k + 1) for p in range(10)), Qs(0)))
        lo, hi = g.bounds(l, u)
        lower[k] = (lo, hi)
    kmin = min(lower, key=lambda k: lower[k][0])
    gmin_lo, gmin_hi = lower[kmin]
    # tail bound
    S_hi = sum(1 / (1 - t.bounds(l, u)[1]) for t in tv)          # upper bound of sum (1-t)^{-1}
    tail = Fr(9, 25) * (5 - 2 * S_hi / (K0 + 2))
    cert = min(gmin_lo, tail)
    if verbose:
        srt = sorted(lower, key=lambda k: lower[k][0])[:6]
        print(f"q = {q};  sqrt(q) in [{float(l):.15f}, {float(u):.15f}]")
        print(f"min over 2<=k<={K0}: k={kmin}, g_k in [{float(gmin_lo):.12f}, {float(gmin_hi):.12f}]  (enclosure width {float(gmin_hi-gmin_lo):.1e})")
        print("smallest degrees:", [(k, round(float(lower[k][0]), 9)) for k in srt])
        print(f"tail k>{K0}: g_k >= {float(tail):.6f}  (S <= {float(S_hi):.4f})")
        print(f"CERTIFIED: gamma(F) >= {float(cert):.12f}   [{time.time()-t0:.0f}s]")
    return cert, kmin, lower

if __name__ == "__main__":
    if len(sys.argv) > 1:
        spec = json.load(open(sys.argv[1]))
        certify(spec['n123'], spec['w'], K0=spec.get('K0', 1000))
    else:
        # test: triangular bipyramid (exp4 float value 1.5452):  n1=e3, n2=-e3, n3=e1, s=e1, w=e2
        certify([["0","0","1"], ["0","0","-1"], ["1","0","0"]], ["0","1","0"], K0=300)

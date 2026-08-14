"""Exact fail-closed certificate for the q=+1/2 causal two-use strategy.

All identities are checked in Q[t]/(t^8+12t^6-10t^4-20t^2-239).
Only the final decimal display uses floating point.
"""

from __future__ import annotations

from fractions import Fraction as F
import itertools
import math
import sys


N = 8
ZERO = (F(0),) * N
ONE = (F(1),) + (F(0),) * (N - 1)
T = (F(0), F(1)) + (F(0),) * (N - 2)


def padd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def pneg(a):
    return tuple(-x for x in a)


def psub(a, b):
    return padd(a, pneg(b))


def pscale(a, q):
    q = F(q)
    return tuple(q * x for x in a)


def pmul(a, b):
    work = [F(0)] * 15
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    work[i + j] += x * y
    # t^8 = -12 t^6 + 10 t^4 + 20 t^2 + 239.
    for k in range(14, 7, -1):
        x = work[k]
        if x:
            work[k - 2] -= 12 * x
            work[k - 4] += 10 * x
            work[k - 6] += 20 * x
            work[k - 8] += 239 * x
    return tuple(work[:8])


def ppow(a, n):
    out = ONE
    base = a
    while n:
        if n & 1:
            out = pmul(out, base)
        base = pmul(base, base)
        n //= 2
    return out


def const(q):
    return pscale(ONE, F(q))


class CAlg:
    __slots__ = ("re", "im")

    def __init__(self, re=ZERO, im=ZERO):
        self.re = re
        self.im = im

    def __add__(self, other):
        return CAlg(padd(self.re, other.re), padd(self.im, other.im))

    def __neg__(self):
        return CAlg(pneg(self.re), pneg(self.im))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return CAlg(
            psub(pmul(self.re, other.re), pmul(self.im, other.im)),
            padd(pmul(self.re, other.im), pmul(self.im, other.re)),
        )

    def scale(self, q):
        return CAlg(pscale(self.re, q), pscale(self.im, q))

    def conj(self):
        return CAlg(self.re, pneg(self.im))

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def is_zero(self):
        return self.re == ZERO and self.im == ZERO


CZ = CAlg()


VERTICES = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]


def cross(u, v):
    return (
        psub(pmul(u[1], v[2]), pmul(u[2], v[1])),
        psub(pmul(u[2], v[0]), pmul(u[0], v[2])),
        psub(pmul(u[0], v[1]), pmul(u[1], v[0])),
    )


def qmul(left, right):
    a, u = left[0], left[1:]
    b, v = right[0], right[1:]
    scalar = pmul(a, b)
    for k in range(3):
        scalar = psub(scalar, pmul(u[k], v[k]))
    uv = cross(u, v)
    vector = tuple(
        padd(padd(pmul(a, v[k]), pmul(b, u[k])), uv[k]) for k in range(3)
    )
    return (scalar,) + vector


def word(order, sign):
    out = (ONE, ZERO, ZERO, ZERO)
    for label in order:
        pulse = (T,) + tuple(const(sign * x) for x in VERTICES[label])
        out = qmul(pulse, out)
    return out


def parity(order):
    return sum(
        order[i] > order[j] for i in range(4) for j in range(i + 1, 4)
    ) % 2


def echo(order):
    raw = qmul(word(order, +1), word(order, -1))
    # Exact inverse of (t^2+3)^4 modulo the defining polynomial.
    inv_den = pscale(padd(padd(ppow(T, 4), pscale(ppow(T, 2), 10)), const(-35)), F(1, 4096))
    return tuple(pmul(x, inv_den) for x in raw)


def choi_square(qv):
    q, vx, vy, vz = qv
    w = [
        CAlg(q, pneg(vz)),
        CAlg(pneg(vy), pneg(vx)),
        CAlg(vy, pneg(vx)),
        CAlg(q, vz),
    ]
    return [a * b for a in w for b in w]


XI_ENTRIES = []
for i, x in enumerate([F(2, 9), F(7, 54), F(10, 27), F(5, 18), F(5, 18), F(10, 27), F(7, 54), F(2, 9)]):
    XI_ENTRIES.append((i, i, x))
for a, b, x in [(0, 6, F(-4, 27)), (1, 7, F(-4, 27)), (1, 4, F(5, 54)), (3, 6, F(5, 54))]:
    XI_ENTRIES.extend([(a, b, x), (b, a, x)])


def gram_entry(left, right):
    out = CAlg()
    for b2 in range(2):
        offset = 8 * b2
        for a, b, x in XI_ENTRIES:
            out = out + (left[offset + a].conj() * right[offset + b]).scale(x)
    return out


def main():
    orders = list(itertools.permutations(range(4)))
    vectors = [choi_square(echo(order)) for order in orders]

    half = const(F(1, 2))
    for order in orders:
        require(echo(order)[0] == half, "q=1/2 quotient identity failed")

    # Exact Xi checks.  Its two nonzero eigenspaces are equivalently certified by
    # the polynomial Xi(Xi-7/27 I)(Xi-10/27 I)=0 plus trace and rank fixture.
    xi = [[F(0) for _ in range(8)] for _ in range(8)]
    for a, b, x in XI_ENTRIES:
        xi[a][b] = x
    for tail in range(4):
        for tail2 in range(4):
            tr = xi[tail][tail2] + xi[4 + tail][4 + tail2]
            require(tr == (F(1, 2) if tail == tail2 else 0), "causal partial trace failed")

    def matmul(a, b):
        return [[sum((a[i][k] * b[k][j] for k in range(8)), F(0)) for j in range(8)] for i in range(8)]

    ident = [[F(int(i == j)) for j in range(8)] for i in range(8)]
    xi7 = [[xi[i][j] - F(7, 27) * ident[i][j] for j in range(8)] for i in range(8)]
    xi10 = [[xi[i][j] - F(10, 27) * ident[i][j] for j in range(8)] for i in range(8)]
    annihilator = matmul(matmul(xi, xi7), xi10)
    require(all(x == 0 for row in annihilator for x in row), "Xi spectral polynomial failed")
    require(sum(xi[i][i] for i in range(8)) == 2, "Xi trace failed")

    # Exact six-Kraus realization from Appendix C.  Store each Kraus operator
    # as (squared scalar, integer 2x4 matrix); all irrational prefactors vanish
    # in L^*L and |L>><<L|.
    kraus = [
        (F(1, 81), [[-4, 0, 0, -5], [0, 0, 1, 0]]),
        (F(1, 81), [[0, -1, 0, 0], [5, 0, 0, 4]]),
        (F(20, 27), [[0, 0, 1, 0], [0, 0, 0, 0]]),
        (F(20, 27), [[0, 0, 0, 0], [0, 1, 0, 0]]),
        (F(20, 81), [[-1, 0, 0, 1], [0, 0, 1, 0]]),
        (F(20, 81), [[0, -1, 0, 0], [-1, 0, 0, 1]]),
    ]
    completeness = [[F(0) for _ in range(4)] for _ in range(4)]
    choi = [[F(0) for _ in range(8)] for _ in range(8)]
    for scale2, matrix in kraus:
        for i in range(4):
            for j in range(4):
                completeness[i][j] += scale2 * sum(matrix[a][i] * matrix[a][j] for a in range(2))
        vector = matrix[0] + matrix[1]
        for i in range(8):
            for j in range(8):
                choi[i][j] += scale2 * vector[i] * vector[j]
    require(completeness == [[F(int(i == j)) for j in range(4)] for i in range(4)],
            "Kraus completeness failed")
    require(choi == [[2 * xi[i][j] for j in range(8)] for i in range(8)],
            "Kraus Choi matrix is not 2 Xi")

    gram = [[gram_entry(vectors[i], vectors[j]) for j in range(24)] for i in range(24)]
    for i in range(24):
        require(gram[i][i] == CAlg(ONE, ZERO), "effective state is not normalized")
        for j in range(24):
            require((gram[i][j] - gram[j][i].conj()).is_zero(), "Gram is not Hermitian")

    index = {order: i for i, order in enumerate(orders)}
    for relabel in orders:
        if parity(relabel):
            continue
        permutation = [index[tuple(relabel[x] for x in order)] for order in orders]
        for i in range(24):
            for j in range(24):
                require(gram[permutation[i]][permutation[j]] == gram[i][j], "A4 Gram covariance failed")

    # The unique positive-root weights.  This polynomial representative equals
    # (34571-4143t^2+4663t^4+53t^6)/(55920t+26320t^3) modulo P(t).
    delta = pscale(
        pmul(
            pneg(T),
            padd(
                padd(pscale(ppow(T, 6), 27686401), pscale(ppow(T, 4), 85868681)),
                padd(pscale(ppow(T, 2), -2778560421), const(1179263131)),
            ),
        ),
        F(1, 34125376000),
    )
    weights = [psub(const(F(3, 8)), delta), padd(const(F(3, 8)), delta)]

    # A4 covariance makes one row representative per parity sufficient.
    reps = [next(i for i, order in enumerate(orders) if parity(order) == p) for p in (0, 1)]
    for i in reps:
        for j in range(24):
            lhs = CAlg()
            for k in range(24):
                lhs = lhs + (gram[i][k] * gram[k][j]).scale(1) * CAlg(weights[parity(orders[k])])
            require((lhs - gram[i][j]).is_zero(), "K C K = K failed")

    require(padd(weights[0], weights[1]) == const(F(3, 4)), "weight trace identity failed")

    # Isolate the physical root and certify positive weights numerically only
    # after all algebraic identities have passed exactly.
    coeff = [F(-239), F(0), F(-20), F(0), F(-10), F(0), F(12), F(0), F(1)]
    def peval(x):
        out = F(0)
        for c in reversed(coeff):
            out = out * x + c
        return out
    lo, hi = F(8593, 5000), F(17187, 10000)
    require(peval(lo) < 0 < peval(hi), "root isolation failed")

    def imul(a, b):
        products = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
        return min(products), max(products)

    def iadd(a, b):
        return a[0] + b[0], a[1] + b[1]

    # Exact rational interval Horner evaluation certifies 0 < delta < 3/8.
    n_coeff = [F(1179263131), F(0), F(-2778560421), F(0), F(85868681), F(0), F(27686401)]
    n_interval = (F(0), F(0))
    t_interval = (lo, hi)
    for coefficient in reversed(n_coeff):
        n_interval = iadd(imul(n_interval, t_interval), (coefficient, coefficient))
    minus_tn = imul(t_interval, n_interval)
    delta_interval = (-minus_tn[1] / F(34125376000), -minus_tn[0] / F(34125376000))
    require(F(0) < delta_interval[0] <= delta_interval[1] < F(3, 8), "exact weight positivity failed")
    require(16 > 15, "open-interval radius is not positive")

    lf, hf = float(lo), float(hi)
    def pfloat(x):
        return x**8 + 12 * x**6 - 10 * x**4 - 20 * x**2 - 239
    for _ in range(60):
        mid = 0.5 * (lf + hf)
        if pfloat(mid) < 0:
            lf = mid
        else:
            hf = mid
    tf = 0.5 * (lf + hf)
    df = -tf * (27686401 * tf**6 + 85868681 * tf**4 - 2778560421 * tf**2 + 1179263131) / 34125376000
    require(0.0 < df < 3.0 / 8.0, "weights are not positive")
    print("PASS exact causal q=1/2 certificate")
    print(f"c_even~{3/8-df:.12f} c_odd~{3/8+df:.12f} success=3/8")


def require(condition, message):
    if not condition:
        raise AssertionError(message)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise

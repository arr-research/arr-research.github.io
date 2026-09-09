"""Independent exact computation of delta_Gr (reviewer's own code, not derived from the author's).

delta_Gr = min sum_j e_j over polynomial vectors f_j in C[z]^N, deg f_j <= e_j, f_j(zeta_i) in Y_i,
with f_1(zeta_i) ^ ... ^ f_k(zeta_i) != 0 at every node (Lemma A, last form).

Exact arithmetic over Q(i) with sympy DomainMatrix (QQ_I).  For k = 2 the wedge test is exact
(a bilinear form on V_{e1} x V_{e2} is identically zero iff its matrix is zero).  For k = 1 the test
is linear.  For k >= 3 a Schwartz-Zippel style random evaluation is used (existence certificates
are exact; non-existence is probabilistic, flagged as such).
"""
import sys, time, random, itertools
from sympy import Matrix, I, Rational, symbols, eye, zeros, expand, Poly, gcd as sgcd
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix

z = symbols('z')

# Pythagorean-triple points on the unit circle (distinct), plus roots of unity
NODES = [Rational(3, 5) + Rational(4, 5) * I, Rational(5, 13) + Rational(12, 13) * I,
         Rational(8, 17) + Rational(15, 17) * I, Rational(7, 25) + Rational(24, 25) * I,
         Rational(20, 29) + Rational(21, 29) * I, Rational(9, 41) + Rational(40, 41) * I,
         Rational(12, 37) + Rational(35, 37) * I, Rational(-3, 5) + Rational(4, 5) * I,
         -1, I]


def DM(M):
    return DomainMatrix.from_Matrix(Matrix(M).applyfunc(expand)).convert_to(QQ_I)


def right_null(M):
    """columns spanning the right null space of M (exact over Q(i))"""
    ns = DM(M).nullspace().to_Matrix()  # rows
    return ns.T


def annihilator(W):
    """rows q with q W = 0"""
    return right_null(Matrix(W).T).T


def rank(M):
    return DM(M).rank()


def eval_map(N, e, zeta):
    """f(zeta) as a linear map on coefficient vectors (c_0,...,c_e), c_s in C^N"""
    return Matrix.hstack(*[zeta ** s * eye(N) for s in range(e + 1)])


class Data:
    def __init__(self, N, k, zetas, Ws):
        self.N, self.k, self.zetas, self.Ws = N, k, list(zetas), [Matrix(W) for W in Ws]
        self.L = len(zetas)
        self.Qs = [annihilator(W) for W in self.Ws]
        # left inverses W^+ (k x N): coordinates of a vector of Y_i in the frame W_i
        self.Wl = [(W.H * W).inv() * W.H for W in self.Ws]
        self.r = rank(Matrix.hstack(*self.Ws))
        self._V = {}

    def V(self, e):
        if e not in self._V:
            A = Matrix.vstack(*[Q * eval_map(self.N, e, zt) for Q, zt in zip(self.Qs, self.zetas)])
            self._V[e] = right_null(A)
        return self._V[e]

    def node_coords(self, e, Vb, i):
        """k x dim V matrix: coordinates in frame W_i of f(zeta_i) for f ranging over the basis Vb"""
        return (self.Wl[i] * eval_map(self.N, e, self.zetas[i]) * Vb).applyfunc(expand)

    def wedge_nonzero(self, es, Vs):
        """True iff there exist f_j in V_{e_j} with wedge nonzero at every node."""
        k = self.k
        for i in range(self.L):
            Cs = [self.node_coords(e, Vb, i) for e, Vb in zip(es, Vs)]
            if k == 1:
                if Cs[0].is_zero_matrix:
                    return False
            elif k == 2:
                C1, C2 = Cs
                B = zeros(C1.shape[1], C2.shape[1])
                for a in range(C1.shape[1]):
                    for b in range(C2.shape[1]):
                        B[a, b] = expand(C1[0, a] * C2[1, b] - C1[1, a] * C2[0, b])
                if B.is_zero_matrix:
                    return False
            else:
                rng = random.Random(12345 + i)
                found = False
                for trial in range(40):
                    vals = [C * Matrix([rng.randint(-7, 7) for _ in range(C.shape[1])]) for C in Cs]
                    if expand(Matrix.hstack(*vals).det()) != 0:
                        found = True
                        break
                if not found:
                    print(f"    [probabilistic] wedge form at node {i} vanished in 40 random trials")
                    return False
        return True

    def delta(self, emax=8, verbose=False):
        k = self.k
        for total in range(0, k * emax + 1):
            # nondecreasing tuples with given sum
            for es in itertools.combinations_with_replacement(range(total + 1), k):
                if sum(es) != total:
                    continue
                Vs = [self.V(e) for e in es]
                dims = [Vb.shape[1] for Vb in Vs]
                ok = all(d > 0 for d in dims) and self.wedge_nonzero(es, Vs)
                if verbose:
                    print(f"    es={es} dimV={dims} ok={ok}")
                if ok:
                    return total, es, Vs
        return None

    def witness(self, es, Vs, seed=3):
        rng = random.Random(seed)
        k = self.k
        for trial in range(50):
            cols = []
            for e, Vb in zip(es, Vs):
                c = Vb * Matrix([rng.randint(-4, 4) for _ in range(Vb.shape[1])])
                cols.append(Matrix([expand(sum(c[s * self.N + a] * z ** s for s in range(e + 1))) for a in range(self.N)]))
            F = Matrix.hstack(*cols)
            good = True
            for i in range(self.L):
                Fz = F.subs(z, self.zetas[i]).applyfunc(expand)
                if rank(Fz) != k or not (self.Qs[i] * Fz).applyfunc(expand).is_zero_matrix:
                    good = False
                    break
            if good:
                return F
        raise RuntimeError("no witness found")


def forney(F, N, k):
    minors = []
    for rows in itertools.combinations(range(N), k):
        m = expand(F.extract(list(rows), list(range(k))).det())
        if m != 0:
            minors.append(Poly(m, z, domain=QQ_I))
    g = minors[0]
    for m in minors[1:]:
        g = g.gcd(m)
    return max(m.degree() for m in minors) - g.degree(), g.as_expr()


def random_frames(N, k, L, seed):
    rng = random.Random(seed)
    Ws = []
    for i in range(L):
        while True:
            W = Matrix(N, k, lambda a, b: rng.randint(-4, 4) + rng.randint(-4, 4) * I)
            if rank(W) == k:
                break
        Ws.append(W)
    return Ws


def run(name, N, k, zetas, Ws, expect=None, verbose=False, emax=8):
    t0 = time.time()
    D = Data(N, k, zetas, Ws)
    res = D.delta(emax=emax, verbose=verbose)
    total, es, Vs = res
    F = D.witness(es, Vs)
    fd, g = forney(F, N, k)
    tag = '' if expect is None else ('  [matches expectation %s]' % expect if total == expect else '  [MISMATCH: expected %s]' % expect)
    print(f"{name}: N={N} k={k} L={len(zetas)} r={D.r}  delta_Gr = {total} (column degrees {es}); witness Forney degree {fd}, gcd {g}; {time.time()-t0:.1f}s{tag}")
    sys.stdout.flush()
    return total, es, D, F


if __name__ == '__main__':
    print("=== A. random k=2, N=4, L=3 (the requested independent instance), several seeds")
    for seed in [101, 202, 303]:
        run(f"  L=3 seed {seed}", 4, 2, NODES[:3], random_frames(4, 2, 3, seed), expect=2, verbose=(seed == 101))
    print("=== B. spot-check: random k=2, N=4, L=4 -> 4 ;  generic law 2*floor(L/2) for L=5,6")
    for seed in [404, 505]:
        run(f"  L=4 seed {seed}", 4, 2, NODES[:4], random_frames(4, 2, 4, seed), expect=4)
    run("  L=5 seed 606", 4, 2, NODES[:5], random_frames(4, 2, 5, 606), expect=4)
    run("  L=6 seed 707", 4, 2, NODES[:6], random_frames(4, 2, 6, 707), expect=6)
    print("=== C. direct-sum words (52B6 law k(L-n_*)), k=2, A (+) B = C^4")
    A = Matrix([[1, 0], [0, 1], [0, 0], [0, 0]]); B = Matrix([[0, 0], [0, 0], [1, 0], [0, 1]])
    # also a skewed direct-sum pair to avoid coordinate coincidences
    T = Matrix([[1, 2, 0, 1], [0, 1, 1, 0], [1, 0, 1, 1], [0, 1, 0, 2]])
    assert T.det() != 0
    A2, B2 = T * A, T * B
    for word, exp in [("AAB", 4), ("ABAB", 4), ("AAAB", 6), ("AABB", 4), ("AAABB", 6), ("ABABA", 4)]:
        Ws = [A2 if c == 'A' else B2 for c in word]
        run(f"  word {word}", 4, 2, NODES[:len(word)], Ws, expect=exp)
    print("=== D. k=1 line laws (6M3V / 33BE)")
    y1 = Matrix([1, 0]); y2 = Matrix([0, 1]); y3 = Matrix([1, 1])
    run("  3 lines coplanar distinct (33BE: 1)", 2, 1, NODES[:3], [y1, y2, y3], expect=1)
    run("  3 lines repeated y1,y1,y2 (33BE: 2)", 2, 1, NODES[:3], [y1, y1, y2], expect=2)
    run("  4 lines pattern 3+1 (6M3V Thm 11.1: 3)", 2, 1, NODES[:4], [y1, y1, y1, y2], expect=3)
    run("  binary word y1 y2 y1 y2 y1 (6M3V Thm 9.2: max(3,2)=3)", 2, 1, NODES[:5], [y1, y2, y1, y2, y1], expect=3)
    for L in [4, 5, 6, 7]:
        run(f"  generic lines in C^3, L={L} (6M3V floor(2L/3)={2*L//3})", 3, 1, NODES[:L], random_frames(3, 1, L, 900 + L), expect=2 * L // 3)
    print("=== E. generic k=2 in C^3 (Gr(2,3)=P^2): expect floor(2L/3)")
    for L in [4, 5, 6]:
        run(f"  Gr(2,3) L={L}", 3, 2, NODES[:L], random_frames(3, 2, L, 800 + L), expect=2 * L // 3)
    print("=== F. k=3 in C^6, direct-sum position L=2 (33BE: k(L-1)=3) and generic L=3 in C^6 (33BE: 6)")
    run("  k=3 N=6 L=2 generic (direct sum)", 6, 3, NODES[:2], random_frames(6, 3, 2, 1000), expect=3)
    run("  k=3 N=6 L=3 generic (r=6, 33BE bound r-k=3, prop 3.5 lower bound 3*floor(9/6)=3)", 6, 3, NODES[:3], random_frames(6, 3, 3, 1001), expect=None)
    print("done")

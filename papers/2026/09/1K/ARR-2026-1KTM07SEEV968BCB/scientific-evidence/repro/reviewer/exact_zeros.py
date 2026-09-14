"""Exact (Q(omega_d)) computation of maximal zero counts for sparse exponential sums.
Generic: points S (support), evaluation points T, pairing e(t,s) in Z/d, matrix M = (omega^{e(t,s)}).
A full-support c with M c = 0 exists (over C) iff rank M < |S| and rank M_{S\\s} = rank M for every s in S.
Ranks: modular filter (F_q, q = 1 mod d) for the full-column-rank case (rank_q <= rank_Q), exact via the
regular representation over Z (python-flint fmpz_mat) otherwise.
"""
import itertools
from math import gcd
import flint
from sympy import cyclotomic_poly, Poly, symbols, isprime, primitive_root

_x = symbols('x')

class ExactRank:
    def __init__(self, d):
        self.d = d
        P = Poly(cyclotomic_poly(d, _x), _x)
        self.phi = [int(c) for c in P.all_coeffs()[::-1]]
        self.deg = P.degree()
        # regular representation of omega^t: matrix of multiplication by x^t on Z[x]/Phi_d
        self.R = [self._regrep(t) for t in range(d)]
        # modular: prime q = 1 mod d, zeta primitive d-th root
        q = d + 1
        while not (isprime(q) and q > 1000): q += d
        self.q = q
        g = primitive_root(q)
        self.zeta = pow(g, (q - 1) // d, q)
        assert pow(self.zeta, d, q) == 1 and all(pow(self.zeta, d // r, q) != 1 for r in range(2, d + 1) if d % r == 0)
    def _reduce(self, c):
        D = self.deg
        c = list(c)
        for i in range(len(c) - 1, D - 1, -1):
            if c[i]:
                f = c[i]
                for j in range(D + 1): c[i - D + j] -= f * self.phi[j]
        c = c[:D] + [0]*max(0, D-len(c))
        return c
    def _regrep(self, t):
        D = self.deg
        cols = []
        for b in range(D):
            v = [0] * (b + t + 1); v[b + t] = 1
            cols.append(self._reduce(v))
        # matrix with column b = coordinates of x^{b+t}
        return [[cols[b][a] for b in range(D)] for a in range(D)]
    def rank_mod(self, E):
        """E: list of rows of exponents (ints mod d) -> rank over F_q"""
        n, m = len(E), len(E[0])
        M = flint.nmod_mat(n, m, [pow(self.zeta, e % self.d, self.q) for row in E for e in row], self.q)
        return M.rank()
    def rank_exact(self, E):
        n, m = len(E), len(E[0]); D = self.deg
        rows = []
        for i in range(n):
            for a in range(D):
                row = []
                for j in range(m):
                    Rt = self.R[E[i][j] % self.d]
                    row.extend(Rt[a])
                rows.append(row)
        M = flint.fmpz_mat(n * D, m * D, [x for row in rows for x in row])
        r = M.rank()
        assert r % D == 0
        return r // D
    def rank(self, E):
        """exact rank; uses the modular value when it already equals the column count"""
        m = len(E[0])
        rq = self.rank_mod(E)
        if rq == m: return m
        return self.rank_exact(E)
    def full_support_solution_exists(self, E):
        m = len(E[0])
        r = self.rank(E)
        if r == m: return False
        for s in range(m):
            Es = [row[:s] + row[s + 1:] for row in E]
            if self.rank(Es) < r: return False
        return True

def orbits(subsets, group_action):
    """subsets: iterable of tuples; group_action: function(subset) -> list of images. returns representatives"""
    seen = set(); reps = []
    for S in subsets:
        if S in seen: continue
        reps.append(S)
        for img in group_action(S): seen.add(img)
    return reps

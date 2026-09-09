"""Independent reviewer's check of steps (3)-(6) of prove_C1_weyl_sparsity.md.

Written from scratch (no import of the author's e2 script).

Part A: Clifford covariance (2.1) with an EXPLICIT phase formula
        U_s W_{a,b} U_s^{-1} = omega^{-(s a^2 /2) - a b} X^{-(s a + b)} Z^a,  U_s = F' Q_s,
        checked exactly in Z[omega] for p in {3,5,7}, all s, all (a,b).  Also p = 2 is examined separately
        (Q_s needs 2^{-1}; only the four Paulis exist and the theorem is trivial there).
Part B: p = 7, l = 5, coefficients in the ring A = Z[omega_7, sqrt2] (a genuine extension in which the prime
        (1-omega) of Z[omega] SPLITS: 2 = 3^2 mod 7), reduction modulo the prime P_3 : omega -> 1, sqrt2 -> 3
        and modulo the other prime P_4 : omega -> 1, sqrt2 -> -3 = 4.  For every one of the 8 directions
        U in {I, F'Q_s}: (i) U C U^* is divisible by 7 in A (so U C U^{-1} is integral), (ii) its reduction is
        the predicted circulant of fibre sums, (iii) F_7-rank of the reduction = 7 - ord_1(gbar) and
        ord_1 <= m - 1, (iv) rank over the field K = Q(omega, sqrt2) (exact, regular representation of degree
        12 over Q) >= reduced rank, and (v) the maximum over directions of the reduced rank >= p - l + 1.
        Includes instances with coefficients of positive valuation at exactly one of P_3, P_4 (multiples of
        sqrt2 - 3 or sqrt2 + 3), a common factor (1-omega)^2 removed by exact scaling, and forced
        fibre-sum cancellations.
Part C: exhaustive check of the Vandermonde/Hasse step: every polynomial over F_p of degree < p with exactly m
        nonzero monomials has ord_{x=1} <= m - 1 (p = 7, all m = 1..7, all exponent sets, all nonzero coefficient
        vectors; p = 5 and p = 11 for m <= 4), and equality is attained.
Part D: sharpness family prod_{i<l-1}(Z - omega^i I): exactly l nonzero Weyl coefficients and nullity l-1, exact.
"""
import itertools, random, sys, time
from fractions import Fraction

# ---------------------------------------------------------------- Z[omega_p] arithmetic (integer vectors)
class Cyc:
    """Z[omega_p] with basis 1, omega, ..., omega^{p-2}; internally length-p vectors with last entry 0."""
    def __init__(self, p):
        self.p = p
    def canon(self, v):
        p = self.p; c = v[p-1]
        return tuple(x - c for x in v[:p-1]) + (0,)
    def zero(self): return (0,)*self.p
    def one(self): return self.om(0)
    def om(self, e):
        v = [0]*self.p; v[e % self.p] = 1; return self.canon(tuple(v))
    def add(self, u, v): return self.canon(tuple(a+b for a, b in zip(u, v)))
    def sub(self, u, v): return self.canon(tuple(a-b for a, b in zip(u, v)))
    def mul(self, u, v):
        p = self.p; w = [0]*p
        for i, a in enumerate(u):
            if a:
                for j, b in enumerate(v):
                    if b: w[(i+j) % p] += a*b
        return self.canon(tuple(w))
    def conj(self, u):
        p = self.p; v = [0]*p
        for i, a in enumerate(u): v[(-i) % p] += a
        return self.canon(tuple(v))
    def iszero(self, u): return not any(u)
    def divint(self, u, k):
        assert all(a % k == 0 for a in u), "not divisible by %d" % k
        return self.canon(tuple(a // k for a in u))
    def res(self, u):  # omega -> 1, mod p
        return sum(u) % self.p

def mat_mul(R, A, B):
    n = len(A)
    return [[_dot(R, A[i], [B[k][j] for k in range(n)]) for j in range(n)] for i in range(n)]

def _dot(R, row, col):
    acc = R.zero()
    for a, b in zip(row, col):
        if not R.iszero(a) and not R.iszero(b):
            acc = R.add(acc, R.mul(a, b))
    return acc

def weyl(R, p, a, b):
    """W_{a,b} = X^a Z^b, X|j> = |j+1>, Z|j> = omega^j |j>:  (X^a Z^b)_{j,k} = omega^{b k} [j = k + a]."""
    M = [[R.zero() for _ in range(p)] for _ in range(p)]
    for k in range(p): M[(k + a) % p][k] = R.om(b*k)
    return M

def fourier(R, p): return [[R.om(j*k) for k in range(p)] for j in range(p)]
def qgate(R, p, s):
    inv2 = pow(2, -1, p)
    M = [[R.zero() for _ in range(p)] for _ in range(p)]
    for j in range(p): M[j][j] = R.om(s*inv2*j*j)
    return M
def adjoint(R, A):
    n = len(A); return [[R.conj(A[j][i]) for j in range(n)] for i in range(n)]

# ---------------------------------------------------------------- Part A
def partA():
    print("=== Part A: Clifford covariance with explicit phase, exact in Z[omega] ===")
    for p in [3, 5, 7]:
        R = Cyc(p); F = fourier(R, p); Fs = adjoint(R, F); inv2 = pow(2, -1, p)
        # sanity: F' X F'^{-1} = Z and F' Z F'^{-1} = X^{-1}, i.e. F' X F'^* = p Z etc.
        X = weyl(R, p, 1, 0); Z = weyl(R, p, 0, 1)
        assert mat_mul(R, mat_mul(R, F, X), Fs) == [[_scal(R, p, z) for z in row] for row in Z]
        assert mat_mul(R, mat_mul(R, F, Z), Fs) == [[_scal(R, p, z) for z in row] for row in weyl(R, p, p-1, 0)]
        count = 0
        for s in range(p):
            U = mat_mul(R, F, qgate(R, p, s)); Us = adjoint(R, U)   # U U^* = p I
            for a in range(p):
                for b in range(p):
                    T = mat_mul(R, mat_mul(R, U, weyl(R, p, a, b)), Us)
                    e = (-(s*inv2*a*a) - a*b) % p
                    Wt = weyl(R, p, (-(s*a + b)) % p, a)
                    pred = [[_scal(R, p, R.mul(R.om(e), z)) for z in row] for row in Wt]
                    assert T == pred, (p, s, a, b)
                    count += 1
        print(f"  p={p}: U_s W_(a,b) U_s^* = p * omega^(-s a^2/2 - a b) * X^(-(s a+b)) Z^a exact for all {count} (s,a,b)")
    # p = 2: no 2^{-1}; the theorem is trivial: l=1 -> invertible, l=2 -> nonzero 2x2 matrix has rank >= 1.
    import numpy as np
    X2 = np.array([[0, 1], [1, 0]]); Z2 = np.diag([1, -1]); Ws = [np.eye(2), X2, Z2, X2 @ Z2]
    worst = 0
    rng = np.random.default_rng(0)
    for S in itertools.combinations(range(4), 2):
        for _ in range(200):
            c = rng.normal(size=2) + 1j*rng.normal(size=2)
            C = c[0]*Ws[S[0]] + c[1]*Ws[S[1]]
            worst = max(worst, 2 - np.linalg.matrix_rank(C))
    print(f"  p=2: max nullity over 2-term Pauli combinations (random) = {worst} <= 1; l=1 invertible; l>=3 vacuous. OK")

def _scal(R, p, z):
    return tuple(p*x for x in z)

# ---------------------------------------------------------------- the ring A = Z[omega_7, sqrt2]
class CycSqrt2:
    """Elements u + v*sqrt2 with u, v in Z[omega_p]; stored as pair of Cyc vectors."""
    def __init__(self, p):
        self.p = p; self.R = Cyc(p)
    def zero(self): return (self.R.zero(), self.R.zero())
    def one(self): return (self.R.one(), self.R.zero())
    def from_cyc(self, u): return (u, self.R.zero())
    def sqrt2(self): return (self.R.zero(), self.R.one())
    def add(self, x, y): return (self.R.add(x[0], y[0]), self.R.add(x[1], y[1]))
    def sub(self, x, y): return (self.R.sub(x[0], y[0]), self.R.sub(x[1], y[1]))
    def mul(self, x, y):
        R = self.R
        u = R.add(R.mul(x[0], y[0]), R.mul(R.mul(x[1], y[1]), R.add(R.one(), R.one())))  # u u' + 2 v v'
        v = R.add(R.mul(x[0], y[1]), R.mul(x[1], y[0]))
        return (u, v)
    def conj(self, x):  # complex conjugation: omega -> omega^{-1}, sqrt2 fixed (sqrt2 real)
        return (self.R.conj(x[0]), self.R.conj(x[1]))
    def iszero(self, x): return self.R.iszero(x[0]) and self.R.iszero(x[1])
    def divint(self, x, k): return (self.R.divint(x[0], k), self.R.divint(x[1], k))
    def res(self, x, root):  # reduction mod P_root : omega -> 1, sqrt2 -> root (root^2 = 2 mod p)
        return (self.R.res(x[0]) + root*self.R.res(x[1])) % self.p
    def div_one_minus_omega(self, x):
        """exact division by (1-omega): multiply by prod_{t=2}^{p-1}(1-omega^t) and divide by p."""
        R = self.R; prodrest = R.one()
        for t in range(2, self.p): prodrest = R.mul(prodrest, R.sub(R.one(), R.om(t)))
        return (R.divint(R.mul(x[0], prodrest), self.p), R.divint(R.mul(x[1], prodrest), self.p))
    def coords(self, x):  # Z-coordinates in basis omega^i sqrt2^j, i < p-1, j < 2 (length 2(p-1))
        return list(x[0][:self.p-1]) + list(x[1][:self.p-1])
    def basis(self):
        out = []
        for j in range(2):
            for i in range(self.p-1):
                out.append((self.R.om(i), self.R.zero()) if j == 0 else (self.R.zero(), self.R.om(i)))
        return out

def rank_Q(M):
    M = [row[:] for row in M]; rows = len(M); cols = len(M[0]); r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [x - f*y for x, y in zip(M[i], M[r])]
        r += 1
        if r == rows: break
    return r

def rank_modp(M, p):
    M = [[x % p for x in row] for row in M]; rows = len(M); cols = len(M[0]); r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c]), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], -1, p); M[r] = [(x*inv) % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]; M[i] = [(x - f*y) % p for x, y in zip(M[i], M[r])]
        r += 1
    return r

def rank_over_K(A, C):
    """exact rank over K = Q(omega_p, sqrt2) via the regular representation (degree n = 2(p-1) over Q)."""
    n = 2*(A.p-1); basis = A.basis(); N = len(C)
    big = [[Fraction(0)]*(N*n) for _ in range(N*n)]
    for i in range(N):
        for j in range(N):
            x = C[i][j]
            if A.iszero(x): continue
            for cidx, bvec in enumerate(basis):
                col = A.coords(A.mul(x, bvec))
                for r in range(n): big[i*n + r][j*n + cidx] = Fraction(col[r])
    rk = rank_Q(big); assert rk % n == 0, rk
    return rk // n

def rank_numeric(A, C):
    import numpy as np, cmath
    p = A.p; w = cmath.exp(2j*cmath.pi/p); s2 = 2**0.5
    def val(x): return sum(a*w**i for i, a in enumerate(x[0])) + s2*sum(a*w**i for i, a in enumerate(x[1]))
    M = np.array([[val(x) for x in row] for row in C])
    return int(np.linalg.matrix_rank(M, tol=1e-8))

def ord_at_one(coeffs, p):
    """order of vanishing at x = 1 of sum_t coeffs[t] x^t over F_p (coeffs: length-p list), via repeated division."""
    g = [c % p for c in coeffs]
    assert any(g)
    r = 0
    while True:
        if sum(g) % p: return r
        # synthetic division by (x - 1): g = (x-1) q
        n = len(g); q = [0]*(n-1); acc = 0
        for i in range(n-1, 0, -1):
            acc = (acc + g[i]) % p; q[i-1] = acc
        g = q; r += 1
        if not any(g): return r

def circulant_from_poly(coeffs, p):
    """sum_t gamma_t Xbar^t: entry (j,k) = gamma_{j-k}."""
    return [[coeffs[(j - k) % p] % p for k in range(p)] for j in range(p)]

def partB():
    print("=== Part B: p = 7, l = 5, coefficients in Z[omega_7, sqrt2], primes P_3 (sqrt2->3) and P_4 (sqrt2->4) ===")
    p = 7; l = 5; A = CycSqrt2(p); R = A.R
    F = fourier(R, p)
    Fs = adjoint(R, F)
    # directions: (name, lambda, U, U^*) with U U^* = p I ; entries lifted into A
    lift = lambda M: [[A.from_cyc(z) for z in row] for row in M]
    dirs = [('I', (lambda g: g[0] % p), None, None)]
    for s in range(p):
        U = mat_mul(R, F, qgate(R, p, s)); Us = adjoint(R, U)
        dirs.append((f'F.Q{s}', (lambda g, s=s: (-(s*g[0] + g[1])) % p), lift(U), lift(Us)))
    labels = [(a, b) for a in range(p) for b in range(p)]

    def A_matmul(X, Y):
        n = len(X); out = []
        for i in range(n):
            row = []
            for j in range(n):
                acc = A.zero()
                for k in range(n):
                    if not A.iszero(X[i][k]) and not A.iszero(Y[k][j]):
                        acc = A.add(acc, A.mul(X[i][k], Y[k][j]))
                row.append(acc)
            out.append(row)
        return out

    def build(S, coeffs):
        C = [[A.zero() for _ in range(p)] for _ in range(p)]
        for g, c in zip(S, coeffs):
            W = weyl(R, p, *g)
            for i in range(p):
                for j in range(p):
                    if not R.iszero(W[i][j]):
                        C[i][j] = A.add(C[i][j], A.mul(c, A.from_cyc(W[i][j])))
        return C

    rng = random.Random(2026)
    def rnd():
        while True:
            x = (R.canon(tuple(rng.randint(-2, 2) for _ in range(p))), R.canon(tuple(rng.randint(-2, 2) for _ in range(p))))
            if not A.iszero(x): return x
    s2 = A.sqrt2(); three = A.from_cyc(R.canon((3,)+(0,)*(p-1)))
    pi3 = A.sub(s2, three)          # sqrt2 - 3 : in P_3, unit at P_4
    pi4 = A.add(s2, three)          # sqrt2 + 3 : in P_4, unit at P_3
    one_minus = A.from_cyc(R.sub(R.one(), R.om(1)))

    instances = []
    # (1) generic random supports/coefficients
    for _ in range(6):
        S = rng.sample(labels, l); instances.append(('generic', S, [rnd() for _ in S]))
    # (2) coefficients with positive valuation at P_3 only / at P_4 only (different residue pictures)
    for _ in range(4):
        S = rng.sample(labels, l)
        co = [A.mul(rnd(), pi3) if rng.random() < 0.5 else A.mul(rnd(), pi4) for _ in S]
        co[0] = rnd()  # keep at least one unit at both primes
        instances.append(('mixed valuations', S, co))
    # (3) common factor (1-omega)^2 : exercises the scaling step
    S = rng.sample(labels, l); co = [A.mul(A.mul(rnd(), one_minus), one_minus) for _ in S]
    instances.append(('common (1-omega)^2 factor', S, co))
    # (4) forced cancellation of the vertical fibre sums: 4 points on a vertical line with integer coefficients
    #     summing to 0 mod 7, plus one extra point
    a0 = rng.randrange(p); bs = rng.sample(range(p), 4)
    ints = [1, 2, 3, (-6) % 7]  # 1+2+3+1 = 7
    S = [(a0, b) for b in bs] + [rng.choice([g for g in labels if g[0] != a0])]
    co = [A.from_cyc(R.canon((k,)+(0,)*(p-1))) for k in ints] + [rnd()]
    instances.append(('vertical fibre sums vanish mod 7', S, co))
    # (5) the equality family: collinear product prod_{i<4}(Z - omega^i) (5 terms), coefficients in Z[omega]
    poly = [R.one()]
    for i in range(l-1):
        new = [R.zero()]*(len(poly)+1)
        for k, c in enumerate(poly):
            new[k+1] = R.add(new[k+1], c); new[k] = R.sub(new[k], R.mul(R.om(i), c))
        poly = new
    S = [(0, b) for b in range(l)]; co = [A.from_cyc(c) for c in poly]
    instances.append(('collinear equality case prod(Z-omega^i)', S, co))
    # (6) the same family multiplied on the left by a random unit of A and conjugated by nothing:
    #     coefficients times sqrt2 (unit at both primes)
    instances.append(('collinear x sqrt2', S, [A.mul(c, s2) for c in co]))

    t0 = time.time()
    for name, S, coeffs in instances:
        C = build(S, coeffs)
        rkK = rank_over_K(A, C)
        rkN = rank_numeric(A, C)
        assert rkK == rkN, ("exact vs numeric rank disagree", rkK, rkN)
        # scaling: divide by the largest common power of (1-omega) (this is the only case that occurs here
        # where all residues vanish at both primes)
        scaled = coeffs; nscale = 0
        while all(A.res(c, 3) == 0 for c in scaled) and all(A.res(c, 4) == 0 for c in scaled):
            scaled = [A.div_one_minus_omega(c) for c in scaled]; nscale += 1
        Cs = build(S, scaled)
        assert rank_over_K(A, Cs) == rkK
        print(f"\n[{name}] S={S}  rank_K(C) = {rkK}  (numeric {rkN}); law needs rank >= {p-l+1}; scaled by (1-omega)^-{nscale}")
        for root in (3, 4):
            cbar = [A.res(c, root) for c in scaled]
            if not any(cbar):
                print(f"   P_{root}: all residues vanish after scaling (would need P_{root}-specific scaling) - skipped")
                continue
            best = 0; line = []
            for dname, lam, U, Us in dirs:
                if U is None:
                    T = Cs
                else:
                    T = A_matmul(A_matmul(U, Cs), Us)
                    T = [[A.divint(x, p) for x in row] for row in T]   # integrality test: exact division by p
                red = [[A.res(x, root) for x in row] for row in T]
                fib = [0]*p
                for g, cb in zip(S, cbar): fib[lam(g)] = (fib[lam(g)] + cb) % p
                assert red == circulant_from_poly(fib, p), ("reduction is not the fibre-sum circulant", name, dname)
                rk_red = rank_modp(red, p)
                assert rk_red <= rkK, ("rank inequality violated", name, dname, rk_red, rkK)
                if any(fib):
                    m = sum(1 for x in fib if x); o = ord_at_one(fib, p)
                    assert rk_red == p - o and o <= m - 1, (name, dname, rk_red, o, m)
                    line.append(f"{dname}:gbar={fib} m={m} ord1={o} rank={rk_red}")
                else:
                    line.append(f"{dname}:gbar=0 rank=0")
                best = max(best, rk_red)
            assert best >= p - l + 1, ("bound failed", name, root)
            print(f"   P_{root}: residues cbar={cbar}; max reduced rank over 8 directions = {best} >= {p-l+1}  (rank_K = {rkK})")
            for x in line: print("      " + x)
    print(f"\nPart B: all assertions passed for {len(instances)} instances x 2 primes x 8 directions  [{time.time()-t0:.1f}s]")

# ---------------------------------------------------------------- Part C
def partC():
    print("\n=== Part C: exhaustive ord_1 <= m-1 for polynomials over F_p with m nonzero monomials ===")
    for p, mmax in [(7, 7), (5, 5), (11, 4)]:
        for m in range(1, mmax+1):
            worst = 0; n = 0
            for T in itertools.combinations(range(p), m):
                for cs in itertools.product(range(1, p), repeat=m):
                    g = [0]*p
                    for t, c in zip(T, cs): g[t] = c
                    o = ord_at_one(g, p); n += 1
                    assert o <= m - 1, (p, T, cs, o)
                    worst = max(worst, o)
            print(f"  p={p} m={m}: {n} polynomials, max ord_1 = {worst} (bound m-1 = {m-1}){'  [attained]' if worst == m-1 else ''}")
    # counter-check that the bound is really about exponents distinct mod p: p^2-type failure
    # (x^{p} - 1 pattern does not fit degree < p, so nothing to show; instead show 1 - x^{p} = (1-x)^p has m=2, ord p)
    p = 7; g = [0]*(2*p); g[0] = 1; g[p] = -1
    # ord at 1 of 1 - x^7 over F_7: compute by repeated division with length 2p
    r = 0; h = [c % p for c in g]
    while True:
        if sum(h) % p: break
        n = len(h); q = [0]*(n-1); acc = 0
        for i in range(n-1, 0, -1):
            acc = (acc + h[i]) % p; q[i-1] = acc
        h = q; r += 1
        if not any(h): break
    print(f"  sanity (exponents NOT distinct mod p): 1 - x^7 over F_7 has m = 2 but ord_1 = {r}  -> primality/distinctness is essential")

# ---------------------------------------------------------------- Part D
def partD():
    print("\n=== Part D: sharpness family prod_{i<l-1}(Z - omega^i I), p = 7, exact ===")
    p = 7; R = Cyc(p)
    for l in range(1, p+1):
        poly = [R.one()]
        for i in range(l-1):
            new = [R.zero()]*(len(poly)+1)
            for k, c in enumerate(poly):
                new[k+1] = R.add(new[k+1], c); new[k] = R.sub(new[k], R.mul(R.om(i), c))
            poly = new
        nz = sum(1 for c in poly if not R.iszero(c))
        # nullity: number of j with poly(omega^j) = 0
        zeros = 0
        for j in range(p):
            val = R.zero()
            for k, c in enumerate(poly): val = R.add(val, R.mul(c, R.om(j*k)))
            if R.iszero(val): zeros += 1
        assert nz == l and zeros == l - 1, (l, nz, zeros)
    print(f"  all l = 1..{p}: exactly l nonzero Weyl coefficients, nullity exactly l-1 (Gaussian binomials nonzero). OK")

if __name__ == '__main__':
    t0 = time.time()
    partA(); partB(); partC(); partD()
    print(f"\nALL REVIEWER CHECKS PASSED [{time.time()-t0:.1f}s]")

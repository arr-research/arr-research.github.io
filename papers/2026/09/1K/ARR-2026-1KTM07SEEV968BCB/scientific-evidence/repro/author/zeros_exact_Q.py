"""zeros_exact_Q.py -- EXACT (over Q(omega_n)) maximal number of characters annihilated by a function with prescribed support
on the abelian group G = Z/n ("cyclic") or (Z/n)^2 ("plane"), all coefficients nonzero:
   Z(G, S) = max_c #{ chi : sum_{g in S} c_g chi(g) = 0 },  Z(G, m) = max_{|S| = m} Z(G, S),  Z_<=(G, m) = max_{m' <= m}.
Method: the 'flats' enumeration of cyclic_zeros_exact.py (maximal zero sets are closures of flats cut out by <= m-1 character
rows; a flat contains a full-support vector iff no coordinate vanishes identically on it), but with arithmetic in Q(omega_n)
realised through the regular representation: an element of Q(omega_n) = Q[x]/Phi_n is a phi(n)-vector, a character value
omega^e acts as an integer phi x phi matrix; kernels are computed over Q with Fractions.  Orbit reduction under the affine
group GL_2(Z/n) x translations (plane) or units x translations (cyclic), both of which preserve Z(G, S).
usage: python zeros_exact_Q.py cyclic|plane n mmin mmax
"""
import sys, itertools, time
from fractions import Fraction
from math import gcd
from sympy import cyclotomic_poly, Poly, symbols, ZZ

x = symbols('x')

class Cyc:
    def __init__(self, n):
        self.n = n
        self.Phi = Poly(cyclotomic_poly(n, x), x, domain=ZZ)
        self.phi = self.Phi.degree()
        # matrix of multiplication by x on basis 1..x^{phi-1}
        self.pow_mats = {}
        coeffs = self.Phi.all_coeffs()[::-1]  # low to high, monic
        self.red_top = [-c for c in coeffs[:-1]]  # x^phi = sum red_top[i] x^i
    def mul_by_omega_power(self, e):
        e %= self.n
        if e in self.pow_mats: return self.pow_mats[e]
        phi = self.phi
        M = [[0]*phi for _ in range(phi)]
        for j in range(phi):
            vec = [0]*phi; vec[j] = 1
            for _ in range(e):  # multiply by x
                top = vec[phi-1]
                vec = [0] + vec[:-1]
                if top:
                    for i in range(phi): vec[i] += top*self.red_top[i]
            for i in range(phi): M[i][j] = vec[i]
        self.pow_mats[e] = M
        return M

def nullspace_Q(rows, ncols):
    A = [[Fraction(v) for v in r] for r in rows]
    m = len(A); piv = []; r = 0
    for c in range(ncols):
        pv = None
        for i in range(r, m):
            if A[i][c] != 0: pv = i; break
        if pv is None: continue
        A[r], A[pv] = A[pv], A[r]
        p0 = A[r][c]; A[r] = [v/p0 for v in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]; A[i] = [a - f*b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
        if r == m: break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [Fraction(0)]*ncols; v[fc] = Fraction(1)
        for i, pc in enumerate(piv): v[pc] = -A[i][fc]
        basis.append(v)
    return basis

def setup(kind, n):
    if kind == "cyclic":
        pts = list(range(n)); chars = list(range(n))
        pair = lambda g, ch: (g*ch) % n
        units = [u for u in range(1, n) if gcd(u, n) == 1]
        auts = [lambda g, u=u: (u*g) % n for u in units]
        trans = [lambda g, t=t: (g + t) % n for t in range(n)]
    else:
        pts = [(a, b) for a in range(n) for b in range(n)]; chars = pts
        pair = lambda g, ch: (g[0]*ch[0] + g[1]*ch[1]) % n
        mats = [(a, b, c, d) for a in range(n) for b in range(n) for c in range(n) for d in range(n) if gcd((a*d - b*c) % n, n) == 1]
        auts = [lambda g, M=M: ((M[0]*g[0] + M[1]*g[1]) % n, (M[2]*g[0] + M[3]*g[1]) % n) for M in mats]
        trans = [lambda g, t=t: ((g[0] + t[0]) % n, (g[1] + t[1]) % n) for t in pts]
    return pts, chars, pair, auts, trans

def canon(S, auts, trans):
    best = None
    for A in auts:
        SA = [A(g) for g in S]
        for T in trans:
            St = tuple(sorted(T(g) for g in SA))
            if best is None or St < best: best = St
    return best

def orbit_reps(pts, m, auts, trans):
    seen = set(); reps = []
    base = pts[0]
    for rest in itertools.combinations([g for g in pts if g != base], m - 1):
        S = (base,) + rest
        c = canon(S, auts, trans)
        if c in seen: continue
        seen.add(c); reps.append(c)
    return reps

def Z_of_S(S, chars, pair, K):
    m = len(S); phi = K.phi
    # row block for character ch: phi x (m*phi) integer matrix
    def block(ch):
        rows = [[0]*(m*phi) for _ in range(phi)]
        for s_i, g in enumerate(S):
            M = K.mul_by_omega_power(pair(g, ch))
            for u in range(phi):
                for v in range(phi): rows[u][s_i*phi + v] = M[u][v]
        return rows
    blocks = {ch: block(ch) for ch in chars}
    best = 0; bestT = None
    for j in range(0, m):
        for R in itertools.combinations(chars, j):
            rows = [r for ch in R for r in blocks[ch]]
            basis = nullspace_Q(rows, m*phi) if rows else [[Fraction(int(i == t)) for i in range(m*phi)] for t in range(m*phi)]
            if not basis: continue
            if any(all(v[s_i*phi + u] == 0 for v in basis for u in range(phi)) for s_i in range(m)): continue
            T = []
            for ch in chars:
                B = blocks[ch]
                if all(all(sum(B[u][i]*v[i] for i in range(m*phi)) == 0 for u in range(phi)) for v in basis): T.append(ch)
            if len(T) > best: best, bestT = len(T), tuple(T)
    return best, bestT

if __name__ == "__main__":
    kind, n, mmin, mmax = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    pts, chars, pair, auts, trans = setup(kind, n)
    K = Cyc(n)
    print(f"{kind} n={n}: |G|={len(pts)}, exact arithmetic in Q(omega_{n}) (degree {K.phi}); affine symmetry group size {len(auts)*len(trans)}")
    t0 = time.time(); running = 0
    for m in range(mmin, mmax + 1):
        reps = orbit_reps(pts, m, auts, trans)
        best = -1; bestS = None; bestT = None; hist = {}
        for S in reps:
            z, T = Z_of_S(S, chars, pair, K)
            hist[z] = hist.get(z, 0) + 1
            if z > best: best, bestS, bestT = z, S, T
        running = max(running, best)
        print(f"  m={m}: Z(G,m)={best} (Z_<= = {running}) attained by S={bestS}, zero set T={bestT}; orbits={len(reps)} (exhaustive), histogram={dict(sorted(hist.items()))}  [{time.time()-t0:.1f}s]")
        sys.stdout.flush()
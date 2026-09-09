"""E2: exact checks of the ingredients of the (1-omega)-adic proof.
(a) Clifford identities  F' Q_s W_g Q_s^* F'^*  =  p * omega^e * W_{M_s g},  M_s(a,b) = (-(s a + b), a),
    for all s in F_p, all g, p in {3,5,7,11}; exact arithmetic in Z[omega] = Z[x]/Phi_p.
(b) For random C = sum c_g W_g with c_g in Z[omega] (several regimes incl. forced cancellations and
    positive valuations): exact rank over Q(omega) (via regular representation over Q) versus the
    F_p-rank of the reduction mod (1-omega) of U C U^{-1} for every direction U in {I, F'Q_s};
    checks rank_Q(omega)(C) >= rank_Fp(reduction) for every direction, that the reduction equals the
    predicted circulant of fibre sums, and that max over directions of the reduced rank >= p-l+1.
"""
import random, itertools, sys, time
from fractions import Fraction

def make_ring(p):
    # elements: tuple of p ints (coeffs of omega^0..omega^{p-1}), canonical: last coeff 0
    def canon(v):
        c = v[p-1]
        return tuple(x - c for x in v[:p-1]) + (0,)
    def add(u, v): return canon(tuple(a+b for a, b in zip(u, v)))
    def sub(u, v): return canon(tuple(a-b for a, b in zip(u, v)))
    def neg(u): return canon(tuple(-a for a in u))
    def mul(u, v):
        w = [0]*p
        for i, a in enumerate(u):
            if a:
                for j, b in enumerate(v):
                    if b:
                        w[(i+j) % p] += a*b
        return canon(tuple(w))
    def smul(k, u): return canon(tuple(k*a for a in u))
    def om(e):  # omega^e
        v = [0]*p; v[e % p] = 1; return canon(tuple(v))
    def conj(u):  # omega -> omega^{-1}
        v = [0]*p
        for i, a in enumerate(u): v[(-i) % p] += a
        return canon(tuple(v))
    def iszero(u): return all(a == 0 for a in u)
    def intdiv(u, k):  # exact division by integer k
        assert all(a % k == 0 for a in u), (u, k)
        return canon(tuple(a//k for a in u))
    def red(u):  # reduction mod (1-omega): omega -> 1, then mod p
        return sum(u) % p
    one = om(0); zero = canon((0,)*p)
    return dict(canon=canon, add=add, sub=sub, neg=neg, mul=mul, smul=smul, om=om, conj=conj,
                iszero=iszero, intdiv=intdiv, red=red, one=one, zero=zero)

def matmul(R, A, B):
    p = len(A)
    out = []
    for i in range(p):
        row = []
        for j in range(p):
            acc = R['zero']
            for k in range(p):
                acc = R['add'](acc, R['mul'](A[i][k], B[k][j]))
            row.append(acc)
        out.append(row)
    return out

def weyl(R, p, a, b):
    # (X^a Z^b)_{j,k} = omega^{b k} [j = k+a]
    M = [[R['zero']]*p for _ in range(p)]
    for k in range(p):
        M[(k+a) % p][k] = R['om'](b*k)
    return M

def fourier(R, p):  # F'_{jk} = omega^{jk}
    return [[R['om'](j*k) for k in range(p)] for j in range(p)]

def qgate(R, p, s):  # Q_s = diag(omega^{s * inv2 * j^2})
    inv2 = pow(2, -1, p)
    M = [[R['zero']]*p for _ in range(p)]
    for j in range(p): M[j][j] = R['om'](s*inv2*j*j)
    return M

def adj(R, A):
    p = len(A)
    return [[R['conj'](A[j][i]) for j in range(p)] for i in range(p)]

def identity(R, p):
    return [[R['one'] if i == j else R['zero'] for j in range(p)] for i in range(p)]

def check_clifford(p):
    R = make_ring(p)
    F = fourier(R, p); Fs = adj(R, F)
    ok = 0
    for s in range(p):
        Q = qgate(R, p, s); Qs = adj(R, Q)
        U = matmul(R, F, Q); Us = matmul(R, Qs, Fs)
        for a in range(p):
            for b in range(p):
                W = weyl(R, p, a, b)
                T = matmul(R, matmul(R, U, W), Us)
                a2, b2 = (-(s*a+b)) % p, a % p
                Wt = weyl(R, p, a2, b2)
                t = T[a2][0]
                e = None
                for ee in range(p):
                    if t == R['smul'](p, R['om'](ee)): e = ee; break
                assert e is not None, (p, s, a, b, t)
                E = [[R['smul'](p, R['mul'](R['om'](e), Wt[i][j])) for j in range(p)] for i in range(p)]
                assert T == E, (p, s, a, b)
                ok += 1
    return ok

def rank_frac(M):
    M = [row[:] for row in M]; rows = len(M); cols = len(M[0]); r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] != 0: piv = i; break
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [x - f*y for x, y in zip(M[i], M[r])]
        r += 1
        if r == rows: break
    return r

def rank_Qomega(R, p, C):
    """rank over Q(omega) = rank over Q of the regular representation, divided by p-1."""
    n = p - 1
    def regrep(u):
        cols = []
        for j in range(n):
            v = R['mul'](u, R['om'](j))
            cols.append(list(v[:n]))
        return [[cols[j][i] for j in range(n)] for i in range(n)]
    N = p*n
    big = [[Fraction(0)]*N for _ in range(N)]
    for i in range(p):
        for j in range(p):
            m = regrep(C[i][j])
            for r in range(n):
                for c in range(n):
                    big[i*n+r][j*n+c] = Fraction(m[r][c])
    rk = rank_frac(big)
    assert rk % n == 0
    return rk // n

def rank_modp(M, p):
    M = [[x % p for x in row] for row in M]; rows = len(M); cols = len(M[0]); r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c]: piv = i; break
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], -1, p)
        M[r] = [(x*inv) % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f*y) % p for x, y in zip(M[i], M[r])]
        r += 1
    return r

def valuation_1mo(R, p, u):
    """(1-omega)-adic valuation v of u != 0 in Z[omega], and u/(1-omega)^v."""
    v = 0
    prodrest = R['one']
    for t in range(2, p): prodrest = R['mul'](prodrest, R['sub'](R['one'], R['om'](t)))
    while R['red'](u) == 0:
        u = R['intdiv'](R['mul'](u, prodrest), p)   # (1-omega)^{-1} = prodrest / p
        v += 1
    return v, u

def ord_at_one_modp(coeffs, p):
    g = [0]*p
    for t, c in coeffs.items(): g[t % p] = (g[t % p] + c) % p
    assert any(g)
    r = 0
    while True:
        if sum(g) % p != 0: return r
        n = len(g); q = [0]*(n-1); acc = 0
        for i in range(n-1, 0, -1):
            acc = (acc + g[i]) % p
            q[i-1] = acc
        g = q; r += 1
        if not any(g): return r

def build(R, p, S, coeffs):
    C = None
    for g, c in zip(S, coeffs):
        W = weyl(R, p, *g)
        T = [[R['mul'](c, W[i][j]) for j in range(p)] for i in range(p)]
        C = T if C is None else [[R['add'](C[i][j], T[i][j]) for j in range(p)] for i in range(p)]
    return C

def padic_test(p, S, coeffs, R, U_list):
    l = len(S)
    C = build(R, p, S, coeffs)
    rk = rank_Qomega(R, p, C)
    vals = [valuation_1mo(R, p, c) for c in coeffs]
    vmin = min(v for v, _ in vals)
    one_minus = R['sub'](R['one'], R['om'](1))
    scaled = []
    for (v, u), c in zip(vals, coeffs):
        x = u
        for _ in range(v - vmin): x = R['mul'](x, one_minus)
        scaled.append(x)
    cbar = [R['red'](x) for x in scaled]
    assert any(cbar)
    Cs = build(R, p, S, scaled)
    assert rank_Qomega(R, p, Cs) == rk
    best = 0
    for name, lam, U, Us in U_list:
        T = matmul(R, matmul(R, U, Cs), Us)
        if name != 'I':
            T = [[R['intdiv'](T[i][j], p) for j in range(p)] for i in range(p)]  # exact division (integrality of U C U^-1)
        red = [[R['red'](T[i][j]) for j in range(p)] for i in range(p)]
        rk_red = rank_modp(red, p)
        assert rk_red <= rk, ("rank inequality violated", p, S, name, rk_red, rk)
        fib = {}
        for g, c in zip(S, cbar):
            t = lam(g); fib[t] = (fib.get(t, 0) + c) % p
        pred = [[0]*p for _ in range(p)]
        for t, c in fib.items():
            for k in range(p): pred[(k+t) % p][k] = (pred[(k+t) % p][k] + c) % p
        assert pred == red, ("reduction != predicted circulant", p, S, name)
        nz = {t: c for t, c in fib.items() if c}
        if nz:
            m = len(nz); o = ord_at_one_modp(nz, p)
            assert rk_red == p - o and o <= m - 1, (rk_red, p, o, m)
        best = max(best, rk_red)
    assert best >= p - l + 1, ("bound failed", p, S, best)
    return rk, best

def main():
    t0 = time.time()
    for p in [3, 5, 7, 11]:
        n = check_clifford(p)
        print(f"(a) p={p}: Clifford identities verified exactly for all s,g: {n} cases  [{time.time()-t0:.1f}s]", flush=True)
    random.seed(7)
    for p in [5, 7, 11]:
        R = make_ring(p)
        F = fourier(R, p); Fs = adj(R, F)
        U_list = [('I', (lambda g: g[0]), identity(R, p), identity(R, p))]
        for s in range(p):
            Q = qgate(R, p, s); Qs = adj(R, Q)
            U_list.append((f'FQ{s}', (lambda g, s=s: (-(s*g[0]+g[1])) % p), matmul(R, F, Q), matmul(R, Qs, Fs)))
        labels = [(a, b) for a in range(p) for b in range(p)]
        ntests = 0; eq_cases = 0; results = []
        one_minus = R['sub'](R['one'], R['om'](1))
        def rand_elt(scale=2):
            return R['canon'](tuple(random.randint(-scale, scale) for _ in range(p)))
        trials = 40 if p < 11 else 12
        for trial in range(trials):
            l = random.randint(2, min(5, p - 1))
            regime = trial % 4
            if regime == 0:
                S = random.sample(labels, l); coeffs = [rand_elt() for _ in S]
            elif regime == 1:
                S = [(0, b) for b in range(l)]
                poly = [R['one']]
                for i in range(l-1):
                    new = [R['zero']]*(len(poly)+1)
                    for k, c in enumerate(poly):
                        new[k+1] = R['add'](new[k+1], c)
                        new[k] = R['sub'](new[k], R['mul'](R['om'](i), c))
                    poly = new
                coeffs = poly
            elif regime == 2:
                S = random.sample(labels, l)
                coeffs = [R['mul'](rand_elt(), one_minus) if random.random() < 0.5 else rand_elt() for _ in S]
            else:
                a0 = random.randrange(p)
                S = [(a0, b) for b in random.sample(range(p), l-1)] + [random.choice([x for x in labels if x[0] != a0])]
                ints = [random.randint(1, p-1) for _ in range(l-1)]
                if l - 1 >= 2:
                    ints[-1] = (-sum(ints[:-1])) % p or p
                coeffs = [R['smul'](k, R['one']) for k in ints] + [rand_elt()]
            coeffs = [c if not R['iszero'](c) else R['one'] for c in coeffs]
            rk, best = padic_test(p, S, coeffs, R, U_list)
            ntests += 1
            if rk == p - l + 1: eq_cases += 1
            results.append((l, rk, best))
        print(f"(b) p={p}: {ntests} exact instances; for every direction rank_Q(w)(C) >= rank_Fp(reduction) and reduction == fibre-sum circulant; "
              f"max_dir reduced rank >= p-l+1 in every case; equality rank=p-l+1 in {eq_cases} cases; "
              f"(l, rank, best reduced rank) sample: {results[:8]}  [{time.time()-t0:.1f}s]", flush=True)
    print("ALL EXACT CHECKS PASSED")

if __name__ == '__main__':
    main()

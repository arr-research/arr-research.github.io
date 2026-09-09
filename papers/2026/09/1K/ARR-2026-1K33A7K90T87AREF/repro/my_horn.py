"""Reviewer's own Horn-triple generator (Fulton recursion) and LR coefficients via the bialternant formula:
c^nu_{lam mu} = [x^{nu+delta}] ( a_{lam+delta}(x) * s_mu(x) ),  n = max(len) variables, s_mu by Jacobi-Trudi in h_k."""
from functools import lru_cache
import itertools
from fractions import Fraction as Q

@lru_cache(None)
def T(r, n):
    """Fulton's recursive T^n_r (own implementation)."""
    subs = list(itertools.combinations(range(1, n + 1), r))
    out = []
    for I in subs:
        for J in subs:
            for K in subs:
                if sum(I) + sum(J) != sum(K) + r * (r + 1) // 2: continue
                good = True
                for p in range(1, r):
                    for (F, G, H) in T(p, r):
                        if sum(I[f-1] for f in F) + sum(J[g-1] for g in G) > sum(K[h-1] for h in H) + p*(p+1)//2:
                            good = False; break
                    if not good: break
                if good: out.append((I, J, K))
    return tuple(out)

def part(I):
    r = len(I); return tuple(I[r-1-t] - (r-t) for t in range(r))

# polynomials: dict exponent-tuple -> int
def pmul(A, B):
    C = {}
    for ea, ca in A.items():
        for eb, cb in B.items():
            e = tuple(x + y for x, y in zip(ea, eb)); C[e] = C.get(e, 0) + ca * cb
    return {e: c for e, c in C.items() if c}

def padd(A, B, s=1):
    C = dict(A)
    for e, c in B.items(): C[e] = C.get(e, 0) + s * c
    return {e: c for e, c in C.items() if c}

@lru_cache(None)
def h(k, n):
    """complete homogeneous symmetric polynomial h_k in n variables."""
    if k < 0: return {}
    if k == 0: return {(0,)*n: 1}
    out = {}
    for comb in itertools.combinations_with_replacement(range(n), k):
        e = [0]*n
        for i in comb: e[i] += 1
        out[tuple(e)] = 1
    return out

def det(M):
    """determinant of a matrix of polynomials by Laplace expansion (small sizes)."""
    m = len(M)
    if m == 1: return M[0][0]
    tot = {}
    for j in range(m):
        if not M[0][j]: continue
        minor = [row[:j] + row[j+1:] for row in M[1:]]
        tot = padd(tot, pmul(M[0][j], det(minor)), 1 if j % 2 == 0 else -1)
    return tot

@lru_cache(None)
def schur(mu, n):
    mu = tuple(x for x in mu if x)
    if not mu: return {(0,)*n: 1}
    if len(mu) > n: return {}
    l = len(mu)
    M = [[h(mu[i] - i + j, n) for j in range(l)] for i in range(l)]
    return det(M)

def alt(beta, n):
    """a_beta = sum_sigma sgn(sigma) x^{sigma(beta)}, beta strictly decreasing of length n."""
    out = {}
    for perm in itertools.permutations(range(n)):
        # sign
        sgn = 1
        p = list(perm)
        for i in range(n):
            for j in range(i+1, n):
                if p[i] > p[j]: sgn = -sgn
        e = tuple(beta[perm[i]] for i in range(n))
        out[e] = out.get(e, 0) + sgn
    return {e: c for e, c in out.items() if c}

def lr(lam, mu, nu):
    lam = tuple(x for x in lam if x); mu = tuple(x for x in mu if x); nu = tuple(x for x in nu if x)
    if sum(lam) + sum(mu) != sum(nu): return 0
    n = max(len(lam), len(mu), len(nu), 1)
    if len(nu) > n: return 0
    lamp = lam + (0,)*(n - len(lam)); nup = nu + (0,)*(n - len(nu))
    delta = tuple(n - 1 - i for i in range(n))
    A = alt(tuple(lamp[i] + delta[i] for i in range(n)), n)
    S = schur(mu, n)
    prod = pmul(A, S)
    return prod.get(tuple(nup[i] + delta[i] for i in range(n)), 0)

def horn_lhs_s(I, J, d):
    """s-form of the Horn inequality: sum_{i in I, i<d} s_i - sum_{j in J, j>1} s_{d+1-j}."""
    f = {}
    for i in I:
        if i < d: f[i] = f.get(i, 0) + 1
    for j in J:
        if j > 1: f[d+1-j] = f.get(d+1-j, 0) - 1
    return {k: v for k, v in f.items() if v}

if __name__ == "__main__":
    import time
    # 1. my LR agrees with my Fulton recursion for d <= 7
    for d in range(2, 8):
        t0 = time.time()
        for r in range(1, d):
            S = set(); subs = list(itertools.combinations(range(1, d+1), r))
            for I in subs:
                for J in subs:
                    for K in subs:
                        if sum(I)+sum(J) != sum(K)+r*(r+1)//2: continue
                        if lr(part(I), part(J), part(K)) > 0: S.add((I, J, K))
            assert S == set(T(r, d)), (d, r)
        print(f"d={d}: own LR>0 == own Fulton recursion; counts {[len(T(r,d)) for r in range(1,d)]} ({time.time()-t0:.1f}s)", flush=True)
    # 2. Pieri triple membership for d <= 9 (Fulton) and LR value for d <= 12
    for d in range(5, 13):
        for i in range(2, d-2, 2):   # even i with i+2 <= d-1
            I = (i-1,) + tuple(range(i+1, d-1)); J = tuple(range(1, d-i-1)) + (d-i,); K = tuple(range(i, d-1))
            r = len(I); assert len(J) == r == len(K)
            assert sum(I)+sum(J) == sum(K)+r*(r+1)//2
            c = lr(part(I), part(J), part(K))
            inT = ((I, J, K) in set(T(r, d))) if d <= 9 else None
            print(f"d={d} i={i} r={r}: I={I} J={J} K={K} lam={part(I)},{part(J)},{part(K)} LR={c} inFulton={inT} sform={horn_lhs_s(I,J,d)}")
            assert c == 1 and (inT is None or inT)
    print("PIERI OK")

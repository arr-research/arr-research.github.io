"""charp_order_exhaustive.py -- exact maximal order of vanishing at x=1 in characteristic p
of polynomials with exactly m nonzero terms and exponents in [0, p^k)  (i.e. distinct mod p^k).

For an exponent set S the maximal order over all full-support coefficient vectors (over any field
of characteristic p) is the largest r such that the Lucas matrix B_r = (binom(t, i) mod p)_{i<r, t in S}
has every column in the span of the other columns (then a full-support kernel vector exists over a
large enough field; the rank criterion is field independent).  Binary search on r (monotone).

Compares  O(p^k, m) := max_S ord   with   Omega_k(m) = max{ r < p^k : prod (r_t+1) <= m }  and
checks  max_{m' <= m} O(p^k, m') == Omega_k(m)  (Mattarei 2006 Thm 2 restricted to degree < p^k).

usage: python charp_order_exhaustive.py p k mmax
"""
import sys, itertools, time
from math import comb

def rank_mod_p(rows, ncols, p):
    # rows: list of lists (ints mod p); Gaussian elimination
    M = [r[:] for r in rows]
    rank = 0
    col = 0
    nrows = len(M)
    for col in range(ncols):
        piv = None
        for i in range(rank, nrows):
            if M[i][col] % p:
                piv = i; break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = pow(M[rank][col], -1, p)
        M[rank] = [(x * inv) % p for x in M[rank]]
        for i in range(nrows):
            if i != rank and M[i][col] % p:
                f = M[i][col]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[rank])]
        rank += 1
        if rank == nrows:
            break
    return rank

def good(S, r, p, binom_table):
    # every column of B_r dependent on the others  <=>  full-support kernel vector exists
    if r == 0:
        return True
    rows = [[binom_table[t][i] for t in S] for i in range(r)]
    m = len(S)
    rk = rank_mod_p(rows, m, p)
    if rk == m:
        return False
    for j in range(m):
        rows_j = [[row[i] for i in range(m) if i != j] for row in rows]
        if rank_mod_p(rows_j, m - 1, p) != rk:
            return False
    return True

def max_ord(S, p, d, binom_table):
    lo, hi = 0, d - 1  # ord <= deg < d
    # find max r with good(S, r); good is monotone decreasing in r
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if good(S, mid, p, binom_table):
            lo = mid
        else:
            hi = mid - 1
    return lo

def omega(p, k, m):
    best = 0
    for r in range(p**k):
        w = 1; rr = r
        while rr:
            w *= (rr % p) + 1; rr //= p
        if w <= m:
            best = r
    return best

if __name__ == "__main__":
    p, k, mmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    d = p**k
    binom_table = [[comb(t, i) % p for i in range(d)] for t in range(d)]
    print(f"p={p} k={k} d={d}; exhaustive over exponent sets with 0 in S (translation invariance)")
    Oexact = {}
    t0 = time.time()
    for m in range(1, mmax + 1):
        best = -1; best_S = None; nS = 0
        for rest in itertools.combinations(range(1, d), m - 1):
            S = (0,) + rest
            nS += 1
            o = max_ord(S, p, d, binom_table)
            if o > best:
                best, best_S = o, S
        Oexact[m] = best
        Ole = max(Oexact[mm] for mm in range(1, m + 1))
        om = omega(p, k, m)
        flag = "OK" if Ole == om else "MISMATCH"
        print(f"  m={m:2d}: O_exact(m)={best:3d} (example S={best_S}),  O<=(m)={Ole:3d},  Omega_k(m)={om:3d}  {flag}   [{nS} sets, {time.time()-t0:.1f}s]")
        sys.stdout.flush()

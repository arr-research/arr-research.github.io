"""Independent exhaustive test of Theorem A (digit-weight bound) over F_p-bar.

For d = p^k, Hasse matrix H[i][t] = binom(t,i) mod p (coefficient of y^i in x^t at x = 1+y).
For a support S (subset of [0,d)), the polynomials with support in S and ord_1 >= r are the null
space V_r of H[:r, S].  Over an infinite field of char p:
  * exists f with support EXACTLY S and ord_1 EXACTLY r  <=>  rank(H[:r+1,S]) > rank(H[:r,S])
    and no unit vector e_s lies in rowspace(H[:r,S]).
  * max ord over support subset of S = (min r with rank H[:r,S] = |S|) - 1.
Checks: (1) exact version: w_p(r) <= |S| for all achievable (S, r);
        (2) monotone version: max over |S| <= m equals Omega_k(m).
Supports enumerated up to the affine group of Z/d (translation t->t+1, dilation t->ut).
usage: python thmA_check.py p k mmax
"""
import sys, itertools
from math import comb, gcd

def digit_weight(r, p):
    w = 1
    while r:
        w *= (r % p) + 1; r //= p
    return w

def omega_k(p, k, m):
    return max(r for r in range(p**k) if digit_weight(r, p) <= m)

def reduce_rows(rows, p, ncols):
    """rows: list of vectors (lists) mod p; returns reduced echelon basis (list of (pivot, vec))"""
    basis = []
    for v in rows:
        v = v[:]
        for (piv, b) in basis:
            if v[piv]:
                f = v[piv]
                v = [(x - f*y) % p for x, y in zip(v, b)]
        nz = [i for i in range(ncols) if v[i]]
        if nz:
            piv = nz[0]; inv = pow(v[piv], -1, p)
            v = [(x*inv) % p for x in v]
            # reduce existing basis
            basis = [(pv, [(x - b[piv]*y) % p for x, y in zip(b, v)]) for (pv, b) in basis]
            basis.append((piv, v))
    return basis

def in_rowspace(basis, v, p):
    v = v[:]
    for (piv, b) in basis:
        if v[piv]:
            f = v[piv]; v = [(x - f*y) % p for x, y in zip(v, b)]
    return not any(v)

def canonical(S, d, units):
    best = None
    for u in units:
        for t in range(d):
            T = tuple(sorted(((u*s + t) % d) for s in S))
            if best is None or T < best: best = T
    return best

def main():
    p, k, mmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    d = p**k
    H = [[comb(t, i) % p for t in range(d)] for i in range(d)]
    units = [u for u in range(1, d) if gcd(u, d) == 1]
    om = {m: omega_k(p, k, m) for m in range(1, d+1)}
    seen = set()
    monotone_max = {m: -1 for m in range(1, mmax+1)}   # max ord over supports of size exactly m (subset-allowed)
    exact_max = {m: -1 for m in range(1, mmax+1)}      # max exact order with support exactly m
    exact_viol = []; count = 0
    for m in range(1, mmax+1):
        for rest in itertools.combinations(range(1, d), m-1):
            S = (0,) + rest
            c = canonical(S, d, units)
            if c in seen: continue
            seen.add(c); count += 1
            cols = list(S)
            basis = []
            rank = 0
            for r in range(d):
                row = [H[r][t] for t in cols]
                newbasis = reduce_rows([b for _, b in basis] + [row], p, m)
                newrank = len(newbasis)
                if newrank > rank:
                    # exact order r achievable with support exactly S iff no unit vector in rowspace(H[:r,S])
                    full = all(not in_rowspace(basis, [1 if j == s else 0 for j in range(m)], p) for s in range(m))
                    if full:
                        exact_max[m] = max(exact_max[m], r)
                        if digit_weight(r, p) > m:
                            exact_viol.append((S, r, digit_weight(r, p)))
                basis, rank = newbasis, newrank
                if rank == m:
                    monotone_max[m] = max(monotone_max[m], r)
                    break
            else:
                raise RuntimeError("rank never full")
    print(f"p={p} k={k} d={d}: {count} support orbits examined (m<={mmax})")
    ok = True
    run = -1
    for m in range(1, mmax+1):
        run = max(run, monotone_max[m])
        flag = "OK" if run == om[m] else "MISMATCH"
        if run != om[m]: ok = False
        print(f"  m={m}: max ord (support<=m) = {run}, Omega_k(m) = {om[m]} {flag};  max exact order with exactly m terms = {exact_max[m]}, w_p = {digit_weight(exact_max[m],p) if exact_max[m]>=0 else None}")
    print("exact-version violations (w_p(ord) > #terms):", exact_viol[:5], "count", len(exact_viol))
    print("RESULT:", "ALL OK" if ok and not exact_viol else "PROBLEM")

main()

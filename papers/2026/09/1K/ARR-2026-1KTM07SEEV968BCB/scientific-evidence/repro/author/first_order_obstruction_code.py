"""first_order_obstruction_code.py -- the F_p-linear code N(p,k) of residue vectors c-bar on G = (Z/p^k)^2 whose fibre sums
vanish in EVERY primitive direction (equivalently: zero sum on every coset of every cyclic subgroup of order p^k).
Lemma N of the report claims: every nonzero element of N has support >= 2p, attained by 1_{L1} - 1_{L2} (two parallel lines
in a coset of the p-torsion T_1).  This script computes dim N over F_p and the minimum weight exactly when p^dim is small
(full enumeration), otherwise reports the weight of the two-line word and a randomized low-weight search (upper bound only).
usage: python first_order_obstruction_code.py d [enum_limit]
"""
import sys, itertools, random
from math import gcd

def factor_pk(d):
    p = 2
    while d % p: p += 1
    k = 0; dd = d
    while dd % p == 0: dd //= p; k += 1
    assert dd == 1
    return p, k

def primitive_directions(p, k):
    d = p**k
    dirs = [(1, s) for s in range(d)] + [(s, 1) for s in range(0, d, p)]
    assert len(dirs) == p**(k-1)*(p+1)
    return dirs

def nullspace_mod_p(rows, n, p):
    M = [r[:] for r in rows]; piv = []; rank = 0
    for col in range(n):
        pr = None
        for i in range(rank, len(M)):
            if M[i][col] % p: pr = i; break
        if pr is None: continue
        M[rank], M[pr] = M[pr], M[rank]
        inv = pow(M[rank][col], -1, p)
        M[rank] = [(x*inv) % p for x in M[rank]]
        for i in range(len(M)):
            if i != rank and M[i][col] % p:
                f = M[i][col]; M[i] = [(a - f*b) % p for a, b in zip(M[i], M[rank])]
        piv.append(col); rank += 1
        if rank == len(M): break
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        v = [0]*n; v[fc] = 1
        for i, pc in enumerate(piv): v[pc] = (-M[i][fc]) % p
        basis.append(v)
    return basis

if __name__ == "__main__":
    d = int(sys.argv[1]); enum_limit = int(sys.argv[2]) if len(sys.argv) > 2 else 2*10**6
    p, k = factor_pk(d)
    labels = [(a, b) for a in range(d) for b in range(d)]
    idx = {g: i for i, g in enumerate(labels)}
    rows = []
    for (al, be) in primitive_directions(p, k):
        for t in range(d):
            row = [0]*(d*d)
            for (a, b) in labels:
                if (al*a + be*b) % d == t: row[idx[(a, b)]] = 1
            rows.append(row)
    basis = nullspace_mod_p(rows, d*d, p)
    dim = len(basis)
    print(f"d={d}={p}^{k}: #primitive directions={p**(k-1)*(p+1)}, #fibre conditions={len(rows)}, dim N over F_{p} = {dim}")
    # two-parallel-lines word
    q = p**(k-1)
    L1 = [(0, b*q % d) for b in range(p)]; L2 = [(q, b*q % d) for b in range(p)]
    w = [0]*(d*d)
    for g in L1: w[idx[g]] = 1
    for g in L2: w[idx[g]] = (p-1) % p
    inN = all(sum(r[i]*w[i] for i in range(d*d)) % p == 0 for r in rows)
    print(f"  two-parallel-lines word 1_L1 - 1_L2: weight {sum(1 for x in w if x)} , in N: {inN}")
    if p**dim <= enum_limit:
        best = None; cnt = {}
        for coeffs in itertools.product(range(p), repeat=dim):
            if not any(coeffs): continue
            v = [0]*(d*d)
            for c, bvec in zip(coeffs, basis):
                if c:
                    for i in range(d*d):
                        if bvec[i]: v[i] = (v[i] + c*bvec[i]) % p
            wt = sum(1 for x in v if x)
            cnt[wt] = cnt.get(wt, 0) + 1
            if best is None or wt < best[0]: best = (wt, v)
        print(f"  EXHAUSTIVE over {p**dim - 1} nonzero codewords: min weight = {best[0]}; weight distribution (weight: count) = {dict(sorted(cnt.items()))}")
        supp = [labels[i] for i in range(d*d) if best[1][i]]
        print(f"  a minimum-weight word: support {supp}, values {[best[1][idx[g]] for g in supp]}")
    else:
        rng = random.Random(1)
        best = min(sum(1 for x in v if x) for v in basis)
        for it in range(20000):
            a = [rng.randrange(p) for _ in range(dim)]
            if not any(a): continue
            v = [0]*(d*d)
            for c, bvec in zip(a, basis):
                if c:
                    for i in range(d*d):
                        if bvec[i]: v[i] = (v[i] + c*bvec[i]) % p
            best = min(best, sum(1 for x in v if x))
        print(f"  dim too large for enumeration: basis/random-combination minimum weight (upper bound only) = {best}")
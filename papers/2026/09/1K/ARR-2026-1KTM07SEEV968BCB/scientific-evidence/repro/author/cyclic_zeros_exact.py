"""cyclic_zeros_exact.py -- maximal number of d-th roots of unity annihilated by a polynomial with
prescribed exponent set S (all coefficients nonzero), Z(d,S), and Z(d,m) = max_{|S|=m} Z(d,S),
Z<=(d,m) = max_{m'<=m} Z(d,m').

Exact arithmetic in F_q for a prime q = 1 mod d (omega -> element of order d in F_q); ranks over F_q
can only be <= ranks over Q(omega_d), so results are cross-checked with two independent primes and,
for the extremal examples, certified over Q(omega_d) by cyclotomic_certify.py.

Method ("flats"): the rows F_zeta = (zeta^s)_{s in S}, zeta in mu_d, are d hyperplanes in the coefficient
space k^S; the zero set of a coefficient vector c is {zeta : F_zeta . c = 0}.  The maximal zero sets are
the closures T(L) = {zeta : L subset H_zeta} of flats L (intersections of hyperplanes) that are not
contained in a coordinate hyperplane.  We enumerate flats as kernels of row subsets of size <= m-1
(any flat is cut out by <= m-1 independent rows), which is exhaustive.

usage: python cyclic_zeros_exact.py d mmin mmax [maxorbits]
Symmetry used: translation (0 in S) and Galois action S -> uS, u a unit mod d (both preserve Z(d,S)).
"""
import sys, itertools, time, random
from math import gcd

def find_prime(d, start):
    q = start - (start - 1) % d  # q = 1 mod d
    while True:
        if q % d == 1 and is_prime(q):
            return q
        q += d

def is_prime(n):
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n % p == 0: return n == p
    dd = n - 1; s = 0
    while dd % 2 == 0: dd //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17):
        x = pow(a, dd, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True

def elem_of_order(d, q):
    for g in range(2, q):
        w = pow(g, (q - 1) // d, q)
        ok = True
        for pp in set(prime_factors(d)):
            if pow(w, d // pp, q) == 1: ok = False; break
        if ok: return w
    raise RuntimeError

def prime_factors(n):
    out = []; p = 2
    while p * p <= n:
        while n % p == 0: out.append(p); n //= p
        p += 1
    if n > 1: out.append(n)
    return out

def nullspace_mod(rows, n, q):
    """basis of {c in F_q^n : rows . c = 0}"""
    M = [r[:] for r in rows]
    pivcols = []
    rank = 0
    for col in range(n):
        piv = None
        for i in range(rank, len(M)):
            if M[i][col] % q: piv = i; break
        if piv is None: continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = pow(M[rank][col], -1, q)
        M[rank] = [(x * inv) % q for x in M[rank]]
        for i in range(len(M)):
            if i != rank and M[i][col] % q:
                f = M[i][col]
                M[i] = [(a - f * b) % q for a, b in zip(M[i], M[rank])]
        pivcols.append(col); rank += 1
        if rank == len(M): break
    free = [c for c in range(n) if c not in pivcols]
    basis = []
    for fc in free:
        v = [0] * n; v[fc] = 1
        for i, pc in enumerate(pivcols):
            v[pc] = (-M[i][fc]) % q
        basis.append(v)
    return basis

def Z_of_S(S, d, q, w):
    m = len(S)
    rows = [[pow(w, (j * s) % d, q) for s in S] for j in range(d)]
    best = 0
    best_T = None
    seen = set()
    # flats cut out by <= m-1 rows; also the empty flat (whole space): zero set = rows that vanish identically (none)
    for j in range(0, m):
        for R in itertools.combinations(range(d), j):
            basis = nullspace_mod([rows[i] for i in R], m, q)
            if not basis: continue
            # full support condition: no coordinate identically zero on L
            if any(all(v[s] == 0 for v in basis) for s in range(m)):
                continue
            # closure
            T = tuple(i for i in range(d) if all(sum(rows[i][s] * v[s] for s in range(m)) % q == 0 for v in basis))
            if len(T) > best:
                best, best_T = len(T), T
    return best, best_T

def orbit_reps(d, m, maxorbits=None, seed=0):
    units = [u for u in range(1, d) if gcd(u, d) == 1]
    seen = set(); reps = []
    for rest in itertools.combinations(range(1, d), m - 1):
        S = (0,) + rest
        canon = None
        for u in units:
            Su = sorted((u * s) % d for s in S)
            # translate so that each element is the origin, take lexicographic min
            for t in Su:
                St = tuple(sorted((s - t) % d for s in Su))
                if canon is None or St < canon: canon = St
        if canon in seen: continue
        seen.add(canon); reps.append(canon)
    if maxorbits and len(reps) > maxorbits:
        random.Random(seed).shuffle(reps); reps = reps[:maxorbits]
    return reps

if __name__ == "__main__":
    d = int(sys.argv[1]); mmin = int(sys.argv[2]); mmax = int(sys.argv[3])
    maxorbits = int(sys.argv[4]) if len(sys.argv) > 4 else None
    q1 = find_prime(d, 10**9); q2 = find_prime(d, 2 * 10**9)
    w1 = elem_of_order(d, q1); w2 = elem_of_order(d, q2)
    print(f"d={d}, primes q1={q1}, q2={q2}")
    t0 = time.time()
    for m in range(mmin, mmax + 1):
        reps = orbit_reps(d, m, maxorbits)
        best = -1; bestS = None; bestT = None; per = {}
        for S in reps:
            z1, T1 = Z_of_S(S, d, q1, w1)
            z2, T2 = Z_of_S(S, d, q2, w2)
            if z1 != z2:
                print("  WARNING prime disagreement", S, z1, z2)
            z = max(z1, z2)
            per[S] = z
            if z > best: best, bestS, bestT = z, S, (T1 if z1 >= z2 else T2)
        hist = {}
        for S, z in per.items(): hist[z] = hist.get(z, 0) + 1
        tag = "exhaustive" if maxorbits is None or len(reps) < maxorbits else f"sampled {maxorbits}"
        print(f"  m={m:2d}: Z(d,m)={best:3d}  attained by S={bestS}, T={bestT}   orbits={len(reps)} ({tag}), histogram {dict(sorted(hist.items()))}   [{time.time()-t0:.1f}s]")
        sys.stdout.flush()

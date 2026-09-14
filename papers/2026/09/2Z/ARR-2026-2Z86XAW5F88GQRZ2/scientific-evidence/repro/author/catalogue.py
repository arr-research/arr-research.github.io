"""Tile catalogue for the (m,3) stratum (explicit Horn triples, LR checked by lr.py).
A tile is (K, U, nN): RHS sum_{k in K} lambda_k, LHS  sum_{u in U} s_u - sum_{t=d-nN}^{d-1} s_t, |U| = nN + 1.
Triple: I = U u W, J = {1} u {d+1-t : t in W u N}, with W the largest r-1-nN elements of [d-1-nN] minus U (or alternatives).
RHS families: tails (t..d-q) with optional b-indices, single/double holes, singletons, lower Weyl."""
import itertools, numpy as np
from functools import lru_cache
from lr import lr, part, strip

def rhs_sets(m, z, maxholes=2):
    d = m + z + 3; zeros = list(range(m + 1, m + z + 1)); Ks = set()
    bidx = {1: d, 2: d - 1, 3: d - 2}
    bsubsets = [()] + [(i,) for i in (1, 2, 3)] + [(1, 2), (1, 3), (2, 3)]
    for t in range(1, m + 1):
        hole_sets = [()]
        for h in range(1, maxholes + 1): hole_sets += list(itertools.combinations(range(t, m + 1), h))
        for holes in hole_sets:
            Ka = [k for k in range(t, m + 1) if k not in holes]
            if not Ka: continue
            for bs in bsubsets:
                Ks.add(tuple(sorted(Ka + zeros + [bidx[i] for i in bs])))
    for j in range(1, m + 1): Ks.add((j,))                       # Weyl
    for j in (1, 2, 3): Ks.add(tuple(k for k in range(1, d + 1) if k != d + 1 - j))   # lower Weyl s_j >= b_j
    return sorted(Ks, key=lambda K: (len(K), K))

@lru_cache(None)
def lr_pos(I, J, K):
    return lr(part(I), part(J), part(K)) > 0

def tiles(m, z, umax=None, verbose=False, maxholes=2, maxN=2):
    d = m + z + 3; umax = umax or (m + 2); out = []
    for K in rhs_sets(m, z, maxholes):
        r = len(K)
        for nN in range(0, maxN + 1):
            if r - 1 - nN < 0: continue
            N = tuple(range(d - nN, d)); sN = sum(N)
            sU = sum(K) + r * (r + 1) // 2 - 1 - (r - 1) * (d + 1) + sN
            for U in itertools.combinations(range(1, min(umax, d - 1 - nN) + 1), nN + 1):
                if sum(U) != sU: continue
                pool = [t for t in range(1, d - nN) if t not in U]
                nW = r - 1 - nN
                if nW > len(pool): continue
                # all W subset pool with the forced sum (sum condition), first with LR > 0 wins
                sW = sum(K) + r * (r + 1) // 2 - sum(U) - 1 - (nW + nN) * (d + 1) + sN + sum(U)  # placeholder, recomputed below
                target = sum(K) + r * (r + 1) // 2 - (sum(U) + 1 + (nW + nN) * (d + 1) - sN)   # = 2*sum(W)?? see derivation
                ok = None
                for W in itertools.combinations(pool, nW):
                    I = tuple(sorted(U + W)); J = tuple(sorted((1,) + tuple(d + 1 - t for t in W + N)))
                    if len(set(J)) < r or max(J) > d: continue
                    if sum(I) + sum(J) != sum(K) + r * (r + 1) // 2: continue
                    if lr_pos(I, J, K): ok = (I, J, K); break
                if ok: out.append((K, U, N, ok))
    return out

def tile_rows(m, z, umax=None, maxholes=2, maxN=2):
    """Rows (coef on s_1..s_{d-1}, coef on lambda_1..lambda_d) for the restricted LP."""
    d = m + z + 3; rows = []
    for K, U, N, (I, J, KK) in tiles(m, z, umax, maxholes=maxholes, maxN=maxN):
        a = np.zeros(d - 1)
        for u in U: a[u - 1] += 1
        for t in N: a[t - 1] -= 1
        b = np.zeros(d)
        for k in K: b[k - 1] += 1
        rows.append((a, b, (K, U, N, I, J)))
    return rows

if __name__ == "__main__":
    import sys, time
    m, z = int(sys.argv[1]), int(sys.argv[2]); t0 = time.time()
    T = tiles(m, z); d = m + z + 3
    print(f"m={m} z={z} d={d}: {len(T)} tiles ({time.time()-t0:.1f}s)")
    for K, U, N, (I, J, KK) in T:
        Ka = [k for k in K if k <= m]; Kb = [{d: 1, d - 1: 2, d - 2: 3}[k] for k in K if k >= d - 2]
        print(f"  +s{list(U)} -s{[f'd-{d-t}' for t in N]} >= {'+'.join('a%d'%k for k in Ka)}{''.join('-b%d'%i for i in Kb)}   I={I} J={J}")

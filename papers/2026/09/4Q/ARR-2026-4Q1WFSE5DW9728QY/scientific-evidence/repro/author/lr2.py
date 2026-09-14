"""Independent Littlewood-Richardson coefficients (second implementation, for cross-checking lr.py):
c^nu_{lam mu} = sum_{w in S_n} sgn(w) K_{mu, nu+delta - w(lam+delta)}   (bialternant a_{lam+delta} s_mu = sum_nu c^nu a_{nu+delta}),
with Kostka numbers K_{mu,alpha} (SSYT of shape mu, content alpha) by horizontal-strip recursion. n = number of parts used."""
from functools import lru_cache
import itertools

def strip(p):
    p = list(p)
    while p and p[-1] == 0: p.pop()
    return tuple(p)

@lru_cache(None)
def kostka(mu, alpha):
    """SSYT of shape mu with content alpha (composition, entries >= 0)."""
    mu = strip(mu); alpha = tuple(alpha)
    if sum(mu) != sum(alpha): return 0
    if not alpha: return 1 if not mu else 0
    k = alpha[-1]; rest = alpha[:-1]
    if k == 0: return kostka(mu, rest)
    # remove a horizontal strip of size k from mu: mu' with mu'_i <= mu_i, mu'_i >= mu_{i+1}, sum diff = k
    L = len(mu); tot = 0
    def rec(i, remaining, cur):
        nonlocal tot
        if i == L:
            if remaining == 0: tot += kostka(tuple(cur), rest)
            return
        lo = mu[i + 1] if i + 1 < L else 0
        for take in range(0, min(remaining, mu[i] - lo) + 1):
            cur.append(mu[i] - take); rec(i + 1, remaining - take, cur); cur.pop()
    rec(0, k, [])
    return tot

def lr2(lam, mu, nu):
    lam, mu, nu = strip(lam), strip(mu), strip(nu)
    if sum(lam) + sum(mu) != sum(nu): return 0
    n = max(len(lam), len(nu), 1)
    if len(lam) > len(nu) or any(lam[i] > nu[i] for i in range(len(lam))): return 0
    lam = lam + (0,) * (n - len(lam)); nu = nu + (0,) * (n - len(nu))
    ld = [lam[i] + n - 1 - i for i in range(n)]; nd = [nu[i] + n - 1 - i for i in range(n)]
    total = 0
    # assign w(i) for i = 0..n-1 with content_i = nd[i] - ld[w(i)] >= 0, pruned; sign by inversion count
    def rec(i, used, content, inv):
        nonlocal total
        if i == n:
            total += (-1) ** inv * kostka(mu, tuple(content)); return
        for j in range(n):
            if used & (1 << j): continue
            c = nd[i] - ld[j]
            if c < 0: continue
            # inversions: number of already-used indices greater than j
            inv_add = bin(used >> (j + 1)).count("1")
            content.append(c); rec(i + 1, used | (1 << j), content, inv + inv_add); content.pop()
    rec(0, 0, [], 0)
    return total

if __name__ == "__main__":
    from lr import lr
    import random
    random.seed(1); bad = 0; n = 0
    # cross-check on random small partitions
    def rp(maxlen, maxpart):
        L = random.randint(0, maxlen); p = sorted([random.randint(0, maxpart) for _ in range(L)], reverse=True); return strip(p)
    for _ in range(3000):
        lam, mu = rp(4, 4), rp(3, 3)
        # random nu containing lam with the right size
        size = sum(lam) + sum(mu)
        nu = list(lam) + [0] * 3
        for _ in range(sum(mu)):
            i = random.randint(0, len(nu) - 1); nu[i] += 1
        nu = tuple(sorted(nu, reverse=True))
        if list(nu) != sorted(nu, reverse=True): continue
        a, b = lr(lam, mu, nu), lr2(lam, mu, nu); n += 1
        if a != b: bad += 1; print("MISMATCH", lam, mu, nu, a, b)
    print(f"cross-check lr vs lr2 on {n} random triples: {bad} mismatches")
    # known values
    print("c^{(3,2,1)}_{(2,1),(2,1)} =", lr2((2,1),(2,1),(3,2,1)), "(expected 2)")
    print("c^{(4,2)}_{(2,1),(2,1)} =", lr2((2,1),(2,1),(4,2)), "(expected 1)")
    print("c^{(2,2,1,1)}_{(1,1),(1,1)}... c^{(2,2)}_{(1,1),(1,1)} =", lr2((1,1),(1,1),(2,2)), "(expected 1)")

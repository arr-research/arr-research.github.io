"""Littlewood-Richardson coefficients by counting LR tableaux (small partitions), and the Horn-triple <-> partition dictionary.
lam(I) = (i_r - r, ..., i_1 - 1) for I = (i_1 < ... < i_r).  Convention check against Fulton's recursion (horn_t) for d <= 7."""
from functools import lru_cache
import itertools

def part(I):
    r = len(I)
    return tuple(I[r - 1 - t] - (r - t) for t in range(r))  # (i_r - r, i_{r-1} - (r-1), ..., i_1 - 1)

def strip(p):
    p = list(p)
    while p and p[-1] == 0: p.pop()
    return tuple(p)

@lru_cache(None)
def lr(lam, mu, nu):
    """c^nu_{lam mu}: number of LR tableaux of shape nu/lam and content mu."""
    lam, mu, nu = strip(lam), strip(mu), strip(nu)
    if sum(lam) + sum(mu) != sum(nu): return 0
    n = len(nu)
    if len(lam) > n or any(lam[i] > nu[i] for i in range(len(lam))): return 0
    lam = lam + (0,) * (n - len(lam))
    if not mu: return 1 if lam == nu else 0
    k = len(mu)
    # fill rows top to bottom; row i has cells lam[i]..nu[i]-1 ; entries in 1..k weakly increasing along the row,
    # strictly increasing down columns; reverse reading word (right-to-left, top-to-bottom) is a lattice word.
    count = 0
    def rec(i, above, cnt):
        nonlocal count
        if i == n:
            count += 1; return
        L = nu[i] - lam[i]
        # choose weakly increasing sequence of length L with values 1..k; process right to left for lattice condition
        def fill(pos, row, cnt2):
            if pos < 0:
                # column strictness: entry at column c must exceed entry above (row i-1, column c) if that cell exists
                for c in range(lam[i], nu[i]):
                    up = above.get(c)
                    if up is not None and row[c - lam[i]] <= up: return
                rec(i + 1, {c: row[c - lam[i]] for c in range(lam[i], nu[i])}, cnt2)
                return
            hi = row[pos + 1] if pos + 1 < L else k
            for v in range(1, hi + 1):
                # lattice: after adding v, cnt[v] <= cnt[v-1]
                if v > 1 and cnt2[v] + 1 > cnt2[v - 1]: continue
                if cnt2[v] + 1 > mu[v - 1]: continue
                row[pos] = v; cnt2[v] += 1
                fill(pos - 1, row, cnt2)
                cnt2[v] -= 1
        fill(L - 1, [0] * L, dict(cnt))
    rec(0, {}, {v: 0 for v in range(0, k + 1)} | {0: 10**9})
    return count

def horn_valid_lr(I, J, K):
    return lr(part(I), part(J), part(K)) > 0

if __name__ == "__main__":
    from check_horn_lp import horn_t
    # convention check: for all r < d <= 7, {(I,J,K) : sum condition and c>0} == horn_t(r,d)
    for d in range(2, 8):
        for r in range(1, d):
            T = set(horn_t(r, d)); cnt = 0
            subsets = list(itertools.combinations(range(1, d + 1), r))
            S = set()
            for I in subsets:
                for J in subsets:
                    for K in subsets:
                        if sum(I) + sum(J) != sum(K) + r * (r + 1) // 2: continue
                        if horn_valid_lr(I, J, K): S.add((I, J, K))
            assert S == T, (d, r, len(S), len(T))
        print(f"d={d}: LR>0 criterion == Fulton recursion for all r (counts {[len(horn_t(r,d)) for r in range(1,d)]})")
    # Pieri triple for even i in d: I={i-1} u (i+1..d-2), J=(1..d-i-2) u {d-i}, K=(i..d-2)
    for d in range(6, 13):
        for i in range(2, d - 3):
            I = (i - 1,) + tuple(range(i + 1, d - 1)); J = tuple(range(1, d - i - 1)) + (d - i,); K = tuple(range(i, d - 1))
            assert sum(I) + sum(J) == sum(K) + len(I) * (len(I) + 1) // 2
            assert strip(part(J)) == (1,) and lr(part(I), part(J), part(K)) == 1, (d, i, part(I), part(J), part(K))
        print(f"d={d}: shifted-pair triples i=2..{d-4}: partitions (lam,mu,nu)=(((i-1)^(r-1),i-2),(1),((i-1)^r)), all c=1")

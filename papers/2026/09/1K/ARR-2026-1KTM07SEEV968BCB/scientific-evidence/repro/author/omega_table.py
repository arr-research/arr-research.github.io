"""omega_table.py -- the function Omega_k(m) = max{ r < p^k : prod_t (r_t + 1) <= m }
(r = sum_t r_t p^t base-p digits), and the equivalent recursion
    Omega_k(m) = max_{1<=n<=min(m,p)} [ (n-1) p^{k-1} + Omega_{k-1}( floor(m/n) ) ],  Omega_0(m) = 0.
Checks equality of the two definitions for all p^k <= 128 and all m, prints tables.
Also prints Meshulam's bound  zeros <= p^k - ceil( p^k (d1+d2-m)/(d1 d2) )  for comparison.
"""
import math, sys
from functools import lru_cache

def digits(r, p):
    out = []
    while r:
        out.append(r % p); r //= p
    return out

def weight(r, p):
    w = 1
    for t in digits(r, p):
        w *= (t + 1)
    return w

def omega_direct(p, k, m):
    best = 0
    for r in range(p**k):
        if weight(r, p) <= m:
            best = r
    return best

def omega_rec(p, k, m):
    @lru_cache(None)
    def O(kk, mm):
        if kk == 0 or mm <= 0:
            return 0
        best = 0
        for n in range(1, min(mm, p) + 1):
            best = max(best, (n - 1) * p**(kk - 1) + O(kk - 1, mm // n))
        return best
    return O(k, m)

def meshulam_zero_bound(d, m):
    divs = [x for x in range(1, d + 1) if d % x == 0]
    for d1, d2 in zip(divs, divs[1:]):
        if d1 <= m <= d2:
            return d - math.ceil(d * (d1 + d2 - m) / (d1 * d2))
    return d - 1

if __name__ == "__main__":
    ok = True
    for p in (2, 3, 5, 7):
        for k in range(1, 8):
            d = p**k
            if d > 128:
                break
            for m in range(1, d + 1):
                a, b = omega_direct(p, k, m), omega_rec(p, k, m)
                if a != b:
                    ok = False
                    print("MISMATCH", p, k, m, a, b)
    print("direct == recursion for all p^k<=128, all m:", ok)
    for (p, k) in [(2, 2), (2, 3), (3, 2), (2, 4), (5, 2), (3, 3)]:
        d = p**k
        print(f"\nd = {d} = {p}^{k}:  m : Omega_k(m) | Meshulam bound | (m-1)p^(k-1)")
        for m in range(1, d + 1):
            print(f"  {m:2d} : {omega_direct(p,k,m):3d} | {meshulam_zero_bound(d,m):3d} | {(m-1)*p**(k-1):3d}")

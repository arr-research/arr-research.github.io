"""Independent sanity check of the inverse-commutator Horn LP (Theorem 2.2 of 3M/37B)
against the closed formulas for d=3,4,5, and of the Kirwan-gauge identification.

kappa_d(F) = 1/2 min { sum p_j : p_1>=...>=p_{d-1}>=0, (alpha(p),beta(p),2*lambda) Horn-feasible }
alpha = (p_1..p_{d-1},0), beta = (0,-p_{d-1},...,-p_1), gamma = 2*lambda.
Horn inequality: sum_{k in K} gamma_k <= sum_{i in I} alpha_i + sum_{j in J} beta_j.
"""
from __future__ import annotations
import itertools, sys
from functools import lru_cache
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog

@lru_cache(None)
def horn_t(r: int, n: int):
    subsets = tuple(itertools.combinations(range(1, n + 1), r))
    out = []
    for I in subsets:
        for J in subsets:
            for K in subsets:
                if sum(I) + sum(J) != sum(K) + r * (r + 1) // 2:
                    continue
                ok = True
                for q in range(1, r):
                    for F, G, H in horn_t(q, r):
                        lhs = sum(I[f - 1] for f in F) + sum(J[g - 1] for g in G)
                        rhs = sum(K[h - 1] for h in H) + q * (q + 1) // 2
                        if lhs > rhs:
                            ok = False; break
                    if not ok: break
                if ok:
                    out.append((I, J, K))
    return tuple(out)

def horn_rows(d):
    """Return (A_ub, coeff-of-lambda rows): A_ub @ p >= B @ (2 lambda) i.e. -A p <= -B(2lambda)."""
    rows = []
    for r in range(1, d):
        for I, J, K in horn_t(r, d):
            a = np.zeros(d - 1)
            for i in I:
                if i < d: a[i - 1] += 1
            for j in J:
                if j > 1: a[d - j] -= 1   # beta_j = -p_{d+1-j}, index d-j (0-based) for p_{d+1-j}
            b = np.zeros(d)
            for k in K: b[k - 1] += 1
            rows.append((a, b))
    return rows

def kappa_lp(lam, rows=None):
    d = len(lam)
    if rows is None: rows = horn_rows(d)
    gam = 2 * np.asarray(lam, float)
    A = []; ub = []
    for a, b in rows:
        A.append(-a); ub.append(-(b @ gam))
    # ordering p_1>=p_2>=...>=p_{d-1}>=0
    for j in range(d - 2):
        e = np.zeros(d - 1); e[j] = -1; e[j + 1] = 1
        A.append(e); ub.append(0.0)
    res = linprog(np.ones(d - 1) * 0.5, A_ub=np.array(A), b_ub=np.array(ub), bounds=[(0, None)] * (d - 1), method="highs")
    assert res.status == 0, res.message
    return res.fun, res.x

def f3(l):
    return max(l[0] - l[1], l[1] - l[2])

def f4(l):
    l1, l2, l3, l4 = l
    return max(l1 - l3, l2 - l4, l1 - 2 * l2 - l3, l2 + 2 * l3 - l4)

def f5(l):
    l1, l2, l3, l4, l5 = l
    return max(2*l1-2*l2-l3+l5, -l1+l3+2*l4-2*l5, l1-l3-l4, l2+l3-l5, l2-2*l3-l4, l2+2*l3-l4,
               2*l1-l3+l5, -l1+l3-2*l5, l1+l2-l3, l3-l4-l5, l1+l3-l4, l2-l3-l5)

def rand_spec(d, rng):
    x = np.sort(rng.normal(size=d))[::-1]
    return x - x.mean()

if __name__ == "__main__":
    rng = np.random.default_rng(1)
    for d, f in [(3, f3), (4, f4), (5, f5)]:
        rows = horn_rows(d)
        counts = [len(horn_t(r, d)) for r in range(1, d)]
        err = 0.0; worst = None
        N = 400 if d < 5 else 300
        for _ in range(N):
            lam = rand_spec(d, rng)
            v, _p = kappa_lp(lam, rows)
            e = abs(v - f(lam))
            if e > err: err, worst = e, lam
        print(f"d={d}: Horn triple counts {counts} (total {sum(counts)}); max |LP - formula| over {N} spectra = {err:.2e}")
    # specific checks
    rows4 = horn_rows(4)
    print("kappa_4(3,-1,-1,-1) =", kappa_lp([3, -1, -1, -1], rows4)[0], "(paper: 6)")
    print("kappa_4(5,1,-3,-3) =", kappa_lp([5, 1, -3, -3], rows4)[0], "(paper 7N: 8)")
    print("kappa_4(-1,1/3,1/3,1/3)=", kappa_lp([1/3, 1/3, 1/3, -1], rows4)[0], "(paper 1D: 2)")
    rows5 = horn_rows(5)
    print("kappa_5(4,-1,-1,-1,-1) =", kappa_lp([4, -1, -1, -1, -1], rows5)[0], "(paper: 10)")
    # one-spike formula check in d=5: spectrum (6,-3,-2,-1,0) -> 3+4+3 = 10
    print("kappa_5(6,0,-1,-2,-3) =", kappa_lp([6, 0, -1, -2, -3], rows5)[0], "(7N one-spike: 10)")
    # zero padding non-invariance (5Q Remark 3.3): (25,18,18,-10,-17,-17,-17)/7 cost 74/7 in d=7, 73/7 in d=8
    rows7 = horn_rows(7); print("triples d=7:", sum(len(horn_t(r,7)) for r in range(1,7)))
    lam7 = np.array([25, 18, 18, -10, -17, -17, -17]) / 7
    v7, _ = kappa_lp(lam7, rows7)
    print("kappa_7 =", v7, "~", v7 * 7, "/7 (paper: 74/7)")
    rows8 = horn_rows(8); print("triples d=8:", sum(len(horn_t(r,8)) for r in range(1,8)))
    lam8 = np.array([25, 18, 18, 0, -10, -17, -17, -17]) / 7
    v8, _ = kappa_lp(lam8, rows8)
    print("kappa_8(padded) =", v8, "~", v8 * 7, "/7 (paper: 73/7)")
    # 5Q Cor 4.2: (5,1,1,1,-2,-2,-2,-2) cost 13
    v, p = kappa_lp([5, 1, 1, 1, -2, -2, -2, -2], rows8)
    print("kappa_8(5,1,1,1,-2^4) =", v, "p =", np.round(p, 6), "(paper: 13, rank 5)")
    # Kirwan-gauge check: sample random C with ||C||_HS=1, mu = spec(CC*-C*C); need kappa_d(mu) <= 1, sup -> 1
    for d, f in [(3, f3), (4, f4), (5, f5)]:
        mx = 0.0
        for _ in range(20000):
            C = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
            C /= np.linalg.norm(C)
            mu = np.sort(np.linalg.eigvalsh(C @ C.conj().T - C.conj().T @ C))[::-1]
            mx = max(mx, f(mu))
        # also try the known extremal C (one-spike shift): d=3: C = e_1 e_2^* -> mu=(1,-1,0), kappa=1
        print(f"d={d}: max over random unit C of kappa_d(spec(CC*-C*C)) = {mx:.4f} (must be <= 1; sup should be 1)")

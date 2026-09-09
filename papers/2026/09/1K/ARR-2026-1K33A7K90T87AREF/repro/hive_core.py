"""Hive LP for kappa_d(lambda) = min{ sum s : (s, -s^rev, lambda) Horn-feasible } with dual extraction.
Labeling (calibrated in scratch_A_inverse_commutator/hive_lp.py, A5): edge (0,0)->(n,0) carries s (forward),
edge (n,0)->(0,n) carries -s^rev (forward), edge (0,0)->(0,n) carries lambda (forward).
Sparse build; returns gradient d kappa / d lambda_k from the equality-row marginals.
"""
from __future__ import annotations
import numpy as np
from fractions import Fraction as Q
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, lil_matrix

def hive_index(n):
    idx = {}
    for i in range(n + 1):
        for j in range(n + 1 - i):
            idx[(i, j)] = len(idx)
    return idx

def rhombi(n):
    R = []
    ok = lambda p: p[0] >= 0 and p[1] >= 0 and p[0] + p[1] <= n
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j > n - 1: continue
            t1 = [((i + 1, j), (i, j + 1), (i, j), (i + 1, j + 1))]
            t2 = [((i, j), (i + 1, j), (i, j + 1), (i + 1, j - 1))]
            t3 = [((i, j), (i, j + 1), (i + 1, j), (i - 1, j + 1))]
            for r in t1 + t2 + t3:
                if all(ok(p) for p in r): R.append(r)
    return R

class HiveLP:
    def __init__(self, n, rank_cap=None):
        self.n = n
        idx = hive_index(n); self.idx = idx; H = len(idx); self.H = H; nv = H + n; self.nv = nv
        self.R = rhombi(n)
        Aub = lil_matrix((len(self.R) + n - 1, nv))
        for r, (o1, o2, a1, a2) in enumerate(self.R):
            Aub[r, idx[o1]] -= 1; Aub[r, idx[o2]] -= 1; Aub[r, idx[a1]] += 1; Aub[r, idx[a2]] += 1
        for k in range(n - 1):
            Aub[len(self.R) + k, H + k] = -1; Aub[len(self.R) + k, H + k + 1] = 1
        self.Aub = csr_matrix(Aub); self.bub = np.zeros(Aub.shape[0])
        edgesA = [((i - 1, 0), (i, 0)) for i in range(1, n + 1)]
        edgesB = [((n - k + 1, k - 1), (n - k, k)) for k in range(1, n + 1)]
        edgesC = [((0, j - 1), (0, j)) for j in range(1, n + 1)]
        rows = []  # (dict col->coef, kind, k)
        rows.append(({idx[(0, 0)]: 1.0}, 'zero', None))
        for t, (p, q) in enumerate(edgesA):   # h(q)-h(p) = s_t
            rows.append(({idx[q]: 1.0, idx[p]: -1.0, H + t: -1.0}, 'zero', None))
        for t, (p, q) in enumerate(edgesB):   # h(q)-h(p) = -s_{n-1-t}
            rows.append(({idx[q]: 1.0, idx[p]: -1.0, H + (n - 1 - t): 1.0}, 'zero', None))
        self.lam_rows = []
        for t, (p, q) in enumerate(edgesC):   # h(q)-h(p) = lambda_t
            self.lam_rows.append(len(rows))
            rows.append(({idx[q]: 1.0, idx[p]: -1.0}, 'lam', t))
        Aeq = lil_matrix((len(rows), nv))
        for r, (dct, _, _) in enumerate(rows):
            for c, v in dct.items(): Aeq[r, c] += v
        self.Aeq = csr_matrix(Aeq); self.neq = len(rows)
        self.c = np.zeros(nv); self.c[H:] = 1.0
        self.rank_cap = rank_cap
        self.bounds = [(None, None)] * H + [(0, None)] * n
        if rank_cap is not None:
            for k in range(rank_cap, n): self.bounds[H + k] = (0, 0)

    def solve(self, lam):
        lam = np.asarray(lam, float)
        beq = np.zeros(self.neq)
        for t, r in enumerate(self.lam_rows): beq[r] = lam[t]
        res = linprog(self.c, A_ub=self.Aub, b_ub=self.bub, A_eq=self.Aeq, b_eq=beq, bounds=self.bounds, method='highs')
        if res.status != 0: return None
        grad = np.array([res.eqlin.marginals[r] for r in self.lam_rows])
        return dict(val=res.fun, s=res.x[self.H:], h=res.x[:self.H], grad=grad,
                    y_ub=-res.ineqlin.marginals, y_eq=res.eqlin.marginals, res=res)

def spec_mn2(a, b, pad=0):
    """lambda = (a_1..a_m, 0^pad, -b_2, -b_1)."""
    return np.array(list(a) + [0.0] * pad + [-b[1], -b[0]])

def rand_mn2(m, rng, law='exp'):
    if law == 'exp':
        a = np.sort(rng.exponential(size=m))[::-1]
        b = np.sort(rng.exponential(size=2))[::-1]
    elif law == 'unif':
        a = np.sort(rng.uniform(size=m))[::-1]
        b = np.sort(rng.uniform(size=2))[::-1]
    elif law == 'sq':  # squared normals -> more spread
        a = np.sort(rng.normal(size=m) ** 2)[::-1]
        b = np.sort(rng.normal(size=2) ** 2)[::-1]
    a = a / a.sum(); b = b / b.sum()
    return a, b

def canon_form(grad, m, pad):
    """grad: d kappa/d lambda_k. Return canonical (alpha_1..alpha_m, beta_1) with beta_2 normalized to 0,
    using sum a = sum b. kappa = sum alpha_j a_j + beta_1 b_1 (+ 0*b_2)."""
    d = m + pad + 2
    alpha = grad[:m].copy(); beta2 = -grad[d - 2]; beta1 = -grad[d - 1]
    # kappa = alpha.a + beta1 b1 + beta2 b2 ; subtract t=beta2: alpha -= beta2, beta += beta2 ... careful sign:
    # sum alpha_j a_j + beta1 b1 + beta2 b2 = sum (alpha_j - t) a_j + (beta1 + t) b1 + (beta2 + t) b2 with t = -beta2
    t = -beta2
    return np.concatenate([alpha - t, [beta1 + t]])

def rat(x, den=720):
    return Q(x).limit_denominator(den)

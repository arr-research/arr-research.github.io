"""Independent (reviewer) implementations: Fulton/Horn recursion T^n_r, LR coefficients via Jacobi-Trudi + Pieri,
Horn LP for kappa_d, hive LP for kappa_d.  Written from scratch for the review of report_A3_inertia_m3."""
import itertools, pickle, os, sys
from functools import lru_cache
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, csr_matrix

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "T_cache.pkl")
_T = {}


def T(r, n):
    """Fulton's recursive description: (I,J,K) in T^n_r iff sum I + sum J = sum K + r(r+1)/2 and for all p<r, (F,G,H) in T^r_p:
    sum_{f in F} i_f + sum_{g in G} j_g <= sum_{h in H} k_h + p(p+1)/2."""
    key = (r, n)
    if key in _T: return _T[key]
    subs = list(itertools.combinations(range(1, n + 1), r))
    bysum = {}
    for K in subs: bysum.setdefault(sum(K), []).append(K)
    inner = [(p, T(p, r)) for p in range(1, r)]
    out = []
    for I in subs:
        for J in subs:
            target = sum(I) + sum(J) - r * (r + 1) // 2
            for K in bysum.get(target, []):
                good = True
                for p, Tp in inner:
                    for F, G, H in Tp:
                        if sum(I[f - 1] for f in F) + sum(J[g - 1] for g in G) > sum(K[h - 1] for h in H) + p * (p + 1) // 2:
                            good = False; break
                    if not good: break
                if good: out.append((I, J, K))
    _T[key] = tuple(out)
    # Fresh local audit: memory-only recursion; no pickle I/O.
    return _T[key]

def all_T(n):
    return [t for r in range(1, n) for t in T(r, n)]

# ---------------- LR via Jacobi-Trudi + Pieri ----------------
def hstrips(lam, k):
    """All partitions nu with nu/lam a horizontal strip of size k (nu_{i+1} <= lam_i)."""
    lam = list(lam) + [0]
    n = len(lam)
    out = []
    def rec(i, rem, cur):
        if i == n:
            if rem == 0: out.append(tuple(x for x in cur if x > 0))
            return
        for add in range(0, rem + 1):
            nu_i = lam[i] + add
            if i > 0 and nu_i > lam[i - 1]: break
            rec(i + 1, rem - add, cur + [nu_i])
    rec(0, k, [])
    return out

def perm_sign(p):
    s = 1; p = list(p)
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s

@lru_cache(None)
def schur_product(lam, mu):
    """dict nu -> c^nu_{lam mu}, via s_mu = det(h_{mu_i - i + j}) and the Pieri rule."""
    lam = tuple(x for x in lam if x > 0); mu = tuple(x for x in mu if x > 0)
    l = len(mu)
    total = {}
    for sigma in itertools.permutations(range(l)):
        ks = [mu[i] - i + sigma[i] for i in range(l)]
        if any(k < 0 for k in ks): continue
        sg = perm_sign(sigma)
        cur = {lam: 1}
        for k in ks:
            if k == 0: continue
            nxt = {}
            for p, c in cur.items():
                for nu in hstrips(p, k): nxt[nu] = nxt.get(nu, 0) + c
            cur = nxt
        for nu, c in cur.items(): total[nu] = total.get(nu, 0) + sg * c
    return {nu: c for nu, c in total.items() if c != 0}

def lr_own(lam, mu, nu):
    nu = tuple(x for x in nu if x > 0)
    return schur_product(tuple(lam), tuple(mu)).get(nu, 0)

def part(I):
    r = len(I); I = sorted(I)
    return tuple(I[r - 1 - t] - (r - t) for t in range(r))

# ---------------- Horn LP for kappa_d ----------------
def horn_rows(d):
    rows = []
    for I, J, K in all_T(d):
        a = np.zeros(d - 1)
        for i in I:
            if i < d: a[i - 1] += 1
        for j in J:
            if j > 1: a[d - j] -= 1          # -s_{d+1-j}, 0-based index d-j
        b = np.zeros(d)
        for k in K: b[k - 1] += 1
        rows.append((a, b, (I, J, K)))
    return rows

def kappa_horn(lam, rows, tight=True, extra_eq=None, cap=None, objective=None):
    d = len(lam); lam = np.asarray(lam, float)
    A = np.array([-a for a, b, _ in rows]); ub = np.array([-(b @ lam) for a, b, _ in rows])
    O = np.zeros((d - 2, d - 1))
    for j in range(d - 2): O[j, j] = -1; O[j, j + 1] = 1
    A = np.vstack([A, O]); ub = np.concatenate([ub, np.zeros(d - 2)])
    bounds = [(0, None)] * (d - 1)
    if cap is not None:
        for k in range(cap, d - 1): bounds[k] = (0, 0)
    c = np.ones(d - 1) if objective is None else np.asarray(objective, float)
    opts = dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10) if tight else {}
    kw = {}
    if extra_eq is not None: kw = dict(A_eq=extra_eq[0], b_eq=extra_eq[1])
    res = linprog(c, A_ub=A, b_ub=ub, bounds=bounds, method='highs', options=opts, **kw)
    return res

# ---------------- hive LP ----------------
class Hive:
    """Hive of size n on points (i,j), i,j>=0, i+j<=n.  Rhombus inequalities: sum(obtuse) >= sum(acute) for every unit rhombus
    (the shared short diagonal joins the two obtuse vertices).
    Boundary: h(i,0)-h(i-1,0) = alpha_i; h(n-k,k)-h(n-k+1,k-1) = beta_k; h(0,j)-h(0,j-1) = gamma_j; h(0,0)=0.
    alpha = (s_1..s_{d-1}, 0), beta = (0, -s_{d-1}, ..., -s_1), gamma = lambda.  Variables: h (H), s (n)."""
    def __init__(self, n):
        self.n = n
        pts = [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]
        idx = {p: k for k, p in enumerate(pts)}; self.idx = idx; H = len(pts); self.H = H
        nv = H + n; self.nv = nv
        rh = []
        inside = lambda p: p[0] >= 0 and p[1] >= 0 and p[0] + p[1] <= n
        for i in range(n + 1):
            for j in range(n + 1):
                if i + j > n: continue
                cand = [(((i, j), (i + 1, j)), ((i + 1, j - 1), (i, j + 1))),
                        (((i, j), (i, j + 1)), ((i - 1, j + 1), (i + 1, j))),
                        (((i, j), (i + 1, j - 1)), ((i, j - 1), (i + 1, j)))]
                for ob, ac in cand:
                    if all(inside(p) for p in ob + ac): rh.append((ob, ac))
        self.rh = rh
        A = lil_matrix((len(rh) + (n - 1), nv))
        for r, (ob, ac) in enumerate(rh):
            for p in ob: A[r, idx[p]] -= 1
            for p in ac: A[r, idx[p]] += 1
        for k in range(n - 1):     # s_{k+2} <= s_{k+1}
            A[len(rh) + k, H + k] = -1; A[len(rh) + k, H + k + 1] = 1
        self.A = csr_matrix(A); self.bub = np.zeros(A.shape[0])
        eq = []
        eq.append(({idx[(0, 0)]: 1.0}, None))
        for i in range(1, n + 1):       # alpha_i = s_i (s_n = 0)
            row = {idx[(i, 0)]: 1.0, idx[(i - 1, 0)]: -1.0}
            if i < n: row[H + i - 1] = -1.0
            eq.append((row, None))
        for k in range(1, n + 1):       # beta_k = -s_{n+1-k}, beta_1 = 0
            row = {idx[(n - k, k)]: 1.0, idx[(n - k + 1, k - 1)]: -1.0}
            if k > 1: row[H + (n + 1 - k) - 1] = 1.0
            eq.append((row, None))
        self.lam_rows = []
        for j in range(1, n + 1):
            self.lam_rows.append(len(eq)); eq.append(({idx[(0, j)]: 1.0, idx[(0, j - 1)]: -1.0}, j - 1))
        E = lil_matrix((len(eq), nv))
        for r, (row, _) in enumerate(eq):
            for c, v in row.items(): E[r, c] += v
        self.E = csr_matrix(E); self.neq = len(eq)
        self.bounds = [(None, None)] * H + [(0, None)] * n
        self.c = np.zeros(nv); self.c[H:] = 1.0

    def solve(self, lam, tight=True, cap=None, objective=None):
        beq = np.zeros(self.neq)
        for t, r in enumerate(self.lam_rows): beq[r] = lam[t]
        bounds = list(self.bounds)
        if cap is not None:
            for k in range(cap, self.n): bounds[self.H + k] = (0, 0)
        c = self.c if objective is None else objective
        opts = dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10) if tight else {}
        res = linprog(c, A_ub=self.A, b_ub=self.bub, A_eq=self.E, b_eq=beq, bounds=bounds, method='highs', options=opts)
        if res.status != 0: return None
        return dict(val=res.fun, s=res.x[self.H:], grad=np.array([res.eqlin.marginals[r] for r in self.lam_rows]), res=res)

def spec(a, b, z):
    return np.array(list(a) + [0.0] * z + [-b[2], -b[1], -b[0]])

def rand_point(m, rng, law=0):
    if law == 0: a = rng.exponential(size=m); b = rng.exponential(size=3)
    elif law == 1: a = rng.uniform(size=m); b = rng.uniform(size=3)
    elif law == 2: a = rng.normal(size=m) ** 2; b = rng.normal(size=3) ** 2
    elif law == 3:  # tie-heavy: few distinct values
        vals = rng.exponential(size=3); a = rng.choice(vals, size=m); b = rng.choice(vals, size=3) * rng.uniform(0.5, 1.5, size=3)
    elif law == 4:  # dominant a_1
        a = rng.exponential(size=m); a[0] *= 10; b = rng.exponential(size=3)
    else:            # flat b
        a = rng.exponential(size=m); b = np.ones(3) + 0.01 * rng.uniform(size=3)
    a = np.sort(a)[::-1]; b = np.sort(b)[::-1]
    return a / a.sum(), b / b.sum()

def form_val(g, a, b):
    m = len(a); return float(np.dot(g[:m], a) + g[m] * b[0] + g[m + 1] * b[1])

if __name__ == "__main__":
    import time
    for n in range(2, 10):
        t0 = time.time(); tot = sum(len(T(r, n)) for r in range(1, n)); print(f"n={n}: |T^n| = {tot}  ({time.time()-t0:.1f}s)", flush=True)

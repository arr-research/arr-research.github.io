"""Reviewer's independent Horn machinery.
T^d_r by Fulton/Horn recursion (vectorised numpy), NOT by LR; own LR counter only for spot checks of tiles.
kappa_d(lambda) = min sum_{t<d} s_t, s_1>=...>=s_{d-1}>=0, all (I,J,K) in T^d_r:
   sum_{i in I, i<d} s_i - sum_{j in J, j>1} s_{d+1-j} >= sum_{k in K} lambda_k.
"""
import itertools, os, numpy as np
from functools import lru_cache
from scipy.optimize import linprog
from scipy.sparse import csr_matrix

HERE = os.path.dirname(os.path.abspath(__file__))
_TCACHE = {}

def horn_T(d):
    """dict r -> np.array of shape (N, 3, r) of 1-based index triples (I,J,K) in T^d_r."""
    if d in _TCACHE: return _TCACHE[d]
    fn = os.path.join(HERE, f"myT_{d}.pkl")
    out = {}
    for r in range(1, d):
        subs = np.array(list(itertools.combinations(range(1, d + 1), r)), dtype=np.int64)  # (S, r)
        sums = subs.sum(1)
        bysum = {}
        for idx, sm in enumerate(sums): bysum.setdefault(int(sm), []).append(idx)
        cand = []
        target_off = r * (r + 1) // 2
        for iI in range(len(subs)):
            for iJ in range(len(subs)):
                tk = int(sums[iI] + sums[iJ]) - target_off
                for iK in bysum.get(tk, []):
                    cand.append((iI, iJ, iK))
        cand = np.array(cand, dtype=np.int64).reshape(-1, 3)
        I = subs[cand[:, 0]]; J = subs[cand[:, 1]]; K = subs[cand[:, 2]]
        ok = np.ones(len(cand), bool)
        if r >= 2:
            Tr = horn_T(r)
            for p in range(1, r):
                for (F, G, H) in Tr[p]:
                    lhs = I[:, F - 1].sum(1) + J[:, G - 1].sum(1) - K[:, H - 1].sum(1)
                    ok &= lhs <= p * (p + 1) // 2
        arr = np.stack([I[ok], J[ok], K[ok]], axis=1)  # (N,3,r)
        out[r] = arr
    _TCACHE[d] = out
    # ASTRA work copy: memory-only regenerated cache
    return out

def part(I):
    I = list(I); r = len(I)
    return tuple(I[r - 1 - t] - (r - t) for t in range(r))

def strip(p):
    p = list(p)
    while p and p[-1] == 0: p.pop()
    return tuple(p)

@lru_cache(None)
def lr_coeff(lam, mu, nu):
    """Own LR counter: number of SSYT of shape nu/lam, content mu, whose reverse reading word (rows top to bottom,
    each row right to left) is a lattice word.  Cells are filled in reading order."""
    lam, mu, nu = strip(lam), strip(mu), strip(nu)
    if sum(lam) + sum(mu) != sum(nu): return 0
    n = len(nu); lam = lam + (0,) * (n - len(lam))
    if any(lam[i] > nu[i] for i in range(n)): return 0
    if not mu: return 1 if strip(lam) == nu else 0
    k = len(mu)
    cells = [(i, c) for i in range(n) for c in range(nu[i] - 1, lam[i] - 1, -1)]
    fill = {}
    cnt = [0] * (k + 1)
    total = 0
    def rec(pos):
        nonlocal total
        if pos == len(cells): total += 1; return
        i, c = cells[pos]
        hi = fill.get((i, c + 1), k)                      # row weakly increasing (right neighbour already filled)
        lo = fill[(i - 1, c)] + 1 if (i - 1, c) in fill else 1   # column strict (cell above already filled)
        for v in range(lo, hi + 1):
            if cnt[v] + 1 > mu[v - 1]: continue
            if v > 1 and cnt[v] + 1 > cnt[v - 1]: continue   # lattice condition
            fill[(i, c)] = v; cnt[v] += 1
            rec(pos + 1)
            cnt[v] -= 1; del fill[(i, c)]
    rec(0)
    return total

class HornLP:
    def __init__(self, d):
        self.d = d; T = horn_T(d)
        rows = []; lam_rows = []; info = []
        for r in range(1, d):
            for (I, J, K) in T[r]:
                a = np.zeros(d - 1)
                for i in I:
                    if i < d: a[i - 1] += 1
                for j in J:
                    if j > 1: a[d - j] -= 1
                bb = np.zeros(d)
                for kk in K: bb[kk - 1] += 1
                lI, lJ, lK = strip(part(I)), strip(part(J)), strip(part(K))
                rows.append(a); lam_rows.append(bb)
                info.append(dict(I=tuple(int(x) for x in I), J=tuple(int(x) for x in J), K=tuple(int(x) for x in K),
                                 lI=lI, lJ=lJ, lK=lK, box=min(sum(lI), sum(lJ)), r=r))
        self.A = np.array(rows); self.B = np.array(lam_rows); self.info = info
        self.box = np.array([x['box'] for x in info])
        ordrows = np.zeros((d - 2, d - 1))
        for j in range(d - 2): ordrows[j, j] = -1; ordrows[j, j + 1] = 1
        self.ord = ordrows
        self.ntri = len(info)

    def solve(self, lam, Bmax=None, want_dual=False, tol=None):
        lam = np.asarray(lam, float); d = self.d
        sel = np.ones(self.ntri, bool) if Bmax is None else (self.box <= Bmax)
        A = np.vstack([-self.A[sel], self.ord]); ub = np.concatenate([-(self.B[sel] @ lam), np.zeros(d - 2)])
        opts = {} if tol is None else dict(primal_feasibility_tolerance=tol, dual_feasibility_tolerance=tol)
        res = linprog(np.ones(d - 1), A_ub=csr_matrix(A), b_ub=ub, bounds=[(0, None)] * (d - 1), method='highs', options=opts)
        assert res.status == 0, res.message
        out = dict(val=res.fun, s=res.x)
        if want_dual:
            y = -res.ineqlin.marginals[:sel.sum()]
            idx = np.nonzero(sel)[0]
            out['active'] = [(int(idx[k]), float(y[k])) for k in range(len(y)) if y[k] > 1e-9]
            out['grad'] = (y @ self.B[sel])
        return out

    def min_coord_on_optimal_face(self, lam, t, kap, slack=1e-9):
        """min s_t (1-based) subject to Horn feasibility and sum s <= kap + slack."""
        lam = np.asarray(lam, float); d = self.d
        A = np.vstack([-self.A, self.ord, np.ones((1, d - 1))]); ub = np.concatenate([-(self.B @ lam), np.zeros(d - 2), [kap + slack]])
        c = np.zeros(d - 1); c[t - 1] = 1
        res = linprog(c, A_ub=csr_matrix(A), b_ub=ub, bounds=[(0, None)] * (d - 1), method='highs')
        assert res.status == 0, res.message
        return res.fun

def spec(a, b, z=0):
    return np.array(list(a) + [0.0] * z + [-x for x in b[::-1]], float)

def kappa4(l):
    l1, l2, l3, l4 = l
    return max(l1 - l3, l2 - l4, l1 - 2 * l2 - l3, l2 + 2 * l3 - l4)


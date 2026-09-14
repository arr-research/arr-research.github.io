"""Explicit Horn LP for kappa_d (d <= 9) over Fulton's T^d_r lists (pickles horn_d{d}.pkl from cycle2/work/A3_inertia_m3),
with a filter on the 'box count' of a triple: box(I,J,K) = min(|lambda(I)|, |lambda(J)|) (0 for Lidskii-Wielandt / Weyl
triples). kappa restricted to triples with box <= B is a lower bound that increases with B; B_min = least B attaining kappa.
s-notation (2.2): sum_{i in I, i<d} s_i - sum_{j in J, j>1} s_{d+1-j} >= sum_{k in K} lambda_k."""
import pickle, os, numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix
from lr import part, strip

PKL = os.path.dirname(os.path.abspath(__file__))  # REPRO: pickles horn_d6..9.pkl copied from cycle2/work/A3_inertia_m3 into this directory

def is_rect(p):
    p = strip(p); return len(set(p)) <= 1

class HornLP:
    def __init__(self, d):
        self.d = d
        fn = os.path.join(PKL, f"horn_d{d}.pkl")
        if os.path.exists(fn): T = pickle.load(open(fn, "rb"))
        else:
            from check_horn_lp import horn_t
            T = {r: horn_t(r, d) for r in range(1, d)}
        self.triples = [t for r in range(1, d) for t in T[r]]
        rows = []; lamrows = []; info = []
        for (I, J, K) in self.triples:
            a = np.zeros(d - 1)
            for i in I:
                if i < d: a[i - 1] += 1
            for j in J:
                if j > 1: a[d - j] -= 1
            bb = np.zeros(d)
            for k in K: bb[k - 1] += 1
            lI, lJ, lK = strip(part(I)), strip(part(J)), strip(part(K))
            rows.append(a); lamrows.append(bb)
            info.append(dict(lI=lI, lJ=lJ, lK=lK, box=min(sum(lI), sum(lJ)), nJ=sum(lJ), nI=sum(lI), rectK=is_rect(lK), r=len(I)))
        self.A = np.array(rows); self.B = np.array(lamrows); self.info = info
        self.box = np.array([x['box'] for x in info])
        ordrows = []
        for j in range(d - 2):
            e = np.zeros(d - 1); e[j] = -1; e[j + 1] = 1; ordrows.append(e)
        self.ord = np.array(ordrows)

    def solve(self, lam, Bmax=None, want_dual=False):
        lam = np.asarray(lam, float)
        sel = np.ones(len(self.triples), bool) if Bmax is None else (self.box <= Bmax)
        A = np.vstack([-self.A[sel], self.ord]); ub = np.concatenate([-(self.B[sel] @ lam), np.zeros(self.d - 2)])
        res = linprog(np.ones(self.d - 1), A_ub=csr_matrix(A), b_ub=ub, bounds=[(0, None)] * (self.d - 1), method='highs')
        assert res.status == 0, res.message
        out = dict(val=res.fun, s=res.x)
        if want_dual:
            y = -res.ineqlin.marginals[:sel.sum()]      # multipliers >= 0 on the selected Horn rows
            idx = np.nonzero(sel)[0]
            out['active'] = [(int(idx[k]), float(y[k])) for k in range(len(y)) if y[k] > 1e-9]
        return out

    def bmin(self, lam, tol=1e-9):
        full = self.solve(lam)['val']
        for B in range(0, 10):
            v = self.solve(lam, Bmax=B)['val']
            if v >= full - tol: return B, full
        return None, full

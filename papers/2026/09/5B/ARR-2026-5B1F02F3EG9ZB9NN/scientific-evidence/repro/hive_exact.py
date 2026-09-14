"""hive_exact.py -- exact rational primal/dual certificates for the hive LP value of

    kappa_d(lambda) = min { sum_i s_i : s_1 >= ... >= s_d >= 0, (s, -s^rev, lambda) Horn-feasible }

Horn feasibility of (s, -s^rev, lambda) <=> existence of an order-d hive (Knutson-Tao) with boundary
increments: edge (0,0)->(d,0) carries s_1..s_d, edge (d,0)->(0,d) carries -s_d..-s_1, edge (0,0)->(0,d)
carries lambda_1..lambda_d (labeling calibrated against the explicit Horn LP; see calibrate()).
Rhombus inequality: h(o1)+h(o2) >= h(a1)+h(a2) for every unit rhombus (obtuse vertices o, acute a).

Pipeline: float LP (HiGHS dual simplex) -> rationalize primal (s, interior h) and dual multipliers
(limit_denominator) -> verify EXACTLY with Fractions -> emit certificate dict.  If rationalization
fails, an exact re-solve on the float support is attempted (solve_support_*).
"""
from __future__ import annotations
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, lil_matrix

# ---------------------------------------------------------------- lattice ------------------------
def hive_points(n):
    return [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]

def hive_index(n):
    return {p: k for k, p in enumerate(hive_points(n))}

def rhombi(n):
    """All unit rhombi of the order-n hive triangle as (o1,o2,a1,a2): obtuse pair, acute pair.
    Enumerated by (up-triangle (i,j),(i+1,j),(i,j+1); side)."""
    R = []
    ok = lambda p: p[0] >= 0 and p[1] >= 0 and p[0] + p[1] <= n
    for i in range(n):
        for j in range(n - i):
            cand = [((i + 1, j), (i, j + 1), (i, j), (i + 1, j + 1)),
                    ((i, j), (i + 1, j), (i, j + 1), (i + 1, j - 1)),
                    ((i, j), (i, j + 1), (i + 1, j), (i - 1, j + 1))]
            for r in cand:
                if all(ok(p) for p in r):
                    R.append(r)
    return R

def boundary_equations(n):
    """List of (dict var->coef, rhs_kind) with vars ('h',(i,j)) or ('s',k) (1-based); rhs_kind: ('zero',) or ('lam', j)."""
    eqs = [({('h', (0, 0)): 1}, ('zero',))]
    for i in range(1, n + 1):      # edge A: h(i,0)-h(i-1,0) = s_i
        eqs.append(({('h', (i, 0)): 1, ('h', (i - 1, 0)): -1, ('s', i): -1}, ('zero',)))
    for k in range(1, n + 1):      # edge B: h(n-k,k)-h(n-k+1,k-1) = -s_{n+1-k}
        eqs.append(({('h', (n - k, k)): 1, ('h', (n - k + 1, k - 1)): -1, ('s', n + 1 - k): 1}, ('zero',)))
    for j in range(1, n + 1):      # edge C: h(0,j)-h(0,j-1) = lambda_j
        eqs.append(({('h', (0, j)): 1, ('h', (0, j - 1)): -1}, ('lam', j)))
    return eqs

# ---------------------------------------------------------------- LP model -----------------------
class HiveLP:
    def __init__(self, n):
        self.n = n
        self.idx = hive_index(n); self.H = len(self.idx); self.nv = self.H + n
        self.R = rhombi(n)
        self.eqs = boundary_equations(n)
        nv = self.nv
        A = lil_matrix((len(self.R) + (n - 1), nv))
        for r, (o1, o2, a1, a2) in enumerate(self.R):
            A[r, self.idx[a1]] += 1; A[r, self.idx[a2]] += 1
            A[r, self.idx[o1]] -= 1; A[r, self.idx[o2]] -= 1
        for k in range(n - 1):     # ordering s_{k+2} - s_{k+1} <= 0
            A[len(self.R) + k, self.H + k] = -1; A[len(self.R) + k, self.H + k + 1] = 1
        self.Aub = csr_matrix(A)
        E = lil_matrix((len(self.eqs), nv))
        for r, (coefs, kind) in enumerate(self.eqs):
            for v, c in coefs.items():
                E[r, self.var(v)] += c
        self.Aeq = csr_matrix(E)
        self.c = np.zeros(nv); self.c[self.H:] = 1
        self.bounds = [(None, None)] * self.H + [(0, None)] * n

    def var(self, v):
        return self.idx[v[1]] if v[0] == 'h' else self.H + v[1] - 1

    def beq(self, lam):
        return np.array([0.0 if kind[0] == 'zero' else float(lam[kind[1] - 1]) for _, kind in self.eqs])

    def solve_float(self, lam):
        res = linprog(self.c, A_ub=self.Aub, b_ub=np.zeros(self.Aub.shape[0]), A_eq=self.Aeq,
                      b_eq=self.beq(lam), bounds=self.bounds, method='highs-ds')
        if res.status != 0:
            raise RuntimeError(res.message)
        return res

    # ------------------------------------------------------------ exact verification -------------
    def primal_from_s_and_interior(self, lam, s, hint):
        """Build exact h: boundary from s and lam (exact), interior from hint (dict point->Fraction)."""
        n = self.n; h = {}
        h[(0, 0)] = Q(0)
        for i in range(1, n + 1): h[(i, 0)] = h[(i - 1, 0)] + s[i - 1]
        for k in range(1, n + 1): h[(n - k, k)] = h[(n - k + 1, k - 1)] - s[n - k]
        hc = Q(0)
        for j in range(1, n + 1):
            hc += lam[j - 1]
            if (0, j) in h:
                if h[(0, j)] != hc: return None    # inconsistent (sum lam != 0)
            else:
                h[(0, j)] = hc
        for p in self.idx:
            if p not in h: h[p] = hint[p]
        return h

    def check_primal(self, lam, s, h):
        """Exact feasibility: returns (ok, cost)."""
        n = self.n
        if any(x < 0 for x in s): return False, None
        if any(s[k] < s[k + 1] for k in range(n - 1)): return False, None
        if h[(0, 0)] != 0: return False, None
        for i in range(1, n + 1):
            if h[(i, 0)] - h[(i - 1, 0)] != s[i - 1]: return False, None
        for k in range(1, n + 1):
            if h[(n - k, k)] - h[(n - k + 1, k - 1)] != -s[n - k]: return False, None
        for j in range(1, n + 1):
            if h[(0, j)] - h[(0, j - 1)] != lam[j - 1]: return False, None
        for o1, o2, a1, a2 in self.R:
            if h[o1] + h[o2] < h[a1] + h[a2]: return False, None
        return True, sum(s)

    def check_dual(self, lam, y, z, mu):
        """y: dict rhombus-index->Q (>=0), z: list of n-1 Q (>=0) for ordering rows, mu: list Q for eqs.
        Stationarity: c + G^T y + D^T z + E^T mu = residual; residual_h must be 0, residual_s >= 0.
        Returns (ok, value) with value = -mu . b(lam)."""
        n = self.n
        if any(v < 0 for v in y.values()) or any(v < 0 for v in z): return False, None
        res = {p: Q(0) for p in self.idx}; rs = [Q(1)] * n
        for r, v in y.items():
            if v == 0: continue
            o1, o2, a1, a2 = self.R[r]
            res[a1] += v; res[a2] += v; res[o1] -= v; res[o2] -= v
        for k in range(n - 1):
            rs[k] -= z[k]; rs[k + 1] += z[k]
        for r, (coefs, kind) in enumerate(self.eqs):
            m = mu[r]
            if m == 0: continue
            for v, c in coefs.items():
                if v[0] == 'h': res[v[1]] += m * c
                else: rs[v[1] - 1] += m * c
        if any(v != 0 for v in res.values()): return False, None
        if any(v < 0 for v in rs): return False, None
        val = Q(0)
        for r, (coefs, kind) in enumerate(self.eqs):
            if kind[0] == 'lam': val -= mu[r] * lam[kind[1] - 1]
        return True, val

    # ------------------------------------------------------------ rationalize + certify ----------
    def certify(self, lam, want_dual=True, dens=(10**3, 10**4, 10**5, 10**6, 10**7)):
        """lam: list of Fractions (sum 0, decreasing). Returns dict with exact primal (and dual)."""
        lam = [Q(x) for x in lam]
        assert sum(lam) == 0
        n = self.n
        res = self.solve_float(lam)
        x = res.x
        out = {'d': n, 'lam': lam, 'float': float(res.fun)}
        primal = None
        for den in dens:
            s = [Q(float(v)).limit_denominator(den) for v in x[self.H:]]
            hint = {p: Q(float(x[self.idx[p]])).limit_denominator(den) for p in self.idx}
            h = self.primal_from_s_and_interior(lam, s, hint)
            if h is None: continue
            ok, cost = self.check_primal(lam, s, h)
            if ok:
                primal = (s, h, cost, den); break
        if primal is None:
            primal = self.solve_support_primal(lam, x)
        if primal is None:
            out['primal'] = None
        else:
            s, h, cost, den = primal
            out['primal'] = {'s': s, 'h': h, 'cost': cost, 'den_used': den}
        if not want_dual:
            return out
        yf = -res.ineqlin.marginals; muf = -res.eqlin.marginals
        nR = len(self.R)
        dual = None
        for den in dens:
            y = {r: Q(float(yf[r])).limit_denominator(den) for r in range(nR) if abs(yf[r]) > 1e-12}
            z = [Q(float(yf[nR + k])).limit_denominator(den) for k in range(n - 1)]
            mu = [Q(float(muf[r])).limit_denominator(den) for r in range(len(self.eqs))]
            ok, val = self.check_dual(lam, y, z, mu)
            if ok:
                dual = (y, z, mu, val, den); break
        if dual is None:
            dual = self.solve_support_dual(lam, yf, muf, x)
        out['dual'] = None if dual is None else {'y': dual[0], 'z': dual[1], 'mu': dual[2], 'value': dual[3], 'den_used': dual[4]}
        return out

    # ------------------------------------------------------------ exact fallbacks ---------------
    def solve_support_dual(self, lam, yf, muf, x, tol=1e-9):
        """Exact re-solve of the dual on the float support: unknowns = multipliers with float>tol
        (rhombus y, ordering z), all mu, and the slack nu_k for s-components whose float value is ~0;
        equations = stationarity for every variable.  Any exact solution with the right signs certifies."""
        n = self.n; nR = len(self.R)
        supp_y = [r for r in range(nR) if yf[r] > tol]
        supp_z = [k for k in range(n - 1) if yf[nR + k] > tol]
        supp_nu = [k for k in range(n) if x[self.H + k] < tol]
        unknowns = [('y', r) for r in supp_y] + [('z', k) for k in supp_z] + \
                   [('mu', r) for r in range(len(self.eqs))] + [('nu', k) for k in supp_nu]
        col = {u: i for i, u in enumerate(unknowns)}
        eqrows = {('h', p): {} for p in self.idx}
        for k in range(n): eqrows[('s', k)] = {}
        def add(key, c, v):
            eqrows[key][c] = eqrows[key].get(c, 0) + v
        for r in supp_y:
            o1, o2, a1, a2 = self.R[r]
            for p, c in ((a1, 1), (a2, 1), (o1, -1), (o2, -1)):
                add(('h', p), col[('y', r)], c)
        for k in supp_z:
            add(('s', k), col[('z', k)], -1); add(('s', k + 1), col[('z', k)], 1)
        for r, (coefs, kind) in enumerate(self.eqs):
            for v, c in coefs.items():
                key = ('h', v[1]) if v[0] == 'h' else ('s', v[1] - 1)
                add(key, col[('mu', r)], c)
        for k in supp_nu:
            add(('s', k), col[('nu', k)], -1)
        rows = []; rhs = []
        for key, row in eqrows.items():
            rows.append(row); rhs.append(Q(-1) if key[0] == 's' else Q(0))
        sol = solve_sparse_exact(rows, rhs, len(unknowns))
        if sol is None: return None
        y = {r: sol[col[('y', r)]] for r in supp_y}
        z = [sol[col[('z', k)]] if k in supp_z else Q(0) for k in range(n - 1)]
        mu = [sol[col[('mu', r)]] for r in range(len(self.eqs))]
        ok, val = self.check_dual(lam, y, z, mu)
        return (y, z, mu, val, 'support') if ok else None

    def solve_support_primal(self, lam, x, tol=1e-9):
        """Exact re-solve of the primal on the float active set: unknowns h and s; equations:
        tight rhombi, tight ordering rows, s_k = 0 where float ~ 0, boundary equalities.
        Free directions (if any) are fixed at rationalized float values."""
        n = self.n
        Gx = self.Aub @ x
        tight = [r for r in range(len(self.R)) if abs(Gx[r]) < tol]
        tight_ord = [k for k in range(n - 1) if abs(Gx[len(self.R) + k]) < tol]
        zero_s = [k for k in range(n) if x[self.H + k] < tol]
        unknowns = [('h', p) for p in self.idx] + [('s', k) for k in range(n)]
        col = {u: i for i, u in enumerate(unknowns)}
        rows = []; rhs = []
        for r in tight:
            o1, o2, a1, a2 = self.R[r]
            rows.append({col[('h', a1)]: 1, col[('h', a2)]: 1, col[('h', o1)]: -1, col[('h', o2)]: -1}); rhs.append(Q(0))
        for k in tight_ord:
            rows.append({col[('s', k)]: -1, col[('s', k + 1)]: 1}); rhs.append(Q(0))
        for k in zero_s:
            rows.append({col[('s', k)]: 1}); rhs.append(Q(0))
        for coefs, kind in self.eqs:
            row = {}
            for v, c in coefs.items():
                key = ('h', v[1]) if v[0] == 'h' else ('s', v[1] - 1)
                row[col[key]] = row.get(col[key], 0) + c
            rows.append(row); rhs.append(Q(0) if kind[0] == 'zero' else lam[kind[1] - 1])
        guess = [Q(float(x[self.idx[p]])).limit_denominator(10**6) for p in self.idx] + \
                [Q(float(x[self.H + k])).limit_denominator(10**6) for k in range(n)]
        sol = solve_sparse_exact(rows, rhs, len(unknowns), free_values=guess)
        if sol is None: return None
        h = {p: sol[col[('h', p)]] for p in self.idx}; s = [sol[col[('s', k)]] for k in range(n)]
        ok, cost = self.check_primal(lam, s, h)
        return (s, h, cost, 'support') if ok else None

def solve_sparse_exact(rows, rhs, nvar, free_values=None):
    """Exact Gaussian elimination over Q for a sparse system (list of dict col->coef).  Returns one
    solution (free variables set to free_values or 0), or None if inconsistent."""
    rows = [dict((c, Q(v)) for c, v in r.items()) for r in rows]; rhs = [Q(v) for v in rhs]
    pivots = {}   # col -> row index (reduced row echelon, pivot rows kept fully reduced)
    for i in range(len(rows)):
        r = rows[i]; b = rhs[i]
        for pc, pi in list(pivots.items()):
            if pc in r:
                f = r[pc]
                for c2, v2 in rows[pi].items():
                    nv_ = r.get(c2, Q(0)) - f * v2
                    if nv_ == 0:
                        r.pop(c2, None)
                    else:
                        r[c2] = nv_
                b -= f * rhs[pi]
        rows[i] = r; rhs[i] = b
        if not r:
            if b != 0: return None
            continue
        pc = min(r)
        f = r[pc]
        rows[i] = {c: v / f for c, v in r.items()}; rhs[i] = b / f
        for qc, qi in pivots.items():
            if pc in rows[qi]:
                g = rows[qi][pc]
                for c2, v2 in rows[i].items():
                    nv_ = rows[qi].get(c2, Q(0)) - g * v2
                    if nv_ == 0:
                        rows[qi].pop(c2, None)
                    else:
                        rows[qi][c2] = nv_
                rhs[qi] -= g * rhs[i]
        pivots[pc] = i
    sol = [Q(0)] * nvar
    if free_values is not None:
        for c in range(nvar):
            if c not in pivots: sol[c] = Q(free_values[c])
    for pc, pi in pivots.items():
        v = rhs[pi]
        for c2, coef in rows[pi].items():
            if c2 != pc: v -= coef * sol[c2]
        sol[pc] = v
    return sol

# ---------------------------------------------------------------- calibration --------------------
def calibrate(seed=3, ntest=12):
    """Check the boundary labeling against the explicit Horn LP (check_horn_lp.kappa_lp) on d=4,5."""
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'scratch_A_inverse_commutator'))
    from check_horn_lp import kappa_lp, horn_rows, rand_spec
    rng = np.random.default_rng(seed)
    worst = 0.0
    for d in (4, 5):
        rows = horn_rows(d); M = HiveLP(d)
        for _ in range(ntest):
            lam = rand_spec(d, rng)
            v = kappa_lp(lam, rows)[0]
            f = M.solve_float(lam).fun
            worst = max(worst, abs(f - v))
    return worst

if __name__ == '__main__':
    import time
    t = time.time(); w = calibrate(); print(f"calibration vs Horn LP (d=4,5): max |diff| = {w:.2e}  [{time.time()-t:.1f}s]")
    M = HiveLP(8); c = M.certify([5, 1, 1, 1, -2, -2, -2, -2])
    print("kappa_8(5,1,1,1,-2^4): primal", c['primal']['cost'], "dual", c['dual']['value'], "s =", [str(v) for v in c['primal']['s']])
    M = HiveLP(7); lam = [Q(v, 7) for v in (25, 18, 18, -10, -17, -17, -17)]
    c = M.certify(lam); print("kappa_7 padded example: primal", c['primal']['cost'], "dual", c['dual']['value'], "(paper 74/7)")
    M = HiveLP(8); lam = [Q(v, 7) for v in (25, 18, 18, 0, -10, -17, -17, -17)]
    c = M.certify(lam); print("kappa_8 padded example: primal", c['primal']['cost'], "dual", c['dual']['value'], "(paper 73/7)")

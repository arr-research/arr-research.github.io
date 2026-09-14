"""gen_kappa6.py -- exact chamber certificate for the conjectured 22-form formula

    kappa_6(F) = max_{r=1..22} q_r . g,     g = (lambda_1-lambda_2, ..., lambda_5-lambda_6) >= 0.

Horn program (d=6): kappa_6 = min { s_1+...+s_5 : s_1>=...>=s_5>=0, for all (I,J,K) in T^6_r, 1<=r<=5:
    sum_{k in K} lambda_k <= sum_{i in I, i<=5} s_i - sum_{j in J, j>=2} s_{7-j} }.
For each form q_r:
  LOWER BOUND (global): nonnegative multipliers y on the 522 Horn rows and z on the 5 ordering rows
     (s_k - s_{k+1} >= 0, k=1..4; s_5 >= 0) with  sum_r y_r a_r + D^T z = (1,1,1,1,1)  and  sum_r y_r 1_{K_r} = q_r
     (as a linear form on trace-zero lambda, i.e. in gap coordinates); hence sum s >= q_r . g for every feasible s.
  UPPER BOUND on the chamber C_r = {g >= 0 : (q_r - q_j).g >= 0 for all j}: for every extreme ray rho of C_r an
     exact feasible s(rho) with sum s(rho) = q_r . rho.  Conic combinations of feasible (s, lambda) are feasible
     (the Horn polyhedron is a convex cone), so kappa_6 <= q_r . g on all of C_r.
If a ray fails (LP value > q_r . rho) the LP dual at that ray is a missing facet; it is added and the loop repeats.
Output: certs/kappa6_certificate.json.
"""
import sys, os, json, time, itertools
from fractions import Fraction as Q
from math import gcd
import numpy as np
from scipy.optimize import linprog
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'scratch_A_inverse_commutator'))
from check_horn_lp import horn_t
from hive_exact import solve_sparse_exact

D = 6
def fr(x): return str(Q(x))

def triples(d=D):
    T = []
    for r in range(1, d):
        for I, J, K in horn_t(r, d): T.append((I, J, K))
    return T

def row_coefs(I, J, K, d=D):
    """Return (a: s-coefficients length d-1, kvec: indicator of K length d)."""
    a = [Q(0)] * (d - 1)
    for i in I:
        if i <= d - 1: a[i - 1] += 1
    for j in J:
        if j >= 2: a[d - j] -= 1          # beta_j = -s_{d+1-j}; 0-based index d-j
    k = [Q(0)] * d
    for kk in K: k[kk - 1] = Q(1)
    return a, k

def lam_from_gap(g, d=D):
    """trace-zero lambda from gaps."""
    lam = [sum(g[j:]) for j in range(d - 1)] + [Q(0)]
    m = sum(lam) / d
    return [x - m for x in lam]

def gap_form(w, d=D):
    """Linear form w.lambda on trace-zero lambda -> gap coefficients q_j = W_j - (j/d) W_d."""
    W = list(itertools.accumulate(w)); tot = W[-1]
    return tuple(W[j - 1] - Q(j, d) * tot for j in range(1, d))

class HornLP:
    def __init__(self, d=D):
        self.d = d; self.T = triples(d)
        self.rows = [row_coefs(*t, d=d) for t in self.T]
        A = [[-float(x) for x in a] for a, _ in self.rows]
        for k in range(d - 2):
            e = [0.0] * (d - 1); e[k] = -1; e[k + 1] = 1; A.append(e)
        self.A = np.array(A); self.nT = len(self.T)

    def solve(self, lam):
        lamf = [float(x) for x in lam]
        ub = [-sum(lamf[kk - 1] for kk in K) for (_, _, K) in self.T] + [0.0] * (self.d - 2)
        res = linprog(np.ones(self.d - 1), A_ub=self.A, b_ub=np.array(ub), bounds=[(0, None)] * (self.d - 1), method='highs-ds')
        assert res.status == 0, res.message
        return res

    def exact_witness(self, lam, res, dens=(10**3, 10**4, 10**6)):
        for den in dens:
            s = [Q(float(v)).limit_denominator(den) for v in res.x]
            if self.check_primal(lam, s): return s
        return None

    def check_primal(self, lam, s):
        d = self.d
        if any(x < 0 for x in s) or any(s[k] < s[k + 1] for k in range(d - 2)): return False
        for (a, kv) in self.rows:
            if sum(kv[i] * lam[i] for i in range(d)) > sum(a[i] * s[i] for i in range(d - 1)): return False
        return True

    def exact_dual(self, res, dens=(10**2, 10**3, 10**4, 10**6)):
        """Rationalize the LP dual; return (y dict, z list, q gap-form) verified exactly, else exact re-solve."""
        d = self.d
        yf = -res.ineqlin.marginals
        for den in dens:
            y = {r: Q(float(yf[r])).limit_denominator(den) for r in range(self.nT) if yf[r] > 1e-12}
            z = [Q(float(yf[self.nT + k])).limit_denominator(den) for k in range(d - 2)]
            ok, q = self.check_dual(y, z)
            if ok: return y, z, q
        # exact re-solve on support: unknowns y (support), z (support), nu_k (s_k coefficient slack, k with s float ~0)
        supp_y = [r for r in range(self.nT) if yf[r] > 1e-9]; supp_z = [k for k in range(d - 2) if yf[self.nT + k] > 1e-9]
        supp_nu = [k for k in range(d - 1) if res.x[k] < 1e-9]
        unknowns = [('y', r) for r in supp_y] + [('z', k) for k in supp_z] + [('nu', k) for k in supp_nu]
        col = {u: i for i, u in enumerate(unknowns)}
        rows = [dict() for _ in range(d - 1)]
        for r in supp_y:
            a, _ = self.rows[r]
            for i in range(d - 1):
                if a[i]: rows[i][col[('y', r)]] = rows[i].get(col[('y', r)], 0) + a[i]
        for k in supp_z:
            rows[k][col[('z', k)]] = rows[k].get(col[('z', k)], 0) + 1; rows[k + 1][col[('z', k)]] = rows[k + 1].get(col[('z', k)], 0) - 1
        for k in supp_nu:
            rows[k][col[('nu', k)]] = rows[k].get(col[('nu', k)], 0) + 1
        sol = solve_sparse_exact(rows, [Q(1)] * (d - 1), len(unknowns))
        if sol is None: return None
        y = {r: sol[col[('y', r)]] for r in supp_y}; z = [sol[col[('z', k)]] if k in supp_z else Q(0) for k in range(d - 2)]
        for k in supp_nu: z.append(None)
        # fold nu into the s_{d-1} >= 0 multiplier convention: here we simply re-verify allowing residual >= 0
        ok, q = self.check_dual(y, z[:d - 2])
        return (y, z[:d - 2], q) if ok else None

    def check_dual(self, y, z):
        """Identity: sum_r y_r a_r + D^T z has all coefficients <= 1 ... we require == 1 except that a
        nonnegative slack is allowed (it corresponds to the multiplier of s_k >= 0).  Returns (ok, q)."""
        d = self.d
        if any(v < 0 for v in y.values()) or any(v < 0 for v in z): return False, None
        coef = [Q(0)] * (d - 1); w = [Q(0)] * d
        for r, v in y.items():
            a, kv = self.rows[r]
            for i in range(d - 1): coef[i] += v * a[i]
            for i in range(d): w[i] += v * kv[i]
        for k in range(d - 2):
            coef[k] += z[k]; coef[k + 1] -= z[k]
        if any(c > 1 for c in coef): return False, None      # slack 1 - coef >= 0 is the multiplier of s_k >= 0
        return True, gap_form(w, d)

# ------------------------------------------------------------ exact cone enumeration -------------
def nullspace_1d(rows, n):
    """rows: list of rational n-vectors with rank n-1 -> primitive integer null vector, else None."""
    M = [list(r) for r in rows]; piv = []
    rr = 0
    for c in range(n):
        p = next((i for i in range(rr, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[rr], M[p] = M[p], M[rr]
        M[rr] = [x / M[rr][c] for x in M[rr]]
        for i in range(len(M)):
            if i != rr and M[i][c] != 0:
                f = M[i][c]; M[i] = [x - f * y for x, y in zip(M[i], M[rr])]
        piv.append(c); rr += 1
        if rr == len(M): break
    if rr != n - 1: return None
    free = [c for c in range(n) if c not in piv][0]
    v = [Q(0)] * n; v[free] = Q(1)
    for i, c in enumerate(piv): v[c] = -M[i][free]
    den = 1
    for x in v: den = den * x.denominator // gcd(den, x.denominator)
    iv = [int(x * den) for x in v]; g = 0
    for x in iv: g = gcd(g, abs(x))
    return tuple(x // g for x in iv)

def extreme_rays(H, n):
    """H: list of rational n-vectors (inequalities h.g >= 0). Brute force over (n-1)-subsets."""
    rays = set()
    for sub in itertools.combinations(range(len(H)), n - 1):
        v = nullspace_1d([H[i] for i in sub], n)
        if v is None: continue
        for cand in (v, tuple(-x for x in v)):
            if all(sum(h[i] * cand[i] for i in range(n)) >= 0 for h in H):
                rays.add(cand)
    return sorted(rays)

def rank(rows):
    M = [list(map(Q, r)) for r in rows]; r = 0
    if not M: return 0
    for c in range(len(M[0])):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]; M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
    return r

INITIAL = [(Q(7,6),Q(4,3),Q(3,2),Q(2,3),Q(-1,6)), (Q(3,2),Q(2),Q(1,2),Q(0),Q(-1,2)), (Q(5,6),Q(2,3),Q(3,2),Q(4,3),Q(1,6)),
           (Q(5,6),Q(5,3),Q(3,2),Q(1,3),Q(1,6)), (Q(3,2),Q(1),Q(3,2),Q(0),Q(-1,2)), (Q(1,2),Q(2),Q(1,2),Q(0),Q(1,2)),
           (Q(1),Q(2),Q(1),Q(0),Q(0)), (Q(11,6),Q(5,3),Q(1,2),Q(-2,3),Q(-5,6)), (Q(1,2),Q(2),Q(3,2),Q(0),Q(-1,2)),
           (Q(13,6),Q(4,3),Q(-1,2),Q(-4,3),Q(-7,6)), (Q(5,2),Q(0),Q(-3,2),Q(-2),Q(-3,2))]

def main():
    t0 = time.time()
    LP = HornLP(); print(f"Horn triples d=6: {LP.nT} (counts by r: {[len(horn_t(r,6)) for r in range(1,6)]})")
    forms = []
    for q in INITIAL:
        forms.append(tuple(q)); forms.append(tuple(reversed(q)))
    forms = sorted(set(forms)); print("initial forms:", len(forms))
    n = D - 1
    while True:
        added = False
        chambers = []
        for r, q in enumerate(forms):
            H = [tuple(Q(int(i == k)) for k in range(n)) for i in range(n)]
            H += [tuple(q[i] - qj[i] for i in range(n)) for j, qj in enumerate(forms) if j != r]
            rays = extreme_rays(H, n)
            rk = rank(rays)
            ch = {'q': q, 'rays': rays, 'rank': rk, 'witnesses': []}
            for rho in rays:
                lam = lam_from_gap([Q(x) for x in rho])
                res = LP.solve(lam)
                target = sum(q[i] * rho[i] for i in range(n))
                if res.fun > float(target) + 1e-7:
                    yd = LP.exact_dual(res)
                    print(f"  form {r} {[str(x) for x in q]}: ray {rho} has LP value {res.fun:.6f} > {float(target):.6f}; new facet {None if yd is None else [str(x) for x in yd[2]]}")
                    if yd is not None and yd[2] not in forms:
                        forms.append(yd[2]); forms.append(tuple(reversed(yd[2]))); forms = sorted(set(forms)); added = True
                    break
                s = LP.exact_witness(lam, res)
                assert s is not None, (q, rho)
                assert sum(s) == target, (q, rho, sum(s), target)
                ch['witnesses'].append(s)
            if added: break
            # dual at an interior point (sum of rays)
            g0 = [sum(rho[i] for rho in rays) for i in range(n)]
            res = LP.solve(lam_from_gap([Q(x) for x in g0]))
            yd = LP.exact_dual(res)
            assert yd is not None, ('dual failed', q)
            y, z, qq = yd
            assert qq == q, ('dual form mismatch', q, qq)
            ch['dual'] = (y, z)
            chambers.append(ch)
            print(f"chamber {r:2d} q={[str(x) for x in q]}: {len(rays)} rays, rank {rk}, dual support {len(y)}  [{time.time()-t0:.1f}s]", flush=True)
        if not added: break
        print("forms now:", len(forms))
    out = {'d': 6, 'n_forms': len(forms), 'horn_triple_count': LP.nT,
           'conventions': 'Horn program in s=(s_1..s_5), s_6=0: sum_{k in K} lambda_k <= sum_{i in I,i<=5} s_i - sum_{j in J,j>=2} s_{7-j}; gaps g_j = lambda_j - lambda_{j+1}; a form q acts as q.g; chamber C_r = {g>=0: (q_r-q_j).g>=0}; rays are primitive integer vectors',
           'chambers': []}
    for ch in chambers:
        y, z = ch['dual']
        out['chambers'].append({'q': [fr(x) for x in ch['q']], 'rank': ch['rank'],
                                'rays': [list(rho) for rho in ch['rays']],
                                'witness_s': [[fr(x) for x in s] for s in ch['witnesses']],
                                'dual_y': [[list(LP.T[r][0]), list(LP.T[r][1]), list(LP.T[r][2]), fr(v)] for r, v in sorted(y.items()) if v != 0],
                                'dual_z': [fr(v) for v in z]})
    out['runtime_s'] = round(time.time() - t0, 1)
    with open(os.path.join('certs', 'kappa6_certificate.json'), 'w') as f: json.dump(out, f)
    print(f"wrote certs/kappa6_certificate.json: {len(forms)} forms, total rays {sum(len(c['rays']) for c in chambers)}, {out['runtime_s']}s")

if __name__ == '__main__':
    main()

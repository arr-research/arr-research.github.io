"""stable_templates.py -- dimension-independent lower bounds for kappa_d(a, 0^(d-2N), -b^rev), all d >= d_0.

A *template* is (I0,I1,J0,J1,K0,K1), subsets of [M], with |I0|+|I1| = |J0|+|J1| = |K0|+|K1| = r and
|I1|+|J1| = |K1|.  In dimension d >= 2M it defines the index triple
    I = I0 u {d+1-t : t in I1},  J = J0 u {d+1-t : t in J1},  K = K0 u {d+1-t : t in K1}
("small" indices <= M, "large" indices >= d+1-M).  Horn's recursive membership (I,J,K) in T^d_r is a finite
set of conditions that are affine in d; the template is STABLE from d_0 = 2M on iff every condition has slope <= 0
in d and holds at d = d_0 (then it holds for all d >= d_0).  For a stable template the Horn inequality reads
    sum_{k in K0} lam_k - sum_{t in K1} b_t <= sum_{i in I0} s_i + sum_{t in I1} s'_t - sum_{j in J0} s'_j - sum_{t in J1} s_t
with s'_t := s_{d+1-t} (lam_k = a_k for k <= N, 0 for N < k <= M; b_t := 0 for t > N).  Since sum_{all} s >=
sum_{i<=M} s_i + sum_{t<=M} s'_t (d >= 2M), the LP
    min sum s + sum s'  s.t. all stable-template inequalities, s decreasing >= 0, s' increasing >= 0, s'_M <= s_M
is a lower bound for kappa_d for every d >= 2M.  If it equals the d=2N value, padding invariance is PROVED.
"""
import sys, os, itertools, time, json
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'scratch_A_inverse_commutator'))
from check_horn_lp import horn_t
from gen_AB_costs import A_N, B_N, u3, z_N
from hive_exact import solve_sparse_exact

def fr(x): return str(Q(x))

def sorted_symbolic(small, large):
    """Index list in dimension d as (coef_d, const) pairs, ascending: small j -> (0,j); large t -> (1, 1-t) (= d+1-t)."""
    return [(0, j) for j in sorted(small)] + [(1, 1 - t) for t in sorted(large, reverse=True)]

def stable(I, J, K, r, d0, inner):
    """inner: list of (q, T^r_q). Check all recursive conditions: slope <= 0 and holds at d0."""
    for q, Tq in inner:
        for F, G, H in Tq:
            sl = sum(I[f - 1][0] for f in F) + sum(J[g - 1][0] for g in G) - sum(K[h - 1][0] for h in H)
            if sl > 0: return False
            c = sum(I[f - 1][1] for f in F) + sum(J[g - 1][1] for g in G) - sum(K[h - 1][1] for h in H) - q * (q + 1) // 2
            if sl * d0 + c > 0: return False
    return True

def templates(M, rmax, noI1=False):
    """Yield stable templates (I0,I1,J0,J1,K0,K1,r) with d0 = 2M."""
    d0 = 2 * M; idx = list(range(1, M + 1))
    for r in range(1, rmax + 1):
        inner = [(q, horn_t(q, r)) for q in range(1, r)]
        # all (small, large) splits of size r
        parts = []
        for k1 in range(0, r + 1):
            for S in itertools.combinations(idx, r - k1):
                for L in itertools.combinations(idx, k1):
                    parts.append((S, L))
        # index K parts by (|K1|, sum K0 - sum K1)
        byK = {}
        for S, L in parts:
            byK.setdefault((len(L), sum(S) - sum(L)), []).append((S, L))
        cnt = 0
        for I0, I1 in parts:
            if noI1 and I1: continue
            Isym = sorted_symbolic(I0, I1)
            for J0, J1 in parts:
                k1 = len(I1) + len(J1)
                if k1 > r: continue
                target = sum(I0) - sum(I1) + sum(J0) - sum(J1) - r * (r + 1) // 2
                Jsym = sorted_symbolic(J0, J1)
                for K0, K1 in byK.get((k1, target), []):
                    Ksym = sorted_symbolic(K0, K1)
                    if stable(Isym, Jsym, Ksym, r, d0, inner):
                        cnt += 1
                        yield (I0, I1, J0, J1, K0, K1, r)

def lower_bound_lp(N, a, b, M, rmax, verbose=True, noI1=False):
    t0 = time.time()
    lam_small = [a[k - 1] if k <= N else Q(0) for k in range(1, M + 1)]
    bb = [b[t - 1] if t <= N else Q(0) for t in range(1, M + 1)]
    # variables: s_1..s_M (0..M-1), s'_1..s'_M (M..2M-1)
    nv = 2 * M; rows = []; rhs = []; tmpl = []
    # the feasible set of s is the same for F and -F (swap R,S), so the Horn inequalities of the reflected
    # target (b, 0, -a^rev) are valid constraints on the same s: 'refl' = 0 uses (a,b), 'refl' = 1 uses (b,a).
    lam_small_r = [b[k - 1] if k <= N else Q(0) for k in range(1, M + 1)]
    aa = [a[t - 1] if t <= N else Q(0) for t in range(1, M + 1)]
    for (I0, I1, J0, J1, K0, K1, r) in templates(M, rmax, noI1):
        coef = [Q(0)] * nv
        for i in I0: coef[i - 1] += 1
        for t in I1: coef[M + t - 1] += 1
        for j in J0: coef[M + j - 1] -= 1
        for t in J1: coef[t - 1] -= 1
        for refl, (ls, bs) in enumerate(((lam_small, bb), (lam_small_r, aa))):
            val = sum(ls[k - 1] for k in K0) - sum(bs[t - 1] for t in K1)
            rows.append(coef); rhs.append(val); tmpl.append((I0, I1, J0, J1, K0, K1, r, refl))
    nT = len(rows)
    if verbose: print(f"  N={N} M={M} rmax={rmax}: {nT} stable templates  [{time.time()-t0:.1f}s]", flush=True)
    A = [[-float(c) for c in row] for row in rows]; ub = [-float(v) for v in rhs]
    order = []
    for k in range(M - 1):       # s_{k+1} >= s_{k+2}
        e = [0.0] * nv; e[k] = -1; e[k + 1] = 1; order.append(e)
    for k in range(M - 1):       # s'_{k+1} <= s'_{k+2}
        e = [0.0] * nv; e[M + k] = 1; e[M + k + 1] = -1; order.append(e)
    e = [0.0] * nv; e[2 * M - 1] = 1; e[M - 1] = -1; order.append(e)   # s'_M <= s_M
    A += order; ub += [0.0] * len(order)
    res = linprog(np.ones(nv), A_ub=np.array(A), b_ub=np.array(ub), bounds=[(0, None)] * nv, method='highs-ds')
    assert res.status == 0, res.message
    if verbose: print(f"  LP lower bound = {res.fun:.10f} ~ {Q(res.fun).limit_denominator(10**6)}  x = {[str(Q(v).limit_denominator(10**4)) for v in res.x]}  [{time.time()-t0:.1f}s]", flush=True)
    return res, rows, rhs, tmpl, order

def exact_dual(res, rows, rhs, tmpl, order, nv):
    """Rationalize LP dual -> exact certificate: multipliers y>=0 on templates, w>=0 on ordering rows, such that
    sum y_r coef_r + sum w_k order_k <= 1 componentwise (slack = multiplier of x >= 0); bound = sum y_r val_r."""
    yf = -res.ineqlin.marginals; nT = len(rows)
    for den in (10**2, 10**3, 10**4, 10**6):
        y = {r: Q(float(yf[r])).limit_denominator(den) for r in range(nT) if yf[r] > 1e-12}
        w = [Q(float(yf[nT + k])).limit_denominator(den) for k in range(len(order))]
        coef = [Q(0)] * nv
        for r, v in y.items():
            for i in range(nv): coef[i] += v * rows[r][i]
        for k, v in enumerate(w):
            for i in range(nv): coef[i] -= v * Q(int(order[k][i]))   # order rows are "order.x <= 0": Lagrangian adds -w*order? see below
        # Derivation: sum x >= sum_i coef'_i x_i where coef' = sum_r y_r coef_r - sum_k w_k order_k  (order_k . x <= 0, w_k>=0
        # gives -w_k order_k.x >= 0), provided coef' <= 1 and x >= 0; and sum_r y_r coef_r.x >= sum_r y_r val_r.
        if all(v >= 0 for v in y.values()) and all(v >= 0 for v in w) and all(c <= 1 for c in coef):
            bound = sum(v * rhs[r] for r, v in y.items())
            return y, w, bound
    return None

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    M = int(sys.argv[2]) if len(sys.argv) > 2 else N
    rmax = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    fam = sys.argv[4] if len(sys.argv) > 4 else 'AB'
    noI1 = '--noI1' in sys.argv
    a, b = (A_N(N), B_N(N)) if fam == 'AB' else (u3(N), z_N(N))
    print(f"target ({fam}) N={N}: a={[str(x) for x in a]} b={[str(x) for x in b]}")
    res, rows, rhs, tmpl, order = lower_bound_lp(N, a, b, M, rmax, noI1=noI1)
    ed = exact_dual(res, rows, rhs, tmpl, order, 2 * M)
    if ed is None:
        print("  exact dual rationalization failed"); sys.exit(1)
    y, w, bound = ed
    print(f"  EXACT dimension-independent lower bound (all d >= {2*M}): kappa_d >= {bound}; support {len(y)} templates:")
    for r, v in sorted(y.items(), key=lambda kv: -kv[1]):
        print(f"     y={str(v):>8}  r={tmpl[r][6]} refl={tmpl[r][7]}  I0={tmpl[r][0]} I1={tmpl[r][1]} J0={tmpl[r][2]} J1={tmpl[r][3]} K0={tmpl[r][4]} K1={tmpl[r][5]}   val={rhs[r]}")
    out = {'family': fam, 'N': N, 'M': M, 'rmax': rmax, 'noI1': noI1, 'd0': 2 * M, 'a': [fr(x) for x in a], 'b': [fr(x) for x in b], 'bound': fr(bound),
           'templates': [{'I0': list(tmpl[r][0]), 'I1': list(tmpl[r][1]), 'J0': list(tmpl[r][2]), 'J1': list(tmpl[r][3]), 'K0': list(tmpl[r][4]), 'K1': list(tmpl[r][5]), 'r': tmpl[r][6], 'refl': tmpl[r][7], 'y': fr(v)} for r, v in sorted(y.items()) if v != 0],
           'order_multipliers': [fr(v) for v in w]}
    os.makedirs('certs', exist_ok=True)
    with open(os.path.join('certs', f'alld_lower_{fam}_N{N}.json'), 'w') as f: json.dump(out, f)
    print(f"  wrote certs/alld_lower_{fam}_N{N}.json")

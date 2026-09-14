"""Task (d): padding non-invariance and rank forcing at the rational point a=(17,17,17,10), b=(25,18,18) (units 1/61), m=4.
EXACT (cdd gmp) Horn LPs over the reviewer's own full Fulton lists (d=7: 2062 rows, d=8: 8752 rows):
  kappa_7, kappa_8, min s_5 on the optimal face at z=1, rank-4-capped value at z=1.
Then (float, tight) sampling of the 'new part' {g0 > max S(4,1)}: is rank 5 forced there (cap-4 value > kappa_8)?"""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, time, numpy as np
from fractions import Fraction as Q
import cdd.gmp as g
sys.path.insert(0, AUTHOR_DIR)
from horn_own import all_T, horn_rows, kappa_horn, Hive, spec, rand_point, form_val
W = AUTHOR_DIR

def exact_lp(lam, d, objective, extra_rows=(), cap=None):
    """min objective.s  s.t. Horn rows (own T^d), ordering, s>=0, extra rows (const + coef.s >= 0). lam integers. Returns (status, value, s)."""
    rows = []
    for I, J, K in all_T(d):
        r = [Q(0)] * d   # [const, s_1..s_{d-1}]
        r[0] = -sum(lam[k - 1] for k in K)
        for i in I:
            if i < d: r[i] += 1
        for j in J:
            if j > 1: r[d + 1 - j] -= 1
        rows.append(r)
    for t in range(1, d - 1):
        r = [Q(0)] * d; r[t] = 1; r[t + 1] = -1; rows.append(r)
    for t in range(1, d):
        r = [Q(0)] * d; r[t] = 1; rows.append(r)
    lin = []
    for er in extra_rows: rows.append(list(er))
    if cap is not None:
        for t in range(cap + 1, d):
            r = [Q(0)] * d; r[t] = 1; rows.append(r); lin.append(len(rows) - 1)
    M = g.matrix_from_array(rows, lin_set=lin, rep_type=g.RepType.INEQUALITY)
    M.obj_type = g.LPObjType.MIN; M.obj_func = [Q(0)] + [Q(x) for x in objective]
    lp = g.linprog_from_matrix(M); g.linprog_solve(lp)
    return lp.status, lp.obj_value, lp.primal_solution

lam7 = [17, 17, 17, 10, -18, -18, -25]; lam8 = [17, 17, 17, 10, 0, -18, -18, -25]
t0 = time.time()
st, v7, s7 = exact_lp(lam7, 7, [1] * 6); print(f"EXACT kappa_7 * 61 = {v7} (status {st}), s = {s7}  ({time.time()-t0:.0f}s)", flush=True)
st, v8, s8 = exact_lp(lam8, 8, [1] * 7); print(f"EXACT kappa_8 * 61 = {v8} (status {st}), s = {s8}  ({time.time()-t0:.0f}s)", flush=True)
# min s_5 on the optimal face at z=1: add sum s <= v8 (i.e. v8 - sum s >= 0)
face = [Q(v8)] + [Q(-1)] * 7
st, m5, s = exact_lp(lam8, 8, [0, 0, 0, 0, 1, 0, 0], extra_rows=[face]); print(f"EXACT min s_5 on the optimal face (z=1) = {m5} (status {st}), s = {s}  -> rank >= 5 forced: {m5 > 0}", flush=True)
st, v8c, s = exact_lp(lam8, 8, [1] * 7, cap=4); print(f"EXACT rank-4-capped value at z=1 = {v8c} (status {st}), s = {s}  ({time.time()-t0:.0f}s)", flush=True)
# also min s_4 on the optimal face at z=0 (min rank at z=0)
face7 = [Q(v7)] + [Q(-1)] * 6
st, m4, s = exact_lp(lam7, 7, [0, 0, 0, 1, 0, 0], extra_rows=[face7]); print(f"EXACT min s_4 on optimal face (z=0) = {m4}; min s_5: ", end="")
st, m5z0, s = exact_lp(lam7, 7, [0, 0, 0, 0, 1, 0], extra_rows=[face7]); print(f"{m5z0} -> a rank-4 optimizer exists at z=0: {m5z0 == 0}", flush=True)

# --- the 'new part': points where g0 = (1,2,3,4,-2,-1) exceeds max S(4,1); is rank 5 forced at z=1 there?
S1 = [tuple(f) for f in json.load(open(f"{W}/closed_m4_z1.json"))]; g0 = (1, 2, 3, 4, -2, -1)
rows8 = horn_rows(8); rows7 = horn_rows(7); rng = np.random.default_rng(5)
n_new = 0; forced = 0; cap_eq_k7 = 0; worst = 0
for i in range(4000):
    a, b = rand_point(4, rng, law=i % 6)
    if form_val(g0, a, b) - max(form_val(h, a, b) for h in S1) < 1e-6: continue
    n_new += 1
    k8 = kappa_horn(spec(a, b, 1), rows8).fun; k8c = kappa_horn(spec(a, b, 1), rows8, cap=4).fun; k7 = kappa_horn(spec(a, b, 0), rows7).fun
    if k8c - k8 > 1e-9: forced += 1
    if abs(k8c - k7) < 1e-9: cap_eq_k7 += 1
    worst = max(worst, abs(k7 - form_val(g0, a, b)))
    if n_new >= 150: break
print(f"'new part' sample: {n_new} points with g0 > max S(4,1); rank-5 forced at z=1 (cap-4 value > kappa_8) at {forced}; cap-4 value == kappa_7 at {cap_eq_k7}; max|kappa_7 - g0| = {worst:.1e}")

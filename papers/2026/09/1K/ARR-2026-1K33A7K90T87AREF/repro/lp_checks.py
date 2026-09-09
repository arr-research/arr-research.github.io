"""Own Horn LP (HiGHS): (i) exposed forms via LP duals / gradients for d<=7; (ii) uniqueness of the optimal s (max-min of each s_t at cost=LP value)."""
import sys, random, itertools
sys.path.insert(0, "../research/scratch_A2")
import numpy as np
from fractions import Fraction as Q
from scipy.optimize import linprog
from my_horn import T
from conj_formula import forms_mn2

def rows(d):
    A = []; 
    for r in range(1, d):
        for (I, J, K) in T(r, d):
            a = np.zeros(d); b = np.zeros(d)
            for i in I:
                if i < d: a[i-1] += 1
            for j in J:
                if j > 1: a[d-j] -= 1
            for k in K: b[k-1] += 1
            A.append((a, b))
    return A
def solve(lam, R, extra_obj=None, budget=None):
    d = len(lam); A = []; ub = []
    for a, b in R: A.append(-a); ub.append(-(b @ lam))
    for j in range(d-1):
        e = np.zeros(d); e[j] = -1; e[j+1] = 1; A.append(e); ub.append(0.0)
    if budget is not None: A.append(np.ones(d)); ub.append(budget)
    c = np.ones(d) if extra_obj is None else extra_obj
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(ub), bounds=[(0, None)]*(d-1)+[(0, 0)], method="highs")
    assert res.status == 0, res.message
    return res
def phi(a, b, m):
    vals = {n: sum(x*y for x, y in zip(al, a)) + c1*b[0] + c2*b[1] for n, al, c1, c2 in forms_mn2(m)}
    return vals
rng = np.random.default_rng(5)
def rand_pt(m):
    a = np.sort(rng.exponential(size=m))[::-1]; a /= a.sum()
    b2 = rng.uniform(0, 0.5); return a, (1 - b2, b2)

print("=== (i) exposed forms by LP-dual gradient sampling (own Horn LP), canonical (alpha_1..alpha_m, beta_1) with beta_2 -> 0")
for m, z in [(2,0),(2,1),(2,2),(3,0),(3,1),(3,2),(4,0),(4,1),(5,0)]:
    d = m + z + 2; R = rows(d); seen = {}
    N = 600
    for _ in range(N):
        a, b = rand_pt(m); lam = np.array(list(a) + [0]*z + [-b[1], -b[0]])
        res = solve(lam, R)
        # gradient d kappa/d lambda_k = -sum_r y_r b_r  (dual)
        y = -res.ineqlin.marginals[:len(R)]
        grad = sum(y[r] * R[r][1] for r in range(len(R)))
        alpha = grad[:m]; beta2 = -grad[d-2]; beta1 = -grad[d-1]; t = -beta2
        key = tuple(round(float(x), 6) for x in np.concatenate([alpha - t, [beta1 + t]]))
        seen[key] = seen.get(key, 0) + 1
        v = max(phi(a, b, m).values()); assert abs(res.fun - v) < 1e-9, (a, b, res.fun, v)
    forms = {n: tuple(float(x) for x in al) + (float(c1 - c2),) for n, al, c1, c2 in forms_mn2(m)}   # beta2 -> 0 canonical
    named = {}
    for k, cnt in seen.items():
        nm = [n for n, f in forms.items() if np.allclose(k, f, atol=1e-5)]
        named[nm[0] if nm else str(k)] = cnt
    print(f"m={m} z={z} d={d}: LP==Phi on {N} pts; dual forms: {dict(sorted(named.items(), key=lambda x: -x[1]))}")

print("=== (ii) uniqueness of optimal s: max - min of each s_t over optimal face")
for m, z, N in [(2,0,60),(2,1,60),(3,0,80),(3,1,80),(3,2,40),(4,0,60)]:
    d = m + z + 2; R = rows(d); nonuni = 0; chambers = {}
    for _ in range(N):
        a, b = rand_pt(m); lam = np.array(list(a) + [0]*z + [-b[1], -b[0]])
        res = solve(lam, R); v = res.fun
        spread = 0.0
        for t in range(d-1):
            e = np.zeros(d); e[t] = 1
            hi = -solve(lam, R, extra_obj=-e, budget=v + 1e-9).fun; lo = solve(lam, R, extra_obj=e, budget=v + 1e-9).fun
            spread = max(spread, hi - lo)
        vals = phi(a, b, m); arg = max(vals, key=vals.get)
        if spread > 1e-6:
            nonuni += 1; chambers[arg] = chambers.get(arg, 0) + 1
    print(f"m={m} z={z}: non-unique optimal spectrum at {nonuni}/{N} points; active forms where non-unique: {chambers}")

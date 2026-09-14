"""rev_C.py -- (C) all-d template certificates: explicit-d Horn membership (recursion AND LR), assembled inequality,
symbolic stability, refl sanity, human-readable printout for N=6,7."""
import sys, os, time
from fractions import Fraction as Q
import numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # (repro copy: was the reviewer's scratchpad path)
from rev_lib import *
AUTH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')  # (repro copy: was the author's working directory)

def inst(S0, S1, d): return tuple(sorted(list(S0) + [d + 1 - t for t in S1]))

def symbolic_stable(T, d0):
    """Own symbolic check: every recursive condition is affine in d with slope <= 0 and holds at d0; sum condition
    identically; index sets well-formed for all d >= d0 (requires d0 >= 2M so that small < large)."""
    r = T['r']
    def sym(S0, S1):
        return [(0, j) for j in sorted(S0)] + [(1, 1 - t) for t in sorted(S1, reverse=True)]
    I, J, K = sym(T['I0'], T['I1']), sym(T['J0'], T['J1']), sym(T['K0'], T['K1'])
    if not (len(I) == len(J) == len(K) == r): return False
    if sum(x[0] for x in I) + sum(x[0] for x in J) != sum(x[0] for x in K): return False
    if sum(x[1] for x in I) + sum(x[1] for x in J) != sum(x[1] for x in K) + r * (r + 1) // 2: return False
    for q in range(1, r):
        for F, Gg, Hh in horn_list(q, r):
            sl = sum(I[f - 1][0] for f in F) + sum(J[g - 1][0] for g in Gg) - sum(K[h - 1][0] for h in Hh)
            c0 = sum(I[f - 1][1] for f in F) + sum(J[g - 1][1] for g in Gg) - sum(K[h - 1][1] for h in Hh) - q * (q + 1) // 2
            if sl > 0 or sl * d0 + c0 > 0: return False
    return True

def check_file(fn, ds_extra=(0, 1, 5, 9), verbose=False):
    C = load_json(fn); N, M, d0 = C['N'], C['M'], C['d0']
    a = [Q(x) for x in C['a']]; b = [Q(x) for x in C['b']]; bound = Q(C['bound'])
    w = [Q(x) for x in C['order_multipliers']]
    probs = []
    if d0 != 2 * M or M < N: probs.append('d0/M')
    for T in C['templates']:
        if Q(T['y']) < 0: probs.append('y<0')
        if not symbolic_stable(T, d0): probs.append(f'symbolic stability fails for {T}')
    for dd in ds_extra:
        d = d0 + dd
        lams = [a + [Q(0)] * (d - 2 * N) + [-x for x in reversed(b)], b + [Q(0)] * (d - 2 * N) + [-x for x in reversed(a)]]
        coef = [Q(0)] * d; total = Q(0); lines = []
        for T in C['templates']:
            I, J, K = inst(T['I0'], T['I1'], d), inst(T['J0'], T['J1'], d), inst(T['K0'], T['K1'], d)
            r = T['r']; y = Q(T['y'])
            if not horn_member(I, J, K, d): probs.append(f'd={d}: not Horn (recursion) {T}')
            if not horn_member_lr(I, J, K, d): probs.append(f'd={d}: not Horn (LR) {T}')
            lam = lams[T['refl']]
            val = sum(lam[k - 1] for k in K)
            row = [Q(0)] * d
            for i in I: row[i - 1] += 1
            for j in J: row[d - j] -= 1        # beta_j = -s_{d+1-j}
            for i in range(d): coef[i] += y * row[i]
            total += y * val
            if verbose:
                terms = ' + '.join(f"{'' if row[i]==1 else str(row[i])+'*'}s_{i+1}" for i in range(d) if row[i] != 0)
                lines.append(f"      y={y}  r={r} refl={T['refl']}  I={I} J={J} K={K}:   {val} <= {terms}")
        # ordering multipliers (rows order.x <= 0): s_{k+2}-s_{k+1}<=0 (k<M-1); s_{d-k}-s_{d-k-1}<=0 ; s_{d+1-M}-s_M<=0
        order = []
        for k in range(M - 1):
            e = [Q(0)] * d; e[k] = -1; e[k + 1] = 1; order.append(e)
        for k in range(M - 1):
            e = [Q(0)] * d; e[d - 1 - k] = 1; e[d - 2 - k] = -1; order.append(e)
        e = [Q(0)] * d; e[d - M] = 1; e[M - 1] = -1; order.append(e)
        if len(w) != len(order) or any(x < 0 for x in w): probs.append('order multipliers')
        for wk, row in zip(w, order):
            for i in range(d): coef[i] -= wk * row[i]
        if any(c > 1 for c in coef): probs.append(f'd={d}: coefficient > 1: {[str(c) for c in coef]}')
        if total != bound: probs.append(f'd={d}: total {total} != bound {bound}')
        if verbose and dd in (0, 9):
            print(f"   d={d}: assembled inequalities:"); print('\n'.join(lines))
            print(f"      => sum_i c_i s_i >= {total}, c = {[str(c) for c in coef]}")
    print(f"{os.path.basename(fn)}: N={N} M={M} d0={d0} bound={bound} templates={len(C['templates'])}: checked d={[d0+x for x in ds_extra]}; problems: {probs if probs else 'NONE'}", flush=True)
    return bound, probs

if __name__ == '__main__':
    t0 = time.time()
    for fn in sorted(os.listdir(os.path.join(AUTH, 'certs'))):
        if fn.startswith('alld_lower_') and fn.endswith('.json'):
            check_file(os.path.join(AUTH, 'certs', fn), verbose=(fn in ('alld_lower_AB_N6_fam.json', 'alld_lower_UZ_N7_fam.json')))
    # refl sanity: kappa_d(lam) == kappa_d(-lam^rev) numerically (d = 6, 7)
    rng = np.random.default_rng(3)
    for d in (6, 7):
        T = all_horn(d); worst = 0
        for _ in range(20):
            x = np.sort(rng.normal(size=d))[::-1]; x -= x.mean()
            v1, _ = horn_lp(list(x), T); v2, _ = horn_lp(list(-x[::-1]), T); worst = max(worst, abs(v1 - v2))
        print(f"refl sanity d={d}: max |kappa(lam) - kappa(-lam^rev)| = {worst:.1e}")
    print(f"[{time.time()-t0:.1f}s]")

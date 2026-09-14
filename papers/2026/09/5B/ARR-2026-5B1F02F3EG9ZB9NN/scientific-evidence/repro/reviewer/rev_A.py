"""rev_A.py -- (A) conventions: Horn lists vs LR, hive LP vs Horn LP, author's exact duals vs my Horn LP."""
import sys, time, itertools, random
from fractions import Fraction as Q
import numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # (repro copy: was the reviewer's scratchpad path)
from rev_lib import *

t0 = time.time()
# 1. counts
for n in range(2, 8):
    cnt = [len(horn_list(r, n)) for r in range(1, n)]
    print(f"d={n}: Horn counts by r {cnt} total {sum(cnt)}  [{time.time()-t0:.1f}s]")

# 2. LR cross-check of the recursive lists for n = 5, 6, 7: over ALL sum-condition triples
for n in (5, 6, 7):
    mism = 0; tot = 0
    for r in range(1, n):
        Tset = set(horn_list(r, n))
        subs = list(itertools.combinations(range(1, n + 1), r)); tri = r * (r + 1) // 2
        for I in subs:
            for J in subs:
                for K in subs:
                    if sum(I) + sum(J) != sum(K) + tri: continue
                    tot += 1
                    inT = (I, J, K) in Tset
                    c = lr_coeff(part_of(I, n), part_of(J, n), part_of(K, n))
                    if inT != (c > 0): mism += 1
    print(f"d={n}: LR-vs-recursion on {tot} sum-condition triples: {mism} mismatches  [{time.time()-t0:.1f}s]")

# 3. hive LP (own) vs Horn LP (own), random spectra
rng = np.random.default_rng(7)
for d in range(3, 8):
    T = all_horn(d); worst = 0
    for _ in range(25):
        x = np.sort(rng.normal(size=d))[::-1]; x -= x.mean()
        v1, _ = horn_lp(list(x), T); v2 = hive_lp(list(x))
        worst = max(worst, abs(v1 - v2))
    print(f"d={d}: own hive LP vs own Horn LP on 25 random spectra: max|diff| = {worst:.1e}; rhombi {len(rhombi(d))}  [{time.time()-t0:.1f}s]")

# also compare with the author's rhombus enumeration count
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))  # (repro copy: was the author's working directory)
import hive_exact as HE
for d in (3, 6, 8):
    mine = rhombi(d); theirs = set((frozenset((o1, o2)), frozenset((a1, a2))) for o1, o2, a1, a2 in HE.rhombi(d))
    print(f"d={d}: my rhombi == author's rhombi (as obtuse/acute pairs): {mine == theirs}  ({len(mine)} vs {len(theirs)})")

# 4. author's exact certificates on random rational spectra, judged by MY checker and MY Horn LP
for d in (4, 5, 6, 7):
    M = HE.HiveLP(d); T = all_horn(d); R = rhombi(d)
    nbad = 0; worst = 0; ndual = 0
    for _ in range(15):
        v = sorted([Q(int(x), 10) for x in rng.integers(-25, 26, size=d)], reverse=True)
        m = sum(v) / d; lam = [x - m for x in v]
        c = M.certify(lam)
        s = c['primal']['s']; h = c['primal']['h']
        ok, why = check_hive_primal(d, lam, s, h, R)
        if not ok: nbad += 1; print('   primal rejected', why); continue
        # convert dual to the JSON format used in the certificates
        dj = {'y': [[list(M.R[r][0]), list(M.R[r][1]), list(M.R[r][2]), list(M.R[r][3]), str(v)] for r, v in c['dual']['y'].items()],
              'z': [str(v) for v in c['dual']['z']], 'mu': [str(v) for v in c['dual']['mu']]}
        val, why = check_hive_dual(d, lam, dj, R)
        if val is None: nbad += 1; print('   dual rejected', why); continue
        ndual += 1
        if val != sum(s): nbad += 1; print('   dual value != primal cost', val, sum(s))
        if val != c['dual']['value']: nbad += 1; print('   my dual value != stored', val, c['dual']['value'])
        vh, _ = horn_lp(lam, T)
        worst = max(worst, abs(vh - float(sum(s))))
    print(f"d={d}: 15 random rational spectra: author certificates judged by my checkers: {nbad} rejections, {ndual} duals ok, max|Horn LP - certified| = {worst:.1e}  [{time.time()-t0:.1f}s]")

# 5. sanity that the dual checker rejects a wrong certificate: perturb a multiplier
M = HE.HiveLP(4); lam = [Q(3), Q(-1), Q(-1), Q(-1)]; c = M.certify(lam)
dj = {'y': [[list(M.R[r][0]), list(M.R[r][1]), list(M.R[r][2]), list(M.R[r][3]), str(v)] for r, v in c['dual']['y'].items()],
      'z': [str(v) for v in c['dual']['z']], 'mu': [str(v) for v in c['dual']['mu']]}
print("kappa_4(3,-1,-1,-1) certified:", c['primal']['cost'], "my dual check:", check_hive_dual(4, lam, dj))
dj2 = dict(dj); dj2['mu'] = list(dj['mu']); dj2['mu'][-1] = str(Q(dj['mu'][-1]) + 1)
print("perturbed mu ->", check_hive_dual(4, lam, dj2))
dj3 = dict(dj); dj3['y'] = [row[:4] + [str(Q(row[4]) + Q(1, 7))] for row in dj['y'][:1]] + dj['y'][1:]
print("perturbed y ->", check_hive_dual(4, lam, dj3))
print("paper checks: kappa_4(3,-1,-1,-1)=6? hive:", hive_lp([3, -1, -1, -1]), " Horn:", horn_lp([3, -1, -1, -1])[0])
print("kappa_7 padded example 74/7 =", 74/7, ":", hive_lp([Q(v, 7) for v in (25, 18, 18, -10, -17, -17, -17)]),
      "; kappa_8 padded 73/7 =", 73/7, ":", hive_lp([Q(v, 7) for v in (25, 18, 18, 0, -10, -17, -17, -17)]))

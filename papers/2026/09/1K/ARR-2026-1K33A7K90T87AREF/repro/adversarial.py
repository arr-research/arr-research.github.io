"""Adversarial search for stratum points with NO feasible layering (own exact recursion), boundary-heavy sampling;
cross-check own forward() vs author's feasible(); build C at boundary points with own constructor."""
import sys, random
sys.path.insert(0, "../research/scratch_A2")
from fractions import Fraction as Q
from my_construct import forward, build
from layer_chain import layerings, feasible, cost
from conj_formula import forms_mn2
import numpy as np

def Phi(a, b):
    m = len(a); best = None
    for name, al, c1, c2 in forms_mn2(m):
        v = sum(Q(x)*y for x, y in zip(al, a)) + c1*b[0] + c2*b[1]
        best = v if best is None or v > best else best
    return best
def E(a, i): return sum(a[i-1::2]) if i <= len(a) else Q(0)
def gaps(a):
    aa = list(a) + [Q(0)]; return [aa[j-1]-aa[j] for j in range(1, len(a)+1, 2)]

rng = random.Random(123)
def gen(m, mode):
    if mode == 0: a = sorted([Q(rng.randint(1, 30), 30) for _ in range(m)], reverse=True)
    elif mode == 1: a = [Q(1)]*m                                    # flat
    elif mode == 2: a = sorted([Q(rng.choice([1, 2, 3]), 3) for _ in range(m)], reverse=True)   # many ties
    elif mode == 3: a = sorted([Q(rng.randint(1, 30), 30) for _ in range(m-1)], reverse=True) + [Q(1, 10**6)]  # a_m tiny
    elif mode == 4: a = [Q(1)] + [Q(1, 10**5)]*(m-1)              # one dominant
    else: a = [Q(2**(m-i)) for i in range(m)]                     # geometric
    P = sum(a)
    # b2 choices: random, b1=b2, exactly at all breakpoints E_k and E_1 - g_j (clipped to (0, P/2])
    cands = [P/2, P*Q(rng.randint(1, 50), 100)] + [E(a, k) for k in range(1, m+2)] + [E(a, 1) - g for g in gaps(a)]
    out = []
    for b2 in cands:
        if 0 < b2 <= P/2: out.append((a, (P - b2, b2)))
    return out

tot = 0; bad = 0; mism = 0; worst = 0.0; built = 0
for m in range(2, 13):
    for mode in range(6):
        for rep in range(8 if mode in (0, 2, 3) else 1):
            for a, b in gen(m, mode):
                lay = layerings(a, b); ph = Phi(a, b)
                feas_mine = {n: forward(L) is not None for n, L in lay.items()}
                feas_auth = {n: feasible(L) for n, L in lay.items()}
                if feas_mine != feas_auth: mism += 1; print("MISMATCH own vs author", m, a, b, feas_mine, feas_auth)
                if not any(feas_mine.values()): bad += 1; print("NO FEASIBLE LAYERING", m, a, b)
                for n in lay:
                    if feas_mine[n]:
                        assert cost(lay[n]) == ph, ("feasible layering with cost != Phi", m, n, a, b)
                        if m <= 9 and built < 400:
                            C, resid, c = build(lay[n]); built += 1
                            worst = max(worst, resid, abs(c - float(ph)))
                tot += 1
    print(f"m={m}: cumulative points={tot} no-feasible={bad} own/author mismatches={mism} built C={built} worst residual={worst:.1e}", flush=True)

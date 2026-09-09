"""Rank-(m+1) optimizers for odd m, z>=1, G_m chamber, via layerings that put the zero eigenvalue inside a layer.
Also: build C at boundary points for larger m; exact unique-argmax count (exposed forms of the max-formula)."""
import sys, random
sys.path.insert(0, "../research/scratch_A2")
from fractions import Fraction as Q
import numpy as np
from my_construct import forward, build
from layer_chain import layerings, cost
from conj_formula import forms_mn2
def pairs(seq): return [list(seq[i:i+2]) for i in range(0, len(seq), 2)]
def Phi(a, b):
    m = len(a); return max(sum(Q(x)*y for x, y in zip(al, a)) + c1*b[0] + c2*b[1] for n, al, c1, c2 in forms_mn2(m))

print("=== rank m+1 optimizers (m odd, z>=1, G_m chamber): layering {-b2},{-b1,a1},{a2,a3},...,{a_{m-1},0},{a_m}")
for m in (3, 5, 7):
    a = [Q(1)]*(m-1) + [Q(9, 10)]          # g_m = a_m = 0.9 is the max odd gap; G_m chamber: b2 >= E_1 - a_m
    P = sum(a); b2 = P/2 - Q(1, 20); b1 = P - b2
    L = [[-b2]] + pairs([-b1] + a[:m-1]) + [[a[m-1]]]     # zero not used -> reference (rank m)
    Lz = [[-b2]] + pairs([-b1] + a[:m-2]) + [[a[m-2], Q(0)], [a[m-1]]]
    ph = Phi(a, (b1, b2))
    for name, lay in (("no-zero", L), ("zero-in-layer", Lz)):
        ok = forward(lay) is not None
        print(f"m={m} z=1 {name}: feasible={ok} cost={cost(lay)} Phi={ph}", end="")
        if ok:
            C, resid, c = build(lay); sv = np.linalg.svd(C, compute_uv=False)
            print(f"  built: resid={resid:.1e} cost={c:.6f} rank={np.linalg.matrix_rank(C, tol=1e-9)} s={np.round(sv**2/2, 4)}")
        else: print()
print("=== build C at boundary points, m = 6, 9, 12 (own constructor)")
rng = random.Random(9); worst = 0.0; n = 0
def E(a, i): return sum(a[i-1::2]) if i <= len(a) else Q(0)
for m in (6, 9, 12):
    for rep in range(6):
        a = sorted([Q(rng.randint(1, 20), 20) for _ in range(m)], reverse=True); P = sum(a)
        aa = a + [Q(0)]
        for b2 in [P/2] + [E(a, k) for k in range(2, m+1)] + [E(a, 1) - (aa[j-1]-aa[j]) for j in range(1, m+1, 2)]:
            if not (0 < b2 <= P/2): continue
            b = (P - b2, b2); ph = Phi(a, b)
            for nm, lay in layerings(a, b).items():
                if forward(lay) is not None:
                    C, resid, c = build(lay); n += 1; worst = max(worst, resid, abs(c - float(ph)))
                    assert np.linalg.matrix_rank(C, tol=1e-8) == m
    print(f"m={m}: built {n} matrices so far, worst max(residual, |cost-Phi|) = {worst:.1e}, all rank m")
print("=== exposed forms of the max-formula: forms that are the unique argmax at some sampled stratum point")
for m in range(2, 10):
    uniq = set()
    for it in range(20000):
        a = sorted([Q(rng.randint(1, 60), 60) for _ in range(m)], reverse=True); P = sum(a)
        b2 = P*Q(rng.randint(1, 50), 100); b = (P - b2, b2)
        vals = {nm: sum(Q(x)*y for x, y in zip(al, a)) + c1*b[0] + c2*b[1] for nm, al, c1, c2 in forms_mn2(m)}
        mx = max(vals.values()); arg = [nm for nm in vals if vals[nm] == mx]
        if len(arg) == 1: uniq.add(arg[0])
    pred = (m-1) + (m+1)//2 + (1 if m >= 3 else 0)
    print(f"m={m}: unique-argmax forms = {len(uniq)} (predicted {pred}); missing: {sorted(set(n for n,_,_,_ in forms_mn2(m)) - uniq)}")

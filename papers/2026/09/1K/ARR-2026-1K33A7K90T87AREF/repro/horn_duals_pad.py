"""Horn dual certificates of each conjectured form F_k, G_j at a random interior point of its chamber, for given (m, pad).
Prints the Horn triples with nonzero dual multiplier, in s-notation (s = p/2)."""
import sys, numpy as np
from check_horn_lp import horn_t
from scipy.optimize import linprog
from conj_formula import forms_mn2
from hive_core import rand_mn2, spec_mn2

def horn_lp_dual(lam):
    d = len(lam); rows = []; trip = []
    for r in range(1, d):
        for I, J, K in horn_t(r, d):
            a = np.zeros(d - 1)
            for i in I:
                if i < d: a[i - 1] += 1
            for j in J:
                if j > 1: a[d - j] -= 1
            b = np.zeros(d)
            for k in K: b[k - 1] += 1
            rows.append((a, b)); trip.append((I, J, K))
    gam = 2 * np.asarray(lam, float)
    A = [-a for a, b in rows]; ub = [-(b @ gam) for a, b in rows]
    for j in range(d - 2):
        e = np.zeros(d - 1); e[j] = -1; e[j + 1] = 1; A.append(e); ub.append(0.0)
    res = linprog(np.ones(d - 1) * 0.5, A_ub=np.array(A), b_ub=np.array(ub), bounds=[(0, None)] * (d - 1), method="highs")
    y = -res.ineqlin.marginals
    return res.fun, res.x, y, trip

m = int(sys.argv[1]); pad = int(sys.argv[2]); seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
rng = np.random.default_rng(seed)
forms = forms_mn2(m)
# find, for each form, a sample where it is the unique argmax with margin
samples = {}
for it in range(20000):
    a, b = rand_mn2(m, rng, law=['exp', 'unif', 'sq'][it % 3])
    vals = [(sum(x * y for x, y in zip(al, a)) + b1c * b[0] + b2c * b[1], name) for name, al, b1c, b2c in forms]
    vals.sort(reverse=True)
    if vals[0][0] - vals[1][0] > 0.02 * vals[0][0] and vals[0][1] not in samples:
        samples[vals[0][1]] = (a, b)
    if len(samples) == len(forms): break
print(f"m={m} pad={pad} d={m+pad+2}: found samples for {sorted(samples)}")
for name, al, b1c, b2c in forms:
    if name not in samples: print("NO SAMPLE for", name); continue
    a, b = samples[name]; lam = spec_mn2(a, b, pad); d = len(lam)
    val, p, y, trip = horn_lp_dual(lam)
    conj = sum(x * y_ for x, y_ in zip(al, a)) + b1c * b[0] + b2c * b[1]
    print(f"--- {name}: alpha={al} b1={b1c} b2={b2c}  LP={val:.6f} conj={conj:.6f}  s={np.round(p/2,4)}")
    for r, t in enumerate(trip):
        if y[r] > 1e-9:
            I, J, K = t; lhs = {}
            for i in I:
                if i < d: lhs[i] = lhs.get(i, 0) + 1
            for j in J:
                if j > 1: lhs[d + 1 - j] = lhs.get(d + 1 - j, 0) - 1
            lhs = {k: v for k, v in sorted(lhs.items()) if v != 0}
            print(f"    y={y[r]:.4f}  I={I} J={J} K={K}   ->  " + " ".join(f"{'+' if v>0 else '-'}{abs(v) if abs(v)!=1 else ''}s{k}" for k, v in lhs.items()) + "  >=  lam" + str(K))
    for j in range(d - 2):
        if y[len(trip) + j] > 1e-9: print(f"    y={y[len(trip)+j]:.4f}  ordering s_{j+1}>=s_{j+2}")

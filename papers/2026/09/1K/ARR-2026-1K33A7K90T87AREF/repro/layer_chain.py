"""Exact (Fractions) feasibility of 2x2-block weighted-shift layerings for the (m,2) stratum.
Layering = list of layers, each a list of 1 or 2 eigenvalues (Fractions). Feasible iff the 2x2 Horn chain
S_1 = -D_0, R_t ~ S_t (same spectrum), S_{t+1} = R_t - D_t >= 0, R_T = D_T is solvable.
State: (trace Tr of S_t, interval [lo,hi] of admissible second eigenvalue sigma_2 of S_t)."""
from fractions import Fraction as Q
import itertools, random

def cost(layers):
    tot = Q(0); Tr = Q(0)
    for L in layers[:-1]:
        Tr -= sum(L); tot += Tr
    return tot

def feasible(layers):
    """Return True/False; layers[0] must be all <= 0, layers[-1] all >= 0."""
    L0 = layers[0]
    if any(x > 0 for x in L0): return False
    Tr = -sum(L0)
    if len(L0) == 1: lo = hi = Q(0)
    else:
        lo = hi = min(-x for x in L0)
    T = len(layers) - 1
    for t in range(1, T + 1):
        L = layers[t]
        if t == T:
            if len(L) == 1: return lo <= 0 <= hi and Tr == L[0]
            d1, d2 = max(L), min(L)
            return lo <= d2 <= hi and Tr == d1 + d2
        if len(L) == 1:
            if not (lo <= 0 <= hi): return False
            Tr = Tr - L[0]
            if Tr < 0: return False
            lo = hi = Q(0); continue
        d1, d2 = max(L), min(L)
        # sigma_2 in [lo,hi]; tau_2 in [sigma_2 - d1, min(Tr - sigma_2 - d1, sigma_2 - d2)] cap [0, inf)
        nlo = max(Q(0), lo - d1)
        mstar = (Tr - d1 + d2) / 2
        if lo <= mstar <= hi: nhi = (Tr - d1 - d2) / 2
        elif hi < mstar: nhi = hi - d2
        else: nhi = Tr - d1 - lo
        if nlo > nhi: return False
        Tr = Tr - d1 - d2; lo, hi = nlo, nhi
    return True

def pairs(seq):
    return [list(seq[i:i + 2]) for i in range(0, len(seq), 2)]

def layerings(a, b):
    """Dict name -> layering for the (m,2) stratum."""
    m = len(a); b1, b2 = b; out = {}
    out["F0"] = pairs([-b1, -b2] + list(a))
    for k in range(1, m):
        out[f"F{k}"] = [[-b1]] + [[a[i]] for i in range(k - 1)] + pairs([a[k - 1], -b2] + list(a[k:]))
    for j in range(1, m + 1, 2):
        seq = [-b1] + list(a)          # a_0 = -b_1, a_1..a_m ; swap positions j and j+1 (1-based in a)
        if j + 1 <= m:
            seq[j], seq[j + 1] = seq[j + 1], seq[j]
            out[f"G{j}"] = [[-b2]] + pairs(seq)
        else:                           # j = m odd: ..., {a_{m-2}}? no: pairs of (a_0..a_{m-2}) then singletons {a_{m-1}}, {a_m}
            out[f"G{j}"] = [[-b2]] + pairs(seq[:m - 1]) + [[a[m - 2]], [a[m - 1]]]
    return out

def forms(a, b):
    from conj_formula import forms_mn2
    m = len(a); vals = {}
    for name, al, b1c, b2c in forms_mn2(m):
        vals[name] = sum(Q(x) * y for x, y in zip(al, a)) + b1c * b[0] + b2c * b[1]
    return vals

def rand_stratum(m, rng, den=60):
    while True:
        a = sorted([Q(rng.randint(1, den), den) for _ in range(m)], reverse=True)
        s = sum(a); b2 = Q(rng.randint(1, den), den) * s / 2
        b1 = s - b2
        if b1 >= b2 > 0: return a, (b1, b2)

if __name__ == "__main__":
    import sys
    rng = random.Random(1)
    mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    for m in range(2, mmax + 1):
        bad = 0; nfeas_hist = {}
        for it in range(N):
            a, b = rand_stratum(m, rng)
            lay = layerings(a, b); fv = forms(a, b)
            # cost of layering must equal the form value
            for name, L in lay.items():
                assert cost(L) == fv[name], (name, cost(L), fv[name])
            mx = max(fv.values())
            feas = {name: feasible(L) for name, L in lay.items()}
            # every feasible layering must have cost == mx (lower bound)
            for name in feas:
                if feas[name] and fv[name] != mx: print("LOWER BOUND VIOLATION?", m, name, a, b); bad += 1
            argmax = [n for n in fv if fv[n] == mx]
            if not any(feas[n] for n in argmax):
                bad += 1
                if bad <= 5: print("NO FEASIBLE ARGMAX LAYERING:", m, a, b, argmax, {n: feas[n] for n in feas if feas[n]})
            k = sum(feas.values()); nfeas_hist[k] = nfeas_hist.get(k, 0) + 1
        print(f"m={m}: {N} samples, failures={bad}, #feasible-layerings histogram={dict(sorted(nfeas_hist.items()))}", flush=True)

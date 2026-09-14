"""Horn-LP dual certificates for each exposed form of the (m,3) stratum at (m,z), d=m+z+3 <= 9.
Usage: python m3_horn_duals.py m z [prefix]   (uses cand_/forms_ json files; forms filtered by validity+radius)"""
import sys, json, glob, pickle, numpy as np
from fractions import Fraction as Q
from scipy.optimize import linprog
from m3_tools import JointLP, radius
from m3_forms import spec_m3

def load_forms(m, z, prefix):
    out = {}
    for fn in glob.glob(f"{prefix}_m{m}_z*.json"):
        for k, v in json.load(open(fn)).items():
            out[tuple(int(Q(x)) for x in eval(k))] = 1
    cands = sorted(out); J = JointLP(m, z)
    valid = []
    for f in cands:
        v = J.validity(np.array(f, float))[0]
        if v is not None and v > -1e-9: valid.append(f)
    exp = []
    for f in valid:
        t, arg = radius(np.array(f, float), [np.array(g, float) for g in valid if g != f], m, strict=True)
        if t is not None and t > 1e-9: exp.append((f, arg))
    return exp

def horn_rows(d):
    T = pickle.load(open(f"horn_d{d}.pkl", "rb")); rows = []; trip = []
    for r in range(1, d):
        for I, J, K in T[r]:
            a = np.zeros(d - 1)
            for i in I:
                if i < d: a[i - 1] += 1
            for j in J:
                if j > 1: a[d - j] -= 1
            b = np.zeros(d)
            for k in K: b[k - 1] += 1
            rows.append((a, b)); trip.append((I, J, K))
    return rows, trip

def horn_lp_dual(lam, rows):
    d = len(lam); A = [-a for a, b in rows]; ub = [-(b @ lam) for a, b in rows]
    for j in range(d - 2):
        e = np.zeros(d - 1); e[j] = -1; e[j + 1] = 1; A.append(e); ub.append(0.0)
    res = linprog(np.ones(d - 1), A_ub=np.array(A), b_ub=np.array(ub), bounds=[(0, None)] * (d - 1), method='highs')
    return res.fun, res.x, -res.ineqlin.marginals

def sform(I, J, K, d):
    lhs = {}
    for i in I:
        if i < d: lhs[i] = lhs.get(i, 0) + 1
    for j in J:
        if j > 1: lhs[d + 1 - j] = lhs.get(d + 1 - j, 0) - 1
    lhs = {k: v for k, v in sorted(lhs.items()) if v != 0}
    return " ".join(f"{'+' if v>0 else '-'}{abs(v) if abs(v)!=1 else ''}s{k}" for k, v in lhs.items())

if __name__ == "__main__":
    m, z = int(sys.argv[1]), int(sys.argv[2]); prefix = sys.argv[3] if len(sys.argv) > 3 else 'cand'
    d = m + z + 3; rows, trip = horn_rows(d)
    exp = load_forms(m, z, prefix)
    print(f"m={m} z={z} d={d}: {len(exp)} exposed forms; {len(trip)} Horn triples")
    for f, (a, b) in exp:
        lam = spec_m3(a, b, z); val, s, y = horn_lp_dual(lam, rows)
        fv = float(np.dot(f[:m], a) + f[m] * b[0] + f[m + 1] * b[1])
        print(f"--- form {list(f)}  LP={val:.6f} form={fv:.6f}  a={np.round(a,3)} b={np.round(b,3)}  s={np.round(s,3)}")
        for r, t in enumerate(trip):
            if y[r] > 1e-9:
                I, J, K = t
                print(f"    y={y[r]:.3f}  I={I} J={J} K={K}  ->  {sform(I,J,K,d)} >= lam{list(K)}")
        for j in range(d - 2):
            if y[len(trip) + j] > 1e-9: print(f"    y={y[len(trip)+j]:.3f}  ordering s_{j+1}>=s_{j+2}")

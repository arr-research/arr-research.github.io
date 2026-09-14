"""Tiling certificates for every exposed form of the (m,3) stratum at (m,z), d = m+z+3 (d <= 12), from the restricted
catalogue LP (tiles = Horn triples with s-form +s[U] -s[N]); exact integer check that the tiles' right sides sum to the form
(canonical coordinates, using sum a = sum b), multipliers = 1, each s_t used at most once; LR >= 1 by lr.py AND lr2.py;
T^d_r membership by Fulton's recursion for d <= 9.  Output: certs_m{m}_z{z}.json and a log.
Usage: python certs.py m z"""
import sys, json, pickle, os, time, numpy as np
from fractions import Fraction as Q
from scipy.optimize import linprog
from catalogue import tile_rows
from restricted import restricted_lp
from m3_tools import radius
from m3_forms import spec_m3
from lr import lr, part, strip
from lr2 import lr2

def rhs_vec(K, m, z, d):
    """coefficient vector (a_1..a_m, b_1, b_2, b_3) of sum_{k in K} lambda_k."""
    v = [0] * (m + 3)
    for k in K:
        if k <= m: v[k - 1] += 1
        elif k > m + z: v[m + (d - k)] -= 1   # k = d -> -b_1 -> index m+0 ; k = d-1 -> -b_2 ; k = d-2 -> -b_3
    return v

def canon(v, m):
    """(a coeffs, b_1, b_2, b_3) -> canonical (alpha - beta3, beta1 - beta3, beta2 - beta3) via sum a = sum b (add t*(sum a - sum b), t = -beta3)."""
    t = -v[m + 2]
    return tuple(x - t for x in v[:m]) + (v[m] + t, v[m + 1] + t)

def s_coeffs(I, J, d):
    c = [0] * (d + 1)
    for i in I:
        if i < d: c[i] += 1
    for j in J:
        if j > 1: c[d + 1 - j] -= 1
    return c

if __name__ == "__main__":
    m, z = int(sys.argv[1]), int(sys.argv[2]); d = m + z + 3; t0 = time.time()
    S = [tuple(f) for f in json.load(open(f"closed_m{m}_z{0 if z == 0 else 1}.json"))]
    rows = tile_rows(m, z, m + 2, maxholes=3, maxN=3)
    # Candidate-2: build the optional Fulton membership lists in memory; no supplied pickle is loaded.
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "reviewer"))
    from horn_own import T
    horn = {r: T(r, d) for r in range(1, d)} if d <= 9 else None
    hornset = set(t for r in horn for t in horn[r]) if horn else None
    print(f"m={m} z={z} d={d}: {len(S)} exposed forms, {len(rows)} catalogue tiles ({time.time()-t0:.0f}s)", flush=True)
    out = {}; nbad = 0; sigs = {}
    for g in S:
        others = [np.array(h, float) for h in S if h != g]
        rad, (a, b) = radius(np.array(g, float), others, m, strict=True)
        lam = spec_m3(a, b, z); val, s, y = restricted_lp(lam, rows)
        gv = float(np.dot(g[:m], a) + g[m] * b[0] + g[m + 1] * b[1])
        used = [(r, y[r]) for r in range(len(rows)) if y[r] > 1e-7]
        tot = [0] * (m + 3); scoef = [0] * (d + 1); ok = True; tiles = []
        for r, yr in used:
            A_, B_, (K, U, N, I, J) = rows[r]
            if abs(yr - 1) > 1e-6: ok = False; print(f"  form {list(g)}: multiplier {yr} != 1 on tile {(K,U,N)}")
            v = rhs_vec(K, m, z, d); tot = [x + w for x, w in zip(tot, v)]
            c = s_coeffs(I, J, d); scoef = [x + w for x, w in zip(scoef, c)]
            lI, lJ, lK = part(I), part(J), part(K)
            c1 = lr(lI, lJ, lK); c2 = lr2(lI, lJ, lK)
            inT = (I, J, K) in hornset if hornset is not None else None
            if c1 < 1 or c2 < 1 or c1 != c2 or inT is False: ok = False; print(f"  form {list(g)}: LR/T problem {I,J,K} c1={c1} c2={c2} inT={inT}")
            Ka = tuple(k for k in K if k <= m); Kb = tuple({d: 1, d - 1: 2, d - 2: 3}[k] for k in K if k > m + z)
            Noff = tuple(d - t for t in N)
            tiles.append(dict(K=K, U=U, N=N, I=I, J=J, Ka=Ka, Kb=Kb, Noff=Noff, lamI=strip(lI), lamJ=strip(lJ), lamK=strip(lK), lr=c1, inT=inT))
        if canon(tot, m) != g: ok = False; print(f"  form {list(g)}: tile sum {canon(tot, m)} != form")
        if any(scoef[t] > 1 for t in range(1, d)): ok = False; print(f"  form {list(g)}: s-coefficient > 1: {scoef}")
        if abs(val - gv) > 1e-8: ok = False; print(f"  form {list(g)}: restricted LP value {val} != form value {gv} at centre")
        if not ok: nbad += 1
        out[str(list(g))] = dict(ok=ok, centre=dict(a=list(a), b=list(b)), tiles=tiles, s_used=[t for t in range(1, d) if scoef[t] == 1], s_neg=[t for t in range(1, d) if scoef[t] < 0])
        sig = tuple(sorted((t['Ka'], t['Kb'], t['U'], t['Noff']) for t in tiles))
        sigs[g] = sig
    json.dump(out, open(f"certs_m{m}_z{z}.json", "w"), indent=1, default=lambda o: list(o) if isinstance(o, tuple) else o)
    types = {}
    for g in S:
        for t in out[str(list(g))]['tiles']:
            lJ = t['lamJ']; kind = 'LW' if not lJ else ('row' if len(lJ) == 1 else ('col' if all(x == 1 for x in lJ) else 'other'))
            types[kind] = types.get(kind, 0) + 1
    print(f"RESULT m={m} z={z} d={d}: {len(S)-nbad}/{len(S)} forms certified (multipliers 1, each s_t <= once, tiles sum exactly to the form, LR>=1 by lr and lr2{', in T^d_r' if hornset else ''}); tile types {types}; max s index used {max(max(out[str(list(g))]['s_used']) for g in S)}  ({time.time()-t0:.0f}s)")

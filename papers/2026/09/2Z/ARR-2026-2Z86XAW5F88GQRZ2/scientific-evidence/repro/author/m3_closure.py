"""Closure loop: starting from the candidate forms of (m,z), iterate {validity+exposedness filter -> chamber-vertex completeness ->
at every gap vertex, add the hive-LP dual form} until no gap remains. Writes closed_m{m}_z{z}.json (final exposed set).
Usage: python m3_closure.py m z [prefix]"""
import sys, json, glob, time, numpy as np
from fractions import Fraction as Q
from m3_tools import JointLP, radius, chamber_vertices, chamber_vertices_qhull, form_val
from hive_core import HiveLP, rat
from m3_forms import spec_m3, canon

def filt(cands, m, z):
    J = JointLP(m, z); valid = []
    for f in cands:
        v = J.validity(np.array(f, float))[0]
        if v is not None and v > -1e-9: valid.append(f)
    exp = []
    for f in valid:
        t, arg = radius(np.array(f, float), [np.array(g, float) for g in valid if g != f], m)
        if t is not None and t > 1e-9: exp.append(f)
    return exp

if __name__ == "__main__":
    m, z = int(sys.argv[1]), int(sys.argv[2]); prefix = sys.argv[3] if len(sys.argv) > 3 else 'cand'
    d = m + z + 3; M = HiveLP(d); t0 = time.time()
    cands = set()
    for fn in glob.glob(f"{prefix}_m{m}_z*.json"):
        for k, v in json.load(open(fn)).items(): cands.add(tuple(int(Q(x)) for x in eval(k)))
    it = 0
    while True:
        it += 1; S = filt(sorted(cands), m, z); new = set(); worst = 0; nv = 0
        for g in S:
            others = [np.array(h, float) for h in S if h != g]
            V = (chamber_vertices if m <= 4 else chamber_vertices_qhull)(np.array(g, float), others, m); nv += len(V)
            for a, b in V:
                lam = spec_m3(a, b, z); r = M.solve(lam); gap = r['val'] - form_val(np.array(g, float), a, b)
                worst = max(worst, gap)
                if gap > 1e-8:
                    # perturb slightly into the chamber interior direction to get a generic dual, then rationalise
                    for eps in (0.0, 1e-4, 1e-3):
                        a2 = np.abs(a + eps * np.random.default_rng(1).normal(size=m)); b2 = np.abs(b + eps * np.random.default_rng(2).normal(size=3))
                        a2 = np.sort(a2)[::-1]; b2 = np.sort(b2)[::-1]; a2 /= a2.sum(); b2 /= b2.sum()
                        r2 = M.solve(spec_m3(a2, b2, z)); f = canon(r2['grad'], m, z); key = tuple(rat(x, 2000) for x in f)
                        if all(k.denominator == 1 for k in key): new.add(tuple(int(k) for k in key))
        print(f"iter {it}: {len(S)} exposed forms, {nv} vertices, max gap {worst:.2e}, {len(new - cands)} new forms ({time.time()-t0:.0f}s)", flush=True)
        if not (new - cands): break
        cands |= new
    json.dump([list(f) for f in S], open(f"closed_m{m}_z{z}.json", "w"))
    print(f"RESULT m={m} z={z}: {len(S)} exposed forms, complete (max gap {worst:.2e})")

"""Completeness certificate (floating LP) of a form set S for (m,z): for each exposed form g in S, enumerate the vertices of its
chamber C_g (within the P=1 stratum) and check kappa_d(v) = g(v) at every vertex. Since kappa_d - g is convex on C_g and >= 0,
equality at all vertices implies kappa_d = g on C_g; the chambers cover the stratum => kappa_d = max S.
Usage: python m3_complete.py m z [prefix]"""
import sys, json, glob, time, numpy as np
from fractions import Fraction as Q
from m3_tools import JointLP, radius, chamber_vertices, chamber_vertices_qhull, form_val
from hive_core import HiveLP
from m3_forms import spec_m3

def exposed_forms(m, z, prefix='cand'):
    out = {}
    for fn in glob.glob(f"{prefix}_m{m}_z*.json"):
        for k, v in json.load(open(fn)).items(): out[tuple(int(Q(x)) for x in eval(k))] = 1
    cands = sorted(out); J = JointLP(m, z); valid = []
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
    t0 = time.time(); S = exposed_forms(m, z, prefix); d = m + z + 3; M = HiveLP(d)
    print(f"m={m} z={z} d={d}: {len(S)} exposed forms ({time.time()-t0:.0f}s)")
    worst = 0; nv_tot = 0
    for g in S:
        others = [np.array(h, float) for h in S if h != g]
        V = (chamber_vertices if m <= 4 else chamber_vertices_qhull)(np.array(g, float), others, m); nv_tot += len(V)
        for a, b in V:
            r = M.solve(spec_m3(a, b, z)); gap = r['val'] - form_val(np.array(g, float), a, b)
            if gap > worst: worst = gap
            if gap > 1e-8: print(f"  GAP {gap:.3e} at form {list(g)} vertex a={np.round(a,4)} b={np.round(b,4)}")
        print(f"  form {list(g)}: {len(V)} vertices, ok", flush=True)
    print(f"RESULT m={m} z={z}: {nv_tot} chamber vertices, max(kappa - form) = {worst:.2e}  ({time.time()-t0:.0f}s)")

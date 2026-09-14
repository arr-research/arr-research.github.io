"""For given m and pad list: union of candidate forms over pads (files cand_/forms_ m{m}_z{z}.json), then for each z:
validity LP (min kappa_d - f over stratum), and radius of each valid form relative to the other valid forms.
Usage: python m3_analyze.py m pads [prefix=cand]"""
import sys, json, glob, numpy as np
from fractions import Fraction as Q
from m3_tools import JointLP, radius

m = int(sys.argv[1]); pads = [int(x) for x in sys.argv[2].split(',')]
prefix = sys.argv[3] if len(sys.argv) > 3 else 'cand'
def load(z):
    out = {}
    for fn in glob.glob(f"{prefix}_m{m}_z{z}.json"):
        for k, v in json.load(open(fn)).items():
            key = tuple(int(Q(x)) for x in eval(k)); out[key] = out.get(key, 0) + v['n']
    return out
cands = {}
counts = {z: load(z) for z in pads}
for z in pads:
    for k in counts[z]: cands[k] = 1
cands = sorted(cands)
print(f"m={m}: {len(cands)} distinct candidate forms over pads {pads}")
valid = {}
for z in pads:
    J = JointLP(m, z); v = []
    for f in cands:
        val, arg = J.validity(np.array(f, float))
        if val is not None and val > -1e-9: v.append(f)
        elif val is not None and val > -1e-6: print("   borderline", z, f, val)
    valid[z] = v
    print(f"  z={z} (d={m+z+3}): {len(v)} valid of {len(cands)}")
# exposedness: radius wrt the other valid forms in the same z
for z in pads:
    exp = []
    for f in valid[z]:
        others = [g for g in valid[z] if g != f]
        t, arg = radius(np.array(f, float), [np.array(g, float) for g in others], m)
        if t is not None and t > 1e-9: exp.append((f, t))
    print(f"  z={z}: exposed (radius>0 among valid): {len(exp)}")
    for f, t in sorted(exp, key=lambda x: -x[1]):
        print(f"     {list(f)}  r={t:.4f}  count={counts[z].get(f,0)}")

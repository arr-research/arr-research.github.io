import json, sys
from collections import defaultdict
def layering(f, m):
    al = f[:m]; be = list(f[m:]) + [0]
    w3 = max(al); v = [w3 - x for x in al]; w = [x + w3 for x in be]; T = max(w); lay = []
    for t in range(T, -1, -1):
        L = [f"b{i+1}" for i in range(3) if w[i] == t] + [f"a{j+1}" for j in range(m) if v[j] == t]
        lay.append(L)
    return lay, tuple(w), tuple(v)
for m in range(int(sys.argv[1]), int(sys.argv[2])+1):
    z = 1
    forms = json.load(open(f"closed_m{m}_z{z}.json"))
    groups = defaultdict(list)
    for f in forms:
        lay, w, v = layering(f, m)
        # b-schedule: layer index (from start) of each b: T - w
        T = len(lay) - 1
        groups[tuple(T - x for x in w)].append((lay, f))
    print(f"=== m={m}: {len(forms)} forms, {len(groups)} b-schedules")
    for key in sorted(groups):
        print(f"  b-layers {key}: {len(groups[key])}")
        for lay, f in sorted(groups[key], key=lambda t: t[1]):
            print("      " + " ".join("{" + ",".join(L) + "}" for L in lay) + "   " + str(f))

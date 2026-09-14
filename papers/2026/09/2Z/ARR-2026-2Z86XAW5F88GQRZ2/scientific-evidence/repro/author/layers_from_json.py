import json, sys
m = int(sys.argv[1]); z = int(sys.argv[2]) if len(sys.argv) > 2 else 1
forms = json.load(open(f"closed_m{m}_z{z}.json"))
def layering(f):
    al = f[:m]; be = list(f[m:]) + [0]
    w3 = max(al); v = [w3 - x for x in al]; w = [x + w3 for x in be]; T = max(w); lay = []
    for t in range(T, -1, -1):
        L = [f"b{i+1}" for i in range(3) if w[i] == t] + [f"a{j+1}" for j in range(m) if v[j] == t]
        lay.append("{" + ",".join(L) + "}")
    return " ".join(lay)
out = sorted((layering(f), f) for f in forms)
for s, f in out: print(f"{str(f):36s} {s}")

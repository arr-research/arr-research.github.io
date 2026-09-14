"""Print each exposed form (from analyze log) as a layering: w3 = max alpha, v_j = w3 - alpha_j (level of a_j from the end),
w_i = beta_i + w3 (level of b_i from the end). Layer t (from the end) contains a_j with v_j = t and b_i with w_i = t."""
import sys, re
fn = sys.argv[1]; zsel = sys.argv[2]
txt = open(fn).read()
sec = txt.split(f"  z={zsel}: exposed")[1].split("\n  z=")[0]
forms = [eval(l.strip().split("]")[0] + "]") for l in sec.strip().split("\n")[1:] if l.strip().startswith("[")]
m = len(forms[0]) - 2
def layering(f):
    al = f[:m]; be = list(f[m:]) + [0]
    w3 = max(al); v = [w3 - x for x in al]; w = [x + w3 for x in be]
    T = max(w)
    lay = []
    for t in range(T, -1, -1):
        L = [f"b{i+1}" for i in range(3) if w[i] == t] + [f"a{j+1}" for j in range(m) if v[j] == t]
        lay.append("{" + ",".join(L) + "}")
    return " ".join(lay), max(len(l.split(",")) for l in lay)
out = []
for f in forms:
    s, mx = layering(f)
    out.append((mx, s, f))
for mx, s, f in sorted(out):
    print(f"{str(f):32s} maxlayer={mx}  {s}")

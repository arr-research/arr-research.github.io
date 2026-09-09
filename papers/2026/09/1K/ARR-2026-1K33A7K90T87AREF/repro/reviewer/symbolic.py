"""Symbolic checks (sympy): tail-sum forms == closed forms; F_k-F_{k-1}=E_{k+1}-b2; G_j-F0=b2-E1+g_j; G_j-G_j'=g_j-g_j';
cost(layering)==form for the three layer families; m=2 vs 3M d=4 formula; m=3 vs 37B twelve terms (identification)."""
import sympy as sp, math

def setup(m):
    a = sp.symbols(f"a1:{m+1}", positive=True); b2 = sp.Symbol("b2", positive=True)
    b1 = sum(a) - b2
    A = lambda i: sum(a[i-1:]) if i <= m else sp.Integer(0)
    E = lambda i: sum(a[i-1::2]) if i <= m else sp.Integer(0)
    aa = list(a) + [sp.Integer(0)]
    g = lambda j: aa[j-1] - aa[j]
    def F(k):
        if k == 0: return sum(A(t) for t in range(1, m+1, 2))
        return b1 + sum(A(j) - b2 for j in range(2, k+1)) + sum(A(t) for t in range(k+1, m+1) if (t-k) % 2 == 1)
    def G(j):
        return b2 + sum(A(i) for i in range(2, j, 2)) + a[j-1] + A(j+2) + sum(A(i) for i in range(j+3, m+1) if i % 2 == 0)
    def Fc(k): return k*b1 + sum(((j-k) if j <= k else math.ceil((j-k)/2)) * a[j-1] for j in range(1, m+1))
    def Gc(j): return b2 + sum((i//2)*a[i-1] for i in range(1, m+1)) + (aa[j-1] - aa[j])
    return a, b1, b2, A, E, g, F, G, Fc, Gc

def cost(layers):
    tot = 0; Tr = 0
    for L in layers[:-1]:
        Tr -= sum(L); tot += Tr
    return sp.expand(tot)
def pairs(seq): return [list(seq[i:i+2]) for i in range(0, len(seq), 2)]

for m in range(2, 10):
    a, b1, b2, A, E, g, F, G, Fc, Gc = setup(m)
    for k in range(m): assert sp.expand(F(k) - Fc(k)) == 0
    for j in range(1, m+1, 2): assert sp.expand(G(j) - Gc(j)) == 0
    for k in range(1, m): assert sp.expand(F(k) - F(k-1) - (E(k+1) - b2)) == 0
    for j in range(1, m+1, 2):
        assert sp.expand(G(j) - F(0) - (b2 - E(1) + g(j))) == 0
        for jj in range(1, m+1, 2): assert sp.expand(G(j) - G(jj) - (g(j) - g(jj))) == 0
    assert sp.expand(E(1) - E(2) - sum(g(j) for j in range(1, m+1, 2))) == 0
    # layering costs
    assert sp.expand(cost(pairs([-b1, -b2] + list(a))) - F(0)) == 0
    for k in range(1, m):
        L = [[-b1]] + [[a[i]] for i in range(k-1)] + pairs([a[k-1], -b2] + list(a[k:]))
        assert sp.expand(cost(L) - F(k)) == 0
    for j in range(1, m+1, 2):
        seq = [-b1] + list(a)
        if j + 1 <= m:
            seq[j], seq[j+1] = seq[j+1], seq[j]; L = [[-b2]] + pairs(seq)
        else:
            L = [[-b2]] + pairs(seq[:m-1]) + [[a[m-2]], [a[m-1]]]
        assert sp.expand(cost(L) - G(j)) == 0, (m, j)
    # one-spike limit b2 -> 0 : F_{m-1} = sum j a_j
    assert sp.expand(F(m-1).subs(b2, 0) - sum((j+1)*a[j] for j in range(m))) == 0
    print(f"m={m}: tail-sum==closed forms, chamber differences, layering costs, one-spike limit: all identities hold symbolically")

# m=2 vs 3M
a, b1, b2, A, E, g, F, G, Fc, Gc = setup(2)
l = [a[0], a[1], -b2, -b1]
terms3M = [l[0]-l[2], l[1]-l[3], l[0]-2*l[1]-l[2], l[1]+2*l[2]-l[3]]
print("m=2: 3M terms in (a,b):", [sp.expand(t) for t in terms3M], " forms F1,G1,F0:", sp.expand(F(1)), sp.expand(G(1)), sp.expand(F(0)))
print("   l1-l3 - G1 =", sp.expand(terms3M[0]-G(1)), "; l2-l4 - F1 =", sp.expand(terms3M[1]-F(1)),
      "; (l1-2l2-l3) - G1 =", sp.expand(terms3M[2]-G(1)), "(<=0 since a2>0); (l2+2l3-l4) - F1 =", sp.expand(terms3M[3]-F(1)), "(<=0)")
print("   F0 - F1 =", sp.expand(F(0)-F(1)), "; F0 - G1 =", sp.expand(F(0)-G(1)), " -> F0 <= max(F1,G1) since (a1-b1)+(a2-b2)=0")
# m=3 vs 37B twelve terms
a, b1, b2, A, E, g, F, G, Fc, Gc = setup(3)
l1, l2, l3, l4, l5 = a[0], a[1], a[2], -b2, -b1
tw = {"2l1-2l2-l3+l5": 2*l1-2*l2-l3+l5, "-l1+l3+2l4-2l5": -l1+l3+2*l4-2*l5, "l1-l3-l4": l1-l3-l4, "l2+l3-l5": l2+l3-l5,
      "l2-2l3-l4": l2-2*l3-l4, "l2+2l3-l4": l2+2*l3-l4, "2l1-l3+l5": 2*l1-l3+l5, "-l1+l3-2l5": -l1+l3-2*l5,
      "l1+l2-l3": l1+l2-l3, "l3-l4-l5": l3-l4-l5, "l1+l3-l4": l1+l3-l4, "l2-l3-l5": l2-l3-l5}
forms = {"F0": F(0), "F1": F(1), "F2": F(2), "G1": G(1), "G3": G(3)}
for name, t in tw.items():
    match = [fn for fn, f in forms.items() if sp.expand(t - f) == 0]
    print(f"   37B term {name:16s} = {sp.expand(t)}   matches {match}")

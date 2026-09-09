"""Own re-derivation of the lower-bound certificates from the recipe in explore_A2 sections 2.2/2.3,
checked with the reviewer's own LR (bialternant) and own Fulton generator (d<=9)."""
import sys, itertools
from fractions import Fraction as Q
from my_horn import T, lr as lr_bialt, part, horn_lhs_s
def lr(lam, mu, nu):
    # exact fast paths (Pieri rule) for the only shapes occurring in the certificates; general case = bialternant
    lam = tuple(x for x in lam if x); mu = tuple(x for x in mu if x); nu = tuple(x for x in nu if x)
    if not mu: return 1 if lam == nu else 0
    if not lam: return 1 if mu == nu else 0
    if mu == (1,):
        n = max(len(lam), len(nu)); l = lam + (0,)*(n-len(lam)); v = nu + (0,)*(n-len(nu))
        diff = [v[i]-l[i] for i in range(n)]
        return 1 if all(x >= 0 for x in diff) and sum(diff) == 1 else 0
    return lr_bialt(lam, mu, nu)

def lam_forms(m, z):
    d = m + z + 2; L = []
    for k in range(1, d + 1):
        if k <= m: L.append({f"a{k}": Q(1)})
        elif k <= m + z: L.append({})
        elif k == d - 1: L.append({"b2": Q(-1)})
        else: L.append({"b1": Q(-1)})
    return L
def add(f, g, c=1):
    h = dict(f)
    for k, v in g.items(): h[k] = h.get(k, 0) + c * v
    return {k: v for k, v in h.items() if v != 0}
def canon(f, m):   # eliminate b1 = sum a - b2  (different elimination than the author's, on purpose)
    f = dict(f)
    if "b1" in f:
        c = f.pop("b1")
        for j in range(1, m + 1): f[f"a{j}"] = f.get(f"a{j}", 0) + c
        f["b2"] = f.get("b2", 0) - c
    return {k: v for k, v in f.items() if v != 0}

# forms in tail-sum notation (document, section 1)
def A(m, i): return {f"a{k}": Q(1) for k in range(i, m + 1)}
def F_form(m, k):
    if k == 0:
        f = {}
        for t in range(1, m + 1, 2): f = add(f, A(m, t))
        return f
    f = {"b1": Q(1)}
    for j in range(2, k + 1): f = add(f, add(A(m, j), {"b2": Q(-1)}))
    for t in range(k + 1, m + 1):
        if (t - k) % 2 == 1: f = add(f, A(m, t))
    return f
def G_form(m, j):
    f = {"b2": Q(1)}
    for i in range(2, j, 2): f = add(f, A(m, i))
    f = add(f, {f"a{j}": Q(1)}); f = add(f, A(m, j + 2))
    for i in range(j + 3, m + 1):
        if i % 2 == 0: f = add(f, A(m, i))
    return f

def lidskii(K, d): return (tuple(K), tuple(range(1, len(K) + 1)), tuple(K))
def weyl_s2(d): I = tuple(range(1, d)); J = tuple(x for x in range(1, d + 1) if x != d - 1); return (I, J, J)
def pieri(i, d): return ((i - 1,) + tuple(range(i + 1, d - 1)), tuple(range(1, d - i - 1)) + (d - i,), tuple(range(i, d - 1)))

def cert(name, m, z):
    d = m + z + 2; out = []
    def pair(t):
        if t <= m - 1: out.append(("Pi_%d" % t, lidskii(range(t, d - 1), d)))
        else: out.append(("Weyl s_m>=a_m", lidskii((m,), d)))
    if name[0] == "F":
        k = int(name[1:])
        if k == 0:
            for t in range(1, m + 1, 2): pair(t)
        else:
            out.append(("s1>=b1", lidskii(range(1, d), d)))
            for j in range(2, k + 1): out.append(("T_%d" % j, lidskii(range(j, d), d)))
            for t in range(k + 1, m + 1, 2): pair(t)
    else:
        j = int(name[1:])
        out.append(("s2>=b2", weyl_s2(d)))
        for i in range(2, j, 2): out.append(("Pieri_%d" % i, pieri(i, d)))
        if j + 2 <= m: out.append(("B_%d" % j, lidskii((j,) + tuple(range(j + 2, d - 1)), d)))
        else: out.append(("Weyl s_j>=a_j", lidskii((j,), d)))
        for t in range(j + 3, m + 1, 2): pair(t)
    return out

def check(name, m, z, verbose=False):
    d = m + z + 2; L = lam_forms(m, z)
    target = canon(F_form(m, int(name[1:])) if name[0] == "F" else G_form(m, int(name[1:])), m)
    lhs = {}; rhs = {}
    for label, (I, J, K) in cert(name, m, z):
        r = len(I); assert len(J) == r == len(K)
        assert sum(I) + sum(J) == sum(K) + r * (r + 1) // 2, (name, m, z, label)
        c = lr(part(I), part(J), part(K)); assert c >= 1, (name, m, z, label, I, J, K)
        if d <= 8: assert (I, J, K) in set(T(r, d)), ("Fulton", name, m, z, label)
        sf = horn_lhs_s(I, J, d); rh = {}
        for k in K: rh = add(rh, L[k - 1])
        lhs = add(lhs, sf); rhs = add(rhs, rh)
        if verbose:
            print(f"   [{label}] I={I} J={J} K={K}  LR={c}  :  " + " ".join(f"{'+' if v>0 else '-'}{abs(v)}s{k}" for k, v in sorted(sf.items())) + "  >=  " + str(rh))
    assert all(v <= 1 for v in lhs.values()), (name, m, z, lhs)
    assert canon(rhs, m) == target, (name, m, z, canon(rhs, m), target)
    coef_gt_m = {t: v for t, v in lhs.items() if t > m}
    if verbose:
        print("   SUM:", " ".join(f"{'+' if v>0 else '-'}{abs(v)}s{k}" for k, v in sorted(lhs.items())), " >= ", rhs, "\n   = form", target, "(b1 eliminated)")
        print("   coefficients of s_t, t>m:", coef_gt_m)
    return coef_gt_m

if __name__ == "__main__":
    for m in (4,):
        for name in ("F2", "G3"):
            for z in (0, 1, 5):
                print(f"=== {name}, m={m}, z={z}, d={m+z+2}")
                check(name, m, z, verbose=True)
    print("\n=== systematic check m<=7, z in {0,1,2,5}; report certificates where some s_t (t>m) has coefficient +1 (rank-m loophole)")
    n = 0; loop = []
    for m in range(2, 8):
        for z in (0, 1, 2, 5):
            names = [f"F{k}" for k in range(m)] + [f"G{j}" for j in range(1, m + 1, 2)]
            for name in names:
                cg = check(name, m, z); n += 1
                if any(v == 1 for v in cg.values()): loop.append((m, z, name, cg))
    print("certificates checked:", n)
    print("loophole certificates (coefficient +1 on some s_t, t>m):")
    for x in loop: print("  ", x)

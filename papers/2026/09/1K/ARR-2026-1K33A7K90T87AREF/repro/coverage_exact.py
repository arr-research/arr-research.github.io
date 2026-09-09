"""Exact-arithmetic coverage check of Theorem A / Theorem B / Proposition 5.4 / Theorem C'(3),(4) on a fine rational grid
for 2 <= m <= MMAX (default 10), including every tie and boundary case:
  - a-vectors: all-equal, strictly decreasing, equal pairs, one dominant a_1, one dominant odd gap g_j for each odd j,
    geometric, random with small denominators (many ties), a_m tiny;
  - b_2 values: every breakpoint E_k (2<=k<=m), E_1 - g_j (odd j), P/2 (b_1 = b_2), the midpoints between consecutive
    breakpoints, a uniform grid of N points in (0, P/2], and b_2 -> 0+ (P/10^6).
Checks at every point (all in fractions.Fraction):
  (i)   cost(layering X) == form X for all layerings (Section 5.1);
  (ii)  feasible(layering X) <=> closed-form region of Proposition 5.4, for every X;
  (iii) some feasible layering exists and its form equals Phi (Proposition 5.5, Theorem A);
  (iv)  the chamber description of Theorem B (F_{k*} / F_0 / G_{j*}) and the unimodality/ordering identities;
  (v)   Theorem C'(3): for m odd, the layering L'_m (zero inside the penultimate layer) is feasible iff b_2 >= E_1 - a_m,
        and the sigma_2-interval before the layer {a_{m-1}, 0} has positive upper end iff b_2 > E_1 - a_m;
  (vi)  Theorem C'(4): for m >= 4 in the open F_{m-3} chamber with a_{m-2} > a_{m-1}, the sigma_2-interval after the
        mixed layer has upper end h > a_{m-1} (a nondegenerate family of optimal spectra);
  (vii) the corrected statement of Section 6: some G_j attains Phi at some grid point iff sum_{j' != j*} g_{j'} <= g_{j*}.
Run: python coverage_exact.py [MMAX] [N]   (defaults 10, 40; about 60 s)."""
import sys, random, itertools, time
from fractions import Fraction as Q
from layer_chain import layerings, feasible, cost, forms
from my_construct import forward

def E(a, i): return sum(a[i - 1::2]) if i <= len(a) else Q(0)
def A(a, i): return sum(a[i - 1:]) if i <= len(a) else Q(0)
def gaps(a):
    aa = list(a) + [Q(0)]; return {j: aa[j - 1] - aa[j] for j in range(1, len(a) + 1, 2)}
def region(name, a, b2):
    g = gaps(a); gs = max(g.values())
    if name == "F0": return E(a, 2) <= b2 <= E(a, 1) - gs
    if name[0] == "F": k = int(name[1:]); return E(a, k + 2) <= b2 <= E(a, k + 1)
    return b2 >= E(a, 1) - g[int(name[1:])]

def a_vectors(m, rng):
    out = [[Q(1)] * m, [Q(m - i) for i in range(m)], [Q((m - i + 1) // 2) for i in range(m)]]          # flat, strict, equal pairs
    out.append([Q(10)] + [Q(1)] * (m - 1))                                                              # dominant a_1
    for j in range(1, m + 1, 2): out.append([Q(1)] * j + [Q(1, 7)] * (m - j))                           # dominant odd gap g_j
    out.append([Q(1, 2 ** i) for i in range(m)]); out.append([Q(1)] * (m - 1) + [Q(1, 10 ** 6)])       # geometric, tiny a_m
    for _ in range(12): out.append(sorted([Q(rng.randint(1, 4), rng.choice([1, 2, 3])) for _ in range(m)], reverse=True))
    return [[Q(x) for x in a] for a in out]

def b2_values(a, N):
    P = sum(a); g = gaps(a)
    bp = sorted(set([E(a, k) for k in range(2, len(a) + 1)] + [E(a, 1) - g[j] for j in g] + [P / 2]))
    bp = [x for x in bp if 0 < x <= P / 2]
    vals = set(bp) | {(x + y) / 2 for x, y in zip(bp, bp[1:])} | {P * Q(i, 2 * N) for i in range(1, N + 1)} | {P / 10 ** 6}
    if bp: vals.add(bp[0] / 2)
    return sorted(vals)

def main(MMAX, N):
    rng = random.Random(20260908); total = 0; t0 = time.time()
    for m in range(2, MMAX + 1):
        gact = {}
        for a in a_vectors(m, rng):
            P = sum(a); g = gaps(a); gs = max(g.values()); jstar = [j for j in g if g[j] == gs]
            cond_c = sum(g[j] for j in g if j != jstar[0]) <= gs        # (vii) hypothesis
            g_seen = False
            for b2 in b2_values(a, N):
                b1 = P - b2; assert b1 >= b2 > 0; b = (b1, b2)
                lay = layerings(a, b); fv = forms(a, b); phi = max(fv.values()); total += 1
                feas = {n: feasible(L) for n, L in lay.items()}
                for n in lay:
                    assert cost(lay[n]) == fv[n], ("(i) cost", m, n, a, b2)                                 # (i)
                    assert feas[n] == region(n, a, b2), ("(ii) region", m, n, a, b2, feas[n])              # (ii)
                    if feas[n]: assert fv[n] == phi, ("(iii) feasible but below Phi", m, n, a, b2)
                assert any(feas.values()), ("(iii) no feasible layering", m, a, b2)                          # (iii)
                if b2 <= E(a, 2):                                                                             # (iv)
                    ks = max(k for k in range(1, m) if E(a, k + 1) >= b2); assert fv[f"F{ks}"] == phi
                    assert E(a, ks + 2) <= b2 <= E(a, ks + 1)
                elif b2 <= E(a, 1) - gs: assert fv["F0"] == phi
                else: assert all(fv[f"G{j}"] == phi for j in jstar)
                for k in range(1, m): assert (fv[f"F{k}"] >= fv[f"F{k-1}"]) == (E(a, k + 1) >= b2)
                for j in g: assert (fv[f"G{j}"] >= fv["F0"]) == (b2 >= E(a, 1) - g[j])
                if any(fv[f"G{j}"] == phi for j in g): g_seen = True
                if m % 2 == 1:                                                                                # (v)
                    Lp = [[-b2], [-b1, a[0]]] + [[a[i], a[i + 1]] for i in range(1, m - 2, 2)] + [[a[m - 2], Q(0)], [a[m - 1]]]
                    st = forward(Lp); assert cost(Lp) == fv[f"G{m}"]
                    assert (st is not None) == (b2 >= E(a, 1) - a[m - 1]), ("(v) L'_m feasibility", m, a, b2)
                    if st is not None:
                        h = st[-2][2]          # state of S_{T-1}: the sigma_2-interval before the layer {a_{m-1}, 0}
                        assert (h > 0) == (b2 > E(a, 1) - a[m - 1]), ("(v) rank m+1 attainable iff strict", m, a, b2, h)
                if m >= 4 and a[m - 3] > a[m - 2] and E(a, m - 1) < b2 < E(a, m - 2):                        # (vi)
                    st = forward(lay[f"F{m-3}"]); assert st is not None
                    h = st[m - 3][2]           # state of S_{m-2} on the mixed layer {a_{m-3}, -b_2}
                    assert h == min(b2, A(a, m - 2) - b2) and h > a[m - 2], ("(vi)", m, a, b2, h)
            gact[tuple(a)] = (cond_c, g_seen)
        for a, (c, seen) in gact.items():
            assert c == seen, ("(vii) G-activity", m, a, c, seen)                                            # (vii)
        print(f"m={m}: {len(gact)} a-vectors, checks (i)-(vii) passed at all grid points so far ({total} points, {time.time()-t0:.0f} s)", flush=True)
    print(f"ALL COVERAGE CHECKS PASSED: {total} exact points, m <= {MMAX}")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 10, int(sys.argv[2]) if len(sys.argv) > 2 else 40)

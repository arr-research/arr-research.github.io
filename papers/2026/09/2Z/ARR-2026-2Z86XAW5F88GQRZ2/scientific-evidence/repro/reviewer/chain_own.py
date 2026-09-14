"""Task (b): independent, EXACT (rational) re-check of the upper-bound step for m = 3..6, z = 0,1,2:
- chamber vertices of every exposed form by pycddlib (gmp, exact) on the polytope {stratum, P=1, g >= h for all h in S};
- level layering of g (own implementation), 3x3 chain feasibility LP in exact arithmetic (cdd gmp) with the Horn inequalities of
  size <= 3 taken from the reviewer's own T^n_r; candidates: base layering, and with 1 or 2 zeros inserted (z >= 1);
- reports which chambers need a zero, vertex counts, and the exact result at each vertex.
Usage: python chain_own.py m_max"""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, itertools, time
from fractions import Fraction as Q
import cdd.gmp as g
sys.path.insert(0, AUTHOR_DIR)
from horn_own import T
W = AUTHOR_DIR

HORN = {n: [(I, J, K) for r in range(1, n) for (I, J, K) in T(r, n)] for n in (1, 2, 3)}

def chamber_vertices_exact(gform, others, m):
    """Polytope in x = (a_1..a_m, b_1, b_2, b_3): sum a = 1, sum b = 1, a ordered >= 0, b ordered >= 0, g - h >= 0. Returns exact vertices."""
    n = m + 3; rows = []; lin = []
    def row(const, coef): return [Q(const)] + [Q(c) for c in coef]
    rows.append(row(-1, [1] * m + [0, 0, 0])); lin.append(0)
    rows.append(row(-1, [0] * m + [1, 1, 1])); lin.append(1)
    for j in range(m - 1):
        c = [0] * n; c[j] = 1; c[j + 1] = -1; rows.append(row(0, c))
    c = [0] * n; c[m - 1] = 1; rows.append(row(0, c))
    for j in range(2):
        c = [0] * n; c[m + j] = 1; c[m + j + 1] = -1; rows.append(row(0, c))
    c = [0] * n; c[m + 2] = 1; rows.append(row(0, c))
    for h in others:
        c = [gform[j] - h[j] for j in range(m)] + [gform[m] - h[m], gform[m + 1] - h[m + 1], 0]; rows.append(row(0, c))
    M = g.matrix_from_array(rows, lin_set=lin, rep_type=g.RepType.INEQUALITY)
    P = g.polyhedron_from_matrix(M); G = g.copy_generators(P)
    verts = []
    for gen in G.array:
        if gen[0] == 1: verts.append(tuple(gen[1:]))
        else: raise RuntimeError("unbounded direction found")
    return verts

def layering(gform, m):
    """Level layering: symbolic layers (list of lists of ('a',j)/('b',i)), from layer of highest level (index 0) downwards."""
    al = list(gform[:m]); be = list(gform[m:m + 2]) + [0]; w3 = max(al)
    lev_a = [w3 - x for x in al]; lev_b = [x + w3 for x in be]; Tm = max(lev_b)
    assert min(lev_a) == 0 and min(lev_b) >= 0
    lay = []
    for t in range(Tm, -1, -1):
        lay.append([('b', i) for i in range(3) if lev_b[i] == t] + [('a', j) for j in range(m) if lev_a[j] == t])
    return lay

def with_zeros(base, nz):
    slots = [t for t in range(len(base)) if len(base[t]) < 3]; out = []
    for combo in itertools.combinations_with_replacement(slots, nz):
        new = [list(L) for L in base]; ok = True
        for t in combo:
            if len(new[t]) >= 3: ok = False; break
            new[t].append(('z', 0))
        if ok: out.append(new)
    return out

def inst(chain, a, b):
    return [[(-b[i] if k == 'b' else (a[i] if k == 'a' else Q(0))) for (k, i) in L] for L in chain]

def chain_feasible_exact(layers):
    """Exact LP feasibility of the 3x3 block-shift chain (variables sigma^(t)_k, t=1..T, k=1..3)."""
    Tn = len(layers) - 1; n = [len(L) for L in layers]; nv = 3 * Tn
    def var(t, k): return (t - 1) * 3 + (k - 1)
    ineq = []; eq = []   # rows [const, coef...] meaning const + coef.x >= 0 (ineq) or = 0 (eq)
    def R(const, coefs):
        r = [Q(0)] * (nv + 1); r[0] = Q(const)
        for v, c in coefs: r[v + 1] += Q(c)
        return r
    for t in range(1, Tn + 1):
        for k in (1, 2, 3): ineq.append(R(0, [(var(t, k), 1)]))
        for k in (1, 2): ineq.append(R(0, [(var(t, k), 1), (var(t, k + 1), -1)]))
        cap = min(n[t - 1], n[t])
        for k in range(cap + 1, 4): eq.append(R(0, [(var(t, k), 1)]))
    s1 = sorted([-x for x in layers[0]], reverse=True) + [Q(0)] * (3 - n[0])
    if any(x < 0 for x in s1): return False
    for k in range(1, 4): eq.append(R(-s1[k - 1], [(var(1, k), 1)]))
    for t in range(1, Tn):
        nt = n[t]; beta = sorted([-x for x in layers[t]], reverse=True)
        eq.append(R(-sum(beta), [(var(t + 1, k), 1) for k in range(1, nt + 1)] + [(var(t, k), -1) for k in range(1, nt + 1)]))
        for I, J, K in HORN[nt]:
            # sum_K gamma <= sum_I alpha + sum_J beta  ->  sum_J beta + sum_I alpha - sum_K gamma >= 0
            ineq.append(R(sum(beta[j - 1] for j in J), [(var(t, i), 1) for i in I] + [(var(t + 1, k), -1) for k in K]))
    sT = sorted(layers[Tn], reverse=True) + [Q(0)] * (3 - n[Tn])
    if any(x < 0 for x in sT): return False
    for k in range(1, 4): eq.append(R(-sT[k - 1], [(var(Tn, k), 1)]))
    rows = ineq + eq; lin = list(range(len(ineq), len(rows)))
    M = g.matrix_from_array(rows, lin_set=lin, rep_type=g.RepType.INEQUALITY)
    M.obj_type = g.LPObjType.MAX; M.obj_func = [Q(0)] * (nv + 1)
    lp = g.linprog_from_matrix(M); g.linprog_solve(lp)
    return lp.status == g.LPStatusType.OPTIMAL

def show(ch): return " ".join("{" + ",".join((f"b{i+1}" if k == 'b' else (f"a{i+1}" if k == 'a' else "0")) for k, i in L) + "}" for L in ch)

if __name__ == "__main__":
    mmax = int(sys.argv[1]); zs = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [0, 1, 2]
    for m in range(3, mmax + 1):
        for z in zs:
            d = m + z + 3; t0 = time.time()
            S = [tuple(f) for f in json.load(open(f"{W}/closed_m{m}_z{0 if z == 0 else 1}.json"))]
            nv_tot = 0; allok = True; needzero = []
            for gform in S:
                others = [h for h in S if h != gform]
                V = chamber_vertices_exact(gform, others, m); nv_tot += len(V)
                base = layering(gform, m)
                cands = [base] + ([c for nz in range(1, min(z, 2) + 1) for c in with_zeros(base, nz)] if z >= 1 else [])
                good = None
                for ci, ch in enumerate(cands):
                    if all(chain_feasible_exact(inst(ch, v[:m], v[m:])) for v in V): good = ci; break
                if good is None: allok = False; print(f"  m={m} z={z} form {gform}: NO candidate chain feasible at all {len(V)} vertices", flush=True)
                elif good > 0: needzero.append((gform, show(cands[good])))
            print(f"m={m} z={z} d={d}: |S|={len(S)}, exact chamber vertices total {nv_tot}; every chamber covered by one chain: {allok}; "
                  f"chambers needing an inserted zero: {len(needzero)}  ({time.time()-t0:.0f}s)", flush=True)
            for f, s in needzero: print(f"   zero needed: {f} -> {s}")

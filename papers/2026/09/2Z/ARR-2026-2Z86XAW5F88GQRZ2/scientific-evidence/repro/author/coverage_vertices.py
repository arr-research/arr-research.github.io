"""Chamber coverage by 3x3 block-shift chains, checked at ALL chamber vertices (convexity of the chain-feasibility region in
lambda then gives the whole chamber).  For each exposed form g of (m,z): vertices of C_g (brute force m<=4, qhull m>=5),
candidate chains = the level layering of g with 0, 1 or 2 zeros inserted (z >= 1); report the chains feasible at every vertex.
Usage: python coverage_vertices.py m z"""
import sys, json, time, numpy as np
from m3_tools import chamber_vertices, chamber_vertices_qhull
from layering_lp import feasible, layering_of_form, with_zeros, cost
from hive_core import HiveLP
from m3_forms import spec_m3

m, z = int(sys.argv[1]), int(sys.argv[2]); d = m + z + 3; t0 = time.time()
S = [tuple(f) for f in json.load(open(f"closed_m{m}_z{0 if z == 0 else 1}.json"))]
M = HiveLP(d)
print(f"m={m} z={z} d={d}: {len(S)} exposed forms", flush=True)
summary = {}; allok = True; nv_tot = 0
for g in S:
    others = [np.array(h, float) for h in S if h != g]
    V = (chamber_vertices if m <= 4 else chamber_vertices_qhull)(np.array(g, float), others, m); nv_tot += len(V)
    # candidate chains: layer structure is fixed by g; zeros inserted in slots (positions independent of lambda)
    a0, b0 = V[0]
    L0 = layering_of_form(g, a0, b0, m)   # values at V[0], but we only use the SHAPE; rebuild per vertex below
    # represent a chain as (list of layers of symbolic entries): 'a{j}', 'b{i}', 'z'
    al = list(g[:m]); be = list(g[m:m + 2]) + [0]; w3 = max(al); lev_a = [w3 - x for x in al]; lev_b = [x + w3 for x in be]
    T = max(lev_b); base = []
    for t in range(T, -1, -1):
        base.append([('b', i) for i in range(3) if lev_b[i] == t] + [('a', j) for j in range(m) if lev_a[j] == t])
    cands = [base]
    if z >= 1:
        slots = [t for t in range(len(base)) if len(base[t]) < 3]
        import itertools
        for nz in range(1, min(z, 2) + 1):
            for combo in itertools.combinations_with_replacement(slots, nz):
                new = [list(L) for L in base]; ok = True
                for t in combo:
                    if len(new[t]) >= 3: ok = False; break
                    new[t].append(('z', 0))
                if ok: cands.append(new)
    def inst(chain, a, b):
        return [[(-b[i] if k == 'b' else (a[i] if k == 'a' else 0.0)) for (k, i) in L] for L in chain]
    good = []; per_vertex_any = 0
    fe = np.zeros((len(cands), len(V)), bool)
    for ci, ch in enumerate(cands):
        for vi, (a, b) in enumerate(V):
            fe[ci, vi] = feasible(inst(ch, a, b))
    for ci in range(len(cands)):
        if fe[ci].all(): good.append(ci)
    per_vertex_any = int(fe.any(axis=0).sum())
    # also check cost = form at a vertex and kappa = form (sanity)
    a, b = V[0]; c0 = cost(inst(base, a, b)); gv = float(np.dot(g[:m], a) + g[m] * b[0] + g[m + 1] * b[1])
    kap = M.solve(spec_m3(a, b, z))['val']
    def show(ch): return " ".join("{" + ",".join((f"b{i+1}" if k == 'b' else (f"a{i+1}" if k == 'a' else "0")) for k, i in L) + "}" for L in ch)
    status = "OK" if good else ("PARTIAL" if per_vertex_any == len(V) else "FAIL")
    if not good: allok = False
    print(f"  form {list(g)}: {len(V)} vertices; chains feasible at all vertices: {len(good)}/{len(cands)} "
          f"({'base' if 0 in good else ('zeros needed: ' + (show(cands[good[0]]) if good else 'NONE'))}); vertices covered by some chain: {per_vertex_any}/{len(V)}; "
          f"|cost-form|={abs(c0-gv):.1e} |kappa-form|={abs(kap-gv):.1e}  [{status}]", flush=True)
    summary[str(list(g))] = dict(status=status, nV=len(V), good=[show(cands[c]) for c in good], covered=per_vertex_any)
json.dump(summary, open(f"coverage_m{m}_z{z}.json", "w"), indent=1)
print(f"RESULT m={m} z={z} d={d}: {nv_tot} chamber vertices; every chamber covered by a single chain feasible at all its vertices: {allok}  ({time.time()-t0:.0f}s)")

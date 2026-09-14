"""Run the reviewer's exact chain check (chain_own.py) for m = 9 only, one z per process. Usage: python chain_m9.py z"""
import sys, json, time
import chain_own as co
z = int(sys.argv[1]); m = 9; d = m + z + 3; t0 = time.time()
S = [tuple(f) for f in json.load(open(f"{co.W}/closed_m{m}_z{0 if z == 0 else 1}.json"))]
nv_tot = 0; allok = True; needzero = []
for gform in S:
    others = [h for h in S if h != gform]
    V = co.chamber_vertices_exact(gform, others, m); nv_tot += len(V)
    base = co.layering(gform, m)
    cands = [base] + ([c for nz in range(1, min(z, 2) + 1) for c in co.with_zeros(base, nz)] if z >= 1 else [])
    good = None
    for ci, ch in enumerate(cands):
        if all(co.chain_feasible_exact(co.inst(ch, v[:m], v[m:])) for v in V): good = ci; break
    if good is None: allok = False; print(f"  m={m} z={z} form {gform}: NO candidate chain feasible at all {len(V)} vertices", flush=True)
    elif good > 0: needzero.append((gform, co.show(cands[good])))
    print(f"  form {gform}: {len(V)} exact vertices, chain index {good}  ({time.time()-t0:.0f}s)", flush=True)
print(f"m={m} z={z} d={d}: |S|={len(S)}, exact chamber vertices total {nv_tot}; every chamber covered by one chain: {allok}; "
      f"chambers needing an inserted zero: {len(needzero)}  ({time.time()-t0:.0f}s)", flush=True)
for f, s in needzero: print(f"   zero needed: {f} -> {s}")

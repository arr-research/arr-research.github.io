"""Parse duals_m{m}_z{z}.log files and print the distinct tiles (Horn inequalities used in certificates) with a
dimension-free signature: LHS as +s_i / -s_{d-k}, RHS as (a-indices, b-indices)."""
import re, glob, sys
def parse(fn):
    m, z = map(int, re.findall(r"duals_m(\d+)_z(\d+)", fn)[0]); d = m + z + 3
    tiles = set()
    for line in open(fn):
        mt = re.search(r"I=\((.*?)\) J=\((.*?)\) K=\((.*?)\)", line)
        if not mt: continue
        I, J, K = [tuple(int(x) for x in g.replace(" ", "").split(",") if x) for g in mt.groups()]
        lhs = {}
        for i in I:
            if i < d: lhs[i] = lhs.get(i, 0) + 1
        for j in J:
            if j > 1: lhs[d + 1 - j] = lhs.get(d + 1 - j, 0) - 1
        lhs = {k: v for k, v in lhs.items() if v}
        pos = tuple(sorted(k for k, v in lhs.items() if v > 0)); neg = tuple(sorted(k for k, v in lhs.items() if v < 0))
        assert all(abs(v) == 1 for v in lhs.values()), (fn, I, J, K, lhs)
        Ka = tuple(k for k in K if k <= m); Kb = tuple({d: 1, d - 1: 2, d - 2: 3}[k] for k in K if k >= d - 2)
        tiles.add((pos, neg, Ka, Kb, I, J, K))
    return m, z, d, tiles
if __name__ == "__main__":
    for fn in sorted(glob.glob("duals_m*_z*.log")):
        m, z, d, tiles = parse(fn)
        print(f"=== {fn}: m={m} z={z} d={d}: {len(tiles)} distinct tiles")
        def enc(idx): return ",".join(str(k) if k <= m + 2 else f"d-{d-k}" for k in idx)
        for pos, neg, Ka, Kb, I, J, K in sorted(tiles, key=lambda t: (len(t[0]), t[0], t[1])):
            rhs = "+".join(f"a{k}" for k in Ka) + "".join(f"-b{i}" for i in Kb)
            if len(Ka) == m and not Kb: rhs = "P"
            print(f"   +s[{enc(pos)}] -s[{enc(neg)}]  >=  {rhs:28s}   I={I} J={J} K={K}")

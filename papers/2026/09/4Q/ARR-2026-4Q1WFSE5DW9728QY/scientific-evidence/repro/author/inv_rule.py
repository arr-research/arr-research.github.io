"""Experiment 6: structural rules on the exposed forms of (m,n,z) (files forms_m{m}_n{n}_z{z}.json).
For each exposed form's level layering: q_u = # a's in layer u, c_u = # b's in layers < u (capacity), b-inv = # b-inversions,
a-inv = # pairs j<j' with t(a_j) > t(a_j') + sum_u (c_u - q_u)_+ * #{a's in layers > u}  (virtual slots count as +infinity,
as in the (m,3) manuscript's slot model).  Rules tested: (R1) q_u <= c_u for every layer u >= 1; (R2) a-inv = b-inv;
(R3) layer 0 pure b, last layer pure a; (R4) max layer size <= min(m, n); (R5) no empty layer.
Usage: python inv_rule.py "m,n,z;..." """
import sys, json
from mn_tools import *

def rules(L, m, n):
    t = {}
    for u, layer in enumerate(L):
        for x in layer: t[x] = u
    T = len(L) - 1
    sched = [t[('b', i)] for i in range(1, n + 1)]
    binv = sum(1 for i in range(n) for j in range(i + 1, n) if sched[i] > sched[j])
    ta = [t[('a', j)] for j in range(1, m + 1)]
    ainv = sum(1 for j in range(m) for jj in range(j + 1, m) if ta[j] > ta[jj])
    R1 = True; virt = 0
    for u in range(1, T + 1):
        c = sum(1 for s in sched if s < u); q = sum(1 for k, _ in L[u] if k == 'a')
        if q > c: R1 = False
        later = sum(1 for x in ta if x > u)
        virt += max(c - q, 0) * later
    ainv_v = ainv + virt
    R3 = all(k == 'b' for k, _ in L[0]) and all(k == 'a' for k, _ in L[-1])
    R4 = max(len(x) for x in L) <= min(m, n)
    R5 = all(len(x) > 0 for x in L)
    return dict(R1=R1, R2=(ainv_v == binv), R3=R3, R4=R4, R5=R5, binv=binv, ainv=ainv_v, sched=tuple(sched))

if __name__ == "__main__":
    cases = [tuple(int(x) for x in c.split(',')) for c in sys.argv[1].split(';')]
    for (m, n, z) in cases:
        data = json.load(open(f"forms_m{m}_n{n}_z{z}.json")); S = [tuple(json.loads(k)) for k in data if not k.startswith('_')]
        cnt = {k: 0 for k in ['R1', 'R2', 'R3', 'R4', 'R5']}; viol = {k: [] for k in cnt}
        for f in S:
            L = level_layering(f, m, n); r = rules(L, m, n)
            for k in cnt:
                if r[k]: cnt[k] += 1
                else: viol[k].append((f, show(L), r['ainv'], r['binv']))
        print(f"(m,n,z)=({m},{n},{z}): {len(S)} exposed forms; rules satisfied: " + ", ".join(f"{k}: {cnt[k]}/{len(S)}" for k in cnt))
        for k in cnt:
            for v in viol[k][:4]: print(f"    violates {k}: {list(v[0])} {v[1]} a-inv={v[2]} b-inv={v[3]}")

"""Conjectural family description (rules v2) of the exposed forms of kappa_d on inertia (m,3), z >= 1.
Layering = b-schedule (u1,u2,u3) + a-arrangement in capacity slots (c_u = number of b's in layers < u), virtual slots (0)
allowed after a_m.  Families:
  A(u2,u3): u1=0, 0<=u2<=u3, ordered a's; need C(u3) <= m-1 (a real a after b3's layer), u2 <= m-2 if u2>=1, m>=4 if (u2,u3)=(0,0).
  B(u2; j): u1=0, u3=u2-1>=0, one boundary transposition at a boundary after b2's layer.
  C(k; j): (1,0,k), k>=1, one boundary transposition at any boundary.
  D: (1,0,0): two boundary transpositions at distinct boundaries, or one forward 3-cycle (x,y|z)->(y,z|x) at a boundary.
  E: (1,1,0): two boundary transpositions, or one backward 3-cycle (x|y,z)->(z|x,y).
  F: (2,1,0): exactly the two arrangements (a3|a1,a4|a2,a5,a6|...) and (a2|a3,a4|a1,a5,a6|...).
Inversion count (virtual = +inf) must equal the number of b-inversions; the last layer must contain no b.
Usage: python families2.py m_min m_max [compare]"""
import sys, json, itertools
from families import layers_from, form_of, show, binv

INF = 10**6
def inversions(seq): return sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])

def slots_bounds(u, m, nvirt=3):
    cap = [sum(1 for i in range(3) if u[i] < t) for t in range(1, 200)]
    nslots = m + nvirt; bounds = []; c = 0; t = 0; layer_of_bound = {}
    while c < nslots:
        c += cap[t]; bounds.append(c); layer_of_bound[c] = t + 1; t += 1   # boundary after layer t+1
    return [b for b in bounds if b < nslots], layer_of_bound

def T(s, b): s = list(s); s[b - 1], s[b] = s[b], s[b - 1]; return tuple(s)
def F(s, b): s = list(s); s[b - 2], s[b - 1], s[b] = s[b - 1], s[b], s[b - 2]; return tuple(s)
def B(s, b):
    s = list(s)
    if b + 1 >= len(s): return None
    s[b - 1], s[b], s[b + 1] = s[b + 1], s[b - 1], s[b]; return tuple(s)

def gen2(m, nvirt=3, families=None):
    out = {}
    base = tuple(range(1, m + 1)) + (INF,) * nvirt
    def add(u, p, fam):
        if inversions(p) != binv(u): return
        lay = layers_from(u, m, list(p))
        if any(x[0] == 'b' for x in lay[-1]): return
        f = form_of(lay, m); out.setdefault(f, []).append((fam, u, lay))
    # A
    for u2 in range(0, m):
        for u3 in range(u2, m + 1):
            u = (0, u2, u3); C = 2 * u3 if u2 == 0 else 2 * u3 - u2
            if C > m - 1: continue
            if u2 >= 1 and u2 > m - 2: continue
            if (u2, u3) == (0, 0) and m < 4: continue
            add(u, base, 'A')
    # B
    for u2 in range(1, m + 1):
        u = (0, u2, u2 - 1); bounds, lob = slots_bounds(u, m, nvirt)
        for b in bounds:
            if lob[b] >= u2: add(u, T(base, b), 'B')
    # C
    for k in range(1, m + 1):
        u = (1, 0, k); bounds, lob = slots_bounds(u, m, nvirt)
        for b in bounds: add(u, T(base, b), 'C')
    # D
    u = (1, 0, 0); bounds, lob = slots_bounds(u, m, nvirt)
    for b1, b2 in itertools.combinations(bounds, 2): add(u, T(T(base, b1), b2), 'D')
    for b in bounds:
        if b >= 2: add(u, F(base, b), 'D')
    # E
    u = (1, 1, 0); bounds, lob = slots_bounds(u, m, nvirt)
    for b1, b2 in itertools.combinations(bounds, 2): add(u, T(T(base, b1), b2), 'E')
    for b in bounds:
        p = B(base, b)
        if p: add(u, p, 'E')
    # F
    u = (2, 1, 0)
    if m >= 2:
        p1 = list(base); p1[0], p1[1], p1[2], p1[3] = base[2], base[0], base[3], base[1]; add(u, tuple(p1), 'F')   # (3,1,4,2,...)
        p2 = list(base); p2[0], p2[1], p2[2], p2[3] = base[1], base[2], base[3], base[0]; add(u, tuple(p2), 'F')   # (2,3,4,1,...)
    return out

if __name__ == "__main__":
    m0, m1 = int(sys.argv[1]), int(sys.argv[2])
    for m in range(m0, m1 + 1):
        G = gen2(m); Gs = set(G)
        fam = {}
        for f, v in G.items(): fam[v[0][0]] = fam.get(v[0][0], 0) + 1
        dup = sum(1 for f, v in G.items() if len(v) > 1)
        line = f"m={m}: generated {len(Gs)} forms; per family {dict(sorted(fam.items()))}; forms with >1 layering: {dup}"
        try:
            truth = set(tuple(f) for f in json.load(open(f"closed_m{m}_z1.json")))
            line += f"; truth {len(truth)}, extra {len(Gs - truth)}, missing {len(truth - Gs)}"
            for f in sorted(truth - Gs): line += f"\n   MISSING {f}"
            for f in sorted(Gs - truth): line += f"\n   EXTRA {f} {G[f][0][0]} {show(G[f][0][2])}"
        except FileNotFoundError: pass
        print(line)
        if len(sys.argv) > 3:
            json.dump([list(f) for f in sorted(Gs)], open(f"pred_m{m}.json", "w"))

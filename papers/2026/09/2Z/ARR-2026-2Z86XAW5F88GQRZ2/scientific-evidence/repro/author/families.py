"""Conjectural generator of the exposed layerings of the (m,3) stratum (z >= 1 sets).
Model: b-schedule (u1,u2,u3) = layer indices of b1,b2,b3 (min = 0, u_i <= u_{i+1}+1); capacities c_u = #{i: u_i < u};
slots filled by a_1..a_m then virtual zeros; the a-arrangement is a permutation with #inversions (virtual = 0) equal to the
number of b-inversions (#{i<j : u_i > u_j}), built from boundary transpositions and 3-cycles as observed.
Usage: python families.py m_min m_max  -> compares with closed_m{m}_z1.json"""
import sys, json, itertools

def sched_list(m):
    out = []
    for u2 in range(0, m + 2):
        for u3 in range(max(0, u2 - 1), m + 2): out.append((0, u2, u3))
    for u3 in range(0, m + 2): out.append((1, 0, u3))
    out += [(1, 1, 0), (2, 1, 0)]
    return out

def binv(u):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if u[i] > u[j])

def layers_from(u, m, perm):
    """perm: list of slot contents (a-index 1..m or 0 = virtual) in slot order. Returns layers (list of lists of ('b',i)/('a',j))."""
    T = max(u); cap = [None] + [sum(1 for i in range(3) if u[i] < t) for t in range(1, 100)]
    lay = [[('b', i + 1) for i in range(3) if u[i] == 0]]
    pos = 0; t = 1
    while pos < len(perm) or t <= T:
        L = [('b', i + 1) for i in range(3) if u[i] == t]
        for _ in range(cap[t]):
            if pos < len(perm):
                if perm[pos] <= m: L.append(('a', perm[pos]))
                pos += 1
        lay.append(L); t += 1
    while lay and not lay[-1]: lay.pop()
    return lay

def form_of(lay, m):
    T = len(lay) - 1; lev = {}
    for t, L in enumerate(lay):
        for x in L: lev[x] = T - t
    lb3 = lev[('b', 3)]
    return tuple(lb3 - lev[('a', j)] for j in range(1, m + 1)) + (lev[('b', 1)] - lb3, lev[('b', 2)] - lb3)

def inversions(seq):
    return sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])

def gen(m, nvirt=3):
    out = {}
    for u in sched_list(m):
        T = max(u); cap = [sum(1 for i in range(3) if u[i] < t) for t in range(1, 100)]
        # slots and layer boundaries
        nslots = m + nvirt; bounds = []; c = 0; t = 0
        while c < nslots:
            c += cap[t]; bounds.append(c); t += 1
        bounds = [b for b in bounds if b < nslots]          # boundary after slot b (1-based count)
        base = list(range(1, m + 1)) + [10**6] * nvirt
        k = binv(u)
        perms = set(); how = {}
        if k == 0: perms.add(tuple(base)); how[tuple(base)] = ()
        moves = []
        for b in bounds:
            moves.append(('T', b))     # transposition slots b, b+1
            if b >= 2: moves.append(('F', b))   # forward 3-cycle (b-1, b | b+1) -> (b, b+1 | b-1)
            moves.append(('B', b))     # backward 3-cycle (b | b+1, b+2) -> (b+2 | b, b+1)
        def apply(seq, mv):
            s = list(seq); kind, b = mv
            if kind == 'T': s[b - 1], s[b] = s[b], s[b - 1]
            elif kind == 'F': s[b - 2], s[b - 1], s[b] = s[b - 1], s[b], s[b - 2]
            else:
                if b + 1 >= len(s): return None
                s[b - 1], s[b], s[b + 1] = s[b + 1], s[b - 1], s[b]
            return tuple(s)
        if k == 1:
            for mv in moves:
                if mv[0] == 'T':
                    s = apply(base, mv)
                    if s and inversions(s) == 1: perms.add(s); how.setdefault(s, (mv,))
        if k == 2:
            for mv1, mv2 in itertools.combinations([mv for mv in moves if mv[0] == 'T'], 2):
                s = apply(apply(base, mv1), mv2)
                if s and inversions(s) == 2: perms.add(s); how.setdefault(s, (mv1, mv2))
            for mv in moves:
                if mv[0] in ('F', 'B'):
                    s = apply(base, mv)
                    if s and inversions(s) == 2: perms.add(s); how.setdefault(s, (mv,))
        if k == 3:
            for mv1 in moves:
                s1 = apply(base, mv1)
                if s1 is None: continue
                for mv2 in moves:
                    s = apply(s1, mv2)
                    if s and inversions(s) == 3: perms.add(s); how.setdefault(s, (mv1, mv2))
        for p in perms:
            lay = layers_from(u, m, list(p))
            if any(x[0] == 'b' for x in lay[-1]): continue     # last layer must be pure a
            f = form_of(lay, m)
            out.setdefault(f, []).append((u, p, lay, how[p]))
    return out

def show(lay):
    return " ".join("{" + ",".join(f"{k}{i}" for k, i in L) + "}" for L in lay)

if __name__ == "__main__":
    m0, m1 = int(sys.argv[1]), int(sys.argv[2])
    for m in range(m0, m1 + 1):
        G = gen(m); truth = set(tuple(f) for f in json.load(open(f"closed_m{m}_z1.json")))
        Gs = set(G)
        print(f"m={m}: generated {len(Gs)} forms, truth {len(truth)}, common {len(Gs & truth)}, extra {len(Gs - truth)}, missing {len(truth - Gs)}")
        for f in sorted(truth - Gs): print("   MISSING", f)
        for f in sorted(Gs - truth): print("   EXTRA  ", f, [(g[0], show(g[2]), g[3]) for g in G[f]])

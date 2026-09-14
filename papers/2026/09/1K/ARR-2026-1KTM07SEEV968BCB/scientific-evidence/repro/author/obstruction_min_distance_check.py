"""obstruction_min_distance_check.py -- computational cross-check of Lemma N (min weight of N(p,k) >= 2p) for d = 8, 16 (p = 2)
and d = 9 (p = 3), independent of the proof: N = kernel of the fibre-sum parity-check matrix H (rows: cosets of primitive
cyclic subgroups).  Min weight >= 2p  <=>  every 2p-1 columns of H are linearly independent over F_p.
p = 2: columns as Python ints (bitmasks); no dependency among <= 3 columns <=> columns nonzero, distinct, and no c1^c2 = c3.
p = 3, d = 9: no dependency among <= 5 columns <=> no vector is both a (<=2)-combination and the negative of a
(<=3)-combination (meet in the middle over all coefficient choices in {1,2}).
"""
import sys, itertools

def factor_pk(d):
    p = 2
    while d % p: p += 1
    k = 0; dd = d
    while dd % p == 0: dd //= p; k += 1
    return p, k

def columns(d):
    p, k = factor_pk(d)
    dirs = [(1, s) for s in range(d)] + [(s, 1) for s in range(0, d, p)]
    labels = [(a, b) for a in range(d) for b in range(d)]
    cols = []
    for (a, b) in labels:
        col = []
        for (al, be) in dirs:
            t = (al*a + be*b) % d
            for tt in range(d): col.append(1 if tt == t else 0)
        cols.append(col)
    return p, k, labels, cols

for d in map(int, sys.argv[1:]):
    p, k, labels, cols = columns(d)
    if p == 2:
        ints = [int("".join(map(str, c)), 2) for c in cols]
        ok = all(ints) and len(set(ints)) == len(ints)
        S = set(ints); bad = None
        for i in range(len(ints)):
            for j in range(i+1, len(ints)):
                if ints[i] ^ ints[j] in S: bad = (labels[i], labels[j]); break
            if bad: break
        print(f"d={d}: columns nonzero & distinct: {ok}; no c_i + c_j = c_k: {bad is None} => min weight of N >= 4 = 2p: {ok and bad is None}")
    else:
        assert d == 9
        n = len(cols); L = len(cols[0])
        def add(u, v, cv):
            return tuple((x + cv*y) % p for x, y in zip(u, v))
        zero = tuple([0]*L)
        two = {}
        for i in range(n):
            for ci in (1, 2):
                v = add(zero, cols[i], ci); two.setdefault(v, (i, ci))
        for i in range(n):
            for j in range(i+1, n):
                for ci in (1, 2):
                    for cj in (1, 2):
                        v = add(add(zero, cols[i], ci), cols[j], cj); two.setdefault(v, (i, ci, j, cj))
        # dependency among <= 5 columns: v3 (<=3 cols) + v2 (<=2 cols) = 0, or v3 = 0 or v2 = 0 alone, disjoint index sets
        dep = None
        for key, val in two.items():
            if key == zero: dep = ("two-combination is zero", val); break
        if dep is None:
            for i in range(n):
                for j in range(i+1, n):
                    for l in range(j+1, n):
                        for ci, cj, cl in itertools.product((1, 2), repeat=3):
                            v = add(add(add(zero, cols[i], ci), cols[j], cj), cols[l], cl)
                            if v == zero: dep = ("three-combination zero", (i, j, l)); break
                            neg = tuple((-x) % p for x in v)
                            if neg in two:
                                idx = two[neg][0::2]
                                if not set(idx) & {i, j, l}: dep = ("3+2", (i, j, l), two[neg]); break
                        if dep: break
                    if dep: break
                if dep: break
            # also 3-combinations equal to a single column handled via two (single entries); 1+3 handled; 2+3 handled; 1+1..: in two
        print(f"d={d}: dependency among <= 5 columns over F_3: {dep} => min weight of N >= 6 = 2p: {dep is None}")
"""Explicit, LP-free certificate for the ordered family A (b-schedule (0,u2,u3), u2<=u3, no inversions), all m and z.
Tiles: for each b_i in layer 0 the Weyl tile s_i >= b_i (i = 1,2,3; triples (1..d-1;1..d-1;1..d-1), ((1..d-1); [d] minus {d-1}; [d] minus {d-1}),
((1..d-1); [d] minus {d-2}; [d] minus {d-2})), and for each layer u >= 1 with a-indices (t..t+q-1) the Lidskii-Wielandt tile I=K=(t..d) minus B_u,
J=(1..r), B_u = spectrum indices of the b's placed in layers < u, whose s-form is s_t+...+s_{t+|B_u|-1} - sum_{beta in B_u, beta<d} s_beta,
truncated (LW tile with K=(t..m)) or replaced by Weyl tiles s_j >= a_j when fewer than |B_u| a-indices remain.
Exact checks (integer arithmetic): each triple satisfies the sum condition, LR coefficient = 1 (lr2), s-coefficients <= 1 and
disjoint, sum of right sides = the family-A form. Usage: python familyA_cert.py m_max z_max"""
import sys, itertools
from lr2 import lr2
from lr import part, strip
from families2 import gen2
from families import form_of

def canon(v, m):
    t = -v[m + 2]; return tuple(x - t for x in v[:m]) + (v[m] + t, v[m + 1] + t)

def rhs_vec(K, m, z, d):
    v = [0] * (m + 3)
    for k in K:
        if k <= m: v[k - 1] += 1
        elif k > m + z: v[m + (d - k)] -= 1
    return v

def s_coeffs(I, J, d):
    c = [0] * (d + 1)
    for i in I:
        if i < d: c[i] += 1
    for j in J:
        if j > 1: c[d + 1 - j] -= 1
    return c

def check_triple(I, J, K, d):
    """Sum condition; LR coefficient: lambda(J) = 0 (Lidskii-Wielandt, I = K) gives c = 1 by definition of the LR rule
    (c^nu_{lambda,0} = [lambda = nu]); Weyl-type tiles with lambda(J) a single box are checked by lr2; for d <= 9 all triples
    are additionally checked by lr2."""
    r = len(I); assert len(J) == r == len(K)
    assert sum(I) + sum(J) == sum(K) + r * (r + 1) // 2, (I, J, K)
    lI, lJ, lK = strip(part(I)), strip(part(J)), strip(part(K))
    if not lJ:
        assert lI == lK, (I, J, K); c = 1
    else:
        c = lr2(lI, lJ, lK)
    if d <= 9: assert lr2(lI, lJ, lK) == c
    assert c == 1, (I, J, K, c); return c

def certificate_A(u, lay, m, z):
    """One tile per tail: tail_u = sum of layers >= u (u = 1..T). B_u = spectrum indices of b's in layers < u, t_u = smallest
    a-index in layers >= u. Tile = Lidskii-Wielandt I=K=(t_u..d)\B_u, J=(1..r) with s-form s_{t_u}+..+s_{t_u+|B_u|-1} - sum_{B_u\{d}} s;
    when t_u+|B_u|-1 > m+z (last layer, fewer a's than capacity) Weyl tiles s_j >= a_j for the remaining a's instead."""
    d = m + z + 3; bidx = {1: d, 2: d - 1, 3: d - 2}
    tiles = []; placed = set()
    for uu in range(0, len(lay) - 1):
        placed |= set(i for kind, i in lay[uu] if kind == 'b')          # b's in layers <= uu = layers < uu+1
        rest = [i for L in lay[uu + 1:] for kind, i in L if kind == 'a']
        t = min(rest); q = len(placed); B = set(bidx[i] for i in placed)
        if t + q - 1 <= m + z:
            K = tuple(k for k in range(t, d + 1) if k not in B); tiles.append((K, tuple(range(1, len(K) + 1)), K))
        else:
            assert uu + 1 == len(lay) - 1, "partial layer that is not the last"
            for j in rest: tiles.append(((j,), (1,), (j,)))
    return tiles

if __name__ == "__main__":
    mmax, zmax = int(sys.argv[1]), int(sys.argv[2]); tot = 0
    for m in range(3, mmax + 1):
        G = gen2(m); nA = 0
        for f, v in G.items():
            fam, u, lay = v[0]
            if fam != 'A': continue
            for z in range(0, zmax + 1):
                d = m + z + 3; tiles = certificate_A(u, lay, m, z); tot_rhs = [0] * (m + 3); sc = [0] * (d + 1)
                for I, J, K in tiles:
                    check_triple(I, J, K, d)
                    tot_rhs = [x + y for x, y in zip(tot_rhs, rhs_vec(K, m, z, d))]
                    sc = [x + y for x, y in zip(sc, s_coeffs(I, J, d))]
                assert canon(tot_rhs, m) == f, (m, z, u, f, canon(tot_rhs, m))
                assert all(sc[t] <= 1 for t in range(1, d)), (m, z, u, sc)
                tot += 1
            nA += 1
        print(f"m={m}: {nA} family-A forms, certificates verified exactly for z = 0..{zmax} (LR = 1 via lr2, sum condition, disjoint indices, exact form sum)", flush=True)
    print(f"TOTAL {tot} (form, z) certificates verified")

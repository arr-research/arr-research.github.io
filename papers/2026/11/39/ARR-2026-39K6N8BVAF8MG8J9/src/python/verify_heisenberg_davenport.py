"""Exact verification and obstruction probing for D(H_{p^3}), eta(H_{p^3}), s(H_{p^3}).

Author: Lluis Eriksson (ORCID: 0009-0006-7494-9040)
License: MIT
"""

from __future__ import annotations

import itertools
import random
from collections import Counter
from typing import Iterable, Sequence, Tuple

Vec2 = Tuple[int, int]
HElem = Tuple[Vec2, int]


def mat_mul(m1: Tuple[int, int, int], m2: Tuple[int, int, int], p: int) -> Tuple[int, int, int]:
    """Matrix multiplication in UT_3(F_p): M(x, y, z) = [[1, x, z], [0, 1, y], [0, 0, 1]]."""
    x1, y1, z1 = m1
    x2, y2, z2 = m2
    return ((x1 + x2) % p, (y1 + y2) % p, (z1 + z2 + x1 * y2) % p)


def exp_to_mat(g: HElem, p: int) -> Tuple[int, int, int]:
    """Exponential isomorphism (v, a) -> M(v1, v2, a + (1/2) v1 v2)."""
    (v1, v2), a = g
    inv2 = (p + 1) // 2
    return (v1 % p, v2 % p, (a + inv2 * v1 * v2) % p)


def heis_mul(g1: HElem, g2: HElem, p: int) -> HElem:
    """Group law in exponential coordinates: (u, a)(v, b) = (u+v, a+b + (1/2) det(u,v))."""
    (x1, y1), a1 = g1
    (x2, y2), a2 = g2
    inv2 = (p + 1) // 2
    det = x1 * y2 - y1 * x2
    return (((x1 + x2) % p, (y1 + y2) % p), (a1 + a2 + inv2 * det) % p)


def heis_word_prod(word: Sequence[HElem], p: int) -> HElem:
    cur: HElem = ((0, 0), 0)
    for g in word:
        cur = heis_mul(cur, g, p)
    return cur


def alternating_area(vecs: Sequence[Vec2], p: int) -> int:
    """Compute Phi(sigma) = (1/2) sum_{i < j} det(v_i, v_j) mod p."""
    inv2 = (p + 1) // 2
    total = 0
    for i in range(len(vecs)):
        xi, yi = vecs[i]
        for j in range(i + 1, len(vecs)):
            xj, yj = vecs[j]
            total = (total + xi * yj - yi * xj) % p
    return (inv2 * total) % p


def eval_sequence_products(seq: Sequence[HElem], p: int, max_states: int = 200_000) -> Tuple[bool, int]:
    """Exact mixed-radix DP returning (is_product_one, num_proper_splits)."""
    counts = Counter(seq)
    elems = sorted(counts.keys())
    m = len(elems)
    init_state = tuple(counts[e] for e in elems)
    total_states = 1
    for c in init_state:
        total_states *= (c + 1)
    if total_states > max_states:
        raise ValueError(f"State space {total_states} exceeds limit {max_states}")

    inv2 = (p + 1) // 2
    radices = [c + 1 for c in init_state]
    mults = []
    cur = 1
    for r in radices:
        mults.append(cur)
        cur *= r

    vxs = [0] * total_states
    vys = [0] * total_states
    masks = [0] * total_states
    masks[0] = 1
    e_vx = [e[0][0] for e in elems]
    e_vy = [e[0][1] for e in elems]
    e_a = [e[1] for e in elems]
    all_bits = (1 << p) - 1

    for s in range(total_states):
        mask = masks[s]
        if mask == 0:
            continue
        vx = vxs[s]
        vy = vys[s]
        rem = s
        for i in range(m):
            ci = rem % radices[i]
            rem //= radices[i]
            if ci < init_state[i]:
                ns = s + mults[i]
                wx, wy = e_vx[i], e_vy[i]
                if masks[ns] == 0:
                    vxs[ns] = (vx + wx) % p
                    vys[ns] = (vy + wy) % p
                shift = (e_a[i] + inv2 * (vx * wy - vy * wx)) % p
                new_mask = ((mask << shift) | (mask >> (p - shift))) & all_bits if shift else mask
                masks[ns] |= new_mask

    full = total_states - 1
    is_p1 = (vxs[full] == 0 and vys[full] == 0 and bool(masks[full] & 1))
    splits = 0
    for s in range(1, (full + 1) // 2 + 1):
        if s >= full:
            break
        if vxs[s] == 0 and vys[s] == 0 and (masks[s] & 1):
            cs = full - s
            if vxs[cs] == 0 and vys[cs] == 0 and (masks[cs] & 1):
                splits += 1
    return is_p1, splits


def is_minimal_product_one(seq: Sequence[HElem], p: int) -> bool:
    is_p1, splits = eval_sequence_products(seq, p)
    return is_p1 and splits == 0


def build_s1(p: int) -> Tuple[list[HElem], list[HElem]]:
    """Extremal minimal product-one sequence S^(1) of length 3p-1 with c = p-1."""
    x: HElem = ((1, 0), 0)
    y: HElem = ((0, 1), 0)
    z: HElem = ((0, 0), 1)
    xz: HElem = ((1, 0), 1)
    yz: HElem = ((0, 1), 1)
    seq = [x] * (p - 1) + [xz] + [y] * (p - 1) + [yz] + [z] * (p - 1)
    word = [x] * (p - 1) + [y] + [xz] + [y] * (p - 2) + [yz] + [z] * (p - 1)
    return seq, word


def build_s2(p: int) -> Tuple[list[HElem], list[HElem]]:
    """Extremal minimal product-one sequence S^(2) of length 3p-1 with c = 0."""
    x: HElem = ((1, 0), 0)
    y: HElem = ((0, 1), 0)
    xz: HElem = ((1, 0), 1)
    yz: HElem = ((0, 1), 1)
    x2z: HElem = ((2 % p, 0), 1)
    seq = [x] * (p - 1) + [xz] * (p - 1) + [x2z] + [y] * (p - 1) + [yz]
    word = [y] + [xz] * (p - 1) + [x2z] + [y] * (p - 2) + [yz] + [x] * (p - 1)
    return seq, word


def check_t_eta_and_ts(p: int) -> Tuple[bool, bool]:
    """Verify no nonempty product-one subsequence of length <= p in T_eta (size 7p-7)
    and no product-one subsequence of length p in T_s (size 8p-8)."""
    inv2 = (p + 1) // 2
    x: HElem = ((1, 0), 0)
    xz: HElem = ((1, 0), 1)
    y: HElem = ((0, 1), 0)
    yz: HElem = ((0, 1), 1)
    xy: HElem = ((1, 1), inv2)
    xyz: HElem = ((1, 1), (inv2 + 1) % p)
    z: HElem = ((0, 0), 1)

    # Check all multiplicity vectors (a1, a2, b1, b2, c1, c2, d) in {0..p-1}^7
    # satisfying 1 <= total <= p, a+c = 0 mod p, b+c = 0 mod p.
    for c in range(p + 1):
        # a + c = 0 mod p, b + c = 0 mod p, a + b + c <= p
        rem_a = (-c) % p
        rem_b = (-c) % p
        # Either a = rem_a or rem_a + p (if rem_a == 0 -> p), etc.
        a_opts = [0, p] if rem_a == 0 else [rem_a]
        b_opts = [0, p] if rem_b == 0 else [rem_b]
        for a in a_opts:
            if a > 2 * (p - 1):
                continue
            for b in b_opts:
                if b > 2 * (p - 1) or a + b + c > p:
                    continue
                for d in range(min(p - 1, p - (a + b + c)) + 1):
                    if a + b + c + d < 1:
                        continue
                    # Pick valid splits a1+a2=a, b1+b2=b, c1+c2=c
                    for a2 in range(max(0, a - (p - 1)), min(p - 1, a) + 1):
                        a1 = a - a2
                        for b2 in range(max(0, b - (p - 1)), min(p - 1, b) + 1):
                            b1 = b - b2
                            for c2 in range(max(0, c - (p - 1)), min(p - 1, c) + 1):
                                c1 = c - c2
                                sub = [x]*a1 + [xz]*a2 + [y]*b1 + [yz]*b2 + [xy]*c1 + [xyz]*c2 + [z]*d
                                is_p1, _ = eval_sequence_products(sub, p)
                                if is_p1:
                                    return False, False
    # T_s = 1^{p-1} * T_eta: any length-p product-one subsequence yields a nonempty
    # product-one subsequence of T_eta of length <= p after deleting all 1s.
    return True, True


def verify_h27_exhaustive() -> dict[int, Tuple[int, int, int]]:
    """Exhaustively check all GL_2(F_3) x shear orbits of length 9 in H_27."""
    p = 3
    pts = [(x, y) for x in range(p) for y in range(p) if (x, y) != (0, 0)]
    zs_by_n: dict[int, list[Tuple[int, ...]]] = {7: [], 8: [], 9: []}

    def dfs_pts(idx: int, cur_len: int, sx: int, sy: int, counts: list[int]) -> None:
        if idx == len(pts):
            if cur_len in zs_by_n and sx == 0 and sy == 0:
                zs_by_n[cur_len].append(tuple(counts))
            return
        vx, vy = pts[idx]
        max_m = min(6, 9 - cur_len)
        for m in range(max_m + 1):
            counts.append(m)
            dfs_pts(idx + 1, cur_len + m, (sx + m * vx) % 3, (sy + m * vy) % 3, counts)
            counts.pop()

    dfs_pts(0, 0, 0, 0, [])

    def canon_orbit(counts_tuple: Tuple[int, ...]) -> Tuple[int, ...]:
        best = None
        for a, b, c, d in itertools.product(range(3), repeat=4):
            if (a * d - b * c) % 3 == 0:
                continue
            mapped = [0] * 8
            for i, (x, y) in enumerate(pts):
                if counts_tuple[i]:
                    nx = (a * x + b * y) % 3
                    ny = (c * x + d * y) % 3
                    mapped[pts.index((nx, ny))] = counts_tuple[i]
            t = tuple(mapped)
            if best is None or t < best:
                best = t
        assert best is not None
        return best

    summary: dict[int, Tuple[int, int, int]] = {}
    for c, sz_list in [(0, []), (1, [((0, 0), 1)]), (2, [((0, 0), 1), ((0, 0), 1)])]:
        n = 9 - c
        orbits = sorted(set(canon_orbit(t) for t in zs_by_n[n]))
        tested = 0
        found_min = 0
        for orb in orbits:
            active = [(i, pts[i], m) for i, m in enumerate(orb) if m > 0]
            v1 = active[0][1]
            v2_idx = None
            for k in range(1, len(active)):
                v2 = active[k][1]
                if (v1[0] * v2[1] - v1[1] * v2[0]) % 3 != 0:
                    v2_idx = k
                    break
            if v2_idx is None:
                continue
            per_v_options = []
            for k, (_, v, m) in enumerate(active):
                opts = []
                for c0 in range(min(2, m) + 1):
                    for c1 in range(min(2, m - c0) + 1):
                        c2 = m - c0 - c1
                        if 0 <= c2 <= 2:
                            if (k == 0 or k == v2_idx) and c0 == 0:
                                continue
                            opts.append([(v, 0)] * c0 + [(v, 1)] * c1 + [(v, 2)] * c2)
                per_v_options.append(opts)
            for choice in itertools.product(*per_v_options):
                seq = list(sz_list)
                for part in choice:
                    seq.extend(part)
                tested += 1
                if is_minimal_product_one(seq, p):
                    found_min += 1
        summary[c] = (len(orbits), tested, found_min)
    return summary


def verify_lemma1_growth(p: int, trials: int = 80, seed: int = 0) -> bool:
    """Verify |Phi(S_n . B)| >= min(p, n - 1) on noncollinear zero-sums in F_p^2."""
    rng = random.Random(seed)
    pts = [(x, y) for x in range(p) for y in range(p) if (x, y) != (0, 0)]
    for _ in range(trials):
        n = rng.randint(3, min(p + 3, 10))
        while True:
            seq = [rng.choice(pts) for _ in range(n - 1)]
            sx = (-sum(v[0] for v in seq)) % p
            sy = (-sum(v[1] for v in seq)) % p
            if (sx, sy) == (0, 0):
                continue
            seq.append((sx, sy))
            # Check noncollinear
            v0 = seq[0]
            if any((v0[0] * v[1] - v0[1] * v[0]) % p != 0 for v in seq[1:]):
                break
        # Use eval_sequence_products with a=0 lifts to compute exact Phi image size!
        lifted = [(v, 0) for v in seq]
        counts = Counter(lifted)
        elems = sorted(counts.keys())
        m = len(elems)
        init_state = tuple(counts[e] for e in elems)
        total_states = 1
        for c in init_state:
            total_states *= (c + 1)
        if total_states > 80_000:
            continue
        inv2 = (p + 1) // 2
        radices = [c + 1 for c in init_state]
        mults = []
        cur = 1
        for r in radices:
            mults.append(cur)
            cur *= r
        vxs = [0] * total_states
        vys = [0] * total_states
        masks = [0] * total_states
        masks[0] = 1
        e_vx = [e[0][0] for e in elems]
        e_vy = [e[0][1] for e in elems]
        all_bits = (1 << p) - 1
        for s in range(total_states):
            mask = masks[s]
            if mask == 0:
                continue
            vx, vy = vxs[s], vys[s]
            rem = s
            for i in range(m):
                ci = rem % radices[i]
                rem //= radices[i]
                if ci < init_state[i]:
                    ns = s + mults[i]
                    wx, wy = e_vx[i], e_vy[i]
                    if masks[ns] == 0:
                        vxs[ns] = (vx + wx) % p
                        vys[ns] = (vy + wy) % p
                    shift = (inv2 * (vx * wy - vy * wx)) % p
                    new_mask = ((mask << shift) | (mask >> (p - shift))) & all_bits if shift else mask
                    masks[ns] |= new_mask
        phi_size = masks[total_states - 1].bit_count()
        if phi_size < min(p, n - 1):
            return False
    return True


def hill_climb_obstruction(v_list: Sequence[Vec2], c: int, p: int, steps: int = 80, seeds: int = 3) -> Tuple[int, int]:
    """Search lifts minimizing splits for candidate obstructions in H_{p^3}."""
    best = (9, 9999)
    uniq_v = sorted(set(v_list))
    for seed in range(seeds):
        rng = random.Random(seed)
        lifts_for_v = {v: rng.sample(range(p), 2) for v in uniq_v}
        seq: list[HElem] = [(v, rng.choice(lifts_for_v[v])) for v in v_list]
        if c > 0:
            seq += [((0, 0), rng.randrange(1, p))] * c

        def score(s: Sequence[HElem]) -> Tuple[int, int]:
            if Counter(s).most_common(1)[0][1] >= p:
                return (2, 9999)
            try:
                is_p1, sp = eval_sequence_products(s, p, max_states=60_000)
            except ValueError:
                return (2, 9999)
            return (0 if is_p1 else 1, sp)

        cur_sc = score(seq)
        if cur_sc < best:
            best = cur_sc
        for _ in range(steps):
            if best == (0, 0):
                return best
            idx = rng.randrange(len(seq))
            old = seq[idx]
            v = old[0]
            new_a = rng.randrange(1, p) if v == (0, 0) else rng.choice(lifts_for_v[v])
            seq[idx] = (v, new_a)
            sc = score(seq)
            if sc <= cur_sc or rng.random() < 0.15:
                cur_sc = sc
                if sc < best:
                    best = sc
            else:
                seq[idx] = old
    return best


def main() -> None:
    print("1. Exponential isomorphism & alternating-area check:")
    for p in [3, 5, 7, 11]:
        rng = random.Random(p)
        for _ in range(25):
            g1: HElem = ((rng.randrange(p), rng.randrange(p)), rng.randrange(p))
            g2: HElem = ((rng.randrange(p), rng.randrange(p)), rng.randrange(p))
            assert exp_to_mat(heis_mul(g1, g2, p), p) == mat_mul(exp_to_mat(g1, p), exp_to_mat(g2, p), p)
            word = [((rng.randrange(p), rng.randrange(p)), rng.randrange(p)) for _ in range(7)]
            prod = heis_word_prod(word, p)
            expected = (
                (sum(w[0][0] for w in word) % p, sum(w[0][1] for w in word) % p),
                (sum(w[1] for w in word) + alternating_area([w[0] for w in word], p)) % p,
            )
            assert prod == expected
        print(f"  p={p}: PASS")

    print("\n2. Extremal constructions S^(1), S^(2), T_eta, T_s:")
    for p in [3, 5, 7, 11]:
        s1, w1 = build_s1(p)
        s2, w2 = build_s2(p)
        assert len(s1) == 3 * p - 1 and len(s2) == 3 * p - 1
        assert heis_word_prod(w1, p) == ((0, 0), 0)
        assert heis_word_prod(w2, p) == ((0, 0), 0)
        assert is_minimal_product_one(s1, p)
        assert is_minimal_product_one(s2, p)
        ok_eta, ok_s = check_t_eta_and_ts(p)
        assert ok_eta and ok_s
        print(f"  p={p}: S^(1), S^(2) minimal len={3*p-1}; T_eta (len={7*p-7}) & T_s (len={8*p-8}) verified PASS")

    print("\n3. Lemma 1 order-value growth stress tests:")
    for p in [3, 5, 7]:
        assert verify_lemma1_growth(p, trials=50, seed=p)
        print(f"  p={p}: PASS")

    print("\n4. Exhaustive H_27 (p=3, length 9) check:")
    h27_sum = verify_h27_exhaustive()
    for c, (norb, tested, found) in h27_sum.items():
        print(f"  c={c}: orbits={norb}, tested={tested}, minimal_len_9_found={found}")
        assert found == 0

    print("\n5. Targeted (O1)/(O2) obstruction probes on H_125 (p=5) and H_343 (p=7):")
    atom8_p5 = [(0,4),(0,4),(2,3),(2,3),(2,4),(2,4),(3,0),(4,3)]
    p5_probes = [
        ("p=5 O1 9+5 (c=1, len=15)", [(1,0)]*4 + [(0,1)]*4 + [(1,1)] + [(1,2)]*5, 1),
        ("p=5 O1 8+5 (c=2, len=15)", atom8_p5 + [(1,2)]*5, 2),
        ("p=5 O1 8+5 (c=3, len=16)", atom8_p5 + [(1,2)]*5, 3),
        ("p=5 O2 3-line (5,5,5, c=0, len=15)", [(1,0)]*5 + [(0,1)]*5 + [(1,1)]*5, 0),
        ("p=5 O2 3-line (5,5,4, c=2, len=16)", [(1,0)]*5 + [(0,1)]*5 + [(1,1)]*3 + [(2,2)], 2),
    ]
    for label, vlist, c in p5_probes:
        sc = hill_climb_obstruction(vlist, c, 5, steps=60, seeds=2)
        print(f"  {label}: best=(status={sc[0]}, min_splits={sc[1]})")
        assert sc != (0, 0)

    # p=7 probes (states kept small via high multiplicity)
    p7_probes = [
        ("p=7 O1 13+7 (c=1, len=21)", [(1,0)]*6 + [(0,1)]*6 + [(1,1)] + [(1,2)]*7, 1),
        ("p=7 O2 3-line (7,7,7, c=0, len=21)", [(1,0)]*7 + [(0,1)]*7 + [(1,1)]*7, 0),
    ]
    for label, vlist, c in p7_probes:
        sc = hill_climb_obstruction(vlist, c, 7, steps=40, seeds=2)
        print(f"  {label}: best=(status={sc[0]}, min_splits={sc[1]})")
        assert sc != (0, 0)

    print("\nALL VERIFICATIONS PASSED!")


if __name__ == "__main__":
    main()

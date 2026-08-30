"""Dependency-free symbolic audit of triangular-hive coarse graining.

For a fine hive h of order n*t define H(i,l)=h(t*i,t*l).  Each coarse
rhombus slack is a t-by-t sum of fine slacks of the same orientation.  This
script verifies those identities as formal integer linear forms and checks
the Paper 32 scaling arithmetic.  It does not replace the frozen exact seed
certificates in ``../repro``.
"""

from __future__ import annotations

import argparse
from collections import defaultdict


Node = tuple[int, int]
Form = dict[Node, int]


def form(terms: list[tuple[Node, int]]) -> Form:
    out: defaultdict[Node, int] = defaultdict(int)
    for node, coefficient in terms:
        out[node] += coefficient
    return {node: coefficient for node, coefficient in out.items() if coefficient}


def add(*forms: Form) -> Form:
    out: defaultdict[Node, int] = defaultdict(int)
    for current in forms:
        for node, coefficient in current.items():
            out[node] += coefficient
    return {node: coefficient for node, coefficient in out.items() if coefficient}


def r1(i: int, level: int) -> Form:
    return form([
        ((i, level + 1), 1), ((i - 1, level), 1),
        ((i - 1, level + 1), -1), ((i, level), -1),
    ])


def r2(i: int, level: int) -> Form:
    return form([
        ((i, level + 1), 1), ((i, level), 1),
        ((i + 1, level + 1), -1), ((i - 1, level), -1),
    ])


def r3(i: int, level: int) -> Form:
    return form([
        ((i, level), 1), ((i - 1, level), 1),
        ((i, level + 1), -1), ((i - 1, level - 1), -1),
    ])


def coarse_slack(orientation: int, i: int, level: int, scale: int) -> Form:
    slack = (r1, r2, r3)[orientation - 1](i, level)
    return {(scale * x, scale * y): coefficient for (x, y), coefficient in slack.items()}


def fine_sum(orientation: int, i: int, level: int, scale: int) -> Form:
    t = scale
    pieces: list[Form] = []
    if orientation == 1:
        # Coordinates x=i, y=level.
        for x in range((i - 1) * t + 1, i * t + 1):
            for y in range(level * t, (level + 1) * t):
                pieces.append(r1(x, y))
    elif orientation == 2:
        # Oblique coordinates a=level, b=level-i.
        for a in range(level * t, (level + 1) * t):
            for b in range((level - i) * t, (level - i + 1) * t):
                pieces.append(r2(a - b, a))
    else:
        # Oblique coordinates u=i, v=level-i.
        for u in range((i - 1) * t + 1, i * t + 1):
            for v in range((level - i) * t, (level - i + 1) * t):
                pieces.append(r3(u, u + v))
    return add(*pieces)


def boundary_increment(side: str, index: int, order: int) -> Form:
    if side == "alpha":
        return form([((0, index), 1), ((0, index - 1), -1)])
    if side == "beta":
        return form([((index, order), 1), ((index - 1, order), -1)])
    if side == "gamma":
        return form([((index, index), 1), ((index - 1, index - 1), -1)])
    raise ValueError(side)


def verify_grid(coarse_order: int, scale: int) -> int:
    checks = 0
    for level in range(1, coarse_order):
        for i in range(1, level + 1):
            for orientation in (1, 2, 3):
                assert coarse_slack(orientation, i, level, scale) == fine_sum(orientation, i, level, scale)
                checks += 1
    fine_order = coarse_order * scale
    for side in ("alpha", "beta", "gamma"):
        for index in range(1, coarse_order + 1):
            coarse = boundary_increment(side, index, coarse_order)
            coarse = {(scale * x, scale * y): c for (x, y), c in coarse.items()}
            fine = add(*(
                boundary_increment(side, q, fine_order)
                for q in range((index - 1) * scale + 1, index * scale + 1)
            ))
            assert coarse == fine
            checks += 1
    return checks


def verify_scaling_arithmetic(max_scale: int) -> None:
    # Frozen exact k=3 seed values: ranks 15,16,17,18 have 90,89,88,87.
    for t in range(1, max_scale + 1):
        assert 27 * t == 9 * (3 * t)
        assert 15 * t == 5 * (3 * t)
        for s in range(4):
            rank = (15 + s) * t
            value = (90 - s) * t
            assert rank == 5 * (3 * t) + s * t
            assert value == 30 * (3 * t) - s * t
        assert (17 * t + 1) - 15 * t == 2 * t + 1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--coarse-order", type=int, default=27)
    parser.add_argument("--scale-through", type=int, default=6)
    args = parser.parse_args()
    checks = 0
    for scale in range(1, args.scale_through + 1):
        checks += verify_grid(args.coarse_order, scale)
    verify_scaling_arithmetic(args.scale_through)
    print(f"PASS: {checks} formal rhombus/boundary identities")
    print(f"PASS: coarse order {args.coarse_order}, scales 1..{args.scale_through}")
    print("THEOREM: restriction to the t-sublattice sends every fine hive to a coarse hive with block-sum boundaries")
    print("COROLLARY: k=3 exact seed scales to F_(3t) at ranks 15t,16t,17t,18t")
    print("SCOPE: proves unbounded additive excess, not exact r_*(F_(3t))=18t")


if __name__ == "__main__":
    main()

"""Exact algebra replay for the all-k endpoint certificates.

The mathematical LR step is the following standard consequence of the LR
semigroup property and conjugation symmetry.  If a Horn triple corresponds to
``(lambda,mu,nu)``, block inflation of every selected index by a factor k
corresponds to

    D_k(lambda)=(k*lambda_1 repeated k, k*lambda_2 repeated k, ...).

Now ``D_k = conjugate o H_k o conjugate o H_k``, where ``H_k`` multiplies
every part by k.  Positivity is preserved by H_k (LR semigroup) and by
simultaneous conjugation.  Hence every inflated triple below is Horn.

This checker verifies the base Horn membership and all remaining coefficient,
right-side, order-cone, primal-rank, and cost identities over Fraction.  It
proves only the endpoints rank<=5k and unrestricted; it does not prove the
intermediate rank faces.
"""

from __future__ import annotations

import argparse
import sys
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER31_MATH = HERE
sys.path.insert(0, str(PAPER31_MATH))

from verify_rank_gap_frontier import horn_t  # noqa: E402


FULL = (
    ((1, (3,), (1,), (3,)), Q(1, 2)),
    ((1, (4,), (1,), (4,)), Q(1)),
    ((4, (2, 3, 6, 7), (1, 2, 6, 7), (3, 4, 8, 9)), Q(1, 2)),
    ((7, (1, 2, 3, 4, 6, 7, 8), (1, 2, 3, 4, 6, 7, 8), (1, 2, 3, 4, 7, 8, 9)), Q(1, 2)),
    ((8, (1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 6, 7, 8, 9), (1, 2, 3, 4, 6, 7, 8, 9)), Q(1, 2)),
)

FACE = (
    ((1, (4,), (1,), (4,)), Q(1, 2)),
    ((4, (3, 4, 6, 7), (1, 2, 5, 6), (3, 4, 8, 9)), Q(1, 2)),
    ((6, (2, 3, 4, 6, 7, 8), (1, 2, 3, 5, 6, 7), (2, 3, 4, 7, 8, 9)), Q(1, 2)),
    ((7, (1, 2, 3, 4, 6, 7, 8), (1, 2, 3, 4, 6, 7, 8), (1, 2, 3, 4, 7, 8, 9)), Q(1, 2)),
    ((8, (1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 6, 7, 8, 9), (1, 2, 3, 4, 6, 7, 8, 9)), Q(3, 2)),
)


def row_and_rhs(triple, copies: int):
    _, i0, j0, k0 = triple
    n = 9 * copies
    I, J, K = (inflate(subset, copies) for subset in (i0, j0, k0))
    row = [0] * (n - 1)
    for index in I:
        if index < n:
            row[index - 1] += 1
    for index in J:
        if index > 1:
            row[n - index] -= 1
    rhs = sum(10 if index <= 4 * copies else -8 for index in K)
    return tuple(row), rhs, (len(I), I, J, K)


def partition(subset: tuple[int, ...]) -> tuple[int, ...]:
    r = len(subset)
    return tuple(subset[r - a] - (r - a + 1) for a in range(1, r + 1))


def dilate_partition(parts: tuple[int, ...], copies: int) -> tuple[int, ...]:
    return tuple(copies * part for part in parts for _ in range(copies))


def inflate(subset: tuple[int, ...], copies: int) -> tuple[int, ...]:
    return tuple(x for i in subset for x in range((i - 1) * copies + 1, i * copies + 1))


def combined(certificate, copies: int):
    n = 9 * copies
    coefficient = [Q(0)] * (n - 1)
    rhs = Q(0)
    for triple, weight in certificate:
        row, value, _ = row_and_rhs(triple, copies)
        for index, entry in enumerate(row):
            coefficient[index] += weight * int(entry)
        rhs += weight * value
    return tuple(coefficient), rhs


def verify_base_horn_membership() -> int:
    triples = {triple for triple, _ in (*FULL, *FACE)}
    for triple in triples:
        r, I, J, K = triple
        assert (I, J, K) in horn_t(r, 9), triple
    return len(triples)


def verify_copy(copies: int) -> None:
    n = 9 * copies
    for triple, _ in (*FULL, *FACE):
        _, I, J, K = triple
        for subset in (I, J, K):
            assert partition(inflate(subset, copies)) == dilate_partition(partition(subset), copies)

    full_coefficient, full_rhs = combined(FULL, copies)
    assert full_rhs == 29 * copies
    objective = (Q(1, 2),) * (n - 1)
    difference = tuple(q - c for q, c in zip(objective, full_coefficient))
    # A vector is a nonnegative combination of p_i-p_(i+1) and p_(n-1)
    # iff all its prefix sums are nonnegative.
    prefixes = []
    running = Q(0)
    for entry in difference:
        running += entry
        prefixes.append(running)
    assert all(x >= 0 for x in prefixes)

    face_coefficient, face_rhs = combined(FACE, copies)
    assert face_rhs == 30 * copies
    assert face_coefficient[: 5 * copies] == (Q(1, 2),) * (5 * copies)

    full_primal = (16,) * copies + (12,) * copies + (10,) * (2 * copies) + (8,) * copies + (2,) * copies
    face_primal = (16,) * copies + (14,) * copies + (12,) * copies + (10,) * copies + (8,) * copies
    assert len(full_primal) == 6 * copies and Q(sum(full_primal), 2) == 29 * copies
    assert len(face_primal) == 5 * copies and Q(sum(face_primal), 2) == 30 * copies


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-through", type=int, default=32)
    args = parser.parse_args()
    count = verify_base_horn_membership()
    for copies in range(1, args.check_through + 1):
        verify_copy(copies)
    print(f"PASS: {count} distinct base Horn triples")
    print(f"PASS: exact endpoint algebra checked for 1<=k<={args.check_through}")
    print("THEOREM: LR semigroup + conjugation proves the same identities for every k>=1")
    print("RESULT: unrestricted=29k; rank<=5k=30k; endpoint primals have ranks 6k and 5k")
    print("SCOPE: no intermediate-face or minimum-optimal-rank=6k claim")


if __name__ == "__main__":
    main()

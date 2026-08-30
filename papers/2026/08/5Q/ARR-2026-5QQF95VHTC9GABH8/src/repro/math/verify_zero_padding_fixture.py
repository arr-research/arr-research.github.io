"""Exact replay for the zero-padding warning in Paper 31.

This standard-library-only verifier checks all Horn inequalities for three
displayed primal spectra and exact sparse nonnegative dual combinations for
their matching lower bounds. It proves only this finite fixture.
"""

from fractions import Fraction as Q

from verify_rank_gap_frontier import constraints, verify_dual, verify_primal


def row_map(rows):
    return {name: (row, b0, b1) for name, row, b0, b1 in rows}


def verify_d7():
    gamma = tuple(Q(2 * x, 7) for x in (25, 18, 18, -10, -17, -17, -17))
    rows = constraints(7, gamma)
    primal = tuple(Q(x, 7) for x in (54, 36, 36, 20, 2, 0))
    certificate = (
        ((1, (3,), (1,), (3,)), Q(1, 2)),
        ((3, (2, 3, 5), (1, 2, 5), (2, 3, 7)), Q(1, 2)),
        ((5, (1, 2, 3, 5, 6), (1, 2, 3, 5, 6), (1, 2, 3, 6, 7)), Q(1, 2)),
        ((6, (1, 2, 3, 4, 5, 6), (1, 2, 3, 5, 6, 7), (1, 2, 3, 5, 6, 7)), Q(1, 2)),
        (("nonnegative",), Q(1)),
    )
    verify_primal(
        "d7_full", rows, primal, (Q(0),) * 6, (Q(0),),
        lambda _t: Q(74, 7), lambda _t: 5,
    )
    verify_dual("d7_full", certificate, row_map(rows), 6, (Q(74, 7), Q(0)))


def verify_d8():
    gamma = tuple(Q(2 * x, 7) for x in (25, 18, 18, 0, -10, -17, -17, -17))
    rows = constraints(8, gamma)
    full = tuple(Q(x, 7) for x in (52, 36, 36, 20, 2, 0, 0))
    face = tuple(Q(x, 7) for x in (54, 38, 36, 20, 0, 0, 0))
    h1 = (1, (3,), (1,), (3,))
    h2 = (2, (2, 5), (1, 6), (3, 8))
    h3 = (3, (1, 2, 6), (1, 2, 6), (1, 3, 8))
    h5 = (5, (1, 2, 3, 5, 6), (1, 2, 3, 6, 7), (1, 2, 3, 7, 8))
    h7 = (
        7,
        (1, 2, 3, 4, 5, 6, 7),
        (1, 2, 3, 4, 6, 7, 8),
        (1, 2, 3, 4, 6, 7, 8),
    )
    full_certificate = (
        (h1, Q(1)), (h2, Q(1, 4)), (h3, Q(1, 4)),
        (h5, Q(1, 4)), (h7, Q(1, 2)),
        (("order", 6), Q(1, 4)), (("nonnegative",), Q(5, 4)),
    )
    face_certificate = (
        (h1, Q(1)), (h2, Q(1, 2)), (h5, Q(1, 2)), (h7, Q(1, 2)),
    )
    zero = (Q(0),) * 7
    verify_primal(
        "d8_full", rows, full, zero, (Q(0),),
        lambda _t: Q(73, 7), lambda _t: 5,
    )
    verify_primal(
        "d8_rank4", rows, face, zero, (Q(0),),
        lambda _t: Q(74, 7), lambda _t: 4,
    )
    mapping = row_map(rows)
    verify_dual("d8_full", full_certificate, mapping, 7, (Q(73, 7), Q(0)))
    verify_dual("d8_rank4", face_certificate, mapping, 4, (Q(74, 7), Q(0)))


if __name__ == "__main__":
    verify_d7()
    verify_d8()
    print("PASS: exact zero-padding fixture (d7=74/7; d8=73/7; d8 rank<=4=74/7)")

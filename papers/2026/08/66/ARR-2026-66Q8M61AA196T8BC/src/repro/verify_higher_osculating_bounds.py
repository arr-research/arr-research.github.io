#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact finite checks for higher-order osculating-absorption bounds.

These checks certify integer identities, finite optimization, and displayed
unisolvence fixtures only.  They do not prove the universal geometric theorem,
novelty, or priority.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb


def jet_length(dimension: int, order: int) -> int:
    """Length of O/m^(order+1) at a smooth point; order -1 means no block."""
    if order == -1:
        return 0
    if dimension < 1 or order < 0:
        raise ValueError("dimension must be positive and order at least -1")
    return comb(dimension + order, dimension)


def higher_bound(dimension: int, degree: int, order: int) -> int:
    """B_{d,s}(m), for 1 <= s <= m."""
    if dimension < 1 or not 1 <= order <= degree:
        raise ValueError("require dimension >= 1 and 1 <= order <= degree")
    quotient, remainder = divmod(degree + 1, order + 1)
    return (
        quotient * jet_length(dimension, order)
        + jet_length(dimension, remainder - 1)
    )


def first_order_bound(dimension: int, degree: int) -> int:
    """The published J(d,m) bound."""
    return (
        ((degree + 1) // 2) * (dimension + 1)
        + (1 if degree % 2 == 0 else 0)
    )


def partition_optimum(dimension: int, degree: int, order: int) -> int:
    """Brute-force the best mixed-jet length under degree budget m."""
    budget = degree + 1
    weights = range(1, order + 2)
    best = 0
    # At most budget blocks, each consuming at least one unit.
    for count in range(1, budget + 1):
        for blocks in combinations_with_replacement(weights, count):
            if sum(blocks) <= budget:
                value = sum(jet_length(dimension, weight - 1) for weight in blocks)
                best = max(best, value)
    return best


def rational_rank(matrix: list[list[int]]) -> int:
    work = [[Fraction(entry) for entry in row] for row in matrix]
    if not work:
        return 0
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row:
                continue
            coefficient = work[row][column]
            if coefficient:
                work[row] = [
                    entry - coefficient * pivot_entry
                    for entry, pivot_entry in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def curve_fixture(degree: int, order: int) -> dict[str, int | str]:
    """m+1 affine points are unisolvent for degree-m polynomials on P^1."""
    points = list(range(degree + 1))
    values = [[point**power for power in range(degree + 1)] for point in points]
    value_rank = rational_rank(values)

    jet_rows: list[list[int]] = []
    for point in points:
        for derivative_order in range(order + 1):
            row = []
            for power in range(degree + 1):
                if derivative_order > power:
                    row.append(0)
                else:
                    coefficient = 1
                    for step in range(derivative_order):
                        coefficient *= power - step
                    row.append(coefficient * point ** (power - derivative_order))
            jet_rows.append(row)
    jet_rank = rational_rank(jet_rows)
    expected = degree + 1
    assert value_rank == expected
    assert jet_rank == expected
    assert higher_bound(1, degree, order) == expected
    return {
        "dimension": 1,
        "degree": degree,
        "order": order,
        "point_count": expected,
        "value_rank_over_Q": value_rank,
        "value_plus_order_s_jets_rank_over_Q": jet_rank,
        "status": "PASS",
    }


def lattice_tuples(dimension: int, degree: int) -> list[tuple[int, ...]]:
    """Nonnegative d-tuples of total degree at most degree."""
    if dimension == 0:
        return [()]
    return [
        (head, *tail)
        for head in range(degree + 1)
        for tail in lattice_tuples(dimension - 1, degree - head)
    ]


def hasse_entry(
    exponent: tuple[int, ...],
    derivative: tuple[int, ...],
    point: tuple[int, ...],
) -> int:
    """Coefficient of the indicated multivariate Hasse derivative."""
    if any(derivative[i] > exponent[i] for i in range(len(exponent))):
        return 0
    coefficient = 1
    value = 1
    for exp_i, der_i, point_i in zip(exponent, derivative, point):
        coefficient *= comb(exp_i, der_i)
        value *= point_i ** (exp_i - der_i)
    return coefficient * value


def projective_space_fixture(
    dimension: int, degree: int
) -> dict[str, int | str]:
    """A rational simplex lattice is unisolvent in the top-order regime."""
    monomials = lattice_tuples(dimension, degree)
    points = lattice_tuples(dimension, degree)
    values = [
        [
            hasse_entry(exponent, (0,) * dimension, point)
            for exponent in monomials
        ]
        for point in points
    ]
    jet_rows = [
        [hasse_entry(exponent, derivative, point) for exponent in monomials]
        for point in points
        for derivative in lattice_tuples(dimension, degree)
    ]
    expected = comb(dimension + degree, dimension)
    value_rank = rational_rank(values)
    jet_rank = rational_rank(jet_rows)
    assert len(points) == expected
    assert value_rank == expected
    assert jet_rank == expected
    assert higher_bound(dimension, degree, degree) == expected
    return {
        "dimension": dimension,
        "degree": degree,
        "order": degree,
        "point_count": expected,
        "value_rank_over_Q": value_rank,
        "value_plus_order_s_hasse_jets_rank_over_Q": jet_rank,
        "status": "PASS",
    }


def main() -> None:
    # The order-one specialization is exactly the published J(d,m).
    for dimension in range(1, 9):
        for degree in range(1, 61):
            assert higher_bound(dimension, degree, 1) == first_order_bound(
                dimension, degree
            )

    # On curves every higher-order bound collapses to the exact value m+1.
    for degree in range(1, 61):
        for order in range(1, degree + 1):
            assert higher_bound(1, degree, order) == degree + 1

    # Exhaustively check the convex mixed-block optimization on a broad range.
    # The brute-force range is intentionally modest because the number of
    # integer partitions grows quickly.
    optimization_cases = 0
    for dimension in range(1, 6):
        for order in range(1, 6):
            for degree in range(order, 13):
                assert higher_bound(dimension, degree, order) == partition_optimum(
                    dimension, degree, order
                )
                optimization_cases += 1

    # For d >= 2, the asymptotic coefficient strictly increases with s.
    for dimension in range(2, 9):
        for order in range(1, 12):
            left_num = jet_length(dimension, order)
            right_num = jet_length(dimension, order + 1)
            assert left_num * (order + 2) < right_num * (order + 1)

    fixtures = [
        curve_fixture(3, 1),
        curve_fixture(5, 2),
        curve_fixture(8, 3),
        curve_fixture(10, 5),
        projective_space_fixture(2, 2),
        projective_space_fixture(3, 3),
    ]
    result = {
        "status": "PASS",
        "optimization_cases": optimization_cases,
        "fixtures": fixtures,
        "scope": (
            "Exact integer optimization and finite rational-matrix fixtures only; "
            "does not prove the universal theorem, novelty, or priority."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

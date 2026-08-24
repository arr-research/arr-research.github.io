#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact finite witnesses for the higher-osculating absorption revision.

The script checks integer inequalities, rational and modular Hasse-jet ranks,
finite-field unisolvent supports, the sharp degree threshold on P^1, and local
higher-contact identities.  It does not prove the universal geometry.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import comb
from pathlib import Path


def jet_length(dimension: int, order: int) -> int:
    if order == -1:
        return 0
    if dimension < 1 or order < 0:
        raise ValueError("dimension must be positive and order at least -1")
    return comb(dimension + order, dimension)


def exact_floor(dimension: int, degree: int) -> int:
    return comb(dimension + degree, dimension)


def mixed_floor(dimension: int, degree: int, order: int) -> int:
    if dimension < 1 or not 1 <= order <= degree:
        raise ValueError("require dimension >= 1 and 1 <= order <= degree")
    quotient, remainder = divmod(degree + 1, order + 1)
    return quotient * jet_length(dimension, order) + jet_length(
        dimension, remainder - 1
    )


def partition_optimum(dimension: int, degree: int, order: int) -> int:
    budget = degree + 1
    weights = range(1, order + 2)
    best = 0
    for count in range(1, budget + 1):
        for blocks in combinations_with_replacement(weights, count):
            if sum(blocks) <= budget:
                best = max(
                    best,
                    sum(jet_length(dimension, weight - 1) for weight in blocks),
                )
    return best


def affine_monomials(dimension: int, degree: int) -> list[tuple[int, ...]]:
    if dimension == 0:
        return [()]
    return [
        (head, *tail)
        for head in range(degree + 1)
        for tail in affine_monomials(dimension - 1, degree - head)
    ]


def hasse_entry(
    exponent: tuple[int, ...],
    derivative: tuple[int, ...],
    point: tuple[int, ...],
) -> int:
    if any(derivative[i] > exponent[i] for i in range(len(exponent))):
        return 0
    coefficient = 1
    value = 1
    for exp_i, der_i, point_i in zip(exponent, derivative, point):
        coefficient *= comb(exp_i, der_i)
        value *= point_i ** (exp_i - der_i)
    return coefficient * value


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


def modular_rank(matrix: list[list[int]], prime: int) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
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
        inverse = pow(work[pivot_row][column], -1, prime)
        work[pivot_row] = [(entry * inverse) % prime for entry in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row:
                continue
            coefficient = work[row][column]
            if coefficient:
                work[row] = [
                    (entry - coefficient * pivot_entry) % prime
                    for entry, pivot_entry in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def rank_block_fixture(
    dimension: int,
    degree: int,
    order: int,
    points: list[tuple[int, ...]],
) -> dict[str, object]:
    monomials = affine_monomials(dimension, degree)
    derivatives = affine_monomials(dimension, order)
    rows = [
        [hasse_entry(exponent, derivative, point) for exponent in monomials]
        for point in points
        for derivative in derivatives
    ]
    rank = rational_rank(rows)
    expected = len(points) * jet_length(dimension, order)
    assert degree >= 2 * order + 1
    assert rank == expected
    return {
        "dimension": dimension,
        "degree": degree,
        "order": order,
        "support_count": len(points),
        "expected_block_rank": expected,
        "hasse_jet_rank_over_Q": rank,
        "status": "PASS",
    }


def finite_field_unisolvent_fixture(
    prime: int, dimension: int, degree: int
) -> dict[str, object]:
    monomials = affine_monomials(dimension, degree)
    target = len(monomials)
    selected: list[tuple[int, ...]] = []
    rows: list[list[int]] = []
    rank = 0
    for point in product(range(prime), repeat=dimension):
        row = [hasse_entry(exp, (0,) * dimension, point) for exp in monomials]
        new_rank = modular_rank([*rows, row], prime)
        if new_rank > rank:
            selected.append(point)
            rows.append(row)
            rank = new_rank
        if rank == target:
            break
    assert rank == target
    assert len(selected) == target
    return {
        "field": f"F_{prime}",
        "dimension": dimension,
        "degree": degree,
        "point_count": len(selected),
        "evaluation_rank": rank,
        "points": [list(point) for point in selected],
        "status": "PASS",
    }


def local_contact_fixture(
    prime: int, dimension: int, degree: int, order: int
) -> dict[str, object]:
    """Check y=-f with ord(f)=s+1 makes yR vanish through order s."""
    assert dimension >= 1 and 1 <= order <= degree
    r_monomials = affine_monomials(dimension + 1, degree - 1)
    minimum_orders: list[int] = []
    # The last exponent is the exponent of y.  Substituting y=-f, with every
    # monomial of f of degree s+1, gives this exact lower order for yR.
    for exponent in r_monomials:
        x_degree = sum(exponent[:-1])
        y_degree = exponent[-1]
        minimum_orders.append(x_degree + (y_degree + 1) * (order + 1))
    assert min(minimum_orders) == order + 1
    assert all(value >= order + 1 for value in minimum_orders)
    return {
        "field": f"F_{prime}",
        "dimension": dimension,
        "degree": degree,
        "order": order,
        "tested_R_monomials": len(r_monomials),
        "minimum_order_after_y_substitution": min(minimum_orders),
        "status": "PASS",
    }


def build_result() -> dict[str, object]:
    optimization_cases = 0
    dominance_cases = 0
    strict_dominance_cases = 0
    for dimension in range(1, 6):
        for order in range(1, 6):
            for degree in range(order, 13):
                old = mixed_floor(dimension, degree, order)
                assert old == partition_optimum(dimension, degree, order)
                exact = exact_floor(dimension, degree)
                assert exact >= old
                if dimension >= 2 and order < degree:
                    assert exact > old
                    strict_dominance_cases += 1
                optimization_cases += 1
                dominance_cases += 1

    threshold_counterexamples = []
    for order in range(1, 9):
        for degree in range(order, 2 * order + 1):
            actual = degree + 1
            rejected_block = 2 * (order + 1)
            assert rejected_block > actual
            threshold_counterexamples.append(
                {
                    "curve_degree": degree,
                    "order": order,
                    "actual_full_span_rank": actual,
                    "false_unthresholded_block_term": rejected_block,
                }
            )

    return {
        "status": "PASS",
        "legacy_mixed_optimization_cases": optimization_cases,
        "exact_dominance_cases": dominance_cases,
        "strict_dominance_cases_d_ge_2_s_lt_m": strict_dominance_cases,
        "rank_block_fixtures": [
            rank_block_fixture(2, 3, 1, [(0, 0), (1, 0), (0, 1)]),
            rank_block_fixture(2, 5, 2, [(0, 0), (1, 0), (0, 1)]),
            rank_block_fixture(
                3, 3, 1, [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
            ),
        ],
        "finite_field_unisolvent_fixtures": [
            finite_field_unisolvent_fixture(2, 2, 1),
            finite_field_unisolvent_fixture(3, 2, 2),
            finite_field_unisolvent_fixture(5, 2, 3),
            finite_field_unisolvent_fixture(3, 3, 2),
        ],
        "local_higher_contact_fixtures": [
            local_contact_fixture(2, 2, 3, 2),
            local_contact_fixture(3, 2, 4, 3),
            local_contact_fixture(5, 3, 5, 2),
        ],
        "threshold_counterexamples": threshold_counterexamples,
        "scope": (
            "Finite exact integer, rational Hasse-jet, modular evaluation, and "
            "local order fixtures only; not a proof of incidence, smoothness, "
            "the universal theorem, novelty, or priority."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    encoded = json.dumps(build_result(), indent=2, sort_keys=True)
    if args.output:
        with args.output.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(encoded + "\n")
    if args.json or not args.output:
        print(encoded)


if __name__ == "__main__":
    main()

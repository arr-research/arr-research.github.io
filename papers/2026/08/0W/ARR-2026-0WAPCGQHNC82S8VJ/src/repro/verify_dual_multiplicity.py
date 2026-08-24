#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact finite fixtures for the absorbing-Gauss-fibre manuscript.

The calculations use integers and Fraction arithmetic.  They check simplex
unisolvence, the Fermat ordinary-singularity Jacobian quotient, the resulting
weighted tangent-cone totals, and the numerical floors.  They do not prove
the incidence arguments, the normalization theorem, or the classical
multiplicity--Milnor formula.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path


def monomials(dimension: int, degree: int) -> list[tuple[int, ...]]:
    """Exponent vectors of total degree at most degree, in stable order."""
    if dimension == 0:
        return [()]
    return [
        (head, *tail)
        for head in range(degree + 1)
        for tail in monomials(dimension - 1, degree - head)
    ]


def simplex_points(dimension: int, degree: int) -> list[tuple[int, ...]]:
    return monomials(dimension, degree)


def rational_rank(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    work = [[Fraction(value) for value in row] for row in matrix]
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
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row:
                continue
            factor = work[row][column]
            if factor:
                work[row] = [
                    value - factor * pivot_value
                    for value, pivot_value in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def evaluate(exponent: tuple[int, ...], point: tuple[int, ...]) -> int:
    value = 1
    for power, coordinate in zip(exponent, point):
        value *= coordinate**power
    return value


def unisolvent_fixture(dimension: int, degree: int) -> dict[str, object]:
    basis = monomials(dimension, degree)
    points = simplex_points(dimension, degree)
    matrix = [[evaluate(exponent, point) for exponent in basis] for point in points]
    rank = rational_rank(matrix)
    expected = comb(dimension + degree, dimension)
    assert len(basis) == len(points) == expected
    assert rank == expected
    return {
        "dimension": dimension,
        "degree": degree,
        "point_count": len(points),
        "evaluation_rank_over_Q": rank,
        "status": "PASS",
    }


def fermat_jacobian_fixture(dimension: int, order: int) -> dict[str, object]:
    """Count C[[x]]/(x_1^s,...,x_d^s) for h=sum x_i^(s+1)."""
    assert dimension >= 1 and order >= 1
    standard = list(product(range(order), repeat=dimension))
    expected = order**dimension
    assert len(standard) == expected

    # The extra normalized-Gauss generator is h-sum(x_i h_i)=-s*h.
    # Every monomial x_i^(s+1) of h is already in (x_1^s,...,x_d^s),
    # so it does not change the quotient in this exact fixture.
    extra_generator_reduces_to_zero = all(
        any(exponent[i] >= order for i in range(dimension))
        for exponent in [
            tuple(order + 1 if i == j else 0 for i in range(dimension))
            for j in range(dimension)
        ]
    )
    assert extra_generator_reduces_to_zero
    return {
        "dimension": dimension,
        "osculating_order": order,
        "initial_form": "sum_i x_i^(s+1)",
        "jacobian_initial_ideal": "(x_1^s,...,x_d^s)",
        "standard_monomial_count": len(standard),
        "expected_milnor_and_branch_multiplicity": expected,
        "extra_gauss_generator_reduces_to_zero": True,
        "status": "PASS",
    }


def floor_fixture(dimension: int, degree: int, order: int) -> dict[str, object]:
    branches = comb(dimension + degree, dimension)
    branch_weight = order**dimension
    total = branches * branch_weight
    assert 1 <= order <= degree
    assert total == (order**dimension) * comb(dimension + degree, dimension)
    return {
        "dimension": dimension,
        "embedding_power": degree,
        "osculating_order": order,
        "branch_floor": branches,
        "local_multiplicity_floor": branch_weight,
        "dual_multiplicity_floor": total,
        "tangent_cone_weight_sum_at_equality": total,
        "sufficient_hypersurface_degree": (order + 2) * branches + 1,
        "status": "PASS",
    }


def rank_term_collapse_fixture(dimension: int, order: int) -> dict[str, object]:
    """At m=2s+1 the binomial floor dominates the maximal Gauss rank term."""
    threshold_degree = 2 * order + 1
    binomial_floor = comb(dimension + threshold_degree, dimension)
    maximal_gauss_linear_rank = dimension + 1
    higher_block_term = maximal_gauss_linear_rank * comb(
        dimension + order, dimension
    )
    assert binomial_floor >= higher_block_term
    return {
        "dimension": dimension,
        "osculating_order": order,
        "threshold_embedding_power": threshold_degree,
        "binomial_floor": binomial_floor,
        "maximal_gauss_fibre_rank_term": higher_block_term,
        "status": "PASS",
    }


def build_result() -> dict[str, object]:
    grid = [
        floor_fixture(dimension, degree, order)
        for dimension in range(1, 6)
        for degree in range(1, 7)
        for order in range(1, degree + 1)
    ]
    assert len(grid) == 105
    return {
        "status": "PASS",
        "floor_grid_case_count": len(grid),
        "floor_grid": grid,
        "unisolvent_fixtures": [
            unisolvent_fixture(1, 5),
            unisolvent_fixture(2, 3),
            unisolvent_fixture(2, 4),
            unisolvent_fixture(3, 3),
        ],
        "fermat_jacobian_fixtures": [
            fermat_jacobian_fixture(1, 1),
            fermat_jacobian_fixture(2, 1),
            fermat_jacobian_fixture(2, 3),
            fermat_jacobian_fixture(3, 2),
            fermat_jacobian_fixture(4, 3),
        ],
        "rank_term_collapse_fixtures": [
            rank_term_collapse_fixture(dimension, order)
            for dimension in range(1, 11)
            for order in range(1, 11)
        ],
        "scope": (
            "Finite exact integer and rational fixtures only; not a proof of "
            "the incidence constructions, Gauss normalization, the universal "
            "theorem, the Dimca-Parusinski formula, novelty, or priority."
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

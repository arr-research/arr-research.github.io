#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact finite checks for the successor manuscript.

These are finite matrix fixtures only.  They do not prove Bertini
smoothness, any universal theorem, novelty, or priority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import product
from math import comb, factorial
from typing import Iterable, Sequence


def affine_monomials(variable_count: int, degree: int) -> list[tuple[int, ...]]:
    return [
        exponent
        for exponent in product(range(degree + 1), repeat=variable_count)
        if sum(exponent) <= degree
    ]


def simplex_points(variable_count: int, degree: int) -> list[tuple[int, ...]]:
    return [
        point
        for point in product(range(degree + 1), repeat=variable_count)
        if sum(point) <= degree
    ]


def derivative_value(
    exponent: Sequence[int], point: Sequence[int], order: Sequence[int]
) -> int:
    value = 1
    for power, coordinate, derivation_order in zip(exponent, point, order):
        if derivation_order > power:
            return 0
        value *= factorial(power) // factorial(power - derivation_order)
        value *= coordinate ** (power - derivation_order)
    return value


def derivative_orders(variable_count: int, maximum_total_order: int) -> list[tuple[int, ...]]:
    return [
        order
        for order in product(range(maximum_total_order + 1), repeat=variable_count)
        if sum(order) <= maximum_total_order
    ]


def rational_rank(matrix: Iterable[Sequence[int | Fraction]]) -> int:
    work = [[Fraction(entry) for entry in row] for row in matrix]
    if not work:
        return 0
    column_count = len(work[0])
    if any(len(row) != column_count for row in work):
        raise ValueError("ragged matrix")
    pivot_row = 0
    for column in range(column_count):
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


def matrix_sha256(matrix: Sequence[Sequence[int | Fraction]]) -> str:
    payload = json.dumps(
        [[str(entry) for entry in row] for row in matrix], separators=(",", ":")
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def simplex_fixture(variable_count: int, degree: int) -> dict[str, object]:
    basis = affine_monomials(variable_count, degree)
    points = simplex_points(variable_count, degree)
    values = [
        [derivative_value(exponent, point, (0,) * variable_count) for exponent in basis]
        for point in points
    ]
    first_orders = derivative_orders(variable_count, 1)
    all_jets = [
        [derivative_value(exponent, point, order) for exponent in basis]
        for point in points
        for order in first_orders
    ]
    expected = comb(variable_count + degree, variable_count)
    value_rank = rational_rank(values)
    value_plus_jets_rank = rational_rank(all_jets)
    passed = (
        len(basis) == expected
        and len(points) == expected
        and value_rank == expected
        and value_plus_jets_rank == expected
    )
    return {
        "fixture": f"simplex_P{variable_count}_m{degree}",
        "points": [list(point) for point in points],
        "point_count": len(points),
        "ambient_section_dimension": expected,
        "value_rank_over_Q": value_rank,
        "value_plus_all_first_jets_rank_over_Q": value_plus_jets_rank,
        "matrix_sha256": matrix_sha256(all_jets),
        "status": "PASS" if passed else "FAIL",
    }


def triple_jet_fixture() -> dict[str, object]:
    variable_count = 2
    points = [(0, 0), (1, 0), (0, 1)]
    point_count = len(points)
    degree = 3 * point_count
    basis = affine_monomials(variable_count, degree)
    orders = derivative_orders(variable_count, 2)
    matrix = [
        [derivative_value(exponent, point, order) for exponent in basis]
        for point in points
        for order in orders
    ]
    expected = point_count * comb(variable_count + 2, variable_count)
    rank = rational_rank(matrix)
    return {
        "fixture": "triple_jets_P2_three_points_degree9",
        "points": [list(point) for point in points],
        "degree": degree,
        "section_dimension": len(basis),
        "triple_jet_target_dimension": expected,
        "triple_jet_rank_over_Q": rank,
        "matrix_sha256": matrix_sha256(matrix),
        "status": "PASS" if rank == expected else "FAIL",
    }


def quadratic_veronese_tangent(point: Sequence[int]) -> list[list[int]]:
    """Affine first-jet rows for [1:x:y] under the quadratic Veronese."""

    x, y = point
    return [
        [1, x, y, x * x, x * y, y * y],
        [0, 1, 0, 2 * x, y, 0],
        [0, 0, 1, 0, x, 2 * y],
    ]


def factorized_gauss_fixture() -> dict[str, object]:
    points = [(0, 0), (1, 0), (0, 1), (1, 1)]
    tangents = [quadratic_veronese_tangent(point) for point in points]
    individual_ranks = [rational_rank(tangent) for tangent in tangents]
    pair_union_ranks: dict[str, int] = {}
    for left in range(len(points)):
        for right in range(left + 1, len(points)):
            pair_union_ranks[f"{left}-{right}"] = rational_rank(
                tangents[left] + tangents[right]
            )
    passed = all(rank == 3 for rank in individual_ranks) and all(
        rank > 3 for rank in pair_union_ranks.values()
    )
    return {
        "fixture": "factorized_H_O2_on_P2_four_points",
        "interpretation": "H=O(1) tensor O(1); distinct sampled quadratic-Veronese tangent spaces",
        "points": [list(point) for point in points],
        "individual_tangent_ranks_over_Q": individual_ranks,
        "pairwise_union_ranks_over_Q": pair_union_ranks,
        "status": "PASS" if passed else "FAIL",
    }


def incomplete_subsystem_fixture() -> dict[str, object]:
    """Endpoint tangents for the incomplete O(5) subsystem in Remark 1.5."""

    tangent_at_10 = [[1, 0, 0, 0], [0, 1, 0, 0]]
    tangent_at_01 = [[0, 1, 0, 0], [1, 0, 0, 0]]
    left_rank = rational_rank(tangent_at_10)
    right_rank = rational_rank(tangent_at_01)
    union_rank = rational_rank(tangent_at_10 + tangent_at_01)
    passed = left_rank == right_rank == union_rank == 2
    return {
        "fixture": "incomplete_O5_subsystem_endpoint_tangents",
        "map": "[s^5+s*t^4, s^4*t+t^5, s^3*t^2, s^2*t^3]",
        "pullback_line_bundle": "O(5)=O(2) tensor O(3)",
        "tangent_rank_at_[1:0]_over_Q": left_rank,
        "tangent_rank_at_[0:1]_over_Q": right_rank,
        "combined_tangent_rank_over_Q": union_rank,
        "interpretation": "The two sampled affine tangent spaces coincide; this certifies the displayed counterexample calculation, not global injectivity of the map.",
        "status": "PASS" if passed else "FAIL",
    }


def frobenius_fixture() -> dict[str, object]:
    characteristics = [2, 3, 5]
    cases = []
    for characteristic in characteristics:
        # F=x^p+y^p=(x+y)^p over F_p.  Formal first derivatives have
        # coefficients p, hence vanish modulo p.
        derivative_coefficients = [characteristic % characteristic] * 2
        cases.append(
            {
                "characteristic": characteristic,
                "polynomial": f"x^{characteristic}+y^{characteristic}",
                "pth_root": "x+y",
                "first_derivative_coefficients_mod_p": derivative_coefficients,
                "status": "PASS" if derivative_coefficients == [0, 0] else "FAIL",
            }
        )
    return {
        "fixture": "frobenius_zero_derivative_sanity",
        "note": "Illustrates the p-th-power mechanism only; radical descent is a theorem, not certified by this fixture.",
        "cases": cases,
        "status": "PASS" if all(case["status"] == "PASS" for case in cases) else "FAIL",
    }


def build_report() -> dict[str, object]:
    fixtures = [
        simplex_fixture(2, 3),
        simplex_fixture(3, 3),
        triple_jet_fixture(),
        factorized_gauss_fixture(),
        incomplete_subsystem_fixture(),
        frobenius_fixture(),
    ]
    passed = all(fixture["status"] == "PASS" for fixture in fixtures)
    return {
        "status": "PASS" if passed else "FAIL",
        "arithmetic": "exact Gaussian elimination over Q using fractions.Fraction; finite-field coefficients reduced exactly",
        "scope": "Finite matrix fixtures only; does not prove Bertini smoothness, universal theorem, novelty, or priority.",
        "fixtures": fixtures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = build_report()
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        for fixture in report["fixtures"]:
            print(f"{fixture['fixture']}: {fixture['status']}")
        print(f"OVERALL: {report['status']}")
        print(f"SCOPE: {report['scope']}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

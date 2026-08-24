#!/usr/bin/env python3
"""Exact finite-field falsification fixtures for the perfect-field gap.

This replay exhausts every nonempty subset of several small projective
spaces.  It computes, over F_p, the degree-a kernels for values and for
value-plus-first-jet conditions.  The calculation only certifies the listed
finite fixtures; the manuscript supplies the universal proof.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def homogeneous_indices(variable_count: int, degree: int):
    if variable_count == 1:
        return [(degree,)]
    out = []
    for first in range(degree + 1):
        for tail in homogeneous_indices(variable_count - 1, degree - first):
            out.append((first,) + tail)
    return out


def projective_points(p: int, d: int):
    """Normalized F_p-points of P^d, first nonzero coordinate equal to one."""
    points = []
    for vector in itertools.product(range(p), repeat=d + 1):
        pivot = next((i for i, x in enumerate(vector) if x), None)
        if pivot is None:
            continue
        inverse = pow(vector[pivot], -1, p)
        normalized = tuple((x * inverse) % p for x in vector)
        if normalized not in points:
            points.append(normalized)
    return points


def monomial_value(point, exponent, p):
    value = 1
    for x, e in zip(point, exponent):
        value = value * pow(x, e, p) % p
    return value


def monomial_derivative(point, exponent, variable, p):
    if exponent[variable] == 0:
        return 0
    value = exponent[variable] % p
    for i, (x, e) in enumerate(zip(point, exponent)):
        power = e - 1 if i == variable else e
        value = value * pow(x, power, p) % p
    return value


def rank_mod_p(matrix, p):
    if not matrix:
        return 0
    a = [[x % p for x in row] for row in matrix]
    rows, cols, rank = len(a), len(a[0]), 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][col], -1, p)
        a[rank] = [(inverse * x) % p for x in a[rank]]
        for i in range(rows):
            if i == rank or not a[i][col]:
                continue
            multiple = a[i][col]
            a[i] = [(x - multiple * y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def condition_matrices(points, degree, p):
    monomials = homogeneous_indices(len(points[0]), degree)
    values, double_conditions = [], []
    for point in points:
        value_row = [monomial_value(point, exponent, p) for exponent in monomials]
        values.append(value_row)
        double_conditions.append(value_row)
        pivot = next(i for i, x in enumerate(point) if x)
        # Dehomogenize in x_pivot=1.  These d derivatives plus the value are
        # exactly the first-neighbourhood conditions in this affine chart.
        for variable in range(len(point)):
            if variable != pivot:
                double_conditions.append([
                    monomial_derivative(point, exponent, variable, p)
                    for exponent in monomials
                ])
    columns = len(monomials)
    return {
        "degree": degree,
        "columns": columns,
        "ideal_nullity": columns - rank_mod_p(values, p),
        "symbolic_square_nullity": columns - rank_mod_p(double_conditions, p),
    }


def audit_support(points, p, max_degree):
    degrees = [condition_matrices(points, degree, p) for degree in range(max_degree + 1)]
    alpha = next(item["degree"] for item in degrees if item["ideal_nullity"])
    alpha_two = next(
        item["degree"] for item in degrees if item["symbolic_square_nullity"]
    )
    assert alpha_two >= alpha + 1
    for item in degrees:
        equal_kernels = item["ideal_nullity"] == item["symbolic_square_nullity"]
        if equal_kernels:
            assert item["ideal_nullity"] == 0
    return {
        "point_count": len(points),
        "alpha_radical_ideal": alpha,
        "alpha_symbolic_square": alpha_two,
        "gap": alpha_two - alpha,
        "degrees": degrees,
    }


def exhaustive_fixture(p, d, max_degree):
    ambient = projective_points(p, d)
    supports = []
    for mask in range(1, 1 << len(ambient)):
        points = [point for i, point in enumerate(ambient) if mask & (1 << i)]
        supports.append(audit_support(points, p, max_degree))
    return {
        "field": f"F_{p}",
        "projective_dimension": d,
        "ambient_rational_point_count": len(ambient),
        "nonempty_supports_exhausted": len(supports),
        "minimum_observed_gap": min(item["gap"] for item in supports),
        "maximum_observed_gap": max(item["gap"] for item in supports),
        "maximum_alpha": max(item["alpha_radical_ideal"] for item in supports),
        "maximum_alpha_symbolic_square": max(
            item["alpha_symbolic_square"] for item in supports
        ),
        "all_gap_and_equal_kernel_assertions_passed": True,
    }


def frobenius_fixture(p):
    # On P^1 take q=[1:0], G=x_1, and F=G^p.  Then F is doubly zero at q,
    # every formal partial of F is zero, and radicality recovers G.
    q = (1, 0)
    g_exponent = (0, 1)
    f_exponent = (0, p)
    f_partials = [
        monomial_derivative(q, f_exponent, variable, p) for variable in range(2)
    ]
    assert monomial_value(q, g_exponent, p) == 0
    assert monomial_value(q, f_exponent, p) == 0
    assert f_partials == [0, 0]
    assert sum(g_exponent) < sum(f_exponent)
    return {
        "field": f"F_{p}",
        "support": [list(q)],
        "G": "x_1",
        "F": f"x_1^{p}=G^{p}",
        "formal_partials_of_F_at_support": f_partials,
        "root_degree": 1,
        "frobenius_degree": p,
        "interpretation": "all first partials vanish, but the radical ideal contains the lower-degree pth root G",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    fixtures = [
        exhaustive_fixture(2, 1, 6),
        exhaustive_fixture(3, 1, 8),
        exhaustive_fixture(2, 2, 8),
    ]
    payload = {
        "arithmetic": "exact Gaussian elimination modulo p; no random choices",
        "fixtures": fixtures,
        "frobenius_root_fixtures": [frobenius_fixture(2), frobenius_fixture(3)],
        "all_assertions_passed": True,
        "scope": "exhaustive only for the displayed finite projective spaces and degree ranges; not a proof of the universal theorem",
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        with args.output.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(encoded + "\n")
    if args.json:
        print(encoded)
    else:
        for item in fixtures:
            print(
                f"{item['field']} P^{item['projective_dimension']}: "
                f"supports={item['nonempty_supports_exhausted']} "
                f"gap={item['minimum_observed_gap']}..{item['maximum_observed_gap']} PASS"
            )
        print("Frobenius-root fixtures: PASS")
        print("ALL ASSERTIONS PASSED")


if __name__ == "__main__":
    main()

"""Finite exact fixtures for simplex unisolvence and spectrum arithmetic.

This replay does not construct the global hypersurfaces.  It checks the
explicit evaluation sets and the elementary integer decomposition used by
the realization theorems.
"""

from __future__ import annotations

import json
import math
from itertools import product
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
RESULTS = HERE / "global_fixture_results.json"


def exponents(d: int, m: int):
    return [a for a in product(range(m + 1), repeat=d) if sum(a) <= m]


def simplex_rank(d: int, m: int):
    basis = exponents(d, m)
    points = basis
    matrix = sp.Matrix(
        [[math.prod(point[j] ** exponent[j] for j in range(d)) for exponent in basis] for point in points]
    )
    rank = int(matrix.rank())
    expected = math.comb(d + m, d)
    if len(basis) != expected or rank != expected:
        raise AssertionError((d, m, len(basis), rank, expected))
    return {"d": d, "m": m, "points": len(points), "rank": rank}


def plane_floor(s: int):
    return (3 * s * s + 4 * s - 3) // 4


def greedy_decomposition(total: int, count: int, capacity: int):
    values = []
    remaining = total
    for _ in range(count):
        value = min(capacity, remaining)
        values.append(value)
        remaining -= value
    if remaining or sum(values) != total or any(not 0 <= x <= capacity for x in values):
        raise AssertionError((total, count, capacity, values, remaining))
    return values


def spectrum_fixture(s: int, m: int):
    count = math.comb(m + 2, 2)
    minimum = count * plane_floor(s)
    maximum = count * s * s
    capacity = s * s - plane_floor(s)
    for length in range(minimum, maximum + 1):
        increments = greedy_decomposition(length - minimum, count, capacity)
        if minimum + sum(increments) != length:
            raise AssertionError((s, m, length))
    return {
        "s": s,
        "m": m,
        "support": count,
        "minimum_length": minimum,
        "maximum_length": maximum,
        "number_of_integer_lengths": maximum - minimum + 1,
    }


def main():
    result = {
        "scope": (
            "Finite exact fixtures only: rational ranks for simplex evaluation "
            "and integer spectrum decompositions. Global Bertini and contact-"
            "determinacy arguments are proved in the manuscript, not by this file."
        ),
        "simplex_unisolvence": [
            simplex_rank(d, m)
            for d, maximum_m in ((1, 8), (2, 7), (3, 6), (4, 4))
            for m in range(1, maximum_m + 1)
        ],
        "surface_spectrum": [
            spectrum_fixture(s, m) for m in range(1, 9) for s in range(1, m + 1)
        ],
        "status": "pass",
    }
    RESULTS.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"results": str(RESULTS), "status": "pass"}, sort_keys=True))


if __name__ == "__main__":
    main()

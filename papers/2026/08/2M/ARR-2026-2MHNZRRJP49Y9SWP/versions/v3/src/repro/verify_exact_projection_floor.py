#!/usr/bin/env python3
"""Exact rational witnesses for the binomial projection floor."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def multiindices(d: int, m: int):
    return [a for a in itertools.product(range(m + 1), repeat=d) if sum(a) <= m]


def value(alpha, beta):
    out = 1
    for a, b in zip(alpha, beta):
        out *= a ** b
    return Fraction(out)


def derivative(alpha, beta, j):
    if beta[j] == 0:
        return Fraction(0)
    out = beta[j]
    for i, (a, b) in enumerate(zip(alpha, beta)):
        out *= a ** (b - 1 if i == j else b)
    return Fraction(out)


def rank(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    if not a:
        return 0
    rows, cols, r = len(a), len(a[0]), 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == rows:
            break
    return r


def fixture(d, m):
    basis = multiindices(d, m)
    points = multiindices(d, m)
    values = [[value(p, b) for b in basis] for p in points]
    jets = []
    for p in points:
        jets.append([value(p, b) for b in basis])
        jets.extend([[derivative(p, b, j) for b in basis] for j in range(d)])

    truncated = points[:-1]
    truncated_values = [[value(p, b) for b in basis] for p in truncated]
    truncated_jets = []
    for p in truncated:
        truncated_jets.append([value(p, b) for b in basis])
        truncated_jets.extend(
            [[derivative(p, b, j) for b in basis] for j in range(d)]
        )

    expected = math.comb(d + m, d)
    result = {
        "d": d,
        "m": m,
        "binomial_floor": expected,
        "point_count": len(points),
        "value_rank": rank(values),
        "value_plus_first_jets_rank": rank(jets),
        "deleted_node_point_count": len(truncated),
        "deleted_node_value_rank": rank(truncated_values),
        "deleted_node_value_plus_first_jets_rank": rank(truncated_jets),
    }
    assert len(basis) == len(points) == expected
    assert result["value_rank"] == expected
    assert result["value_plus_first_jets_rank"] == expected
    assert result["deleted_node_value_rank"] == expected - 1
    assert result["deleted_node_value_plus_first_jets_rank"] > expected - 1
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = [(d, m) for d in range(1, 5) for m in range(1, 6) if math.comb(d + m, d) <= 126]
    payload = {
        "arithmetic": "fractions.Fraction exact Gaussian elimination",
        "cases": [fixture(d, m) for d, m in cases],
        "all_assertions_passed": True,
        "scope": "finite simplex-lattice value and first-jet rank witnesses only",
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        with args.output.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(encoded + "\n")
    if args.json:
        print(encoded)
    else:
        for item in payload["cases"]:
            print(
                f"d={item['d']} m={item['m']} B={item['binomial_floor']} "
                f"rank={item['value_rank']} truncated jets="
                f"{item['deleted_node_value_plus_first_jets_rank']} PASS"
            )
        print("ALL ASSERTIONS PASSED")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact local algebra witnesses for common-tangent equality fixtures."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def multiindices(d, m):
    return [a for a in itertools.product(range(m + 1), repeat=d) if sum(a) <= m]


def ambient_indices(d, m):
    # Affine monomials t^beta y^b of total degree at most m.
    return [(beta, b) for b in range(m + 1) for beta in multiindices(d, m - b)]


def monomial(p, beta):
    out = 1
    for x, e in zip(p, beta):
        out *= x ** e
    return Fraction(out)


def derivative(p, beta, j):
    if beta[j] == 0:
        return Fraction(0)
    out = beta[j]
    for i, (x, e) in enumerate(zip(p, beta)):
        out *= x ** (e - 1 if i == j else e)
    return Fraction(out)


def rank(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    r = 0
    for c in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def linear_form(p, t):
    # l_p(t)=sum (i+1)(t_i-p_i), so l_p(p)=0.
    return sum((i + 1) * (t[i] - p[i]) for i in range(len(p)))


def local_f(points, t):
    out = 1
    for p in points:
        out *= linear_form(p, t) ** 2
    return out


def fixture(d, m):
    points = multiindices(d, m)
    columns = ambient_indices(d, m)
    values, jets = [], []
    for p in points:
        row = [monomial(p, beta) if b == 0 else Fraction(0) for beta, b in columns]
        values.append(row)
        jets.append(row)
        for j in range(d):
            # On X: y=-f(t), and f(p)=df_p=0.  Thus y-columns have zero 1-jet.
            jets.append([
                derivative(p, beta, j) if b == 0 else Fraction(0)
                for beta, b in columns
            ])

    # Direct exact check of f(p)=0.  The symbolic factor l_p(t)^2 proves df_p=0.
    local_checks = []
    for p in points:
        fp = local_f(points, p)
        local_checks.append({
            "point": list(p),
            "f_value": fp,
            "tangential_gradient": [0] * d,
            "gradient_reason": "the factor l_p(t)^2 divides f",
            "normal_derivative": 1,
        })
        assert fp == 0

    expected = math.comb(d + m, d)
    vr, jr = rank(values), rank(jets)
    assert len(points) == expected
    assert vr == jr == expected
    return {
        "d": d,
        "m": m,
        "B": expected,
        "ambient_degree_m_column_count": len(columns),
        "value_rank": vr,
        "double_point_rank": jr,
        "proper_span": vr < len(columns),
        "local_model": "F=f(t)+y with f=product_p l_p(t)^2",
        "local_checks": local_checks,
        "interpretation": "f and df vanish at every support; dF/dy=1; hence y=-f lies in m_p^2",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (3, 1)]
    payload = {
        "arithmetic": "fractions.Fraction exact Gaussian elimination",
        "cases": [fixture(d, m) for d, m in cases],
        "all_assertions_passed": True,
        "scope": "local prescribed-tangent and rank algebra; global smoothness is supplied by Bertini, not this replay",
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
                f"d={item['d']} m={item['m']} B={item['B']} "
                f"value={item['value_rank']} double={item['double_point_rank']} "
                f"proper={item['proper_span']} PASS"
            )
        print("ALL ASSERTIONS PASSED")


if __name__ == "__main__":
    main()

"""Exact rational Gröbner replay for the sharp plane Tjurina family.

The calculation is over QQ and certifies only 1 <= s <= 12.  The general
sharpness statement in the manuscript is proved from the cited classical
family formula, not extrapolated from this finite replay.
"""

from __future__ import annotations

import argparse
import json
from math import floor

from sympy import QQ, diff, groebner, symbols


def expected_floor(s: int) -> int:
    return floor((3 * s * s + 4 * s - 3) / 4)


def sharp_exponents(s: int) -> tuple[int, int]:
    multiplicity = s + 1
    if multiplicity % 2 == 0:
        half = multiplicity // 2
        return half + 1, half
    half_up = (multiplicity + 1) // 2
    return half_up, half_up


def exact_tjurina_colength(s: int) -> dict:
    x, y = symbols("x y")
    multiplicity = s + 1
    b, c = sharp_exponents(s)
    h = x**multiplicity + y**multiplicity + x**b * y**c
    basis = groebner([h, diff(h, x), diff(h, y)], x, y, domain=QQ, order="grlex")
    leading = [tuple(poly.LM(order=basis.order).exponents) for poly in basis.polys]

    # The basis contains pure powers x^multiplicity and y^multiplicity.
    # Hence every standard monomial lies in this finite square.
    assert any(i <= multiplicity and j == 0 for i, j in leading)
    assert any(j <= multiplicity and i == 0 for i, j in leading)
    standard = [
        (i, j)
        for i in range(multiplicity)
        for j in range(multiplicity)
        if not any(i >= u and j >= v for u, v in leading)
    ]
    value = len(standard)
    expected = expected_floor(s)
    assert value == expected, (s, value, expected, leading)
    return {
        "s": s,
        "multiplicity": multiplicity,
        "perturbation_exponents": [b, c],
        "tjurina_colength_over_QQ": value,
        "expected_floor": expected,
        "leading_monomial_exponents": [list(item) for item in leading],
        "standard_monomial_count": len(standard),
    }


def build_report() -> dict:
    fixtures = [exact_tjurina_colength(s) for s in range(1, 13)]
    return {
        "scope": {
            "field": "QQ",
            "range": "1 <= s <= 12",
            "claim": "finite exact Groebner verification only",
        },
        "check": "all sharp plane fixtures attain the Euler-reduced floor",
        "passed": True,
        "fixtures": fixtures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", help="optional UTF-8 JSON output path")
    args = parser.parse_args()
    payload = json.dumps(build_report(), indent=2, sort_keys=True) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()

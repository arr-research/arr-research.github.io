"""Exact replay for the proposed dimension-three sharp Tjurina floor.

The theorem is proved in the manuscript; this replay checks finite fixtures.
It uses exact integer/binomial arithmetic and exact rational ranks for the
strong-Lefschetz multiplication maps.  Direct Tjurina quotients are checked
independently over two large prime fields.  No finite fixture proves the
universal statement.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp

from search_fermat_perturbations import PRIMES, e_floor, evaluate, monomials, polynomial


HERE = Path(__file__).resolve().parent
RESULTS = HERE / "dimension_three_sharpness_results.json"


def box_degree_basis(s: int, degree: int):
    return [a for a in monomials(3, degree) if sum(a) == degree and all(x < s for x in a)]


def ell_power_coefficient(delta, power: int):
    if any(x < 0 for x in delta) or sum(delta) != power:
        return 0
    return math.factorial(power) // math.prod(math.factorial(x) for x in delta)


def multiplication_rank(s: int, source_degree: int, power: int):
    source = box_degree_basis(s, source_degree)
    target = box_degree_basis(s, source_degree + power)
    matrix = sp.Matrix(
        [
            [ell_power_coefficient(tuple(b - a for a, b in zip(src, dst)), power) for src in source]
            for dst in target
        ]
    )
    return len(source), len(target), int(matrix.rank())


def lefschetz_fixture(s: int):
    power = s + 2
    socle = 3 * (s - 1)
    quotient_length = 0
    maps = []
    for source_degree in range(max(0, socle - power + 1)):
        source, target, rank = multiplication_rank(s, source_degree, power)
        expected = min(source, target)
        if rank != expected:
            raise AssertionError((s, source_degree, source, target, rank))
        quotient_length += target - rank
        maps.append(
            {
                "source_degree": source_degree,
                "source_dimension": source,
                "target_dimension": target,
                "rank": rank,
            }
        )
    # Degrees below `power` are untouched, and any remaining target degrees
    # not represented above also contribute their full Hilbert value.
    total = s**3
    image_dimension = sum(item["rank"] for item in maps)
    quotient_length = total - image_dimension
    formula = s * (s + 2) * (2 * s - 1) // 3
    if quotient_length != formula:
        raise AssertionError((s, quotient_length, formula))
    return {
        "s": s,
        "socle_degree": socle,
        "power": power,
        "ambient_length": total,
        "image_dimension": image_dimension,
        "quotient_length": quotient_length,
        "formula": formula,
        "maps": maps,
    }


def ell_perturbation(s: int):
    degree = s + 2
    terms = {}
    for exponent in monomials(3, degree):
        if sum(exponent) == degree:
            terms[exponent] = math.factorial(degree) // math.prod(math.factorial(x) for x in exponent)
    mu, tau, tail = evaluate(polynomial(3, s, terms), 3, s)
    formula, maximizing_k = e_floor(3, s)
    if mu != s**3 or tau != formula:
        raise AssertionError((s, mu, tau, formula))
    return {
        "s": s,
        "mu": mu,
        "tau": tau,
        "formula": formula,
        "maximizing_truncation": maximizing_k,
        "stable_tail": [list(row) for row in tail],
        "primes": list(PRIMES),
    }


def main():
    symbolic_grid = []
    for s in range(1, 51):
        formula = s * (s + 2) * (2 * s - 1) // 3
        optimized, maximizing_k = e_floor(3, s)
        if optimized != formula or maximizing_k != 2 * s - 1:
            raise AssertionError((s, optimized, maximizing_k, formula))
        symbolic_grid.append({"s": s, "formula": formula, "maximizing_truncation": maximizing_k})

    result = {
        "scope": (
            "Finite replay only: exact combinatorics for 1<=s<=50, exact rational "
            "Lefschetz-map ranks for 1<=s<=8, and direct two-prime Tjurina "
            "quotients for 2<=s<=7. The universal theorem is not proved by this file."
        ),
        "symbolic_grid": symbolic_grid,
        "lefschetz_fixtures": [lefschetz_fixture(s) for s in range(1, 9)],
        "direct_tjurina_fixtures": [ell_perturbation(s) for s in range(2, 8)],
        "status": "pass",
    }
    RESULTS.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": result["status"], "results": str(RESULTS)}, sort_keys=True))


if __name__ == "__main__":
    main()

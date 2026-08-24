"""Exact integer checks for the truncated-generator Tjurina floor.

This replay certifies only the displayed finite grids and local fixtures.  It
does not replace the proof of the general dimension-count theorem.
"""

from __future__ import annotations

import argparse
import json
from math import ceil, comb, floor

from explore_monomial_defects import fixture


def choose(n: int, k: int) -> int:
    return 0 if n < k or k < 0 else comb(n, k)


def raw_truncated_floor_at(d: int, s: int, k: int) -> int:
    return (
        choose(d + k, d)
        - d * choose(d + k - s, d)
        - choose(d + k - s - 1, d)
    )


def euler_truncated_floor_at(d: int, s: int, k: int) -> int:
    """Generator count after Euler cancellation raises h from s+1 to s+2."""
    return (
        choose(d + k, d)
        - d * choose(d + k - s, d)
        - choose(d + k - s - 2, d)
    )


def optimized_floor(floor_at, d: int, s: int) -> tuple[int, list[int]]:
    # The forward difference is eventually negative and remains negative.
    # This generous exact range covers the finite verification grid below.
    values = [floor_at(d, s, k) for k in range((d + 3) * s + 20)]
    maximum = max(values)
    return maximum, [k for k, value in enumerate(values) if value == maximum]


def old_floor(d: int, s: int) -> int:
    return choose(d + s - 1, d)


def plane_raw_closed_floor(s: int) -> int:
    return floor((3 * s * s + 2 * s) / 4)


def plane_euler_closed_floor(s: int) -> int:
    return floor((3 * s * s + 4 * s - 3) / 4)


def build_report() -> dict:
    grid = []
    for d in range(1, 9):
        for s in range(1, 21):
            raw_value, raw_maximizers = optimized_floor(raw_truncated_floor_at, d, s)
            value, maximizers = optimized_floor(euler_truncated_floor_at, d, s)
            assert raw_value <= value <= s**d, (d, s, raw_value, value, s**d)
            if d >= 2 and s >= 2:
                assert value > old_floor(d, s), (d, s, value, old_floor(d, s))
            assert value >= choose(d + s, d) - d
            if d == 2:
                assert raw_value == plane_raw_closed_floor(s), (
                    s,
                    raw_value,
                    plane_raw_closed_floor(s),
                )
                assert value == plane_euler_closed_floor(s), (
                    s,
                    value,
                    plane_euler_closed_floor(s),
                )
            grid.append(
                {
                    "d": d,
                    "s": s,
                    "old_floor": old_floor(d, s),
                    "clean_floor": choose(d + s, d) - d,
                    "raw_optimized_floor": raw_value,
                    "raw_maximizers": raw_maximizers,
                    "optimized_floor": value,
                    "maximizers": maximizers,
                    "milnor_upper_s_to_d": s**d,
                    "liu_floor": ceil(s**d / d),
                }
            )

    local_cases = [
        (2, 4, (3, 3)),
        (2, 5, (3, 4)),
        (2, 6, (4, 4)),
        (3, 3, (2, 2, 2)),
        (3, 4, (2, 2, 2)),
        (3, 5, (3, 2, 2)),
        (3, 5, (3, 3, 3)),
        (3, 6, (3, 3, 3)),
        (4, 2, (1, 1, 1, 1)),
        (4, 3, (2, 1, 1, 1)),
        (4, 5, (2, 2, 2, 2)),
    ]
    fixtures = []
    for case in local_cases:
        item = fixture(*case)
        raw_value, raw_maximizers = optimized_floor(
            raw_truncated_floor_at, item["d"], item["s"]
        )
        value, maximizers = optimized_floor(
            euler_truncated_floor_at, item["d"], item["s"]
        )
        assert item["tau"] >= value, (item, value)
        item["raw_optimized_floor"] = raw_value
        item["raw_maximizers"] = raw_maximizers
        item["optimized_floor"] = value
        item["maximizers"] = maximizers
        fixtures.append(item)

    plane_sharpness = []
    for s in range(1, 13):
        multiplicity = s + 1
        if multiplicity % 2 == 0:
            half = multiplicity // 2
            exponents = (half + 1, half)
        else:
            half_up = (multiplicity + 1) // 2
            exponents = (half_up, half_up)
        item = fixture(2, s, exponents)
        expected = plane_euler_closed_floor(s)
        assert item["tau"] == expected, (item, expected)
        item["multiplicity"] = multiplicity
        item["expected_sharp_floor"] = expected
        plane_sharpness.append(item)

    selected = [
        row
        for row in grid
        if (row["d"], row["s"])
        in {(2, 2), (2, 3), (2, 4), (2, 8), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3)}
    ]
    return {
        "scope": {
            "grid": "1 <= d <= 8 and 1 <= s <= 20",
            "claim": "finite exact-integer verification only",
        },
        "checks": {
            "optimized_floor_at_most_milnor": True,
            "Euler_reduced_floor_dominates_raw_floor": True,
            "strict_improvement_over_old_floor_for_d_s_at_least_2": True,
            "clean_K_equals_s_corollary": True,
            "plane_raw_and_Euler_reduced_closed_formulas": True,
            "all_two_prime_modular_local_fixtures_satisfy_floor": True,
            "plane_monomial_family_attains_floor_for_1_le_s_le_12": True,
        },
        "selected_grid_rows": selected,
        "two_prime_modular_local_fixtures": fixtures,
        "plane_sharpness_fixtures": plane_sharpness,
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

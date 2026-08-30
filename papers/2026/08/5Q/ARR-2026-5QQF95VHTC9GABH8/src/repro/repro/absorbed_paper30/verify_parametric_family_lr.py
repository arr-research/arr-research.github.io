#!/usr/bin/env python3
"""Independent LR-tableau replay for the Paper 30 parametric family.

This checker does not import the recursive Horn generator or the primary
parametric verifier.  It constructs the positive Littlewood--Richardson
triples by direct tableau enumeration, specializes every Horn inequality to

    lambda(t) = (4-3t,t,t,t,-1,-1,-1,-1),  0 <= t <= 1,

and checks the affine primal and dual certificates over Fraction arithmetic.
Because every residual is affine, exact checks at both endpoints of each
closed interval prove feasibility throughout that interval.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path
from typing import Any


N = 8
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "results" / "parametric_family_lr_certificate.json"

Affine = tuple[Q, Q]
Subset = tuple[int, ...]
HornKey = tuple[Any, ...]


def qtext(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def affine_text(x: Affine) -> list[str]:
    return [qtext(x[0]), qtext(x[1])]


def add(x: Affine, y: Affine) -> Affine:
    return x[0] + y[0], x[1] + y[1]


def scale(c: Q, x: Affine) -> Affine:
    return c * x[0], c * x[1]


def evaluate(x: Affine, t: Q) -> Q:
    return x[0] + x[1] * t


def subset_partition(subset: Subset) -> tuple[int, ...]:
    """Partition associated with a subset in the Horn convention."""

    r = len(subset)
    return tuple(subset[r - 1 - k] - (r - k) for k in range(r))


def lr_positive(
    lam: tuple[int, ...], mu: tuple[int, ...], nu: tuple[int, ...]
) -> bool:
    """Decide positivity of c^nu_(lam,mu) by direct LR tableaux."""

    r = len(lam)
    if any(lam[i] > nu[i] for i in range(r)):
        return False
    if sum(lam) + sum(mu) != sum(nu):
        return False
    # Reverse row-reading order: right to left, top to bottom.
    cells = [
        (row, column)
        for row in range(r)
        for column in range(nu[row], lam[row], -1)
    ]
    if not cells:
        return sum(mu) == 0

    remaining = list(mu)
    used = [0] * r
    entries: dict[tuple[int, int], int] = {}

    def visit(position: int) -> bool:
        if position == len(cells):
            return all(value == 0 for value in remaining)
        row, column = cells[position]
        right = entries.get((row, column + 1))
        above = entries.get((row - 1, column))
        for value in range(1, r + 1):
            index = value - 1
            if remaining[index] == 0:
                continue
            if right is not None and value > right:
                continue
            if above is not None and value <= above:
                continue
            remaining[index] -= 1
            used[index] += 1
            if all(used[k] >= used[k + 1] for k in range(r - 1)):
                entries[(row, column)] = value
                if visit(position + 1):
                    return True
                del entries[(row, column)]
            used[index] -= 1
            remaining[index] += 1
        return False

    return visit(0)


def lr_horn_triples() -> list[tuple[Subset, Subset, Subset]]:
    triples: list[tuple[Subset, Subset, Subset]] = []
    universe = range(1, N + 1)
    for r in range(1, N):
        subsets = list(itertools.combinations(universe, r))
        for i_set, j_set, k_set in itertools.product(subsets, repeat=3):
            if lr_positive(
                subset_partition(i_set),
                subset_partition(j_set),
                subset_partition(k_set),
            ):
                triples.append((i_set, j_set, k_set))
    return triples


LAMBDA: tuple[Affine, ...] = (
    (Q(4), Q(-3)),
    (Q(0), Q(1)),
    (Q(0), Q(1)),
    (Q(0), Q(1)),
    (Q(-1), Q(0)),
    (Q(-1), Q(0)),
    (Q(-1), Q(0)),
    (Q(-1), Q(0)),
)
GAMMA = tuple(scale(Q(2), item) for item in LAMBDA)


def build_constraints(
    triples: list[tuple[Subset, Subset, Subset]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for i_set, j_set, k_set in triples:
        r = len(i_set)
        coefficients = [Q(0)] * (N - 1)
        # alpha=(p_1,...,p_7,0), beta=(0,-p_7,...,-p_1).
        for index in i_set:
            if index < N:
                coefficients[index - 1] += 1
        for index in j_set:
            if index >= 2:
                coefficients[N - index] -= 1
        rhs = (Q(0), Q(0))
        for index in k_set:
            rhs = add(rhs, GAMMA[index - 1])
        key: HornKey = ("horn", r, i_set, j_set, k_set)
        rows.append(
            {
                "key": key,
                "display": f"H{r}:{i_set}:{j_set}:{k_set}",
                "a": tuple(coefficients),
                "rhs": rhs,
            }
        )
    for index in range(N - 2):
        coefficients = [Q(0)] * (N - 1)
        coefficients[index] = 1
        coefficients[index + 1] = -1
        rows.append(
            {
                "key": ("order", index + 1),
                "display": f"order:{index + 1}",
                "a": tuple(coefficients),
                "rhs": (Q(0), Q(0)),
            }
        )
    coefficients = [Q(0)] * (N - 1)
    coefficients[-1] = 1
    rows.append(
        {
            "key": ("nonnegative", 7),
            "display": "nonnegative",
            "a": tuple(coefficients),
            "rhs": (Q(0), Q(0)),
        }
    )
    return rows


P_LOW: tuple[Affine, ...] = (
    (Q(8), Q(-6)),
    (Q(6), Q(-6)),
    (Q(4), Q(-4)),
    (Q(2), Q(0)),
    (Q(0), Q(2)),
    (Q(0), Q(0)),
    (Q(0), Q(0)),
)
P_HIGH: tuple[Affine, ...] = (
    (Q(8), Q(-6)),
    (Q(4), Q(-2)),
    (Q(2), Q(0)),
    (Q(2), Q(0)),
    (Q(2), Q(-2)),
    (Q(0), Q(0)),
    (Q(0), Q(0)),
)
P_FACE: tuple[Affine, ...] = (
    (Q(8), Q(-6)),
    (Q(6), Q(-4)),
    (Q(4), Q(-2)),
    (Q(2), Q(0)),
    (Q(0), Q(0)),
    (Q(0), Q(0)),
    (Q(0), Q(0)),
)


LOW_DUAL: tuple[tuple[HornKey, Q], ...] = (
    (("horn", 1, (1,), (1,), (1,)), Q(1, 2)),
    (("horn", 2, (1, 2), (1, 8), (1, 8)), Q(1, 2)),
    (
        (
            "horn",
            6,
            (1, 2, 3, 5, 6, 7),
            (1, 2, 3, 5, 7, 8),
            (1, 3, 4, 6, 7, 8),
        ),
        Q(1, 2),
    ),
    (
        (
            "horn",
            7,
            (1, 2, 3, 4, 5, 6, 7),
            (1, 2, 3, 4, 6, 7, 8),
            (1, 2, 3, 4, 6, 7, 8),
        ),
        Q(1),
    ),
    (("order", 6), Q(1, 2)),
    (("nonnegative", 7), Q(1)),
)

HIGH_DUAL: tuple[tuple[HornKey, Q], ...] = (
    (("horn", 1, (1,), (1,), (1,)), Q(1, 2)),
    (
        ("horn", 4, (1, 2, 5, 6), (1, 2, 5, 8), (1, 4, 7, 8)),
        Q(1, 2),
    ),
    (
        (
            "horn",
            7,
            (1, 2, 3, 4, 5, 6, 7),
            (1, 2, 3, 4, 5, 7, 8),
            (1, 2, 3, 4, 5, 7, 8),
        ),
        Q(1, 2),
    ),
    (
        (
            "horn",
            7,
            (1, 2, 3, 4, 5, 6, 7),
            (1, 2, 3, 4, 6, 7, 8),
            (1, 2, 3, 4, 6, 7, 8),
        ),
        Q(1),
    ),
    (("nonnegative", 7), Q(1)),
)

FACE_DUAL: tuple[tuple[HornKey, Q], ...] = (
    (("horn", 1, (1,), (1,), (1,)), Q(1, 2)),
    (("horn", 3, (1, 2, 5), (1, 2, 8), (1, 4, 8)), Q(1, 2)),
    (
        (
            "horn",
            5,
            (1, 2, 3, 5, 6),
            (1, 2, 3, 7, 8),
            (1, 3, 4, 7, 8),
        ),
        Q(1, 2),
    ),
    (
        (
            "horn",
            7,
            (1, 2, 3, 4, 5, 6, 7),
            (1, 2, 3, 4, 6, 7, 8),
            (1, 2, 3, 4, 6, 7, 8),
        ),
        Q(1, 2),
    ),
)


def primal_check(
    label: str,
    p: tuple[Affine, ...],
    interval: tuple[Q, Q],
    rows: list[dict[str, Any]],
) -> tuple[dict[str, Any], list[Affine]]:
    residuals: list[Affine] = []
    records = []
    for row in rows:
        lhs = (Q(0), Q(0))
        for coefficient, item in zip(row["a"], p):
            lhs = add(lhs, scale(coefficient, item))
        residual = add(lhs, scale(Q(-1), row["rhs"]))
        endpoints = [evaluate(residual, t) for t in interval]
        assert min(endpoints) >= 0, (label, row["display"], endpoints)
        residuals.append(residual)
        records.append(
            {
                "name": row["display"],
                "residual_affine": affine_text(residual),
                "endpoint_residuals": [qtext(value) for value in endpoints],
            }
        )

    for t in interval:
        point = [evaluate(item, t) for item in p]
        assert all(point[i] >= point[i + 1] for i in range(N - 2))
        assert point[-1] >= 0

    total = (Q(0), Q(0))
    for item in p:
        total = add(total, item)
    objective = scale(Q(1, 2), total)
    stream = json.dumps(
        [[row["display"], affine_text(residual)] for row, residual in zip(rows, residuals)],
        separators=(",", ":"),
    ).encode("utf-8")
    summary = {
        "label": label,
        "interval": [qtext(t) for t in interval],
        "p_affine": [affine_text(item) for item in p],
        "objective_affine": affine_text(objective),
        "minimum_endpoint_residual": qtext(
            min(evaluate(residual, t) for residual in residuals for t in interval)
        ),
        "active_at_left": sum(evaluate(residual, interval[0]) == 0 for residual in residuals),
        "active_at_right": sum(evaluate(residual, interval[1]) == 0 for residual in residuals),
        "affine_residual_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "rows": records,
    }
    return summary, residuals


def dual_check(
    label: str,
    support: tuple[tuple[HornKey, Q], ...],
    lookup: dict[HornKey, dict[str, Any]],
    variable_count: int,
    expected: Affine,
) -> dict[str, Any]:
    coefficients = [Q(0)] * (N - 1)
    rhs = (Q(0), Q(0))
    weights = []
    for key, weight in support:
        assert weight >= 0
        row = lookup[key]
        coefficients = [
            current + weight * coefficient
            for current, coefficient in zip(coefficients, row["a"])
        ]
        rhs = add(rhs, scale(weight, row["rhs"]))
        weights.append([row["display"], qtext(weight)])
    assert coefficients[:variable_count] == [Q(1, 2)] * variable_count
    assert rhs == expected, (label, rhs, expected)
    return {
        "label": label,
        "weights": weights,
        "combined_coefficients": [qtext(value) for value in coefficients],
        "lower_bound_affine": affine_text(rhs),
    }


def main() -> None:
    # The spectral family is ordered and traceless throughout [0,1].
    assert add(add(add(LAMBDA[0], LAMBDA[1]), add(LAMBDA[2], LAMBDA[3])),
               add(add(LAMBDA[4], LAMBDA[5]), add(LAMBDA[6], LAMBDA[7]))) == (Q(0), Q(0))
    for t in (Q(0), Q(1, 2), Q(1)):
        spectrum = [evaluate(item, t) for item in LAMBDA]
        assert spectrum == sorted(spectrum, reverse=True)

    triples = lr_horn_triples()
    counts = {r: sum(len(i_set) == r for i_set, _, _ in triples) for r in range(1, N)}
    assert counts == {1: 36, 2: 462, 3: 2120, 4: 3516, 5: 2120, 6: 462, 7: 36}
    rows = build_constraints(triples)
    assert len(rows) == 8759
    assert len({row["key"] for row in rows}) == 8759

    canonical_names = [row["key"] for row in rows]
    canonical_hash = hashlib.sha256(
        json.dumps(canonical_names, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    assert canonical_hash == "833c6e2c9e2c5d78001572ad9975d64212254d7acc37af69a02cf4c999806bb8"

    low, _ = primal_check("unrestricted_low", P_LOW, (Q(0), Q(1, 2)), rows)
    high, _ = primal_check("unrestricted_high", P_HIGH, (Q(1, 2), Q(1)), rows)
    face, _ = primal_check("rank_at_most_four", P_FACE, (Q(0), Q(1)), rows)

    # The two unrestricted affine spectra meet exactly at the breakpoint.
    assert [evaluate(item, Q(1, 2)) for item in P_LOW] == [
        evaluate(item, Q(1, 2)) for item in P_HIGH
    ]
    assert low["objective_affine"] == ["10", "-7"]
    assert high["objective_affine"] == ["9", "-5"]
    assert face["objective_affine"] == ["10", "-6"]

    lookup = {row["key"]: row for row in rows}
    duals = [
        dual_check("unrestricted_low", LOW_DUAL, lookup, 7, (Q(10), Q(-7))),
        dual_check("unrestricted_high", HIGH_DUAL, lookup, 7, (Q(9), Q(-5))),
        dual_check("rank_at_most_four", FACE_DUAL, lookup, 4, (Q(10), Q(-6))),
    ]

    # Exact endpoint and rank logic for the claimed gap.
    for t in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
        full_value = Q(10) - 7 * t if t <= Q(1, 2) else Q(9) - 5 * t
        face_value = Q(10) - 6 * t
        assert face_value - full_value == min(t, Q(1) - t)
    assert sum(evaluate(item, Q(0)) > 0 for item in P_LOW) == 4
    assert sum(evaluate(item, Q(1, 2)) > 0 for item in P_LOW) == 5
    assert sum(evaluate(item, Q(1)) > 0 for item in P_HIGH) == 4
    assert all(sum(evaluate(item, t) > 0 for item in P_LOW) == 5
               for t in (Q(1, 4), Q(1, 2)))
    assert all(sum(evaluate(item, t) > 0 for item in P_HIGH) == 5
               for t in (Q(1, 2), Q(3, 4)))

    payload = {
        "status": "PASS",
        "engine": "direct Littlewood-Richardson tableau enumeration; fractions.Fraction",
        "independence": "imports neither the recursive Horn generator nor the primary family verifier",
        "family": "lambda(t)=(4-3t,t,t,t,-1,-1,-1,-1), 0<=t<=1",
        "scope": "exact d=8 one-parameter family; no smallest-dimension claim",
        "horn_counts": {str(r): counts[r] for r in range(1, N)},
        "constraint_count": len(rows),
        "canonical_constraint_names_sha256": canonical_hash,
        "primal_chambers": [low, high, face],
        "duals": duals,
        "unrestricted_value": {"0<=t<=1/2": "10-7t", "1/2<=t<=1": "9-5t"},
        "rank4_value": "10-6t",
        "gap": "min(t,1-t)",
        "minimum_optimal_rank": "5 for 0<t<1; 4 at t=0,1",
        "limitations": [
            "does not prove that dimension eight is the first failing dimension",
            "does not classify spectra outside the displayed family",
            "uses the classical Horn existence theorem rather than constructing matrix entries",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(text, encoding="utf-8", newline="\n")
    print("PASS: independent LR-tableau enumeration produced 8,752 Horn triples")
    print("PASS: all affine residuals are nonnegative by exact endpoint checks")
    print("PASS: all three sparse dual identities hold symbolically")
    print("PASS: kappa=10-7t / 9-5t; rank<=4=10-6t; gap=min(t,1-t)")
    print(f"JSON_SHA256: {hashlib.sha256(text.encode('utf-8')).hexdigest()}")
    print(f"WROTE: {OUTPUT}")


if __name__ == "__main__":
    main()

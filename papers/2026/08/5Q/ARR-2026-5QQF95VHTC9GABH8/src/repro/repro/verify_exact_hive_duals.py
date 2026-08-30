#!/usr/bin/env python3
"""Dependency-free exact verifier for the frozen finite hive certificates.

This checker does not import the floating extractor and never invokes an LP
solver.  It reconstructs the full hive system from scratch and evaluates all
identities with ``fractions.Fraction``.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "exact_hive_duals.json"
EXPECTED_SHA256 = "c6b3588a2415db067f7ff34f7e23592ac9d85f3e10399dd0f8838fc244352b69"
EXPECTED_CASES = {(2, 1): (11, 59), (3, 1): (16, 89), (3, 2): (17, 88)}


def Q(text: str | int) -> Fraction:
    return Fraction(text)


class ExactHive:
    def __init__(self, copies: int, rank_cap: int):
        self.copies = copies
        self.n = 9 * copies
        self.rank_cap = rank_cap
        self.nodes = [(i, level) for level in range(self.n + 1) for i in range(level + 1)]
        self.node_index = {node: index for index, node in enumerate(self.nodes)}
        self.p_offset = len(self.nodes)
        self.variable_count = self.p_offset + self.n - 1
        self.equalities: list[tuple[tuple, dict[int, int], int]] = []
        self.inequalities: list[tuple[tuple, dict[int, int]]] = []
        self._construct()

    def t(self, i: int, level: int) -> int:
        return self.node_index[(i, level)]

    def p(self, j: int) -> int:
        if not 1 <= j < self.n:
            raise ValueError(j)
        return self.p_offset + j - 1

    @staticmethod
    def make_row(terms: tuple[tuple[int, int], ...], scale: int = 1) -> dict[int, int]:
        row: dict[int, int] = {}
        for index, coefficient in terms:
            row[index] = row.get(index, 0) + scale * coefficient
        return {index: coefficient for index, coefficient in row.items() if coefficient}

    def eq(self, name: tuple, *terms: tuple[int, int], rhs: int = 0) -> None:
        self.equalities.append((name, self.make_row(terms), rhs))

    def ge(self, name: tuple, *terms: tuple[int, int]) -> None:
        # Convert the displayed >=0 rhombus/order relation into A_ub x <=0.
        self.inequalities.append((name, self.make_row(terms, -1)))

    def _construct(self) -> None:
        n = self.n
        self.eq(("origin",), (self.t(0, 0), 1))
        for j in range(1, n + 1):
            terms = [(self.t(0, j), 1), (self.t(0, j - 1), -1)]
            if j < n:
                terms.append((self.p(j), -1))
            self.eq(("alpha", j), *terms)
        for j in range(1, n + 1):
            terms = [(self.t(j, n), 1), (self.t(j - 1, n), -1)]
            if j >= 2:
                terms.append((self.p(n - j + 1), 1))
            self.eq(("beta", j), *terms)
        gamma = [10] * (4 * self.copies) + [-8] * (5 * self.copies)
        for j, rhs in enumerate(gamma, start=1):
            self.eq(
                ("gamma", j),
                (self.t(j, j), 1),
                (self.t(j - 1, j - 1), -1),
                rhs=rhs,
            )
        for level in range(1, n):
            for i in range(1, level + 1):
                self.ge(
                    ("rhombus", 1, level, i),
                    (self.t(i, level + 1), 1), (self.t(i - 1, level), 1),
                    (self.t(i - 1, level + 1), -1), (self.t(i, level), -1),
                )
                self.ge(
                    ("rhombus", 2, level, i),
                    (self.t(i, level + 1), 1), (self.t(i, level), 1),
                    (self.t(i + 1, level + 1), -1), (self.t(i - 1, level), -1),
                )
                self.ge(
                    ("rhombus", 3, level, i),
                    (self.t(i, level), 1), (self.t(i - 1, level), 1),
                    (self.t(i, level + 1), -1), (self.t(i - 1, level - 1), -1),
                )
        for j in range(1, n - 1):
            self.ge(("order", j), (self.p(j), 1), (self.p(j + 1), -1))
        self.ge(("nonnegative",), (self.p(n - 1), 1))


def positional(entries: list[dict], size: int) -> list[Fraction]:
    vector = [Fraction(0) for _ in range(size)]
    seen: set[int] = set()
    for entry in entries:
        index = int(entry["index"])
        if index in seen or not 0 <= index < size:
            raise AssertionError(f"bad or duplicate positional index {index}")
        seen.add(index)
        value = Q(entry["value"])
        if not value:
            raise AssertionError("sparse certificate contains zero")
        vector[index] = value
    return vector


def named(entries: list[dict], canonical: list[tuple]) -> list[Fraction]:
    positions = {name: index for index, name in enumerate(canonical)}
    if len(positions) != len(canonical):
        raise AssertionError("canonical names are not unique")
    vector = [Fraction(0) for _ in canonical]
    seen: set[tuple] = set()
    for entry in entries:
        name = tuple(entry["name"])
        if name in seen or name not in positions:
            raise AssertionError(f"bad or duplicate named row {name}")
        seen.add(name)
        value = Q(entry["value"])
        if not value:
            raise AssertionError("sparse certificate contains zero")
        vector[positions[name]] = value
    return vector


def dot(row: dict[int, int], vector: list[Fraction]) -> Fraction:
    return sum(Fraction(coefficient) * vector[index] for index, coefficient in row.items())


def verify_case(case: dict) -> dict:
    copies, j = int(case["copies"]), int(case["j"])
    if (copies, j) not in EXPECTED_CASES:
        raise AssertionError(f"unexpected case {(copies, j)}")
    rank_cap, expected = EXPECTED_CASES[(copies, j)]
    if (case["rank_cap"], case["expected_value"]) != (rank_cap, expected):
        raise AssertionError("case metadata mismatch")
    hive = ExactHive(copies, rank_cap)
    if case["dimension"] != hive.n or case["variable_count"] != hive.variable_count:
        raise AssertionError("layout metadata mismatch")
    if case["equality_count"] != len(hive.equalities) or case["inequality_count"] != len(hive.inequalities):
        raise AssertionError("row-count metadata mismatch")

    x = positional(case["primal_nonzero"], hive.variable_count)
    y = named(case["equality_dual_nonzero"], [row[0] for row in hive.equalities])
    z = named(case["inequality_dual_nonzero"], [row[0] for row in hive.inequalities])
    w = positional(case["fixed_coordinate_dual_nonzero"], hive.variable_count)

    # Primal certificate.
    for _, row, rhs in hive.equalities:
        if dot(row, x) != rhs:
            raise AssertionError("primal equality residual")
    for name, row in hive.inequalities:
        if dot(row, x) > 0:
            raise AssertionError(f"primal inequality residual at {name}")
    fixed = {hive.p(index) for index in range(rank_cap + 1, hive.n)}
    if any(x[index] for index in fixed):
        raise AssertionError("rank-face coordinate is nonzero")
    objective_value = sum(x[hive.p(index)] for index in range(1, hive.n)) / 2
    if objective_value != expected:
        raise AssertionError("primal objective mismatch")

    # Dual certificate.  Because each row is A_ub x<=0, valid multipliers
    # satisfy z<=0.  The free w multipliers may occur only where x is fixed 0.
    if any(multiplier > 0 for multiplier in z):
        raise AssertionError("dual inequality multiplier has wrong sign")
    if any(multiplier for index, multiplier in enumerate(w) if index not in fixed):
        raise AssertionError("bound multiplier outside the fixed rank face")
    stationarity = [Fraction(0) for _ in range(hive.variable_count)]
    for multiplier, (_, row, _) in zip(y, hive.equalities):
        for index, coefficient in row.items():
            stationarity[index] += multiplier * coefficient
    for multiplier, (_, row) in zip(z, hive.inequalities):
        for index, coefficient in row.items():
            stationarity[index] += multiplier * coefficient
    for index, multiplier in enumerate(w):
        stationarity[index] += multiplier
    objective = [Fraction(0)] * hive.p_offset + [Fraction(1, 2)] * (hive.n - 1)
    if stationarity != objective:
        bad = [i for i, (left, right) in enumerate(zip(stationarity, objective)) if left != right]
        raise AssertionError(f"dual stationarity residual at {bad[:5]}")
    dual_value = sum(multiplier * rhs for multiplier, (_, _, rhs) in zip(y, hive.equalities))
    if dual_value != expected:
        raise AssertionError("dual RHS mismatch")

    summary = case["support_summary"]
    observed_summary = {
        "primal": sum(value != 0 for value in x),
        "equalities": sum(value != 0 for value in y),
        "inequalities": sum(value != 0 for value in z),
        "fixed_coordinates": sum(value != 0 for value in w),
        "dual_max_denominator": max(value.denominator for value in y + z + w),
    }
    if summary != observed_summary:
        raise AssertionError("support summary mismatch")
    return observed_summary


def main() -> None:
    raw = CERTIFICATE.read_bytes()
    observed_hash = hashlib.sha256(raw).hexdigest()
    if observed_hash != EXPECTED_SHA256:
        raise SystemExit(f"certificate hash mismatch: {observed_hash} != {EXPECTED_SHA256}")
    payload = json.loads(raw)
    if payload.get("status") != "PASS" or len(payload.get("cases", [])) != len(EXPECTED_CASES):
        raise SystemExit("certificate envelope mismatch")
    seen: set[tuple[int, int]] = set()
    for case in payload["cases"]:
        key = (case["copies"], case["j"])
        if key in seen:
            raise AssertionError(f"duplicate case {key}")
        seen.add(key)
        summary = verify_case(case)
        print(
            f"PASS exact hive primal+dual: k={key[0]} j={key[1]} rank={case['rank_cap']} "
            f"value={case['expected_value']} supports={summary['equalities']}+"
            f"{summary['inequalities']}+{summary['fixed_coordinates']}"
        )
    if seen != set(EXPECTED_CASES):
        raise AssertionError("missing finite regression case")
    print("PASS finite exact hive audit; no all-k claim")


if __name__ == "__main__":
    main()

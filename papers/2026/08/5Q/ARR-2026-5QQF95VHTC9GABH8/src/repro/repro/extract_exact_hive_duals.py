#!/usr/bin/env python3
"""Extract floating hive LP optima and freeze exact rational certificates.

SciPy/HiGHS is used only to propose primal and dual vectors.  Before anything
is written, every equality, inequality, sign, fixed-coordinate, stationarity,
and objective identity is rechecked over ``fractions.Fraction``.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "exact_hive_duals.json"
CASES = ((2, 1, 59), (3, 1, 89), (3, 2, 88))
MAX_DENOMINATOR = 4096


def q(value: float) -> Fraction:
    if abs(value) < 1e-9:
        return Fraction(0)
    candidate = Fraction(float(value)).limit_denominator(MAX_DENOMINATOR)
    if abs(float(candidate) - value) > 1e-8:
        raise RuntimeError(f"failed to rationalize {value!r}")
    return candidate


def qs(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


class System:
    def __init__(self, copies: int, rank: int):
        self.copies = copies
        self.n = 9 * copies
        self.rank = rank
        self.nodes = [(i, level) for level in range(self.n + 1) for i in range(level + 1)]
        self.node_index = {node: index for index, node in enumerate(self.nodes)}
        self.p_offset = len(self.nodes)
        self.variable_count = self.p_offset + self.n - 1
        self.gamma = [10] * (4 * copies) + [-8] * (5 * copies)
        self.equalities: list[tuple[tuple, dict[int, int], int]] = []
        self.inequalities: list[tuple[tuple, dict[int, int]]] = []
        self._build()

    def t(self, i: int, level: int) -> int:
        return self.node_index[(i, level)]

    def p(self, one_based: int) -> int:
        assert 1 <= one_based < self.n
        return self.p_offset + one_based - 1

    @staticmethod
    def row(terms: list[tuple[int, int]], negate: bool = False) -> dict[int, int]:
        result: dict[int, int] = {}
        sign = -1 if negate else 1
        for index, coefficient in terms:
            result[index] = result.get(index, 0) + sign * coefficient
        return {index: coefficient for index, coefficient in result.items() if coefficient}

    def equality(self, name: tuple, terms: list[tuple[int, int]], rhs: int = 0) -> None:
        self.equalities.append((name, self.row(terms), rhs))

    def ge(self, name: tuple, terms: list[tuple[int, int]]) -> None:
        # Stored in scipy form A_ub x <= 0.
        self.inequalities.append((name, self.row(terms, negate=True)))

    def _build(self) -> None:
        n = self.n
        self.equality(("origin",), [(self.t(0, 0), 1)])
        for j in range(1, n + 1):
            terms = [(self.t(0, j), 1), (self.t(0, j - 1), -1)]
            if j < n:
                terms.append((self.p(j), -1))
            self.equality(("alpha", j), terms)
        for j in range(1, n + 1):
            terms = [(self.t(j, n), 1), (self.t(j - 1, n), -1)]
            if j >= 2:
                terms.append((self.p(n - j + 1), 1))
            self.equality(("beta", j), terms)
        for j in range(1, n + 1):
            self.equality(
                ("gamma", j),
                [(self.t(j, j), 1), (self.t(j - 1, j - 1), -1)],
                self.gamma[j - 1],
            )
        for level in range(1, n):
            for i in range(1, level + 1):
                self.ge(("rhombus", 1, level, i), [
                    (self.t(i, level + 1), 1), (self.t(i - 1, level), 1),
                    (self.t(i - 1, level + 1), -1), (self.t(i, level), -1),
                ])
                self.ge(("rhombus", 2, level, i), [
                    (self.t(i, level + 1), 1), (self.t(i, level), 1),
                    (self.t(i + 1, level + 1), -1), (self.t(i - 1, level), -1),
                ])
                self.ge(("rhombus", 3, level, i), [
                    (self.t(i, level), 1), (self.t(i - 1, level), 1),
                    (self.t(i, level + 1), -1), (self.t(i - 1, level - 1), -1),
                ])
        for j in range(1, n - 1):
            self.ge(("order", j), [(self.p(j), 1), (self.p(j + 1), -1)])
        self.ge(("nonnegative",), [(self.p(n - 1), 1)])

    def dense(self, rows: list[tuple]) -> np.ndarray:
        matrix = np.zeros((len(rows), self.variable_count))
        for i, item in enumerate(rows):
            row = item[1]
            for j, coefficient in row.items():
                matrix[i, j] = coefficient
        return matrix

    def solve(self):
        objective = np.zeros(self.variable_count)
        objective[self.p_offset:] = 0.5
        bounds = [(None, None)] * self.variable_count
        for j in range(self.rank + 1, self.n):
            bounds[self.p(j)] = (0.0, 0.0)
        return linprog(
            objective,
            A_ub=self.dense(self.inequalities),
            b_ub=np.zeros(len(self.inequalities)),
            A_eq=self.dense(self.equalities),
            b_eq=np.asarray([item[2] for item in self.equalities], dtype=float),
            bounds=bounds,
            method="highs-ds",
        )


def sparse_vector(values: list[Fraction]) -> list[dict]:
    return [{"index": i, "value": qs(value)} for i, value in enumerate(values) if value]


def named_vector(names: list[tuple], values: list[Fraction]) -> list[dict]:
    return [{"name": list(name), "value": qs(value)} for name, value in zip(names, values) if value]


def verify_and_serialize(system: System, expected: int) -> dict:
    result = system.solve()
    if not result.success:
        raise RuntimeError(result.message)
    if abs(result.fun - expected) > 1e-8:
        raise RuntimeError(f"unexpected float optimum {result.fun} != {expected}")

    primal = [q(value) for value in result.x]
    y = [q(value) for value in result.eqlin.marginals]
    z = [q(value) for value in result.ineqlin.marginals]
    bound = [q(lo + hi) for lo, hi in zip(result.lower.marginals, result.upper.marginals)]

    # Exact primal feasibility.
    for _, row, rhs in system.equalities:
        assert sum(Fraction(a) * primal[i] for i, a in row.items()) == rhs
    for _, row in system.inequalities:
        assert sum(Fraction(a) * primal[i] for i, a in row.items()) <= 0
    for j in range(system.rank + 1, system.n):
        assert primal[system.p(j)] == 0
    primal_objective = sum(primal[system.p(j)] for j in range(1, system.n)) / 2
    assert primal_objective == expected

    # Exact dual signs, support, stationarity, and value.
    assert all(value <= 0 for value in z)
    fixed = {system.p(j) for j in range(system.rank + 1, system.n)}
    assert all(value == 0 for i, value in enumerate(bound) if i not in fixed)
    stationarity = [Fraction(0) for _ in range(system.variable_count)]
    for multiplier, (_, row, _) in zip(y, system.equalities):
        for i, coefficient in row.items():
            stationarity[i] += multiplier * coefficient
    for multiplier, (_, row) in zip(z, system.inequalities):
        for i, coefficient in row.items():
            stationarity[i] += multiplier * coefficient
    for i, multiplier in enumerate(bound):
        stationarity[i] += multiplier
    objective = [Fraction(0)] * system.p_offset + [Fraction(1, 2)] * (system.n - 1)
    assert stationarity == objective
    dual_value = sum(multiplier * rhs for multiplier, (_, _, rhs) in zip(y, system.equalities))
    assert dual_value == expected

    return {
        "copies": system.copies,
        "j": system.rank - 5 * system.copies,
        "dimension": system.n,
        "rank_cap": system.rank,
        "expected_value": expected,
        "variable_count": system.variable_count,
        "equality_count": len(system.equalities),
        "inequality_count": len(system.inequalities),
        "primal_nonzero": sparse_vector(primal),
        "equality_dual_nonzero": named_vector([item[0] for item in system.equalities], y),
        "inequality_dual_nonzero": named_vector([item[0] for item in system.inequalities], z),
        "fixed_coordinate_dual_nonzero": sparse_vector(bound),
        "support_summary": {
            "primal": sum(value != 0 for value in primal),
            "equalities": sum(value != 0 for value in y),
            "inequalities": sum(value != 0 for value in z),
            "fixed_coordinates": sum(value != 0 for value in bound),
            "dual_max_denominator": max(value.denominator for value in y + z + bound),
        },
    }


def main() -> None:
    cases = [verify_and_serialize(System(copies, 5 * copies + j), expected) for copies, j, expected in CASES]
    payload = {
        "schema_version": 1,
        "status": "PASS",
        "scope": "finite exact hive-LP certificates only; no all-k assertion",
        "sign_convention": "min c.x, Aeq.x=b, Aub.x<=0: c=Aeq^T y+Aub^T z+w, z<=0, w on x_fixed=0",
        "cases": cases,
    }
    data = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    OUTPUT.write_bytes(data)
    print(f"PASS: froze {len(cases)} exact primal/dual certificates")
    for case in cases:
        print(
            f"  k={case['copies']} j={case['j']} rank={case['rank_cap']} value={case['expected_value']} "
            f"dual-support={case['support_summary']['equalities']}+{case['support_summary']['inequalities']}+"
            f"{case['support_summary']['fixed_coordinates']} denom<={case['support_summary']['dual_max_denominator']}"
        )
    print(f"SHA256 {hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()

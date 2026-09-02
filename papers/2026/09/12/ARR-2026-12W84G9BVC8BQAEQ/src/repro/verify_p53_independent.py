#!/usr/bin/env python3
"""Independent standard-library replay of the p=53 cost-and-rank theorem.

This verifier deliberately shares no row builder or import with the discovery
code or the primary replay.  It reconstructs canonical hive rows on demand
from their names and checks the frozen primal and both duals over Fraction.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRIMAL = HERE / "p53_rank115_primal_certificate.json"
FULL = HERE / "p53_unrestricted_dual_certificate.json"
RANK114 = HERE / "p53_rank114_dual_certificate.json"
N = 160
P = 53
QNEG = 107
NODE_COUNT = (N + 1) * (N + 2) // 2
VARIABLE_COUNT = NODE_COUNT + N - 1


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def frac(value: object) -> Q:
    return Q(str(value))


def node(i: int, level: int) -> int:
    require(0 <= i <= level <= N, "invalid triangular coordinate")
    return level * (level + 1) // 2 + i


def spectral(j: int) -> int:
    require(1 <= j < N, "invalid spectral coordinate")
    return NODE_COUNT + j - 1


def combine(terms: list[tuple[int, int]], sign: int = 1) -> dict[int, int]:
    row: dict[int, int] = {}
    for index, coefficient in terms:
        row[index] = row.get(index, 0) + sign * coefficient
    return {index: coefficient for index, coefficient in row.items() if coefficient}


def equality(name: tuple) -> tuple[dict[int, int], int]:
    family = name[0]
    if family == "origin" and len(name) == 1:
        return {node(0, 0): 1}, 0
    require(len(name) == 2, f"malformed equality {name}")
    j = int(name[1])
    require(1 <= j <= N, f"invalid equality index {name}")
    if family == "alpha":
        terms = [(node(0, j), 1), (node(0, j - 1), -1)]
        if j < N:
            terms.append((spectral(j), -1))
        return combine(terms), 0
    if family == "beta":
        terms = [(node(j, N), 1), (node(j - 1, N), -1)]
        if j >= 2:
            terms.append((spectral(N - j + 1), 1))
        return combine(terms), 0
    require(family == "gamma", f"unknown equality {name}")
    gamma = QNEG if j <= P else -P
    return combine([(node(j, j), 1), (node(j - 1, j - 1), -1)]), gamma


def inequality(name: tuple) -> dict[int, int]:
    family = name[0]
    if family == "nonnegative" and len(name) == 1:
        return {spectral(N - 1): -1}
    if family == "order" and len(name) == 2:
        j = int(name[1])
        require(1 <= j < N - 1, f"invalid order row {name}")
        return combine([(spectral(j), 1), (spectral(j + 1), -1)], -1)
    require(family == "rhombus" and len(name) == 4, f"unknown inequality {name}")
    kind, level, i = map(int, name[1:])
    require(1 <= level < N and 1 <= i <= level and 1 <= kind <= 3,
            f"invalid rhombus row {name}")
    if kind == 1:
        terms = [(node(i, level + 1), 1), (node(i - 1, level), 1),
                 (node(i - 1, level + 1), -1), (node(i, level), -1)]
    elif kind == 2:
        terms = [(node(i, level + 1), 1), (node(i, level), 1),
                 (node(i + 1, level + 1), -1), (node(i - 1, level), -1)]
    else:
        terms = [(node(i, level), 1), (node(i - 1, level), 1),
                 (node(i, level + 1), -1), (node(i - 1, level - 1), -1)]
    return combine(terms, -1)


def equality_names():
    yield ("origin",)
    for family in ("alpha", "beta", "gamma"):
        for j in range(1, N + 1):
            yield (family, j)


def inequality_names():
    for level in range(1, N):
        for i in range(1, level + 1):
            for kind in (1, 2, 3):
                yield ("rhombus", kind, level, i)
    for j in range(1, N - 1):
        yield ("order", j)
    yield ("nonnegative",)


def canonical_hash(payload: dict) -> str:
    body = dict(payload)
    expected = body.pop("certificate_sha256")
    stream = json.dumps(body, sort_keys=True, separators=(",", ":"))
    actual = hashlib.sha256(stream.encode()).hexdigest()
    require(actual == expected, "canonical certificate hash mismatch")
    return actual


def dot(row: dict[int, int], vector: list[Q]) -> Q:
    return sum(Q(coefficient) * vector[index] for index, coefficient in row.items())


def verify_primal() -> dict:
    payload = json.loads(PRIMAL.read_text(encoding="utf-8"))
    require(payload.get("status") == "PASS", "primal status is not PASS")
    canonical_hash(payload)
    vector = [Q(0)] * VARIABLE_COUNT
    seen: set[int] = set()
    for raw_index, raw_value in payload["primal"]:
        index = int(raw_index)
        require(0 <= index < VARIABLE_COUNT and index not in seen, "bad primal index")
        seen.add(index)
        vector[index] = frac(raw_value)
    eq_count = 0
    for name in equality_names():
        row, rhs = equality(name)
        require(dot(row, vector) == rhs, f"primal equality failure {name}")
        eq_count += 1
    ineq_count = tight = 0
    for name in inequality_names():
        value = dot(inequality(name), vector)
        require(value <= 0, f"primal inequality failure {name}: {value}")
        tight += value == 0
        ineq_count += 1
    spectrum = [vector[spectral(j)] for j in range(1, N)] + [Q(0)]
    require(spectrum == [frac(value) for value in payload["positive_spectrum"]],
            "primal spectrum mismatch")
    require(spectrum == sorted(spectrum, reverse=True), "unordered primal spectrum")
    require(sum(spectrum) == 8847 and sum(value > 0 for value in spectrum) == 115,
            "wrong primal trace or rank")
    require(eq_count == 481 and ineq_count == 38319 and tight == 34589,
            "unexpected hive inventory")
    return {"equalities": eq_count, "inequalities": ineq_count, "tight": tight}


def add_scaled(total: list[Q], row: dict[int, int], multiplier: Q) -> None:
    for index, coefficient in row.items():
        total[index] += multiplier * coefficient


def verify_dual(path: Path, rank_cap: int | None, expected: int) -> int:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(payload.get("status") == "PASS" and payload["rank_cap"] == rank_cap,
            f"bad dual header {path.name}")
    canonical_hash(payload)
    stationarity = [Q(0)] * VARIABLE_COUNT
    objective = Q(0)
    names_seen: set[tuple[str, tuple]] = set()
    for raw_name, raw_value in payload["equality_dual"]:
        name = tuple(raw_name)
        key = ("eq", name)
        require(key not in names_seen, "duplicate dual equality")
        names_seen.add(key)
        row, rhs = equality(name)
        multiplier = frac(raw_value)
        add_scaled(stationarity, row, multiplier)
        objective += multiplier * rhs
    for raw_name, raw_value in payload["inequality_dual"]:
        name = tuple(raw_name)
        key = ("ineq", name)
        require(key not in names_seen, "duplicate dual inequality")
        names_seen.add(key)
        multiplier = frac(raw_value)
        require(multiplier < 0, "wrong inequality-dual sign")
        add_scaled(stationarity, inequality(name), multiplier)
    fixed_seen: set[int] = set()
    for raw_index, raw_value in payload["fixed_bound_dual"]:
        index = int(raw_index)
        require(rank_cap is not None and index not in fixed_seen, "bad fixed-bound dual")
        fixed_seen.add(index)
        require(spectral(rank_cap + 1) <= index < VARIABLE_COUNT, "fixed bound outside tail")
        stationarity[index] += frac(raw_value)
    target = [Q(0)] * VARIABLE_COUNT
    for j in range(1, N):
        target[spectral(j)] = Q(1, 2)
    require(stationarity == target, f"dual stationarity failure {path.name}")
    require(objective == Q(expected, 2), f"dual objective failure {path.name}")
    require(frac(payload["paper_kappa_lower"]) == expected, "stored lower bound mismatch")
    return len(names_seen) + len(fixed_seen)


def main() -> None:
    if not __debug__:
        raise SystemExit("refusing optimized Python: exact replay requires __debug__")
    primal = verify_primal()
    full_support = verify_dual(FULL, None, 8847)
    rank_support = verify_dual(RANK114, 114, 8848)
    print(
        "PASS independent p=53 replay: "
        f"primal={primal['equalities']}+{primal['inequalities']} "
        f"dual_supports={full_support},{rank_support} "
        "kappa=8847 minimum_rank=115"
    )


if __name__ == "__main__":
    main()

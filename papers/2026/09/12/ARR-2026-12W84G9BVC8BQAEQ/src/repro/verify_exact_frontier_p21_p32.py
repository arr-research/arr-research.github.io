#!/usr/bin/env python3
"""Exact standard-library replay of the complete frontier 21 <= p <= 32."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from verify_p28_exact_duals import HiveRows, add_scaled, require
EXPECTED = {
    21: (1461, 45, 1462), 22: (1598, 47, 1599),
    23: (1741, 49, 1742), 24: (1890, 51, 1891),
    25: (2045, 53, 2047), 26: (2206, 55, 2209),
    27: (2373, 58, 2374), 28: (2546, 61, 2547),
    29: (2726, 63, 2727), 30: (2912, 65, 2913),
    31: (3104, 67, 3105), 32: (3302, 69, 3303),
}


def frac(value: object) -> Q:
    return Q(str(value))


def canonical_hash(payload: dict) -> str:
    body = dict(payload)
    expected = body.pop("certificate_sha256")
    stream = json.dumps(body, sort_keys=True, separators=(",", ":"))
    actual = hashlib.sha256(stream.encode()).hexdigest()
    require(actual == expected, "canonical certificate hash mismatch")
    return actual


def full_path(p: int) -> Path:
    if p == 24:
        return HERE / "basis_dual_l1_p24.json"
    if p == 28:
        return HERE / "basis_dual_l1_p28.json"
    return HERE / f"basis_dual_l1_p{p}_full.json"


def primal_path(p: int, rank: int) -> Path:
    return HERE / f"primal_p{p}_rank{rank}.json"


def predecessor_path(p: int, rank: int) -> Path:
    return HERE / f"basis_dual_l1_p{p}_rank{rank - 1}.json"


def verify_primal(path: Path, rows: HiveRows, expected_kappa: int,
                  expected_rank: int) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(payload.get("status") == "PASS", f"{path.name}: primal status")
    certificate_hash = canonical_hash(payload)
    vector = [Q(0)] * rows.variable_count
    seen: set[int] = set()
    for raw_index, raw_value in payload["primal"]:
        index = int(raw_index)
        require(index not in seen, f"{path.name}: duplicate primal index")
        seen.add(index)
        vector[index] = frac(raw_value)
    for name, (row, rhs) in rows.equalities.items():
        require(sum(Q(a) * vector[index] for index, a in row.items()) == rhs,
                f"{path.name}: equality {name}")
    tight = 0
    for name, row in rows.inequalities.items():
        value = sum(Q(a) * vector[index] for index, a in row.items())
        require(value <= 0, f"{path.name}: inequality {name}")
        tight += value == 0
    spectrum = [vector[rows.pv(j)] for j in range(1, rows.n)] + [Q(0)]
    require(spectrum == [frac(value) for value in payload["positive_spectrum"]],
            f"{path.name}: spectrum mismatch")
    require(spectrum == sorted(spectrum, reverse=True), f"{path.name}: order")
    require(sum(spectrum) == expected_kappa, f"{path.name}: trace")
    require(sum(value > 0 for value in spectrum) == expected_rank, f"{path.name}: rank")
    return {"hash": certificate_hash, "tight": tight}


def verify_dual(path: Path, rows: HiveRows, rank_cap: int | None,
                expected_kappa: int) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(payload.get("status") == "PASS", f"{path.name}: dual status")
    require(payload["rank_cap"] == rank_cap, f"{path.name}: rank cap")
    require(frac(payload["paper_kappa_for_2F"]) == expected_kappa,
            f"{path.name}: stored value")
    certificate_hash = canonical_hash(payload)
    stationarity = [Q(0)] * rows.variable_count
    objective = Q(0)
    seen: set[tuple[str, tuple | int]] = set()
    for raw_name, raw_value in payload["equality_dual"]:
        name = tuple(raw_name)
        key = ("eq", name)
        require(name in rows.equalities and key not in seen, f"{path.name}: equality name")
        seen.add(key)
        multiplier = frac(raw_value)
        row, rhs = rows.equalities[name]
        add_scaled(stationarity, row, multiplier)
        objective += multiplier * rhs
    for raw_name, raw_value in payload["inequality_dual"]:
        name = tuple(raw_name)
        key = ("ineq", name)
        require(name in rows.inequalities and key not in seen, f"{path.name}: inequality name")
        seen.add(key)
        multiplier = frac(raw_value)
        require(multiplier < 0, f"{path.name}: inequality sign")
        add_scaled(stationarity, rows.inequalities[name], multiplier)
    for raw_index, raw_value in payload["fixed_bound_dual"]:
        index = int(raw_index)
        key = ("fixed", index)
        require(rank_cap is not None and key not in seen, f"{path.name}: fixed bound")
        require(rows.pv(rank_cap + 1) <= index < rows.variable_count,
                f"{path.name}: fixed bound outside tail")
        seen.add(key)
        stationarity[index] += frac(raw_value)
    target = [Q(0)] * rows.variable_count
    for j in range(1, rows.n):
        target[rows.pv(j)] = Q(1, 2)
    require(stationarity == target, f"{path.name}: stationarity")
    require(objective == Q(expected_kappa, 2), f"{path.name}: objective")
    return {"hash": certificate_hash, "support": len(seen)}


def main() -> None:
    if not __debug__:
        raise SystemExit("refusing optimized Python: exact replay requires __debug__")
    records = []
    for p, (kappa, rank, predecessor) in EXPECTED.items():
        rows = HiveRows(p, 2 * p + 1)
        primal = verify_primal(primal_path(p, rank), rows, kappa, rank)
        full = verify_dual(full_path(p), rows, None, kappa)
        strict = verify_dual(predecessor_path(p, rank), rows, rank - 1, predecessor)
        require(predecessor > kappa, f"p={p}: predecessor face is not strict")
        records.append({
            "p": p, "q": 2 * p + 1, "kappa": kappa, "minimum_rank": rank,
            "rank_excess": rank - (2 * p + 1), "predecessor_value": predecessor,
            "primal": primal, "unrestricted_dual": full, "predecessor_dual": strict,
        })
        print(f"PASS p={p} kappa={kappa} r*={rank} predecessor={predecessor}", flush=True)
    report = {
        "status": "PASS",
        "scope": "exact primal-dual and minimum-rank replay for 21<=p<=32, q=2p+1",
        "records": records,
        "conclusion": (
            "The rank excess equals 2 for 21<=p<=26, 3 at p=27, and 4 for 28<=p<=32."
        ),
    }
    destination = HERE / "exact_frontier_p21_p32_audit.json"
    destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {destination.resolve()}")


if __name__ == "__main__":
    main()

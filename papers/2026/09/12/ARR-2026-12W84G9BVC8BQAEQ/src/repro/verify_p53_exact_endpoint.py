#!/usr/bin/env python3
"""Standard-library exact replay of the completed p=53 endpoint theorem."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from verify_p28_exact_duals import HiveRows, add_scaled, require
PRIMAL = HERE / "p53_rank115_primal_certificate.json"
FULL_DUAL = HERE / "p53_unrestricted_dual_certificate.json"
RANK114_DUAL = HERE / "p53_rank114_dual_certificate.json"
REPORT = HERE / "p53_exact_endpoint_audit.json"


def q(value: object) -> Q:
    return Q(str(value))


def canonical_hash(payload: dict) -> str:
    body = dict(payload)
    expected = body.pop("certificate_sha256")
    stream = json.dumps(body, sort_keys=True, separators=(",", ":"))
    actual = hashlib.sha256(stream.encode()).hexdigest()
    require(actual == expected, "certificate canonical hash mismatch")
    return actual


def verify_primal(rows: HiveRows) -> dict:
    payload = json.loads(PRIMAL.read_text(encoding="utf-8"))
    require(payload.get("status") == "PASS", "primal status is not PASS")
    require((payload["p"], payload["q"], payload["dimension"]) == (53, 107, 160),
            "wrong primal parameters")
    certificate_hash = canonical_hash(payload)
    primal = [Q(0)] * rows.variable_count
    seen: set[int] = set()
    for raw_index, raw_value in payload["primal"]:
        index = int(raw_index)
        require(index not in seen, f"duplicate primal coordinate {index}")
        seen.add(index)
        primal[index] = q(raw_value)
    for name, (row, rhs) in rows.equalities.items():
        require(sum(Q(a) * primal[index] for index, a in row.items()) == rhs,
                f"primal equality failure {name}")
    tight = 0
    for name, row in rows.inequalities.items():
        value = sum(Q(a) * primal[index] for index, a in row.items())
        require(value <= 0, f"primal inequality failure {name}: {value}")
        tight += value == 0
    spectrum = [primal[rows.pv(j)] for j in range(1, rows.n)] + [Q(0)]
    stored = [q(value) for value in payload["positive_spectrum"]]
    require(spectrum == stored, "stored spectrum differs from primal boundary")
    require(spectrum == sorted(spectrum, reverse=True), "spectrum is not ordered")
    require(sum(spectrum) == 8847, "wrong primal trace")
    require(sum(value > 0 for value in spectrum) == 115, "wrong primal rank")
    require(max(value.denominator for value in primal) <= 2, "primal is not half-integral")
    return {
        "file": PRIMAL.name,
        "certificate_sha256": certificate_hash,
        "trace_upper": 8847,
        "attaining_rank": 115,
        "tight_inequalities": tight,
        "maximum_denominator": max(value.denominator for value in primal),
    }


def verify_dual(path: Path, rows: HiveRows, rank_cap: int | None,
                expected_kappa: int) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(payload.get("status") == "PASS", f"{path.name}: status is not PASS")
    require(payload["rank_cap"] == rank_cap, f"{path.name}: wrong rank cap")
    require(q(payload["paper_kappa_lower"]) == expected_kappa,
            f"{path.name}: wrong lower bound")
    certificate_hash = canonical_hash(payload)
    stationarity = [Q(0)] * rows.variable_count
    dual_value = Q(0)
    equality_seen: set[tuple] = set()
    for raw_name, raw_value in payload["equality_dual"]:
        name = tuple(raw_name)
        require(name in rows.equalities and name not in equality_seen,
                f"unknown or duplicate equality {name}")
        equality_seen.add(name)
        value = q(raw_value)
        row, rhs = rows.equalities[name]
        add_scaled(stationarity, row, value)
        dual_value += value * rhs
    inequality_seen: set[tuple] = set()
    for raw_name, raw_value in payload["inequality_dual"]:
        name = tuple(raw_name)
        require(name in rows.inequalities and name not in inequality_seen,
                f"unknown or duplicate inequality {name}")
        inequality_seen.add(name)
        value = q(raw_value)
        require(value < 0, f"nonnegative inequality multiplier {name}")
        add_scaled(stationarity, rows.inequalities[name], value)
    fixed_seen: set[int] = set()
    for raw_index, raw_value in payload["fixed_bound_dual"]:
        index = int(raw_index)
        require(rank_cap is not None, "unrestricted dual contains a fixed bound")
        require(index not in fixed_seen, f"duplicate fixed bound {index}")
        fixed_seen.add(index)
        require(rows.pv(rank_cap + 1) <= index < rows.variable_count,
                f"fixed-bound index outside rank face: {index}")
        stationarity[index] += q(raw_value)
    objective = [Q(0)] * rows.variable_count
    for j in range(1, rows.n):
        objective[rows.pv(j)] = Q(1, 2)
    require(stationarity == objective, f"{path.name}: stationarity failure")
    require(dual_value == Q(expected_kappa, 2), f"{path.name}: objective failure")
    multipliers = (
        [q(value) for _, value in payload["equality_dual"]]
        + [q(value) for _, value in payload["inequality_dual"]]
        + [q(value) for _, value in payload["fixed_bound_dual"]]
    )
    require(max(value.denominator for value in multipliers) <= 2,
            f"{path.name}: dual is not half-integral")
    return {
        "file": path.name,
        "certificate_sha256": certificate_hash,
        "rank_cap": rank_cap,
        "dual_lower_bound": expected_kappa,
        "support": len(equality_seen) + len(inequality_seen) + len(fixed_seen),
        "maximum_denominator": max(value.denominator for value in multipliers),
    }


def main() -> None:
    if not __debug__:
        raise SystemExit("refusing optimized Python: exact replay requires __debug__")
    rows = HiveRows(53, 107)
    primal = verify_primal(rows)
    full = verify_dual(FULL_DUAL, rows, None, 8847)
    predecessor = verify_dual(RANK114_DUAL, rows, 114, 8848)
    report = {
        "status": "PASS",
        "scope": "standard-library exact p=53 primal-dual and rank replay",
        "hive_variables": rows.variable_count,
        "equalities_available": len(rows.equalities),
        "inequalities_available": len(rows.inequalities),
        "primal": primal,
        "unrestricted_dual": full,
        "rank114_dual": predecessor,
        "theorem": "kappa(F_(53,107)) = 8847 and the minimum attaining rank is 115",
        "logic": (
            "The rational hive gives value <=8847 at rank 115; the unrestricted dual gives "
            "value >=8847; the rank<=114 dual gives value >=8848, and smaller rank faces are nested."
        ),
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("PASS kappa(F_(53,107))=8847 minimum_attaining_rank=115")
    print(f"WROTE {REPORT.resolve()}")


if __name__ == "__main__":
    main()

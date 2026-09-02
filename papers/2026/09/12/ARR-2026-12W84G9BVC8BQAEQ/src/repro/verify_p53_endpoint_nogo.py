#!/usr/bin/env python3
"""Standard-library replay of the exact p=53 endpoint-spectrum NO-GO."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from endpoint_horn_candidates import candidate
from verify_p28_exact_duals import HiveRows, require
CERTIFICATE = HERE / "endpoint_p53_farkas_nogo.json"
REPORT = HERE / "endpoint_p53_nogo_audit.json"


def q(value: object) -> Q:
    return Q(str(value))


def canonical_hash(payload: dict) -> str:
    body = dict(payload)
    expected = body.pop("certificate_sha256")
    stream = json.dumps(body, sort_keys=True, separators=(",", ":"))
    actual = hashlib.sha256(stream.encode()).hexdigest()
    require(actual == expected, "certificate canonical hash mismatch")
    return actual


def reduced_row(rows: HiveRows, spectrum: list[Q], kind: str, name: tuple):
    if kind == "equality":
        require(name in rows.equalities, f"unknown equality {name}")
        full, rhs = rows.equalities[name]
    else:
        require(kind == "upper", f"unknown row kind {kind}")
        require(name in rows.inequalities, f"unknown upper row {name}")
        full = rows.inequalities[name]
        rhs = 0
    hive = {index: coefficient for index, coefficient in full.items() if index < rows.p_offset}
    fixed = sum(
        Q(coefficient) * spectrum[index - rows.p_offset]
        for index, coefficient in full.items()
        if index >= rows.p_offset
    )
    return hive, Q(rhs) - fixed


def main() -> None:
    if not __debug__:
        raise SystemExit("refusing optimized Python: exact replay requires __debug__")
    payload = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    require(payload.get("status") == "PASS", "certificate status is not PASS")
    require(payload.get("claim") == "exact Farkas certificate: the fixed endpoint spectrum has no hive",
            "unexpected certificate claim")
    formula = candidate(4)
    require((payload["m"], payload["p"], payload["q"], payload["dimension"]) ==
            (4, 53, 107, 160), "wrong endpoint parameters")
    require(payload["candidate_kappa"] == formula["kappa"] == 8843, "wrong candidate cost")
    require(payload["candidate_rank"] == formula["attaining_rank_if_feasible"] == 115,
            "wrong candidate rank")
    spectrum = [q(value) for value in payload["positive_spectrum"]]
    require(spectrum == [Q(value) for value in formula["spectrum"]],
            "certificate spectrum differs from the explicit endpoint formula")
    certificate_hash = canonical_hash(payload)

    rows = HiveRows(53, 107)
    require(payload["free_hive_variables"] == rows.p_offset == 13041,
            "wrong number of hive variables")
    require(payload["rows_available"] == len(rows.equalities) + len(rows.inequalities) == 38800,
            "wrong row inventory")
    annihilator = [Q(0)] * rows.p_offset
    rhs_sum = Q(0)
    seen: set[tuple[str, tuple]] = set()
    for item in payload["ray_support"]:
        kind = item["kind"]
        name = tuple(item["name"])
        key = (kind, name)
        require(key not in seen, f"duplicate certificate row {key}")
        seen.add(key)
        multiplier = q(item["multiplier"])
        require(multiplier != 0, f"zero multiplier stored for {key}")
        if kind == "upper":
            require(multiplier < 0, f"upper multiplier is not negative for {name}")
        hive, rhs = reduced_row(rows, spectrum, kind, name)
        for index, coefficient in hive.items():
            annihilator[index] += multiplier * coefficient
        rhs_sum += multiplier * rhs
    require(all(value == 0 for value in annihilator), "Farkas hive coefficients do not cancel")
    require(rhs_sum == Q(1), f"expected contradiction 1, got {rhs_sum}")
    require(q(payload["farkas_contradiction"]) == rhs_sum, "stored contradiction mismatch")
    require(payload["max_denominator"] == 1, "certificate is not integral")
    require(len(seen) == 636, "unexpected certificate support")

    report = {
        "status": "PASS",
        "scope": "standard-library exact replay of the p=53 endpoint-spectrum Farkas certificate",
        "certificate_sha256": certificate_hash,
        "p": 53,
        "dimension": 160,
        "candidate_kappa": 8843,
        "candidate_rank_if_feasible": 115,
        "support": len(seen),
        "max_denominator": 1,
        "contradiction": "0 >= 1",
        "conclusion": (
            "The explicit A_m/B_m/C_m endpoint spectrum at m=4 has no hive and "
            "therefore cannot be an LR-feasible spectrum."
        ),
        "limitation": (
            "The certificate does not disprove the existence of a different p=53 "
            "optimum with cost 8843 or rank 115, nor any weaker cost/rank recurrence."
        ),
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("PASS p=53 endpoint spectrum infeasible: exact integral Farkas contradiction 0>=1")
    print(f"WROTE {REPORT.resolve()}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Run and cross-check the recursive and direct-LR Paper 30 replays."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRIMARY = HERE / "results" / "parametric_family_certificate.json"
LR = HERE / "results" / "parametric_family_lr_certificate.json"


def run(script: str) -> None:
    result = subprocess.run([sys.executable, script], cwd=HERE, text=True)
    if result.returncode:
        raise SystemExit(f"{script} failed with exit code {result.returncode}")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    run("verify_parametric_family.py")
    run("verify_parametric_family_lr.py")
    primary = json.loads(PRIMARY.read_text(encoding="utf-8"))
    lr = json.loads(LR.read_text(encoding="utf-8"))

    assert primary["status"] == lr["status"] == "PASS"
    assert primary["family"] == lr["family"]
    assert primary["horn_counts"] == [lr["horn_counts"][str(r)] for r in range(1, 8)]
    assert primary["constraint_count"] == lr["constraint_count"] == 8759
    for key in ("unrestricted_value", "rank4_value", "gap", "minimum_optimal_rank"):
        assert primary[key] == lr[key]

    primary_primals = primary["primal_chambers"]
    lr_primals = lr["primal_chambers"]
    assert len(primary_primals) == len(lr_primals) == 3
    primal_fields = (
        "label",
        "interval",
        "p_affine",
        "objective_affine",
        "minimum_endpoint_residual",
        "affine_residual_stream_sha256",
    )
    for left, right in zip(primary_primals, lr_primals):
        for field in primal_fields:
            assert left[field] == right[field], (left["label"], field)

    assert len(primary["duals"]) == len(lr["duals"]) == 3
    dual_fields = ("label", "weights", "combined_coefficients", "lower_bound_affine")
    for left, right in zip(primary["duals"], lr["duals"]):
        for field in dual_fields:
            assert left[field] == right[field], (left["label"], field)

    print("PASS: recursive-Horn and direct-LR routes agree on all frozen invariants")
    print(f"PRIMARY_JSON_SHA256: {digest(PRIMARY)}")
    print(f"LR_JSON_SHA256: {digest(LR)}")


if __name__ == "__main__":
    main()

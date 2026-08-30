#!/usr/bin/env python3
"""Fail-closed scientific replay for the standalone Paper 32 package."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MATH = ROOT / "math"
FROZEN_THRESHOLD = MATH / "results" / "d_le_7_epigraph_certificate.json"
EXPECTED_VERSIONS = {
    "numpy": "2.5.1",
    "pycddlib": "3.0.2",
    "scipy": "1.18.0",
    "sympy": "1.14.0",
}
EXPECTED_CORE_HASHES = {
    "math/verify_d_le_7_epigraph.py": "e5009d579933af66283de296ac8aa46b8f0b35bae1e43dd300768ef625129bd6",
    "math/results/d_le_7_epigraph_certificate.json": "0103a643644977400052a68738102a7633d6371db8717383ddefa687da8a18a0",
    "math/verify_d8_sharpness.py": "979605969b0c6df628d619b8255ba9f8ab2bef5f4f63d790d2ca4b48e1a2fa9c",
    "math/verify_rank_gap_frontier.py": "00bdbbfd8adbf3aff8f847ae3574241fc7bed887573c8fa6142bb242cf874be7",
    "math/verify_zero_padding_fixture.py": "6c8a804a3b7b8d77acac9d7e000dd48857858b7c616c11565b06efc38075fa2d",
    "math/audit_d_le_7_equalities.py": "0362a3dae16a027b87b3e39c360dfa657f42fd686401c2340d46013bd7bfb95e",
}
EXPECTED_PAPER32_HASHES = {
    "math/verify_hive_coarse_graining.py": "e3bfc7df692c021b600bd85fa1b8604b5f12b7bc4995e1dee4e0b1ea8c6fef89",
    "math/verify_block_inflation_endpoints.py": "f7c66a937e100e293ee68794606036afc09e6eb4e603e1a275bfb9f8d3978d80",
    "repro/exact_hive_duals.json": "c6b3588a2415db067f7ff34f7e23592ac9d85f3e10399dd0f8838fc244352b69",
    "repro/verify_exact_hive_duals.py": "e353f0f65d7edc2b3274ba2842263747fe5a5728f65c0e1ff4cf05407fde09e2",
    "repro/verify_coarse_graining_theorem.py": "b1ea0d5dad40b56d217cbbe32054110a63267ec7be0e862af964b17cf0cda91f",
}
EXPECTED_PAPER30_HASHES = {
    "verify_parametric_family.py": "c4c3aacfa58b60f592d065e760abbf92b44aa32e3f6a7503a06d2426cd43b2b1",
    "verify_parametric_family_lr.py": "5b473e819a0267d727bf227a1322e0c6afdef6733d322fb5426257d6f9534952",
    "run_parametric_family_replay.py": "e3bf6f629899b7e43b65f295dd914da81d466743fdc8ac075a80517b9a29faf8",
    "verify_rank_gap_frontier.py": "00bdbbfd8adbf3aff8f847ae3574241fc7bed887573c8fa6142bb242cf874be7",
    "results/parametric_family_certificate.json": "390fe0686df8939a6b64683acce1a977bfc21ab402054f039bbb4e3fc597c2ff",
    "results/parametric_family_lr_certificate.json": "4d85a3425be09d675aea57e2227f02a9cb2e24ff52d82499d25633fd08a447a4",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def absorbed_paper30() -> Path:
    packaged = ROOT / "repro" / "absorbed_paper30"
    development = ROOT.parent / "paper30-frontier"
    if packaged.is_dir():
        return packaged
    if development.is_dir():
        return development
    raise FileNotFoundError("Paper 30 replay sources are neither absorbed nor available as a sibling")


def run(script: Path, cwd: Path | None = None, *arguments: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(script), *arguments],
        cwd=cwd or ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    if completed.returncode:
        print(completed.stdout, end="")
        print(completed.stderr, file=sys.stderr, end="")
        raise SystemExit(f"FAIL: {script.name} exited {completed.returncode}")
    return completed.stdout


def check_versions() -> None:
    observed = {name: importlib.metadata.version(name) for name in EXPECTED_VERSIONS}
    if observed != EXPECTED_VERSIONS:
        raise SystemExit(f"dependency mismatch: expected {EXPECTED_VERSIONS}, got {observed}")
    if sys.version_info[:2] != (3, 12):
        raise SystemExit(f"Python 3.12 required, got {sys.version.split()[0]}")
    print("PASS: frozen Python/dependency versions")


def check_hashes(root: Path, expected: dict[str, str], label: str) -> None:
    for relative, wanted in expected.items():
        path = root / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        observed = digest(path)
        if observed != wanted:
            raise SystemExit(f"{label} hash mismatch: {relative}: {observed} != {wanted}")
    print(f"PASS: {label} frozen hashes ({len(expected)} files)")


def check_threshold() -> None:
    output = run(MATH / "verify_d_le_7_epigraph.py")
    observed = json.loads(output)
    frozen = json.loads(FROZEN_THRESHOLD.read_text(encoding="utf-8"))
    if observed != frozen or observed.get("status") != "PASS":
        raise SystemExit("canonical d<=7 replay differs from frozen certificate")
    print("PASS: canonical d<=7 replay matches frozen 33-stratum certificate")

    supplemental = run(MATH / "audit_d_le_7_equalities.py")
    marker = "PASS: preserved lin_set and verified both exact Farkas orientations for 46 projected equalities"
    if marker not in supplemental:
        raise SystemExit("supplemental equality-orientation audit marker missing")
    print("PASS: supplemental 46-equality two-orientation Farkas audit")


def check_sharpness() -> None:
    payload = json.loads(run(MATH / "verify_d8_sharpness.py"))
    if payload.get("status") != "PASS" or payload.get("conclusion") != "minimum optimal rank 5; rank-four penalty 1":
        raise SystemExit("dimension-eight sharpness replay mismatch")
    print("PASS: dependency-free dimension-eight integer witness")

    frontier = json.loads(run(MATH / "verify_rank_gap_frontier.py"))
    if frontier.get("status") != "PASS":
        raise SystemExit("canonical d8/d9 frontier replay did not pass")
    d8 = frontier["d8_parametric_family"]
    d9 = frontier["d9_two_valued_witness"]
    if d8["gap"] != "min(t,1-t)" or d9["full_value"] != 29 or d9["rank5_value"] != 30:
        raise SystemExit("canonical d8/d9 frontier invariants differ")
    print("PASS: canonical complete d8 phase and d9 two-valued witness")

    padding = run(MATH / "verify_zero_padding_fixture.py", MATH)
    if "PASS: exact zero-padding fixture (d7=74/7; d8=73/7; d8 rank<=4=74/7)" not in padding:
        raise SystemExit("zero-padding fixture marker missing")
    print("PASS: exact singular zero-padding warning fixture")


def check_absorbed_paper30(source: Path) -> None:
    check_hashes(source, EXPECTED_PAPER30_HASHES, "absorbed Paper 30")
    with tempfile.TemporaryDirectory(prefix="paper32-paper30-replay-") as directory:
        replay = Path(directory)
        (replay / "results").mkdir()
        for relative in EXPECTED_PAPER30_HASHES:
            origin = source / relative
            target = replay / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(origin, target)

        family_output = run(replay / "run_parametric_family_replay.py", replay)
        if "PASS: recursive-Horn and direct-LR routes agree on all frozen invariants" not in family_output:
            raise SystemExit("absorbed Paper 30 cross-route marker missing")
        for relative in (
            "results/parametric_family_certificate.json",
            "results/parametric_family_lr_certificate.json",
        ):
            if (replay / relative).read_bytes() != (source / relative).read_bytes():
                raise SystemExit(f"absorbed Paper 30 regenerated artifact differs: {relative}")
    print("PASS: Paper 30 full d8 phase and d9 witness absorbed without loss")


def check_wsl_route() -> None:
    output = run(MATH / "verify_low_dimension_minimality_exact.py")
    if '"status": "PASS"' not in output or '"summary_sha256": "4ccffca292a1f8d8774f50c656f723a299632d40362474ec9a83ffc0490fb9e3"' not in output:
        raise SystemExit("independent WSL/lcdd route marker missing")
    print("PASS: independent WSL/lcdd nonsingular route")


def check_unbounded_amplification() -> None:
    coarse = run(MATH / "verify_hive_coarse_graining.py")
    if "PASS: 6804 formal rhombus/boundary identities" not in coarse:
        raise SystemExit("symbolic hive coarse-graining marker missing")

    endpoints = run(MATH / "verify_block_inflation_endpoints.py")
    if "RESULT: unrestricted=29k; rank<=5k=30k" not in endpoints:
        raise SystemExit("all-k endpoint marker missing")

    finite = run(ROOT / "repro" / "verify_exact_hive_duals.py")
    if "PASS finite exact hive audit; no all-k claim" not in finite:
        raise SystemExit("finite exact hive-dual marker missing")

    theorem = run(ROOT / "repro" / "verify_coarse_graining_theorem.py")
    if "PASS theorem replay: kappa(F_(3t))=87t and 17t<r_*(F_(3t))<=18t" not in theorem:
        raise SystemExit("unbounded-rank theorem marker missing")
    print("PASS: exact seed, symbolic amplification, and unbounded rank excess")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--with-wsl-route", action="store_true")
    args = parser.parse_args()
    check_versions()
    check_hashes(ROOT, EXPECTED_CORE_HASHES, "absorbed Paper 31 core")
    check_hashes(ROOT, EXPECTED_PAPER32_HASHES, "Paper 32 amplification")
    check_threshold()
    check_sharpness()
    check_absorbed_paper30(absorbed_paper30())
    check_unbounded_amplification()
    if args.with_wsl_route:
        check_wsl_route()
    else:
        print("SKIP: optional Windows/WSL lcdd route (use --with-wsl-route)")
    print("PASS: complete standalone Paper 32 scientific replay")


if __name__ == "__main__":
    main()

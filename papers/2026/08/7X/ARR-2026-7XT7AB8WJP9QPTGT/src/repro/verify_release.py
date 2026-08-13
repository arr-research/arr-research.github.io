"""Fail-closed verification for the support-0.72 v3 release."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import numpy as np


AGGREGATE = "theta-schur-a072-d12-p47-tail8192-v3.npz"
BAND = "theta-near-band-a072-d12-to24-by-degree-p512-v3.npz"
RESULT = "theta-schur-a072-multiband-to24-by-degree-v3.json"
SOURCE = "paper17-v3-source.zip"
PREDECESSOR = "provenance-input/theta-schur-a072-d12-p47-tail8192-v1.npz"
FRESH_REPLAY = "provenance-input/theta-schur-a072-d12-p47-tail8192-v3-overconservative-replay.npz"
PROVENANCE = "AGGREGATE_PROVENANCE_AUDIT.json"
UPGRADER = "upgrade_float_export_v3.py"
SHADOW_AUDITOR = "independent_reference_audit.py"
SHADOW_RECORD = "independent-reference-audit.json"

# Filled only after the terminal corrected-source replays.
EXPECTED_SHA256 = {
    AGGREGATE: "fab69bc8fa1d21ac0d3faca85d317ec5655fd991e7af29329329be4e5f8c1ebb",
    BAND: "9119dbd4bad1a3c0de406445bbcb537e7c6d10fc6010f7a9d90ea79ae561751c",
    RESULT: "63b0dd91dab9fe7a00b734644c7a0400c2240a51cc25e6dde42751208dfc4f08",
    SOURCE: "6f744332b9b068ec050c9e36b502b3b4241687acb87c7b35c99a5dee926721fb",
    PREDECESSOR: "c5cff9fba1684a5822e1544a2a96f91aa843d9b0074e239df6e81a51875ecad4",
    FRESH_REPLAY: "63ce54787c994bcd524ec3c323d3738c9a082b0e41d8274dcce9ddc92bd820f7",
    PROVENANCE: "3a948203846797b54bc27bd1f8d4003dca6d2eeccb8db0906e4de5d60f5b5d94",
    UPGRADER: "be886107fe934b63804857c4c1f4566aa8100656c7ad2c74284b6b6ea35b1af4",
    SHADOW_AUDITOR: "a0bee89423b8415c7ae5ae0746c97225196be71dabc6e40fc01ec923357c8276",
    SHADOW_RECORD: "42ad78222edc6b27dfd39bde6b7f511c22cce5362c3a3b3cff51adffb5efab2b",
}

PUBLIC_EVEN_FLOOR = 5.890e-17
PUBLIC_ODD_FLOOR = 1.652e-13

AGGREGATE_METADATA = {
    "format": 3,
    "accumulator_version": 2,
    "float_export_version": 2,
    "architecture": "third-window-thirteen-block",
    "half_width": "0.72",
    "low_degree_count": 12,
    "tail_start": 176,
    "explicit_end": 8192,
    "maximum_smooth_power": 47,
    "retain_self_tail": True,
    "self_remainder_end": 32768,
    "precision": 512,
    "pointwise_subdivisions": 1024,
    "smooth_target_rule": "maximum_power+source_degree_count+2",
    "singular_moment_order": 8,
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def numeric_array(payload, key: str, radius: bool) -> np.ndarray:
    require(key in payload.files, f"missing array {key}")
    array = np.asarray(payload[key])
    require(array.shape == (78, 78), f"{key} has wrong shape {array.shape}")
    require(np.issubdtype(array.dtype, np.number), f"{key} is not numeric")
    require(np.all(np.isfinite(array)), f"{key} contains a nonfinite entry")
    if radius:
        require(np.all(array >= 0), f"{key} contains a negative radius")
    return array


def verify_aggregate(path: Path) -> None:
    expected_keys = {"metadata", "smooth_remainder", "other_tail_norm", "complement_floor"}
    for prefix in ("source", "band", "flux", "singular", "self"):
        for parity in ("even", "odd"):
            expected_keys |= {f"{prefix}_{parity}_midpoint", f"{prefix}_{parity}_radius"}
    with np.load(path, allow_pickle=False) as payload:
        require(set(payload.files) == expected_keys, "aggregate key set mismatch")
        metadata = json.loads(str(payload["metadata"].item()))
        require(metadata == AGGREGATE_METADATA, "aggregate metadata mismatch")
        for prefix in ("source", "band", "flux", "singular", "self"):
            for parity in ("even", "odd"):
                midpoint = numeric_array(payload, f"{prefix}_{parity}_midpoint", False)
                radius = numeric_array(payload, f"{prefix}_{parity}_radius", True)
                if prefix == "band":
                    trace_lower = float(np.sum(np.diag(midpoint) - np.diag(radius)))
                    require(trace_lower > 0, f"aggregate {parity} band is semantically zero")
        smooth = float(payload["smooth_remainder"])
        other = float(payload["other_tail_norm"])
        floor = float(payload["complement_floor"])
        require(math.isfinite(smooth) and smooth >= 0, "invalid smooth remainder")
        require(math.isfinite(other) and other >= 0, "invalid other-tail norm")
        require(math.isfinite(floor) and floor > 0, "invalid complement floor")


def verify_band(path: Path) -> None:
    expected_keys = {"metadata"}
    for index in range(12):
        for parity in ("even", "odd"):
            expected_keys |= {f"band_{index}_{parity}_midpoint", f"band_{index}_{parity}_radius"}
    with np.load(path, allow_pickle=False) as payload:
        require(set(payload.files) == expected_keys, "band key set mismatch")
        metadata = json.loads(str(payload["metadata"].item()))
        required = {
            "format": 3,
            "accumulator_version": 2,
            "float_export_version": 2,
            "architecture": "third-window-near-tail-bands",
            "half_width": "0.72",
            "degree": 12,
            "precision": 512,
            "maximum_smooth_power": 47,
            "boundaries": list(range(12, 25)),
        }
        require(all(metadata.get(k) == v for k, v in required.items()), "band metadata mismatch")
        for index in range(12):
            for parity in ("even", "odd"):
                midpoint = numeric_array(payload, f"band_{index}_{parity}_midpoint", False)
                radius = numeric_array(payload, f"band_{index}_{parity}_radius", True)
                trace_lower = float(np.sum(np.diag(midpoint) - np.diag(radius)))
                require(trace_lower > 0, f"band {index}/{parity} has nonpositive trace")


def verify_record(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    require(data.get("half_width") == 0.72, "result support mismatch")
    require(data.get("band_boundaries") == list(range(12, 25)) + [176], "result split mismatch")
    for name, floor in (("even", PUBLIC_EVEN_FLOOR), ("odd", PUBLIC_ODD_FLOOR)):
        sector = data.get(name, {})
        require(sector.get("negative_count") == 0, f"{name} negative count")
        require(sector.get("positive_count") == 78, f"{name} positive count")
        require(sector.get("unresolved_count") == 0, f"{name} unresolved count")
        require(sector.get("inertia_method") == "congruence-gershgorin", f"{name} method")
        require(float(sector.get("coercive_lower", 0)) >= floor, f"{name} coercive floor")
    return data


def verify_provenance(root: Path) -> None:
    audit = json.loads((root / PROVENANCE).read_text(encoding="utf-8"))
    require(audit.get("legacy_sha256") == EXPECTED_SHA256[PREDECESSOR], "legacy provenance hash")
    require(audit.get("final_upgraded_sha256") == EXPECTED_SHA256[AGGREGATE], "final provenance hash")
    require(audit.get("fresh_overconservative_replay_sha256") == EXPECTED_SHA256[FRESH_REPLAY], "fresh replay provenance hash")
    with tempfile.TemporaryDirectory(prefix="paper17-provenance-") as temporary:
        rebuilt = Path(temporary) / AGGREGATE
        subprocess.run(
            [sys.executable, str(root / UPGRADER), str(root / PREDECESSOR), str(rebuilt)],
            check=True,
            capture_output=True,
            text=True,
        )
        require(sha256(rebuilt) == EXPECTED_SHA256[AGGREGATE], "allowlisted upgrade is not byte-exact")
    with np.load(root / AGGREGATE, allow_pickle=False) as final, np.load(
        root / FRESH_REPLAY, allow_pickle=False
    ) as fresh:
        for prefix in ("source", "band", "flux", "singular", "self"):
            for parity in ("even", "odd"):
                key = f"{prefix}_{parity}_midpoint"
                require(np.array_equal(final[key], fresh[key]), f"fresh replay midpoint mismatch: {key}")
        for parity in ("even", "odd"):
            midpoint = fresh[f"band_{parity}_midpoint"]
            require(float(np.trace(midpoint)) > 0, f"fresh replay {parity} aggregate is zero")


def replay_adjudicator(root: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="paper17-v3-") as temporary:
        source_root = Path(temporary)
        with zipfile.ZipFile(root / SOURCE) as archive:
            archive.extractall(source_root)
        sys.path.insert(0, str(source_root))
        try:
            from experiments.theta_pencil.third_window_multiband_schur_certificate import (
                certify_third_window_multiband_schur,
            )
            certificate = certify_third_window_multiband_schur(
                root / AGGREGATE, root / BAND
            )
        finally:
            sys.path.pop(0)
        require(certificate.even.negative_count == 0, "replay even negative count")
        require(certificate.even.positive_count == 78, "replay even positive count")
        require(certificate.even.unresolved_count == 0, "replay even unresolved count")
        require(certificate.even.coercive_lower >= PUBLIC_EVEN_FLOOR, "replay even floor")
        require(certificate.odd.negative_count == 0, "replay odd negative count")
        require(certificate.odd.positive_count == 78, "replay odd positive count")
        require(certificate.odd.unresolved_count == 0, "replay odd unresolved count")
        require(certificate.odd.coercive_lower >= PUBLIC_ODD_FLOOR, "replay odd floor")


def replay_shadow_audit(root: Path) -> None:
    completed = subprocess.run(
        [sys.executable, str(root / SHADOW_AUDITOR), str(root)],
        check=True,
        capture_output=True,
        text=True,
    )
    replay = json.loads(completed.stdout)
    frozen = json.loads((root / SHADOW_RECORD).read_text(encoding="utf-8"))
    require(replay == frozen, "independent shadow audit record mismatch")
    require(replay.get("graph_and_parity") == "PASS", "independent graph/parity audit")
    for parity in ("even", "odd"):
        require(float(replay[parity]["weyl_lower"]) > 0, f"independent {parity} Weyl margin")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", nargs="?", type=Path, default=Path("."))
    args = parser.parse_args()
    root = args.directory.resolve()
    for filename, expected in EXPECTED_SHA256.items():
        path = root / filename
        require(path.is_file(), f"missing {filename}")
        require("__" not in expected, "release hashes have not been frozen")
        require(sha256(path) == expected, f"SHA-256 mismatch for {filename}")
    verify_aggregate(root / AGGREGATE)
    verify_band(root / BAND)
    verify_record(root / RESULT)
    verify_provenance(root)
    replay_adjudicator(root)
    replay_shadow_audit(root)
    print("PASS: hashes, provenance, schemas, interval objects, Arb readjudication, and independent shadow audit")


if __name__ == "__main__":
    main()

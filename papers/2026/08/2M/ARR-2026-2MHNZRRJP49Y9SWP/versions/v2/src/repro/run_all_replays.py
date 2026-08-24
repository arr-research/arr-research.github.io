#!/usr/bin/env python3
"""Run every exact replay and verify the committed JSON byte for byte."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CASES = (
    ("verify_exact_projection_floor.py", "last_exact_projection_floor_v0.7.json"),
    ("verify_common_tangent_extremizer.py", "last_common_tangent_extremizer_v0.7.json"),
    ("verify_perfect_field_fattening.py", "last_perfect_field_fattening_v0.7.json"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="arr-fattening-replay-") as temp:
        temp_root = Path(temp)
        for script_name, expected_name in CASES:
            actual = temp_root / expected_name
            completed = subprocess.run(
                [sys.executable, str(ROOT / script_name), "--output", str(actual)],
                check=True,
                capture_output=True,
                text=True,
            )
            expected = ROOT / expected_name
            if actual.read_bytes() != expected.read_bytes():
                raise AssertionError(f"fresh output differs from {expected_name}")
            print(completed.stdout, end="")
            print(f"MATCH {expected_name} sha256={sha256(expected)}")
    print("ALL REPLAYS AND COMMITTED RESULTS MATCH")


if __name__ == "__main__":
    main()

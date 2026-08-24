#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Regenerate the exact evidence and compare it byte for byte."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    expected = ROOT / "results.json"
    with tempfile.TemporaryDirectory(prefix="dual-multiplicity-") as temp:
        actual = Path(temp) / "results.json"
        subprocess.run(
            [
                sys.executable,
                str(ROOT / "verify_dual_multiplicity.py"),
                "--output",
                str(actual),
            ],
            check=True,
        )
        if actual.read_bytes() != expected.read_bytes():
            raise AssertionError("fresh output differs from results.json")
    print(f"MATCH results.json sha256={sha256(expected)}")
    print("ALL REPLAYS AND COMMITTED RESULTS MATCH")


if __name__ == "__main__":
    main()

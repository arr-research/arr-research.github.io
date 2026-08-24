#!/usr/bin/env python3
"""Run the exact replay in isolation and compare with committed results."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def main() -> None:
    root = Path(__file__).resolve().parent
    expected_path = root / "results.json"
    expected = expected_path.read_bytes()
    expected_json = json.loads(expected)
    if expected_json.get("overall_status") != "PASS":
        raise SystemExit("Committed results do not have overall_status=PASS")

    with tempfile.TemporaryDirectory(prefix="gauss-tjurina-replay-") as temp:
        actual_path = Path(temp) / "results.json"
        subprocess.run(
            [sys.executable, str(root / "verify_tjurina_fibres.py"), "--output", str(actual_path)],
            check=True,
        )
        actual = actual_path.read_bytes()

    digest = hashlib.sha256(actual).hexdigest()
    if actual != expected:
        raise SystemExit(
            "MISMATCH generated results differ from committed results "
            f"(generated sha256={digest})"
        )
    print(f"MATCH results.json sha256={digest}")
    print("ALL REPLAYS AND COMMITTED RESULTS MATCH")


if __name__ == "__main__":
    main()

"""One-command exact replay wrapper for Paper 16.

Run from this directory with:

    python run_all_replays.py

The wrapper executes the five theorem-bearing checks sequentially, captures
their complete output, and writes replay_results.json.  A nonzero child exit
terminates the wrapper with failure.  No network access or parallel worker is
used.
"""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


CHECKS = [
    "verify_low_degree_order.py",
    "verify_finite_tail_cutoffs.py",
    "verify_gr36_two_block_laplace.py",
    "verify_d5r2_canonical_crossing.py",
    "verify_r4_all_degree.py",
]


def main() -> None:
    here = Path(__file__).resolve().parent
    records: list[dict[str, object]] = []
    for script in CHECKS:
        completed = subprocess.run(
            [sys.executable, script],
            cwd=here,
            check=False,
            capture_output=True,
            text=True,
        )
        record = {
            "script": script,
            "returncode": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }
        records.append(record)
        print(f"{script}: {'PASS' if completed.returncode == 0 else 'FAIL'}")
        if completed.returncode != 0:
            break

    result = {
        "status": "PASS" if len(records) == len(CHECKS) and all(r["returncode"] == 0 for r in records) else "FAIL",
        "command": "python run_all_replays.py",
        "network": "not used",
        "parallel_workers": 0,
        "checks": records,
    }
    output = here / "replay_results.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"overall: {result['status']}")
    print(f"result: {output.name}")
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()

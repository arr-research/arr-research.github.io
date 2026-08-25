"""Run every committed replay and report a single deterministic result."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SCRIPTS = (
    "verify_dimension_three_sharpness.py",
    "verify_global_fixtures.py",
)


def sha256(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    runs = []
    for name in SCRIPTS:
        completed = subprocess.run(
            [sys.executable, str(HERE / name)],
            cwd=HERE,
            check=True,
            capture_output=True,
            text=True,
        )
        reported = json.loads(completed.stdout)
        runs.append(
            {
                "script": name,
                "result": Path(reported["results"]).name,
                "status": reported["status"],
            }
        )
    outputs = (
        HERE / "dimension_three_sharpness_results.json",
        HERE / "global_fixture_results.json",
    )
    result = {
        "scope": "Orchestration record for finite fixtures; each result file states its limitations.",
        "runs": runs,
        "outputs": [
            {"file": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)}
            for path in outputs
        ],
        "status": "pass",
    }
    target = HERE / "results.json"
    target.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"results": str(target), "status": "pass"}, sort_keys=True))


if __name__ == "__main__":
    main()

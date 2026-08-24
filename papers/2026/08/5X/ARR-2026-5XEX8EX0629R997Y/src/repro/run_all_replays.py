"""Run every replay and write one deterministic JSON report."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from pathlib import Path

from verify_plane_sharpness_exact import build_report as plane_report
from verify_truncated_tjurina_floor import build_report as floor_report


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=str(Path(__file__).with_name("results.json")),
        help="combined UTF-8 JSON result path",
    )
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    scripts = [
        base / "explore_monomial_defects.py",
        base / "verify_truncated_tjurina_floor.py",
        base / "verify_plane_sharpness_exact.py",
        base / "run_all_replays.py",
    ]
    report = {
        "status": "pass",
        "scope": (
            "Finite exact integer, exact QQ Groebner, and two-prime modular "
            "checks only; the manuscript proofs carry the universal claims."
        ),
        "runtime": {
            "python": sys.version.split()[0],
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "script_sha256": {path.name: sha256(path) for path in scripts},
        "truncated_floor": floor_report(),
        "plane_sharpness_exact": plane_report(),
    }
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(payload, encoding="utf-8", newline="\n")
    print(payload, end="")


if __name__ == "__main__":
    main()

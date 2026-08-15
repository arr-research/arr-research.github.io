# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import argparse
import json
import re
import shutil
import uuid
from datetime import date
from pathlib import Path

from arrlib import PAPERS_DIR, ROOT, discover_papers, select_paper


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create the next immutable-version candidate for an ARR record.")
    parser.add_argument("paper_id", help="Existing ARR public identifier")
    parser.add_argument("--date", default=date.today().isoformat(), help="Version date in YYYY-MM-DD form")
    parser.add_argument("--change-size", choices=("minor", "major"), required=True)
    parser.add_argument("--summary", required=True, help="Meaningful summary of the revision")
    return parser.parse_args()


def update_citation(path: Path, version: str, release_date: str) -> None:
    if not path.is_file():
        return
    value = path.read_text(encoding="utf-8")
    value = re.sub(r"(?m)^version:\s*.*$", f'version: "{version}"', value)
    value = re.sub(r"(?m)^date-released:\s*.*$", f'date-released: "{release_date}"', value)
    path.write_text(value, encoding="utf-8", newline="\n")


def main() -> int:
    args = parse_args()
    revision_date = date.fromisoformat(args.date).isoformat()
    summary = args.summary.strip()
    if len(summary) < 20:
        raise ValueError("--summary must contain at least 20 characters")

    latest = select_paper(discover_papers(), args.paper_id)
    record_root = latest.record_root
    if record_root is None or not record_root.is_relative_to(PAPERS_DIR):
        raise ValueError(f"Cannot resolve the storage root for {args.paper_id}")

    next_version = f"v{latest.version_number + 1}"
    destination = record_root / "versions" / next_version
    if destination.exists():
        raise FileExistsError(destination)

    ignore = shutil.ignore_patterns("versions") if latest.path == record_root else None
    shutil.copytree(latest.path, destination, ignore=ignore)

    metadata_path = destination / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    previous_version_id = metadata["version_id"]
    metadata.update(
        {
            "schema_version": "1.2",
            "version_id": f"arr:version:{uuid.uuid4()}",
            "supersedes_version_id": previous_version_id,
            "version": next_version,
            "date": revision_date,
            "status": "corrected",
            "revision": {"change_size": args.change_size, "summary": summary},
        }
    )
    metadata.pop("release_url", None)
    metadata["screening"] = {
        "protocol": metadata.get("screening", {}).get("protocol", "ARR-SCREEN-1.0"),
        "status": "not_assessed",
        "critical_objections_unresolved": 0,
        "human_signoff": True,
        "evaluators": [],
    }
    verification = metadata.setdefault("verification", {})
    verification["bibliography"] = "not_assessed"
    verification["reproducibility"] = "not_assessed"
    verification["lean4"] = "not_assessed" if any(destination.glob("**/*.lean")) else "not_applicable"
    verification.pop("report", None)
    editorial = metadata.setdefault("editorial", {})
    editorial["decision"] = "correction"
    editorial["statement"] = (
        f"Version {next_version} supersedes {latest.version}. Declared {args.change_size} revision: {summary} "
        "All assessments apply only when explicitly rerun and recorded for this exact version."
    )
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    provenance_path = destination / "PROVENANCE.json"
    if provenance_path.is_file():
        provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
        provenance.update(
            {
                "version_id": metadata["version_id"],
                "supersedes_version_id": previous_version_id,
                "revision": metadata["revision"],
            }
        )
        provenance_path.write_text(
            json.dumps(provenance, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    update_citation(destination / "CITATION.cff", next_version, revision_date)
    try:
        print(destination.relative_to(ROOT))
    except ValueError:
        print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# SPDX-License-Identifier: AGPL-3.0-or-later
"""Create an accepted metadata version from an unchanged, reviewed working paper."""
from __future__ import annotations

import argparse
import json
import shutil
import uuid
from datetime import date

from arrlib import PAPERS_DIR, discover_papers, select_paper
from new_version import update_citation


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Promote a reviewed AIRR working paper without altering its canonical manuscript bytes."
    )
    parser.add_argument("paper_id")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--signed-by", required=True)
    parser.add_argument("--decision", choices=("founder_pilot", "standard_acceptance"), required=True)
    parser.add_argument("--statement", required=True)
    parser.add_argument("--conflict", action="append", default=[])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    admission_date = date.fromisoformat(args.date).isoformat()
    statement = args.statement.strip()
    if len(statement) < 20:
        raise ValueError("--statement must contain at least 20 characters")

    versions = [paper for paper in discover_papers() if paper.id == args.paper_id]
    latest = select_paper(versions, args.paper_id)
    if latest.metadata.get("status") != "working_paper":
        raise ValueError("Only the latest working_paper version can be admitted")
    screening = latest.metadata.get("screening", {})
    if screening.get("status") != "pass" or screening.get("critical_objections_unresolved") != 0 or not screening.get("evaluators"):
        raise ValueError("The exact working-paper version must pass its recorded audit with zero unresolved objections")

    record_root = latest.record_root
    if record_root is None or not record_root.is_relative_to(PAPERS_DIR):
        raise ValueError(f"Cannot resolve the storage root for {args.paper_id}")
    next_version = f"v{latest.version_number + 1}"
    destination = record_root / "versions" / next_version
    if destination.exists():
        raise FileExistsError(destination)
    shutil.copytree(latest.path, destination, ignore=shutil.ignore_patterns("versions"))

    metadata_path = destination / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    previous_version_id = metadata["version_id"]
    had_accepted_version = any(p.metadata.get("status") in {"accepted", "corrected"} for p in versions)
    metadata.update(
        {
            "schema_version": "1.4",
            "version_id": f"arr:version:{uuid.uuid4()}",
            "supersedes_version_id": previous_version_id,
            "version": next_version,
            "date": admission_date,
            "status": "corrected" if had_accepted_version else "accepted",
            "revision": {
                "change_size": "minor",
                "summary": (
                    f"Admission record for the unchanged canonical manuscript from {latest.version}; "
                    "the PDF SHA-256 remains identical and the completed exact-version assessment is preserved."
                ),
            },
            "editorial": {
                "decision": "correction" if had_accepted_version else args.decision,
                "signed_by": args.signed_by.strip(),
                "conflicts": sorted(set(args.conflict)),
                "statement": statement,
            },
        }
    )
    metadata["screening"]["human_signoff"] = True
    metadata.pop("release_url", None)
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    provenance_path = destination / "PROVENANCE.json"
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    provenance.update(
        {
            "version_id": metadata["version_id"],
            "supersedes_version_id": previous_version_id,
            "revision": metadata["revision"],
            "admission_from_working_version": latest.version,
            "canonical_manuscript_unchanged": True,
        }
    )
    provenance_path.write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    update_citation(destination / "CITATION.cff", next_version, admission_date)
    print(destination.relative_to(PAPERS_DIR.parent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

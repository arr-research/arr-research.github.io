# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import sys

from arrlib import discover_papers, validate_collection, validate_record_timestamps
from assessmentlib import load_assessment_registry, validate_public_assessments


def main() -> int:
    papers = discover_papers()
    failures = validate_collection(papers)
    timestamp_errors = validate_record_timestamps(papers)
    assessment_errors = []
    if not failures:
        try:
            assessment_errors = validate_public_assessments(load_assessment_registry(), papers)
        except (OSError, ValueError) as error:
            assessment_errors = [str(error)]
    if failures or timestamp_errors or assessment_errors:
        print("AIRR validation failed:")
        for path, errors in failures.items():
            print(f"\n{path}")
            for error in errors:
                print(f"  - {error}")
        if timestamp_errors:
            print("\nregistry/record-timestamps.json")
            for error in timestamp_errors:
                print(f"  - {error}")
        if assessment_errors:
            print("\nregistry/model-assessments.json")
            for error in assessment_errors:
                print(f"  - {error}")
        return 1
    paper_count = sum(paper.record_type == "research_paper" for paper in papers)
    note_count = sum(paper.record_type == "technical_note" for paper in papers)
    print(f"AIRR validation passed ({paper_count} paper(s), {note_count} technical note(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

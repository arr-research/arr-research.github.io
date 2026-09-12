# SPDX-License-Identifier: AGPL-3.0-or-later
"""Project an already-public exact-PDF intake report without rewriting its protocol."""
from __future__ import annotations

import argparse
import hashlib
import json
import uuid
from pathlib import Path

from arrlib import ROOT, discover_papers, select_paper
from assessmentlib import (
    ASSESSMENTS_PATH, INTAKE_PROMPT_VERSION, assessment_artifact_sha256,
    load_assessment_registry, source_hash, validate_assessment, validate_registry,
)


def project_report(paper, source: Path) -> dict:
    source = source.resolve()
    if not source.is_relative_to((paper.path / "screening").resolve()):
        raise ValueError("Only this version's already-public screening reports can be imported")
    raw = source.read_bytes()
    native = json.loads(raw)
    if native.get("prompt_version") != INTAKE_PROMPT_VERSION:
        raise ValueError("Unsupported native intake protocol")
    if native.get("manuscript_sha256") != assessment_artifact_sha256(paper):
        raise ValueError("Native report concerns a different PDF")
    result = {k: v for k, v in native.items() if k not in {"submission_id", "manuscript_sha256"}}
    result.update(
        paper_id=paper.id, version=paper.version, version_id=paper.metadata["version_id"],
        canonical_sha256=native["manuscript_sha256"], assessment_id=f"arr:assessment:{uuid.uuid4()}",
        source_response_sha256=source_hash(native),
        intake_source={"path":source.relative_to(ROOT).as_posix(),
                       "file_sha256":hashlib.sha256(raw).hexdigest(),
                       "submission_id":native["submission_id"]},
    )
    errors = validate_assessment(result, [paper])
    if errors:
        raise ValueError("; ".join(errors))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper_id")
    parser.add_argument("source", type=Path)
    parser.add_argument("--version")
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    papers = discover_papers()
    report = project_report(select_paper(papers,args.paper_id,args.version),args.source)
    registry = load_assessment_registry()
    registry["assessments"].append(report)
    errors = validate_registry(registry,papers)
    if errors:
        raise ValueError("; ".join(errors))
    if args.publish:
        ASSESSMENTS_PATH.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({"assessment_id":report["assessment_id"],"source":report["intake_source"],"registry_updated":args.publish},indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# SPDX-License-Identifier: AGPL-3.0-or-later
"""Materialize author-authorized ai.vixra history as visibly unassessed ARR archive records."""
from __future__ import annotations

import argparse
import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader

from arrlib import CROCKFORD, ROOT, crockford_prefix


INVENTORY = ROOT / "registry" / "ai-vixra-import.json"
PDF_DIR = ROOT / "tmp" / "pdfs" / "ai-vixra"
TIMESTAMPS = ROOT / "registry" / "record-timestamps.json"


def args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=INVENTORY)
    parser.add_argument("--pdf-dir", type=Path, default=PDF_DIR)
    parser.add_argument("--deposit-commit", help="Full Git SHA of the first commit containing the imported record files.")
    return parser.parse_args()


def new_identity(year: int) -> dict[str, str]:
    record_uuid = uuid.uuid4()
    version_uuid = uuid.uuid4()
    return {
        "record_id": f"arr:record:{record_uuid}",
        "version_id": f"arr:version:{version_uuid}",
        "id": f"ARR-{year}-{crockford_prefix(record_uuid)}",
        "version": "v1",
    }


def dump_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def extract_text(pdf: Path) -> str:
    reader = PdfReader(pdf)
    pages = []
    for index, page in enumerate(reader.pages, start=1):
        pages.append(f"\n\n--- Page {index} ---\n\n{page.extract_text() or ''}")
    return "".join(pages).strip() + "\n"


def cff_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def materialize(record: dict) -> Path:
    first = datetime.fromisoformat(record["first_submitted_at"])
    identity = record.get("arr_record") or new_identity(first.year)
    record["arr_record"] = identity
    shard = identity["id"].split("-")[-1][:2]
    target = ROOT / "papers" / f"{first.year:04d}" / f"{first.month:02d}" / shard / identity["id"]
    target.mkdir(parents=True, exist_ok=True)
    (target / "LICENSES").mkdir(exist_ok=True)

    asset = record["latest_asset"]
    source_pdf = PDF_DIR / asset["name"]
    versions = [
        {"version": item["version"], "submitted_at": item["submitted_at"], "pdf_url": item["pdf_url"]}
        for item in record["versions"]
    ]
    metadata = {
        "schema_version": "1.3",
        **identity,
        "record_type": "research_paper",
        "title": record["title"],
        "abstract": record["abstract"],
        "authors": [{"name": name, "affiliation": "Independent researcher"} for name in record["authors"]],
        "date": first.date().isoformat(),
        "status": "archived",
        "archival_source": {
            "archive": "ai.vixra",
            "identifier": record["identifier"],
            "abstract_url": record["abstract_url"],
            "first_submitted_at": record["first_submitted_at"],
            "latest_declared_version": record["latest_version"],
            "latest_submitted_at": record["latest_submitted_at"],
            "mirrored_version": asset["source_version"],
            "mirror_pdf_url": asset["mirror_pdf_url"],
            "mirror_release_url": asset["mirror_release_url"],
            "versions": versions,
        },
        "licenses": {
            "manuscript": "LicenseRef-Author-Retained",
            "metadata": "CC0-1.0",
            "code": [],
            "data": [],
        },
        "source_of_truth": "external_pdf",
        "keywords": [record["category"]],
        "subjects": [record["category"]],
        "deposit": {
            "depositor_name": "Lluis Eriksson",
            "relationship": "author",
            "deposit_authorized": True,
            "third_party_material_disclosed": False,
            "terms_version": "ARR-HISTORICAL-IMPORT-1.0",
        },
        "integrity": {
            "algorithm": "sha256",
            "manifest": "MANIFEST.sha256",
            "canonical_sha256": asset["sha256"],
            "canonical_bytes": asset["bytes"],
        },
        "ai_assistance": {
            "used": True,
            "statement": "Historical import from ai.vixra, an AI-assisted e-print archive. ARR has not normalized or independently verified the original manuscript's model-use disclosure; the author remains responsible for its contents.",
        },
        "screening": {
            "protocol": "ARR-SCREEN-1.0",
            "status": "not_assessed",
            "critical_objections_unresolved": 0,
            "human_signoff": True,
            "evaluators": [],
        },
        "verification": {
            "protocol": "ARR-HISTORICAL-IMPORT-1.0",
            "bibliography": "not_assessed",
            "source_integrity": "pass",
            "reproducibility": "not_assessed",
            "lean4": "not_assessed",
            "report": "VERIFICATION.md",
        },
        "editorial": {
            "decision": "historical_import",
            "signed_by": "Lluis Eriksson",
            "conflicts": ["author_is_founder_editor"],
            "statement": "Author-authorized historical import. ARR verified file retrieval and integrity only; it did not perform the current hostile frontier-model admission audit, peer review, novelty review, or correctness certification.",
        },
    }
    dump_json(target / "metadata.json", metadata)

    history = "\n".join(
        f"- [{item['version']}]({item['pdf_url']}) — {item['submitted_at']}" for item in versions
    )
    paper_md = f"""# {record['title']}

**Author:** {', '.join(record['authors'])}  
**Original archive:** [ai.vixra:{record['identifier']}]({record['abstract_url']})  
**First submitted:** {record['first_submitted_at']} (source displays no timezone)  
**Latest declared source version:** {record['latest_version']}  
**ARR mirror:** [{asset['source_version']} PDF]({asset['mirror_pdf_url']})

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

{record['abstract']}

## Source version history

{history}
"""
    (target / "paper.md").write_text(paper_md, encoding="utf-8")
    (target / "paper.txt").write_text(extract_text(source_pdf), encoding="utf-8")

    provenance = {
        "schema_version": "1.0",
        "record_id": identity["record_id"],
        "version_id": identity["version_id"],
        "created_by": ["Lluis Eriksson"],
        "source_of_truth": "external_pdf",
        "canonical_source": {
            "url": asset["mirror_pdf_url"],
            "source_archive_url": next(item["pdf_url"] for item in versions if item["version"] == asset["source_version"]),
            "source_version": asset["source_version"],
            "media_type": "application/pdf",
            "bytes": asset["bytes"],
            "pages": asset["pages"],
            "sha256": asset["sha256"],
        },
        "version_history": versions,
        "tools": ["ARR ai.vixra archival importer", "pypdf structural and text extraction", "SHA-256"],
        "verification_notes": "Author-authorized historical import. File readability and SHA-256 integrity verified; scientific claims were not assessed.",
    }
    dump_json(target / "PROVENANCE.json", provenance)

    licenses = {
        "manuscript": {"spdx": "LicenseRef-Author-Retained", "notice": "Author-retained rights; ARR mirror authorized by the author."},
        "metadata": {"spdx": "CC0-1.0", "url": "https://creativecommons.org/publicdomain/zero/1.0/"},
        "code": [],
        "data": [],
    }
    dump_json(target / "LICENSES.json", licenses)
    (target / "LICENSES" / "MANUSCRIPT.md").write_text(
        "# Manuscript rights\n\nCopyright retained by Lluis Eriksson. The author authorized ARR to preserve and serve this historical mirror. No additional public reuse license is inferred.\n",
        encoding="utf-8",
    )
    (target / "VERIFICATION.md").write_text(
        f"# Historical import verification\n\n- Mirrored source version: {asset['source_version']}\n- PDF pages: {asset['pages']}\n- Bytes: {asset['bytes']}\n- SHA-256: `{asset['sha256']}`\n- Scientific assessment: not performed\n",
        encoding="utf-8",
    )
    cff = f"""cff-version: 1.2.0
message: {cff_quote('If you use this work, cite the original author and record.')}
title: {cff_quote(record['title'])}
type: article
authors:
  - family-names: Eriksson
    given-names: Lluis
version: {cff_quote(asset['source_version'])}
date-released: {first.date().isoformat()}
url: {cff_quote(record['abstract_url'])}
"""
    (target / "CITATION.cff").write_text(cff, encoding="utf-8")
    (target / "README.md").write_text(
        f"# {identity['id']}\n\nHistorical mirror of ai.vixra:{record['identifier']}. See `metadata.json` for exact provenance and source-version history. This import is not an ARR assessment.\n",
        encoding="utf-8",
    )
    manifest_files = [
        "CITATION.cff", "LICENSES.json", "LICENSES/MANUSCRIPT.md", "PROVENANCE.json",
        "README.md", "VERIFICATION.md", "metadata.json", "paper.md", "paper.txt",
    ]
    manifest = "".join(
        f"{hashlib.sha256((target / name).read_bytes()).hexdigest()}  {name}\n" for name in manifest_files
    )
    manifest += f"{asset['sha256']}  REMOTE:{asset['mirror_pdf_url']}\n"
    (target / "MANIFEST.sha256").write_text(manifest, encoding="utf-8")
    return target


def update_timestamps(records: list[dict], commit: str) -> None:
    if len(commit) != 40 or any(character not in "0123456789abcdef" for character in commit):
        raise ValueError("--deposit-commit must be a full lowercase Git SHA")
    registry = json.loads(TIMESTAMPS.read_text(encoding="utf-8"))
    existing = {(item["id"], item["version"]) for item in registry["records"]}
    recorded_at = datetime.now(timezone.utc).isoformat()
    for record in records:
        identity = record["arr_record"]
        key = (identity["id"], identity["version"])
        if key not in existing:
            registry["records"].append(
                {
                    "id": identity["id"],
                    "version": identity["version"],
                    "deposit_recorded_at": recorded_at,
                    "deposit_timestamp_basis": "first_repository_commit",
                    "deposit_commit": commit,
                    "publication_state": "pending",
                }
            )
    dump_json(TIMESTAMPS, registry)


def main() -> int:
    options = args()
    inventory = json.loads(options.inventory.read_text(encoding="utf-8"))
    records = inventory["records"]
    paths = [materialize(record) for record in records]
    inventory["arr_materialized_at"] = datetime.now(timezone.utc).isoformat()
    dump_json(options.inventory, inventory)
    if options.deposit_commit:
        update_timestamps(records, options.deposit_commit)
    print(f"Materialized {len(paths)} historical records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

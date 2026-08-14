# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import argparse
import json
import shutil
import uuid
from datetime import date
from pathlib import Path

from arrlib import PAPERS_DIR, ROOT, crockford_prefix


TEMPLATE_DIR = ROOT / "templates" / "paper"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a sharded ARR research-record candidate from the canonical template.")
    parser.add_argument("--date", default=date.today().isoformat(), help="Deposit date in YYYY-MM-DD form")
    parser.add_argument("--author", default="Author Name", help="Initial depositor/author name")
    parser.add_argument(
        "--type",
        choices=("research-paper", "technical-note"),
        default="research-paper",
        help="Public record type (default: research-paper)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    publication_date = date.fromisoformat(args.date)
    record_uuid = uuid.uuid4()
    version_uuid = uuid.uuid4()
    suffix = crockford_prefix(record_uuid)
    public_id = f"ARR-{publication_date.year}-{suffix}"
    destination = PAPERS_DIR / str(publication_date.year) / f"{publication_date.month:02d}" / suffix[:2] / public_id
    if destination.exists():
        raise FileExistsError(destination)

    shutil.copytree(TEMPLATE_DIR, destination)
    metadata_path = destination / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata.update(
        {
            "schema_version": "1.1",
            "record_id": f"arr:record:{record_uuid}",
            "version_id": f"arr:version:{version_uuid}",
            "id": public_id,
            "date": publication_date.isoformat(),
            "record_type": args.type.replace("-", "_"),
        }
    )
    if metadata["record_type"] == "technical_note":
        metadata["title"] = "Replace with the complete technical-note title"
        metadata["abstract"] = (
            "Replace this text with a concise summary of the technical contribution, "
            "method or evidence, result, limitations, and exact intended scope."
        )
        metadata["technical_note"] = {
            "kind": "result",
            "maturity": "complete_in_scope",
            "scope_statement": "Replace with the precise contribution and boundary of this technical note.",
            "limitations": "Replace with the known limitations, exclusions, and unresolved questions.",
        }
    metadata["authors"][0]["name"] = args.author
    metadata["deposit"]["depositor_name"] = args.author
    metadata["editorial"]["signed_by"] = args.author
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    provenance_path = destination / "PROVENANCE.json"
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    provenance.update(
        {
            "record_id": metadata["record_id"],
            "version_id": metadata["version_id"],
            "created_by": [args.author],
        }
    )
    provenance_path.write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(destination.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

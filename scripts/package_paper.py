# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import argparse
import json
import shutil
import sys
import zipfile
from pathlib import Path

from arrlib import ROOT, discover_papers, iter_package_files, sha256, validate_paper


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build immutable release assets for one ARR paper.")
    parser.add_argument("paper_id", help="ARR public identifier, for example ARR-2026-01K2M3N4P5Q6R7S8")
    parser.add_argument("--output", default="dist/release", help="Output directory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    matches = [paper for paper in discover_papers() if paper.id == args.paper_id]
    if len(matches) != 1:
        print(f"Expected exactly one paper named {args.paper_id}; found {len(matches)}.", file=sys.stderr)
        return 1

    paper = matches[0]
    errors = validate_paper(paper)
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    output = ROOT / args.output / paper.id / paper.version
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    bundle = output / f"{paper.id}-{paper.version}-sources.zip"
    with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source in iter_package_files(paper.path):
            archive.write(source, source.relative_to(paper.path))

    manifest_lines: list[str] = []
    for source in iter_package_files(paper.path):
        manifest_lines.append(f"{sha256(source)}  {source.relative_to(paper.path).as_posix()}")
    manifest_lines.append(f"{sha256(bundle)}  {bundle.name}")
    manifest = output / "MANIFEST.sha256"
    manifest.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8", newline="\n")

    metadata_copy = output / "RECORD.json"
    metadata_copy.write_text(json.dumps(paper.metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    paper_pdf = paper.path / "paper.pdf"
    if paper_pdf.is_file():
        shutil.copy2(paper_pdf, output / f"{paper.id}-{paper.version}.pdf")

    notes = output / "RELEASE_NOTES.md"
    notes.write_text(
        f"# {paper.metadata['title']}\n\n"
        f"ARR record: `{paper.id}`  \n"
        f"Version: `{paper.version}`  \n"
        f"Protocol: `{paper.metadata['verification']['protocol']}`\n\n"
        "The attached manifest records SHA-256 hashes for every published source file and the complete source bundle.\n",
        encoding="utf-8",
        newline="\n",
    )
    print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())

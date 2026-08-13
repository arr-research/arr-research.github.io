# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import argparse
import subprocess
import tempfile
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create machine-readable ARR renditions from a canonical PDF.")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output", type=Path, help="ARR paper directory")
    parser.add_argument("--title", required=True)
    parser.add_argument("--pdftotext", default="pdftotext", help="pdftotext executable")
    return parser.parse_args()


def normalize_pages(raw: str) -> list[str]:
    pages = []
    for page in raw.replace("\r\n", "\n").replace("\r", "\n").split("\f"):
        lines = [line.rstrip() for line in page.splitlines()]
        text = "\n".join(lines).strip()
        if text:
            pages.append(text)
    return pages


def main() -> int:
    args = parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary:
        extracted = Path(temporary) / "paper.txt"
        subprocess.run(
            [args.pdftotext, "-layout", "-enc", "UTF-8", str(args.pdf), str(extracted)],
            check=True,
        )
        pages = normalize_pages(extracted.read_text(encoding="utf-8", errors="replace"))

    plain = "\n\n\f\n\n".join(pages) + "\n"
    (args.output / "paper.txt").write_text(plain, encoding="utf-8", newline="\n")

    sections = []
    for index, page in enumerate(pages, 1):
        sections.append(f"## Page {index}\n\n```text\n{page}\n```")
    markdown = (
        f"# {args.title}\n\n"
        "> Machine-readable rendition extracted from the hash-identified canonical PDF. "
        "Mathematical typography may be degraded; cite and verify against `paper.pdf`.\n\n"
        + "\n\n---\n\n".join(sections)
        + "\n"
    )
    (args.output / "paper.md").write_text(markdown, encoding="utf-8", newline="\n")
    print(f"Wrote {len(pages)} pages to {args.output / 'paper.md'} and {args.output / 'paper.txt'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

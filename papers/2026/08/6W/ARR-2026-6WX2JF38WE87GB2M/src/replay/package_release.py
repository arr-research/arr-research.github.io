"""Build or verify the deterministic Paper 19 release archive."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
SOURCE_PDF = ROOT / "paper" / "oracle_varieties_query_support.pdf"
OUTPUT_PDF = ROOT / "output" / "pdf" / "Algebraic_Query_Support_for_Unitary_Oracles.pdf"
PAPER_TEXT = ROOT / "output" / "pdf" / "paper.txt"
MANIFEST = ROOT / "output" / "release" / "manifest.json"
ARCHIVE = ROOT / "output" / "release" / "Algebraic_Query_Support_Reproducibility.zip"

FILES = [
    "README.md",
    "CLAIM_LEDGER.md",
    "SUBMISSION_SHEET.md",
    "requirements.txt",
    "package_release.py",
    "paper/oracle_varieties_query_support.tex",
    "paper/oracle_varieties_query_support.pdf",
    "paper/references.bib",
    "paper/oracle_variety_spectrum.pdf",
    "paper/oracle_variety_spectrum.png",
    "verification/verify_oracle_varieties.py",
    "verification/make_figure.py",
    "output/pdf/Algebraic_Query_Support_for_Unitary_Oracles.pdf",
    "output/pdf/paper.txt",
]


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def current_manifest() -> dict:
    records = []
    for relative in FILES:
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        records.append({"path": relative.replace("\\", "/"), "bytes": path.stat().st_size, "sha256": digest(path)})
    return {"schema": 1, "files": records}


def build() -> None:
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE_PDF, OUTPUT_PDF)
    reader = PdfReader(OUTPUT_PDF)
    extracted = "\n\f\n".join(page.extract_text() or "" for page in reader.pages)
    PAPER_TEXT.write_text(extracted.rstrip() + "\n", encoding="utf-8", newline="\n")
    data = current_manifest()
    MANIFEST.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for relative in FILES + ["output/release/manifest.json"]:
            path = ROOT / relative
            info = zipfile.ZipInfo(relative.replace("\\", "/"), (2026, 8, 14, 12, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def check() -> None:
    recorded = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if recorded != current_manifest():
        raise AssertionError("manifest differs from current files")
    if digest(SOURCE_PDF) != digest(OUTPUT_PDF):
        raise AssertionError("canonical PDF differs from compiled PDF")
    expected = [item.replace("\\", "/") for item in FILES + ["output/release/manifest.json"]]
    archive_status = "extracted tree"
    if ARCHIVE.is_file():
        with zipfile.ZipFile(ARCHIVE, "r") as zf:
            if zf.namelist() != expected:
                raise AssertionError("archive member list differs")
            for relative in expected:
                if zf.read(relative) != (ROOT / relative).read_bytes():
                    raise AssertionError(f"archive member differs: {relative}")
        archive_status = f"ZIP {digest(ARCHIVE)}"
    print(f"PASS release: {len(FILES)} manifested files; PDF {digest(OUTPUT_PDF)}; {archive_status}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        check()
    else:
        build()
        check()


if __name__ == "__main__":
    main()

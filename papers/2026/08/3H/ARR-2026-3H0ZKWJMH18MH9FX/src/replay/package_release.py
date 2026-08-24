"""Build or verify the deterministic exterior-list-decoder release."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import zipfile
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
SOURCE_PDF = ROOT / "output" / "build" / "exterior_list_decoders.pdf"
OUTPUT_PDF = ROOT / "output" / "pdf" / "Exterior_Power_Decoders_for_Quantum_Lists.pdf"
PAPER_TEXT = ROOT / "output" / "pdf" / "paper.txt"
MANIFEST = ROOT / "output" / "release" / "manifest.json"
ARCHIVE = ROOT / "output" / "release" / "Exterior_Power_Decoders_Reproducibility.zip"
SUBMISSION_SHEET = ROOT / "SUBMISSION_SHEET.md"

FILES = [
    "README.md",
    "README_REPRODUCIBILITY.md",
    "RESEARCH_MEMO.md",
    "CLAIM_LEDGER.md",
    "PRIORITY_AUDIT.md",
    "EXTERNAL_ASSESSMENT.md",
    "EXTERNAL_REVIEW_PROMPT.es.txt",
    "SUBMISSION_SHEET.md",
    "requirements.txt",
    "build_final_local.ps1",
    "package_release.py",
    "paper/exterior_list_decoders.tex",
    "paper/references.bib",
    "verify_full_spark_list_threshold.py",
    "results/full_spark_list_threshold_certificate.json",
    "output/pdf/Exterior_Power_Decoders_for_Quantum_Lists.pdf",
    "output/pdf/paper.txt",
]

def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def current_manifest() -> dict:
    records = []
    for relative in FILES:
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        records.append({
            "path": relative.replace("\\", "/"),
            "bytes": path.stat().st_size,
            "sha256": digest(path),
        })
    return {"schema": 1, "files": records}


def validate_pdf(path: Path) -> None:
    reader = PdfReader(path)
    if not 11 <= len(reader.pages) <= 16:
        raise AssertionError(f"unexpected PDF page count: {len(reader.pages)}")
    metadata = reader.metadata or {}
    if metadata.get("/Title") != (
        "Strictly Scalable Exterior Decoders for Quantum Lists: Exact "
        "Full-Spark Widths and Fixed-Probe Weyl Bayes Curves"
    ):
        raise AssertionError("unexpected PDF metadata title")
    if metadata.get("/Author") != "Lluis Eriksson":
        raise AssertionError("unexpected PDF metadata author")
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    for marker in (
        "Strictly Scalable Exterior Decoders for Quantum Lists",
        "The exact scalable full-spark threshold",
        "Constructive",
        "Spectral list-error bound",
        "Exact rank-two Weyl list curve",
        "The support pattern matters",
    ):
        if marker not in text:
            raise AssertionError(f"expected PDF text missing: {marker}")


def refresh_submission_sheet(path: Path) -> None:
    reader = PdfReader(path)
    content = SUBMISSION_SHEET.read_text(encoding="utf-8")
    content = re.sub(
        r"^- \*\*PDF:\*\* .*?$",
        f"- **PDF:** {len(reader.pages)} A4 pages, 2 tables, 0 figures, {path.stat().st_size} bytes",
        content,
        flags=re.MULTILINE,
    )
    content = re.sub(
        r"^- \*\*PDF SHA-256:\*\* `[^`]+`$",
        f"- **PDF SHA-256:** `{digest(path)}`",
        content,
        flags=re.MULTILINE,
    )
    SUBMISSION_SHEET.write_text(content, encoding="utf-8", newline="\n")


def build() -> None:
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    if not SOURCE_PDF.is_file():
        raise FileNotFoundError("compile output/build/exterior_list_decoders.pdf first")
    latest_source = max(
        (ROOT / "paper" / "exterior_list_decoders.tex").stat().st_mtime_ns,
        (ROOT / "paper" / "references.bib").stat().st_mtime_ns,
    )
    if SOURCE_PDF.stat().st_mtime_ns < latest_source:
        raise AssertionError("compiled PDF is older than TeX or bibliography")
    validate_pdf(SOURCE_PDF)
    shutil.copyfile(SOURCE_PDF, OUTPUT_PDF)
    refresh_submission_sheet(OUTPUT_PDF)
    reader = PdfReader(OUTPUT_PDF)
    extracted = "\n\f\n".join(page.extract_text() or "" for page in reader.pages)
    PAPER_TEXT.write_text(extracted.rstrip() + "\n", encoding="utf-8", newline="\n")
    MANIFEST.write_text(
        json.dumps(current_manifest(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in FILES + ["output/release/manifest.json"]:
            path = ROOT / relative
            info = zipfile.ZipInfo(relative.replace("\\", "/"), (2026, 8, 15, 12, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def check() -> None:
    recorded = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if recorded != current_manifest():
        raise AssertionError("manifest differs from current files")
    validate_pdf(OUTPUT_PDF)
    if SOURCE_PDF.is_file() and digest(SOURCE_PDF) != digest(OUTPUT_PDF):
        raise AssertionError("canonical PDF differs from compiled PDF")
    expected = [item.replace("\\", "/") for item in FILES + ["output/release/manifest.json"]]
    archive_status = "extracted tree"
    if ARCHIVE.is_file():
        with zipfile.ZipFile(ARCHIVE, "r") as archive:
            if archive.namelist() != expected:
                raise AssertionError("archive member list differs")
            for relative in expected:
                if archive.read(relative) != (ROOT / relative).read_bytes():
                    raise AssertionError(f"archive member differs: {relative}")
        archive_status = f"ZIP {digest(ARCHIVE)}"
    print(
        f"PASS release: {len(FILES)} manifested files; "
        f"PDF {digest(OUTPUT_PDF)}; {archive_status}"
    )


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

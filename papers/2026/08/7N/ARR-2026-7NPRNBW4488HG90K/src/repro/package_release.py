"""Build and verify the deterministic local Paper 28 release archive."""

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
SOURCE_PDF = ROOT / "build" / "paper.pdf"
OUTPUT_PDF = ROOT / "output" / "pdf" / "One_Spike_Inverse_Selfcommutators_and_Exact_Switching.pdf"
PAPER_TEXT = ROOT / "output" / "pdf" / "paper.txt"
MANIFEST = ROOT / "output" / "release" / "manifest.json"
ARCHIVE = ROOT / "output" / "release" / "One_Spike_Inverse_Selfcommutators_and_Exact_Switching_Reproducibility.zip"

FILES = [
    "README.md",
    "CLAIM_LEDGER.md",
    "SUBMISSION_SHEET.md",
    "QA_REPORT.md",
    "MATH_AUDIT_INDEPENDENT.md",
    "FINAL_REAUDIT.md",
    "PRIORITY_AUDIT_INDEPENDENT.md",
    "FINAL_PRIORITY_REAUDIT.md",
    "REPRO_AUDIT.md",
    "paper.tex",
    "references.bib",
    "build_local.ps1",
    "run_scientific_replay.ps1",
    "package_release.py",
    "repro/README.md",
    "repro/requirements.txt",
    "repro/run_replay.py",
    "repro/verify_four_kick_gram.py",
    "repro/verify_symbolic_constructors.py",
    "repro/results/four_kick_gram.json",
    "repro/results/symbolic_constructors.json",
    "build/paper.pdf",
    "build/paper.log",
    "build/paper.blg",
    "build/scientific_replay.log",
    "output/pdf/One_Spike_Inverse_Selfcommutators_and_Exact_Switching.pdf",
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
        records.append(
            {
                "path": relative.replace("\\", "/"),
                "bytes": path.stat().st_size,
                "sha256": digest(path),
            }
        )
    return {"schema": 1, "files": records}


def validate_logs() -> None:
    checks = {
        ROOT / "build" / "paper.log": (
            r"(?:LaTeX|Package|Class) .*Warning",
            r"(?:Overfull|Underfull) \\[hv]box",
            r"Missing character:",
            r"undefined references",
            r"multiply defined",
        ),
        ROOT / "build" / "paper.blg": (r"Warning--", r"error message"),
    }
    for path, patterns in checks.items():
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in patterns:
            if re.search(pattern, text, re.I):
                raise AssertionError(f"disallowed build-log pattern {pattern!r} in {path.name}")
    replay = (ROOT / "build" / "scientific_replay.log").read_text(encoding="utf-8")
    if "PASS: both independent exact replay routes completed." not in replay:
        raise AssertionError("scientific replay completion marker missing")
    if replay.count("frozen SHA-256") != 2:
        raise AssertionError("expected two frozen replay hashes")


def validate_audits() -> None:
    required = {
        "FINAL_REAUDIT.md": "PASS",
        "FINAL_PRIORITY_REAUDIT.md": "PASS",
        "QA_REPORT.md": "PASS for local release packaging",
    }
    for relative, marker in required.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        if marker not in text:
            raise AssertionError(f"missing audit marker {marker!r} in {relative}")


def validate_pdf(path: Path) -> PdfReader:
    reader = PdfReader(path)
    if len(reader.pages) < 9:
        raise AssertionError(f"unexpectedly short PDF: {len(reader.pages)} pages")
    metadata = reader.metadata or {}
    if metadata.get("/Author") != "Lluis Eriksson":
        raise AssertionError("unexpected PDF author")
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    markers = (
        "One-Spike Inverse Self-Commutators",
        "exact cost and optimizer rigidity",
        "Gini identity and sharp trace-distance stability",
        "exact triangular action",
        "exact quadrilateral action",
        "why the determinant is necessary",
        "Relation to earlier records and development provenance",
        "Reproducibility, limitations, and conclusion",
        "Author and AI disclosure",
    )
    for marker in markers:
        if marker not in text:
            raise AssertionError(f"missing PDF marker: {marker}")
    lower = text.lower()
    forbidden = (
        "first exact",
        "novelty is established",
        "unprecedented",
        "machine-certified proof",
        "all optimizing matrices are weighted shifts",
        "every optimal square uses",
    )
    for stale in forbidden:
        if stale in lower:
            raise AssertionError(f"stale or excessive claim in PDF: {stale}")
    return reader


def build() -> None:
    if not SOURCE_PDF.is_file():
        raise FileNotFoundError("compile build/paper.pdf first")
    latest = max((ROOT / "paper.tex").stat().st_mtime_ns, (ROOT / "references.bib").stat().st_mtime_ns)
    if SOURCE_PDF.stat().st_mtime_ns < latest:
        raise AssertionError("PDF is older than source")
    validate_logs()
    validate_audits()
    reader = validate_pdf(SOURCE_PDF)
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE_PDF, OUTPUT_PDF)
    PAPER_TEXT.write_text(
        "\n\f\n".join(page.extract_text() or "" for page in reader.pages).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    MANIFEST.write_text(
        json.dumps(current_manifest(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    members = FILES + ["output/release/manifest.json"]
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in members:
            info = zipfile.ZipInfo(relative.replace("\\", "/"), (2026, 8, 24, 12, 30, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(
                info,
                (ROOT / relative).read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )


def check() -> None:
    if json.loads(MANIFEST.read_text(encoding="utf-8")) != current_manifest():
        raise AssertionError("manifest differs from current files")
    validate_logs()
    validate_audits()
    validate_pdf(OUTPUT_PDF)
    if digest(SOURCE_PDF) != digest(OUTPUT_PDF):
        raise AssertionError("canonical PDF differs from build")
    expected = [item.replace("\\", "/") for item in FILES + ["output/release/manifest.json"]]
    if ARCHIVE.is_file():
        with zipfile.ZipFile(ARCHIVE) as archive:
            if archive.namelist() != expected:
                raise AssertionError("archive member list differs")
            for relative in expected:
                if archive.read(relative) != (ROOT / relative).read_bytes():
                    raise AssertionError(f"archive member differs: {relative}")
        container = f"; ZIP {digest(ARCHIVE)}"
    else:
        container = "; extracted tree (container not nested)"
    print(
        f"PASS release: {len(FILES)} files; "
        f"PDF {digest(OUTPUT_PDF)}{container}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    check() if args.check else build()


if __name__ == "__main__":
    main()

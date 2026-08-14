from __future__ import annotations

import argparse
import hashlib
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PAPER_PDF = ROOT / "paper" / "two_query_tetrahedral_echo.pdf"
PDF_NAME = "Two_Query_Chirality_in_Tetrahedral_Quantum_Echoes.pdf"
OUT_PDF = ROOT / "output" / "pdf" / PDF_NAME
CANONICAL_PDF = ROOT.parents[1] / "outputs" / PDF_NAME
OUT_ZIP = ROOT / "output" / "release" / "Two_Query_Chirality_Reproducibility.zip"
MANIFEST = ROOT / "MANIFEST.sha256"

FILES = {
    PDF_NAME: OUT_PDF,
    "README.md": ROOT / "README.md",
    "CLAIM_LEDGER.md": ROOT / "CLAIM_LEDGER.md",
    "SUBMISSION_SHEET.md": ROOT / "SUBMISSION_SHEET.md",
    "requirements.txt": ROOT / "requirements.txt",
    "package_release.py": ROOT / "package_release.py",
    "paper/two_query_tetrahedral_echo.tex": ROOT / "paper" / "two_query_tetrahedral_echo.tex",
    "paper/references.bib": ROOT / "paper" / "references.bib",
    "verification/verify_coherent_order_echo.py": ROOT / "verification" / "verify_coherent_order_echo.py",
    "verification/verify_two_use_a4.py": ROOT / "verification" / "verify_two_use_a4.py",
    "verification/verify_two_use_causal_qhalf.py": ROOT / "verification" / "verify_two_use_causal_qhalf.py",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build() -> None:
    if not PAPER_PDF.is_file():
        raise SystemExit(f"missing compiled PDF: {PAPER_PDF}")
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    OUT_ZIP.parent.mkdir(parents=True, exist_ok=True)
    CANONICAL_PDF.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PAPER_PDF, OUT_PDF)
    shutil.copy2(PAPER_PDF, CANONICAL_PDF)

    for archive_name, source in FILES.items():
        if not source.is_file():
            raise SystemExit(f"missing release input {archive_name}: {source}")

    lines = [f"{sha256(source)}  {name}" for name, source in sorted(FILES.items())]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    members = dict(FILES)
    members["MANIFEST.sha256"] = MANIFEST
    with zipfile.ZipFile(OUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for archive_name, source in sorted(members.items()):
            info = zipfile.ZipInfo(archive_name, date_time=(2026, 8, 14, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, source.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def check() -> None:
    if not OUT_PDF.is_file() or not CANONICAL_PDF.is_file() or not OUT_ZIP.is_file() or not MANIFEST.is_file():
        raise SystemExit("release outputs are incomplete; run without --check first")
    if sha256(PAPER_PDF) != sha256(OUT_PDF) or sha256(PAPER_PDF) != sha256(CANONICAL_PDF):
        raise SystemExit("PDF copies differ")

    expected = {name: sha256(source) for name, source in FILES.items()}
    parsed: dict[str, str] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        parsed[name] = digest
    if parsed != expected:
        raise SystemExit("manifest differs from current release inputs")

    with zipfile.ZipFile(OUT_ZIP) as bundle:
        names = set(bundle.namelist())
        if names != set(FILES) | {"MANIFEST.sha256"}:
            raise SystemExit("ZIP member set differs")
        for name, digest in expected.items():
            if hashlib.sha256(bundle.read(name)).hexdigest() != digest:
                raise SystemExit(f"ZIP hash mismatch: {name}")
        if bundle.read("MANIFEST.sha256") != MANIFEST.read_bytes():
            raise SystemExit("ZIP manifest mismatch")
    print("PASS release package")
    print(f"PDF sha256 {sha256(OUT_PDF)}")
    print(f"ZIP sha256 {sha256(OUT_ZIP)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        check()
    else:
        build()
        check()

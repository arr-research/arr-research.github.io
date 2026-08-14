"""Build and verify the deterministic Paper 20 release bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import zipfile
from io import BytesIO
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PDF_NAME = "Matroidal_Bayes_Bounds_for_General_Quantum_Process_Discrimination.pdf"
ZIP_NAME = "Matroidal_Bayes_Bounds_Paper20_Reproducibility.zip"
CANONICAL_PDF = ROOT / "output" / "pdf" / PDF_NAME
ZIP_PATH = ROOT / "output" / "release" / ZIP_NAME
MANIFEST_PATH = ROOT / "release_manifest.json"
SOURCE_PDF = ROOT / "paper" / "rado_matroid_testers.pdf"
ZIP_TIME = (2026, 8, 14, 0, 0, 0)

PAYLOAD = [
    "CLAIM_LEDGER.md",
    "README.md",
    "SUBMISSION_SHEET.md",
    "requirements.txt",
    "verify_canonical_tester_compression.py",
    "package_release.py",
    "paper/rado_matroid_testers.tex",
    "paper/references.bib",
    "paper/rado_matroid_testers.pdf",
    "figure/make_matroid_figure.py",
    "figure/paper20_matroidal_bayes_figure.pdf",
    "figure/paper20_matroidal_bayes_figure.png",
    "figure/README.md",
    "figure/SHA256SUMS.txt",
    f"output/pdf/{PDF_NAME}",
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def manifest() -> dict[str, object]:
    files: list[dict[str, object]] = []
    for relative in PAYLOAD:
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        data = path.read_bytes()
        files.append({"path": relative, "bytes": len(data), "sha256": sha256(data)})
    return {
        "schema": 1,
        "title": "Matroidal Bayes Bounds for General Quantum Process Discrimination",
        "author": "Lluis Eriksson",
        "files": files,
    }


def manifest_bytes(value: dict[str, object]) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def zip_bytes(value: dict[str, object]) -> bytes:
    output = BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in PAYLOAD:
            info = zipfile.ZipInfo(relative, ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 0
            info.external_attr = 0
            archive.writestr(info, (ROOT / relative).read_bytes())
        info = zipfile.ZipInfo("release_manifest.json", ZIP_TIME)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.create_system = 0
        info.external_attr = 0
        archive.writestr(info, manifest_bytes(value))
    return output.getvalue()


def build() -> None:
    CANONICAL_PDF.parent.mkdir(parents=True, exist_ok=True)
    ZIP_PATH.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE_PDF, CANONICAL_PDF)
    value = manifest()
    MANIFEST_PATH.write_bytes(manifest_bytes(value))
    ZIP_PATH.write_bytes(zip_bytes(value))
    print(f"PDF {CANONICAL_PDF} {sha256(CANONICAL_PDF.read_bytes())}")
    print(f"ZIP {ZIP_PATH} {sha256(ZIP_PATH.read_bytes())}")


def check() -> None:
    if SOURCE_PDF.read_bytes() != CANONICAL_PDF.read_bytes():
        raise AssertionError("canonical PDF differs from the audited source PDF")
    expected = manifest()
    actual = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if actual != expected:
        raise AssertionError("release manifest is stale")
    if ZIP_PATH.is_file():
        expected_zip = zip_bytes(expected)
        actual_zip = ZIP_PATH.read_bytes()
        if actual_zip != expected_zip:
            raise AssertionError("release ZIP is not the deterministic current build")
        with zipfile.ZipFile(ZIP_PATH) as archive:
            expected_names = set(PAYLOAD) | {"release_manifest.json"}
            if set(archive.namelist()) != expected_names:
                raise AssertionError("ZIP entry set mismatch")
            for entry in expected["files"]:  # type: ignore[index]
                data = archive.read(entry["path"])  # type: ignore[index]
                if len(data) != entry["bytes"] or sha256(data) != entry["sha256"]:  # type: ignore[index]
                    raise AssertionError(f"ZIP payload mismatch: {entry['path']}")
        print(f"PASS: {len(PAYLOAD)} payload files, deterministic ZIP, canonical PDF exact")
        print(f"ZIP_SHA256={sha256(actual_zip)}")
    else:
        print(f"PASS: {len(PAYLOAD)} extracted payload files, manifest and canonical PDF exact")
        print("ARCHIVE_CHECK=skipped (outer ZIP not present in extracted payload)")
    print(f"PDF_SHA256={sha256(CANONICAL_PDF.read_bytes())}")


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--build", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.build:
        build()
    else:
        check()


if __name__ == "__main__":
    main()

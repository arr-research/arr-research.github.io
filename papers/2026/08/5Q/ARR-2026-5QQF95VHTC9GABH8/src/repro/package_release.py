#!/usr/bin/env python3
"""Build or verify the deterministic standalone Paper 32 release archive."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output" / "release"
ARCHIVE = OUTPUT / "Sharp_Onset_Unbounded_Selfcommutator_Rank_Reproducibility.zip"
MANIFEST_COPY = OUTPUT / "manifest.json"
PDF = ROOT / "output" / "pdf" / "Sharp_Onset_Unbounded_Norm_Optimal_Selfcommutator_Rank.pdf"
EXPECTED_PDF_SHA256 = "17b2361721027649b8ef5b98440032b91b5b04e89e2a9535fcbe7a27954ac1c5"
ZIP_TIME = (2026, 8, 30, 12, 0, 0)


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def paper30_source() -> Path:
    absorbed = ROOT / "repro" / "absorbed_paper30"
    sibling = ROOT.parent / "paper30-frontier"
    if absorbed.is_dir():
        return absorbed
    if sibling.is_dir():
        return sibling
    raise FileNotFoundError("Paper 30 source not found")


def add(entries: dict[str, Path], archive_path: str, source: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(source)
    if archive_path in entries:
        raise RuntimeError(f"duplicate archive path: {archive_path}")
    entries[archive_path] = source


def source_entries() -> dict[str, Path]:
    entries: dict[str, Path] = {}
    core = (
        "README.md",
        "CLAIM_LEDGER.md",
        "QA_REPORT.md",
        "REPRO_RELEASE_AUDIT.md",
        "paper.tex",
        "references.bib",
        "requirements.txt",
        "build_local.ps1",
        "run_scientific_replay.py",
        "package_release.py",
    )
    for relative in core:
        add(entries, relative, ROOT / relative)
    add(entries, "paper.pdf", PDF)
    add(entries, "paper.txt", ROOT / "output" / "pdf" / "paper.txt")

    math_files = (
        "math/verify_d_le_7_epigraph.py",
        "math/verify_d8_sharpness.py",
        "math/verify_rank_gap_frontier.py",
        "math/verify_zero_padding_fixture.py",
        "math/audit_d_le_7_equalities.py",
        "math/verify_low_dimension_minimality_exact.py",
        "math/results/d_le_7_epigraph_certificate.json",
        "math/MATH_AUDIT.md",
        "math/MANUSCRIPT_MATH_AUDIT.md",
        "math/INDEPENDENT_LOW_DIMENSION_AUDIT.md",
        "priority/MANUSCRIPT_PRIORITY_AUDIT.md",
        "priority/PRIORITY_MINIMAL_DIMENSION_AUDIT.md",
        "math/COARSE_GRAINING_THEOREM.md",
        "math/verify_hive_coarse_graining.py",
        "math/verify_block_inflation_endpoints.py",
        "repro/exact_hive_duals.json",
        "repro/extract_exact_hive_duals.py",
        "repro/verify_exact_hive_duals.py",
        "repro/EXACT_HIVE_DUAL_AUDIT.md",
        "repro/verify_coarse_graining_theorem.py",
        "repro/COARSE_GRAINING_AUDIT.md",
        "VIABILITY_MEMO.md",
        "priority/AMPLIFICATION_LITERATURE_ROUTE.md",
        "priority/FRONTIER_AUDIT.md",
        "priority/UNBOUNDED_EXCESS_GATE.md",
    )
    for relative in math_files:
        add(entries, relative, ROOT / relative)

    for source in sorted((ROOT / "tools").rglob("*")):
        archive_path = source.relative_to(ROOT).as_posix()
        try:
            regular = source.is_file()
        except OSError:
            regular = False
        if regular:
            add(entries, archive_path, source)
            continue
        # WSL-created ELF soname links appear as inaccessible Windows reparse
        # points.  Store a regular byte-identical soname copy so an ordinary
        # ZIP extraction remains standalone on both Windows/WSL and Linux.
        if source.name.endswith(".so.0"):
            targets = sorted(source.parent.glob(source.name + ".*"))
            if len(targets) != 1 or not targets[0].is_file():
                raise RuntimeError(f"cannot resolve WSL soname reparse point: {source}")
            add(entries, archive_path, targets[0])

    prior = paper30_source()
    paper30_files = (
        "README.md",
        "CLAIM_LEDGER.md",
        "MATH_AUDIT.md",
        "REPRO_FAMILY_AUDIT.md",
        "paper.tex",
        "references.bib",
        "verify_rank_gap_frontier.py",
        "verify_parametric_family.py",
        "verify_parametric_family_lr.py",
        "run_parametric_family_replay.py",
        "run_scientific_replay.ps1",
        "results/parametric_family_certificate.json",
        "results/parametric_family_lr_certificate.json",
    )
    for relative in paper30_files:
        add(entries, f"repro/absorbed_paper30/{relative}", prior / relative)
    return dict(sorted(entries.items()))


def manifest_bytes(entries: dict[str, Path]) -> bytes:
    files = [
        {
            "path": archive_path,
            "bytes": source.stat().st_size,
            "sha256": digest(source),
        }
        for archive_path, source in entries.items()
    ]
    payload = {
        "schema_version": 1,
        "title": "Sharp Onset and Unbounded Growth of Norm-Optimal Self-Commutator Rank",
        "author": "Lluis Eriksson",
        "frozen_date": "2026-08-30",
        "arr_record": "ARR-2026-5QQF95VHTC9GABH8",
        "record_type": "research_paper",
        "paper_pdf_sha256": EXPECTED_PDF_SHA256,
        "paper30_absorption": (
            "complete d8 parametric phase, independent recursive-Horn/direct-LR replays, "
            "and d9 two-valued witness preserved under repro/absorbed_paper30"
        ),
        "paper31_absorption": (
            "the complete sharp d<=7 threshold, d8 onset, and d9 seed are integrated into "
            "the present manuscript with their exact finite proof objects"
        ),
        "verification_scope": (
            "exact finite Horn/polyhedral replay and symbolic hive coarse-graining conditional on the classical Horn theorem; "
            "not peer review, formal proof-assistant certification, or priority adjudication"
        ),
        "files": files,
    }
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    executable = "/usr/bin/" in name or "/usr/lib/cdd-tools/" in name
    info.external_attr = (0o100755 if executable else 0o100644) << 16
    return info


def expected_payload() -> tuple[dict[str, Path], bytes]:
    entries = source_entries()
    if digest(PDF) != EXPECTED_PDF_SHA256:
        raise SystemExit(f"PDF hash mismatch: {digest(PDF)} != {EXPECTED_PDF_SHA256}")
    return entries, manifest_bytes(entries)


def check_archive(entries: dict[str, Path], manifest: bytes) -> None:
    if not ARCHIVE.is_file():
        raise FileNotFoundError(ARCHIVE)
    expected_names = set(entries) | {"manifest.json"}
    with zipfile.ZipFile(ARCHIVE, "r") as archive:
        if set(archive.namelist()) != expected_names:
            missing = expected_names - set(archive.namelist())
            extra = set(archive.namelist()) - expected_names
            raise SystemExit(f"archive member mismatch; missing={sorted(missing)}, extra={sorted(extra)}")
        for name, source in entries.items():
            if archive.read(name) != source.read_bytes():
                raise SystemExit(f"archive byte mismatch: {name}")
        if archive.read("manifest.json") != manifest:
            raise SystemExit("archive manifest differs")
    if MANIFEST_COPY.read_bytes() != manifest:
        raise SystemExit("external manifest copy differs")
    print(
        f"PASS release: {len(entries)} files; PDF {EXPECTED_PDF_SHA256}; "
        f"ZIP {digest(ARCHIVE)}; manifest {digest_bytes(manifest)}"
    )


def build(entries: dict[str, Path], manifest: bytes, skip_replay: bool) -> None:
    if not skip_replay:
        subprocess.run([sys.executable, str(ROOT / "run_scientific_replay.py")], cwd=ROOT, check=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    MANIFEST_COPY.write_bytes(manifest)
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, source in entries.items():
            archive.writestr(zip_info(name), source.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        archive.writestr(zip_info("manifest.json"), manifest, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    check_archive(entries, manifest)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify the existing ZIP without rebuilding")
    parser.add_argument("--skip-replay", action="store_true", help="development only: package without rerunning science")
    args = parser.parse_args()
    entries, manifest = expected_payload()
    if args.check:
        check_archive(entries, manifest)
    else:
        build(entries, manifest, args.skip_replay)


if __name__ == "__main__":
    main()

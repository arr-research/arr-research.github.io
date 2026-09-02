#!/usr/bin/env python3
"""Build the deterministic public reproducibility archive."""

from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PDF = ROOT / "output" / "pdf" / "Exact_Rank_Transitions_through_p32_and_p53_Optimum.pdf"
OUTPUT = ROOT / "output" / "release" / "Exact_Rank_Transitions_through_p32_REPRODUCIBILITY.zip"


def certificate_files() -> list[str]:
    names: list[str] = []
    expected_rank = {
        21: 45, 22: 47, 23: 49, 24: 51, 25: 53, 26: 55,
        27: 58, 28: 61, 29: 63, 30: 65, 31: 67, 32: 69,
    }
    for p, rank in expected_rank.items():
        names.append(f"primal_p{p}_rank{rank}.json")
        if p == 24:
            names.append("basis_dual_l1_p24.json")
        elif p == 28:
            names.append("basis_dual_l1_p28.json")
        else:
            names.append(f"basis_dual_l1_p{p}_full.json")
        names.append(f"basis_dual_l1_p{p}_rank{rank - 1}.json")
    return names


def source_map() -> dict[str, Path]:
    mapping = {
        "paper/paper.pdf": PDF,
        "paper/source/build_manuscript_pdf.py": HERE / "build_endpoint_nogo_note_pdf.py",
        "README.md": HERE / "REPRODUCIBILITY_README.md",
        "tools/package_release.py": HERE / "package_release.py",
    }
    replay_names = [
        "verify_exact_frontier_p21_p32.py",
        "verify_p28_exact_duals.py",
        "verify_p53_independent.py",
        "verify_p53_exact_endpoint.py",
        "verify_p53_endpoint_nogo.py",
        "verify_lr_frontier_bundle.py",
        "endpoint_horn_candidates.py",
    ]
    for name in replay_names:
        mapping[f"replay/{name}"] = HERE / name
    data_names = certificate_files() + [
        "p53_rank115_primal_certificate.json",
        "p53_unrestricted_dual_certificate.json",
        "p53_rank114_dual_certificate.json",
        "endpoint_p53_farkas_nogo.json",
        "horn_states_exact_p4_p18.json",
        "horn_states_exact_p19_p20.json",
        "lr_tableau_p4.json",
        "lr_tableaux_p5_p8.json",
        "lr_tableaux_p9_p15.json",
        "lr_tableaux_p16_p20.json",
        "lr_tableau_endpoint_p28.json",
    ]
    for name in data_names:
        mapping[f"replay/{name}"] = HERE / name
    return mapping


def main() -> None:
    if not __debug__:
        raise SystemExit("refusing optimized Python: packaging validation requires __debug__")
    files = source_map()
    missing = [str(path) for path in files.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError("missing release inputs:\n" + "\n".join(missing))
    hashes = {
        archive: hashlib.sha256(path.read_bytes()).hexdigest()
        for archive, path in sorted(files.items())
    }
    manifest = "".join(f"{digest}  {name}\n" for name, digest in hashes.items()).encode()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    timestamp = (2026, 9, 2, 0, 0, 0)
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, path in sorted(files.items()):
            info = zipfile.ZipInfo(name, timestamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
        info = zipfile.ZipInfo("MANIFEST.sha256", timestamp)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, manifest)
    print(OUTPUT.resolve())
    print(hashlib.sha256(OUTPUT.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()

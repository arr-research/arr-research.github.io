"""Independent exact certificate for the nonsingular part of the threshold.

The script proves, chamber by chamber, that for full-rank targets in
dimensions at most seven the
full Horn epigraph has the same ``(lambda,z)`` projection as the face whose
singular-value rank equals the inertia lower bound.  Hence a nuclear-norm
minimizer can always be chosen at inertia rank for those nonsingular targets.
Singular spectra are deliberately excluded here: assigning zero eigenvalues
to either sign chamber changes the face rank.  They are covered separately by
``verify_d_le_7_epigraph.py``, which enumerates every exact
``(n_+,n_-,n_0)`` stratum.

The only double-precision operation is sparse-certificate *discovery* by
HiGHS.  Every reported Farkas identity is reconstructed and checked over
``fractions.Fraction``.  Polyhedral conversion itself is performed by the GMP
rational build of cddlib (``lcdd_gmp``), vendored from Ubuntu's unmodified
``libcdd-tools``/``libcdd0t64`` packages.  The resulting H and V descriptions
are round-tripped exactly.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import subprocess
import sys
import tempfile
import time
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SPEC = importlib.util.spec_from_file_location(
    "lowproj", HERE / "explore_low_dimension_projection.py"
)
lowproj = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(lowproj)


def wsl_path(path: Path) -> str:
    resolved = path.resolve()
    drive = resolved.drive.rstrip(":").lower()
    rest = resolved.as_posix().split(":", 1)[1]
    return f"/mnt/{drive}{rest}"


CDD_ROOT = ROOT / "tools" / "linux" / "root"
CDD_LIB = wsl_path(CDD_ROOT / "usr" / "lib" / "x86_64-linux-gnu")
LCDD_GMP = wsl_path(CDD_ROOT / "usr" / "lib" / "cdd-tools" / "lcdd_gmp")
REDCHECK_GMP = wsl_path(CDD_ROOT / "usr" / "bin" / "redcheck_gmp")


def qtext(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def cdd_text(rep: str, rows) -> str:
    rows = [tuple(Q(x) for x in row) for row in rows]
    assert rep in {"H", "V"}
    kind = "H-representation" if rep == "H" else "V-representation"
    body = "\n".join(" ".join(qtext(x) for x in row) for row in rows)
    return f"{kind}\nbegin\n{len(rows)} {len(rows[0])} rational\n{body}\nend\n"


def parse_cdd_matrix(output: str):
    lines = [line.strip() for line in output.splitlines()]
    starts = [i for i, line in enumerate(lines) if line in {"H-representation", "V-representation"}]
    if not starts:
        raise RuntimeError(f"cdd output contains no representation:\n{output[-2000:]}")
    start = starts[-1]
    begin = next(i for i in range(start + 1, len(lines)) if lines[i] == "begin")
    count, width, _number_type = lines[begin + 1].split()[:3]
    count, width = int(count), int(width)
    rows = []
    for line in lines[begin + 2 : begin + 2 + count]:
        row = tuple(Q(token) for token in line.split())
        assert len(row) == width
        rows.append(row)
    assert lines[begin + 2 + count] == "end"
    return tuple(rows)


def lcdd(rep: str, rows):
    if not (CDD_ROOT / "usr" / "lib" / "cdd-tools" / "lcdd_gmp").exists():
        raise FileNotFoundError(
            "exact cdd binary missing; run bootstrap_exact_cdd.ps1 from the Paper 31 root"
        )
    command = (
        f"export LD_LIBRARY_PATH='{CDD_LIB}'; "
        f"exec '{LCDD_GMP}'"
    )
    result = subprocess.run(
        ["wsl", "-e", "sh", "-lc", command],
        input=cdd_text(rep, rows),
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"lcdd_gmp failed ({result.returncode})\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    return parse_cdd_matrix(result.stdout)


def redcheck(rep: str, rows):
    """Remove redundant rows using exact rational LPs in cddlib."""

    handle = tempfile.NamedTemporaryFile(
        mode="w", suffix=".ine" if rep == "H" else ".ext", delete=False, encoding="ascii"
    )
    try:
        with handle:
            handle.write(cdd_text(rep, rows))
        source = wsl_path(Path(handle.name))
        command = (
            f"export LD_LIBRARY_PATH='{CDD_LIB}'; "
            f"exec '{REDCHECK_GMP}'"
        )
        result = subprocess.run(
            ["wsl", "-e", "sh", "-lc", command],
            input=source + "\n",
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode:
            raise RuntimeError(
                f"redcheck_gmp failed ({result.returncode})\n"
                f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
            )
        return parse_cdd_matrix(result.stdout)
    finally:
        Path(handle.name).unlink(missing_ok=True)


def primitive_ray(row):
    assert row[0] == 0, row
    coordinates = tuple(row[1:])
    lcm = math.lcm(*(x.denominator for x in coordinates))
    integers = [int(x * lcm) for x in coordinates]
    gcd = math.gcd(*(abs(x) for x in integers if x))
    assert gcd
    integers = tuple(x // gcd for x in integers)
    # A ray has a fixed orientation; do not flip its sign.
    return integers


def primitive_inequality(row):
    assert row[0] == 0, row
    coordinates = tuple(row[1:])
    lcm = math.lcm(*(x.denominator for x in coordinates))
    integers = [int(x * lcm) for x in coordinates]
    gcd = math.gcd(*(abs(x) for x in integers if x))
    assert gcd
    return tuple(x // gcd for x in integers)


def exact_farkas(rows, target):
    """Find then exactly verify y>=0 with rows^T y=target."""

    array = np.asarray(rows, dtype=float)
    result = linprog(
        np.ones(len(rows)),
        A_eq=array.T,
        b_eq=np.asarray([float(x) for x in target]),
        bounds=(0, None),
        method="highs-ds",
        options={"dual_feasibility_tolerance": 1e-9, "primal_feasibility_tolerance": 1e-9},
    )
    if not result.success:
        raise AssertionError(result.message)
    support = [i for i, value in enumerate(result.x) if value > 1e-8]
    matrix = sp.Matrix(
        [[sp.Rational(rows[i][j]) for i in support] for j in range(len(target))]
    )
    rhs = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in target])
    solution, parameters = matrix.gauss_jordan_solve(rhs)
    if parameters.rows:
        solution = solution.subs({symbol: 0 for symbol in parameters})
    weights = [Q(int(x.p), int(x.q)) for x in solution]
    assert all(weight >= 0 for weight in weights)
    check = [Q(0)] * len(target)
    for index, weight in zip(support, weights):
        for j, value in enumerate(rows[index]):
            check[j] += weight * Q(value)
    assert tuple(check) == tuple(target)
    return tuple((i, w) for i, w in zip(support, weights) if w)


def project_v(rows, d: int, p_count: int):
    keep = [0, *range(1, d), d + p_count]
    projected = []
    for row in rows:
        assert row[0] == 0, "all epigraph generators must be rays"
        candidate = tuple(row[j] for j in keep)
        if any(candidate[1:]):
            projected.append(candidate)
    return tuple(projected)


def stable_digest(payload) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def verify_case(d: int, m: int):
    rank = max(m, d - m)
    full_h = tuple(tuple(Q(x) for x in row) for row in lowproj.chamber_rows(d, m, d - 1))
    face_h = tuple(tuple(Q(x) for x in row) for row in lowproj.chamber_rows(d, m, rank))
    print(f"d={d}, m={m}, r={rank}: exact face reduction ({len(face_h)} rows)", flush=True)
    started = time.perf_counter()
    reduced_face_h = redcheck("H", face_h)
    print(f"  retained {len(reduced_face_h)} exact nonredundant rows; H->V", flush=True)
    face_v = lcdd("H", reduced_face_h)
    projected_input_v = project_v(face_v, d, rank)
    projected_h = lcdd("V", projected_input_v)
    projected_extreme_v = lcdd("H", projected_h)

    input_rays = {primitive_ray(row) for row in projected_input_v}
    extreme_rays = {primitive_ray(row) for row in projected_extreme_v}
    assert extreme_rays <= input_rays
    # Exact H/V incidence checks in both directions.
    for ray in extreme_rays:
        assert all(sum(a * x for a, x in zip(h[1:], ray)) >= 0 for h in projected_h)
    assert sp.Matrix([list(h[1:]) for h in projected_h]).rank() == d

    face_rows = [row[1:] for row in face_h]
    full_rows = [row[1:] for row in full_h]
    certificate_records = []
    for h in projected_h:
        projected = h[1:]
        face_target = (*projected[: d - 1], *([Q(0)] * rank), projected[-1])
        full_target = (*projected[: d - 1], *([Q(0)] * (d - 1)), projected[-1])
        face_certificate = exact_farkas(face_rows, face_target)
        full_certificate = exact_farkas(full_rows, full_target)
        certificate_records.append(
            {
                "facet": list(primitive_inequality(h)),
                "face": [[i, qtext(w)] for i, w in face_certificate],
                "full": [[i, qtext(w)] for i, w in full_certificate],
            }
        )

    payload = {
        "d": d,
        "positive_count": m,
        "inertia_rank": rank,
        "horn_rows_full": len(full_h),
        "horn_rows_face": len(face_h),
        "nonredundant_face_rows": len(reduced_face_h),
        "face_extended_rays": len(face_v),
        "projected_input_rays": len(projected_input_v),
        "projected_extreme_rays": len(extreme_rays),
        "projected_facets": len(projected_h),
        "all_facets_exactly_valid_on_full": True,
        "roundtrip_extreme_rays_contained": True,
        "certificate_sha256": stable_digest(certificate_records),
        "elapsed_seconds": round(time.perf_counter() - started, 3),
    }
    print(json.dumps(payload, sort_keys=True), flush=True)
    return payload


def reflected_case(d: int, m: int):
    return {"d": d, "positive_count": d - m, "by_spectral_reflection_of": [d, m]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--case",
        action="append",
        default=[],
        help="critical case d:m; may be repeated (default: all d<=7 cases)",
    )
    args = parser.parse_args()
    critical = [(4, 2), (5, 2), (6, 2), (6, 3), (7, 2), (7, 3)]
    if args.case:
        critical = [tuple(map(int, item.split(":"))) for item in args.case]
    results = [verify_case(d, m) for d, m in critical]
    reflected = [
        reflected_case(d, m)
        for d, m in critical
        if m != d - m and d - m < d
    ]
    summary = {
        "status": "PASS",
        "theorem_scope": "full-rank trace-zero Hermitian spectra in dimensions d<=7",
        "critical_cases": results,
        "reflected_cases": reflected,
        "trivial_cases": "for nonsingular targets, inertia side 1 has rank d-1",
        "conclusion": (
            "the full and inertia-rank Horn epigraph projections coincide on "
            "every nonsingular chamber; singular strata require the companion verifier"
        ),
    }
    summary["summary_sha256"] = stable_digest(summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

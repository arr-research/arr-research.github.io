#!/usr/bin/env python3
"""Fail-closed verification of the calibration-memory certificate."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "results" / "calibration_memory" / "certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_record_structure(payload: dict) -> None:
    """Validate the fixed six-order certificate described in the manuscript."""
    require(type(payload.get("schema_version")) is int and payload["schema_version"] == 1, "unexpected schema")
    require(type(payload.get("alpha")) in (int, float) and math.isfinite(payload["alpha"]) and payload["alpha"] == 0.45, "wrong fixed alpha")
    rows = payload["records"]
    require(isinstance(rows, list), "records must be a list")
    require(all(isinstance(row, dict) and type(row.get("order")) is int for row in rows), "invalid order")
    require(sorted(row["order"] for row in rows) == [5, 7, 9, 11, 15, 19], "missing, duplicate or unexpected order")
    for row in rows:
        order = row["order"]
        for key in ["calibration_multiplicity", "full_network_mcmillan_degree", "degree_overhead", "loss_minor_scalar_degree", "loss_minor_calibration_zeros"]:
            require(type(row[key]) is int and row[key] >= 0, "invalid integral count: " + key)
        require(row["loss_minor_scalar_degree"] == 3 * order + 3, "wrong loss-minor degree")
        require(row["topological_lower_bound_satisfied"] is True, "invalid bound flag")
        for key in ["maximum_boundary_root_error", "maximum_loss_minor_zero_residual", "strict_stop_loss_determinant", "wigner_smith_integral_over_2pi", "wigner_smith_quadrature_error_over_2pi", "wigner_smith_peak_trace"]:
            finite_nonnegative(row[key], key)
        require(row["wigner_smith_peak_trace"] >= row["full_network_mcmillan_degree"], "peak below mean")
        require(row["strict_stop_loss_determinant"] <= 1 + 1e-10, "stop determinant exceeds contractive bound")
        expected_stop = math.cos(0.5 * math.exp(-payload["alpha"] * order)) ** 2
        require(math.isclose(row["strict_stop_loss_determinant"], expected_stop, rel_tol=1e-10, abs_tol=1e-12), "wrong analytic strict-stop formula")
        expected_peak = 6 + 3 * order * (2 * math.exp(payload["alpha"] * order) - 1)
        require(math.isclose(row["wigner_smith_peak_trace"], expected_peak, rel_tol=1e-8, abs_tol=1e-9), "wrong analytic peak formula")
        require(row["wigner_smith_quadrature_error_over_2pi"] <= 2e-7, "excessive quadrature error estimate")
    rouche = payload["rouche_passive_perturbation"]
    require(type(rouche["order"]) is int and rouche["order"] == 5, "unexpected perturbation order")
    require(type(rouche["calibration_zero_count"]) is int and rouche["calibration_zero_count"] == 15, "wrong perturbation zero count")
    counts = rouche["root_counts_per_contour"]
    require(isinstance(counts, list) and len(counts) == rouche["calibration_zero_count"], "incomplete contour inventory")
    require(all(type(count) is int and count == 1 for count in counts), "invalid contour multiplicity")
    require(rouche["all_contours_retain_one_zero"] is True, "invalid contour flag")
    for key in ["perturbation_radians", "minimum_contour_radius", "minimum_reference_modulus", "maximum_perturbation_modulus", "maximum_rouche_ratio"]:
        finite_nonnegative(rouche[key], key)
    require(rouche["minimum_contour_radius"] > 0 and rouche["minimum_reference_modulus"] > 0, "nonpositive contour margin")
    require(rouche["perturbation_radians"] == 0.0002, "wrong fixed perturbation")
    delta_max = rouche["maximum_perturbation_modulus"]
    ratio = rouche["maximum_rouche_ratio"]
    upper_ratio = delta_max / rouche["minimum_reference_modulus"]
    require((delta_max == 0) == (ratio == 0), "inconsistent zero perturbation and ratio")
    require(ratio <= upper_ratio + 1e-12 * max(1.0, upper_ratio), "Rouche ratio exceeds extrema upper bound")
    random = payload["random_potapov_minor_stress_test"]
    require(type(random["seed"]) is int and random["seed"] == 20260810, "wrong fixed seed")
    require(type(random["trials"]) is int and random["trials"] == 128, "wrong fixed trial count")
    require(type(random["maximum_factor_count"]) is int and random["maximum_factor_count"] == 9, "wrong fixed factor count")
    require(all(type(v) is int for v in random["minor_sizes_tested"]), "invalid rank type")
    require(type(random["trials"]) is int and random["trials"] >= 100, "invalid trial count")
    require(type(random["matrix_size"]) is int and random["matrix_size"] == 6, "wrong matrix size")
    require(type(random["maximum_factor_count"]) is int and random["maximum_factor_count"] > 0, "invalid factor budget")
    require(type(random["largest_fitted_polynomial_degree"]) is int and 0 <= random["largest_fitted_polynomial_degree"] <= random["maximum_factor_count"], "invalid fitted degree")
    require(random["all_minors_fit_the_factor_count_budget"] is True, "invalid minor flag")
    finite_nonnegative(random["maximum_relative_interpolation_residual"], "minor residual")


def finite_nonnegative(value: object, name: str) -> None:
    require(type(value) in (int, float) and math.isfinite(value) and value >= 0, "invalid magnitude: " + name)


def main() -> None:
    payload = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    check_record_structure(payload)
    require(payload["schema_version"] == 1, "unexpected schema")
    require(len(payload["records"]) >= 6, "scaling ledger is incomplete")
    for record in payload["records"]:
        order = record["order"]
        require(record["calibration_multiplicity"] == 3 * order, f"wrong calibration count at S={order}")
        require(record["full_network_mcmillan_degree"] == 3 * order + 6, f"wrong degree at S={order}")
        require(record["degree_overhead"] == 6, f"construction is not near-optimal at S={order}")
        require(record["loss_minor_calibration_zeros"] == 3 * order, f"loss zero count failed at S={order}")
        require(record["maximum_boundary_root_error"] < 1.0e-14, f"root audit failed at S={order}")
        require(record["maximum_loss_minor_zero_residual"] < 2.0e-10, f"loss zero residual failed at S={order}")
        require(record["strict_stop_loss_determinant"] > 0.5, f"loss minor may be trivial at S={order}")
        require(abs(record["wigner_smith_integral_over_2pi"] - (3 * order + 6)) < 2.0e-7, f"delay sum rule failed at S={order}")
        require(record["topological_lower_bound_satisfied"], f"topological bound failed at S={order}")
    rouche = payload["rouche_passive_perturbation"]
    require(rouche["maximum_rouche_ratio"] < 1.0, "Rouche inequality is not strict")
    require(rouche["all_contours_retain_one_zero"], "perturbed root left a certified contour")
    require(all(count == 1 for count in rouche["root_counts_per_contour"]), "wrong contour root multiplicity")
    random_minors = payload["random_potapov_minor_stress_test"]
    require(random_minors["trials"] >= 100, "random minor stress test is too small")
    require(random_minors["minor_sizes_tested"] == [1, 2, 3, 4, 5, 6], "not all compound ranks were tested")
    require(random_minors["all_minors_fit_the_factor_count_budget"], "a random minor exceeded its Potapov degree budget")
    require(random_minors["maximum_relative_interpolation_residual"] < 1.0e-8, "random minor interpolation residual is too large")
    print("calibration-memory certificate: PASS")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"calibration-memory certificate: FAIL: {exc}", file=sys.stderr)
        raise

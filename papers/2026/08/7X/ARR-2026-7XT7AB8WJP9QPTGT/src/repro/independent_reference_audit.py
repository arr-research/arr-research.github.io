"""Independent shadow audit for the support-0.72 release.

This program deliberately imports no project module and no python-flint code.
It reconstructs the prime-power graph and parity dimensions from the printed
formulas, then reassembles the two Schur balls from the exported component
balls.  High-precision mpmath eigenvalues and a row-sum bound for the radius
matrix provide an independent wiring/sign diagnostic.  The formal theorem
still rests on the Arb verifier; this audit is designed to catch a shared
assembly or serialization mistake.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np


EXPECTED_EDGES = {
    2: ((0, 6), (1, 7), (2, 8), (3, 9), (4, 10), (5, 11), (6, 12)),
    3: ((0, 10), (1, 11), (2, 12)),
    4: ((0, 12),),
}


def as_mp(value: float) -> mp.mpf:
    numerator, denominator = float(value).as_integer_ratio()
    return mp.mpf(numerator) / denominator


def matrix(array: np.ndarray) -> mp.matrix:
    rows, columns = array.shape
    return mp.matrix([[as_mp(array[i, j]) for j in range(columns)] for i in range(rows)])


def graph_and_parity_audit() -> None:
    mp.mp.dps = 100
    a = mp.mpf(18) / 25
    h2, h3 = mp.log(2) / a, mp.log(3) / a
    cuts = (
        -1, 1 - 2 * h2, -1 + 2 * h2 - h3, 1 - h3,
        -1 - h2 + h3, 1 - 3 * h2 + h3, -1 + h2, 1 - h2,
        -1 + 3 * h2 - h3, 1 + h2 - h3, -1 + h3,
        1 - 2 * h2 + h3, -1 + 2 * h2, 1,
    )
    assert all(cuts[i] < cuts[i + 1] for i in range(13))
    for prime, shift in ((2, h2), (3, h3), (4, 2 * h2)):
        recovered = []
        for left in range(13):
            for right in range(left + 1, 13):
                if abs((cuts[right] - cuts[left]) - shift) < mp.mpf("1e-90"):
                    if abs((cuts[right + 1] - cuts[left + 1]) - shift) < mp.mpf("1e-90"):
                        recovered.append((left, right))
        assert tuple(recovered) == EXPECTED_EDGES[prime]

    degree = 12
    total = 13 * degree
    even = np.zeros((total, 78))
    odd = np.zeros((total, 78))
    invsqrt2 = 2.0 ** -0.5
    column = 0
    for left, right in ((0, 12), (1, 11), (2, 10), (3, 9), (4, 8), (5, 7)):
        for local in range(degree):
            reflection = -1.0 if local % 2 else 1.0
            even[left * degree + local, column] = invsqrt2
            even[right * degree + local, column] = reflection * invsqrt2
            odd[left * degree + local, column] = invsqrt2
            odd[right * degree + local, column] = -reflection * invsqrt2
            column += 1
    for local in range(0, degree, 2):
        even[6 * degree + local, column] = 1.0
        column += 1
    column = 72
    for local in range(1, degree, 2):
        odd[6 * degree + local, column] = 1.0
        column += 1
    identity_error = np.max(np.abs(even.T @ even - np.eye(78)))
    identity_error = max(identity_error, np.max(np.abs(odd.T @ odd - np.eye(78))))
    completeness_error = np.max(np.abs(even @ even.T + odd @ odd.T - np.eye(total)))
    assert identity_error < 3e-16 and completeness_error < 3e-16


def add_scaled(mid: mp.matrix, rad: mp.matrix, part_mid, part_rad, scale: mp.mpf, sign=-1):
    pm, pr = matrix(part_mid), matrix(part_rad)
    return mid + sign * pm / scale, rad + pr / scale


def parity_schur(root: Path, aggregate, bands, record, parity: str):
    def component(name: str):
        return (
            aggregate[f"{name}_{parity}_midpoint"],
            aggregate[f"{name}_{parity}_radius"],
        )

    source_mid, source_rad = component("source")
    aggregate_mid, aggregate_rad = component("band")
    flux_mid, flux_rad = component("flux")
    singular_mid, singular_rad = component("singular")
    self_mid, self_rad = component("self")
    mid, rad = matrix(source_mid), matrix(source_rad)
    smooth = as_mp(record["smooth_remainder"])
    for i in range(78):
        mid[i, i] -= smooth

    registered_mid = np.zeros((78, 78))
    registered_rad = np.zeros((78, 78))
    for index in range(12):
        part_mid = bands[f"band_{index}_{parity}_midpoint"]
        part_rad = bands[f"band_{index}_{parity}_radius"]
        registered_mid += part_mid
        registered_rad += part_rad
        denominator = as_mp(record["band_denominator_lowers"][index])
        mid, rad = add_scaled(mid, rad, part_mid, part_rad, denominator)
    residual_mid = aggregate_mid - registered_mid
    residual_rad = aggregate_rad + registered_rad
    residual_denominator = as_mp(record["band_denominator_lowers"][12])
    mid, rad = add_scaled(mid, rad, residual_mid, residual_rad, residual_denominator)

    balance = as_mp(record["tail_balance"])
    residual_balance = as_mp(record["residual_balance"])
    structured_mid = 2 * (matrix(flux_mid) + matrix(singular_mid))
    structured_rad = 2 * (matrix(flux_rad) + matrix(singular_rad))
    coupling_mid = (1 + residual_balance) * (
        (1 + balance) * structured_mid + (1 + 1 / balance) * matrix(self_mid)
    )
    coupling_rad = (1 + residual_balance) * (
        (1 + balance) * structured_rad + (1 + 1 / balance) * matrix(self_rad)
    )
    scalar_tail = (1 + 1 / residual_balance) * as_mp(record["other_tail_norm"]) ** 2
    for i in range(78):
        coupling_mid[i, i] += scalar_tail

    low = Fraction.from_float(float(record["complement_floor"]))
    tail = low + sum(Fraction(1, k) for k in range(13, 177))
    tail_denominator = mp.mpf(tail.numerator) / tail.denominator
    mid -= coupling_mid / tail_denominator
    rad += coupling_rad / tail_denominator

    mid = (mid + mid.T) / 2
    eigenvalues = mp.eigsy(mid, eigvals_only=True)
    radius_row_bound = max(sum(rad[i, j] for j in range(78)) for i in range(78))
    independent_lower = eigenvalues[0] - radius_row_bound
    if not independent_lower > 0:
        raise AssertionError(f"{parity} shadow Schur audit did not close")
    return {
        "midpoint_lambda_min": mp.nstr(eigenvalues[0], 18),
        "radius_row_sum_upper": mp.nstr(radius_row_bound, 18),
        "weyl_lower": mp.nstr(independent_lower, 18),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.directory.resolve()
    graph_and_parity_audit()
    aggregate = np.load(root / "theta-schur-a072-d12-p47-tail8192-v3.npz")
    bands = np.load(root / "theta-near-band-a072-d12-to24-by-degree-p512-v3.npz")
    record = json.loads(
        (root / "theta-schur-a072-multiband-to24-by-degree-v3.json").read_text()
    )
    result = {
        "role": "independent non-Arb shadow audit; the Arb verifier remains the proof",
        "graph_and_parity": "PASS",
        "even": parity_schur(root, aggregate, bands, record, "even"),
        "odd": parity_schur(root, aggregate, bands, record, "odd"),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()

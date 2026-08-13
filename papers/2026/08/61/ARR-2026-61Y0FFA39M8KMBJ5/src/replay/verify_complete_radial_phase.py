"""Exact-algebra replay for the complete radial phase theorem.

The proof in the paper is analytic.  This script checks the closed coefficient
formula that makes the proof possible and reports high-precision diagnostics
for the unique fold and coexistence contact.  It performs no search over
matrices and is not a substitute for the sign proof printed in the paper.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp


def coefficient_sum(n: int) -> int:
    """Integer S_n with [k^(2n)]N(k)=8 S_n/(2n)! for n>=4."""
    return sum(
        math.comb(2 * n, 2 * i) * (n - 4 - (2 * i - n) ** 2)
        for i in range(2, n - 1)
    )


def coefficient_closed(n: int) -> int:
    return (
        2 ** (2 * n - 2) * (n - 8)
        + 2 * (2 * n**4 - 11 * n**3 + 22 * n**2 - 9 * n + 4)
    )


def exact_coefficient_checks(max_n: int = 80) -> dict:
    assert max_n >= 8
    rows = []
    for n in range(4, max_n + 1):
        direct = coefficient_sum(n)
        closed = coefficient_closed(n)
        assert direct == closed
        rows.append({"n": n, "S_n": direct})
    assert coefficient_closed(4) == 0
    assert coefficient_closed(5) == 0
    assert coefficient_closed(6) == -132
    assert coefficient_closed(7) == 0
    for n in range(8, max_n + 1):
        assert coefficient_closed(n) > 0
    return {
        "identity_checked_through_n": max_n,
        "exceptional_values": {str(n): coefficient_closed(n) for n in range(4, 8)},
        "minimum_positive_S_n_n_ge_8": min(coefficient_closed(n) for n in range(8, max_n + 1)),
        "analytic_tail_reason": (
            "For n>=8, 2^(2n-2)(n-8)>=0 and, on writing n=m+8, "
            "the remaining polynomial is "
            "2(2m^4+53m^3+526m^2+2327m+3900)>0."
        ),
        "scope": "Finite exact replay of the coefficient identity; the all-n sign proof is printed in the manuscript.",
    }


def A(k: mp.mpf) -> mp.mpf:
    return 2 * mp.cosh(k) - 2 - k * k


def K(k: mp.mpf) -> mp.mpf:
    return mp.log(12 * A(k) / k**4)


def Kp(k: mp.mpf) -> mp.mpf:
    return (2 * mp.sinh(k) - 2 * k) / A(k) - 4 / k


def Kpp(k: mp.mpf) -> mp.mpf:
    ap = 2 * mp.sinh(k) - 2 * k
    app = 2 * mp.cosh(k) - 2
    return app / A(k) - (ap / A(k)) ** 2 + 4 / k**2


def H(k: mp.mpf) -> mp.mpf:
    return Kp(k) - k * Kpp(k)


def F(k: mp.mpf) -> mp.mpf:
    return 2 * K(k) - k * Kp(k)


def phase_diagnostics(dps: int = 70) -> dict:
    mp.mp.dps = dps
    fold = mp.findroot(H, (mp.mpf("4.2"), mp.mpf("4.7")))
    contact = mp.findroot(F, (mp.mpf("5.2"), mp.mpf("5.9")))
    b_fold = Kp(fold)
    b_contact = Kp(contact)
    lambda_fold = 2 * fold / b_fold
    lambda_contact = 2 * contact / b_contact
    d_contact = (1 - b_contact**2) / 4
    r_contact = contact * b_contact - K(contact)
    assert fold > 0 and contact > fold
    assert lambda_fold < lambda_contact < 30
    assert abs(H(fold)) < mp.mpf(10) ** (-(dps - 15))
    assert abs(F(contact)) < mp.mpf(10) ** (-(dps - 15))
    assert abs(r_contact - lambda_contact * (mp.mpf(1) / 4 - d_contact)) < mp.mpf(10) ** (-(dps - 15))

    def s(x: mp.mpf) -> str:
        return mp.nstr(x, 45)

    return {
        "precision_decimal_digits": dps,
        "unique_fold_diagnostics": {
            "kappa_fold": s(fold),
            "b_fold": s(b_fold),
            "lambda_min": s(lambda_fold),
            "H_residual": s(H(fold)),
        },
        "unique_contact_diagnostics": {
            "kappa_c": s(contact),
            "b_c": s(b_contact),
            "lambda_c": s(lambda_contact),
            "D_c": s(d_contact),
            "R_c_nats": s(r_contact),
            "F_residual": s(F(contact)),
            "coexistence_line_residual": s(
                r_contact - lambda_contact * (mp.mpf(1) / 4 - d_contact)
            ),
        },
        "scope": "High-precision diagnostics; uniqueness and no-reentrance follow analytically from the coefficient signs.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=80)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("work/tenth_paper/repro/complete_radial_phase.json"),
    )
    args = parser.parse_args()
    result = {
        "exact_coefficient_replay": exact_coefficient_checks(args.max_n),
        "phase_diagnostics": phase_diagnostics(args.dps),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    result["output_sha256"] = hashlib.sha256(args.output.read_bytes()).hexdigest()
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

"""Bounded numerical replay for the exact large-q contact asymptotics."""

import json
from math import log, pi

from scipy.optimize import brentq
from scipy.special import hyp1f1, logsumexp


def k_m(q: int, kappa: float) -> tuple[float, float]:
    lp = float(hyp1f1(1.0, q + 1.0, kappa))
    lm = float(hyp1f1(1.0, q + 1.0, -kappa))
    l = 0.5 * (lp + lm)
    derivative = 0.5 / (q + 1.0) * (
        float(hyp1f1(2.0, q + 2.0, kappa))
        - float(hyp1f1(2.0, q + 2.0, -kappa))
    )
    return log(l), derivative / l


def contact(q: int) -> dict[str, float]:
    def f(kappa: float) -> float:
        k, m = k_m(q, kappa)
        return 2.0 * k - kappa * m

    root = brentq(f, 1.05 * q, 6.0 * q, xtol=2e-12, rtol=2e-14)
    k, b = k_m(q, root)
    lam = root / (2.0 * b)
    return {"q": q, "kappa_c": root, "lambda_c": lam,
            "b_c": b, "D_c": 1.0 - b * b,
            "R_c": root * b - k}


def main() -> None:
    y_star = brentq(lambda y: y - 1.0 - 2.0 * log(y), 2.01, 6.0)
    alpha = y_star * y_star / (2.0 * (y_star - 1.0))
    b_star = 1.0 - 1.0 / y_star
    d_star = 1.0 - b_star * b_star
    rows = []
    for q in (4, 5, 6, 8, 12, 20, 40, 80, 120):
        row = contact(q)
        ell = log(pi * q / 2.0)
        row["kappa_residual"] = row["kappa_c"] - (
            q * y_star - y_star / (y_star - 2.0) * ell
        )
        row["lambda_residual"] = row["lambda_c"] - (
            q * alpha - y_star**2 / (2.0 * (y_star - 1.0) ** 2) * ell
        )
        rows.append(row)
    assert abs(rows[-1]["kappa_residual"]) < abs(rows[0]["kappa_residual"])
    assert abs(rows[-1]["lambda_residual"]) < abs(rows[0]["lambda_residual"])
    payload = {"y_star": y_star, "alpha_star": alpha,
               "b_star": b_star, "D_star": d_star, "rows": rows}
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()

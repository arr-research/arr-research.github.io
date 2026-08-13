from __future__ import annotations

import json
import math
import random
from fractions import Fraction as F
from pathlib import Path


def recurrence(n: int, x: float, kind: str) -> float:
    if n == 0:
        return 1.0
    if kind == "T":
        p0, p1 = 1.0, x
    elif kind == "W":
        p0, p1 = 1.0, 2.0 * x + 1.0
    else:
        raise ValueError(kind)
    if n == 1:
        return p1
    for _ in range(2, n + 1):
        p0, p1 = p1, 2.0 * x * p1 - p0
    return p1


def evaluate(coefficients: list[float], x: float) -> float:
    value = 0.0
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


def weighted_sup(coefficients: list[float], points: int = 20001) -> float:
    maximum = 0.0
    for j in range(points):
        y = -1.0 + 2.0 * j / (points - 1)
        maximum = max(maximum, math.sqrt(max(0.0, 1.0 - y)) * abs(evaluate(coefficients, y)))
    return maximum


def main() -> None:
    theta = F(1, 2)
    delta = F(1, 4)
    gamma = F(1, 5)
    y_delta = 2.0
    degree = 2
    t_den = recurrence(degree, y_delta, "T")
    w_den = recurrence(degree, y_delta, "W")
    assert t_den == 7.0 and w_den == 19.0
    old_loss = theta / F(49)
    new_loss = theta / F(361)
    old_margin = delta * gamma - old_loss * (1 - gamma)
    new_margin = delta * gamma - new_loss * (1 - gamma)
    assert old_margin == F(41, 980)
    assert new_margin == F(353, 7220)

    for n in range(1, 9):
        assert recurrence(n, y_delta, "W") > recurrence(n, y_delta, "T")
        den = recurrence(n, y_delta, "W")
        candidate = [0.0] * (n + 1)
        # Interpolate coefficients from the recurrence itself.
        w0 = [1.0]
        if n == 1:
            candidate = [1.0 / den, 2.0 / den]
        elif n == 0:
            candidate = [1.0]
        else:
            w1 = [1.0, 2.0]
            for _ in range(2, n + 1):
                shifted = [0.0] + [2.0 * c for c in w1]
                size = max(len(shifted), len(w0))
                shifted += [0.0] * (size - len(shifted))
                previous = w0 + [0.0] * (size - len(w0))
                w0, w1 = w1, [a - b for a, b in zip(shifted, previous)]
            candidate = [c / den for c in w1]
        optimum = math.sqrt(2.0) / den
        assert abs(weighted_sup(candidate) - optimum) < 2e-7

        rng = random.Random(7100 + n)
        for _ in range(250):
            trial = [rng.uniform(-2.0, 2.0) for _ in range(n + 1)]
            value = evaluate(trial, y_delta)
            if abs(value) < 1e-8:
                continue
            trial = [coefficient / value for coefficient in trial]
            assert weighted_sup(trial, points=4001) >= optimum - 2e-4

    beta = F(24109, 2500)
    dimension = 2
    fisher = ((beta - 1) ** 2 + dimension - 1) / 2
    assert fisher == F(473198881, 12500000)
    w = F(1, 100)
    samples = 25
    tau = 1 + float(w * (beta - 1))
    rho = 1 - float(w)
    exact_kl = samples * 0.5 * (
        (dimension - 1) * (rho - 1 - math.log(rho))
        + tau - 1 - math.log(tau)
    )
    eigenvalue_kl = samples * 0.5 * sum(
        t - math.log1p(t) for t in (float(w * (beta - 1)), float(-w))
    )
    assert abs(exact_kl - eigenvalue_kl) < 1e-13

    payload = {
        "status": "PASS",
        "schema": "paper16-weighted-boundary-v1",
        "fixture": {
            "theta": str(theta),
            "delta": str(delta),
            "gamma": str(gamma),
            "degree": degree,
            "T2_at_2": t_den,
            "W2_at_2": w_den,
            "first_kind_margin": str(old_margin),
            "fourth_kind_margin": str(new_margin),
            "fisher_information": str(fisher),
            "exact_product_KL": exact_kl,
        },
        "deterministic_random_competitors_checked": 8 * 250,
    }
    output = Path(__file__).with_name("weighted_boundary_certificate.json")
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("weighted localizer and LAN certificate: PASS")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

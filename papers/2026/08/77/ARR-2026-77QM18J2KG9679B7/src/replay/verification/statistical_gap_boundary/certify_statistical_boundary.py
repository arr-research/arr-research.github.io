from __future__ import annotations

import json
import math
from fractions import Fraction as F
from pathlib import Path


def chebyshev_coefficients(n: int) -> list[int]:
    t0 = [1]
    if n == 0:
        return t0
    t1 = [0, 1]
    if n == 1:
        return t1
    for _ in range(2, n + 1):
        twice_x_t1 = [0] + [2 * c for c in t1]
        size = max(len(twice_x_t1), len(t0))
        twice_x_t1 += [0] * (size - len(twice_x_t1))
        old = t0 + [0] * (size - len(t0))
        t0, t1 = t1, [a - b for a, b in zip(twice_x_t1, old)]
    return t1


def fourth_kind_coefficients(n: int) -> list[int]:
    """Coefficients of W_n(x), with W_0=1 and W_1=2x+1."""
    w0 = [1]
    if n == 0:
        return w0
    w1 = [1, 2]
    if n == 1:
        return w1
    for _ in range(2, n + 1):
        twice_x_w1 = [0] + [2 * c for c in w1]
        size = max(len(twice_x_w1), len(w0))
        twice_x_w1 += [0] * (size - len(twice_x_w1))
        old = w0 + [0] * (size - len(w0))
        w0, w1 = w1, [a - b for a, b in zip(twice_x_w1, old)]
    return w1


def evaluate(coefficients: list[int], x: F) -> F:
    value = F(0)
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


def exact_upper_fixture() -> dict[str, str | int | float]:
    theta = F(1, 2)
    delta = F(1, 4)
    gamma = F(1, 5)
    degree = 2
    # 1 + 2 delta/theta = 2.  The old first-kind filter has T_2(2)=7;
    # the localizer-optimal fourth-kind filter has W_2(2)=19.
    t2 = chebyshev_coefficients(degree)
    assert t2 == [-1, 0, 2]
    w2 = fourth_kind_coefficients(degree)
    assert w2 == [-1, 2, 4]
    first_kind_denominator = evaluate(t2, F(2))
    fourth_kind_denominator = evaluate(w2, F(2))
    assert first_kind_denominator == 7
    assert fourth_kind_denominator == 19
    first_kind_loss = theta / first_kind_denominator**2
    weighted_loss = theta / fourth_kind_denominator**2
    margin = delta * gamma - weighted_loss * (1 - gamma)
    r0 = margin / (1 + theta)
    assert first_kind_loss == F(1, 98)
    assert weighted_loss == F(1, 722)
    assert margin == F(353, 7220)
    assert r0 == F(353, 10830)
    extremal_q = weighted_loss * (1 - gamma) - delta * gamma
    assert extremal_q == -margin

    alpha = 0.05
    # The Chebyshev filter is precommitted, so each raw sketch is compressed
    # to (p_N(T)V, T p_N(T)V) before the 2D Wishart band is formed.
    dimension = 2
    prefactor = (math.sqrt(dimension) + math.sqrt(2 * math.log(2 / alpha))) ** 2
    sample_bound = prefactor * (math.sqrt(1 + float(r0)) + 1) ** 4 / float(r0) ** 2
    return {
        "theta": str(theta),
        "delta": str(delta),
        "gamma": str(gamma),
        "degree": degree,
        "first_kind_denominator": str(first_kind_denominator),
        "fourth_kind_denominator": str(fourth_kind_denominator),
        "first_kind_localizer_loss": str(first_kind_loss),
        "optimal_weighted_localizer_loss": str(weighted_loss),
        "population_margin": str(margin),
        "extremal_localizer_value": str(extremal_q),
        "uncertainty_ratio_lower_bound": str(r0),
        "confidence_alpha": alpha,
        "feature_dimension": dimension,
        "strict_sample_size_threshold": sample_bound,
        "integer_sample_size_sufficient": math.floor(sample_bound) + 1,
    }


def exact_lower_fixture() -> dict[str, str | int | float]:
    # N=0, theta=1/2. Two support points x=y^2 with y=1/3,2/3
    # give K0=[[1,1/2],[1/2,5/18]]. Its exact inverse is below.
    k00, k01, k11 = F(1), F(1, 2), F(5, 18)
    det = k00 * k11 - k01 * k01
    assert det == F(1, 36)
    inv = ((F(10), F(-18)), (F(-18), F(36)))
    # A strictly subunit near-critical atom: x_*=(99/100)^2.
    sqrt_x_star = F(99, 100)
    x_star = sqrt_x_star**2
    beta = (
        inv[0][0]
        + (inv[0][1] + inv[1][0]) * sqrt_x_star
        + inv[1][1] * x_star
    )
    assert beta == F(24109, 2500)
    op_norm_a = max(abs(beta - 1), 1)
    frobenius_sq_a = (beta - 1) ** 2 + 1
    assert op_norm_a == F(21609, 2500)

    w = F(1, 100)
    samples = 25
    assert w * op_norm_a <= F(1, 2)
    kl_upper = samples * float(w**2 * frobenius_sq_a) / 2
    tv_upper = float(w) * math.sqrt(samples * float(frobenius_sq_a)) / 2
    eig_t = (float(w * (beta - 1)), float(-w))
    kl_exact = samples * 0.5 * sum(t - math.log1p(t) for t in eig_t)
    assert kl_exact <= kl_upper + 1e-15
    assert math.sqrt(kl_exact / 2) <= tv_upper + 1e-15
    fisher_information = frobenius_sq_a / 2
    local_h = F(1, 5)
    normal = math.erf
    z_95 = 1.6448536269514722
    local_power = 1 - 0.5 * (
        1 + normal((z_95 - float(local_h) * math.sqrt(float(fisher_information))) / math.sqrt(2))
    )
    return {
        "theta": "1/2",
        "support_x": ["1/9", "4/9"],
        "K0_determinant": str(det),
        "beta": str(beta),
        "near_critical_atom_x": str(x_star),
        "near_critical_positive_gap": -math.log(float(x_star)),
        "A_operator_norm": str(op_norm_a),
        "A_frobenius_norm_squared": str(frobenius_sq_a),
        "hidden_atom_weight": str(w),
        "samples": samples,
        "exact_product_KL": kl_exact,
        "quadratic_KL_upper_bound": kl_upper,
        "pinsker_TV_upper_bound": tv_upper,
        "hidden_atom_fisher_information": str(fisher_information),
        "local_parameter_h": str(local_h),
        "asymptotic_level_0.05_power": local_power,
    }


def bounded_unknown_mean_fixture() -> dict[str, str | int | float]:
    theta = F(1, 2)
    delta = F(1, 4)
    gamma = F(1, 5)
    fourth_kind_denominator = F(19)
    weighted_loss = theta / fourth_kind_denominator**2
    margin = delta * gamma - weighted_loss * (1 - gamma)
    assert margin == F(353, 7220)

    raw_coordinate_bound = F(1)
    # At theta=1/2 both branches of L_theta(B) equal 4 B^2.
    range_length = 4 * raw_coordinate_bound**2
    filter_count = 3
    alpha = 0.05
    beta = 0.05
    paired_threshold = (
        float(range_length**2) / (2 * float(margin**2))
        * (
            math.sqrt(math.log(filter_count / alpha))
            + math.sqrt(math.log(1 / beta))
        )
        ** 2
    )
    paired_sufficient = math.floor(paired_threshold) + 1
    return {
        "theta": str(theta),
        "raw_coordinate_bound": str(raw_coordinate_bound),
        "exact_statistic_range_length": str(range_length),
        "filter_count": filter_count,
        "confidence_alpha": alpha,
        "power_beta": beta,
        "population_margin": str(margin),
        "strict_paired_sample_threshold": paired_threshold,
        "integer_paired_samples_sufficient": paired_sufficient,
        "integer_raw_observations_sufficient": 2 * paired_sufficient,
    }


def dependent_mixing_fixture() -> dict[str, str | int | float]:
    theta = F(1, 2)
    margin = F(353, 7220)
    raw_coordinate_bound = F(1)
    range_length = F(4)
    filter_count = 3
    alpha = 0.05
    miss_probability = 0.05
    coupling_budget = F(1, 100)

    def conservative_bias(n: int) -> F:
        return 2 * (1 + theta) * raw_coordinate_bound**2 * coupling_budget / (n - 1)

    def threshold(n: int) -> float:
        bias = conservative_bias(n)
        separation = margin - 2 * bias
        if separation <= 0:
            return math.inf
        return (
            float(range_length**2) / (2 * float(separation**2))
            * (
                math.sqrt(math.log(filter_count / (alpha - float(coupling_budget))))
                + math.sqrt(math.log(1 / (miss_probability - float(coupling_budget))))
            )
            ** 2
        )

    paired_blocks = 2
    while paired_blocks <= threshold(paired_blocks):
        paired_blocks += 1
    assert paired_blocks == 50177
    assert paired_blocks - 1 <= threshold(paired_blocks - 1)

    # beta_mix(q) <= 2^{-q}; q is the smallest integer with
    # (n-1) 2^{-q} <= coupling_budget.
    lag = math.ceil(math.log2((paired_blocks - 1) / float(coupling_budget)))
    actual_coupling = F(paired_blocks - 1, 2**lag)
    actual_bias = 2 * (1 + theta) * raw_coordinate_bound**2 / (2**lag)
    bias_envelope = conservative_bias(paired_blocks)
    assert lag == 23
    assert actual_coupling <= coupling_budget
    assert actual_bias <= bias_envelope
    horizon = 1 + (2 * paired_blocks - 1) * lag
    assert horizon == 2308120
    return {
        "theta": str(theta),
        "population_margin": str(margin),
        "filter_count": filter_count,
        "confidence_alpha": alpha,
        "miss_probability": miss_probability,
        "coupling_budget": str(coupling_budget),
        "mixing_envelope": "beta_mix(q) <= 2^(-q)",
        "integer_paired_blocks_sufficient": paired_blocks,
        "retained_readouts": 2 * paired_blocks,
        "certified_lag": lag,
        "actual_coupling_failure_bound": str(actual_coupling),
        "actual_lag_bias_bound": str(actual_bias),
        "conservative_lag_bias_envelope": str(bias_envelope),
        "trajectory_horizon": horizon,
        "strict_sample_threshold_at_integer_n": threshold(paired_blocks),
    }


def main() -> None:
    payload = {
        "schema": "paper16-statistical-gap-boundary-v4",
        "upper_visibility_fixture": exact_upper_fixture(),
        "lower_near_critical_fixture": exact_lower_fixture(),
        "bounded_unknown_mean_fixture": bounded_unknown_mean_fixture(),
        "dependent_mixing_fixture": dependent_mixing_fixture(),
        "status": "PASS",
    }
    output = Path(__file__).with_name("statistical_boundary_certificate.json")
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("statistical gap boundary certificate: PASS")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

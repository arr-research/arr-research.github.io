"""Conservative closed constants for the logistic finite-sample corollary.

The formulas are direct majorants of Theorem 7.1 after putting
    s = d + log(12/delta),  x = sqrt(r*s/n),  y = r*s/n.
They are intentionally conservative and are recorded so that the phrase
"computable constant" can be replaced by an auditable number.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import ceil, exp, gamma, log, pi, sqrt

from scipy.special import polygamma


PHI0 = 1.0 / sqrt(2.0 * pi)
LOG9 = log(9.0)
CQ = 1.0 + sqrt(2.0)


@dataclass(frozen=True)
class SampleConstants:
    p: float
    radius_threshold: float
    a_t: float
    b_t: float
    a_r: float
    b_r: float
    a_q: float
    b_q: float
    c_p_raw: float
    c_p: int
    c_p_angle: float


def moments(p: float) -> tuple[float, float, float]:
    m0 = gamma(p) ** 2 / gamma(2.0 * p)
    psi1 = float(polygamma(1, p))
    psi3 = float(polygamma(3, p))
    m2 = 2.0 * psi1 * m0
    m4 = (12.0 * psi1**2 + 2.0 * psi3) * m0
    return m0, m2, m4


def constants(p: float) -> SampleConstants:
    if p <= 0.0:
        raise ValueError("p must be positive")
    m0, m2, m4 = moments(p)
    a0 = PHI0 * m0 / 2.0
    b0 = PHI0 * m2 / 2.0
    h = 4.0 ** (-p)
    k1 = exp(-2.0) / p**2
    k2 = 4.0 * exp(-2.0) / p**2
    g0 = PHI0 / p
    g1 = PHI0 / (2.0 * p**3)
    g2 = 3.0 * PHI0 / (2.0 * p**5)

    # e_T/alpha <= a_t*x + b_t*y.  The mixed x^(3/2) term is
    # absorbed into x because the displayed sample condition makes x <= 1.
    a_t = (
        sqrt(2.0 * g0)
        + 4.0 * sqrt(g0 * LOG9)
        + 4.0 * sqrt(h) * (2.0 * g0) ** 0.25 * sqrt(LOG9)
    ) / a0
    b_t = (h / 3.0 + 4.0 * h * sqrt(LOG9 / 3.0) + 4.0 * h * LOG9) / a0

    # e_R/beta <= a_r*x + b_r*y.
    a_r = sqrt(2.0 * g2) / b0
    b_r = k2 / (3.0 * b0)

    # q_n/sqrt(alpha*beta) <= a_q*x + b_q*y.
    root_ab = sqrt(a0 * b0)
    a_q = CQ * (sqrt(g1) + (2.0 * k1 * g1) ** 0.25) / root_ab
    b_q = CQ * sqrt(k1 / 3.0) / root_ab

    a = max(a_t, a_r) + a_q
    b = max(b_t, b_r) + b_q
    a_gap = 2.0 * a_t + 2.0 * a_r / 3.0
    b_gap = 2.0 * b_t + 2.0 * b_r / 3.0
    c_raw = max(1.0, 4.0 * a**2, b, 4.0 * a_gap**2, b_gap)

    # Under the quantitative gap, q_n/G is bounded by the two terms in
    # Corollary 7.2.  Taking the larger coefficient gives one common constant.
    c_angle_1 = 2.0 * CQ * (sqrt(g1) + (2.0 * k1 * g1) ** 0.25) / a0
    c_angle_2 = 2.0 * CQ * sqrt(k1 / 3.0) / a0

    return SampleConstants(
        p=p,
        radius_threshold=sqrt(max(3.0 * m2 / m0, m4 / m2)),
        a_t=a_t,
        b_t=b_t,
        a_r=a_r,
        b_r=b_r,
        a_q=a_q,
        b_q=b_q,
        c_p_raw=c_raw,
        c_p=ceil(c_raw),
        c_p_angle=max(c_angle_1, c_angle_2),
    )


def main() -> None:
    for p in (1.0, 2.0):
        print(asdict(constants(p)))


if __name__ == "__main__":
    main()

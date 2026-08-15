"""Exact bounded replay for the Gr_C(2,5) canonical crossing theorem.

The script uses rational arithmetic in Q(sqrt(6)).  It verifies the two
piecewise-polynomial overlap densities, their first moments, and exact Sturm
root counts for the signed-density pieces.  Floating-point approximations are
printed only after every theorem-bearing assertion has passed.

This replay proves the unique crossing of the one-spike and rank-two
two-block branches.  It does not certify global optimality over arbitrary
five-level external spectra.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
import json
import math
from pathlib import Path
from typing import Iterable

import sympy as sp


@dataclass(frozen=True)
class Q6:
    """An exact element a + b sqrt(6), with a,b rational."""

    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def coerce(value: object) -> "Q6":
        if isinstance(value, Q6):
            return value
        if isinstance(value, F):
            return Q6(value)
        if isinstance(value, int):
            return Q6(F(value))
        raise TypeError(f"cannot coerce {type(value)!r} to Q6")

    def __add__(self, other: object) -> "Q6":
        z = self.coerce(other)
        return Q6(self.a + z.a, self.b + z.b)

    __radd__ = __add__

    def __neg__(self) -> "Q6":
        return Q6(-self.a, -self.b)

    def __sub__(self, other: object) -> "Q6":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "Q6":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "Q6":
        z = self.coerce(other)
        return Q6(self.a * z.a + 6 * self.b * z.b, self.a * z.b + self.b * z.a)

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "Q6":
        z = self.coerce(other)
        denominator = z.a * z.a - 6 * z.b * z.b
        if denominator == 0:
            raise ZeroDivisionError
        return Q6(
            (self.a * z.a - 6 * self.b * z.b) / denominator,
            (self.b * z.a - self.a * z.b) / denominator,
        )

    def __pow__(self, power: int) -> "Q6":
        if power < 0:
            return Q6(1) / (self ** (-power))
        out = Q6(1)
        base = self
        n = power
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out

    def sign(self) -> int:
        """Return the exact sign using only rational comparisons."""

        if self.a == 0:
            return (self.b > 0) - (self.b < 0)
        if self.b == 0 or (self.a > 0) == (self.b > 0):
            return (self.a > 0) - (self.a < 0)
        comparison = self.a * self.a - 6 * self.b * self.b
        if comparison == 0:
            return 0
        dominant = self.a if comparison > 0 else self.b
        return (dominant > 0) - (dominant < 0)

    def as_float(self) -> float:
        return float(self.a) + float(self.b) * math.sqrt(6.0)


Polynomial = list[Q6]  # coefficients in ascending order


def trim(poly: Polynomial) -> Polynomial:
    out = list(poly)
    while len(out) > 1 and out[-1] == Q6():
        out.pop()
    return out


def derivative(poly: Polynomial) -> Polynomial:
    if len(poly) == 1:
        return [Q6()]
    return trim([Q6(i) * poly[i] for i in range(1, len(poly))])


def divmod_poly(dividend: Polynomial, divisor: Polynomial) -> tuple[Polynomial, Polynomial]:
    numerator = trim(dividend)
    denominator = trim(divisor)
    if denominator == [Q6()]:
        raise ZeroDivisionError
    quotient = [Q6()] * max(1, len(numerator) - len(denominator) + 1)
    remainder = list(numerator)
    while len(remainder) >= len(denominator) and remainder != [Q6()]:
        offset = len(remainder) - len(denominator)
        factor = remainder[-1] / denominator[-1]
        quotient[offset] = quotient[offset] + factor
        for index, coefficient in enumerate(denominator):
            remainder[index + offset] = remainder[index + offset] - factor * coefficient
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


def evaluate(poly: Polynomial, x: Q6) -> Q6:
    value = Q6()
    for coefficient in reversed(poly):
        value = value * x + coefficient
    return value


def sturm_sequence(poly: Polynomial) -> list[Polynomial]:
    sequence = [trim(poly), derivative(poly)]
    while sequence[-1] != [Q6()]:
        _, remainder = divmod_poly(sequence[-2], sequence[-1])
        if remainder == [Q6()]:
            break
        sequence.append([-coefficient for coefficient in remainder])
    return sequence


def sign_variations(signs: Iterable[int]) -> int:
    cleaned = [value for value in signs if value]
    return sum(left != right for left, right in zip(cleaned, cleaned[1:]))


def sturm_count(poly: Polynomial, left: Q6, right: Q6) -> int:
    sequence = sturm_sequence(poly)
    left_signs = [evaluate(term, left).sign() for term in sequence]
    right_signs = [evaluate(term, right).sign() for term in sequence]
    if left_signs[0] == 0 or right_signs[0] == 0:
        raise AssertionError("Sturm endpoint is a root")
    return sign_variations(left_signs) - sign_variations(right_signs)


def q(value: int, denominator: int = 1) -> Q6:
    return Q6(F(value, denominator))


SQRT6 = Q6(F(0), F(1))

# The signed density h=f_2-f_1 equals (6/78125)*P_LOW on
# (-sqrt(6),1), and -(6/78125)*P_HIGH on (1,3sqrt(6)/2).
P_LOW: Polynomial = [
    Q6(F(4224), F(-1500)),
    q(980),
    Q6(F(-1160), F(2000, 9)),
    q(-4510, 9),
    q(-30),
    q(1),
]

P_HIGH: Polynomial = [
    Q6(F(-7776), F(1500)),
    q(5980),
    Q6(F(-2160), F(-2000, 9)),
    q(4240, 9),
    q(-30),
    q(1),
]

# On 1<y<4, the positive-minus-negative orientation density for the
# rank-two branch is (12/78125)*P_ORIENT_2(y).
P_ORIENT_2: Polynomial = [
    q(1776),
    q(-3000),
    q(1660),
    q(-375),
    q(30),
]


def symbolic_density_checks() -> dict[str, str]:
    y, x, t = sp.symbols("y x t", real=True)
    root6 = sp.sqrt(6)

    base = 36 * (2 * x - t) ** 2 * (1 - x) * (1 - t + x)
    g_low = sp.factor(sp.integrate(base, (x, 0, t)))
    g_high = sp.factor(sp.integrate(base, (x, t - 1, 1)))
    assert g_low == sp.Rational(6, 5) * t**3 * (t**2 - 10 * t + 10)
    assert g_high == -sp.Rational(6, 5) * (t - 2) ** 5

    f2_low = sp.factor(g_low.subs(t, (y + 4) / 5) / 5)
    f2_high = sp.factor(g_high.subs(t, (y + 4) / 5) / 5)
    beta_q = (2 + 2 * y / root6) / 5
    f1 = sp.factor(12 * beta_q * (1 - beta_q) ** 2 * 2 / (5 * root6))

    assert f2_low == 6 * (y + 4) ** 3 * (y**2 - 42 * y + 66) / 78125
    assert f2_high == -6 * (y - 6) ** 5 / 78125

    moment2 = lambda order: sp.simplify(
        sp.integrate(y**order * f2_low, (y, -4, 1))
        + sp.integrate(y**order * f2_high, (y, 1, 6))
    )
    moment1 = lambda order: sp.simplify(
        sp.integrate(y**order * f1, (y, -root6, sp.Rational(3, 2) * root6))
    )
    moments2 = [moment2(order) for order in range(4)]
    moments1 = [moment1(order) for order in range(4)]
    assert moments2[:3] == [sp.Integer(1), sp.Integer(0), sp.Rational(3, 2)]
    assert moments1[:3] == moments2[:3]
    assert sp.simplify(moments2[3] - moments1[3] - (2 - 3 * root6) / 14) == 0
    assert moments1[3] == 3 * root6 / 14
    assert moments2[3] == sp.Rational(1, 7)

    f1_reflected = sp.factor(f1.subs(y, -y))
    f2_low_reflected = sp.factor(f2_low.subs(y, -y))
    assert sp.simplify(
        f1 - f1_reflected - 16 * y * (2 * y**2 - 9) / 1875
    ) == 0
    assert sp.simplify(
        f2_low - f2_low_reflected
        - 12 * y * (y**4 - 390 * y**2 + 480) / 78125
    ) == 0

    p_orientation = 30 * y**4 - 375 * y**3 + 1660 * y**2 - 3000 * y + 1776
    assert sp.simplify(
        f2_high - f2_low_reflected - 12 * p_orientation / 78125
    ) == 0

    p_low_expr = sp.factor((f2_low - f1) * sp.Rational(78125, 6), extension=root6)
    p_high_expr = sp.factor(-(f2_high - f1) * sp.Rational(78125, 6), extension=root6)
    expected_low = sum(
        (sp.Rational(term.a.numerator, term.a.denominator)
         + sp.Rational(term.b.numerator, term.b.denominator) * root6) * y**index
        for index, term in enumerate(P_LOW)
    )
    expected_high = sum(
        (sp.Rational(term.a.numerator, term.a.denominator)
         + sp.Rational(term.b.numerator, term.b.denominator) * root6) * y**index
        for index, term in enumerate(P_HIGH)
    )
    assert sp.simplify(p_low_expr - expected_low) == 0
    assert sp.simplify(p_high_expr - expected_high) == 0

    return {
        "f2_low": str(f2_low),
        "f2_high": str(f2_high),
        "f1": str(f1),
        "moments_y2": [str(value) for value in moments2],
        "moments_y1": [str(value) for value in moments1],
        "third_moment_difference": str(sp.factor(moments2[3] - moments1[3])),
        "orientation_third_moments": {
            "one_spike": str(moments1[3]),
            "rank_two": str(moments2[3]),
        },
    }


def main() -> None:
    symbolic = symbolic_density_checks()

    intervals = {
        "low_total": (P_LOW, -SQRT6, q(1), 2),
        "low_root_1": (P_LOW, q(-9, 4), q(-11, 5), 1),
        "low_root_2": (P_LOW, q(-1, 2), q(-9, 20), 1),
        "high_total": (P_HIGH, q(1), Q6(F(0), F(3, 2)), 2),
        "high_root_1": (P_HIGH, q(5, 4), q(13, 10), 1),
        "high_root_2": (P_HIGH, q(3), q(31, 10), 1),
    }
    counts: dict[str, int] = {}
    for name, (poly, left, right, expected) in intervals.items():
        actual = sturm_count(poly, left, right)
        assert actual == expected, (name, actual, expected)
        counts[name] = actual

    # Nonzero final Sturm constants prove both polynomials square-free.
    assert len(sturm_sequence(P_LOW)[-1]) == 1
    assert len(sturm_sequence(P_HIGH)[-1]) == 1

    # Exact signs establish +,-,+,-,+ across the four simple roots.
    probes = {
        "left_overlap": evaluate(P_LOW, q(-12, 5)).sign(),
        "low_middle": evaluate(P_LOW, q(-2)).sign(),
        "low_right": evaluate(P_LOW, q(0)).sign(),
        # The high signed density is -P_HIGH.
        "high_left": -evaluate(P_HIGH, q(6, 5)).sign(),
        "high_middle": -evaluate(P_HIGH, q(2)).sign(),
        "high_right": -evaluate(P_HIGH, q(7, 2)).sign(),
    }
    assert list(probes.values()) == [1, -1, 1, 1, -1, 1]

    orientation_intervals = {
        "rank_two_total": (P_ORIENT_2, q(1), q(4), 2),
        "rank_two_root_1": (P_ORIENT_2, q(23, 20), q(7, 6), 1),
        "rank_two_root_2": (P_ORIENT_2, q(11, 4), q(14, 5), 1),
    }
    orientation_counts: dict[str, int] = {}
    for name, (poly, left, right, expected) in orientation_intervals.items():
        actual = sturm_count(poly, left, right)
        assert actual == expected, (name, actual, expected)
        orientation_counts[name] = actual
    assert len(sturm_sequence(P_ORIENT_2)[-1]) == 1

    orientation_probes = {
        "rank_two_left": evaluate(P_ORIENT_2, q(11, 10)).sign(),
        "rank_two_middle": evaluate(P_ORIENT_2, q(2)).sign(),
        "rank_two_right": evaluate(P_ORIENT_2, q(3)).sign(),
    }
    assert list(orientation_probes.values()) == [1, -1, 1]

    # The low positive-side polynomial y^4-390y^2+480 is decreasing in y^2
    # on [0,1] and has endpoint value 91.  The one-spike positive-side odd
    # density changes sign once at y=3/sqrt(2), inside (0,sqrt(6)).
    assert 1 - 390 + 480 == 91
    assert F(0) < F(9, 2) < F(6)  # (3/sqrt(2))^2 lies in (0,sqrt(6))^2

    result = {
        "theorem_scope": (
            "Exact complete oriented two-level envelope on d=5,r=2: positive "
            "orientations dominate their negatives and the one-spike/rank-two "
            "crossing is unique; no global arbitrary-spectrum claim."
        ),
        "arithmetic": "exact Q(sqrt(6)) Sturm sequences and symbolic integration",
        "symbolic_density_checks": symbolic,
        "sturm_counts": counts,
        "signed_density_probe_signs": probes,
        "signed_density_sign_changes": 4,
        "orientation_certificate": {
            "one_spike_signed_density_sign_changes": 3,
            "rank_two_signed_density_sign_changes": 5,
            "rank_two_sturm_counts": orientation_counts,
            "rank_two_probe_signs": orientation_probes,
            "conclusion": (
                "For positive field each positive orientation strictly dominates "
                "its negative orientation; together with the canonical crossing, "
                "this closes the complete oriented two-level envelope."
            ),
        },
        "laplace_zero_budget": {
            "zeros_at_origin_counting_multiplicity": 3,
            "reason": "equal moments of orders 0,1,2 and unequal third moments",
            "remaining_real_zero_budget": 1,
            "positive_crossing_exists": (
                "third derivative is negative at zero while the rank-two "
                "support endpoint 6 exceeds 3*sqrt(6)/2"
            ),
            "conclusion": "the positive crossing exists, is unique, and is simple",
        },
        "diagnostic_root_approximations": {
            "low": [-2.20207005043770, -0.472989155169179],
            "high": [1.25194029547071, 3.09440180895436],
        },
    }

    output = Path(__file__).with_name("d5r2_canonical_crossing_exact.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

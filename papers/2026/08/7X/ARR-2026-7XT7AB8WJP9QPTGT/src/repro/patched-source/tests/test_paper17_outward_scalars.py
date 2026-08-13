from __future__ import annotations

import math
from fractions import Fraction

from experiments.theta_pencil.smooth_legendre_series import (
    smooth_kernel_series_remainder_bound,
)


def test_smooth_remainder_binary64_is_an_upper_bound() -> None:
    half_width = Fraction(72, 100)
    maximum_power = 47
    ratio = 2 * half_width / 3
    h_tail = Fraction(2, 3) * ratio ** (maximum_power + 1) / (1 - ratio)
    first_even = maximum_power + 1
    if first_even % 2:
        first_even += 1
    first_term = Fraction(2) * half_width**first_even / math.factorial(first_even)
    next_ratio = half_width**2 / ((first_even + 1) * (first_even + 2))
    exact = 2 * half_width * (h_tail + first_term / (1 - next_ratio))
    exported = smooth_kernel_series_remainder_bound(0.72, maximum_power)
    assert Fraction.from_float(exported) >= exact

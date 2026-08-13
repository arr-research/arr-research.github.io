from __future__ import annotations

import math

from flint import arb, ctx

from experiments.theta_pencil.arb_prime_translation import _arb_radius_as_float


def test_binary64_export_radius_covers_midpoint_rounding() -> None:
    ctx.prec = 256
    values = [
        arb(1) / 3,
        arb(-7) / 11,
        arb("0.1 +/- 1e-50"),
        arb("-2.3 +/- 1e-40"),
        arb(0),
    ]
    for value in values:
        midpoint = float(value.mid())
        radius = _arb_radius_as_float(value)
        exported = arb(str(midpoint))
        enclosure = arb(str(midpoint)) + arb(f"0 +/- {radius!r}")
        assert enclosure.contains(value)
        assert radius >= math.ulp(midpoint)
        assert exported in enclosure

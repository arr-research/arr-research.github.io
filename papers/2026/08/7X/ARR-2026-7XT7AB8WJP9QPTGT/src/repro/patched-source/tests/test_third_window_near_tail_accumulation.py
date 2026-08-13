import numpy as np

from experiments.theta_pencil.arb_third_window_near_tail_gram import (
    build_arb_third_window_near_tail_gram,
)


def test_near_tail_accumulates_target_contributions() -> None:
    """Regression: augmented assignment through a loop variable lost all bands."""

    (band,) = build_arb_third_window_near_tail_gram(
        half_width=0.72,
        edge_degree=1,
        bridge_degree=1,
        center_degree=1,
        first_degree=1,
        last_degree=2,
        precision=128,
        maximum_smooth_power=None,
        band_boundaries=(1, 2),
    )
    assert np.max(np.abs(band.even_midpoint)) > 0.3
    assert np.max(np.abs(band.odd_midpoint)) > 0.3

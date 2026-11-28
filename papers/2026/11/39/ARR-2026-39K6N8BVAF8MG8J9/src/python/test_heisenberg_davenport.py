"""Targeted pytest verification suite for paper-heisenberg-large-davenport."""

import random
import pytest

from verify_heisenberg_davenport import (
    alternating_area,
    build_s1,
    build_s2,
    check_t_eta_and_ts,
    eval_sequence_products,
    exp_to_mat,
    heis_mul,
    heis_word_prod,
    hill_climb_obstruction,
    is_minimal_product_one,
    mat_mul,
    verify_h27_exhaustive,
    verify_lemma1_growth,
)


@pytest.mark.parametrize("p", [3, 5, 7, 11])
def test_exponential_isomorphism_and_area_identity(p: int) -> None:
    rng = random.Random(100 + p)
    for _ in range(20):
        g1 = ((rng.randrange(p), rng.randrange(p)), rng.randrange(p))
        g2 = ((rng.randrange(p), rng.randrange(p)), rng.randrange(p))
        assert exp_to_mat(heis_mul(g1, g2, p), p) == mat_mul(exp_to_mat(g1, p), exp_to_mat(g2, p), p)
        word = [((rng.randrange(p), rng.randrange(p)), rng.randrange(p)) for _ in range(6)]
        prod = heis_word_prod(word, p)
        assert prod == (
            (sum(w[0][0] for w in word) % p, sum(w[0][1] for w in word) % p),
            (sum(w[1] for w in word) + alternating_area([w[0] for w in word], p)) % p,
        )


@pytest.mark.parametrize("p", [3, 5, 7, 11])
def test_extremal_families_s1_s2(p: int) -> None:
    s1, w1 = build_s1(p)
    s2, w2 = build_s2(p)
    assert len(s1) == 3 * p - 1
    assert len(s2) == 3 * p - 1
    assert heis_word_prod(w1, p) == ((0, 0), 0)
    assert heis_word_prod(w2, p) == ((0, 0), 0)
    assert is_minimal_product_one(s1, p)
    assert is_minimal_product_one(s2, p)
    # Non-isomorphism invariant: count central elements
    assert sum(1 for v, _ in s1 if v == (0, 0)) == p - 1
    assert sum(1 for v, _ in s2 if v == (0, 0)) == 0


@pytest.mark.parametrize("p", [3, 5, 7, 11])
def test_fiber_doubled_eta_and_s_bounds(p: int) -> None:
    ok_eta, ok_s = check_t_eta_and_ts(p)
    assert ok_eta and ok_s


@pytest.mark.parametrize("p", [3, 5, 7])
def test_lemma1_order_value_growth(p: int) -> None:
    assert verify_lemma1_growth(p, trials=40, seed=200 + p)


def test_h27_exhaustive_no_length_9_atom() -> None:
    summary = verify_h27_exhaustive()
    assert summary[0][2] == 0
    assert summary[1][2] == 0
    assert summary[2][2] == 0


def test_lemma5_cross_splitting_p5_p7() -> None:
    # Verify Lemma 5 cross-splitting on concrete A_1 (len 2p-1, all x_i != 0) + L on F_p e_2
    for p in [5, 7]:
        # A_1 = (1,0)^(p-1) * (1,1)^(p-1) * (2,1) (sum x_i = (p-1)+2 = 1 mod p, all x_i != 0)
        # L = (0,1)^p with c = p-2 (len 4p-3)
        A1 = [((1, 0), 0)] * (p - 1) + [((1, 1), 1)] * (p - 1) + [((2, 1), 0)]
        L = [((0, 1), 0)] * (p - 1) + [((0, 1), 1)]
        S = A1 + L + [((0, 0), 1)] * (p - 2)
        assert len(S) == 4 * p - 3
        is_p1, splits = eval_sequence_products(S, p, max_states=200_000)
        assert is_p1 and splits >= 1


def test_obstruction_probes_h125_and_h343() -> None:
    atom8 = [(0, 4), (0, 4), (2, 3), (2, 3), (2, 4), (2, 4), (3, 0), (4, 3)]
    assert hill_climb_obstruction(atom8 + [(1, 2)] * 5, c=2, p=5, steps=40, seeds=2) != (0, 0)
    assert hill_climb_obstruction([(1, 0)] * 5 + [(0, 1)] * 5 + [(1, 1)] * 5, c=0, p=5, steps=40, seeds=2) != (0, 0)
    assert hill_climb_obstruction([(1, 0)] * 7 + [(0, 1)] * 7 + [(1, 1)] * 7, c=0, p=7, steps=30, seeds=2) != (0, 0)

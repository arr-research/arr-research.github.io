"""Pytest suite for split-graph pebbling verification."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "code"))

import verify_split_pebbling as vsp


def test_split_graph_atlas_counts():
    splits = vsp.enumerate_connected_split_graphs(7)
    assert len(splits) == 164
    counts = {}
    for G in splits:
        n = G.number_of_nodes()
        counts[n] = counts.get(n, 0) + 1
    assert counts == {1: 1, 2: 1, 3: 2, 4: 5, 5: 12, 6: 35, 7: 108}


def test_intra_clique_elimination_lemma_n6():
    res = vsp.verify_intra_clique_lemma_n6()
    assert res["non_complete_n6_count"] == 34
    assert res["instances_cross_checked"] == 612


def test_exhaustive_2pp_and_t_pebbling_n_le_7():
    res = vsp.verify_all_splits_up_to_7()
    assert res["total_splits_n_le_7"] == 164


def test_extremal_families_and_G8_G44():
    res = vsp.verify_extremal_families()
    assert res["G8"]["pi_by_t"] == {1: 8, 2: 16, 3: 24}
    assert res["G44"]["pi_by_t"] == {1: 10, 2: 16, 3: 24}
    assert res["K3_leaf_box_K2_pi"] == 9

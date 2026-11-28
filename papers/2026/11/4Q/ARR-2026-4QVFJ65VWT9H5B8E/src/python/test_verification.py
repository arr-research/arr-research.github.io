"""Pytest suite exercising the exact rational verifier across Theorems 1-3."""

from fractions import Fraction
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))

import verify_quantum_entropic_metrics as vq


@pytest.fixture(scope="module")
def theorem_2_data():
    return vq.verify_theorem_2_and_qfail()


def test_cb4_plus_triangle_violation():
    res = vq.verify_cb4_plus()
    assert Fraction(res["S_cond_min"]) >= 0
    assert res["dQ"]["0-1"] == "0"
    assert res["dQ"]["1-2"] == "0"
    assert res["dQ"]["0-2"] == "1"


def test_theorem_1_n6_hierarchy():
    t1 = vq.verify_theorem_1()
    assert t1["K23_CB5_plus_min_cond"] == "0"
    assert t1["K23_CB5_plus_singletons"] == ["3/2", "1/2", "3/2", "5/2", "3/2"]
    assert t1["MET6_rays"] == 296
    assert t1["MET6_orbits"] == 8
    assert len(t1["CB6_plus_orbits"]) == 8
    assert len(t1["D4_K33e_proof"]) == 10
    assert t1["K33e_primal_h_verified"] is True
    assert t1["K33e_primal_num_ineqs"] == 246
    assert set(t1["K33e_primal_d"]) == {"9/8", "2", "3"}
    assert t1["POLY6_rays"] == 1736
    assert len(t1["POLY6_orbits"]) == 12
    assert t1["POLY6_orbits"][8]["kappa_POLY_ZY"] == "31/30"
    assert t1["POLY6_orbits"][8]["in_CB6_plus"] is True
    assert t1["n6_graphs_total"] == 112
    assert len(t1["n6_graphs_fail_POLY"]) == 2


def test_theorem_2_segre_and_n7_graphs(theorem_2_data):
    t2 = theorem_2_data
    assert [s["m"] for s in t2["segre_quadrics"]] == [3, 4, 6, 8]
    assert t2["n7_total"] == 853
    assert t2["n7_fail_POLY"] == 38
    assert t2["n7_fail_CB"] == 128
    assert t2["n7_fail_both_POLY_CB"] == 16
    assert t2["n7_rem_count"] == 14
    assert t2["rem_ghz_spread_realized_count"] == 6
    assert t2["rem_ghz_spread_separated_count"] == 8
    assert t2["sep0"]["name"] == "G550"
    assert t2["sep0"]["kappa_POLY"] == "9/8"
    assert t2["sep0"]["kappa_CB"] == "8/7"
    assert t2["sep0"]["kappa_Q"] == "1"
    rem4 = t2["rem4"]
    assert rem4["name"] == "G800"
    assert rem4["kappa_POLY"] == "17/16"
    assert rem4["kappa_CB"] == "13/12"
    assert rem4["kappa_CB_plus"] == "13/12"
    assert rem4["F4_value"] == -1
    assert rem4["min_F4_126_cuts"] == 0
    assert rem4["min_F4_21_bells"] == 0
    assert rem4["quantum_realization"]["verified_21_distances"] is True
    assert Fraction(rem4["quantum_realization"]["min_conditional_entropy"]) >= 0


def test_theorem_3_qfail_and_staircase(theorem_2_data):
    t2 = theorem_2_data
    qfail_map = {q["name"]: q for q in t2["n7_fail_Q"]}
    assert set(qfail_map.keys()) == {"G708", "G873"}
    assert qfail_map["G708"]["kappa_Q"] == "21/20"
    assert qfail_map["G708"]["pure_primal_verified"] is True
    assert qfail_map["G708"]["num_ineq_checked"] == 896
    assert len(qfail_map["G708"]["pure_primal_orbits"]) == 26
    assert qfail_map["G873"]["kappa_Q"] == "41/40"
    assert qfail_map["G873"]["pure_primal_verified"] is True
    assert qfail_map["G873"]["num_ineq_checked"] == 896
    assert len(qfail_map["G873"]["pure_primal_orbits"]) == 26

    t3 = vq.verify_theorem_3_staircase()
    rows = {r["m"]: r for r in t3["staircase"]}
    assert rows[5]["kappa_CUT"] == "4/3"
    assert rows[5]["kappa_POLY"] == "9/8"
    assert rows[5]["kappa_Q"] == "12/11"
    assert rows[6]["kappa_Q"] == "9/8"
    assert rows[16]["kappa_POLY"] == "26833/23520"
    assert rows[16]["kappa_Q"] == "26833/23520"
    assert rows[17]["kappa_POLY"] == "735991/645120"
    assert rows[17]["kappa_Q"] == "81649/71568"

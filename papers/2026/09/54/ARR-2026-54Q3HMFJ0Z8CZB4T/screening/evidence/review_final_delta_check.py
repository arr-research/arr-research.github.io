"""Independent finite checks for the new contact theorem.

Uses the prior reviewer's explicit geometry and LR tableaux, not the deriving
agent's geometry module or recursive Horn implementation. No LP is run.
"""
from fractions import Fraction as F
from itertools import product
from math import lcm
from pathlib import Path
import hashlib
import json
import time
import independent_lr_geometry_review as independent

HERE = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
EXPECTED_HELPER = "f4208f5f36304501932c0e1a788b4c9c3a404222185ed42562d72d6c62b75356"

def simplex(a):
    return len(a) == 4 and sum(a) == 1 and min(a) >= 0 and tuple(sorted(a, reverse=True)) == a

def coordinate_cell(a, r):
    return a[r-1] >= F(1,4) >= a[r]

def q(a):
    return 2*(1-a[0]) - sum(abs(x-F(1,4)) for x in a)

def distance(a,b):
    ea, eb = 2*(1-a[0]), 2*(1-b[0])
    ua, ub = sum(abs(x-F(1,4)) for x in a), sum(abs(x-F(1,4)) for x in b)
    return min(ea+ub,ua+eb)

def main():
    started = time.monotonic()
    assert sha(HERE / "independent_lr_geometry_review.py") == EXPECTED_HELPER
    base, edges, vertices, cuts = independent.explicit_geometry(4)
    assert len(vertices) == 89
    triples, counts, histogram = independent.lr_triples(8)
    assert len(triples) == len(set(triples)) == 8752
    proposed = json.loads((HERE / "optimal_constant_N4_d8.json").read_text(encoding="utf-8"))
    witnesses = {}
    for row in proposed["certificates"]:
        a,b,s = [tuple(map(F,row[k])) for k in ("a","b","common_spectrum")]
        assert simplex(a) and simplex(b)
        assert len(s) == 8 and min(s) >= 0 and tuple(sorted(s,reverse=True)) == s
        assert (a,b) not in witnesses
        witnesses[a,b] = s
        witnesses[b,a] = s
    assert set(witnesses) == vertices
    checks = 0
    def verify(a,b,s):
        nonlocal checks
        assert simplex(a) and simplex(b)
        assert len(s) == 8 and min(s) >= 0 and tuple(sorted(s,reverse=True)) == s
        lam = a + tuple(-x for x in reversed(b))
        assert sum(lam) == 0
        den = lcm(*(v.denominator for v in s+lam))
        si, li = [int(v*den) for v in s], [int(v*den) for v in lam]
        for I,J,K in triples:
            assert sum(si[i-1] for i in I) - sum(si[8-j] for j in J) >= sum(li[k-1] for k in K)
            checks += 1
        gap = F(5,2) - sum(s) - F(4,7)*distance(a,b)
        assert gap >= 0
        return gap
    slacks = {pair:verify(*pair,s) for pair,s in witnesses.items()}
    zero = {pair for pair,gap in slacks.items() if gap == 0}
    e = (F(1),F(0),F(0),F(0))
    u = (F(1,4),)*4
    A = (F(5,8),F(1,8),F(1,8),F(1,8))
    B = (F(1,2),F(1,2),F(0),F(0))
    assert zero == {(e,u),(u,e),(A,B),(B,A)}
    assert [q(x) for x in (e,u,A,B)] == [F(-3,2),F(3,2),0,0]
    incidence = {name:[r for r in (1,2,3) if coordinate_cell(a,r)]
                 for name,a in {"e":e,"u":u,"A":A,"B":B}.items()}
    assert incidence == {"e":[1],"u":[1,2,3],"A":[1],"B":[2]}
    cell_contacts = []
    candidates = set()
    histogram = {0:0,1:0,2:0}
    for r,s,orientation in product((1,2,3),(1,2,3),(-1,1)):
        contact = tuple(sorted(pair for pair in zero
                        if coordinate_cell(pair[0],r) and coordinate_cell(pair[1],s)
                        and orientation*(q(pair[0])-q(pair[1])) >= 0))
        assert len(contact) <= 2
        histogram[len(contact)] += 1
        cell_contacts.append({"r":r,"s":s,"orientation":orientation,"contacts":contact})
        if len(contact) == 2:
            candidates.add(contact)
    assert candidates == {tuple(sorted(((e,u),(A,B)))), tuple(sorted(((u,e),(B,A))))}
    a = tuple((x+y)/2 for x,y in zip(e,A))
    b = tuple((x+y)/2 for x,y in zip(u,B))
    s = tuple(map(F,["13/16","7/16","1/8","1/8","1/16","0","0","0"]))
    midpoint = json.loads((HERE / "contact_midpoint.json").read_text(encoding="utf-8"))
    assert (a,b,s) == tuple(tuple(map(F,midpoint[k])) for k in ("a","b","s"))
    assert sum(s) == F(25,16) and distance(a,b) == F(7,8)
    assert verify(a,b,s) == F(7,16)
    assert checks == 787680
    result = {
        "status":"PASS",
        "elapsed_seconds":time.monotonic()-started,
        "method":"Independent explicit geometry and LR-tableau Horn enumeration, no author geometry/Horn import and no LP execution.",
        "vertices":len(vertices),"LR_triples":len(triples),"LR_counts":counts,
        "exact_Horn_checks":checks,
        "zero_witness_slack_vertices":sorted(zero),
        "strict_positive_vertex_count":sum(v>0 for v in slacks.values()),
        "minimum_positive_vertex_slack":min(v for v in slacks.values() if v>0),
        "vertex_slacks":[{"a":a,"b":b,"certified_gap_lower":gap} for (a,b),gap in sorted(slacks.items())],
        "one_factor_contact_incidence":incidence,
        "cell_contact_count_histogram":histogram,
        "cell_contacts":cell_contacts,
        "candidate_segments":sorted(candidates),
        "midpoint":{"a":a,"b":b,"s":s,"cost_upper":sum(s),
                    "distance":distance(a,b),"gap_lower":F(7,16)},
        "source_hashes":{p.name:sha(p) for p in [
            HERE/"paper.md",Path(__file__),HERE/"independent_lr_geometry_review.py",
            HERE/"optimal_constant_N4_d8.json",HERE/"contact_midpoint.json"]},
        "limits":[
            "Positive witness slack is a lower bound for the true gap, not a claim that a vertex LP optimum was recomputed.",
            "Zero gap at four vertices uses the manuscript's separate exact lower bounds.",
            "Concavity, hull reduction, and all-dimensional preservation require the written analytic argument.",
            "Classical Horn sufficiency imported; no formalization or human peer review.",
        ],
    }
    (HERE/"review_final_delta_check.json").write_text(json.dumps(result,default=str,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("status","vertices","LR_triples","exact_Horn_checks","strict_positive_vertex_count","minimum_positive_vertex_slack","cell_contact_count_histogram","midpoint")},default=str,indent=2))

if __name__ == "__main__":
    main()

# SPDX-License-Identifier: Apache-2.0
"""Exact replay for the sharp inertia-dependent inverse self-commutator bound.

Python 3.10+, standard library only. This checks explicit finite witnesses and
the algebraic decomposition; the all-dimensional proof is in the manuscript.
It does not implement or formally prove the Horn theorem.
"""
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
import argparse
import hashlib
import json
import random


def require(condition, message):
    if not condition:
        raise ValueError(message)


def flat_witness(k, l, ambient=None):
    """Squared singular values /2, and actual diagonal R,S with R-S=E_kl."""
    require(k >= 1 and l >= 1, "positive multiplicities required")
    d = ambient or k + l
    require(d >= k + l, "ambient too small")
    g = gcd(k, l)
    length = (k + l) // g
    unit = Q(g, k * l)
    residues = [j * (l // g) % length for j in range(length)] + [0]
    require(sorted(residues[:-1]) == list(range(length)), "not a full orbit")
    partial = [unit * x for x in residues]
    # For each shift C e_(j+1) = sqrt(2 partial[j]) e_j, R=CC*/2,S=C*C/2.
    R = partial[1:] * g + [Q(0)] * (d - k - l)
    S = partial[:-1] * g + [Q(0)] * (d - k - l)
    delta = [a - b for a, b in zip(R, S)]
    expected = [Q(1, k)] * k + [Q(-1, l)] * l + [Q(0)] * (d-k-l)
    require(sorted(delta) == sorted(expected), "wrong self-commutator")
    require(sorted(R) == sorted(S), "positive matrices not isospectral")
    require(min(R + S) >= 0, "negative squared weight")
    cost = Q((k + l) * (k + l - g), 2 * k * l)
    require(sum(R) == cost, "wrong cost formula")
    ceiling = Q(max(k, l) + 1, 2)
    require(cost == ceiling if min(k, l) == 1 else cost < ceiling,
            "arithmetic comparison failed")
    return {
        "k": k, "l": l, "ambient": d, "gcd": g,
        "R": R, "S": S, "lambda": sorted(delta, reverse=True),
        "s": sorted(R, reverse=True), "cost": cost,
    }


def decompose(positive, negative, zeros=0):
    a, b = sorted(map(Q, positive), reverse=True), sorted(map(Q, negative), reverse=True)
    require(a and b and min(a + b) > 0, "use strictly positive magnitudes")
    P = sum(a)
    require(P == sum(b), "target not traceless")
    a, b = [v/P for v in a], [v/P for v in b]
    m, n = len(a), len(b)
    d = m + n + zeros
    require(zeros >= 0, "negative zero multiplicity")
    alpha = [(i+1)*(a[i]-(a[i+1] if i+1<m else 0)) for i in range(m)]
    beta = [(j+1)*(b[j]-(b[j+1] if j+1<n else 0)) for j in range(n)]
    require(sum(alpha) == sum(beta) == 1, "barycentric sum failed")
    require(min(alpha + beta) >= 0, "negative coefficient")
    lam, s = [Q(0)]*d, [Q(0)]*d
    cost = Q(0)
    terms = []
    for i, ai in enumerate(alpha, 1):
        for j, bj in enumerate(beta, 1):
            weight = ai*bj
            if not weight:
                continue
            w = flat_witness(i, j, d)
            for h in range(d):
                lam[h] += weight*w["lambda"][h]
                s[h] += weight*w["s"][h]
            cost += weight*w["cost"]
            terms.append({"k": i, "l": j, "weight": weight, "cost": w["cost"]})
    target = a + [Q(0)]*zeros + [-x for x in reversed(b)]
    require(lam == target, "spectral reconstruction failed")
    require(s == sorted(s, reverse=True) and min(s)>=0, "unordered singular certificate")
    require(sum(s) == cost, "cost reconstruction failed")
    ceiling = Q(max(m,n)+1, 2)
    require(cost <= ceiling, "ceiling failed")
    if min(m,n)>=2:
        require(cost < ceiling, "strictness failed")
        gap = alpha[-1]*beta[-1]*(ceiling-flat_witness(m,n)["cost"])
        require(ceiling-cost >= gap > 0, "explicit gap failed")
    return {
        "positive_mass": P, "inertia": [m,n,zeros],
        "lambda_normalized": lam, "alpha": alpha, "beta": beta,
        "horn_feasible_s_over_mass": s, "cost_upper_over_mass": cost,
        "sharp_inertia_ceiling": ceiling, "terms": terms,
        "interpretation": "Horn feasibility follows analytically from convexity of the spectral-sum cone. This program verifies every flat matrix witness and their exact convex coefficients; it does not prove the imported theorem."
    }


def stability_replay(n, mass=Q(1), eps=Q(1,1000)):
    require(n>=2, "need n>=2")
    # Two-level deviations: sharp lower Gini/mean-deviation constant.
    k=max(1,n//2)
    y=[eps/k]*k+[-eps/(n-k)]*(n-k)
    b=[mass/n+t for t in y]
    require(min(b)>0, "nonpositive test spectrum")
    cost=sum((j+1)*v for j,v in enumerate(b))
    D=Q(n+1,2)*mass-cost
    L=sum(abs(v-mass/n) for v in b)
    gini=sum(b[i]-b[j] for i in range(n) for j in range(i+1,n))/2
    require(D==gini==Q(n,4)*L, "sharp lower constant failed")
    # Endpoint-only deviation: sharp upper constant.
    b=[mass/n]*n
    b[0]+=eps
    b[-1]-=eps
    D=Q(n+1,2)*mass-sum((j+1)*v for j,v in enumerate(b))
    L=sum(abs(v-mass/n) for v in b)
    require(D==Q(n-1,2)*L, "sharp upper constant failed")


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--max-multiplicity", type=int, default=32)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1]/"certificates"/"commutator_inertia.json")
    args=parser.parse_args()
    require(2<=args.max_multiplicity<=256, "replay bound must be 2..256")
    count=0
    for k in range(1,args.max_multiplicity+1):
        for l in range(1,args.max_multiplicity+1):
            flat_witness(k,l,k+l+3)
            count+=1
    rng=random.Random(20260905)
    examples=[]
    for m in range(1,9):
        for n in range(1,9):
            ai=[Q(rng.randrange(1,100)) for _ in range(m)]
            bi=[Q(rng.randrange(1,100)) for _ in range(n)]
            A,B=sum(ai),sum(bi)
            examples.append(decompose([v/A for v in ai],[v/B for v in bi],2))
    for n in range(2,args.max_multiplicity+1):
        stability_replay(n)
    # Preserve the non-convex-matrix warning as exact arithmetic:
    # kappa(1,-1,0)=1 each, kappa(2,-1,-1)=1+2=3.
    require(Q(3)>Q(1)+Q(1), "global convexity warning malformed")
    report={
        "status":"PASS",
        "arithmetic":"fractions.Fraction, no floating-point proof objects",
        "flat_witnesses_checked":count,
        "random_rational_decompositions_checked":len(examples),
        "stability_dimensions_checked":args.max_multiplicity-1,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "selected_certificates":[examples[9],examples[23],examples[-1]],
        "limitations":[
            "Finite exact replay supports the stated constructions and indexing; all-dimensional validity is proved in the manuscript.",
            "The Horn-Klyachko theorem is imported, not implemented or Lean-checked.",
            "The supplied singular spectrum is feasible; its cost is not claimed optimal for arbitrary input."
        ]
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,default=str)+"\n",encoding="utf-8")
    print(json.dumps({k:report[k] for k in ["status","flat_witnesses_checked",
        "random_rational_decompositions_checked","stability_dimensions_checked"]}))


if __name__=="__main__":
    main()

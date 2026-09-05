"""Exact finite replay for sharp_stability.md; analytic proofs cover all dimensions.

Python 3.10+ and SymPy. No LP solver, floating arithmetic or network is used.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
from math import gcd
from pathlib import Path
import hashlib
import json
import sympy as sp


def cost(k, l):
    return Q((k+l)*(k+l-gcd(k,l)), 2*k*l)


@lru_cache(None)
def horn_triples(r, d):
    """Horn's recursive finite index definition, independent of an LP solver."""
    subsets = tuple(combinations(range(1, d+1), r))
    by_sum = {}
    for K in subsets:
        by_sum.setdefault(sum(K), []).append(K)
    lower = tuple((p, horn_triples(p, r)) for p in range(1, r))
    out = []
    for I, J in product(subsets, repeat=2):
        for K in by_sum.get(sum(I)+sum(J)-r*(r+1)//2, ()):
            if all(sum(I[f-1] for f in F)+sum(J[g-1] for g in G)
                   <= sum(K[h-1] for h in H)+p*(p+1)//2
                   for p, ts in lower for F, G, H in ts):
                out.append((I, J, K))
    return tuple(out)


def main():
    counts = {}
    k, l, n = sp.symbols('k l n', positive=True)
    B = k*k*l-2*k*k*n+k*k-k*l*n+k*l+k*n+l*n
    lhs = 2*(2-1/k-1/n)*((n+1)/2-(k+l)*(k+l-1)/(2*k*l)) \
          -(n-k)*(2-1/k-l/n)
    rhs = -(k-1)*(l-1)*B/(k*k*l*n)
    assert sp.factor(lhs-rhs) == 0
    assert sp.expand(B.subs(l, 1)+(2*k*k-1)*(n-1)-k-1) == 0
    assert sp.expand(B.subs(l, n)+(k+n)*(k*n-k-n)) == 0
    counts['symbolic_polynomial_identities'] = 3

    cells = strata = 0
    for n in range(2, 65):
        H = Q(n+1, 2)
        prefix_max = Q(0)
        for k in range(1, n):
            Ckn = 4*(2-Q(1,k)-Q(1,n))/(n-k)
            for l in range(1, n+1):
                h = H-cost(k,l)
                dist = 2*(2-Q(1,k)-Q(l,n))
                assert h >= 0 and dist <= Ckn*h
                if h:
                    prefix_max = max(prefix_max, dist/h)
                else:
                    assert (k,l) == (1,n) and dist == 0
                cells += 1
            # The prefix now contains all atom cells for inertia (k,n).
            assert prefix_max == Ckn
            assert 2*(2-Q(1,k)-Q(1,n))/(H-Q(k+1,2)) == Ckn
            strata += 1
    counts['atom_cells'] = cells
    counts['complete_unbalanced_atom_maxima'] = strata

    families = 0
    for n in range(2, 65):
        H = Q(n+1, 2)
        Gcost = Q(1,n)+Q(n-1,2)
        for q in range(1, 9):
            eps = Q(1,n*q)
            interpolate = (1-n*eps)*H+n*eps*Gcost
            moment = sum(Q(j,n) for j in range(1,n+1))
            horn_weyl_lower = moment-(n-1)*eps
            assert interpolate == horn_weyl_lower == H-(n-1)*eps
            assert (H-interpolate)/(2*eps) == Q(n-1,2)
            # Perturbation-independent identities for the opposite boundary.
            b = [Q(1,n)]*n
            t = Q(1,2*n*q)
            b[0] += t
            b[-1] -= t
            delta = H-sum((j+1)*v for j,v in enumerate(b))
            assert delta == (n-1)*t
            assert sum(abs(v-Q(1,n)) for v in b) == 2*t
            families += 1
    counts['sharpness_interpolation_and_gini_fixtures'] = families

    lam = (Q(3,4),Q(1,4),-Q(1,6),-Q(5,12),-Q(5,12))
    s = (Q(3,4),Q(5,12),Q(1,6),Q(0),Q(0))
    minus_s = tuple(-v for v in reversed(s))
    assert sum(lam) == 0 and sum(s)+sum(minus_s) == 0
    assert all(s[i]>=s[i+1]>=0 for i in range(4))
    assert all(lam[i]>=lam[i+1] for i in range(4))
    rows = []
    for r in range(1,5):
        for I,J,K in horn_triples(r,5):
            slack = sum(s[i-1] for i in I)+sum(minus_s[j-1] for j in J) \
                    -sum(lam[k-1] for k in K)
            assert slack >= 0
            rows.append({'I':I,'J':J,'K':K,'slack':str(slack)})
    assert len(rows) == 142
    lower = max(Q(3,4),Q(5,12))+max(Q(1,4),Q(5,12))+Q(1,6)
    assert sum(s) == lower == Q(4,3)
    counts['exact_dimension_five_horn_inequalities'] = len(rows)

    alpha = (Q(1,2),Q(1,2))
    beta = (Q(0),Q(1,2),Q(1,2))
    pi = ((Q(0),Q(0),Q(1,2)),(Q(0),Q(1,2),Q(0)))
    u = (Q(0),-Q(1,2))
    v = (Q(1),Q(3,2),Q(2))
    assert tuple(sum(row) for row in pi) == alpha
    assert tuple(sum(pi[k][l] for k in range(2)) for l in range(3)) == beta
    assert all(u[k]+v[l]<=cost(k+1,l+1) for k in range(2) for l in range(3))
    primal = sum(pi[k][l]*cost(k+1,l+1) for k in range(2) for l in range(3))
    dual = sum(alpha[k]*u[k] for k in range(2))+sum(beta[l]*v[l] for l in range(3))
    product_cost = sum(alpha[k]*beta[l]*cost(k+1,l+1) for k in range(2) for l in range(3))
    assert primal == dual == Q(3,2) and product_cost == Q(37,24)
    assert primal-lower == Q(1,6) and (primal-lower)/lower == Q(1,8)
    counts['transport_primal_dual_examples'] = 1

    source = Path(__file__)
    result = {
        'status':'PASS',
        'arithmetic':'Fraction rational arithmetic and SymPy polynomial identities',
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'counts':counts,
        'ranges':{'largest_negative_inertia':64,'epsilon_denominator_multipliers':[1,8]},
        'benchmark':{'lambda':list(map(str,lam)),'common_spectrum':list(map(str,s)),
                     'lower':str(lower),'horn_upper':str(sum(s)),
                     'transport':str(primal),'product':str(product_cost)},
        'horn_rows':rows,
        'limitations':[
            'Finite integer grids do not prove all-dimensional inequalities; see the analytic proof.',
            'Horn sufficiency is imported; this verifier checks its finite hypotheses, not the theorem.',
            'Sharpness uses analytic continuity and interpolation, not numerical sampling.',
            'No formal proof assistant or external peer review is claimed.'
        ]
    }
    out = source.with_name('sharp_stability_certificate.json')
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='horn_rows'},indent=2))


if __name__ == '__main__':
    main()

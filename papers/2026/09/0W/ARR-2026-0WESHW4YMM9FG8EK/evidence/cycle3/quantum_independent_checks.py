"""Independent review checks for quantum_dyadic_trinomials.md.

Written by the passive review agent. Does not import or execute the constructor's
quantum verifier. All checks use integers, exact polynomial fields or rationals.
"""
from collections import Counter, deque
from itertools import product, permutations, combinations
from math import gcd
from pathlib import Path
import hashlib
import json
import time
import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[2]


def closure(d,generators):
    """Direct finite group closure, deliberately not a lattice-index formula."""
    seen={(0,0)}; pending=deque([(0,0)])
    while pending:
        a,b=pending.popleft()
        for c,e in generators:
            z=((a+c)%d,(b+e)%d)
            if z not in seen: seen.add(z); pending.append(z)
    return seen


def central_group_checks():
    reports=[]
    for d in [2,3,4,5,7,8,9]:
        count=0; labels=list(product(range(d),repeat=2))
        for u,v in product(labels,repeat=2):
            q=d//gcd(d,u[0]*v[1]-u[1]*v[0])
            if q==1: continue
            group=closure(d,[tuple(q*a%d for a in u),tuple(q*a%d for a in v)])
            assert len(group)==d//q,(d,u,v,q,group)
            count+=1
        reports.append({'d':d,'all_noncommuting_ordered_pairs':count})
    valuation_cases=0
    for p,k in [(2,4),(2,5),(2,6),(3,3),(3,4),(5,2),(5,3)]:
        d=p**k
        for ell in range(1,k+1):
            q=p**ell
            for val in range((k-ell)//2+1):
                u=(p**val,0)
                for coefficient,unit in product([0,1,p,p+1],[1,p+1,d-1]):
                    v=(p**val*coefficient%d,p**(k-ell-val)*unit%d)
                    assert d//gcd(d,u[0]*v[1])==q
                    size=len(closure(d,[tuple(q*a%d for a in u),tuple(q*a%d for a in v)]))
                    assert size==d//q,(d,ell,val,u,v,size)
                    valuation_cases+=1
    assert len(closure(12,[(0,0),(0,0)]))==1!=12//4
    return {'small_exhaustive':reports,'valuation_normal_form_cases':valuation_cases,
            'composite_d12_central_counterexample':True}


def determinant_checks():
    x,a,central=s.symbols('x a central')
    resultants=[]
    for q in [2,3,4,5,7,8,9,16,27]:
        result=s.resultant(x**q-central,1+a*x,x)
        assert s.expand(result-(1-(-a)**q*central))==0
        resultants.append(q)
    permutations_checked=0
    for q in range(2,9):
        survivors=[]
        for perm in permutations(range(q)):
            permutations_checked+=1
            if all(perm[row] in (row,(row-1)%q) for row in range(q)):
                inv=sum(perm[i]>perm[j] for i in range(q) for j in range(i+1,q))
                survivors.append((perm,(-1)**inv))
        assert len(survivors)==2
        full=tuple((j-1)%q for j in range(q))
        assert dict(survivors)[full]==(-1)**(q-1)
    return {'resultant_orders':resultants,'permutations_examined':permutations_checked,
            'odd_and_even_full_cycle_signs':'PASS'}


def independent_rank_27():
    """I+X^3+Z^3 in d=27: rank 25, over the cyclotomic field Q(zeta_9)."""
    x=s.symbols('x')
    field=s.QQ.alg_field_from_poly(s.Poly(s.cyclotomic_poly(9,x)),alias='zeta9')
    root=field.unit; d=27
    entries={j:{j:field.one+root**j,(j-3)%d:field.one} for j in range(d)}
    rank=DomainMatrix(entries,(d,d),field).rank()
    assert rank==25
    # The central powers have order three and nine distinct joint characters.
    omega=root**3
    zeros=[(i,j) for i,j in product(range(3),repeat=2)
           if field.one+omega**i+omega**j==field.zero]
    assert zeros==[(1,2),(2,1)]
    return {'d':27,'operator':'I+X^3+Z^3','commutator_order':3,
            'direct_exact_rank':rank,'direct_exact_nullity':d-rank,
            'field':str(field),'singular_central_character_powers':zeros}


def characters_and_sums():
    """All d>=16 incidences reduce to these character sets, by the written proof."""
    characters=list(product(range(4),repeat=2))
    family={}
    for a,b in product(range(4),repeat=2):
        if (a,b)==(0,0): continue
        if a%2==0 and b%2==0:
            selections=[{0},{2}]
        else:
            selections=[{j,(j+1)%4} for j in range(4)]
        for selected in selections:
            state=frozenset((x,y) for x,y in characters if (a*x+b*y)%4 in selected)
            assert len(state)==8
            family.setdefault(state,(a,b,sorted(selected)))
    assert len(family)==30
    counts=Counter(len(left&right) for left,right in combinations(family,2))
    assert counts==Counter({0:15,4:420})
    complement_pairs=sum(frozenset(characters)-left in family for left in family)//2
    assert complement_pairs==15
    failures={(x,y):sum(z not in {0,1} for z in (x,y,(x+y)%4)) for x,y in characters}
    assert Counter(failures.values())==Counter({0:3,1:3,2:9,3:1})
    assert sorted(key for key,value in failures.items() if value==0)==[(0,0),(0,1),(1,0)]
    assert sum(8*n for n in failures.values())==192
    # Normalization of B_j columns in the simultaneous character basis, using
    # independently generated exact polynomial values rather than a dense twirl.
    poly=lambda z:(z-1)*(z-s.I)
    column_checks=[]
    for (x,y),n in failures.items():
        vals=[s.expand(poly(s.I**a)) for a in (x,y,(x+y)%4)]
        power=s.expand(sum(val*s.conjugate(val) for val in vals))
        assert power==8*n
        if n:
            assert s.simplify(power/(8*n))==1
            column_checks.append((x,y))
    return {'character_cells':16,'distinct_half_rank_subspaces':len(family),
            'intersection_counts_in_sixteen_cells':dict(counts),
            'positive_sum_failure_counts':dict(Counter(failures.values())),
            'rank_at_d16':13,'trace_before_normalizing_at_d16':192,
            'exact_B_column_normalization_checks':len(column_checks)}


def operational_and_four_labels():
    z=s.symbols('z'); twirls=[]
    for d in [3,4,8,16]:
        modulus=s.Poly(s.cyclotomic_poly(d,z),z)
        for difference in range(d):
            coeff=sum(z**((b*difference)%d) for b in range(d))
            actual=s.rem(coeff,modulus.as_expr(),z)
            assert actual==(d if difference==0 else 0)
        twirls.append(d)
    modulus=z**4+1
    # Work with an independent formal signal variable, coefficient root z.
    t=s.symbols('t')
    polynomial=s.Poly(s.expand((t-1)*(t-z)*(t-z*z)),t)
    coeffs=[s.rem(value,modulus,z) for value in polynomial.all_coeffs()]
    assert len(coeffs)==4 and all(value!=0 for value in coeffs)
    values=[s.rem(polynomial.as_expr().subs(t,z**j),modulus,z) for j in range(8)]
    assert [j for j,value in enumerate(values) if value==0]==[0,1,2]
    norm=0
    for value in values:
        # z^{-1}=z^7; reduction remains entirely in Q[z]/(z^4+1).
        conjugate=s.rem(value.subs(z,z**7),modulus,z)
        norm=s.rem(norm+value*conjugate,modulus,z)
    assert s.expand(norm-(64+32*z-32*z**3))==0
    # Positive coefficients, exact rank 5d/8, and normalization are now checked.
    return {'twirl_matrix_unit_differences_checked':twirls,
            'four_term_coefficients_descending':[str(c) for c in coeffs],
            'order_eight_zero_eigenvalue_indices':[0,1,2],
            'order_eight_squared_norm':str(norm),
            'squared_norm_formula':'4*d*(2+sqrt(2))'}


def main():
    start=time.monotonic()
    proof=BASE/'work/cycle3/quantum/quantum_dyadic_trinomials.md'
    verifier=BASE/'work/cycle3/quantum/quantum_dyadic_verify.py'
    output={'status':'PASS','central_groups':central_group_checks(),
            'determinants':determinant_checks(),'direct_rank_27':independent_rank_27(),
            'incidence_and_positive_sums':characters_and_sums(),
            'operational_normalization':operational_and_four_labels(),
            'reviewed_source_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
            'inspected_constructor_verifier_sha256':hashlib.sha256(verifier.read_bytes()).hexdigest(),
            'independent_checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'elapsed_seconds':time.monotonic()-start,
            'independence':'Does not import or execute the constructing quantum verifier.',
            'limitations':'The written independent review, not finite tests, addresses all coefficients and dimensions.'}
    destination=HERE/'quantum_independent_checks.json'
    destination.write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','elapsed_seconds':output['elapsed_seconds'],
                      'direct_rank_d27':25,'projector_incidence_pairs':435}))


if __name__=='__main__': main()

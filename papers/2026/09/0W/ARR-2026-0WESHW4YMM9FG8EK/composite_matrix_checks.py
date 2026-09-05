"""Method-independent exact checks for the universal central-block formula.

Written by the constructing agent; this is a separate computational route, not
a claim of independent agent review. It does not import quantum_weyl_verify.
Groups are enumerated by closure, and ranks use direct exact matrices.
"""
from collections import deque
from itertools import product
from math import gcd
from pathlib import Path
import hashlib
import json
import sympy as s


def closure(d, generators):
    seen, pending = {(0, 0)}, deque([(0, 0)])
    while pending:
        x, y = pending.popleft()
        for a, b in generators:
            z = ((x+a) % d, (y+b) % d)
            if z not in seen:
                seen.add(z)
                pending.append(z)
    return seen


def gaussian_weyl(d, label):
    a, b = label
    assert d % 4 == 0 and b % (d//4) == 0
    matrix = s.zeros(d)
    for col in range(d):
        matrix[(col+a) % d, col] = s.I**((b//(d//4)*col) % 4)
    return matrix


def direct_case(name, d, u, v, c, a=s.Integer(1), b=s.Integer(1),
                uphase=s.Integer(1), vphase=s.Integer(1), expected_nullity=None,
                expected_h=None, expected_m=None):
    U, V = uphase*gaussian_weyl(d, u), vphase*gaussian_weyl(d, v)
    q = d//gcd(d, u[0]*v[1]-u[1]*v[0])
    H = closure(d, (u, v))
    R = closure(d, (tuple(q*x % d for x in u), tuple(q*x % d for x in v)))
    h = len(R)
    assert len(H) == q*q*h and d % (q*h) == 0
    m = d//(q*h)
    assert expected_h is None or h == expected_h
    assert expected_m is None or m == expected_m
    D = c*s.eye(d)+a*U+b*V
    power_test = c**q*s.eye(d)-(-1)**q*(a**q*U**q+b**q*V**q)
    power_test = power_test.applyfunc(s.simplify)
    nullity = d-D.to_DM(extension=True).rank()
    central_nullity = d-power_test.to_DM(extension=True).rank()
    assert expected_nullity is None or nullity == expected_nullity
    assert central_nullity == q*nullity
    assert nullity % m == 0
    singular_sectors = nullity//m
    assert central_nullity == q*m*singular_sectors
    if c != 0:
        assert nullity <= min(2, h)*m
    return {'name':name, 'd':d, 'u':u, 'v':v, 'c':str(c), 'a':str(a), 'b':str(b),
            'u_phase':str(uphase), 'v_phase':str(vphase), 'q':q,
            'H_order_by_closure':len(H), 'h_by_closure':h, 'm':m,
            'direct_exact_rank':d-nullity, 'direct_exact_nullity':nullity,
            'central_polynomial_nullity':central_nullity,
            'singular_sector_count_from_two_exact_ranks':singular_sectors,
            'two_sector_bound_applicable':c != 0, 'rank_field':str(D.to_DM(extension=True).domain)}


def run_checks():
    cases = [
        direct_case('one_sector_three_copies',12,(3,0),(0,3),s.root(2,4),
                    expected_nullity=3,expected_h=1,expected_m=3),
        direct_case('two_central_characters_only_one_singular',12,(3,0),(0,6),s.sqrt(2),
                    expected_nullity=3,expected_h=2,expected_m=3),
        direct_case('elementary_two_group_only_one_singular',24,(6,0),(0,6),s.sqrt(2),
                    expected_nullity=3,expected_h=4,expected_m=3),
        direct_case('two_singular_sectors_multiplicity_one',12,(1,0),(-1,6),s.Integer(1),
                    vphase=s.I,expected_nullity=2,expected_h=6,expected_m=1),
        direct_case('two_singular_sectors_multiplicity_three',36,(3,0),(-3,18),s.Integer(1),
                    vphase=s.I,expected_nullity=6,expected_h=6,expected_m=3),
        direct_case('commuting_two_roots',12,(0,3),(0,6),s.I,a=-(1+s.I),
                    expected_nullity=6,expected_h=4,expected_m=3),
        direct_case('zero_constant_negative_control',12,(1,0),(1,6),s.Integer(0),
                    expected_nullity=6,expected_h=6,expected_m=1),
    ]
    assert cases[-1]['direct_exact_nullity'] > 2*cases[-1]['m']
    # Independent algebraic root count for the two-sixth-root fixtures.
    z=s.Symbol('z')
    field=s.QQ.alg_field_from_poly(s.Poly(s.cyclotomic_poly(6,z)),alias='zeta6')
    root=field.unit
    sixth_root_zeros=[j for j in range(6) if field.one-root**j-root**((-j)%6)==field.zero]
    assert sixth_root_zeros==[1,5]
    # Degenerate centers: distinct sign corners cannot yield two zeros when
    # all three coefficients are nonzero. These fixture values hit one corner.
    elementary_zero_pairs=[(i,j) for i,j in product((1,-1),repeat=2) if i+j==2]
    assert elementary_zero_pairs==[(1,1)]
    return {'arithmetic':'direct SymPy exact number fields and direct group closure',
            'cases':cases,'sixth_root_zero_exponents':sixth_root_zeros,
            'elementary_two_group_zero_pairs':elementary_zero_pairs,
            'zero_constant_exceeds_two_m_as_required':True,
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'independence_scope':'No import of the main verifier; a separate method by the same constructing agent, not a new independent review.'}


if __name__=='__main__':
    result=run_checks()
    path=Path(__file__).with_name('composite_matrix_certificate.json')
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','cases':len(result['cases']),
                      'ranks':[(x['d'],x['direct_exact_rank']) for x in result['cases']]}))

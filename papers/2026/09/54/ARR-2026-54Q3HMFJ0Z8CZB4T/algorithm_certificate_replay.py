"""Independent bounded replay of the stored N=4,d=8 LP certificates.

No solver, floating-point proposals, or certified_constant row builder is used.
Horn triple generation and cell geometry are the already separately reviewed
dependencies; this checks conversion and witnesses directly in full dimension.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import lcm
import hashlib
import json
from geometry import cut_vertices
from verify_balanced_four import horn


def main():
    root = Path(__file__).resolve().parent
    path = root/'optimal_constant_N4_d8.json'
    report = json.loads(path.read_text())
    assert report['N'] == 4 and report['ambient_dimension'] == 8
    assert report['source_sha256'] == hashlib.sha256((root/'certified_constant.py').read_bytes()).hexdigest()
    d, n = 8, 4
    triples = tuple(t for r in range(1, d) for t in horn(r, d))
    allowed = set(triples)
    assert len(triples) == len(allowed) == report['Horn_triples'] == 8752
    covered, ratios, checks, dual_terms = set(), [], 0, 0
    minimum_slack = None
    for row in report['certificates']:
        a, b, spectrum = (tuple(map(Q, row[key])) for key in ('a', 'b', 'common_spectrum'))
        assert len(a) == len(b) == n and len(spectrum) == d
        assert a >= b and (a, b) not in covered
        assert sum(a) == sum(b) == 1 and min(a+b) >= 0
        assert list(a) == sorted(a, reverse=True) and list(b) == sorted(b, reverse=True)
        assert spectrum[-1] == 0 and min(spectrum) >= 0
        assert list(spectrum) == sorted(spectrum, reverse=True)
        lam = a+tuple(-x for x in reversed(b))
        assert sum(lam) == 0
        den = lcm(*(x.denominator for x in spectrum+lam))
        si, li = ([int(x*den) for x in vals] for vals in (spectrum, lam))
        for I, J, K in triples:
            slack = sum(si[i-1] for i in I)-sum(si[d-j] for j in J)-sum(li[k-1] for k in K)
            assert slack >= 0
            value = Q(slack, den)
            minimum_slack = value if minimum_slack is None else min(minimum_slack, value)
            checks += 1
        coeff = [Q(0)]*d
        bound = Q(0)
        for term in row['dual_terms']:
            weight = Q(term['weight'])
            assert weight >= 0
            if 'Horn_triple' in term:
                I, J, K = tuple(tuple(x) for x in term['Horn_triple'])
                assert (I, J, K) in allowed
                for i in I:
                    coeff[i-1] += weight
                for j in J:
                    coeff[d-j] -= weight
                bound += weight*sum(lam[k-1] for k in K)
            else:
                i = term['ordering_index']
                assert 1 <= i <= d-2
                coeff[i-1] += weight
                coeff[i] -= weight
            dual_terms += 1
        residual = tuple(1-c for c in coeff[:-1])
        assert min(residual) >= 0
        assert residual == tuple(map(Q, row['dual_nonnegative_residual']))
        assert bound == sum(spectrum) == Q(row['exact_cost'])
        ea, eb = 2*(1-a[0]), 2*(1-b[0])
        ua, ub = sum(abs(x-Q(1,n)) for x in a), sum(abs(x-Q(1,n)) for x in b)
        distance = min(ea+ub, ua+eb)
        assert distance == Q(row['D'])
        if distance:
            ratio = (Q(n+1,2)-bound)/distance
            assert ratio == Q(row['ratio'])
            ratios.append(ratio)
        else:
            assert row['ratio'] is None and bound == Q(n+1,2)
        covered.update(((a,b),(b,a)))
    assert len(report['certificates']) == report['LPs_solved_up_to_sign'] == 48
    assert len(covered) == report['ordered_vertices'] == 89
    assert covered == set(cut_vertices(n)[0])
    assert min(ratios) == Q(report['optimal_forward_coefficient']) == Q(4,7)
    result = {
        'status':'EXACT_INDEPENDENT_REPLAY_PASS', 'N':n, 'ambient_dimension':d,
        'certificates_checked':48, 'ordered_vertices_covered':89,
        'Horn_triples':len(triples), 'full_dimension_Horn_checks':checks,
        'dual_terms_reconstructed':dual_terms, 'minimum_Horn_slack':str(minimum_slack),
        'exact_optimal_forward_coefficient':str(min(ratios)),
        'minimum_attained_certificate_count':sum(x == min(ratios) for x in ratios),
        'proposer_source_sha256':report['source_sha256'],
        'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'replay_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Independent rational witness reconstruction; Horn enumeration and cell geometry remain the separately reviewed dependencies.'}
    (root/'algorithm_certificate_replay.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()

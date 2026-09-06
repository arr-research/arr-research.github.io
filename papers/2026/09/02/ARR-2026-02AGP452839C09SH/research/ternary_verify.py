"""Exact finite certificates for the ternary low-rank classification.

Standard library only. No floating-point rank decisions. This file is the
constructing agent's replay, not an independent review.
"""
from __future__ import annotations

import hashlib
import itertools as it
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
POINTS = tuple(it.product(range(3), repeat=2))
NORMALS = ((1, 0), (0, 1), (1, 1), (1, 2))
LINES = tuple((a, b, c) for a, b in NORMALS for c in range(3))
SETS = tuple(frozenset(p for p in POINTS if (a*p[0]+b*p[1]-c) % 3 == 0)
             for a, b, c in LINES)


def affine_certificate():
    assert len(set(SETS)) == 12 and all(len(s) == 3 for s in SETS)
    low = []
    union_counts = Counter()
    type_counts = Counter()
    supports = set()
    # Every nonempty subset, not just subsets predicted by the theorem.
    for mask in range(1, 1 << 12):
        ids = tuple(i for i in range(12) if mask >> i & 1)
        support = frozenset().union(*(SETS[i] for i in ids))
        union_counts[len(support)] += 1
        if len(support) > 6:
            continue
        contained = tuple(i for i, s in enumerate(SETS) if s <= support)
        assert ids == contained, (ids, contained)
        assert support not in supports
        supports.add(support)
        if len(ids) == 1:
            kind, rank_cells, factors = 'vertex', 3, 1
        elif len(ids) == 2:
            parallel = LINES[ids[0]][:2] == LINES[ids[1]][:2]
            kind = 'parallel_edge' if parallel else 'crossing_edge'
            rank_cells, factors = (6, 1) if parallel else (5, 2)
        else:
            assert len(ids) == 3
            assert len({LINES[i][:2] for i in ids}) == 3
            assert not set.intersection(*(set(SETS[i]) for i in ids))
            kind, rank_cells, factors = 'triangle', 6, 3
        assert len(support) == rank_cells
        # A private point identifies each coefficient in every listed simplex.
        private = {}
        for i in ids:
            others = frozenset().union(*(SETS[j] for j in ids if j != i))
            private[i] = sorted(SETS[i] - others)
            assert private[i]
        type_counts[kind] += 1
        # Two rational interior probes independently test the spectrum formula.
        probes = []
        for nums in ([1] * len(ids), list(range(1, len(ids)+1))):
            weights = [F(n, sum(nums)) for n in nums]
            values = [sum((w for i, w in zip(ids, weights) if p in SETS[i]), F(0))
                      for p in POINTS]
            assert sum(values) == 3 and sum(v != 0 for v in values) == rank_cells
            actual = sorted(v for v in values if v)
            if kind == 'vertex':
                expected = [F(1)]*3
            elif kind == 'parallel_edge':
                expected = sorted(weights*3)
            elif kind == 'crossing_edge':
                expected = sorted([F(1)] + weights*2)
            else:
                expected = sorted(weights + [1-w for w in weights])
            assert actual == expected
            probes.append({'weights': list(map(str, weights)),
                           'cell_values': list(map(str, values))})
        low.append({'lines': [LINES[i] for i in ids], 'kind': kind,
                    'support': sorted(support), 'rank_ninths': rank_cells,
                    'minimum_sparse_square_count': factors,
                    'private_points': {str(i): p for i,p in private.items()},
                    'probes': probes})
    assert dict(type_counts) == {'vertex': 12, 'parallel_edge': 12,
                                 'crossing_edge': 54, 'triangle': 72}
    assert {len(s) for s in supports} == {3, 5, 6}
    assert sum(len(s) == 6 for s in supports) == math.comb(9, 6) == 84
    return {'all_nonempty_subsets': 4095, 'union_size_counts': dict(union_counts),
            'low_stratum_counts': dict(type_counts), 'strata': low}


# Q(omega), omega^2 + omega + 1 = 0, represented by rational pairs.
ZERO, ONE = (F(0), F(0)), (F(1), F(0))
POW = (ONE, (F(0), F(1)), (F(-1), F(-1)))


def add(x, y): return (x[0]+y[0], x[1]+y[1])
def scale(x, a): return (a*x[0], a*x[1])
def mul(x, y):
    return (x[0]*y[0]-x[1]*y[1],
            x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def star(x): return (x[0]-x[1], -x[1])


def madd(*matrices):
    out = {}
    for matrix in matrices:
        for ij, x in matrix.items():
            out[ij] = add(out.get(ij, ZERO), x)
    return {ij:x for ij,x in out.items() if x != ZERO}


def mscale(matrix, x):
    return {ij:mul(v, x) for ij,v in matrix.items() if mul(v, x) != ZERO}


def mmul(a, b):
    brows = defaultdict(list)
    for (k,j), value in b.items(): brows[k].append((j,value))
    out = {}
    for (i,k), x in a.items():
        for j,y in brows[k]:
            out[i,j] = add(out.get((i,j), ZERO), mul(x,y))
    return {ij:x for ij,x in out.items() if x != ZERO}


def adjoint(matrix): return {(j,i):star(x) for (i,j),x in matrix.items()}
def trace(matrix, d):
    value = ZERO
    for i in range(d): value = add(value, matrix.get((i,i), ZERO))
    return value


def h_weyl(d, a, b):
    return {((j+a*(d//3)) % d,j): POW[(b*j) % 3] for j in range(d)}


def projector(d, line):
    a,b,c = line
    return mscale(madd(*(mscale(h_weyl(d, a*t, b*t), POW[(-c*t) % 3])
                        for t in range(3))), (F(1,3),F(0)))


def matrix_certificate():
    records = []
    for d in (9,27,81):
        identity = h_weyl(d,0,0)
        pp = [projector(d,l) for l in LINES]
        for p in pp:
            assert adjoint(p) == p and mmul(p,p) == p
            assert trace(p,d) == (F(d,3),F(0))
        for a,b in NORMALS:
            assert madd(*(projector(d,(a,b,c)) for c in range(3))) == identity
        cells = [mmul(projector(d,(1,0,x)), projector(d,(0,1,y)))
                 for x,y in POINTS]
        assert madd(*cells) == identity
        for i,e in enumerate(cells):
            assert mmul(e,e) == e and adjoint(e) == e
            assert trace(e,d) == (F(d,9),F(0))
            for j,f in enumerate(cells):
                if i != j: assert not mmul(e,f)
        # Matrix projectors are compared to separately generated affine sets.
        for p, s in zip(pp,SETS):
            assert p == madd(*(cells[i] for i,x in enumerate(POINTS) if x in s))
        pair_counts = Counter()
        for i,j in it.combinations(range(12),2):
            product = mmul(pp[i],pp[j])
            assert product == mmul(pp[j],pp[i])
            tr = trace(product,d)
            assert tr[1] == 0 and tr[0] in (0,F(d,9))
            pair_counts[str(tr[0])] += 1
        assert pair_counts == {'0':12,str(d//9):54}
        # A rational triangle mixture and crossing mixture: range projector
        # equality is an exact rank certificate using orthogonal cells.
        examples = []
        for ids, weights in [((0,3), (F(1,3),F(2,3))),
                             ((0,3,7), (F(1,6),F(1,3),F(1,2))),
                             ((0,1), (F(1,2),F(1,2)))]:
            rho = madd(*(mscale(pp[i],(F(3,d)*w,F(0)))
                         for i,w in zip(ids,weights)))
            assert trace(rho,d) == ONE
            support = frozenset().union(*(SETS[i] for i in ids))
            support_p = madd(*(cells[i] for i,x in enumerate(POINTS) if x in support))
            assert mmul(rho,support_p) == rho
            assert trace(support_p,d) == (F(len(support)*d,9),F(0))
            for i,x in enumerate(POINTS):
                value = F(3,d)*sum((w for j,w in zip(ids,weights) if x in SETS[j]),F(0))
                assert mmul(rho,cells[i]) == mscale(cells[i],(value,F(0)))
            examples.append({'lines':[LINES[i] for i in ids],
                             'weights':list(map(str,weights)),
                             'rank':len(support)*d//9})
        # Four Weyl terms give exact rank 4d/9, in the forbidden three-list gap.
        c = mmul(madd(identity,mscale(h_weyl(d,1,0),(-F(1),F(0)))),
                 madd(identity,mscale(h_weyl(d,0,1),(-F(1),F(0)))))
        square = mmul(c,adjoint(c))
        four_cells = madd(*(cells[i] for i,(x,y) in enumerate(POINTS) if x and y))
        assert square == mscale(four_cells,(F(9),F(0)))
        assert trace(square,d) == (F(4*d),F(0))
        records.append({'dimension':d, 'line_projectors':12, 'joint_cells':9,
                        'cell_rank':d//9, 'pair_intersection_counts':dict(pair_counts),
                        'mixtures':examples, 'four_label_rank':4*d//9,
                        'four_term_square_trace':4*d})
    return records


def arithmetic_certificate():
    # Finite illustrations of the proof's strict rank thresholds. Exhaustive
    # label arithmetic at d=9; higher k is proved in the manuscript, not inferred.
    d=9
    labels = [(a,b) for a,b in it.product(range(d),repeat=2) if (a,b)!=(0,0)]
    counts = Counter()
    for u in labels:
        for v in labels:
            if u==v: continue
            delta = u[0]*v[1]-u[1]*v[0]
            g=math.gcd(d,delta); q=d//g
            lattice_index=math.gcd(d*d,d*u[0],d*u[1],d*v[0],d*v[1],delta)
            group_order=d*d//lattice_index
            m=q*d//group_order
            assert q*d % group_order == 0
            if q>1:
                assert m==1 and d-2>=7*d//9
                counts['noncommuting_multiplicity_one']+=1
            else:
                assert group_order in (3,9)
                counts[f'commuting_group_{group_order}']+=1
    assert sum(counts.values())==80*79
    # Endpoint polynomial has exactly the two distinct ninth-root zeros.
    for k in range(2,9):
        d=3**k
        assert 7*d//9==d-2*(d//9)
        assert (2*d//9) % (d//3) != 0  # nonzero T^2 square coefficient outside H_3
        assert (4*d//9) not in (3**j for j in range(k))
    return {'dimension_9_ordered_pairs':6320, 'counts':dict(counts),
            'threshold_and_positive_sum_counterexample_dimensions':[3**k for k in range(2,9)],
            'dimension_9_feasible_ranks':[3,5,6,7,8,9]}


def main():
    result = {'status':'PASS', 'arithmetic':'rational pairs in Q(omega), exact integers',
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'geometry':affine_certificate(), 'matrices':matrix_certificate(),
              'arithmetic_checks':arithmetic_certificate(),
              'scope':'Finite certificates accompany universal algebraic proofs; not an independent review.'}
    paper=ROOT/'ternary_low_rank.md'
    if paper.exists(): result['manuscript_sha256']=hashlib.sha256(paper.read_bytes()).hexdigest()
    (ROOT/'ternary_certificate.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'], 'strata':result['geometry']['low_stratum_counts'],
                      'all_line_subsets':4095, 'matrix_dimensions':[9,27,81],
                      'ordered_label_pairs':6320},indent=2))


if __name__=='__main__': main()

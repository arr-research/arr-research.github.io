from pathlib import Path
from itertools import product, combinations, permutations
from fractions import Fraction
from math import ceil
import json

BASE = Path(__file__).resolve().parent
out = {}

# Full classification of occupation profiles, allowing more than one run per coset.
types = {
    2: [('singleton', 1, 1), ('full2', 2, 0)],
    4: [('singleton', 1, 1), ('chain2', 2, 1), ('opposite2', 2, 2),
        ('chain3', 3, 1), ('full4', 4, 0)],
}
profiles = {}
for q, options in types.items():
    for s, exits in [(5,1), (6,0), (6,1), (6,2), (7,1), (7,2), (7,3)]:
        solutions = []
        for counts in product(*(range(s//size+1) for name, size, runs in options)):
            if sum(c*item[1] for c,item in zip(counts,options)) != s:
                continue
            if sum(c*item[2] for c,item in zip(counts,options)) != exits:
                continue
            solutions.append({item[0]: c for c,item in zip(counts,options) if c})
        profiles[f'q{q}_s{s}_exits{exits}'] = solutions
assert {'opposite2':1,'full4':1} in profiles['q4_s6_exits2']
assert len(profiles['q4_s6_exits2']) == 3
assert len(profiles['q4_s7_exits3']) == 4
assert not profiles['q2_s6_exits1']
assert not profiles['q2_s7_exits2']
out['complete_short_orbit_profiles'] = profiles

# Check the omitted q4 profile really has period 2h, in a representative model.
for d in (4,8,16,32,64):
    n = d//4
    S = {(0,t*n) for t in range(4)} | {(1,0),(1,2*n)}
    assert {(a,(b+2*n)%d) for a,b in S} == S
out['omitted_q4_s6_profile_has_period_2h'] = 'PASS'

# Check random-order selection EXACTLY over every order, for every loopless
# digraph on four vertices with outdegree <=2. This includes 2-cycles.
V = tuple(range(4))
neighbors = [[set(c) for k in range(3) for c in combinations([w for w in V if w != v],k)] for v in V]
graph_count = order_count = 0
for adj_tuple in product(*neighbors):
    adj = dict(zip(V,adj_tuple))
    max_degree = max(map(len,adj_tuple))
    total_selected = max_selected = 0
    expected = sum(Fraction(1,1+len(adj[v])) for v in V)
    for order in permutations(V):
        position = {v:k for k,v in enumerate(order)}
        I = {v for v in V if all(position[v]<position[w] for w in adj[v])}
        # Every induced arc points forwards: no directed cycle can survive.
        for v in I:
            for w in adj[v] & I:
                assert position[v] < position[w]
        total_selected += len(I)
        max_selected = max(max_selected, len(I))
        order_count += 1
    assert Fraction(total_selected,24) == expected
    assert max_selected >= ceil(Fraction(4,1+max_degree))
    graph_count += 1
out['random_order_acyclic_selection'] = {
    'status':'PASS', 'graphs':graph_count, 'graph_order_pairs':order_count,
    'scope':'All loopless 4-vertex digraphs with maximum outdegree at most two, all 24 orders.'}

# Exact scalar arithmetic for all sizes at which the proof changes branch.
moment_bounds = {str(s): Fraction(s, s+3*(s-1)) for s in (5,6,7)}
assert all(v>Fraction(1,4) for v in moment_bounds.values())
out['generic_rank_over_dimension'] = {s:str(v) for s,v in moment_bounds.items()}
checks = 0
for k in range(3,61):
    q = 2**k
    for numerator,denominator in [(q-2,2),(q-4,2),(q-1,2)]:
        assert Fraction(numerator,denominator) >= Fraction(q,4)
        checks += 1
    assert ceil(Fraction(q-1,3)) >= q//4
    assert ceil(Fraction(q-4,2)) >= q//4
    assert q-6 >= q//4
    assert q-5 >= q//4
    checks += 4
out['exact_power_of_two_branch_arithmetic'] = {'status':'PASS','checks':checks,'q_min':8,'q_max':2**60}

# Run-length distributions needed for q>=8, where no full orbit is possible.
for s,exits in [(6,2),(7,2),(7,3)]:
    for lengths in product(range(1,s+1),repeat=exits):
        if sum(lengths)!=s:
            continue
        if exits==2:
            assert min(lengths)<=3
        else:
            assert min(lengths)<=2
            # If two of the runs occupy one coset, the other has length <=5.
            assert all(l<=5 for l in lengths)
out['large_orbit_run_lengths'] = 'PASS'
erasure_checks = 0
for k in range(4,21):
    d = 2**k
    for r in range(d//16,d//8):
        assert 2*r<d//4 and d//8<=2*r
        previous_budget = (d-1)//(2*r)
        assert previous_budget == ceil(Fraction(d,2*r))-1
        assert (previous_budget<7) == (14*r>=d)
        erasure_checks += 1
assert (128-1)//(2*9) == 7
assert (32-1)//(2*3) == 5
out['exact_erasure_budget_and_strict_improvement_arithmetic'] = {
    'status':'PASS', 'cases':erasure_checks,
    'strict_improvement_condition':'14*r >= d',
    'rounding_counterexample_to_r_greater_d_over_16':{'d':128,'r':9,'old_budget':7},
    'genuine_improvement_example':{'d':32,'r':3,'old_budget':5,'new_budget':7}}
out['status'] = 'PASS'
out['limitations'] = 'Exact finite diagnostics of the classification and graph-selection argument, not a universal theorem proof. The proof for all dimensions is analytic; the classical scalar Fourier bound is invoked separately.'
(BASE/'astra-binary-plateau-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

from itertools import combinations
from fractions import Fraction
from math import ceil, gcd
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
groups = []

for exits, expected in [(1, [(0, 1, 2)]), (2, [(2, 0, 2)])]:
    cases = [(singles, doubles, full)
             for singles in range(9) for doubles in range(5) for full in range(3)
             if singles + doubles == exits
             and singles + 2*doubles + 3*full == 8]
    assert cases == expected, (exits, cases)
    groups.append(dict(name=f'q3 size8 exits{exits} classification',
                       status='PASS', cases=cases,
                       coordinates=['singleton_cosets', 'doubleton_cosets', 'full_cosets']))

checked = 0
min_sizes = {}
for q in (9, 27):
    minima = q
    for delta in range(1, q):
        cycles = []
        unseen = set(range(q))
        while unseen:
            start = min(unseen)
            cycle = []
            j = start
            while j not in cycle:
                cycle.append(j)
                unseen.remove(j)
                j = (j + delta) % q
            cycles.append(cycle)
        assert len(cycles) == gcd(q, delta) <= q//3
        for holes_count in range(4):
            for holes in combinations(range(q), holes_count):
                active = set(range(q)) - set(holes)
                chosen = set(active)
                removed = 0
                for cycle in cycles:
                    if set(cycle) <= chosen:
                        chosen.remove(cycle[0])
                        removed += 1
                assert removed <= len(cycles)
                assert len(chosen) >= q - 3 - q//3
                # Kahn ordering checks acyclicity of the actual induced shift graph.
                remaining = set(chosen)
                order = []
                while remaining:
                    sources = [j for j in remaining if (j-delta) % q not in remaining]
                    assert sources, (q, delta, holes, chosen)
                    for j in sources:
                        remaining.remove(j)
                        order.append(j)
                position = {j: k for k, j in enumerate(order)}
                for j in chosen:
                    nxt = (j+delta) % q
                    if nxt in chosen:
                        assert position[j] < position[nxt]
                minima = min(minima, len(chosen))
                checked += 1
    min_sizes[str(q)] = minima
groups.append(dict(name='exact acyclic sector selection for all <=3 holes and nonzero shifts',
                   status='PASS', cases=checked, minimum_retained_sectors=min_sizes))

value = Fraction(27, 1) / (1 + Fraction(5 * 7, 8))
assert value == Fraction(216, 43) and ceil(value) == 6
assert 27//9 * (9-7) == 6
assert 27//27 * (27-7) == 20
assert 3*(9-3-9//3) == 9
assert 27-3-27//3 == 15
assert (3-2+1) * 3**(3-1-1) == 6
groups.append(dict(name='exact d27 s8 rank arithmetic', status='PASS',
                   generic_bound=str(value), generic_ceiling=ceil(value),
                   one_chain_bounds={'q9': 6, 'q27': 20},
                   two_coset_acyclic_bounds={'q9': 9, 'q27': 15},
                   classical_scalar_H27_8=6))

result = dict(status='PASS', groups=groups,
              limitations='Finite arithmetic and directed-graph diagnostics support, but do not replace, the analytic proof for arbitrary complex coefficients. The classical scalar law is checked arithmetically after assuming its cited theorem.')
(BASE / 'astra-s8-checks.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))

from pathlib import Path
import itertools,json
from fractions import Fraction
from math import ceil,gcd
ROOT=Path(__file__).parent
assert ceil(Fraction(27,1+Fraction(5*7,8)))==6
# Exhaust all possible cycle occupancy profiles in the q3/s8/two-exit branch.
profiles=[]
for full in range(3):
    for a,b in itertools.product((1,2),repeat=2):
        if 3*full+a+b==8:profiles.append((full,a,b))
assert profiles==[(2,1,1)]
# A subset of a directed translation graph is acyclic iff it omits a vertex
# from each complete translation cycle. Check all subsets for q9; for q27,
# exhaust all hole sets of size <=3 (the theorem's active set has >=24 vertices).
checks=0
for q in (9,27):
    hole_sets=([tuple(i for i in range(q) if mask>>i&1) for mask in range(1<<q)] if q==9 else
               [h for k in range(4) for h in itertools.combinations(range(q),k)])
    for delta in range(1,q):
        order=q//gcd(q,delta)
        seen=set();cycles=[]
        for v in range(q):
            if v in seen:continue
            cyc=[];u=v
            while u not in seen:seen.add(u);cyc.append(u);u=(u+delta)%q
            cycles.append(cyc)
        assert len(cycles)==q//order
        for holes in hole_sets:
            active=set(range(q))-set(holes);I=set(active)
            for cyc in cycles:
                if set(cyc)<=I:I.remove(cyc[0])
            assert len(I)>=len(active)-q//order
            # Explicit topological elimination, without using the cycle test again.
            remaining=set(I);removed=0
            while remaining:
                sources=[v for v in remaining if (v-delta)%q not in remaining]
                assert sources
                remaining.difference_update(sources);removed+=len(sources)
            assert removed==len(I)
            checks+=1
out={'status':'PASS','q3_occupancy_profiles':profiles,'exact_acyclic_submatrix_checks':checks,'s8_moment_bound':'ceil(216/43)=6','scalar_branch':'DVB TW470 Theorem10: H9(8)=2, H27(8)=6; theorem invoked, not re-proved by enumeration.'}
(ROOT/'two-run-results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

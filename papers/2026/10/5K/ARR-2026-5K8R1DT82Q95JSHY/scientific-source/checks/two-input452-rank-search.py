"""Direct rational contraction for truncated single-error vectors.
The real diagonal error has entries(d-1,-1,...,-1), so no numerical
eigensolver or root-of-unity approximation enters the Rayleigh values.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product,combinations
import json

d=13
words=[tuple((a+b*x+c*x*x)%d for x in range(6))
       for a,b,c in product(range(d),repeat=3)]
refs=sorted({w[:2] for w in words})
partitions=[]
for u in range(5):
    for S in combinations(range(2,6),u):
        rem=tuple(i for i in range(6) if i not in S)
        partitions.append((S,rem))

def rayleigh(k):
    A=set(refs[:k])
    selected=[w for w in words if w[:2] in A]
    assert len(selected)==k*d
    # With fixed R, each output coordinate ranges over F_d once.
    # Norm of the unnormalized filtered vector is k(d-1)/d^2;
    # its normalized R density is uniform on A, Schmidt rank exactly k.
    norm_numerator=sum(((d-1) if w[2]==0 else -1)**2 for w in selected)
    assert norm_numerator==k*d*(d-1)
    total=Q(0)
    for S,rem in partitions:
        groups=defaultdict(list)
        for w in selected:
            groups[tuple(w[i] for i in rem)].append(
                (tuple(w[i] for i in S),(d-1) if w[2]==0 else -1))
        G=defaultdict(int)
        for entries in groups.values():
            for a,_ in entries:
                for s,weight in entries:G[(a,s)]+=weight
        total+=(-Q(1,2))**(4-len(S))*sum(v*v for v in G.values())
    return total/(d*d*k*(d-1))

values=[rayleigh(k) for k in range(1,d*d+1)]
assert values[-1]==Q(-3,104)
assert all(v>=0 for v in values[:40]),'Counterexample to author451 claimed bound'
negative=[k for k,v in enumerate(values,1) if v<0]
assert negative
k=negative[0]
print(json.dumps({'status':'PASS','d':d,'tested_nested_reference_sets':len(values),
 'guaranteed_order_451':40,'first_negative_in_this_family':k,
 'negative_value':str(values[k-1]),'Schmidt_rank_of_negative_vector':k,
 'definition':'Normalize (projection onto first k lexicographic reference pairs tensor I) (diagonal error on physical0) Psi_MDS. Error has diagonal(12,-1,...,-1).',
 'scope':'This supplies an actual exact rank-k negative witness, not a proof that k is the first failing rank among all vectors. It does not prove low-rank positivity universally.',
 'values':[{'rank':j,'Rayleigh':str(v)} for j,v in enumerate(values,1)]},indent=2))

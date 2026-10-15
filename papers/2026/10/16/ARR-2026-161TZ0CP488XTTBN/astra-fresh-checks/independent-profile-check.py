from itertools import combinations_with_replacement, permutations, product
from fractions import Fraction
from math import ceil
import json
from pathlib import Path
out={}
for q,targets in [(2,[(5,1),(6,0),(6,2),(7,1),(7,3)]),(4,[(5,1),(6,1),(6,2),(7,1),(7,2),(7,3)])]:
    types={}
    for mask in range(1,1<<q):
        points={j for j in range(q) if mask>>j&1}
        exits=sum((j+1)%q not in points for j in points)
        key=(len(points),exits)
        types[key]=str(len(points))+('opp' if q==4 and key==(2,2) else '')
    ordered=sorted(types)
    for s,e in targets:
        profiles=set()
        for ncosets in range(1,s+1):
            for pat in combinations_with_replacement(ordered,ncosets):
                if sum(a for a,b in pat)==s and sum(b for a,b in pat)==e:
                    profiles.add(tuple(types[x] for x in pat))
        out[f'q{q}_s{s}_exits{e}']=sorted(profiles)
expected={
'q2_s5_exits1':[('1','2','2')],
'q2_s6_exits0':[('2','2','2')],
'q2_s6_exits2':[('1','1','2','2')],
'q2_s7_exits1':[('1','2','2','2')],
'q2_s7_exits3':[('1','1','1','2','2')],
'q4_s5_exits1':[('1','4')],
'q4_s6_exits1':[('2','4')],
'q4_s6_exits2':[('1','1','4'),('2opp','4'),('3','3')],
'q4_s7_exits1':[('3','4')],
'q4_s7_exits2':[('1','2','4')],
'q4_s7_exits3':[('1','1','1','4'),('1','2opp','4'),('1','3','3'),('2','2','3')]
}
assert out==expected,(out,expected)
# Enumerate all four-vertex simple directed graphs, including unrestricted degrees;
# the retained set under every ordering must be acyclic, and the average is exact.
graphs=0
V=range(4); arcs=[(a,b) for a in V for b in V if a!=b]
for mask in range(1<<len(arcs)):
    edges=[arcs[i] for i in range(len(arcs)) if mask>>i&1]
    neigh={v:{b for a,b in edges if a==v} for v in V};total=0
    for order in permutations(V):
        pos={v:i for i,v in enumerate(order)}
        retained={v for v in V if all(pos[v]<pos[w] for w in neigh[v])}
        assert all(pos[a]<pos[b] for a,b in edges if a in retained and b in retained)
        total+=len(retained)
    assert Fraction(total,24)==sum(Fraction(1,len(neigh[v])+1) for v in V)
    graphs+=1
out['all_four_vertex_digraphs']=graphs
out['all_orders_per_graph']=24
# Exact arithmetic at low orders plus general symbolic thresholds are documented in report.
for k in range(3,101):
    q=2**k
    assert Fraction(q-4,2)>=Fraction(q,4)
    assert ceil(Fraction(q-1,3))>=Fraction(q,4)
    assert q-6>=Fraction(q,4)
    assert ceil(Fraction(q-2,2))>Fraction(q,4)
out['binary_orders_checked']=98
out['status']='PASS'
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))

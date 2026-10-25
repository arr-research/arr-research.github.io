from collections import defaultdict
from fractions import Fraction as Q
from itertools import product,combinations
import json

def run(d,h):
    selected=[]
    for a,b,c in product(range(d),repeat=3):
        w=tuple((a+b*x+c*x*x)%d for x in range(6))
        if w[1]<h:selected.append(w)
    k=h*d
    assert len(selected)==h*d*d
    norm=sum(((d-1) if w[2]==0 else -1)**2 for w in selected)
    assert norm==h*d*d*(d-1)
    total=Q(0);terms=[]
    for u in range(5):
        for S in combinations(range(2,6),u):
            rem=tuple(i for i in range(6) if i not in S)
            groups=defaultdict(list)
            for w in selected:
                groups[tuple(w[i] for i in rem)].append(
                    (tuple(w[i] for i in S),(d-1) if w[2]==0 else -1))
            G=defaultdict(int)
            for entries in groups.values():
                for a,_ in entries:
                    for s,f in entries:G[(a,s)]+=f
            ch_theta=Q(sum(v*v for v in G.values()),d*d*k*(d-1))
            expected={0:Q(0),1:Q(h) if 2 in S else Q(0),
                      2:Q(h,d) if 2 in S else Q(d-h,d*(d-1)),
                      3:Q(1,d),4:Q(1)}[u]
            assert ch_theta==expected,(d,h,S,ch_theta,expected)
            total+=(-Q(1,2))**(4-u)*ch_theta
            terms.append({'traced':list(S),'d_squared_theta':str(ch_theta)})
    formula=1-Q(2,d)+Q(3,4)*(Q(h,d)+Q(d-h,d*(d-1)))-Q(h,8)
    assert total==formula
    return {'d':d,'h':h,'Schmidt_rank':k,'direct_Rayleigh':str(total),'terms':terms}

r=[run(13,h) for h in (1,3,9,13)]+[run(43,9)]
assert r[-1]['direct_Rayleigh']=='-1/2408'
print(json.dumps({'status':'PASS','method':'Direct weighted integer Gram contractions from sparse MDS vectors; every partial-trace term compared with the proposed counting formula','scope':'Five explicit cases, not a universal independent audit','cases':r},indent=2))

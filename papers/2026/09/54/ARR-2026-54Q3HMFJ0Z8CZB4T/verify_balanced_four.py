"""Exact certificate: optimal balanced (4,4) coefficient 4/7.

All arithmetic below is rational/integer. Proposed witnesses are untrusted data.
Classical Horn sufficiency is imported; its finite hypotheses are reconstructed.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from functools import lru_cache
from pathlib import Path
from math import lcm
import json,hashlib,time
from geometry import cut_vertices,D,solve

ROOT=Path(__file__).resolve().parent

@lru_cache(None)
def horn(r,d):
    subsets=list(combinations(range(1,d+1),r));by_sum={}
    for K in subsets:by_sum.setdefault(sum(K),[]).append(K)
    lower=[(p,horn(p,r)) for p in range(1,r)]
    out=[]
    for I,J in product(subsets,repeat=2):
        for K in by_sum.get(sum(I)+sum(J)-r*(r+1)//2,[]):
            if all(sum(I[i-1] for i in A)+sum(J[j-1] for j in B)<=sum(K[k-1] for k in C)+p*(p+1)//2
                   for p,ts in lower for A,B,C in ts):out.append((I,J,K))
    return tuple(out)

def main():
    started=time.monotonic()
    vertices,cells,cuts=cut_vertices(4)
    assert len(vertices)==89
    assert [(len(c['vertices']),len(c['edges'])) for c in cells]==[(4,6),(5,8),(4,6)]
    proposals=json.loads((ROOT/'witnesses_N4.json').read_text())
    lookup={}
    for row in proposals:
        a,b,s=(tuple(map(Q,row[k])) for k in ('a','b','s'))
        assert (a,b) not in lookup
        lookup[a,b]=s
        lookup[b,a]=s
    assert set(lookup)==set(vertices)
    counts=[len(horn(r,8)) for r in range(1,8)]
    assert counts==[36,462,2120,3516,2120,462,36]
    triples=[t for r in range(1,8) for t in horn(r,8)]
    reports=[]
    for a,b in vertices:
        s=lookup[a,b];lam=a+tuple(-x for x in reversed(b))
        assert len(s)==8 and min(s)>=0 and list(s)==sorted(s,reverse=True)
        assert sum(a)==sum(b)==1 and min(a+b)>=0
        denominator=lcm(*(x.denominator for x in s+lam))
        si=[int(x*denominator) for x in s];li=[int(x*denominator) for x in lam]
        slacks=[sum(si[i-1] for i in I)-sum(si[8-j] for j in J)-sum(li[k-1] for k in K) for I,J,K in triples]
        assert min(slacks)>=0,(a,b,min(slacks))
        distance=D(a,b);cost=sum(s);gap=Q(5,2)-cost-Q(4,7)*distance
        assert gap>=0,(a,b,cost,distance,gap)
        reports.append({'a':a,'b':b,'s':s,'D':distance,'cost_upper':cost,
                        'stability_slack':gap,'Horn_min_slack':Q(min(slacks),denominator)})
    a=(Q(5,8),)+(Q(1,8),)*3;b=(Q(1,2),Q(1,2),Q(0),Q(0))
    assert sum(lookup[a,b])==Q(3,2)
    assert D(a,b)==Q(7,4)
    assert 3*b[1]-a[1]+a[3]==Q(3,2)
    # General lower witness is proved analytically from an r=2 Horn triple.
    # These checks cover its indexing; the manuscript proves every d>=6.
    for d in range(6,65):
        I,J,K=(1,3),(1,d-1),(2,d-1)
        assert sum(I)+sum(J)==sum(K)+3
        assert all(I[f-1]+J[g-1]<=K[h-1]+1 for f,g,h in [(1,1,1),(1,2,2),(2,1,2)])
    # Exact perturbation identities, not a numerical limit argument.
    for eta in [Q(1,32),Q(1,64),Q(1,1000)]:
        be=(Q(1,2)-eta,Q(1,2)-eta,eta,eta)
        assert min(be)>0 and list(be)==sorted(be,reverse=True)
        assert D(a,be)==Q(7,4)-4*eta
        assert 3*be[1]-a[1]+a[3]==Q(3,2)-3*eta
        assert Q(5,2)-Q(4,7)*D(a,be)==Q(3,2)+Q(16,7)*eta
    report={'status':'PASS','coefficient':'4/7','canonical_inertia':[4,4],
            'all_fixed_ambient_dimensions_at_least':8,'unique_ordered_vertices':89,
            'Horn_counts':counts,'Horn_triples':len(triples),'rational_Horn_checks':len(vertices)*len(triples),
            'sharp_boundary_cost':'3/2','sharp_boundary_distance':'7/4','sharpness_lower_bound':'3*b_2-a_2+a_4',
            'source_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'geometry.py',ROOT/'witnesses_N4.json']},
            'cells':cells,'edge_cuts':cuts,'witnesses':reports,
            'scope':'Finite exact checks plus the analytic convex-cell and all-dimension sharpness arguments in the manuscript. Horn sufficiency is imported, not formally proved.'}
    (ROOT/'balanced_four_certificate.json').write_text(json.dumps(report,default=str,indent=2)+'\n',encoding='utf-8',newline='\n')
    print({k:v for k,v in report.items() if k not in ['cells','edge_cuts','witnesses','source_hashes','scope']})
    print('seconds',round(time.monotonic()-started,3))

if __name__=='__main__':main()

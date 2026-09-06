"""Exact N5 verification. No optimizer is imported or executed.

Reconstructs recursive Horn constraints and complete cut geometry. Uses checked
int64 operations for primal constraints; Fraction for duals and all conclusions.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import json,hashlib,time
import numpy as np
from geometry import cut_vertices,D,q
from horn_fast import horn
ROOT=Path(__file__).resolve().parent

def main():
    started=time.monotonic();vertices,cells,cuts=cut_vertices(5)
    triples=[t for r in range(1,10) for t in horn(r,10)]
    assert len(vertices)==267 and len(triples)==191353
    rows=np.zeros((len(triples),10),dtype=np.int64);target=np.zeros_like(rows)
    for z,(I,J,K) in enumerate(triples):
        for i in I:rows[z,i-1]+=1
        for j in J:rows[z,10-j]-=1
        for k in K:target[z,k-1]+=1
    def witness(a,b,s):
        assert len(a)==len(b)==5 and sum(a)==sum(b)==1
        assert min(a+b)>=0 and a==tuple(sorted(a,reverse=True)) and b==tuple(sorted(b,reverse=True))
        assert len(s)==10 and min(s)>=0 and s==tuple(sorted(s,reverse=True)) and s[-1]==0
        lam=a+tuple(-x for x in reversed(b));den=lcm(*(x.denominator for x in lam+s))
        si=np.array([int(x*den) for x in s],dtype=np.int64);li=np.array([int(x*den) for x in lam],dtype=np.int64)
        assert 20*max(max(abs(int(x)) for x in si),max(abs(int(x)) for x in li))<2**60
        slack=rows@si-target@li;assert min(slack)>=0
        return Q(3)-sum(s)-Q(113,152)*D(a,b)
    proposed=json.loads((ROOT/'optimal_constant_N5_d10.json').read_text())['certificates']
    lookup={};dual_count=0;allowed=set(triples)
    for record in proposed:
        a,b,s=[tuple(map(Q,record[k])) for k in ['a','b','common_spectrum']]
        assert (a,b) not in lookup
        gap=witness(a,b,s);assert gap>=0
        lam=a+tuple(-x for x in reversed(b));coeff=[Q(0)]*9;objective=Q(0)
        for term in record['dual_terms']:
            weight=Q(term['weight']);assert weight>=0
            row=[0]*9;rhs=Q(0)
            if 'Horn_triple' in term:
                I,J,K=tuple(tuple(x) for x in term['Horn_triple']);assert (I,J,K) in allowed
                for i in I:
                    if i<10:row[i-1]+=1
                for j in J:
                    if j>1:row[10-j]-=1
                rhs=sum(lam[k-1] for k in K)
            else:
                i=term['ordering_index'];assert 1<=i<=8;row[i-1]=1;row[i]=-1
            coeff=[x+weight*y for x,y in zip(coeff,row)];objective+=weight*rhs;dual_count+=1
        assert all(x<=1 for x in coeff) and objective==sum(s)==Q(record['exact_cost'])
        assert D(a,b)==Q(record['D'])
        if D(a,b):assert (Q(3)-sum(s))/D(a,b)==Q(record['ratio'])
        lookup[a,b]=(s,gap)
        if a!=b:lookup[b,a]=(s,witness(b,a,s))
    assert set(lookup)==set(vertices)
    e=(Q(1),)+(Q(0),)*4;u=(Q(1,5),)*5
    A=(Q(13,20),)+(Q(7,80),)*4;B=(Q(1,2),)*2+(Q(0),)*3
    zero={ab for ab,(s,gap) in lookup.items() if gap==0}
    assert zero=={(e,u),(u,e),(A,B),(B,A)}
    cell_rows=[];segments=set()
    for r in range(1,5):
        for t in range(1,5):
            for orientation in [-1,1]:
                contacts=sorted((a,b) for a,b in zero if a[r-1]>=Q(1,5)>=a[r] and b[t-1]>=Q(1,5)>=b[t] and orientation*(q(a)-q(b))>=0)
                assert len(contacts)<=2
                if len(contacts)==2:segments.add(tuple(contacts))
                cell_rows.append({'r':r,'s':t,'orientation':orientation,'contacts':contacts})
    assert segments=={tuple(sorted([(e,u),(A,B)])),tuple(sorted([(u,e),(B,A)]))}
    midpoint=json.loads((ROOT/'contact_midpoint.json').read_text())
    a,b,s=[tuple(map(Q,midpoint[k])) for k in ['a','b','s']]
    assert a==tuple((x+y)/2 for x,y in zip(e,A)) and b==tuple((x+y)/2 for x,y in zip(u,B))
    midpoint_gap=witness(a,b,s);assert midpoint_gap==Q(91,160)
    assert sum(s)==Q(69,40) and D(a,b)==Q(19,20)
    # Integer identity proving recursive admissibility for every d>=4.
    # I=(1,3), J=(1,d-1), K=(2,d-1), lower r1 tests: 2<=3, d<=d, 4<=d.
    # The proof uses these symbolic inequalities, not the finite examples below.
    for d in range(5,65):
        I,J,K=(1,3),(1,d-1),(2,d-1)
        assert sum(I)+sum(J)==sum(K)+3
        assert all(I[f-1]+J[g-1]<=K[h-1]+1 for f,g,h in [(1,1,1),(1,2,2),(2,1,2)])
    assert 3*B[1]-A[1]+A[3]+A[4]==Q(127,80)==sum(lookup[A,B][0])
    for eta in [Q(1,100),Q(1,1000)]:
        be=(Q(1,2)-Q(3,2)*eta,)*2+(eta,)*3
        assert min(be)>0 and D(A,be)==Q(19,10)-6*eta
        assert 3*be[1]-A[1]+A[3]+A[4]==Q(127,80)-Q(9,2)*eta
    report={'status':'PASS','coefficient':'113/152','ambient_scope':'every fixed d>=10 (analytic padding and obstruction)',
            'ordered_vertices':len(vertices),'representatives':len(proposed),'Horn_counts':[len(horn(r,10)) for r in range(1,10)],
            'Horn_triples':len(triples),'integer_Horn_checks':(len(vertices)+1)*len(triples),'dual_terms_checked':dual_count,
            'zero_slack_vertices':sorted(zero),'positive_vertices':len(vertices)-len(zero),
            'minimum_positive_vertex_slack':min(gap for s,gap in lookup.values() if gap>0),
            'candidate_segments':sorted(segments),'midpoint_gap':midpoint_gap,'cell_contact_sets':cell_rows,
            'elapsed_seconds':time.monotonic()-started,'source_hashes':{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in ['verify_n5.py','geometry.py','horn_fast.py','optimal_constant_N5_d10.json','contact_midpoint.json']},
            'limits':['Horn sufficiency is classical and imported.','Finite verification is combined with the manuscript proofs of coverage, padding, sharpness and contact exclusion.','No proof-assistant verification or external refereeing is claimed.']}
    (ROOT/'n5_certificate.json').write_text(json.dumps(report,default=str,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['source_hashes','cell_contact_sets','candidate_segments','zero_slack_vertices','limits']},default=str,indent=2))
if __name__=='__main__':main()

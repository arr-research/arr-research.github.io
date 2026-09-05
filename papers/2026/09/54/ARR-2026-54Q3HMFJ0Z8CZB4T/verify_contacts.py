"""Exact contact-locus certificate; no floating-point proposals are executed."""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import json,hashlib
from geometry import cut_vertices,D
from verify_balanced_four import horn
ROOT=Path(__file__).resolve().parent
def q(a):return 2*(1-a[0])-sum(abs(x-Q(1,4)) for x in a)
def in_cell(a,r):return a[r-1]>=Q(1,4)>=a[r]
def check(a,b,s,triples):
    assert len(s)==8 and list(s)==sorted(s,reverse=True) and min(s)>=0
    lam=a+tuple(-x for x in reversed(b));den=lcm(*(x.denominator for x in lam+s))
    li=[int(x*den) for x in lam];si=[int(x*den) for x in s]
    assert all(sum(si[i-1] for i in I)-sum(si[8-j] for j in J)>=sum(li[k-1] for k in K) for I,J,K in triples)
    gap=Q(5,2)-sum(s)-Q(4,7)*D(a,b);assert gap>=0
    return gap
def main():
    vertices,_,_=cut_vertices(4);triples=[t for r in range(1,8) for t in horn(r,8)]
    proposed=json.loads((ROOT/'optimal_constant_N4_d8.json').read_text())['certificates']
    witnesses={}
    for row in proposed:
        a,b,s=[tuple(map(Q,row[k])) for k in ['a','b','common_spectrum']]
        witnesses[a,b]=s;witnesses[b,a]=s
    assert set(witnesses)==set(vertices)
    zero={ab for ab,s in witnesses.items() if check(*ab,s,triples)==0}
    e=(Q(1),Q(0),Q(0),Q(0));u=(Q(1,4),)*4
    A=(Q(5,8),)+(Q(1,8),)*3;B=(Q(1,2),)*2+(Q(0),)*2
    assert zero=={(e,u),(u,e),(A,B),(B,A)}
    cell_rows=[];segments=set()
    for r in range(1,4):
        for s in range(1,4):
            for orientation in [-1,1]:
                contact=sorted((a,b) for a,b in zero if in_cell(a,r) and in_cell(b,s) and orientation*(q(a)-q(b))>=0)
                assert len(contact)<=2
                if len(contact)==2:segments.add(tuple(contact))
                cell_rows.append({'r':r,'s':s,'orientation':orientation,'possible_contact_vertices':contact})
    assert segments=={tuple(sorted([(e,u),(A,B)])),tuple(sorted([(u,e),(B,A)]))}
    midpoint=json.loads((ROOT/'contact_midpoint.json').read_text())
    a,b,s=[tuple(map(Q,midpoint[k])) for k in ['a','b','s']]
    assert a==tuple((x+y)/2 for x,y in zip(e,A))
    assert b==tuple((x+y)/2 for x,y in zip(u,B))
    gap=check(a,b,s,triples);assert gap==Q(7,16)
    assert sum(s)==Q(25,16) and D(a,b)==Q(7,8)
    report={'status':'PASS','ordered_vertices':89,'Horn_triples':8752,'exact_Horn_checks':90*8752,'zero_slack_vertices':sorted(zero),'candidate_segments':sorted(segments),'midpoint_cost_upper':sum(s),'midpoint_distance':D(a,b),'midpoint_slack':gap,'cell_contact_sets':cell_rows,'scope':'Finite witnesses and cell incidence. Concavity excludes all segment interiors; the manuscript proves the complete contact classification in every fixed ambient dimension.','source_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'contact_midpoint.json',ROOT/'optimal_constant_N4_d8.json']}}
    (ROOT/'contact_certificate.json').write_text(json.dumps(report,default=str,indent=2)+'\n',encoding='utf-8')
    print({k:v for k,v in report.items() if k not in ['cell_contact_sets','source_hashes','scope']})
if __name__=='__main__':main()

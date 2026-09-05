"""Exact, exhaustive certificate for D_* <= (36/17) delta at inertia (3,3).

Python standard library only. Horn sufficiency is an imported theorem.
Input witnesses are rational proposal data; no floating arithmetic is used here.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from functools import lru_cache
from pathlib import Path
import json, hashlib

ROOT=Path(__file__).resolve().parent

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def mul(c,x): return tuple(c*a for a in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))

def solve(matrix,rhs):
    n=len(rhs); a=[[Q(x) for x in row]+[Q(y)] for row,y in zip(matrix,rhs)]
    for k in range(n):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return None
        a[k],a[pivot]=a[pivot],a[k]
        p=a[k][k]; a[k]=[x/p for x in a[k]]
        for i in range(n):
            if i!=k:
                p=a[i][k]; a[i]=[x-p*y for x,y in zip(a[i],a[k])]
    return tuple(row[-1] for row in a)

def enumerate_cells():
    one=(1,0,0,0,0)
    a=((0,1,0,0,0),(0,0,1,0,0),(1,-1,-1,0,0))
    b=((0,0,0,1,0),(0,0,0,0,1),(1,0,0,-1,-1))
    base=[]
    for v in (a,b):base.extend([sub(v[0],v[1]),sub(v[1],v[2]),v[2]])
    vertices=set();cells=[]
    for j,k,o in product((1,2),(1,2),(0,1)):
        ua=sub(mul(6,tuple(map(sum,zip(*a[:j])))),mul(2*j,one))
        ub=sub(mul(6,tuple(map(sum,zip(*b[:k])))),mul(2*k,one))
        d1=add(mul(6,sub(one,a[0])),ub)
        d2=add(ua,mul(6,sub(one,b[0])))
        rows=base+[sub(mul(3,a[j-1]),one),sub(one,mul(3,a[j])),
                   sub(mul(3,b[k-1]),one),sub(one,mul(3,b[k])),
                   sub(d2,d1) if o==0 else sub(d1,d2)]
        found={}
        for ix in combinations(range(len(rows)),4):
            x=solve([rows[i][1:] for i in ix],[-rows[i][0] for i in ix])
            if x is not None and all(dot(row,(Q(1),)+x)>=0 for row in rows):
                found[x]=ix
        vertices.update(found)
        cells.append({'j':j,'k':k,'orientation':o,'inequalities':rows,
                      'vertices':[{'point':list(map(str,x)),'active_rows':ix} for x,ix in sorted(found.items())]})
    return vertices,cells

@lru_cache(None)
def horn(r,d):
    subsets=list(combinations(range(1,d+1),r)); bysum={}
    for K in subsets:bysum.setdefault(sum(K),[]).append(K)
    out=[]
    for I,J in product(subsets,repeat=2):
        for K in bysum.get(sum(I)+sum(J)-r*(r+1)//2,[]):
            if all(sum(I[f-1] for f in F)+sum(J[g-1] for g in G)
                   <=sum(K[h-1] for h in H)+p*(p+1)//2
                   for p in range(1,r) for F,G,H in horn(p,r)):
                out.append((I,J,K))
    return tuple(out)

def main():
    vertices,cells=enumerate_cells()
    assert [len(c['vertices']) for c in cells]==[8,8,10,7,7,10,8,8]
    assert len(vertices)==22
    witnesses=json.loads((ROOT/'balanced_exploration.json').read_text())
    given={}; proof=[]; counts=[len(horn(r,6)) for r in range(1,6)]
    assert sum(counts)==522
    for row in witnesses:
        a=tuple(map(Q,row['a'])); b=tuple(map(Q,row['b'])); s=tuple(map(Q,row['s']))+(Q(0),)
        x=(a[0],a[1],b[0],b[1]);given[x]=row
        assert sum(a)==sum(b)==1 and all(s[i]>=s[i+1] for i in range(5)) and s[-1]==0
        lam=a+tuple(-v for v in reversed(b)); neg=tuple(-v for v in reversed(s))
        slacks=[sum(s[i-1] for i in I)+sum(neg[j-1] for j in J)-sum(lam[k-1] for k in K)
                for r in range(1,6) for I,J,K in horn(r,6)]
        assert min(slacks)>=0
        D=min(2*(1-a[0])+sum(abs(v-Q(1,3)) for v in b),
              2*(1-b[0])+sum(abs(v-Q(1,3)) for v in a))
        assert D==Q(row['D']) and sum(s)==Q(row['cost'])
        slack=2-sum(s)-Q(17,36)*D
        assert slack>=0,(a,b,s,D,slack)
        proof.append({'a':list(map(str,a)),'b':list(map(str,b)),'s':list(map(str,s)),
                      'D':str(D),'trace_upper_bound':str(sum(s)),'stability_slack':str(slack),
                      'Horn_min_slack':str(min(slacks))})
    assert set(given)==vertices
    extreme=given[(Q(7,12),Q(5,24),Q(1,2),Q(1,2))]
    a=tuple(map(Q,extreme['a']));b=tuple(map(Q,extreme['b']))
    assert sum(max(u,v) for u,v in zip(a,b))==Q(31,24)
    assert Q(extreme['D'])/(2-Q(extreme['cost']))==Q(36,17)
    report={'status':'PASS','arithmetic':'fractions.Fraction; no floating point',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'cell_count':8,'active_sets_examined':8*330,'unique_vertices':22,
            'Horn_counts':counts,'Horn_checks':22*sum(counts),
            'optimal_forward_coefficient':'17/36','extremal_cost':'31/24',
            'cells':cells,'witnesses':proof}
    (ROOT/'balanced_three_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items() if k not in ('cells','witnesses')})

if __name__=='__main__':main()

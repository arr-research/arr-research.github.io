"""Independent N4 review: explicit cell vertices/edges and LR tableaux.
Does not import author's geometry or recursive Horn generator. Read-only
towards author certificates; writes only independent review report.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations,product
from math import lcm,comb
from pathlib import Path
import hashlib,json,time
ROOT=Path(__file__).resolve().parent

def E(a):return 2*(1-a[0])
def U(a):return sum(abs(x-Q(1,len(a))) for x in a)
def q(a):return E(a)-U(a)
def distance(a,b):return min(E(a)+U(b),U(a)+E(b))
def explicit_geometry(n):
    u=(Q(1,n),)*n
    vs={(k,l):(Q(n-l+k,n*k),)*k+(Q(1,n),)*(l-k)+(Q(0),)*(n-l)
        for k in range(1,n) for l in range(k,n)}
    edge=lambda a,b:tuple(sorted((a,b)))
    edges={edge(u,v) for v in vs.values()}
    for (k,l),(h,j) in combinations(vs,2):
        if k==h or l==j:edges.add(edge(vs[k,l],vs[h,j]))
    base=sorted({u}|set(vs.values()))
    assert len(base)==1+comb(n,2)
    assert len(edges)==n*(n-1)*(2*n-1)//6
    vertices=set(product(base,repeat=2));cuts=[]
    for fixed,(a,b) in product(base,sorted(edges)):
        qa,qb=q(a),q(b);target=q(fixed)
        if min(qa,qb)<target<max(qa,qb):
            t=(target-qa)/(qb-qa)
            x=tuple((1-t)*aa+t*bb for aa,bb in zip(a,b))
            assert q(x)==target
            vertices.update([(fixed,x),(x,fixed)])
            cuts.append(dict(fixed=fixed,edge=(a,b),t=t,point=x))
    return base,edges,vertices,cuts

@lru_cache(None)
def lr(left,content,outer):
    """Count semistandard lattice-word skew tableaux in reading order."""
    r=len(outer)
    if sum(left)+sum(content)!=sum(outer) or any(a>c for a,c in zip(left,outer)):return 0
    cells=[(i,j) for i in range(r) for j in range(outer[i]-1,left[i]-1,-1)]
    assigned={};used=[0]*r
    def fill(pos):
        if pos==len(cells):return int(tuple(used)==content)
        i,j=cells[pos];count=0
        for symbol in range(r):
            if used[symbol]>=content[symbol]:continue
            if (i,j+1) in assigned and symbol>assigned[i,j+1]:continue
            if (i-1,j) in assigned and symbol<=assigned[i-1,j]:continue
            used[symbol]+=1
            if all(used[k]>=used[k+1] for k in range(r-1)):
                assigned[i,j]=symbol;count+=fill(pos+1);del assigned[i,j]
            used[symbol]-=1
        return count
    return fill(0)

def partition(subset):return tuple(value-position for value,position in zip(reversed(subset),range(len(subset),0,-1)))
def lr_triples(d):
    allrows=[];counts=[];hist={}
    for r in range(1,d):
        subs=list(combinations(range(1,d+1),r));by_sum={}
        for K in subs:by_sum.setdefault(sum(K),[]).append(K)
        rows=[]
        for I,J in product(subs,repeat=2):
            for K in by_sum.get(sum(I)+sum(J)-r*(r+1)//2,[]):
                c=lr(partition(I),partition(J),partition(K))
                if c:
                    rows.append((I,J,K));hist[c]=hist.get(c,0)+1
        allrows.extend(rows);counts.append(len(rows))
        print('LR',r,len(rows),flush=True)
    return allrows,counts,hist

def main():
    started=time.monotonic();report=dict(status='STARTED',method='Independent explicit geometry and Littlewood-Richardson tableaux; no import of author generator')
    report_path=ROOT/'independent_lr_geometry_review.json';report_path.write_text(json.dumps(report,indent=2)+'\n')
    base,edges,vertices,cuts=explicit_geometry(4)
    original=json.loads((ROOT/'balanced_four_certificate.json').read_text())
    author_vertices={(tuple(map(Q,x['a'])),tuple(map(Q,x['b']))) for x in original['witnesses']}
    assert vertices==author_vertices and len(vertices)==89
    triples,counts,hist=lr_triples(8)
    stored=json.loads((ROOT/'horn_8.json').read_text())
    author_horn={tuple(tuple(x) for x in row) for row in stored}
    assert set(triples)==author_horn
    assert len(triples)==8752 and counts==[36,462,2120,3516,2120,462,36]
    checkrows=[]
    for row in original['witnesses']:
        a,b,s=(tuple(map(Q,row[k])) for k in ['a','b','s']);lam=a+tuple(-x for x in reversed(b))
        assert list(s)==sorted(s,reverse=True) and min(s)>=0 and len(s)==8
        assert sum(a)==sum(b)==1
        d=lcm(*(v.denominator for v in s+lam))
        si=[int(v*d) for v in s];li=[int(v*d) for v in lam]
        minimum=min(sum(si[i-1] for i in I)-sum(si[8-j] for j in J)-sum(li[k-1] for k in K) for I,J,K in triples)
        assert minimum>=0
        D=distance(a,b);gap=Q(5,2)-sum(s)-Q(4,7)*D
        assert D==Q(row['D']) and gap>=0 and gap==Q(row['stability_slack'])
        checkrows.append(dict(a=a,b=b,Horn_min_slack=Q(minimum,d),stability_slack=gap))
    # Independently verify the all-dimension r=2 LR family in small examples;
    # general admissibility is supplied by the three symbolic inequalities.
    for d in range(4,15):assert lr(partition((1,3)),partition((1,d-1)),partition((2,d-1)))==1
    # Independent geometric formula counts, without exponential LP execution.
    geometry_counts=[]
    for n in range(2,9):
        v,e,cut,extra=explicit_geometry(n)
        assert len(cut)<=len(v)**2+2*len(v)*len(e)
        geometry_counts.append(dict(N=n,V=len(v),E=len(e),cut_product_vertices=len(cut),naive_bound=len(v)**2+2*len(v)*len(e)))
    report.update(status='PASS',elapsed_seconds=time.monotonic()-started,coefficient='4/7',explicit_base_vertices=len(base),explicit_base_edges=len(edges),independent_product_cut_vertices=len(vertices),geometry_equals_author=True,LR_counts=counts,LR_triples=len(triples),LR_multiplicity_histogram=hist,LR_equals_recursive_author_rows=True,exact_witness_inequalities=len(vertices)*len(triples),witness_rows=checkrows,general_geometry_count_checks=geometry_counts,source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'balanced_four_certificate.json',ROOT/'horn_8.json']},limits=['Horn sufficiency imported, not proved by these checks.','General cell geometry, convexity and fixed-dimension sharpness require the analytic argument.','No independent novelty search; no Lean or proof-assistant replay.'])
    report_path.write_text(json.dumps(report,default=str,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ['witness_rows','source_hashes','limits']},indent=2))
if __name__=='__main__':main()

"""Exact positive rank-two witnesses for a finite atlas; author-side checks."""
from pathlib import Path
from fractions import Fraction
import itertools,json,math,time,hashlib
import networkx as nx
import sympy as sp
R=Path(__file__).parent

def integer_kernel(G,h,ell):
    a,b=abs(ell.numerator),ell.denominator;tn,td=a*a,b*b
    q=h+2;emax=h*(h-1)//2;B=[[0]*q for _ in range(q)]
    for S0 in itertools.combinations(list(G),h):
        S=set(S0);rem=[v for v in G if v not in S]
        p={v:sum(G.has_edge(u,v) for u in S) for v in rem}
        nu=[sum(r==j for r in p.values()) for j in range(q)]
        e=sum(u in S and v in S for u,v in G.edges())
        weight=(td-tn)**e*td**(emax-e)
        for i in range(q):
            for j in range(q):B[i][j]+=weight*tn*(nu[i]*nu[j]-(nu[i] if i==j else 0))
        for u,v in G.edges():
            if u in p and v in p:
                c,d=p[u],p[v]
                for i,j,sg in [(c,d,1),(c+1,d,-1),(c,d+1,-1),(c+1,d+1,1)]:
                    B[i][j]-=weight*td*sg;B[j][i]-=weight*td*sg
    return sp.Matrix(B),td**(emax+1)

def inertia(M):
    A=M.copy();counts=[0,0,0];blocks=[]
    while A.rows:
        diag=next((i for i in range(A.rows) if A[i,i]!=0),None)
        if diag is not None:
            ix=[diag]+[i for i in range(A.rows) if i!=diag];A=A.extract(ix,ix)
            p=A[0,0];counts[0 if p>0 else 1]+=1
            blocks.append(dict(size=1,index=diag,pivot=str(p)))
            A=A[1:,1:]-A[1:,0:1]*A[0:1,1:]/p
        else:
            pair=next(((i,j) for i in range(A.rows) for j in range(i+1,A.rows) if A[i,j]),None)
            if pair is None:
                counts[2]+=A.rows;blocks.append(dict(size=A.rows,zero_block=True));break
            ix=list(pair)+[i for i in range(A.rows) if i not in pair];A=A.extract(ix,ix)
            P=A[:2,:2];counts[0]+=1;counts[1]+=1
            blocks.append(dict(size=2,indices=list(pair),matrix=[[str(v) for v in row] for row in P.tolist()]))
            A=A[2:,2:]-A[2:,:2]*P.inv()*A[:2,2:]
    return counts,blocks

def direct_hessian(G,h,ell):
    n=len(G);q=h+2
    aa=[sp.Rational(ell.numerator,ell.denominator),sp.Integer(0)]+[sp.Rational(i-1,q) for i in range(2,q)]
    target=sp.Matrix(q,q,lambda i,j:1-aa[i]*aa[j]);den=int(sp.ilcm(*(sp.denom(v) for v in target)))
    T=[[int(v*den) for v in row] for row in target.tolist()]
    edges=list(G.edges());nodes=list(G);beta=[h,n-h-2]+[0]*h;coeffs={}
    def coefficient(ex):
        if ex in coeffs:return coeffs[ex]
        colours={}
        def count(rem,i):
            if i==q-1:
                for v in rem:colours[v]=i
                return math.prod(T[colours[u]][colours[v]] for u,v in edges)
            result=0
            for selected in itertools.combinations(rem,ex[i]):
                selected=set(selected)
                for v in selected:colours[v]=i
                result+=count([v for v in rem if v not in selected],i+1)
            return result
        coeffs[ex]=count(nodes,0);return coeffs[ex]
    M=sp.zeros(q)
    for i in range(q):
        for j in range(i,q):
            ex=beta.copy();ex[i]+=1;ex[j]+=1;ex=tuple(ex)
            v=sp.Rational(coefficient(ex)*math.prod(math.factorial(e) for e in ex),den**len(edges))
            M[i,j]=M[j,i]=v
    U=sp.Matrix([[ (1-aa[0]*x)**r for r in range(q)] for x in aa])
    assert U.det()!=0
    return M,U,aa,target

screen=json.loads((R/'profile-hierarchy-screen.json').read_text())
started=time.time();rows=[]
ells=[Fraction(-999,1000),Fraction(-99,100),Fraction(-7,8),Fraction(-7,10),Fraction(-1,2),Fraction(-1,5),Fraction(-7,100)]
for source in screen['rows']:
    if source['complete']:continue
    G=nx.Graph();G.add_nodes_from(range(source['n']));G.add_edges_from(source['edges'])
    h=source['detected']['h'];selected=None
    order=sorted(ells,key=lambda e:abs(float(e*e)-source['detected']['t']))
    for ell in order:
        B,den=integer_kernel(G,h,ell);ins,blocks=inertia(B)
        if ins[0]>=2:selected=(ell,B,den,ins,blocks);break
    assert selected is not None,source
    ell,B,den,ins,blocks=selected
    M,U,aa,target=direct_hessian(G,h,ell)
    factor=sp.Rational(math.factorial(h)*math.factorial(len(G)-h-2),den)/(sp.Rational(ell.numerator,ell.denominator)**2)
    assert M==factor*U*B*U.T,(source['atlas_index'],h,ell)
    assert min(target)>0 and target.rank()==2
    rows.append(dict(atlas_index=source['atlas_index'],n=len(G),edges=source['edges'],h=h,ell=str(ell),target_parameters=list(map(str,aa)),integer_kernel=[[str(v) for v in row] for row in B.tolist()],positive_scale_denominator=str(den),inertia=ins,congruence_blocks=blocks,direct_partition_identity=True))
    if len(rows)%100==0:print(json.dumps(dict(checked=len(rows),seconds=round(time.time()-started,1))),flush=True)
out=dict(status='PASS_EXACT_FINITE_CENSUS',graphs=len(rows),orders=[3,4,5,6,7],description='Every connected noncomplete graph of orders three through seven in NetworkX graph atlas has a strictly positive rank-two antiferromagnetic normalized target and an exactly certified quadratic derivative with at least two positive eigenvalues.',proof_link='The profile-basis kernel is congruent to the conditioned-set Hessian identity in the current draft; every listed case was also checked directly by enumeration of partition coefficients.',direct_partition_identity_checks=len(rows),rows=rows,limits='Finite census only, author context; no proof for arbitrary order, priority claim, independent review, or score.')
(R/'profile-hierarchy-exact.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],graphs=len(rows),direct_checks=len(rows),seconds=round(time.time()-started,1))),flush=True)
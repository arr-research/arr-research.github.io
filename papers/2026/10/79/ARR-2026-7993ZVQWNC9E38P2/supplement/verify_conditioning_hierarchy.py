"""Exact checks of the general conditioned-set identity, author context."""
from pathlib import Path
import json,itertools,math
import networkx as nx
import sympy as sp
R=Path(__file__).parent
def conditioned_kernel(G,h,s):
    ell=(s-1)/(s+1);q=h+2
    F=sp.Matrix(q,h+1,lambda j,r:sp.binomial(r,j)*(-ell)**j)
    JF=sp.zeros(q,h+1)
    JF[1:,:]=F[:-1,:]
    B=sp.zeros(q)
    for tup in itertools.combinations(list(G),h):
        S=set(tup);rem=[v for v in G if v not in S]
        r={v:sum(G.has_edge(v,u) for u in S) for v in rem}
        nu=sp.Matrix([list(r.values()).count(j) for j in range(h+1)])
        C=sp.zeros(h+1)
        for u,v in G.edges():
            if u in r and v in r:C[r[u],r[v]]+=1;C[r[v],r[u]]+=1
        e=G.subgraph(S).number_of_edges()
        B+=(1-ell**2)**e*(F*(nu*nu.T-sp.diag(*nu))*F.T-JF*C*JF.T)
    return B

def exact_hessian(G,h,s,normalized=False):
    N=len(G);q=h+2;beta=[h,N-h-2]+[0]*h
    t=[s]+list(map(sp.Integer,range(1,h+2)))
    kval=[(v-1)/(v+1) for v in t]
    target=sp.Matrix(q,q,lambda i,j:1-kval[i]*kval[j] if normalized else t[i]+t[j])
    denominator=int(sp.ilcm(*(sp.denom(v) for v in target)))
    target=target*denominator
    wanted={}
    for i in range(q):
        for j in range(q):
            ex=beta.copy();ex[i]+=1;ex[j]+=1
            wanted[tuple(ex)]=math.prod(math.factorial(v) for v in ex)
    coefficients={}
    for ex in wanted:
        def assignments(rem,j,current):
            if j==q-1:
                yield {**current,**{v:j for v in rem}}
                return
            for selected in itertools.combinations(rem,ex[j]):
                selected=set(selected)
                yield from assignments([v for v in rem if v not in selected],j+1,{**current,**{v:j for v in selected}})
        coefficients[ex]=sum(math.prod(int(target[c[u],c[v]]) for u,v in G.edges()) for c in assignments(list(G),0,{}))
    M=sp.zeros(q)
    for i in range(q):
        for j in range(q):
            ex=beta.copy();ex[i]+=1;ex[j]+=1;ex=tuple(ex)
            M[i,j]=sp.Rational(coefficients[ex]*wanted[ex],denominator**G.number_of_edges())
    return M

Gswap=nx.disjoint_union(nx.complete_graph(4),nx.complete_graph(4))
Gswap.remove_edges_from([(0,1),(4,5)]);Gswap.add_edges_from([(0,4),(1,5)])
graphs=[nx.cycle_graph(4),nx.complete_graph(4),nx.cycle_graph(5),nx.cycle_graph(6),nx.complete_bipartite_graph(3,3),Gswap]
checks=[]
for G in graphs:
    N=len(G);d=G.degree(0);m=G.number_of_edges()
    for h in [1,2]+([3] if N==5 else []):
        for s in [sp.Rational(1,3),sp.Rational(1,100)]:
            B=conditioned_kernel(G,h,s)
            t=[s]+list(map(sp.Integer,range(1,h+2)));z=[(v+1)/2 for v in t];k=[(v-1)/(v+1) for v in t]
            V=sp.Matrix([[v**j for j in range(h+2)] for v in k]);Z=sp.diag(*(v**d for v in z))
            scale=math.factorial(h)*math.factorial(N-h-2)*sp.Integer(2)**(m-h*d)*(s+1)**(h*d)
            M=exact_hessian(G,h,s)
            assert M==scale*Z*V*B*V.T*Z,(N,d,h,s)
            checks.append(dict(n=N,d=d,h=h,s=str(s),edges=list(G.edges()),identity_exact=True))

B0=conditioned_kernel(Gswap,2,sp.Integer(0))
assert B0==sp.Matrix([[480,480,60,0],[480,264,-120,-12],[60,-120,-148,-16],[0,-12,-16,-4]])
pivots=[];A=B0
for i in range(4):
    a=A[0,0];pivots.append(str(a));A=A[1:,1:]-A[1:,0:1]*A[0:1,1:]/a
assert pivots==['480','-216','-11/2','106/33']
Bpositive=conditioned_kernel(Gswap,2,sp.Rational(1,100));A=Bpositive;positive_pivots=[]
for i in range(4):
    a=A[0,0];positive_pivots.append(str(a));A=A[1:,1:]-A[1:,0:1]*A[0:1,1:]/a
assert sum(bool(sp.Rational(v)>0) for v in positive_pivots)==2
normalized_checks=[]
extra=[nx.path_graph(5),nx.star_graph(4),nx.Graph([(0,1),(1,2),(2,0),(2,3)]),nx.empty_graph(5)]
for G in graphs+extra:
    N=len(G)
    for h in [1,2]+([3] if N==5 else []):
        s=sp.Rational(1,3);B=conditioned_kernel(G,h,s)
        t=[s]+list(map(sp.Integer,range(1,h+2)));a=[(v-1)/(v+1) for v in t]
        V=sp.Matrix([[v**j for j in range(h+2)] for v in a])
        M=exact_hessian(G,h,s,normalized=True)
        assert M==math.factorial(h)*math.factorial(N-h-2)*V*B*V.T,(N,h,list(G.edges()))
        normalized_checks.append(dict(n=N,h=h,s=str(s),edges=list(G.edges()),identity_exact=True,regular=len(set(dict(G.degree()).values()))==1))
out=dict(status='PASS_EXACT',identity_checks=len(checks),checks=checks,
     normalized_arbitrary_graph_identity_checks=len(normalized_checks),normalized_checks=normalized_checks,
     positive_swap_example=dict(n=8,d=3,triangles=4,s='1/100',h=2,kernel=[[str(v) for v in row] for row in Bpositive.tolist()],pivots=positive_pivots,inertia=[2,2,0]),
     boundary_swap_example=dict(s='0',kernel=B0.tolist(),pivots=pivots,inertia=[2,2,0]),
     limits='Author-side exact finite checks and symbolic construction; no independent review or proof of the full characterization conjecture.')
(R/'conditioning-hierarchy-checks.json').write_text(json.dumps(out,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps(dict(status=out['status'],identity_checks=len(checks),normalized_arbitrary_graph_identity_checks=len(normalized_checks),positive_swap_inertia=[2,2,0])))

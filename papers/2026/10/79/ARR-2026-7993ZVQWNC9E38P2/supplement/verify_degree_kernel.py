"""Exact author checks of the degree-kernel identity and compression certificate."""
from pathlib import Path
from collections import Counter,defaultdict
import itertools,math,json
import networkx as nx
import sympy as sp
R=Path(__file__).parent
def kernel(G):
    deg=dict(G.degree());D=max(deg.values());n=len(G)
    counts=Counter(deg.values());nv=sp.Matrix([counts[r] for r in range(D+1)])
    C=sp.zeros(D,D)
    for u,v in G.edges():C[deg[u]-1,deg[v]-1]+=1;C[deg[v]-1,deg[u]-1]+=1
    L=sp.zeros(D+1,D)
    for r in range(1,D+1):L[r,r-1]=1;L[r-1,r-1]=-1
    return nv*nv.T-sp.diag(*nv)-L*C*L.T
identity=[];compressions=[]
graphs=[G for G in nx.graph_atlas_g() if 3<=len(G)<=7 and nx.is_connected(G)]
for G in graphs:
    N=len(G);degrees=dict(G.degree());D=max(degrees.values());delta=min(degrees.values());B=kernel(G)
    low=[v for v in G if degrees[v]==delta]
    if G.subgraph(low).number_of_edges()==0:
        p=sp.ones(D+1,1);u=sp.zeros(D+1,1);u[delta-1]=1;w=B*u;U=sp.Matrix.hstack(p,u,w);Q=U.T*B*U
        assert Q[0,0]==N*(N-1) and Q[0,1]==0 and Q[1,1]==0 and Q[1,2]>0
        assert Q.det()==-Q[0,0]*Q[1,2]**2<0
        compressions.append(dict(n=N,edges=list(G.edges()),minimum_degree=delta,compression=[[str(v) for v in row] for row in Q.tolist()],determinant=str(Q.det())))
    if N>5:continue
    q=D+1;t=list(range(q));z=[sp.Rational(i+1,2) for i in t]
    V=sp.Matrix([[a**r for r in range(q)] for a in z]);beta=[0]*q;beta[1]=N-2
    wanted={}
    for i in range(q):
        for j in range(q):
            a=beta.copy();a[i]+=1;a[j]+=1;wanted[tuple(a)]=math.prod(math.factorial(v) for v in a)
    coeff=defaultdict(int)
    for a in itertools.product(t,repeat=N):
        exp=tuple(a.count(i) for i in t)
        if exp in wanted:coeff[exp]+=math.prod(a[u]+a[v] for u,v in G.edges())
    M=sp.zeros(q)
    for i in range(q):
        for j in range(q):
            a=beta.copy();a[i]+=1;a[j]+=1;a=tuple(a);M[i,j]=coeff[a]*wanted[a]
    assert M==math.factorial(N-2)*2**G.number_of_edges()*V*B*V.T
    identity.append(dict(n=N,edges=list(G.edges()),spins=q,identity_exact=True))
out=dict(status='PASS_EXACT',identity_graphs=len(identity),compression_graphs=len(compressions),identity_checks=identity,compression_certificates=compressions,limits='Finite exact checks corroborate the written general counting and linear-algebra arguments. No formal proof assistant, novelty certification, or Astra assessment.')
(R/'degree-kernel-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='PASS_EXACT',identity_graphs=len(identity),compression_graphs=len(compressions))))

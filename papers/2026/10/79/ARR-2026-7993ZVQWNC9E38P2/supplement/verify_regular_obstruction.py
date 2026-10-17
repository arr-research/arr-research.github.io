"""Exact verification of the proposed partial-lemma identity, not a general proof."""
from pathlib import Path
from collections import defaultdict
import itertools,json,math
import networkx as nx
import sympy as sp
R=Path(__file__).parent
t=[0,1,2];H=sp.Matrix([[a+b for b in t] for a in t])
k=[sp.Rational(a-1,a+1) for a in t];z=[sp.Rational(a+1,2) for a in t]
V=sp.Matrix([[1,a,a*a] for a in k])
n,d,tau=sp.symbols('n d tau')
B=sp.Matrix([[(n-1)*(n-2),d*(n-2),0],[d*(n-2),d*(d-n+1),-d*(d-1)],[0,-d*(d-1),-tau]])
assert sp.factor(B.det()-d*(n-2)*(tau*((n-1)**2-d)-(n-1)*d*(d-1)**2))==0
graphs=[]
for G in nx.graph_atlas_g():
    if 3<=len(G)<=6 and nx.is_connected(G) and len(set(dict(G.degree()).values()))==1:graphs.append(G)
graphs += [nx.cycle_graph(7),nx.cubical_graph(),nx.petersen_graph()]
rows=[]
for G in graphs:
    N=len(G);D=G.degree(0);m=G.number_of_edges();T=sum(nx.triangles(G).values())//3
    beta=(1,N-3,0);wanted=set()
    for i in range(3):
        for j in range(3):
            a=list(beta);a[i]+=1;a[j]+=1;wanted.add(tuple(a))
    coeff=defaultdict(int)
    for a in itertools.product(range(3),repeat=N):
        exp=tuple(a.count(i) for i in range(3))
        if exp not in wanted:continue
        coeff[exp]+=math.prod(int(H[a[u],a[v]]) for u,v in G.edges())
    M=sp.zeros(3)
    for i in range(3):
        for j in range(3):
            a=list(beta);a[i]+=1;a[j]+=1
            M[i,j]=coeff[tuple(a)]*math.prod(math.factorial(v) for v in a)
    b=B.subs({n:N,d:D,tau:sp.Rational(6*T,N)})
    Z=sp.diag(*(v**D for v in z))
    predicted=math.factorial(N-3)*2**(m-D)*N*Z*V*b*V.T*Z
    assert M==predicted,(N,D,T,M,predicted)
    det=int(M.det());condition=(sp.Rational(6*T,N)*((N-1)**2-D)<(N-1)*D*(D-1)**2 and D>=2)
    if condition:assert det<0
    rows.append(dict(n=N,d=D,triangles=T,edges=list(G.edges()),identity_exact=True,sufficient_condition=bool(condition),hessian_determinant=str(det)))
out=dict(status='PASS_EXACT',symbolic_determinant_identity=True,graphs=len(rows),enumerated_identity_checks=rows,limitations='Finite enumeration verifies the formula on these graphs; the written counting argument is the proposed general proof. No novelty audit completed and no Astra review.')
(R/'regular-obstruction-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='PASS_EXACT',graphs=len(rows),symbolic_identity=True)))

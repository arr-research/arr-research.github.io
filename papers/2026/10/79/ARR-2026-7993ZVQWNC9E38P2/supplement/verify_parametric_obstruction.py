"""Exact author-side checks of a parametric extension; no external review."""
from pathlib import Path
from collections import defaultdict, Counter
import itertools, json, math
import networkx as nx
import sympy as sp

R = Path(__file__).parent
n, d, tau, ell = sp.symbols('n d tau ell')
B = sp.Matrix([[(n-1)*(n-2), -ell*d*(n-2), 0],
               [-ell*d*(n-2), ell**2*d*(d-1)-d*(n-2), ell*d*(d-1)],
               [0, ell*d*(d-1), -ell**2*tau]])
expected = ell**2*d*(n-2)*((n-1)*((n-2)*tau-d*(d-1)**2)+ell**2*tau*(n-1-d))
assert sp.expand(B.det()-expected) == 0

def enumerated_hessian(G, t, beta):
    q=len(t); N=len(G); wanted={}
    for i in range(q):
        for j in range(q):
            a=list(beta); a[i]+=1; a[j]+=1
            wanted[tuple(a)]=math.prod(math.factorial(v) for v in a)
    coeff=defaultdict(lambda: sp.Integer(0))
    # Enumerate only assignments with the requested multiplicities.
    # The previous scripts independently enumerate all q**N assignments.
    vertices=list(G)
    for exponents in wanted:
        def choices(remaining, spin, assignment):
            if spin==q-1:
                yield {**assignment, **{v:spin for v in remaining}}
                return
            for selected in itertools.combinations(remaining,exponents[spin]):
                selected=set(selected)
                yield from choices([v for v in remaining if v not in selected],spin+1,
                                   {**assignment, **{v:spin for v in selected}})
        for a in choices(vertices,0,{}):
            coeff[exponents] += math.prod(t[a[u]]+t[a[v]] for u,v in G.edges())
    M=sp.zeros(q)
    for i in range(q):
        for j in range(q):
            a=list(beta);a[i]+=1;a[j]+=1;a=tuple(a)
            M[i,j]=coeff[a]*wanted[a]
    return M

regular=[G for G in nx.graph_atlas_g() if 3<=len(G)<=7 and nx.is_connected(G)
         and len(set(dict(G.degree()).values()))==1]
regular += [nx.cubical_graph(), nx.petersen_graph(), nx.complete_bipartite_graph(4,4)]
strict_extension=nx.Graph([(0,1),(0,2),(0,8),(0,9),(1,4),(1,7),(1,9),
 (2,5),(2,8),(2,11),(3,6),(3,7),(3,8),(3,11),(4,5),(4,7),(4,10),
 (5,6),(5,9),(6,10),(6,11),(7,10),(8,9),(10,11)])
assert nx.is_connected(strict_extension) and set(dict(strict_extension.degree()).values())=={4}
assert sum(nx.triangles(strict_extension).values())//3==7
regular.append(strict_extension)
rows=[]
for G in regular:
    N=len(G);D=G.degree(0);m=G.number_of_edges();T=sum(nx.triangles(G).values())//3
    tt=sp.Rational(6*T,N)
    for s in [sp.Rational(1,3),sp.Rational(1,2),sp.Rational(3,2),sp.Integer(3),sp.Rational(2,3)]:
        t=[s,sp.Integer(1),sp.Integer(2)]
        kval=[(v-1)/(v+1) for v in t];z=[(v+1)/2 for v in t]
        lam=(s-1)/(s+1)
        V=sp.Matrix([[1,k,k*k] for k in kval]);Z=sp.diag(*(v**D for v in z))
        b=B.subs({n:N,d:D,tau:tt,ell:lam})
        M=enumerated_hessian(G,t,(1,N-3,0))
        predicted=math.factorial(N-3)*2**(m-D)*(s+1)**D*N*Z*V*b*V.T*Z
        assert M==predicted,(N,D,T,s)
        rows.append(dict(n=N,d=D,triangles=T,s=str(s),identity_exact=True,
                         kernel_determinant=str(b.det()),hessian_determinant=str(M.det())))

degree_checks=[]
for G in nx.graph_atlas_g():
    if not(3<=len(G)<=5 and nx.is_connected(G)):continue
    N=len(G);degrees=dict(G.degree());D=max(degrees.values());q=D+1
    counts=Counter(degrees.values());nv=sp.Matrix([counts[r] for r in range(q)])
    C=sp.zeros(D,D);L=sp.zeros(q,D)
    for u,v in G.edges():C[degrees[u]-1,degrees[v]-1]+=1;C[degrees[v]-1,degrees[u]-1]+=1
    for r in range(1,q):L[r,r-1]=1;L[r-1,r-1]=-1
    K=nv*nv.T-sp.diag(*nv)-L*C*L.T
    t=list(map(sp.Integer,range(1,q+1)));z=[(a+1)/2 for a in t]
    V=sp.Matrix([[a**r for r in range(q)] for a in z])
    M=enumerated_hessian(G,t,[N-2]+[0]*(q-1))
    assert M==math.factorial(N-2)*2**G.number_of_edges()*V*K*V.T
    degree_checks.append(dict(n=N,edges=list(G.edges()),positive_target=True,identity_exact=True))

selection=[]
for G in regular:
    N=len(G);D=G.degree(0);T=sum(nx.triangles(G).values())//3;tt=sp.Rational(6*T,N)
    margin=(N-1)*(D*(D-1)**2-(N-2)*tt)
    if margin<=0:continue
    correction=tt*(N-1-D);k=2+sp.ceiling(correction/margin);lam=-sp.Rational(1,k)
    assert B.subs({n:N,d:D,tau:tt,ell:lam}).det()<0
    selection.append(dict(n=N,d=D,triangles=T,k=int(k),s=str((k-1)/(k+1))))

assert B.subs({n:12,d:4,tau:sp.Rational(7,2),ell:-1}).det()==540
assert B.subs({n:12,d:4,tau:sp.Rational(7,2),ell:sp.Rational(-1,5)}).det()==-sp.Rational(2004,125)

out=dict(status='PASS_EXACT',symbolic_identity=True,regular_graphs=len(regular),
         regular_parameter_identity_checks=len(rows),positive_degree_kernel_checks=len(degree_checks),
         regular_checks=rows,degree_checks=degree_checks,rational_selection_checks=selection,
         limits='Author-side finite rational checks, not a proof assistant or independent Astra review.')
(R/'parametric-obstruction-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if not isinstance(v,list)}))

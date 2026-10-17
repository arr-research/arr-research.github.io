"""Exact arbitrary-graph checks for the normalized rank-two target."""
from pathlib import Path
from collections import defaultdict
import math,itertools,json
import networkx as nx
import sympy as sp
R=Path(__file__).parent
N,E,W,U,l=sp.symbols('N E W U l')
B=sp.Matrix([[N,-l*E,0],[-l*E,l*l*W-E,l*W],[0,l*W,-l*l*U]])
assert sp.expand(B.det()-l*l*(N*(E*U-W*W)+l*l*U*(E*E-N*W)))==0
graphs=[G for G in nx.graph_atlas_g() if 3<=len(G)<=6 and nx.is_connected(G)]
graphs += [nx.empty_graph(4),nx.Graph([(0,1),(2,3)]),nx.disjoint_union(nx.path_graph(3),nx.empty_graph(2))]
rows=[]
for G in graphs:
    n=len(G);m=G.number_of_edges();ww=sum(d*(d-1) for _,d in G.degree());uu=sum(nx.triangles(G).values())*2
    nn=n*(n-1)*(n-2);ee=2*m*(n-2)
    for lam in [sp.Rational(-1,2),sp.Rational(-1,3)]:
        a=[lam,sp.Integer(0),sp.Rational(1,2)]
        K=sp.ones(3)-sp.Matrix(a)*sp.Matrix(a).T
        denominator=sp.ilcm(*(sp.denom(x) for x in K));H=K*denominator
        beta=(1,n-3,0);wanted={}
        for i in range(3):
            for j in range(3):
                e=list(beta);e[i]+=1;e[j]+=1;wanted[tuple(e)]=math.prod(math.factorial(v) for v in e)
        coeff=defaultdict(int)
        for assignment in itertools.product(range(3),repeat=n):
            expo=tuple(assignment.count(i) for i in range(3))
            if expo in wanted:
                coeff[expo]+=math.prod(int(H[assignment[v],assignment[w]]) for v,w in G.edges())
        M=sp.zeros(3)
        for i in range(3):
            for j in range(3):
                e=list(beta);e[i]+=1;e[j]+=1;e=tuple(e)
                M[i,j]=sp.Rational(coeff[e]*wanted[e],denominator**m)
        V=sp.Matrix([[1,x,x*x] for x in a]);bb=B.subs({N:nn,E:ee,W:ww,U:uu,l:lam})
        assert M==math.factorial(n-3)*V*bb*V.T,(n,m,lam)
        if uu==0 and ww>0:assert M.det()<0
        rows.append(dict(n=n,m=m,edges=list(G.edges()),wedges_ordered=ww,triangles=uu//6,
             lam=str(lam),identity_exact=True,determinant=str(M.det()),triangle_free_obstruction=(uu==0 and ww>0)))
Kstar=sp.Matrix([[3,4,5],[4,4,4],[5,4,3]])/4
assert Kstar.eigenvals()=={sp.Integer(3):1,sp.Rational(-1,2):1,sp.Integer(0):1}
out=dict(status='PASS_EXACT',source_graphs=len(graphs),identity_checks=len(rows),symbolic_determinant=True,
 fixed_target_eigenvalues=['3','-1/2','0'],checks=rows,
 limits='Finite corroboration of a general counting proof; not a formal proof assistant, priority certificate or independent review.')
(R/'normalized-target-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=out['status'],source_graphs=len(graphs),identity_checks=len(rows))))

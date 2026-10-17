"""Exact checks of the proposed independent-neighbourhood-gap obstruction."""
from pathlib import Path
import ast,json,itertools,math,time
from fractions import Fraction
import networkx as nx
import sympy as sp
R=Path(__file__).parent
module=ast.parse((R/'certify_profile_hierarchy.py').read_text())
exec(compile(ast.Module(body=[n for n in module.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'certify_profile_hierarchy_functions','exec'))

def alpha(G,vertices):
    vv=list(vertices)
    for k in range(len(vv),-1,-1):
        for sub in itertools.combinations(vv,k):
            if all(not G.has_edge(u,v) for u,v in itertools.combinations(sub,2)):return k

def gap_data(G):
    Ns={u:set(G.neighbors(u)) for u in G}
    c=max((alpha(G,Ns[u]&Ns[v]) for u,v in G.edges()),default=0)
    b=max((alpha(G,Ns[u]-{v}) for u in G for v in Ns[u]),default=0)
    return b,c

rows=[];diamond_rows=[];start=time.time()
for idx,G in enumerate(nx.graph_atlas_g()):
    if len(G)<3 or not nx.is_connected(G) or G.number_of_edges()==len(G)*(len(G)-1)//2:continue
    b,c=gap_data(G)
    diamond_free=not any(G.subgraph(S).number_of_edges()==5 for S in itertools.combinations(G,4))
    triangle_free=sum(nx.triangles(G).values())==0
    if diamond_free:assert triangle_free or b>c,(idx,b,c)
    if b<=c:continue
    h=c+1;B,den=integer_kernel(G,h,Fraction(-1));assert den==1
    q=h+2;p=sp.ones(q,1);u=sp.eye(q)[:,q-1];w=B*u
    assert (u.T*B*u)[0]==0 and (p.T*B*u)[0]==0 and w!=sp.zeros(q,1)
    P=sp.Matrix.hstack(p,u,w);Q=P.T*B*P;a=(p.T*B*p)[0];cc=(w.T*w)[0]
    assert a>0 and cc>0 and Q.det()==-a*cc**2<0
    ins,blocks=inertia(B);assert ins[0]>=2
    positive=None
    for k in [10,100,1000,10000,100000]:
        ell=Fraction(1-k,k);Bp,d=integer_kernel(G,h,ell);ii,bb=inertia(Bp)
        if ii[0]>=2:
            positive=dict(ell=str(ell),inertia=ii);break
    assert positive,(idx,h)
    row=dict(atlas_index=idx,n=len(G),edges=list(G.edges()),b=b,c=c,h=h,boundary_inertia=ins,compression_a=str(a),compression_c=str(cc),compression_determinant=str(Q.det()),positive_witness=positive,diamond_free=diamond_free,triangle_free=triangle_free)
    rows.append(row)
    if diamond_free:diamond_rows.append(row)
out=dict(status='PASS_EXACT_BOUNDARY_COMPRESSION_AND_POSITIVE_CONTINUATION',gap_graphs=len(rows),diamond_free_covered_by_gap=len(diamond_rows),diamond_free_with_triangles=sum(not r['triangle_free'] for r in diamond_rows),rows=rows,limits='Finite corroboration of proposed general proof; author context, external assessment pending. The criterion b>c is sufficient, not asserted necessary.')
(R/'neighbourhood-gap-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],gap_graphs=len(rows),diamond_free_covered_by_gap=len(diamond_rows),diamond_free_with_triangles=out['diamond_free_with_triangles'],seconds=round(time.time()-start,1))))
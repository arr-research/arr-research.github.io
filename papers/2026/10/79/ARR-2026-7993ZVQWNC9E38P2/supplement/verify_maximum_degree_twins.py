"""Small-parameter profile obstruction: author-side proof corroboration."""
from pathlib import Path
from fractions import Fraction
import ast,itertools,json,math,time
import networkx as nx
import sympy as sp
R=Path(__file__).parent
raw=(R/'certify_profile_hierarchy.py').read_text();tree=ast.parse(raw)
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))

def edge_profiles(G,h):
    C=[[0]*(h+1) for _ in range(h+1)]
    for ss in itertools.combinations(list(G),h):
        S=set(ss);p={v:len(set(G[v])&S) for v in G if v not in S}
        for u,v in G.edges():
            if u in p and v in p:C[p[u]][p[v]]+=1;C[p[v]][p[u]]+=1
    return sp.Matrix(C)

def closed(G,v):return set(G[v])|{v}

def check(G,label,direct):
    n=len(G);delta=max(dict(G.degree()).values());h=delta-1;q=h+2
    assert nx.is_connected(G) and delta>=2 and h<=n-2
    twins=[(u,v) for u,v in G.edges() if G.degree(u)==delta and closed(G,u)==closed(G,v)]
    assert not twins
    C=edge_profiles(G,h);assert C[h,h]==0
    j=next(j for j in range(h) if C[h,j]>0)
    f=sp.zeros(h+1,1);f[j]=1;f[h]=-sp.Rational(C[j,j]+1,2*C[h,j])
    assert (f.T*C*f)[0]==-1
    D=sp.zeros(h+2,h+1)
    for r in range(h+1):D[r,r]=1;D[r+1,r]=-1
    y=sp.Matrix([sum(f[k] for k in range(r,h+1)) for r in range(h+2)])
    p=sp.ones(h+2,1);assert D.T*y==f
    Q0,d0=integer_kernel(G,h,Fraction(0))
    assert d0==1 and Q0==-D*C*D.T and (y.T*Q0*y)[0]==1 and Q0*p==sp.zeros(h+2,1)
    C0=math.comb(n,h)*(n-h)*(n-h-1);assert C0>0
    chosen=None
    for k in range(1,25):
        ell=Fraction(-1,2**k);Q,den=integer_kernel(G,h,ell)
        V=p.row_join(y);M=V.T*Q*V
        if M[0,0]>0 and M.det()>0:
            chosen=(ell,Q,den,M);break
    assert chosen is not None,label
    ell,Q,den,M=chosen
    ii,blocks=inertia(Q);assert ii[0]>=2
    if direct:
        H,U,aa,target=direct_hessian(G,h,ell)
        factor=sp.Rational(math.factorial(h)*math.factorial(n-h-2),den)/(sp.Rational(ell.numerator,ell.denominator)**2)
        assert H==factor*U*Q*U.T and min(target)>0 and target.rank()==2
    W=sum(d*(d-1) for _,d in G.degree());E=2*len(G.edges())*(n-2);UU=2*sum(nx.triangles(G).values())
    return dict(label=label,n=n,edges=list(G.edges()),maximum_degree=delta,h=h,spins=q,
        selected_profile=j,edge_profile_diagonal=0,negative_vector=list(map(str,f)),
        negative_quadratic_form='-1',leading_compression_coefficient=C0,ell=str(ell),
        inertia=ii,congruence_blocks=blocks,compression=[[str(v) for v in row] for row in M.tolist()],
        scale_denominator=str(den),direct_partition_identity=direct,
        edge_wedge_triangle_sufficient=W*W>E*UU,regular=len(set(dict(G.degree()).values()))==1)

start=time.time();rows=[];eligible=0
for ix,G in enumerate(nx.graph_atlas_g()):
    n=len(G)
    if n<3 or not nx.is_connected(G) or 2*len(G.edges())==n*(n-1):continue
    delta=max(dict(G.degree()).values())
    if any(G.degree(u)==delta and closed(G,u)==closed(G,v) for u,v in G.edges()):continue
    eligible+=1;rows.append(check(G,f'atlas-{ix}',True))
    if eligible%100==0:print(json.dumps(dict(checked=eligible,elapsed=round(time.time()-start,1))),flush=True)
for name,G,direct in [('wheel-8',nx.wheel_graph(8),True),('wheel-10',nx.wheel_graph(10),True),
    ('triangular-6',nx.convert_node_labels_to_integers(nx.line_graph(nx.complete_graph(6))),False),
    ('rook-4x4',nx.convert_node_labels_to_integers(nx.cartesian_product(nx.complete_graph(4),nx.complete_graph(4))),False)]:
    rows.append(check(G,name,direct));print(json.dumps(dict(extra=name,elapsed=round(time.time()-start,1))),flush=True)
out=dict(status='PASS_MAXIMUM_DEGREE_TWIN_CRITERION',atlas_eligible=eligible,exact_cases=len(rows),
    direct_positive_identities=sum(x['direct_partition_identity'] for x in rows),
    beyond_edge_wedge_triangle=sum(not x['edge_wedge_triangle_sufficient'] for x in rows),
    rows=rows,elapsed_seconds=round(time.time()-start,3),
    proof_scope='Connected noncliques whose maximum-degree vertices contain no adjacent true twins. In particular all graphs without true twins, all graphs with a unique maximum-degree vertex, and all connected noncomplete strongly regular graphs.',
    limits='General scope relies on the written small-parameter proof. Exact finite checks are author-side corroboration, not external review. No fixed finite target size for arbitrary degree or importance score is claimed.')
(R/'maximum-degree-twins-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

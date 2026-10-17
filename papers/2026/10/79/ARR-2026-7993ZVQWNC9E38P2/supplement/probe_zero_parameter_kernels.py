"""Exact local-type formula for unweighted profile edge kernels."""
from pathlib import Path
from fractions import Fraction
import ast,itertools,json,math,time,collections
import networkx as nx
import sympy as sp
R=Path(__file__).parent
tree=ast.parse((R/'certify_profile_hierarchy.py').read_text())
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))

def choose(n,k):return math.comb(n,k) if 0<=k<=n else 0

def local_kernel(G,h):
    n=len(G);types=collections.Counter()
    for u,v in G.edges():
        du,dv=sorted([G.degree(u),G.degree(v)])
        c=len(set(G[u])&set(G[v]));types[du,dv,c]+=1
    C=sp.zeros(h+1)
    for (du,dv,c),mult in types.items():
        a=du-1-c;b=dv-1-c;d=n-du-dv+c
        assert min(a,b,c,d)>=0
        for r in range(min(h,du-1)+1):
            for s in range(min(h,dv-1)+1):
                z=sum(choose(c,k)*choose(a,r-k)*choose(b,s-k)*choose(d,h-r-s+k) for k in range(min(r,s,c)+1))
                C[r,s]+=mult*z;C[s,r]+=mult*z
    return C

def blowup_cliques(G,s):
    H=nx.Graph();H.add_nodes_from((v,i) for v in G for i in range(s))
    for v in G:H.add_edges_from(((v,i),(v,j)) for i in range(s) for j in range(i))
    for u,v in G.edges():H.add_edges_from(((u,i),(v,j)) for i in range(s) for j in range(s))
    return nx.convert_node_labels_to_integers(H)

start=time.time();rows=[]
def inspect(G,label,compare=False):
    n=len(G);tests=[]
    for h in range(1,n-1):
        C=local_kernel(G,h);ins,blocks=inertia(C)
        if compare:
            Q0,_=integer_kernel(G,h,Fraction(0));D=sp.zeros(h+2,h+1)
            for j in range(h+1):D[j,j]=1;D[j+1,j]=-1
            assert Q0==-D*C*D.T,(label,h)
        tests.append(dict(h=h,inertia=ins))
        if ins[1]>0:break
    return dict(label=label,n=n,edges=list(G.edges()),tests=tests,detected=any(t['inertia'][1]>0 for t in tests),direct_kernel_comparison=compare)
for ix,G in enumerate(nx.graph_atlas_g()):
    if len(G)<3 or not nx.is_connected(G) or 2*len(G.edges())==len(G)*(len(G)-1):continue
    rows.append(inspect(G,f'atlas-{ix}',True))
print(json.dumps(dict(atlas_done=len(rows),misses=[x['label'] for x in rows if not x['detected']],elapsed=round(time.time()-start,1))),flush=True)
for base_name,G in [('cycle4',nx.cycle_graph(4)),('cycle5',nx.cycle_graph(5)),('cycle6',nx.cycle_graph(6)),('petersen',nx.petersen_graph())]:
    for s in [2,3,4]:
        rows.append(inspect(blowup_cliques(G,s),f'{base_name}-clique-blowup-{s}'))
        print(json.dumps(dict(extra=rows[-1]['label'],n=rows[-1]['n'],detected=rows[-1]['detected'],elapsed=round(time.time()-start,1))),flush=True)
out=dict(status='EXACT_ZERO_PARAMETER_PROBE',cases=len(rows),rows=rows,
    misses=[x['label'] for x in rows if not x['detected']],elapsed_seconds=round(time.time()-start,3),
    scope='Tests all h until an indefinite edge-profile kernel is found; if absent, every h was checked. The local formula depends only on endpoint degrees and common-neighbour counts. Finite evidence only; no universal claim.')
(R/'zero-parameter-kernels-probe.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

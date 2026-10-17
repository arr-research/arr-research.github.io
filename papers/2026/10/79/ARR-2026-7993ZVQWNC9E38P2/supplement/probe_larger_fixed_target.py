"""Seeded search for failure of the fixed four-spin target beyond the atlas."""
from pathlib import Path
from collections import defaultdict
import ast,itertools,json,math,time
import networkx as nx
import sympy as sp
R=Path(__file__).parent
def load_functions(name,selected=None):
    tree=ast.parse((R/name).read_text())
    ns=[x for x in tree.body if isinstance(x,ast.FunctionDef) and (selected is None or x.name in selected)]
    exec(compile(ast.Module(body=ns,type_ignores=[]),name,'exec'),globals())
load_functions('certify_profile_hierarchy.py',{'inertia'})
load_functions('probe_fixed_diamond_scope.py',{'comps','check'})
T=[[0,9,12,15],[9,9,9,9],[12,9,8,7],[15,9,7,5]]
cases=[]
for n,repeats in [(8,5),(9,3),(10,1)]:
    for pi,p in enumerate([.25,.4,.55,.7,.85,.95]):
        for j in range(repeats):
            seed=20261017+n*1000+pi*10+j
            G=nx.gnp_random_graph(n,p,seed=seed)
            if nx.is_connected(G) and G.number_of_edges()<n*(n-1)//2:
                cases.append((dict(model='Erdos-Renyi',n=n,p=p,seed=seed),G))
for n,d in [(8,3),(8,4),(8,5),(9,4),(9,6),(10,3),(10,6),(10,7),(10,8)]:
    G=nx.random_regular_graph(d,n,seed=20261017+n+d)
    if nx.is_connected(G):cases.append((dict(model='random_regular',n=n,d=d,seed=20261017+n+d),G))
for r in [3,4,5]:
    for s in [1,2,3]:
        G=nx.Graph();G.add_nodes_from(range(r+s))
        G.add_edges_from(itertools.combinations(range(s),2))
        G.add_edges_from(itertools.product(range(s),range(s,r+s)))
        cases.append((dict(model='clique_join_independent_set',r=r,s=s),G))
rows=[];start=time.time()
for specification,G in cases:
    G=nx.convert_node_labels_to_integers(G)
    result=check(G)
    rows.append(dict(specification=specification,n=len(G),edges=list(G.edges()),result=result))
    if len(rows)%10==0:print(json.dumps(dict(checked=len(rows),seconds=round(time.time()-start,1))),flush=True)
    if not result['detected']:break
out=dict(status='EXACT_SEEDED_LARGER_GRAPH_PROBE',target_scaled_by_nine=T,graphs_checked=len(rows),
    found_nonclique_with_lorentzian_partition=any(not x['result']['detected'] for x in rows),
    elapsed_seconds=round(time.time()-start,3),rows=rows,
    limits='Selected finite deterministic search, not a complete census beyond order seven. No general theorem, external review or grade. Included only as selected finite evidence in the expanded manuscript.')
(R/'larger-fixed-target-probe.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['target_scaled_by_nine','rows','limits']}),flush=True)

"""Exact finite scope probe of the fixed four-spin target."""
from pathlib import Path
import ast,itertools,json,math,time
from collections import defaultdict
import sympy as sp
import networkx as nx
R=Path(__file__).parent
module=ast.parse((R/'certify_profile_hierarchy.py').read_text())
exec(compile(ast.Module(body=[n for n in module.body if isinstance(n,ast.FunctionDef) and n.name=='inertia'],type_ignores=[]),'exact_inertia','exec'))
T=[[0,9,12,15],[9,9,9,9],[12,9,8,7],[15,9,7,5]]

def comps(n,q):
    if q==1:yield (n,);return
    for a in range(n+1):
        for rest in comps(n-a,q-1):yield (a,)+rest

def check(G):
    n=len(G);edges=list(G.edges());coeff=defaultdict(int)
    for s in itertools.product(range(4),repeat=n):
        w=1
        for u,v in edges:
            w*=T[s[u]][s[v]]
            if not w:break
        if w:coeff[tuple(s.count(c) for c in range(4))]+=w
    hs=[]
    for beta in comps(n-2,4):
        M=sp.zeros(4)
        for i in range(4):
            for j in range(i,4):
                ex=list(beta);ex[i]+=1;ex[j]+=1;ex=tuple(ex)
                v=coeff.get(ex,0)*math.prod(math.factorial(a) for a in ex)
                M[i,j]=M[j,i]=v
        ins,blocks=inertia(M)
        rec=dict(beta=list(beta),hessian=[[str(v) for v in row] for row in M.tolist()],inertia=ins,congruence_blocks=blocks)
        hs.append(rec)
        if ins[0]>=2:return dict(detected=True,witness=rec,derivatives_checked=len(hs))
    support=set(coeff)
    for a in support:
        for b in support:
            for i in range(4):
                if a[i]<=b[i]:continue
                def exchange(j):
                    aa=list(a);bb=list(b);aa[i]-=1;aa[j]+=1;bb[i]+=1;bb[j]-=1
                    return tuple(aa) in support and tuple(bb) in support
                assert any(a[j]<b[j] and exchange(j) for j in range(4)),(a,b,i)
    return dict(detected=False,all_quadratic_derivatives=hs,derivatives_checked=len(hs),support_M_convex_exact_exchange=True,coefficients=[dict(exponent=list(a),coefficient=str(v)) for a,v in sorted(coeff.items())],lorentzian_by_full_hessian_and_support_characterization=True)

source=json.loads((R/'profile-hierarchy-exact.json').read_text());rows=[];start=time.time()
candidates=list(source['rows'])
candidates.sort(key=lambda r:-r['h'])
for r in candidates:
    G=nx.Graph();G.add_nodes_from(range(r['n']));G.add_edges_from(r['edges'])
    result=check(G);row=dict(atlas_index=r['atlas_index'],n=len(G),edges=r['edges'],result=result);rows.append(row)
    if len(rows)%100==0:print(json.dumps(dict(checked=len(rows))),flush=True)
    if not result['detected']:
        assert any(G.subgraph(S).number_of_edges()==5 for S in itertools.combinations(G,4))
        break
out=dict(status='EXACT_NEXT_ROUND_SCOPE_PROBE',target_scaled_by_nine=T,graphs_checked=len(rows),found_nonclique_with_lorentzian_partition=any(not r['result']['detected'] for r in rows),rows=rows,limits='Outside the proved diamond-free class. Does not refute the universal-target conjecture. Same author context; no independent review. Finite evidence in the expanded manuscript, not an arbitrary-order theorem.')
(R/'fixed-diamond-next-scope.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['target_scaled_by_nine','rows','limits']}))
print('elapsed_seconds',round(time.time()-start,1))
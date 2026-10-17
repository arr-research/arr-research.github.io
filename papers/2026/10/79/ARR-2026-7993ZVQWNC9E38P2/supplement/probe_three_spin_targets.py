"""Exact finite tests of fixed three-spin subtargets, without minimality claim."""
from pathlib import Path
from collections import defaultdict
import ast,itertools,json,math,time
import sympy as sp
import networkx as nx
R=Path(__file__).parent
tree=ast.parse((R/'certify_profile_hierarchy.py').read_text())
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='inertia'],type_ignores=[]),'inertia','exec'))
def compositions(n,q):
    if q==1:yield (n,);return
    for x in range(n+1):
        for tail in compositions(n-x,q-1):yield (x,)+tail
def test(G,T):
    n=len(G);q=len(T);coeff=defaultdict(int);edges=list(G.edges())
    for colours in itertools.product(range(q),repeat=n):
        product=math.prod(T[colours[u]][colours[v]] for u,v in edges)
        if product:coeff[tuple(colours.count(j) for j in range(q))]+=product
    certificates=[]
    for beta in compositions(n-2,q):
        H=sp.zeros(q)
        for i in range(q):
            for j in range(i,q):
                exponent=list(beta);exponent[i]+=1;exponent[j]+=1;exponent=tuple(exponent)
                H[i,j]=H[j,i]=coeff.get(exponent,0)*math.prod(math.factorial(a) for a in exponent)
        ii,blocks=inertia(H)
        certificates.append(dict(beta=beta,inertia=ii,hessian=[[str(a) for a in row] for row in H.tolist()],congruence=blocks))
        if ii[0]>=2:return dict(detected=True,witness=certificates[-1])
    support=set(coeff)
    for a in support:
        for b in support:
            for i in range(q):
                if a[i]<=b[i]:continue
                found=False
                for j in range(q):
                    if a[j]>=b[j]:continue
                    aa=list(a);bb=list(b);aa[i]-=1;aa[j]+=1;bb[i]+=1;bb[j]-=1
                    if tuple(aa) in support and tuple(bb) in support:found=True;break
                assert found
    return dict(detected=False,all_quadratic_derivatives=certificates,support_M_convex_exact_exchange=True,
        exact_lorentzian_for_this_target=True,coefficients=[dict(exponent=e,coefficient=str(c)) for e,c in sorted(coeff.items())])
full=sp.Matrix([[0,9,12,15],[9,9,9,9],[12,9,8,7],[15,9,7,5]])
source=json.loads((R/'profile-hierarchy-exact.json').read_text())['rows']
results=[];start=time.time()
for ids in [(0,1,2),(0,1,3),(0,2,3)]:
    T=[[int(full[i,j]) for j in ids] for i in ids];checked=[]
    for row in source:
        G=nx.Graph();G.add_nodes_from(range(row['n']));G.add_edges_from(row['edges'])
        outcome=test(G,T)
        checked.append(dict(atlas_index=row['atlas_index'],n=len(G),edges=row['edges'],result=outcome))
        if not outcome['detected']:break
    result=dict(indices=ids,target_scaled_by_nine=T,graphs_checked=len(checked),
        found_counterexample_to_fixed_target=any(not r['result']['detected'] for r in checked),rows=checked)
    results.append(result)
    print(json.dumps({k:v for k,v in result.items() if k not in ['rows','target_scaled_by_nine']}),flush=True)
out=dict(status='EXACT_THREE_SPIN_SCOPE_AUDIT',results=results,elapsed_seconds=round(time.time()-start,3),
    limits='Tests only these three fixed targets. Does not prove four spins necessary for all possible targets or refute the universal-source characterization. Author computation, not independent review; included only as specific fixed-target limits in the expanded manuscript.')
(R/'three-spin-target-scope.json').write_text(json.dumps(out,indent=2)+'\n')

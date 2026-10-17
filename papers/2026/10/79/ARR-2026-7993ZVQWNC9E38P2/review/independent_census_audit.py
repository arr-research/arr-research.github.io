"""Fresh reconstruction of the two 989-graph certificate sets.
Stored certificate parameters are used as inputs, not as conclusions. All
matrices and derivative factorials are recomputed with referee-owned code.
"""
from pathlib import Path
from math import factorial
import json,time
import networkx as nx
import sympy as sp
from independent_checks import layers,kernel,target,hessian_from_coefficients,exact_inertia
ROOT=Path(__file__).resolve().parent
INP=ROOT.parent/'input'/'supplement'
START=time.time();atlas=nx.graph_atlas_g()
expected={i for i,G in enumerate(atlas) if 3<=len(G)<=7 and nx.is_connected(G) and 2*G.number_of_edges()<len(G)*(len(G)-1)}
out={'kind':'Fresh referee reconstruction using archived witness parameters only','rows':[]}
rows=json.loads((INP/'profile-hierarchy-exact.json').read_text())['rows']
assert len(rows)==989 and {r['atlas_index'] for r in rows}==expected
for r in rows:
    G=atlas[r['atlas_index']];assert [list(e) for e in G.edges()]==r['edges']
    n,h=len(G),r['h'];aa=list(map(sp.Rational,r['target_parameters']));q=len(aa)
    layer,_,_=layers(G,h);Q=kernel(layer,aa[0]**2)
    stored=sp.Matrix(r['integer_kernel'])/sp.Integer(r['positive_scale_denominator'])
    assert Q==stored
    H=target(aa);assert min(H)>0 and H.rank()==2
    beta=[h,n-h-2]+[0]*(q-2)
    M=hessian_from_coefficients(G,H,beta)
    U=sp.Matrix(q,h+2,lambda i,k:(1-aa[0]*aa[i])**k)
    assert M==factorial(h)*factorial(n-h-2)/aa[0]**2*U*Q*U.T
    ins=exact_inertia(Q);assert ins==r['inertia'] and ins[0]>=2
    out['rows'].append({'atlas_index':r['atlas_index'],'n':n,'h':h,'ell':str(aa[0]),'inertia':ins})
out['positive_hierarchy_checks']=len(rows)
print(json.dumps({'positive_hierarchy_checks':len(rows),'seconds':round(time.time()-START,2)}),flush=True)
fixed=json.loads((INP/'fixed-diamond-next-scope.json').read_text())['rows']
assert len(fixed)==989 and {r['atlas_index'] for r in fixed}==expected
H=sp.Matrix([[0,9,12,15],[9,9,9,9],[12,9,8,7],[15,9,7,5]])
fixedrows=[]
for r in fixed:
    G=atlas[r['atlas_index']];assert [list(e) for e in G.edges()]==r['edges']
    witness=r['result']['witness'];beta=witness['beta']
    M=hessian_from_coefficients(G,H,beta)
    assert M==sp.Matrix(witness['hessian'])
    ins=exact_inertia(M);assert ins==witness['inertia'] and ins[0]>=2
    fixedrows.append({'atlas_index':r['atlas_index'],'beta':beta,'inertia':ins})
out['fixed_target_rows']=fixedrows;out['fixed_target_checks']=len(fixedrows)
out['status']='PASS_ALL_1978_CERTIFICATE_RECONSTRUCTIONS';out['seconds']=round(time.time()-START,3)
(ROOT/'independent-census-results.json').write_text(json.dumps(out,ensure_ascii=True,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','fixed_target_rows']}),flush=True)

"""Failure of one specified derivative, not of the fixed target itself."""
from pathlib import Path
from fractions import Fraction
import ast,itertools,json,math
import sympy as sp
import networkx as nx
R=Path(__file__).parent
raw=(R/'certify_profile_hierarchy.py').read_text();tree=ast.parse(raw)
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
source=ast.get_source_segment(raw,next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='direct_hessian'))
source=source.replace('def direct_hessian(', 'def direct_four_hessian(').replace('q=h+2','q=4')
source=source.replace('[sp.Rational(i-1,q) for i in range(2,q)]','[sp.Rational(1,3),sp.Rational(2,3)]')
source=source.replace('beta=[h,n-h-2]+[0]*h','beta=[h,n-h-2]+[0]*(q-2)')
source=source.replace('for r in range(q)] for x in aa','for r in range(h+2)] for x in aa')
source=source.replace('assert U.det()!=0','assert U.rank()==min(U.shape)')
exec(source)
s=sp.symbols('s')
M=sp.Matrix([[0,0,0,s],[0,0,s,-s],[0,s,0,s*(s-1)],[s,-s,s*(s-1),-s*(s-1)]])
V=sp.Matrix([[y,y*y,y**3,y**4] for y in [sp.Integer(1),sp.Rational(4,3),sp.Rational(5,3)]])
formula=sp.Rational(12800,4782969)*s**3*(185*s-473)
assert sp.expand((V*M*V.T).det()-formula)==0
rows=[]
for se in range(1,7):
    n=se+4;G=nx.Graph();G.add_nodes_from(range(n))
    G.add_edges_from(itertools.combinations(range(se),2));G.add_edges_from(itertools.product(range(se),range(se,n)))
    G.add_edge(se,se+1)
    H,U,aa,T=direct_four_hessian(G,3,Fraction(-1));Q,den=integer_kernel(G,3,Fraction(-1))
    scale=math.factorial(3)*math.factorial(n-5)
    assert den==1 and H==scale*U*Q*U.T
    assert H[1:,1:]==2*scale*(V*M*V.T).subs(s,se)
    ii,blocks=inertia(H)
    assert ii==([2,1,1] if se<=2 else [1,2,1])
    rows.append(dict(s=se,n=n,h=3,inertia=ii,hessian=[[str(x) for x in row] for row in H.tolist()],congruence=blocks))
out=dict(status='PASS_EXACT_FOUR_SPIN_DERIVATIVE_LIMIT',family='K_s join (K_2 disjoint union K_1 disjoint union K_1)',
    derivative='partial_0^3 partial_1^(s-1)',target='Kdiamond',normalized_determinant=str(formula),
    exact_direct_checks=len(rows),rows=rows,
    limits='Only this derivative is inconclusive for s>=3. This does not prove Lorentzianity for Kdiamond or necessity of five states for any target.')
(R/'four-spin-restriction-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],exact_direct_checks=len(rows))))

"""Direct checks for the proposed fixed four-state diamond-free witness."""
from pathlib import Path
import ast,json,itertools,math
from fractions import Fraction
import sympy as sp
import networkx as nx
R=Path(__file__).parent
module=ast.parse((R/'certify_profile_hierarchy.py').read_text())
exec(compile(ast.Module(body=[n for n in module.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'hierarchy_functions','exec'))
# Reuse coefficient enumeration, with this newly specified target.
source=ast.get_source_segment((R/'certify_profile_hierarchy.py').read_text(),next(n for n in module.body if isinstance(n,ast.FunctionDef) and n.name=='direct_hessian'))
old='aa=[sp.Rational(ell.numerator,ell.denominator),sp.Integer(0)]+[sp.Rational(i-1,q) for i in range(2,q)]'
new='aa=[sp.Rational(ell.numerator,ell.denominator),sp.Integer(0)]+[sp.Rational(i-1,3) for i in range(2,q)]'
assert old in source
exec(source.replace('def direct_hessian(', 'def direct_fixed_hessian(').replace(old,new))
A=sp.Matrix([[-1],[0],[sp.Rational(1,3)],[sp.Rational(2,3)]])
K=sp.ones(4)-A*A.T
assert 9*K==sp.Matrix([[0,9,12,15],[9,9,9,9],[12,9,8,7],[15,9,7,5]])
assert inertia(K)[0]==[1,1,2]
rows=[];positive_rows=[]
gap=json.loads((R/'neighbourhood-gap-checks.json').read_text())
for row in gap['rows']:
    if not row['diamond_free']:continue
    G=nx.Graph();G.add_nodes_from(range(row['n']));G.add_edges_from(row['edges'])
    h=1 if row['triangle_free'] else 2
    B,d=integer_kernel(G,h,Fraction(-1));M,U,aa,H=direct_fixed_hessian(G,h,Fraction(-1))
    factor=math.factorial(h)*math.factorial(len(G)-h-2)
    assert M==factor*U*B*U.T
    assert H==K[:h+2,:h+2]
    ins,blocks=inertia(M);assert ins[0]>=2
    rowout=dict(atlas_index=row['atlas_index'],n=len(G),h=h,principal_target_size=h+2,edges=row['edges'],hessian=[[str(v) for v in rr] for rr in M.tolist()],inertia=ins,congruence_blocks=blocks)
    rows.append(rowout)
    ell=Fraction(row['positive_witness']['ell'])
    Bp,d=integer_kernel(G,h,ell);Mp,Up,aap,Hp=direct_fixed_hessian(G,h,ell)
    factorp=sp.Rational(factor,d)/(sp.Rational(ell.numerator,ell.denominator)**2)
    assert Mp==factorp*Up*Bp*Up.T and min(Hp)>0
    ip,bp=inertia(Mp);assert ip[0]>=2
    positive_rows.append(dict(atlas_index=row['atlas_index'],ell=str(ell),h=h,inertia=ip,direct_partition_identity=True))
out=dict(status='PASS_EXACT_FIXED_BOUNDARY_AND_POSITIVE_PERTURBATIONS',target=[[str(v) for v in row] for row in K.tolist()],target_inertia=[1,1,2],graphs=len(rows),triangle_free_cases=sum(r['h']==1 for r in rows),with_triangles=sum(r['h']==2 for r in rows),fixed_target_direct_checks=len(rows),positive_perturbation_direct_checks=len(positive_rows),rows=rows,positive_rows=positive_rows,limits='The common target is nonnegative, with one zero entry. Strictly positive perturbations may depend on the graph. Author-side exact finite audit; the general proof is separate, with no external review yet.')
(R/'fixed-diamond-target-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['target','rows','positive_rows','limits']}))
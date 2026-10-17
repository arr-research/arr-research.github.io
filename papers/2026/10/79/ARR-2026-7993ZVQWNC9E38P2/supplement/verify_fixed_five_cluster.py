"""One fixed five-spin target on joins of a clique with disjoint cliques."""
from pathlib import Path
from fractions import Fraction
import ast,json,math,itertools,time
import networkx as nx
import sympy as sp
R=Path(__file__).parent
raw=(R/'certify_profile_hierarchy.py').read_text();tree=ast.parse(raw)
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
original=ast.get_source_segment(raw,next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='direct_hessian'))
fixed=original.replace('def direct_hessian(', 'def direct_five_hessian(')
fixed=fixed.replace('q=h+2','q=5').replace('[sp.Rational(i-1,q) for i in range(2,q)]','[sp.Rational(i,4) for i in range(1,4)]')
fixed=fixed.replace('beta=[h,n-h-2]+[0]*h','beta=[h,n-h-2]+[0]*(q-2)')
fixed=fixed.replace('for r in range(q)] for x in aa','for r in range(h+2)] for x in aa')
fixed=fixed.replace('assert U.det()!=0','assert U.rank()==min(U.shape)')
exec(fixed)
target=sp.Matrix([[0,16,20,24,28],[16,16,16,16,16],[20,16,15,14,13],[24,16,14,12,10],[28,16,13,10,7]])/16
assert target.rank()==2 and min(target)==0
assert inertia(target)[0]==[1,1,3]
L,C,s=sp.symbols('L C s')
M=sp.Matrix([[L*(L-1)-C,C,0,s*L],[C,-C,s*L,-s*L],
             [0,s*L,0,s*(s-1)],[s*L,-s*L,s*(s-1),-s*(s-1)]])
det=L*s*s*(L+s-1)*(s*L*L-(s-1)*C)
assert sp.expand(M.det()-det)==0
assert sp.expand(M.extract([1,2],[1,2]).det()+s*s*L*L)==0
M0=sp.Matrix([[0,0,0,s],[0,0,s,-s],[0,s,0,s*(s-1)],[s,-s,s*(s-1),-s*(s-1)]])
assert sp.expand(M0.det()-s**4)==0
cases=[(sizes,se) for sizes in itertools.combinations_with_replacement(range(1,4),3) for se in range(1,4)]
cases += [(sizes,se) for sizes in [(1,1,1,1),(1,1,1,2),(1,1,2,2),(1,2,2,2),(2,2,2,2),(1,1,1,3)] for se in [1,2]]
cases += [(sizes,se) for sizes in [(1,1),(1,2),(2,2),(2,3)] for se in [1,2]]
cases += [(sizes,se) for sizes in [(1,1,1,1,1),(1,1,1,1,2),(1,1,1,2,2),(2,2,2,2,2),
    (1,1,1,1,1,1),(1,1,1,1,1,2),(1,1,1,1,2,2)] for se in [1,2]]
rows=[];start=time.time()
for sizes,se in cases:
    r=len(sizes);n=se+sum(sizes);G=nx.Graph();G.add_nodes_from(range(n))
    G.add_edges_from(itertools.combinations(range(se),2));offset=se
    for size in sizes:
        branch=range(offset,offset+size);G.add_edges_from(itertools.combinations(branch,2))
        G.add_edges_from(itertools.product(range(se),branch));offset+=size
    lv=sum(x-1 for x in sizes);cv=sum((x-1)*(x-2) for x in sizes)
    h=r if lv else r-1
    Q,den=integer_kernel(G,h,Fraction(-1));assert den==1
    if r>=3:
        expected=sp.zeros(h+2);small=M.subs({L:lv,C:cv,s:se}) if lv else M0.subs(s,se)
        positions=[1,2,h,h+1] if lv else [0,1,h,h+1]
        multiplicity=math.prod(sizes) if lv else r
        for i in range(4):
            for j in range(4):expected[positions[i],positions[j]]=multiplicity*small[i,j]
        assert Q==expected
    H,U,aa,T=direct_five_hessian(G,h,Fraction(-1));assert T==target
    fac=math.factorial(h)*math.factorial(n-h-2)
    assert H==fac*U*Q*U.T
    ii,_=inertia(H);assert ii[0]>=2
    positive=None
    for denominator in [10,100,1000,10000,100000,1000000]:
        ell=Fraction(1-denominator,denominator);P,pd=integer_kernel(G,h,ell)
        aa=[sp.Rational(ell.numerator,ell.denominator),sp.Integer(0),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4)]
        Up=sp.Matrix([[(1-aa[0]*x)**j for j in range(h+2)] for x in aa])
        ins,_=inertia(Up*P*Up.T)
        if ins[0]>=2:positive=dict(ell=str(ell),inertia=ins);break
    assert positive
    positive_direct=se==2
    if positive_direct:
        Hp,Vp,ap,tp=direct_five_hessian(G,h,ell)
        assert min(tp)>0 and tp.rank()==2
        assert Hp==sp.Rational(fac,pd)/(sp.Rational(ell.numerator,ell.denominator)**2)*Vp*P*Vp.T
    rows.append(dict(branch_clique_sizes=sizes,separator_size=se,n=n,h=h,q=5,
        exact_kernel_identity=True,boundary_inertia=ii,direct_boundary_hessian=True,
        positive=positive,direct_positive_hessian=positive_direct))
    if len(rows)%10==0:print(json.dumps(dict(checked=len(rows),seconds=round(time.time()-start,1))),flush=True)
out=dict(status='PASS_FIXED_FIVE_CLIQUE_CLUSTER_CHECKS',
    proposed_family='K_s join disjoint union of r>=2 nonempty cliques, s>=1',
    fixed_target_scaled_by_16=[[int(x*16) for x in row] for row in target.tolist()],
    target_inertia=[1,1,3],symbolic_determinant=str(det),empty_residual_determinant='s**4',
    boundary_direct_checks=len(rows),positive_direct_checks=sum(x['direct_positive_hessian'] for x in rows),
    elapsed_seconds=round(time.time()-start,3),rows=rows,
    limits='Fixed nonnegative five-spin target; positive perturbation may depend on G. Proposed general proof requires the rectangular profile identity and generalized Vandermonde argument, supplied separately. Author computation, not external review. Included in the expanded manuscript; not externally reviewed.')
(R/'fixed-five-cluster-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k in ['status','boundary_direct_checks','positive_direct_checks','elapsed_seconds']}),flush=True)

"""Two-clique-sum extension, with author-side exact checks."""
from pathlib import Path
from fractions import Fraction
import ast,json,math,itertools
import sympy as sp
import networkx as nx
R=Path(__file__).parent
raw=(R/'certify_profile_hierarchy.py').read_text();module=ast.parse(raw)
exec(compile(ast.Module(body=[n for n in module.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'hierarchy_functions','exec'))
source=ast.get_source_segment(raw,next(n for n in module.body if isinstance(n,ast.FunctionDef) and n.name=='direct_hessian'))
source=source.replace('def direct_hessian(', 'def direct_fixed_hessian(').replace('[sp.Rational(i-1,q) for i in range(2,q)]','[sp.Rational(i-1,3) for i in range(2,q)]')
exec(source)
A,B,s=sp.symbols('A B s');L=A+B;C=A*(A-1)+B*(B-1)
M=sp.Matrix([[2*A*B,C,s*L],[C,2*s*L-C,s*(s-1-L)],[s*L,s*(s-1-L),-s*(s-1)]])
factor=-s*(L+s-1)*(L**2*(L+2*s-1)+2*A*B*(s-1)*(L+s))
assert sp.expand(M.det()-factor)==0
assert sp.expand((sp.ones(1,3)*M*sp.ones(3,1))[0]-(L+s)*(L+s-1))==0
N=s*(s+1)*(s+2);E=s**2*(s+3);W=s*(s**2+3*s-2);U=s*(s+4)*(s-1)
assert sp.expand(W**2-E*U-4*s**2)==0
assert sp.expand(N*(E*U-W**2)+U*(E**2-N*W)+24*s**3)==0
checks=[]
for a,b,se in itertools.product(range(1,5),repeat=3):
    n=a+b+se;G=nx.Graph();G.add_nodes_from(range(n))
    sep=list(range(se));left=list(range(se,se+a));right=list(range(se+a,n))
    for group in [sep+left,sep+right]:G.add_edges_from(itertools.combinations(group,2))
    h=1 if a==b==1 else 2
    Q,den=integer_kernel(G,h,Fraction(-1));assert den==1
    if h==2:
        expected=sp.zeros(4);expected[1:,1:]=a*b*M.subs({A:a-1,B:b-1,s:se})
        assert Q==expected,(a,b,se)
        assert Q[1:,1:].det()<0
    ins,blocks=inertia(Q);assert ins[0]>=2,(a,b,se)
    H,V,aa,target=direct_fixed_hessian(G,h,Fraction(-1))
    scale=math.factorial(h)*math.factorial(n-h-2)
    assert H==scale*V*Q*V.T
    chosen=None
    for k in [10,100,1000,10000,100000]:
        ell=Fraction(1-k,k);Qp,dp=integer_kernel(G,h,ell);ii,_=inertia(Qp)
        if ii[0]>=2:chosen=dict(ell=str(ell),inertia=ii);break
    assert chosen
    # Directly test the positive continuation for representatives, including
    # each maximal parameter and both symmetry-degenerate cases.
    positive_direct=(a==b or a==1 or b==1 or se==4)
    if positive_direct:
        Hp,Vp,ap,tp=direct_fixed_hessian(G,h,ell)
        assert min(tp)>0
        assert Hp==sp.Rational(scale,dp)/(sp.Rational(ell.numerator,ell.denominator)**2)*Vp*Qp*Vp.T
    checks.append(dict(a=a,b=b,s=se,n=n,h=h,boundary_identity_exact=True,inertia=ins,positive_witness=chosen,positive_identity_exact=positive_direct))
out=dict(status='PASS_SYMBOLIC_AND_EXACT_TWO_CLIQUE_CHECKS',family='G=K_s join (K_a disjoint union K_b), a,b,s>=1',target='Kdiamond from the 13-page manuscript, fixed nonnegative rank two; positive rational perturbation may depend on source',general_kernel=[[str(x) for x in row] for row in M.tolist()],definitions='A=a-1, B=b-1, L=A+B. For L>0, Q_2(1)=ab*(0 direct_sum M).',determinant_factored=str(factor),positive_direction='ones^T M ones=(L+s)(L+s-1)>0; for L>0 and s>=1 the determinant is negative.',degenerate_case='For a=b=1, G=K_(s+2) minus one edge. The h=1 kernel at ell=-1 has determinant -24*s^3<0.',symbolic_identities_verified=True,boundary_direct_checks=len(checks),positive_direct_checks=sum(c['positive_identity_exact'] for c in checks),checks=checks,limits='Proposed general proof recorded separately; same author context, no independent review or grade. Included in the expanded manuscript as author-side evidence.')
(R/'two-clique-extension-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k in ['status','boundary_direct_checks','positive_direct_checks','symbolic_identities_verified']}))
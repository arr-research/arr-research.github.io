"""Next-round fixed-four-spin candidate on complete multipartite sources."""
from pathlib import Path
from fractions import Fraction
import ast,itertools,json,math,time
import sympy as sp
import networkx as nx
R=Path(__file__).parent
raw=(R/'certify_profile_hierarchy.py').read_text();tree=ast.parse(raw)
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
source=ast.get_source_segment(raw,next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='direct_hessian'))
source=source.replace('def direct_hessian(', 'def direct_four_hessian(').replace('q=h+2','q=4')
source=source.replace('[sp.Rational(i-1,q) for i in range(2,q)]','[sp.Rational(1,3),sp.Rational(2,3)]')
source=source.replace('beta=[h,n-h-2]+[0]*h','beta=[h,n-h-2]+[0]*(q-2)')
source=source.replace('for r in range(q)] for x in aa','for r in range(h+2)] for x in aa')
source=source.replace('assert U.det()!=0','assert U.rank()==min(U.shape)')
exec(source)
A,B,C=sp.symbols('A B C')
M4=sp.Matrix([[0,0,0,B],[0,0,B,-B],[0,B,A,C],[B,-B,C,-C]])
M3=sp.Matrix([[0,0,B],[0,A+2*B,C-B],[B,C-B,-C]])
assert sp.expand(M4.det()-B**4)==0
assert sp.expand(M3.det()+B**2*(A+2*B))==0
cases=[]
for r in [2,3,4]:
    cases += [a for a in itertools.combinations_with_replacement(range(1,4),r) if max(a)>1 and sum(a)<=9]
cases += [(1,4),(2,4),(4,4),(1,1,4),(1,2,4),(2,2,4),(1,5),(2,5),(5,5),(1,1,5),(1,6),(2,6)]
assert len(set(cases))==len(cases)
rows=[];start=time.time()
for sizes in cases:
    G=nx.complete_multipartite_graph(*sizes);n=len(G);alpha=max(sizes);h=alpha-1
    av=bv=cv=0
    for i,size in enumerate(sizes):
        if size<h:continue
        w=math.comb(size,h);k=size-h;y=n-size
        av+=w*sum(x*(x-1) for j,x in enumerate(sizes) if j!=i)
        bv+=w*k*y
        cv+=w*(y*y-sum(x*x for j,x in enumerate(sizes) if j!=i))
    assert av>=0 and bv>0 and cv>=0
    Q,den=integer_kernel(G,h,Fraction(-1));assert den==1
    if h==1:expected=M3.subs({A:av,B:bv,C:cv})
    else:
        expected=sp.zeros(h+2);small=M4.subs({A:av,B:bv,C:cv});positions=[0,1,h,h+1]
        for i in range(4):
            for j in range(4):expected[positions[i],positions[j]]=small[i,j]
    assert Q==expected,sizes
    H,U,aa,T=direct_four_hessian(G,h,Fraction(-1));scale=math.factorial(h)*math.factorial(n-h-2)
    assert H==scale*U*Q*U.T
    ii,_=inertia(H);assert ii==([2,1,1] if h==1 else [2,2,0])
    positive=None
    for denell in [10,100,1000,10000,100000]:
        ell=Fraction(1-denell,denell);P,pd=integer_kernel(G,h,ell)
        aa=[sp.Rational(ell.numerator,ell.denominator),sp.Integer(0),sp.Rational(1,3),sp.Rational(2,3)]
        Up=sp.Matrix([[(1-aa[0]*x)**j for j in range(h+2)] for x in aa])
        ins,_=inertia(Up*P*Up.T)
        if ins[0]>=2:positive=dict(ell=str(ell),inertia=ins);break
    assert positive
    direct_positive=alpha>=4 or len(sizes)==2
    if direct_positive:
        Hp,Vp,ap,tp=direct_four_hessian(G,h,ell);assert min(tp)>0
        assert Hp==sp.Rational(scale,pd)/(sp.Rational(ell.numerator,ell.denominator)**2)*Vp*P*Vp.T
    rows.append(dict(part_sizes=sizes,n=n,alpha=alpha,h=h,profile_totals=dict(A=av,B=bv,C=cv),
        exact_boundary_identity=True,boundary_inertia=ii,positive=positive,direct_positive_identity=direct_positive))
out=dict(status='PASS_EXACT_MULTIPARTITE_CANDIDATE',proposed_family='All connected noncomplete complete multipartite graphs',
    target='One fixed nonnegative four-spin Kdiamond; source-dependent positive rational perturbations.',
    four_dimensional_determinant='B**4',three_dimensional_determinant='-B**2*(A+2*B)',
    exact_boundary_checks=len(rows),exact_positive_checks=sum(x['direct_positive_identity'] for x in rows),
    rows=rows,elapsed_seconds=round(time.time()-start,3),
    limits='Author-side proposed general proof and finite checks; priority and separate review pending. Included as author-side evidence for the complete multipartite theorem.')
(R/'multipartite-extension-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k in ['status','exact_boundary_checks','exact_positive_checks','elapsed_seconds']}))

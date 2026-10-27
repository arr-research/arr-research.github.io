"""Exact rational near-ninefold SLD witness, independent of conjecture997."""
from pathlib import Path
import sympy as s,json
p=Path(__file__).parent;e=s.Rational(1,1000);xi=s.Rational(1,10**18)
a=s.Matrix([1,0,0,0,e,0]);b=s.Matrix([0,e,0,0,0,1]);base=(a*a.T+b*b.T)/(2*(1+e*e));P=2*base;Q=s.eye(6)-P
sigma=(1-xi)*base+xi*s.eye(6)/6;D=s.zeros(6)
for i,j,z in [(0,4,1),(4,0,1),(4,4,2*e),(1,1,-2*e),(1,5,-1),(5,1,-1)]:D[i,j]=z
alpha=(1-xi)/2+xi/6;beta=xi/6
L=P*D*P/alpha+2*(P*D*Q+Q*D*P)/(alpha+beta)
assert sigma*L+L*sigma==2*D
gin=s.factor(s.trace(D*L))
ps=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
ops=[s.kronecker_product(q,s.eye(3)) for q in ps]
N=lambda X:sum((U*X*U.conjugate().T/3 for U in ops),s.zeros(6))
ns=N(sigma);nd=N(D)
# Boundary antipolarizing map has two2x2blocks and2singletons.
ind=[0,4];W=ns.extract(ind,ind);T=nd.extract(ind,ind)
x,y,z=s.symbols('x y z');Y=s.Matrix([[x,y],[y,z]]);res=W*Y+Y*W-2*T
sol=s.solve([res[0,0],res[0,1],res[1,1]],[x,y,z]);Y=Y.subs(sol)
Lout=s.zeros(6);rev=s.Matrix([[0,1],[1,0]])
for indices,block in [([0,4],Y),([1,5],-rev*Y*rev)]:
 for i in range(2):
  for j in range(2):Lout[indices[i],indices[j]]=block[i,j]
assert ns*Lout+Lout*ns==2*nd
gout=s.factor(s.trace(nd*Lout));ratio=s.factor(gout/gin)
checks={'input_SLD_equation':sigma*L+L*sigma==2*D,'output_SLD_equation':ns*Lout+Lout*ns==2*nd,'density_trace':s.trace(sigma)==1,'tangent_partialtrace':D[:3,:3]+D[3:,3:]==s.zeros(3),'input_faithful_eigenvalues':alpha>0 and beta>0,'output_2x2_positive':W[0,0]>0 and W.det()>0,'finite_ratio_above_999997_over_1e6':ratio>s.Rational(999997,10**6),'finite_ratio_below_one':ratio<1,'enhancement_above_8999973_over_1e6':9*ratio>s.Rational(8999973,10**6)}
assert all(checks.values())
out={'scope':'Exact rational localSLD witness forN=(AdX+AdY+AdZ)/3. This finite calculation does NOT depend on997or the universal9fold upper. Parent written, not independently audited.','epsilon':str(e),'regularization':str(xi),'support_eigenvalue':str(alpha),'kernel_eigenvalue':str(beta),'input_SLD':str(gin),'output_SLD':str(gout),'ratio_numerator':str(s.numer(ratio)),'ratio_denominator':str(s.denom(ratio)),'ratio_decimal':str(s.N(ratio,75)),'ordinary_coefficient':'1/9 from exactBlochaction and ordinarySLD theorem','enhancement_decimal':str(s.N(9*ratio,75)),'checks':{k:bool(v) for k,v in checks.items()},'faithful_family':'rho_t=sigma+tD for sufficientlysmallt; Tr_A D=0, no parameter stored solelyinR.','external_audit':None,'score':None}
(p/'CERTIFICATE1003.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))

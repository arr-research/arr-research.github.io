from pathlib import Path
import sympy as s,json
P=Path(__file__).parent;R=s.Rational
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);l=R(1,2);kap=R(3,2);t=R(1,10)
E=lambda a:(a+Z*a*Z)/2
N=lambda a:l*a+(1-l)*E(a)
def resolvent(a,b,z):
 n=a.rows;Q=s.kronecker_product(a,s.eye(n))+s.kronecker_product(s.eye(n),b.T);y=Q.inv()*s.Matrix(list(z));Y=s.Matrix(n,n,list(y));assert a*Y+Y*b==z;return s.trace(z.T*Y)
base=I/2;rho=base+t*X;sig=base-t*X;D=rho-sig
assert E(rho)==E(sig)==base
assert all(v>0 for A in [rho,sig,kap*base-rho,kap*base-sig] for v in A.eigenvals())
local=s.factor(resolvent(N(base),N(base),l*X)/resolvent(base,base,X))
triangle=s.factor(resolvent(N(rho),N(sig),N(D))/resolvent(rho,sig,D))
assert local==triangle==l*l==R(1,4)
candidate=l*l*kap/(1+l*(kap-1));assert candidate==R(3,10)>local
pure=(I+X)/2;assert pure*E(pure)==pure/2 and (2*E(pure)-pure).is_positive_semidefinite
data={'scope':'Exact falsifiers of stronger readings/shortcuts, NOT of correctly defined1017','index_alone_shortcut':{'channel':'pinching E=(id+AdZ)/2; N_lambda=lambda id+(1-lambda)E','index_C_and_Ccb':'2','kappa':str(kap),'lambda':str(l),'actual_complete_equal_E_SLD_chimin_triangle':'lambda^2 by inverse convexity and Z-odd differences; lower at E-fixed bases','SLD_rational':str(local),'finite_triangular_rational':str(triangle),'incorrect_index_order_sharpness':str(candidate),'pure_index_witness_verified':True},'each_fixed_reference_reading':{'d':3,'R':1,'lambda':'1/2','kappa':4,'class_equals_kappa_3':'all faithful qutrit states obey rho<=3 I/3','upper_using_kappa_3':'3/8','formula_with_kappa_4':'2/5','strict_gap':str(R(2,5)-R(3,8)),'meaning':'equality requires complete supremum over R, not each fixed R'},'all_passed':True}
(P/'SHORTCUT_FALSIFIERS1018.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8');print(json.dumps(data))

"""Own full ambient rational superoperator solves; no supplied block solver."""
from pathlib import Path
import sympy as s,json,time,traceback
P=Path(__file__).parent;R=s.Rational;rows=[]
def record(name,**x):
 rows.append({'name':name,**x});(P/'EXACT1018.json').write_text(json.dumps({'method':'Sparse full n² by n² row-vectorized Sylvester solve with exact rational entries and full matrix residual','records':rows},indent=2)+'\n',encoding='utf-8');print(name,flush=True)
def partial(x,d,r):return s.Matrix(r,r,lambda i,j:sum(x[a*r+i,a*r+j] for a in range(d)))
def expectation(x,d,r):return s.kronecker_product(s.eye(d)/d,partial(x,d,r))
def dep(x,l,d,r):return l*x+(1-l)*expectation(x,d,r)
def positive(x):
 L,D=x.LDLdecomposition(hermitian=False);piv=list(D.diagonal());assert L*D*L.T==x
 return {'positive':all(v>0 for v in piv),'LDL_pivots':[str(v) for v in piv]}
def form(a,b,z):
 n=a.rows;Q=s.SparseMatrix(s.kronecker_product(a,s.eye(n))+s.kronecker_product(s.eye(n),b.T));rhs=s.SparseMatrix(n*n,1,{(i,0):v for i,v in enumerate(z) if v!=0});v=Q.inv()*rhs;Y=s.Matrix(n,n,list(v));assert a*Y+Y*b==z
 return s.factor(s.trace(z.T*Y))
def ladder(d,e):
 r=d+1;n=d*r;S=s.zeros(n);D=s.zeros(n)
 for i in range(d):
  a=s.zeros(n,1);b=s.zeros(n,1);a[i*r+i]=1;a[((i+1)%d)*r+d]=e;b[((i+1)%d)*r+d]=1 if i==0 else -1 if i==1 else 0
  S+=a*a.T/(d*(1+e*e));D+=a*b.T+b*a.T
 return S,D
try:
 reference=json.loads(Path(r'D:\Proyectos\airr-investigacion\2026-10-27_dimension1017\FINITE1017.json').read_text())['rows']
 # Two complete144x144 inverses, finite pair and SLD, for a nonqubit case.
 d=3;r=4;e=R(1,100);kap=R(4);theta=R(99,100);l=-R(1,8);t=R(1,10**10);S,D=ladder(d,e);B=expectation(S,d,r);sig=dep(S,theta,d,r);rho=sig+t*D;os=dep(sig,l,d,r);orr=dep(rho,l,d,r)
 fi=form(rho,sig,rho-sig);fo=form(orr,os,orr-os);tri=s.factor(fo/fi);gi=2*form(sig,sig,D);go=2*form(os,os,l*D);local=s.factor(go/gi);ref=next(x for x in reference if x['d']==d and x['kappa']=='4' and x['lambda_']=='-1/8')
 assert local==s.sympify(ref['ratio_SLD']) and tri==s.sympify(ref['ratio_triangular'])
 checks={k:positive(v) for k,v in {'sigma':sig,'rho':rho,'order_sigma':kap*B-sig,'order_rho':kap*B-rho,'output_sigma':os,'output_rho':orr}.items()};assert all(v['positive'] for v in checks.values())
 record('full_144dim_ladder',d=d,R=r,kappa=str(kap),theta=str(theta),lambda_=str(l),SLD=str(local),triangular=str(tri),matches_supplied_exactly=True,checks=checks,equal_actual_R=partial(sig,d,r)==partial(rho,d,r),Gin=str(gi),Gout=str(go))
 # Independent simpler Bell-pair lower. P0 and P1 are rational outer products
 # of orthogonal maximally-entangled vectors (identity and cyclic shift).
 for d,kap in [(3,R(399,100)),(4,R(499,100)),(5,R(599,100))]:
  n=d*d;v=s.zeros(n,1);w=s.zeros(n,1)
  for i in range(d):v[i*d+i]=1;w[i*d+(i+1)%d]=1
  P0=v*v.T/d;P1=w*w.T/d;D=P0-P1;a=kap/(d*d);b=(1-2*a)/(d*d-2);sig=b*s.eye(n)+(a-b)*(P0+P1);B=s.eye(n)/(d*d)
  assert P0*P1==s.zeros(n) and partial(P0,d,d)==s.eye(d)/d and partial(P1,d,d)==s.eye(d)/d
  assert partial(sig,d,d)==s.eye(d)/d and partial(D,d,d)==s.zeros(d) and sig*D==a*D
  l=-R(1,d*d-1);aa=l*a+(1-l)/(d*d);C=l*l*kap/(1+l*(kap-1));gin=2/a;gout=2*l*l/aa;assert s.factor(gout/gin-C)==0
  # Exact finite commuting triangular formula; verify against ambient81x81 atd3.
  t=R(1,10**6);rho=sig+t*D;os=dep(sig,l,d,d);orr=dep(rho,l,d,d);fi=t*t/(2*a+t)+t*t/(2*a-t);fo=(l*t)**2/(2*aa+l*t)+(l*t)**2/(2*aa-l*t);tri=s.factor(fo/fi)
  checks={'sigma_faithful':a>0 and b>0,'rho_faithful':a-t>0 and b>0,'budget_original_d_plus_1':a+t<R(d+1,d*d),'equal_reference':partial(rho,d,d)==partial(sig,d,d),'commuting_pair':rho*sig==sig*rho,'N_output_faithful':aa-abs(l*t)>0 and l*b+(1-l)/d**2>0}
  if d==3:
   assert form(rho,sig,t*D)==fi and form(orr,os,l*t*D)==fo;assert 2*form(sig,sig,D)==gin
  assert all(checks.values());record('simpler_Bell_lower',d=d,R=d,kappa_actual_base=str(kap),original_budget=str(d+1),lambda_=str(l),a=str(a),b=str(b),SLD_exact=str(C),finite_triangular_exact=str(tri),t=str(t),checks=checks,full_ambient_crosscheck=(d==3))
 record('complete',passed=True)
except Exception as ex:record('ERROR',error=repr(ex),traceback=traceback.format_exc());raise

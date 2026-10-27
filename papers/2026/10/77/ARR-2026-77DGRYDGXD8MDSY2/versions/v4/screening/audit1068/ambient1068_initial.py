"""Own full-matrix construction, exact characteristic polynomials and ambient logarithms."""
from pathlib import Path
import sympy as s,mpmath as mp,json,traceback
P=Path(__file__).parent;mp.mp.dps=90;rows=[]
def mm(a):return mp.matrix([[mp.mpf(str(s.N(a[i,j],100))) for j in range(a.cols)] for i in range(a.rows)])
def tr(a):return sum(a[i,i] for i in range(a.rows))
def spec(a):
 ev,V=mp.eigh(a);assert min(ev)>0
 return ev,V,V*mp.diag([mp.log(v) for v in ev])*V.T
cases=[('1063',2,s.Rational(1,4),s.Rational(1,2)),('1063',3,s.Rational(1,9),s.Rational(1,3)),('1063',5,s.Rational(1,25),s.Rational(1,5)),('1066',3,s.Rational(1,3),s.Rational(1,9)),('1066',4,s.Rational(1,16),s.Rational(1,256)),('1066',5,s.Rational(1,5),s.Rational(1,25)),('small_x_gt1',3,s.Rational(2),s.Rational(1,9))]
try:
 for name,d,x,delta in cases:
  n=d*d;a=d-1;q=a+x;theta=1-delta;lam=-s.Rational(1,n-1);e=s.sqrt(x)
  v=s.zeros(n,1);v[0]=e
  for j in range(1,d):v[j*d+j]=1
  pure=v*v.T/q
  ptr=lambda z:s.Matrix(d,d,lambda r,k:sum(z[j*d+r,j*d+k] for j in range(d)))
  marginal=ptr(pure);B=s.kronecker_product(s.eye(d)/d,marginal);state=delta*B+theta*pure
  H=s.kronecker_product(s.diag(0,*([1]*a)),s.eye(d));U=s.eye(n)-2*H;rho=U*state*U.T
  assert s.trace(state)==1 and s.trace(rho)==1 and ptr(state)==ptr(rho)==marginal and U*U.T==s.eye(n)
  Binvhalf=s.diag(*[1/s.sqrt(B[j,j]) for j in range(n)]);white=s.simplify(Binvhalf*state*Binvhalf)
  assert s.simplify(s.trace(Binvhalf*pure*Binvhalf))==n
  K=delta+theta*n;assert s.factor((white-delta*s.eye(n)).trace()-theta*n)==0
  out=lam*state+(1-lam)*B;outr=lam*rho+(1-lam)*B;assert s.simplify(outr-U*out*U.T)==s.zeros(n)
  active=s.zeros(n,2);active[0,1]=1
  for j in range(1,d):active[j*d+j,0]=1/s.sqrt(a)
  assert active.T*active==s.eye(2)
  z=s.symbols('z');spectra=[]
  for label,m,p in [('input',state,theta),('output',out,lam*theta)]:
   W=s.simplify(active.T*m*active);A=1+(d*a-1)*p;F=1+a*p
   expected=s.Matrix([[A,d*p*e*s.sqrt(a)],[d*p*e*s.sqrt(a),F*x]])/(d*q)
   assert s.simplify(W-expected)==s.zeros(2)
   low0=(1-p)*x/(d*q);low1=(1-p)/(d*q)
   expected_char=(z-low0)**(d-1)*(z-low1)**(n-d-1)*(z*z-s.trace(W)*z+W.det())
   assert s.Poly(m.charpoly(z).as_expr()-expected_char,z).is_zero
   spectra.append({'label':label,'inactive_R0':str(low0),'multiplicity_R0':d-1,'inactive_other':str(low1),'multiplicity_other':n-d-1,'active_trace':str(s.factor(s.trace(W))),'active_determinant':str(s.factor(W.det()))})
  si=mm(state);ri=mm(rho);so=mm(out);ro=mm(outr)
  ei,Vi,li=spec(si);er,Vr,lr=spec(ri);eo,Vo,lo=spec(so);eor,Vor,lor=spec(ro)
  din=tr(ri*(lr-li));dout=tr(ro*(lor-lo));assert din>0 and dout>0
  ci=theta**2*x*a/q**2
  def ell(p):
   W=s.simplify(active.T*(p*pure+(1-p)*B)*active);ew,_=mp.eigh(mm(W));return (mp.log(ew[1])-mp.log(ew[0]))/(ew[1]-ew[0])
  expected_in=mp.mpf(str(s.N(4*ci,100)))*ell(theta);expected_out=mp.mpf(str(s.N(4*lam**2*ci,100)))*ell(lam*theta)
  err=max(abs(din/expected_in-1),abs(dout/expected_out-1));assert err<mp.mpf('1e-70')
  min_exact=delta*min(s.Rational(1),x)/(d*q);assert abs(ei[0]/mp.mpf(str(s.N(min_exact,100)))-1)<mp.mpf('1e-70')
  output_max=(1-lam*theta)*max(s.Rational(1),x)/(d*q);assert abs(eo[-1]/mp.mpf(str(s.N(output_max,100)))-1)<mp.mpf('1e-70')
  # Direct physical tangent is imaginary; evaluate BKM in the full ambient eigensystem.
  tangent=-mp.j*(mm(H)*si-si*mm(H));te=Vi.T*tangent*Vi;g=mp.mpf(0)
  for j in range(n):
   for k in range(n):
    kernel=1/ei[j] if abs(ei[j]-ei[k])<mp.mpf('1e-80') else (mp.log(ei[j])-mp.log(ei[k]))/(ei[j]-ei[k])
    g+=abs(te[j,k])**2*kernel
  assert abs(din/(2*g)-1)<mp.mpf('1e-70')
  rows.append({'family':name,'d':d,'x_e_squared':str(x),'delta':str(delta),'actual_order':str(K),'normalization_marginal_unitary_covariance':True,'full_characteristic_polynomials_verified':spectra,'input_min_exact':str(min_exact),'output_max_exact':str(output_max),'direct_ambient_Dinput':str(din),'direct_ambient_Doutput':str(dout),'direct_ambient_ratio':str(dout/din),'relative_error_against_plane':str(err),'Dpi_equals_two_BKM_checked':True,'precision_digits':90})
  print(name,d,'ok',flush=True)
 (P/'AMBIENT1068.json').write_text(json.dumps({'construction':'Full d^2 matrices first; exact partial traces, whitening, characteristic polynomials; independent full eigensystem logarithms at90digits. Geometry is same1051 family, no independence claim.','cases':rows},indent=2)+'\n',encoding='utf-8')
except Exception as ex:
 (P/'AMBIENT_FAILURE1068.json').write_text(json.dumps({'error':repr(ex),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise

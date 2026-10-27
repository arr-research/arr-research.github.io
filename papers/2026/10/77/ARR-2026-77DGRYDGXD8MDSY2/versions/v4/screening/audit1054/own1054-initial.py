from pathlib import Path
import sympy as s,mpmath as m,json,traceback
P=Path(__file__).parent;m.mp.dps=85;rows=[]
def save(): (P/'OWN1054.json').write_text(json.dumps({'records':rows},indent=2)+'\n',encoding='utf-8')
def tr(X):return sum(X[i,i] for i in range(X.rows))
def pt(X,d):return s.Matrix(d,d,lambda j,k:sum(X[i*d+j,i*d+k] for i in range(d)))
def build(d,e,theta):
 n=d*d;q=d-1+e*e;v=s.zeros(n,1);v[0]=e
 for j in range(1,d):v[j*d+j]=1
 sig=v*v.T/q;r=pt(sig,d);B=s.kronecker_product(s.eye(d)/d,r);H=s.diag(*[int(i//d>0) for i in range(n)]);S=(1-theta)*B+theta*sig
 return v,sig,r,B,H,S
def quad(A,B,D):
 n=A.rows;K=s.kronecker_product(s.eye(n),A)+s.kronecker_product(B.T,s.eye(n));v=s.Matrix([D[i,j] for j in range(n) for i in range(n)]);y=K.inv()*v
 assert K*y==v
 return s.simplify((v.conjugate().T*y)[0])
def mp(X):return m.matrix([[m.mpc(str(s.re(x).evalf(90)),str(s.im(x).evalf(90))) for x in X.row(i)] for i in range(X.rows)])
def eig(X):return m.eighe(X)
def logm(X):
 v,U=eig(X);return U*m.diag([m.log(x) for x in v])*U.H
def du(A,B):return m.re(tr(A*(logm(A)-logm(B))))
def metric(S,Z,bkm):
 v,U=eig(S);T=U.H*Z*U
 def k(x,y):return (1/x if abs(x-y)<m.mpf('1e-70') else m.log(x/y)/(x-y)) if bkm else 2/(x+y)
 return m.re(sum(abs(T[i,j])**2*k(v[i],v[j]) for i in range(S.rows) for j in range(S.rows)))
def tri(A,B):
 a,U=eig(A);b,V=eig(B);O=U.H*V
 return sum((a[i]-b[j])**2/(a[i]+b[j])*abs(O[i,j])**2 for i in range(A.rows) for j in range(B.rows))
try:
 d,e,p=s.symbols('d e p',real=True);a=d-1;q=a+e*e;A=1+(d*a-1)*p;F=1+a*p
 W=s.Matrix([[A,d*p*e*s.sqrt(a)],[d*p*e*s.sqrt(a),F*e*e]])/(d*q);T=s.Matrix([[0,-s.I*s.sqrt(a)],[s.I*s.sqrt(a),0]])
 assert s.simplify(W*T+T*W-s.trace(W)*T)==s.zeros(2)
 assert s.factor(W.det()-e*e*(1-p)*(1+(d*d-1)*p)/(d*d*q*q))==0
 h=A/(d*a);k=s.factor((A*F-d*d*p*p*a)/(d*a*A));assert s.factor(k-(1-p)*(1+(d*d-1)*p)/(d*a*A))==0
 rows.append({'name':'general_symbolic','determinant':str(s.factor(W.det())),'ell_log_coefficient':str(2/h),'small_eigen_coefficient_e2':str(k),'SLD_identity':True})
 for dim in [2,3,4,5,6]:
  eps=s.Rational(1,7);theta=s.Rational(7,9);v,sig,r,B,H,S=build(dim,eps,theta);n=dim*dim;Z=-s.I*(H*S-S*H);U=s.eye(n)+(s.Rational(3,5)-s.I*s.Rational(4,5)-1)*H;R=U*S*U.H
  assert tr(sig)==1 and pt(Z,dim)==s.zeros(dim) and pt(R,dim)==r and H*H==H and U*U.H==s.eye(n)
  assert (v.T*B.inv()*v)[0]/(dim-1+eps*eps)==n
  assert B.inv()*sig*(B.inv()*v)==n*(B.inv()*v)
  assert B.inv()*sig*v!=n*v # retains and detects the original mistaken eigenvector.
  Q=s.zeros(n,2);Q[0,1]=1
  for j in range(1,dim):Q[j*dim+j,0]=1/s.sqrt(dim-1)
  assert s.simplify(Q.T*S*Q-W.subs({d:dim,e:eps,p:theta}))==s.zeros(2)
  assert s.simplify(Z-Q*(Q.T*Z*Q)*Q.T)==s.zeros(n)
  assert s.simplify(R-S-Q*(Q.T*(R-S)*Q)*Q.T)==s.zeros(n)
  rows.append({'name':'ambient_geometry','d':dim,'R':dim,'all_exact':True,'wrong_original_eigenvector_detected':True})
 save()
 # Full81-variable inversions with complex rational phase, not a plane solver.
 dim=3;eps=s.Rational(1,100);theta=s.Rational(99,100);lam=-s.Rational(1,8);v,sig,r,B,H,S=build(dim,eps,theta);n=9;U=s.eye(n)+(s.Rational(3,5)-s.I*s.Rational(4,5)-1)*H;R=U*S*U.H;O=lam*S+(1-lam)*B;OR=lam*R+(1-lam)*B;Z=-s.I*(H*S-S*H)
 assert OR==U*O*U.H
 pivots={}
 for label,X in [('base',S),('phase',R),('output_base',O),('output_phase',OR),('slack_base',n*B-S),('slack_phase',n*B-R)]:
  L,V=X.LDLdecomposition(hermitian=True);assert L*V*L.H==X;assert all(s.simplify(V[i,i])>0 for i in range(n));pivots[label]=[str(s.simplify(V[i,i])) for i in range(n)]
 gin=2*quad(S,S,Z);gout=2*quad(O,O,lam*Z);tin=quad(R,S,R-S);tout=quad(OR,O,OR-O)
 wp=W.subs({d:dim,e:eps,p:theta});wo=W.subs({d:dim,e:eps,p:lam*theta});cc=theta**2*eps**2*(dim-1)/(dim-1+eps**2)**2
 assert s.simplify(gin-4*cc/s.trace(wp))==0
 assert s.simplify(tin-4*cc*s.Rational(2,5)/s.trace(wp))==0
 predicted=lam**2*s.trace(wp)/s.trace(wo);assert s.factor(gout/gin-predicted)==0 and s.factor(tout/tin-predicted)==0
 rows.append({'name':'ambient81_rational_complex_phase','d':3,'e':'1/100','theta':'99/100','lambda':'-1/8','exp_minus_i_phi':'(3-4i)/5','SLD_input':str(gin),'triangular_input':str(tin),'retention_exact':str(s.factor(predicted)),'actual_order':'223/25','positive_LDL_pivots':pivots});save()
 # Complex Hermitian spectral controls at finite phases, distinct from input real-pi implementation.
 for dim,eps,theta,lam,phase in [(3,s.Rational(1,100),s.Rational(99,100),-s.Rational(1,8),'pi'),(4,s.Rational(1,100),s.Rational(99,100),-s.Rational(1,15),'pi'),(3,s.Rational(1,7),s.Rational(7,9),s.Rational(1,2),'complex'),(4,s.Rational(1,7),s.Rational(7,9),-s.Rational(1,15),'complex')]:
  v,sig,r,B,H,S=build(dim,eps,theta);n=dim*dim;u=-1 if phase=='pi' else (s.Rational(3,5)-s.I*s.Rational(4,5));cs=-1 if phase=='pi' else s.Rational(3,5);U=s.eye(n)+(u-1)*H;R=U*S*U.H;O=lam*S+(1-lam)*B;OR=lam*R+(1-lam)*B;Z=-s.I*(H*S-S*H)
  sm,rm,om,orm,zm=map(mp,[S,R,O,OR,Z]);din=du(rm,sm);dout=du(orm,om);rin=dout/din;bk=metric(om,mp(lam*Z),True)/metric(sm,zm,True);sl=metric(om,mp(lam*Z),False)/metric(sm,zm,False);trir=tri(orm,om)/tri(rm,sm)
  wp=mp(W.subs({d:dim,e:eps,p:theta}));wo=mp(W.subs({d:dim,e:eps,p:lam*theta}));cc=m.mpf(str((theta**2*eps**2*(dim-1)/(dim-1+eps**2)**2).evalf(90)));lv,_=eig(wp);ell=m.log(lv[1]/lv[0])/(lv[1]-lv[0]);pred=2*cc*ell*(1-m.mpf(str(cs)))
  errors=[abs(din-pred),abs(rin-bk),abs(sl-trir),abs(sl-m.mpf(str(lam))**2*tr(wp)/tr(wo)),abs(du(sm,rm)-din)]
  assert max(errors)<m.mpf('1e-65')
  rows.append({'name':'complex_full_spectral','d':dim,'e':str(eps),'theta':str(theta),'lambda':str(lam),'phase':phase,'input_DU':str(din),'ratio_DU_BKM':str(rin),'ratio_SLD_triangular':str(sl),'reverse_also_equals_forward_for_this_special_orbit':True,'max_identity_error':str(max(errors))});save()
 # Orientation detector outside the symmetric orbit.
 rr=m.diag([m.mpf(1)/10,m.mpf(2)/10,m.mpf(3)/10,m.mpf(4)/10]);ss=m.diag([m.mpf(1)/4,m.mpf(1)/4,m.mpf(1)/5,m.mpf(3)/10]);forward=du(rr,ss);reverse=du(ss,rr)
 assert abs(forward-reverse)>m.mpf('1e-4')
 rows.append({'name':'off_orbit_orientation','forward':str(forward),'reverse':str(reverse),'distinct':True})
 # Genuine falsifier of extending finite-phase=local-BKM to arbitrary unitary orbits.
 ss=m.matrix([[m.mpf('.5'),m.mpf('.1'),m.mpf('.05')],[m.mpf('.1'),m.mpf('.3'),m.mpf('.04')],[m.mpf('.05'),m.mpf('.04'),m.mpf('.2')]])
 hh=m.diag([0,m.mpf('.5'),1]);uu=m.diag([1,-1j,-1]);rr=uu*ss*uu.H;zz=-1j*(hh*ss-ss*hh);oo=ss/2+m.eye(3)/6;orr=rr/2+m.eye(3)/6
 rf=du(orr,oo)/du(rr,ss);rb=metric(oo,zz/2,True)/metric(ss,zz,True)
 assert abs(rf-rb)>m.mpf('1e-8')
 rows.append({'name':'falsifier_generic_phase_extension','same_reference_R1':True,'H_norm':1,'phase':'pi','lambda':'1/2','sigma_entries':'[[.5,.1,.05],[.1,.3,.04],[.05,.04,.2]]','H':'diag(0,.5,1)','finite_DU_retention':str(rf),'local_BKM_retention':str(rb),'difference':str(rf-rb),'scope':'Refutes only an unrestricted extension of the special1051 identity, not1051 itself.'})
 rows.append({'name':'complete','passed':True});save();print('Own ambient, rational, spectral, orientation and adverse-extension controls passed.')
except Exception as ex:
 (P/'OWN_FAILURE1054.json').write_text(json.dumps({'error':repr(ex),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise

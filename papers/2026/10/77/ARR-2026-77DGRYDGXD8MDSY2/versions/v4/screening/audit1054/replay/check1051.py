from pathlib import Path
import sympy as s, mpmath as mp, json, datetime
C=Path(__file__).parent;mp.mp.dps=100
d,p,e=s.symbols('d p e',positive=True);a=d-1;q=a+e**2
A=1+(d*a-1)*p;F=1+(d-1)*p
W=s.Matrix([[A,d*p*e*s.sqrt(a)],[d*p*e*s.sqrt(a),F*e**2]])/(d*q)
det=s.factor(W.det());expected=e**2*(1-p)*(1+(d*d-1)*p)/(d*d*q*q)
assert s.simplify(det-expected)==0
T=s.Matrix([[0,-s.I*s.sqrt(a)],[s.I*s.sqrt(a),0]])
Y=2*T/s.trace(W);assert s.simplify(W*Y+Y*W-2*T)==s.zeros(2)
assert s.simplify(s.trace(T*Y)-4*a/s.trace(W))==0
geometry=[]
for dim in [2,3,4,5]:
 eps=s.Rational(1,10);n=dim*dim;aa=dim-1;qq=aa+eps**2
 v=s.zeros(n,1);v[0]=eps
 for j in range(1,dim):v[j*dim+j]=1
 sigma=v*v.T/qq
 marginal=s.diag(eps**2/qq,*([1/qq]*aa));B=s.kronecker_product(s.eye(dim)/dim,marginal)
 H=s.kronecker_product(s.diag(0,*([1]*aa)),s.eye(dim))
 U=s.eye(n)-2*H
 theta=s.Rational(9,10);base=(1-theta)*B+theta*sigma
 Z=-s.I*(H*base-base*H)
 pt=lambda X:s.Matrix(dim,dim,lambda j,k:sum(X[i*dim+j,i*dim+k] for i in range(dim)))
 assert pt(Z)==s.zeros(dim) and pt(U*base*U)==marginal
 assert (v.T*B.inv()*v)[0]/qq==dim**2
 assert B.inv()*sigma*(B.inv()*v)==dim**2*(B.inv()*v)
 assert H*H==H and U*U==s.eye(n)
 Q=s.zeros(n,2);Q[0,1]=1
 for j in range(1,dim):Q[j*dim+j,0]=1/s.sqrt(aa)
 wp=W.subs({d:dim,p:theta,e:eps})
 assert s.simplify(Q.T*base*Q-wp)==s.zeros(2)
 assert s.simplify(Q.T*Z*Q-theta*eps/qq*T.subs(d,dim))==s.zeros(2)
 # The complement has no tangent. All assertions are exact ambient matrices.
 assert s.simplify(Z-Q*(Q.T*Z*Q)*Q.T)==s.zeros(n)
 geometry.append(dict(d=dim,reference=dim,ambient=n,exact=True))
def ell(dim,theta,eps):
 aa=mp.mpf(dim-1);qq=aa+eps*eps
 aa0=1+(dim*aa-1)*theta;ff=1+(dim-1)*theta
 tr=(aa0+ff*eps*eps)/(dim*qq)
 dt=eps*eps*(1-theta)*(1+(dim*dim-1)*theta)/(dim*dim*qq*qq)
 delta=mp.sqrt(tr*tr-4*dt);hi=(tr+delta)/2;lo=dt/hi
 return (mp.log(hi)-mp.log(lo))/delta
rows=[]
for dim in [2,3,4]:
 for lam in [mp.mpf('0.5'),-1/mp.mpf(dim*dim-1)]:
  for exp in [2,6,12,30]:
   eps=mp.mpf(10)**(-exp);theta=mp.mpf('0.99');P=dim*(dim-1)
   rat=lam*lam*ell(dim,lam*theta,eps)/ell(dim,theta,eps)
   cc=lambda k:lam*lam*k/(1+lam*(k-1))
   c=theta*eps*mp.sqrt(dim-1)/(dim-1+eps*eps)
   du=4*c*c*ell(dim,theta,eps)
   rows.append(dict(d=dim,lambda_=str(lam),e_exponent=exp,theta='99/100',phase='pi',ratio=str(rat),input_relative_entropy=str(du),bell_endpoint=str(cc(mp.mpf(dim*dim)/2)),above_specific_bell_endpoint=bool(rat>cc(mp.mpf(dim*dim)/2)),fixed_theta_asymptote=str(cc(1+(P-1)*theta)),nature='100digit diagnostic, not interval certificate'))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),symbolic=dict(det=str(det),positive_domain='-1/(d²-1)<p<1',sld_sylvester_identity=True),geometry=geometry,finite_phase_diagnostics=rows,technical_audit_pending=True,no_score=True,full_review1048_excludes_this=True)
(C/'CHECK1051.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(geometry=len(geometry),diagnostics=len(rows),positive_gaps=sum(x['above_specific_bell_endpoint'] for x in rows))))

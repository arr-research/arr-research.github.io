from pathlib import Path
import mpmath as mp,sympy as s,json
P=Path(__file__).parent;mp.mp.dps=250
def blocks(d,e,p):
 a=d-1;q=a+e*e
 return mp.matrix([[1+(d*a-1)*p,d*p*e*mp.sqrt(a)],[d*p*e*mp.sqrt(a),(2+(d-2)*p)*e*e]])/(2*d*q),mp.matrix([[0,mp.sqrt(a)],[mp.sqrt(a),2*e]])
def spectral(W):
 A,B,C=W[0,0],W[0,1],W[1,1];delta=mp.sqrt((A-C)**2+4*B*B);hi=(A+C+delta)/2;lo=mp.det(W)/hi
 assert lo>0 and hi>lo
 return hi,lo,(A-C)/delta,2*B/delta
def bkm(W,T):
 hi,lo,c2,s2=spectral(W);off=T[0,1]*c2+(T[1,1]-T[0,0])*s2/2
 zh=T[0,0]*(1+c2)/2+T[1,1]*(1-c2)/2+T[0,1]*s2
 zl=T[0,0]*(1-c2)/2+T[1,1]*(1+c2)/2-T[0,1]*s2
 return zh*zh/hi+zl*zl/lo+2*off*off*(mp.log(hi)-mp.log(lo))/(hi-lo)
def logmatrix(W):
 hi,lo,_,_=spectral(W);return mp.log(lo)*mp.eye(2)+(mp.log(hi)-mp.log(lo))/(hi-lo)*(W-lo*mp.eye(2))
trace=lambda A:A[0,0]+A[1,1]
def pairD(W,T,t):
 LW=logmatrix(W);return sum(trace((W+sgn*t*T)*(logmatrix(W+sgn*t*T)-LW)) for sgn in [-1,1])
rows=[];finite=[]
for d in [2,3,4]:
 a=d-1;theta=mp.mpf('0.99');K=d*a;M=mp.mpf(d*(2*d-1))/2
 for lam in [-mp.mpf(1)/(d*d-1),mp.mpf('.5')]:
  target=lam*lam*(1+(K-1)*theta)/(1+lam*(K-1)*theta)
  diag=[]
  for es in ['1e-4','1e-12','1e-30','1e-50']:
   e=mp.mpf(es);W,T=blocks(d,e,theta);O,_=blocks(d,e,lam*theta);g=bkm(W,T);ratio=lam*lam*bkm(O,T)/g
   asympt=8*d*a*a/(1+(K-1)*theta);diag.append(dict(e=es,ratio=str(ratio),fixed_theta_limit=str(target),difference=str(ratio-target),G_over_log=str(g/mp.log(1/e)),log_coefficient=str(asympt)))
  assert abs(mp.mpf(diag[-1]['difference']))<mp.mpf('.01')
  rows.append(dict(d=d,lambda_=str(lam),theta=str(theta),diagnostics=diag))
  if d>2:
   e=mp.mpf('1e-30');t=mp.mpf('1e-90');W,T=blocks(d,e,theta);O,_=blocks(d,e,lam*theta)
   metric=lam*lam*bkm(O,T)/bkm(W,T);du=pairD(W,T,t);do=pairD(O,T,lam*t);ratio=do/du
   assert du>0 and do>0 and abs(ratio-metric)<mp.mpf('1e-25')
   bell=lam*lam*(mp.mpf(d*d)/2)/(1+lam*(mp.mpf(d*d)/2-1));assert ratio>bell
   # Exact rational/surd Sylvester-plane positivity and order slacks.
   ee=s.Rational(1,10**30);tt=s.Rational(1,10**90);th=s.Rational(99,100);ll=-s.Rational(1,d*d-1) if lam<0 else s.Rational(1,2);mm=s.Rational(d*(2*d-1),2);qq=a+ee*ee
   WW=lambda p:s.Matrix([[1+(d*a-1)*p,d*p*ee*s.sqrt(a)],[d*p*ee*s.sqrt(a),(2+(d-2)*p)*ee*ee]])/(2*d*qq)
   TT=s.Matrix([[0,s.sqrt(a)],[s.sqrt(a),2*ee]]);BB=s.diag(1,2*ee*ee)/(2*d*qq);cert=[]
   for sign in [-1,1]:
    for name,mat in [('rho',WW(th)+sign*tt*TT),('output',WW(ll*th)+sign*ll*tt*TT),('order_slack',mm*BB-WW(th)-sign*tt*TT)]:
     det=s.factor(mat.det());assert mat[0,0]>0 and det>0;cert.append(dict(name=name,sign=sign,first_diagonal=str(mat[0,0]),determinant=str(det),positive=True))
   finite.append(dict(d=d,R=2*d-1,lambda_=str(lam),e='1e-30',t='1e-90',theta='99/100',kappa=str(M),Umegaki_ratio=str(ratio),BKM_ratio=str(metric),Bell_endpoint=str(bell),difference_from_Bell=str(ratio-bell),input_divergence=str(du),output_divergence=str(do),exact_plane_certificates=cert,numerical_logarithms_not_interval_certified=True))
out=dict(scope='Bounded diagnostics for exploratory1035; not an exact finite logarithmic certificate, universal proof, novelty audit or score',precision_digits=mp.mp.dps,diagnostics=rows,finite_pairs=finite,all_declared_checks_passed=True)
(P/'CHECK1035.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(diagnostics=len(rows),finite_pairs=len(finite),all_declared_checks_passed=True)))

"""Fixed controls for1048; no sampling, optimizer or changes to frozen inputs."""
from pathlib import Path
import json,traceback,sympy as s,mpmath as mp
from fractions import Fraction
P=Path(__file__).parent;R=s.Rational;mp.mp.dps=90;out={'checks':[]}
def emit(name,**v):
 out['checks'].append({'name':name,**v});(P/'OWN1048.json').write_text(json.dumps(out,indent=2,default=str)+'\n');print(name,flush=True)
def zero(A):return all(s.simplify(x)==0 for x in A)
try:
 d,p,e=s.symbols('d p e',positive=True);a=d-1;q=a+e**2;M=d*(2*d-1)/2;PP=d*a
 W=s.Matrix([[1+(d*a-1)*p,d*p*e*s.sqrt(a)],[d*p*e*s.sqrt(a),(2+(d-2)*p)*e**2]])/(2*d*q)
 T=s.Matrix([[0,s.sqrt(a)],[s.sqrt(a),2*e]])
 # Direct solve of the three-dimensional linear system, rather than assuming inverse identity.
 x,y,z=s.symbols('x y z');Y=s.Matrix([[x,y],[y,z]])
 sy=s.solve([v for v in (W*Y+Y*W-2*T)],[x,y,z]);Y=Y.subs(sy);G=s.factor(s.trace(T*Y));limit=s.factor(s.limit(G,e,0))
 assert s.factor(limit-8*a*M/(1+(M-1)*p))==0
 identity=(T+W.det()*W.inv()*T*W.inv())/s.trace(W);assert zero(Y-identity)
 A=1+(PP-1)*p;C=2+(d-2)*p;detcore=s.factor(A*C-d*d*p*p*a)
 assert s.factor(detcore-2*(1-p)*(1+(M-1)*p))==0
 small=(1-p)*(1+(M-1)*p)/(d*a*A);large=A/(2*d*a);rotation=d*p*s.sqrt(a)/A
 assert s.factor(2-2*s.sqrt(a)*rotation-2*(1-p)/A)==0
 logcoef=s.factor(4*a/large);assert s.factor(logcoef-8*d*a*a/A)==0
 lam,k=s.symbols('lambda k',real=True);CC=lambda K:lam**2*K/(1+lam*(K-1))
 derivative=s.factor(s.diff(CC(k),k));assert s.factor(derivative-lam**2*(1-lam)/(1+lam*(k-1))**2)==0
 crossover=s.factor(1+(M-1)*(d*d/2-1)/(PP-1))
 assert s.factor(CC(PP).subs(lam,-1/(d*d-1))-1/(d+1))==0
 assert s.factor(CC(d*d/2).subs(lam,-1/(d*d-1))-1/(d*d-1))==0
 emit('symbolic_principal_plane_and_BKM',SLD_general=str(G),SLD_limit=str(limit),determinant_core=str(detcore),eigenvalue_coefficients={'large':str(large),'small_e2':str(small)},BKM_log_coefficient=str(logcoef),C_derivative=str(derivative),budget_crossover=str(crossover),domain='Identities rational; positivity justified analytically for d>=2 and -1/(M-1)<p<1. Symbol declarations do not replace domain analysis.')
 # Geometry at a new fixed dimension, exact rational matrices.
 n=5;r=2*n-1;N=n*r;ee=R(2,7);aa=n-1;qq=aa+ee**2;V=s.zeros(N,2);bs=s.zeros(N,2)
 for j in range(aa):V[(j+1)*r+j,0]=1;V[j*r+aa+j,1]=1
 V[r-1,0]=ee;V[(n-1)*r+r-1,1]=ee;bs[r-1,0]=1;bs[(n-1)*r+r-1,1]=1
 sig=V*V.T/(2*qq);D=V[:,0]*bs[:,0].T+bs[:,0]*V[:,0].T-V[:,1]*bs[:,1].T-bs[:,1]*V[:,1].T
 ptr=lambda X:s.Matrix(r,r,lambda i,j:sum(X[h*r+i,h*r+j] for h in range(n)))
 B=s.kronecker_product(s.eye(n)/n,ptr(sig));cap=R(n*(2*n-1),2);Q=2*sig
 assert ptr(D)==s.zeros(r) and s.trace(sig)==1
 assert V.T*B.inv()*V/(2*qq)==cap*s.eye(2)
 assert zero(Q*Q-Q) and zero((s.eye(N)-Q)*D*(s.eye(N)-Q))
 assert s.factor(4*s.trace(D*D)-2*s.trace((Q*D*Q)**2))==16*qq
 # All support plane/complement residuals, constructed from actual coordinate lists.
 th=R(4,5);sigma=(1-th)*B+th*sig;planes=[]
 for h in range(2):
  u=(V[:,h]-ee*bs[:,h])/s.sqrt(aa);basis=s.Matrix.hstack(u,bs[:,h]);wp=basis.T*sigma*basis;tp=basis.T*D*basis
  expected=W.subs({d:n,p:th,e:ee});assert zero(wp-expected);assert zero(sigma*basis-basis*wp);assert zero(D*basis-basis*tp)
  assert zero(tp-((-1)**h)*T.subs({d:n,e:ee}));planes.append(basis)
 projector=sum((K*K.T for K in planes),s.zeros(N));assert zero(D-projector*D*projector)
 emit('exact_ambient_d5_geometry',dimension=N,R=r,e=str(ee),Gram=str(cap)+' I2',Tr_A_D_zero=True,SLD_boundary=str(16*qq),both_planes_exact=True,no_tangent_in_remaining_modes=True)
 # Full complex ambient calculation at moderate scales. Numerical diagnostic, not interval proof.
 n=3;r=5;N=n*r;ee=R(1,3);th=R(7,10);tt=R(1,10000);ll=-R(1,8);aa=n-1;qq=aa+ee**2
 V=s.zeros(N,2);bs=s.zeros(N,2)
 for j in range(aa):V[(j+1)*r+j,0]=1;V[j*r+aa+j,1]=1
 V[r-1,0]=ee;V[(n-1)*r+r-1,1]=ee;bs[r-1,0]=1;bs[(n-1)*r+r-1,1]=1
 sig=V*V.T/(2*qq);D=V[:,0]*bs[:,0].T+bs[:,0]*V[:,0].T-V[:,1]*bs[:,1].T-bs[:,1]*V[:,1].T
 ptr=lambda X:s.Matrix(r,r,lambda i,j:sum(X[h*r+i,h*r+j] for h in range(n)))
 B=s.kronecker_product(s.eye(n)/n,ptr(sig));sig=(1-th)*B+th*sig;rho=sig+tt*D
 UA=s.eye(n);UA[:2,:2]=s.Matrix([[R(3,5),R(4,5)*s.I],[R(4,5)*s.I,R(3,5)]])
 UR=s.diag(1,s.I,-1,-s.I,1);U=s.kronecker_product(UA,UR)
 rs=(U*sig*U.H).applyfunc(s.simplify);rr=(U*rho*U.H).applyfunc(s.simplify);rd=(U*D*U.H).applyfunc(s.simplify)
 assert zero(U.H*U-s.eye(N)) and zero(ptr(rr)-ptr(rs)) and not zero(rs*rr-rr*rs)
 dep=lambda X:(ll*X+(1-ll)*s.kronecker_product(s.eye(n)/n,ptr(X))).applyfunc(s.simplify)
 ns,nr,nd=dep(rs),dep(rr),ll*rd
 assert zero(nr-ns-tt*nd)
 def num(X):return mp.matrix([[mp.mpc(str(s.N(s.re(X[i,j]),100)),str(s.N(s.im(X[i,j]),100))) for j in range(X.cols)] for i in range(X.rows)])
 trace=lambda X:sum(X[i,i] for i in range(X.rows))
 def metrics(S,Z):
  ev,uv=mp.eighe(S);assert min(ev)>0;zz=uv.H*Z*uv;sl=mp.mpf(0);bk=mp.mpf(0)
  for i in range(S.rows):
   for j in range(S.rows):
    v=abs(zz[i,j])**2;sl+=2*v/(ev[i]+ev[j]);delta=ev[i]-ev[j]
    kernel=2/(ev[i]+ev[j]) if abs(delta)<mp.mpf('1e-75') else (mp.log(ev[i])-mp.log(ev[j]))/delta
    bk+=v*kernel
  return sl,bk,min(ev)
 def logm(S):
  ev,uv=mp.eighe(S);assert min(ev)>0;return uv*mp.diag([mp.log(v) for v in ev])*uv.H
 def rel(A,B):return mp.re(trace(A*(logm(A)-logm(B))))
 sin,bin,mineig=metrics(num(rs),num(rd));sout,bout,minout=metrics(num(ns),num(nd))
 du=rel(num(rr),num(rs));reverse=rel(num(rs),num(rr));dou=rel(num(nr),num(ns));assert du>0 and dou>0 and abs(du-reverse)>mp.mpf('1e-65')
 sl0,bk0,_=metrics(num(sig),num(D));assert abs(sin-sl0)<mp.mpf('1e-70') and abs(bin-bk0)<mp.mpf('1e-70')
 # Direct non-normalized principal-plane global sums for orientation/normalization comparison.
 def pair(p,t):
  w=num(W.subs({d:n,e:ee})).apply if False else num(W.subs({d:n,e:ee,globals()['p']:p}))
  tangent=num(T.subs({d:n,e:ee}));return rel(w+t*tangent,w)+rel(w-t*tangent,w)
 blockin=pair(th,mp.mpf(1)/10000);blockout=pair(ll*th,-mp.mpf(1)/80000)
 assert abs(blockin-du)<mp.mpf('1e-70') and abs(blockout-dou)<mp.mpf('1e-70')
 emit('complex_full_ambient_orientation',dimension=N,precision_digits=90,parameters={'d':n,'e':str(ee),'theta':str(th),'t':str(tt),'lambda':str(ll)},input_min_eig=str(mineig),output_min_eig=str(minout),SLD_ratio=str(sout/sin),BKM_ratio=str(bout/bin),Umegaki_ratio=str(dou/du),D_rho_sigma=str(du),D_sigma_rho=str(reverse),block_vs_global_residual=str(abs(blockin-du)),unitary_invariance=True,numerical_not_interval=True)
 # Verify the displayed outward decimal bounds against reproduced exact dyadic certificates.
 iv=json.loads((P/'reproduction/integer_intervals1044/INTEGER_INTERVAL1044.json').read_text())['cases']
 bounds=[('0.11255711780015','0.11255711780017'),('0.00593846351695','0.00593846351696'),('0.11934942272408','0.11934942272410'),('0.00238915978275','0.00238915978276')]
 for row,(lo,hi) in zip(iv,bounds):
  c=row['positive_gap'];den=1<<c['denominator_power_of_2'];assert Fraction(lo)<Fraction(int(c['lower_integer']),den)<=Fraction(int(c['upper_integer']),den)<Fraction(hi)
 emit('all_four_manuscript_decimal_intervals',all_contain_reproduced_integer_enclosures=True,printed_bounds=bounds)
 out['all_passed']=True
except Exception:
 out['all_passed']=False;out['traceback']=traceback.format_exc();print(out['traceback'],flush=True);raise
finally:(P/'OWN1048.json').write_text(json.dumps(out,indent=2,default=str)+'\n')

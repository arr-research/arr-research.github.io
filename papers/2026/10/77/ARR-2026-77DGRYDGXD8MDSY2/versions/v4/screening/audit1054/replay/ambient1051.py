from pathlib import Path
import mpmath as m,json,datetime
m.mp.dps=95;C=Path(__file__).parent
def trace(X):return sum(X[i,i] for i in range(X.rows))
def eig(X):return m.eigsy(X)
def logmat(X):
 vals,U=eig(X);return U*m.diag([m.log(x) for x in vals])*U.T
def du(A,B):return trace(A*(logmat(A)-logmat(B)))
def triangular(A,B):
 av,AU=eig(A);bv,BU=eig(B);over=AU.T*BU
 return sum(bv[j]*((av[i]/bv[j]-1)**2/(av[i]/bv[j]+1))*over[i,j]**2 for i in range(A.rows) for j in range(B.rows))
def metric(S,Z,bkm):
 vals,U=eig(S);T=U.T*Z*U
 def kernel(x,y):
  if not bkm:return 2/(x+y)
  return 1/x if abs(x-y)<m.mpf('1e-80') else (m.log(x)-m.log(y))/(x-y)
 return sum(abs(T[i,j])**2*kernel(vals[i],vals[j]) for i in range(S.rows) for j in range(S.rows))
rows=[]
for d in [2,3,4]:
 a=d-1;e=m.mpf(1)/5;q=a+e*e;theta=m.mpf(3)/5;n=d*d
 v=m.matrix(n,1);v[0]=e
 for j in range(1,d):v[j*d+j]=1
 sig=v*v.T/q;B=m.diag([(e*e if j==0 else 1)/(d*q) for i in range(d) for j in range(d)])
 H=m.diag([0 if i==0 else 1 for i in range(d) for j in range(d)]);U=m.eye(n)-2*H
 S=(1-theta)*B+theta*sig;A=U*S*U
 Z=-1j*(H*S-S*H)
 def plane(p):return m.matrix([[1+(d*a-1)*p,d*p*e*m.sqrt(a)],[d*p*e*m.sqrt(a),(1+(d-1)*p)*e*e]])/(d*q)
 def ell(W):
  vv,_=eig(W);return (m.log(vv[1])-m.log(vv[0]))/(vv[1]-vv[0])
 for lam in [m.mpf('0.5'),-1/m.mpf(d*d-1)]:
  O=(1-lam)*B+lam*S;OA=U*O*U;OZ=lam*Z
  din=du(A,S);dout=du(OA,O);r=dout/din
  W=plane(theta);V=plane(lam*theta);c=theta*e*m.sqrt(a)/q
  predicted=lam*lam*ell(V)/ell(W)
  sl=metric(O,OZ,False)/metric(S,Z,False)
  bk=metric(O,OZ,True)/metric(S,Z,True)
  tri=triangular(OA,O)/triangular(A,S)
  errors=[abs(r-predicted),abs(bk-r),abs(sl-lam*lam*trace(W)/trace(V)),abs(tri-sl),abs(din-4*c*c*ell(W)),abs(triangular(A,S)-8*c*c/trace(W))]
  assert max(errors)<m.mpf('1e-75'),errors
  # Nonzero finite angle, bounded fixed local H; no tiny-t expansion used.
  rows.append(dict(d=d,lambda_=str(lam),e='1/5',theta='3/5',phase='pi',finite_UMEGAKI_ratio=str(r),BKM_ratio=str(bk),SLD_ratio=str(sl),triangular_ratio=str(tri),input_relative_entropy=str(din),max_identity_error=str(max(errors)),nature='95digit full ambient spectral diagnostic; not interval certificate'))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),rows=rows,all_six_identities_passed=True,universal_proof_not_from_finite_tests=True,audit_pending=True)
(C/'AMBIENT1051.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('Six ambient phase-pair cases validate all six identities at95digits; not an interval certificate.')

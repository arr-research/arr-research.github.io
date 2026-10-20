"""Search floats, then separately check rounded rational binary forms exactly."""
from pathlib import Path
from datetime import datetime,timezone
import cvxpy as cp,numpy as np,sympy as s,json,warnings
out=Path(__file__).resolve().parent/'certificate-search-33.json'
assert not out.exists()
records=[];F={0:-.75,1:1.275,-1:1.275};G={0:1,1:.3,-1:.3}
t=s.Symbol('t',real=True);X,Y=s.symbols('X Y',real=True)
for M in [1,2,3,4,6,8,12,16]:
 pv=cp.Variable(M,complex=True);eps=cp.Variable();A=cp.Variable((M+1,M+1),hermitian=True);B=cp.Variable((M+2,M+2),hermitian=True)
 def pk(k):
  if k==0:return 1
  if abs(k)>M:return 0
  return pv[k-1] if k>0 else cp.conj(pv[-k-1])
 def dk(k):return -M*sum(F[j]*pk(k-j) for j in F)-sum(G[j]*1j*(k-j)*pk(k-j) for j in G)
 constraints=[A>>0,B>>0,cp.real(cp.trace(A))==1-eps,cp.real(cp.trace(B))==cp.real(dk(0))-eps]
 for k in range(1,M+1):constraints.append(sum(A[j,j+k] for j in range(M+1-k))==pk(k))
 for k in range(1,M+2):constraints.append(sum(B[j,j+k] for j in range(M+2-k))==dk(k))
 prob=cp.Problem(cp.Maximize(eps),constraints)
 with warnings.catch_warnings(record=True) as caught:
  prob.solve(solver='CLARABEL',tol_gap_abs=1e-8,tol_gap_rel=1e-8,tol_feas=1e-8,max_iter=300)
 rec={'M':M,'polynomial_degree':2*M,'solver_status':prob.status,'floating_margin':float(eps.value),'warnings':[str(w.message) for w in caught]}
 print(json.dumps(rec),flush=True)
 if eps.value>1e-5:
  coeff=[s.Integer(1)]+[s.Rational(str(round(float(z.real),8)))+s.I*s.Rational(str(round(float(z.imag),8))) for z in pv.value]
  rho=X*X+Y*Y
  P=s.expand(rho**M+sum(2*s.re(coeff[k]*(X+s.I*Y)**(2*k))*rho**(M-k) for k in range(1,M+1)))
  H=rho+s.Rational(3,5)*(X*X-Y*Y);K=-s.Rational(3,4)*H+3*(X*X-Y*Y)
  f1=K*X-H*Y;f2=K*Y+H*X
  negLie=s.expand(-s.diff(P,X)*f1-s.diff(P,Y)*f2)
  # Binary homogeneous forms can be tested directly at(X,Y)=(t,1),
  # plus the separate point(1,0); homogeneity covers all directions.
  ptest=s.Poly(P.subs({X:t,Y:1}),t);ltest=s.Poly(negLie.subs({X:t,Y:1}),t)
  pr=int(ptest.count_roots(-s.oo,s.oo));lr=int(ltest.count_roots(-s.oo,s.oo))
  passed=pr==0 and lr==0 and ptest.eval(0)>0 and ltest.eval(0)>0 and P.subs({X:1,Y:0})>0 and negLie.subs({X:1,Y:0})>0
  rec.update(rational_coefficients=[str(v) for v in coeff],positive_polynomial=str(P),negative_lie=str(negLie),P_real_root_count=pr,negative_lie_real_root_count=lr,P_at_01=str(ptest.eval(0)),negative_lie_at_01=str(ltest.eval(0)),P_at_10=str(P.subs({X:1,Y:0})),negative_lie_at_10=str(negLie.subs({X:1,Y:0})),exact_positive_certificate=bool(passed))
  records.append(rec)
  if passed:break
 else:records.append(rec)
data={'created_at':datetime.now(timezone.utc).isoformat(),'field':'rho=x^2+y^2,H=rho+(3/5)(x^2-y^2),K=-(3/4)H+3(x^2-y^2);xdot=Kx-Hy,ydot=Ky+Hx;this is a=2','scope':'Floating search statuses are diagnostic. Any exact certificate flag follows a separate rational Sturm check of both binary forms; no minimum degree claim.','records':records}
out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8');print(json.dumps({'output':str(out),'records':len(records),'exact_certificate_found':any(r.get('exact_positive_certificate') for r in records)}),flush=True)

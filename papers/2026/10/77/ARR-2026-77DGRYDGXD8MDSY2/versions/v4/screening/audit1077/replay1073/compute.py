from pathlib import Path
from fractions import Fraction
import datetime,json,hashlib,shutil
import sympy as s
P=Path(__file__).parent
rows=[]
def zero(m):return all(s.simplify(x)==0 for x in m)
for d,e in [(2,s.Rational(1,2)),(3,s.Rational(1,3)),(4,s.Rational(1,2))]:
 n=d*d;a=d-1;q=a+e*e;theta=1-s.Rational(1,d*d);lam=-s.Rational(1,d*d-1)
 v=s.zeros(n,1);v[0]=e
 u=s.zeros(n,1)
 for j in range(1,d):v[j*d+j]=1;u[j*d+j]=1
 prep=v*v.T/q;r=s.diag(e*e,*([1]*a))/q;B=s.kronecker_product(s.eye(d)/d,r)
 sigma=(1-theta)*B+theta*prep;U=s.kronecker_product(s.diag(1,*([-1]*a)),s.eye(d));rho=U*sigma*U
 def marginal(m):return s.Matrix(d,d,lambda j,k:sum(m[i*d+j,i*d+k] for i in range(d)))
 assert zero(marginal(sigma)-r) and zero(marginal(rho)-r)
 out=lam*sigma+(1-lam)*B;outrho=lam*rho+(1-lam)*B
 pu=u*u.T/a;p0=s.zeros(n);p0[0,0]=1;Q=pu+p0
 W=Q*out*Q;tr=s.trace(W);p=lam*theta;det=e*e*(1-p)*(1+(d*d-1)*p)/(d*d*q*q);delta=s.sqrt(tr*tr-4*det);hi=(tr+delta)/2;lo=det/hi
 projector=(hi*Q-W)/delta
 assert projector==projector.T and zero(projector*projector-projector) and s.simplify(s.trace(projector)-1)==0
 probq=s.simplify(s.trace(projector*out));probp=s.simplify(s.trace(projector*outrho));b2=(lam*theta)**2*e*e*a/(q*q)
 assert s.simplify(probq-lo)==0 and s.simplify(probp-probq-4*b2/delta)==0
 # Exact Sylvester criterion for input positivity uses diagonal replacement plus a positive rank-one term.
 assert theta>0 and theta<1 and all(x>0 for x in B.diagonal())
 rows.append(dict(d=d,e=str(e),t=str(d*e*e),beta=2,theta=str(theta),lambda_parameter=str(lam),input_reference=[str(x) for x in r.diagonal()],projector_trace=str(s.simplify(s.trace(projector))),q0_exact=str(probq),p0_exact=str(probp),ambient_probability_identity=True,full_projector=[[str(s.simplify(projector[i,j])) for j in range(n)] for i in range(n)],input_sigma=[[str(sigma[i,j]) for j in range(n)] for i in range(n)]))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='own finite full-ambient symbolic controls for1070; no logarithmic asymptotic audit, physical experiment or formal proof assistant',method='SymPy exact radical projectors in full A_dR_d matrices, no scalar spectral-probability function reused',cases=rows,failures=[],not_in1068=True,score=None)
(P/'AMBIENT1073.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')

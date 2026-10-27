from pathlib import Path
import mpmath as m,json,traceback
P=Path(__file__).parent;m.mp.dps=210
def trace(A):return sum(A[i,i] for i in range(A.rows))
def spec(A):
 w,U=m.eighe(A);assert w[0]>0;return w,U
def logm(A):
 w,U=spec(A);return U*m.diag([m.log(x) for x in w])*U.H
def div(A,B):return m.re(trace(A*(logm(A)-logm(B))))
def blockdiag(bs):
 n=len(bs);r=bs[0].rows;X=m.zeros(n*r)
 for i,B in enumerate(bs):
  for j in range(r):
   for k in range(r):X[i*r+j,i*r+k]=B[j,k]
 return X
def kl(p,q):return p*m.log(p/q)+(1-p)*m.log((1-p)/(1-q))
rows=[]
try:
 for n,k in [(3,3),(3,8),(3,256),(4,4),(4,16)]:
  b=m.mpf(1)/(4*n*k);delta=m.mpf(2)**(-k);eps=b*delta;a=m.mpf(1)/n-(n-2)*eps-b;c=m.sqrt(a*b*(1-delta))
  U=m.eye(n);U[0,0]=U[1,1]=m.mpf(3)/5;U[0,1]=U[1,0]=4j/m.mpf(5)
  assert m.norm(U.H*U-m.eye(n))<m.mpf('1e-200')
  f=U*m.matrix([1/m.sqrt(n)]*n);F=f*f.H;PP=m.eye(n)-F;plus=[];minus=[]
  for i in range(n):
   e=m.zeros(n,1);e[i]=1;psi=U*(m.sqrt(m.mpf(n)/(n-1))*(e-m.matrix([m.mpf(1)/n]*n)))
   Pi=psi*psi.H;B=a*Pi+eps*(PP-Pi)+b*F;D=c*(psi*f.H+f*psi.H);plus.append(B+D);minus.append(B-D)
  rp=sum(plus,m.zeros(n));rm=sum(minus,m.zeros(n));assert m.norm(rp-rm)<m.mpf('1e-200')
  def output(bs):return [sum([bs[i] for i in range(n) if i!=j],m.zeros(n))/(n-1) for j in range(n)]
  rho,sig=blockdiag(plus),blockdiag(minus);ro,so=blockdiag(output(plus)),blockdiag(output(minus))
  assert abs(trace(rho)-1)<m.mpf('1e-200') and abs(trace(ro)-1)<m.mpf('1e-200')
  di,do=div(rho,sig),div(ro,so);w,V=spec(so)
  E=sum([V[:,j]*V[:,j].H for j in range(n)],m.zeros(n*n));assert m.norm(E*E-E)<m.mpf('1e-180')
  p,q=m.re(trace(E*ro)),m.re(trace(E*so));dm=kl(p,q)
  ap=(a+n*(n-2)*eps)/(n-1)**2;lam=-m.mpf(1)/(n-1)
  def plane(x,y,z):
   g=m.sqrt((x-y)**2+4*z);h=(x+y+g)/2;l=(x*y-z)/h;return h,l,g,(m.log(h)-m.log(l))/g
  hi,li,gi,ei=plane(a,b,c*c);ho,lo,go,eo=plane(ap,b,lam*lam*c*c)
  refs=[4*n*c*c*ei,4*n*lam*lam*c*c*eo,n*(lo+4*lam*lam*c*c/go),n*lo]
  errs=[abs(x-y) for x,y in zip([di,do,p,q],refs)];assert max(errs)<m.mpf('1e-115')
  flag=blockdiag([F]*n);pf,qf=m.re(trace(flag*ro)),m.re(trace(flag*so));assert abs(pf-qf)<m.mpf('1e-200')
  assert 0<dm<do<di
  rows.append(dict(n=n,k=k,dimension=n*n,complex_rotation=True,di=m.nstr(di,65),do=m.nstr(do,65),binary=m.nstr(dm,65),retention=m.nstr(dm/di,65),gap=m.nstr(dm/di-1/m.mpf(n-1),65),gap_sign='positive' if dm/di>1/m.mpf(n-1) else 'negative',p=m.nstr(p,65),q=m.nstr(q,65),formula_errors=[m.nstr(e,8) for e in errs],projector_rank=n,limit_flag_prob=m.nstr(pf,60),limit_flag_D='0 exact by commonmarginal',wrong_orientation_retention=m.nstr(kl(q,p)/di,60)))
 (P/'AMBIENT1115.json').write_text(json.dumps(dict(method='210decimal fullcomplexambient eigendecomposition/logs and nsmallestoutputeigenvectors; reducedformula used onlycomparison, notconstruction. Diagnostic,notintervalproof.',cases=rows,passed=True),indent=2)+'\n',encoding='utf-8');print(json.dumps({'cases':len(rows),'signs':[r['gap_sign'] for r in rows]}))
except Exception as e:
 (P/'AMBIENT_FAILURE1115.json').write_text(json.dumps(dict(error=repr(e),traceback=traceback.format_exc(),completed=rows),indent=2)+'\n');raise

"""Bounded falsifier screen, NOT universal proof, capsule or manuscript grade."""
import numpy as np,json,argparse
import mpmath as mp
from pathlib import Path
rng=np.random.default_rng(939)
def herm(n):
 out=[]
 for i in range(n):
  a=np.zeros((n,n),complex);a[i,i]=1;out.append(a)
 for i in range(n):
  for j in range(i+1,n):
   a=np.zeros((n,n),complex);a[i,j]=a[j,i]=1/np.sqrt(2);out.append(a)
   a=np.zeros((n,n),complex);a[i,j]=1j/np.sqrt(2);a[j,i]=-1j/np.sqrt(2);out.append(a)
 return out
def gram(s,bs):
 w,u=np.linalg.eigh(s);assert min(w)>0
 e=np.array([[1/a if abs(a-b)<1e-12*max(a,b) else (np.log(a)-np.log(b))/(a-b) for b in w] for a in w])
 z=np.stack([(u.conj().T@b@u).ravel() for b in bs],axis=1)
 return np.real(z.conj().T@(e.ravel()[:,None]*z))
def metricmax(s,r):
 paulis=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
 bs=[np.kron(p,b) for p in paulis for b in herm(r)]
 marginal=np.trace(s.reshape(2,r,2,r),axis1=0,axis2=2);ns=.5*s+.5*np.kron(np.eye(2)/2,marginal)
 a=gram(s,bs);b=.25*gram(ns,bs);w,u=np.linalg.eigh(a);ir=(u*(1/np.sqrt(w)))@u.T
 val,vec=np.linalg.eigh(ir@b@ir);z=ir@vec[:,-1];X=sum((t*q for t,q in zip(z,bs)),np.zeros_like(s));return float(val[-1]),X
rows=[];falsifier=None
for r in [2,3]:
 for i in range(30):
  z=rng.normal(size=(2*r,2*r))+1j*rng.normal(size=(2*r,2*r));q,_=np.linalg.qr(z)
  w=np.exp(rng.uniform(-8,1,size=2*r));w/=sum(w);s=(q*w)@q.conj().T
  value,X=metricmax(s,r);rows.append({'r':r,'case':i,'largest_same_marginal_BKM_ratio':value})
  if value>1/3+1e-7 and falsifier is None:
   falsifier={'r':r,'case':i,'ratio':value,'sigma_real':s.real.tolist(),'sigma_imag':s.imag.tolist(),'X_real':X.real.tolist(),'X_imag':X.imag.tolist()}
# Finite MI for the SEPARABLE one-coherence rational sequence, not a Hessian proxy.
mi=[]
for n in [3,5,10,20]:
 mp.mp.dps=int(2*n*n*mp.log10(2))+120;x=mp.mpf(1)/n;r=mp.mpf(2)**(-n*n);eps=r/(n*n)
 def info(a,b,e):
  plus=(a+b+mp.sqrt((a-b)**2+4*e*e))/2;minus=(a*b-e*e)/plus
  return plus*mp.log(plus)+minus*mp.log(minus)-a*mp.log(a)-b*mp.log(b)
 ain=(1-x)*(1-r);bin=x*r;u=(1+mp.mpf('.5'))/2-mp.mpf('.5')*x;v=1-u
 din=info(ain,bin,eps);dout=info(u*(1-r),v*r,mp.mpf('.5')*eps)
 ell=lambda a,b:(mp.log(a)-mp.log(b))/(a-b)
 lower=(mp.mpf(n-1)/(n+1))*mp.mpf('.25')*ell(u*(1-r),v*r)/ell(ain,bin)
 assert lower<dout/din<1
 mi.append({'n':n,'MI_ratio':str(dout/din),'Hessian_order_lower':str(lower),'MI_input':str(din)})
import sympy as sp
exact=sp.Rational(19,21)*sp.Rational(1,4)*sp.Rational(38,29)*sp.Rational(80,81)
assert exact==sp.Rational(14440,49329) and exact>sp.Rational(2881,10000)
out={'scope':'60 selected full-rank bases in equal-reference-marginal tangent subspaces, plus4 finite high-precision MI states; bounded diagnostics only','upper_bound_conjecture_tested':'eta_complete(D_lambda=.5)<=1/3, UNPROVED; discard if a valid recorded falsifier occurs','screen':rows,'first_falsifier':falsifier,'MI_separable_sequence':mi,'exact_n20_order_certificate':str(exact),'exact_certificate_proof_pending':'Uses log monotonicity bounds stated in PROOF939, not numerical interval certification','new_manuscript_score':None}
p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args();s=json.dumps(out,indent=2)+'\n'
if a.output:Path(a.output).write_text(s)
print(json.dumps({'max_screen':max(x['largest_same_marginal_BKM_ratio'] for x in rows),'falsifier':None if falsifier is None else {k:falsifier[k] for k in ['r','case','ratio']},'MI_n20':mi[-1]['MI_ratio'],'exact_n20_lower':str(exact)}))

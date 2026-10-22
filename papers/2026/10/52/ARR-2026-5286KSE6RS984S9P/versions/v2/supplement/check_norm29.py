from pathlib import Path
from datetime import datetime,timezone
import numpy as np,mpmath as mp,math,json,hashlib,time
root=Path(__file__).parent;out=root/'norm-checks-29.json'
if out.exists():raise SystemExit('Refusing overwrite')
mp.mp.dps=100
target=float(mp.sqrt(15)/mp.power(4,mp.mpf(4)/3))
def params(n):
 m,k=divmod(n-1,34)
 v=mp.findroot(lambda x:x**3-mp.mpf('1.5')*x*x-mp.mpf(n-1)/4,
               mp.root(mp.mpf(n-1)/4,3)+mp.mpf('.5'),tol=mp.mpf('1e-90'))
 d=(v*v/(v-1)-mp.mpf(k)/2)/m;t=(-v*v-mp.mpf(k)/4)/m
 L=(51+d)/2;U=17-t
 X=(U*L+221+mp.sqrt((U*L-289)*(U*L-169)))/(30*U)
 Y=(L-15*X)/2;a=1-X;c=1-Y
 error=max(abs(m*(-30*a-4*c-17)+mp.mpf(k)/2-v*v/(v-1)),
           abs(m*(-15*a/(1-a)-2*c/(1-c))+mp.mpf(k)/4+v*v))
 assert error<mp.mpf('1e-75') and -1<a<1 and -1<c<1 and v>mp.mpf('1.5')
 return m,k,float(v),float(a),float(c),mp.nstr(error,8)
def logabs1minus(x):
 out=np.empty_like(x);near=x<.5
 out[near]=np.log1p(-x[near])
 with np.errstate(divide='ignore'):
  out[~near]=np.log(np.abs(1-x[~near]))
 return out
def integrate(n,N,m,k,v,a,c):
 ds=[];ns=[];masked=0;peak=-float('inf')
 qa=.5+1j*math.sqrt(1-a*a)/(2*(1-a))
 qc=.5+1j*math.sqrt(1-c*c)/(2*(1-c))
 for start in range(0,N,131072):
  index=np.arange(start,min(start+131072,N),dtype=np.int64)
  # Symmetric angles avoid loss of accuracy near2pi.
  index=np.where(index<=N//2,index,index-N)
  theta=(2*math.pi/N)*index
  sh=np.sin(theta/2)**2
  logweight=30*m*logabs1minus(2*sh/(1-a))+4*m*logabs1minus(2*sh/(1-c))+np.log1p(4*v*(v-1)*sh)
  if k:
   with np.errstate(divide='ignore'):logweight+=k*np.log1p(-sh)
  peak=max(peak,float(np.max(logweight)))
  mask=logweight>-600;masked+=int(np.count_nonzero(~mask))
  if not np.any(mask):continue
  w=-2*sh[mask]+1j*np.sin(theta[mask])
  total=15*m*(qa**4/(1+qa*w)+qa.conjugate()**4/(1+qa.conjugate()*w))
  total+=2*m*(qc**4/(1+qc*w)+qc.conjugate()**4/(1+qc.conjugate()*w))
  if k:total+=k/16/(1+w/2)
  total+=v**4/(1+v*w)
  F=-w**3*total;weight=np.exp(logweight[mask])
  ds.append(float(np.sum(weight,dtype=np.float64)))
  ns.append(float(np.sum(weight*(F.real**2+F.imag**2),dtype=np.float64)))
 den=math.fsum(ds)/N;num=math.fsum(ns)/N
 return dict(N=N,denominator_squared=den,numerator_squared=num,
             rho=math.sqrt(num/den),masked_grid_points=masked,
             masking_log_weight_cutoff=-600,max_log_weight=peak)
rows=[];begin=time.monotonic()
for n in [10_000,10_017,100_000,100_017,1_000_000,1_000_017,10_000_000,10_000_017]:
 m,k,v,a,c,err=params(n)
 grids=[integrate(n,N,m,k,v,a,c) for N in [n+1,n+2]]
 rho=grids[0]['rho'];agreement=abs(rho-grids[1]['rho'])/rho
 assert agreement<2e-10
 row=dict(n=n,m=m,k=k,v=v,a=a,c=c,parameter_equation_error=err,grids=grids,
          relative_grid_discrepancy=agreement,scaled_rho=rho*n**(1/6),
          conjectured_asymptotic_constant=target,
          scaled_denominator=grids[0]['denominator_squared']*math.sqrt(n))
 rows.append(row)
 print(json.dumps({k:row[k] for k in ['n','k','scaled_rho','relative_grid_discrepancy']}),flush=True)
data=dict(status='PASS',created_at=datetime.now(timezone.utc).isoformat(),
 script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exact_grid_identity='N>n integrates squared norms exactly for exact coefficients and arithmetic.',
 numeric_precision='100-digit parameters, IEEE double grid evaluation, cancellation-free residual; no interval bounds.',
 caveat='Values with log normalized squared modulus<=-600 are masked to avoid pole-times-underflow artifacts. These are numerical diagnostics, not formally certified finite norms.',
 target_constant=target,expected_scaled_denominator=1/math.sqrt(2*math.pi),
 cases=rows,wall_seconds=time.monotonic()-begin)
out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='PASS',cases=len(rows),wall_seconds=data['wall_seconds'],target=target)),flush=True)

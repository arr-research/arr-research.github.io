from pathlib import Path
import numpy as np,json,traceback
P=Path(__file__).parent;rng=np.random.default_rng(110020261027)
def herm(x):return (x+x.conj().T)/2
def randpd(k):
 x=rng.normal(size=(k,k))+1j*rng.normal(size=(k,k));x=x@x.conj().T+.4*np.eye(k);return x/np.trace(x)
def marginal(x,n,r):return sum(x[i*r:(i+1)*r,i*r:(i+1)*r] for i in range(n))
def chan(x,n,r,lam):
 m=marginal(x,n,r);o=np.zeros_like(x)
 for i in range(n):o[i*r:(i+1)*r,i*r:(i+1)*r]=lam*x[i*r:(i+1)*r,i*r:(i+1)*r]+(1-lam)*m/n
 return o
def divs(a,b):
 va,ua=np.linalg.eigh(a);vb,ub=np.linalg.eigh(b);assert min(va)>0 and min(vb)>0
 weights=np.abs(ua.conj().T@ub)**2*vb[None,:];x=va[:,None]/vb[None,:]
 fs={'Umegaki':x*np.log(x)-x+1,'reverse_Umegaki':-np.log(x)+x-1,'triangular':(x-1)**2/(x+1),'quadratic':(x-1)**2,'inverse_quadratic':(x-1)**2/x,'Hellinger':(np.sqrt(x)-1)**2,'resolvent_007':(x-1)**2/(x+.07),'resolvent_13':(x-1)**2/(x+13)}
 return {k:float(np.sum(weights*f).real) for k,f in fs.items()}
rows=[]
try:
 for n,r in [(2,2),(3,2),(3,3),(4,3),(5,2)]:
  for trial in range(8):
   N=n*r;b=randpd(N);d=herm(rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)));mr=marginal(d,n,r)
   for i in range(n):d[i*r:(i+1)*r,i*r:(i+1)*r]-=mr/n
   d=herm(d);d*=.35*min(np.linalg.eigvalsh(b))/np.linalg.norm(d,2);a=b+d
   assert np.linalg.norm(marginal(a-b,n,r))<1e-13
   di=divs(a,b)
   for lam in [-1/(n-1),-.2/(n-1),0,.13,.63,.999,1]:
    ao,bo=chan(a,n,r,lam),chan(b,n,r,lam);do=divs(ao,bo);H=(n-1)*lam*lam/(1+(n-2)*lam)
    ratios={k:do[k]/di[k] for k in di};excess=max(v-H for v in ratios.values())
    assert excess<2e-8
    rows.append(dict(n=n,R=r,trial=trial,noise=lam,H=H,ratios=ratios,max_excess=excess,input_coherent=True,equal_reference_error=float(np.linalg.norm(marginal(a-b,n,r)))))
 out=dict(seed=110020261027,scope='Float64 bounded falsification only:40 complex coherent equal-reference pairs,7 noise values,8 Petz functions;280 pair/noise points and2240 ratios. No proof or exhaustive search.',cases=rows,max_excess=max(x['max_excess'] for x in rows),passed=True)
 (P/'RANDOM1100.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'points':len(rows),'ratios':8*len(rows),'maximum_excess':out['max_excess']}))
except Exception as e:
 (P/'RANDOM_FAILURE1100.json').write_text(json.dumps(dict(error=repr(e),traceback=traceback.format_exc(),completed=rows),indent=2)+'\n',encoding='utf-8');raise

from pathlib import Path
from datetime import datetime,timezone
import json
import mpmath as mp
mp.mp.dps=100
def h(x):return mp.mpf(0) if x in (0,1) else -x*mp.log(x,2)-(1-x)*mp.log(1-x,2)
def g(x):return mp.mpf(0) if x==0 else ((x+1)*mp.log1p(x)-x*mp.log(x))/mp.log(2)
def upward(x):return f'{int(mp.ceil(x*10**6))/10**6:.6f}'
rows=[];lam=mp.mpf('0.7');M=mp.mpf(10)
for n in [100,1000,10000,100000,1000000,100000000]:
    N=mp.mpf(n);K=int(mp.ceil(mp.sqrt(N)));m=N-K;r=m/(m+1)
    d=int(mp.ceil(2*(m+1)*mp.log(N+1)));t=r**d
    s=g(m)+mp.log(1-t,2)+d*t/(1-t)*mp.log(r,2);a=g(N)-s
    eps=min(mp.mpf(1),M/K);delta=(1-lam)*eps;P=lam+delta;b=P*h(delta/P)
    bounds=[lam*a+b,(2*lam-1)*a+b,2*lam*a+b,lam*a+b+delta*mp.log(5,2)]
    rows.append({'N':n,'K':K,'d':d,'entropy_loss':mp.nstr(a,95),'exact_bounds':[mp.nstr(x,95) for x in bounds],'upward_6':[upward(x) for x in bounds]})
out={'created_at':datetime.now(timezone.utc).isoformat(),'precision_decimal':100,'analytic_table':rows,'scope':'Analytic upper gap bounds, not computed capacities. Replaces the two-way column in manuscript-2; the first three columns are unchanged.'}
Path(__file__).with_name('table-verification-3.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps([{'N':r['N'],'upward_6':r['upward_6']} for r in rows]))

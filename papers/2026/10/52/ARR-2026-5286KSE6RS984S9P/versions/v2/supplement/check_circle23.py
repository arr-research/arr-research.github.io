from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,math
from scipy.special import mathieu_a
from scipy.optimize import minimize_scalar
R=Path(__file__).parent;target=R/'circle-checks-23.json'
if target.exists():raise SystemExit('Refusing overwrite')
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
rows=[]
for m,k in [(3,0),(3,5),(10,0),(10,5),(30,0),(30,5),(100,0),(100,5),(250,0)]:
    n=6*m+k
    co=[math.comb(4*m+k,j) for j in range(4*m+k+1)]
    for j in range(m):co=mul(co,[4*m,-(4*m+2*k-1),4*m])
    assert len(co)==n+1 and co[0]==(4*m)**m
    lam=Q(2*n+1,4)
    assert Q(co[1],co[0])==lam
    assert Q(1,2)+Q(2*k-1,8*m) in [Q(1,2)+Q(2*k-1,8*m)]
    assert -1<Q(1,2)+Q(2*k-1,8*m)<1
    r=[4*(j+1)*co[j+1]-(2*n+1)*co[j] for j in range(n)]+[-(2*n+1)*co[n]]
    sq=Q(sum(x*x for x in r),16*sum(x*x for x in co))
    rows.append({'m':m,'k':k,'degree':n,'rho_squared':str(sq),'rho_decimal_diagnostic':math.sqrt(float(sq)),
                 'scope':'Exact complete coefficient Parseval ratio; displayed square root is floating-point.'})
spectral=[]
for n in [10,20,50,100,200,500]:
    def f(c):
        lam=n/2+c
        return n*n/4+lam*lam+float(mathieu_a(0,2*(n+1)*lam))/4
    fit=minimize_scalar(f,bounds=(-2,2),method='bounded',options={'xatol':1e-8})
    spectral.append({'n':n,'local_window_c':float(fit.x),'ground_lower_diagnostic':float(fit.fun),
                     'scope':'Floating local-window diagnostic using scipy, not a global certificate or proof.'})
out={'created_at':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'exact_Parseval':rows,'Mathieu_diagnostics':spectral,'claimed_limit_squared':'1/8','proof_status':'unaudited'}
target.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'Parseval':[{k:v for k,v in a.items() if k not in ['rho_squared','scope']} for a in rows], 'Mathieu':spectral},indent=2))

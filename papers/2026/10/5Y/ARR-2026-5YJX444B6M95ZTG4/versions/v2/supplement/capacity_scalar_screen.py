"""Reproducible scalar illustrations. Floating-point numerics, not interval certificates."""
from pathlib import Path
import numpy as np,json,math
R=Path(__file__).resolve().parent
def h(x):
    x=np.asarray(x);q=np.clip(x,1e-300,1-1e-16)
    return np.where((x<=0)|(x>=1),0.,-q*np.log(q)-(1-q)*np.log1p(-q))
def curve(a,b,l2,p):
    k=1-a-b;t=a+k*p;v=t*(1-t)-l2*p*(1-p)
    return h((1+np.sqrt(np.maximum(0,1-4*v)))/2)
def solve(a,b,l2,n=20000,summary=True):
    k=1-a-b;p=np.linspace(0,1,n+1);e=curve(a,b,l2,p)
    hull=[]
    for i in range(n+1):
        while len(hull)>1:
            u,v=hull[-2:]
            if (e[v]-e[u])*(i-v)>=(e[i]-e[v])*(v-u):hull.pop()
            else:break
        hull.append(i)
    best=(-1,None)
    for i,j in zip(hull[:-1],hull[1:]):
        slope=(e[j]-e[i])/(p[j]-p[i]);t0=1/(1+math.exp(min(700,max(-700,float(slope/k)))))
        ps=float(np.clip((t0-a)/k,p[i],p[j]));frac=(ps-p[i])/(p[j]-p[i])
        val=float((h(a+k*ps)-(1-frac)*e[i]-frac*e[j])/np.log(2))
        if val>best[0]:best=(val,(ps,int(i),int(j),float(frac)))
    A=a*(1-a);B=k*(1-2*a)-l2;C=l2-k*k
    candidates=[A,A+B+C]
    if C>0 and 0 < -B/(2*C) < 1:candidates.append(A-B*B/(4*C))
    vmin=min(candidates);r=math.sqrt(max(0,1-4*vmin))
    gprime=2 if r<1e-12 else math.log((1+r)/(1-r))/r
    L=max(abs(B),abs(B+2*C))*gprime
    ps,i,j,frac=best[1]
    return dict(a=a,b=b,lambda_squared=l2,k=k,grid_intervals=n,capacity_grid_lower_approx=best[0],p_approx=ps,support_populations=[i/n,j/n],support_weights=[1-frac,frac],hull_nodes=len(hull),v_min=vmin,theoretical_exact_arithmetic_discretization_bound_bits=L/(2*n*np.log(2)),machine_roundoff_not_certified=True)
if __name__=='__main__':
    found=None
    for a,b in ((.02,.3),(.1,.3),(.15,.6),(.01,.6)):
        k=1-a-b
        for l2 in np.linspace(k*k,k,101)[1:-1]:
            r=solve(a,b,float(l2),4000)
            x,y=r['support_populations'];w=r['support_weights']
            if y-x>.02 and min(w)>.02 and (0<x<1 or 0<y<1):found=r;break
        if found:break
    params=[(.1,.3,.5),(.1,.3,.1),(.1,.3,.6)]
    if found:params.append((found['a'],found['b'],found['lambda_squared']))
    records=[solve(*args,200000) for args in params]
    (R/'capacity-scalar-results.json').write_text(json.dumps(dict(status='floating-point illustrations; no machine interval certification',examples=records),indent=2)+'\n')
    print(json.dumps(records),flush=True)

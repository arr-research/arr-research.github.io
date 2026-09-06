import numpy as np
from scipy.optimize import differential_evolution, minimize
from numpy.polynomial import polynomial as P
import json

def peak(v,y,k, detail=False):
    den=np.array([v*v+y*y*k*k,2*y*y*k,y*y-2*v,0.,1.])
    num=y*np.array([v,2*k,v+1,2*k,1.])
    der=P.polysub(P.polymul(P.polyder(num),den),P.polymul(num,P.polyder(den)))
    r=P.polyroots(np.trim_zeros(der,'b'))
    rs=[float(z.real) for z in r if abs(z.imag)<1e-6]
    vals=[(y,None)]+[(float(P.polyval(s,num)/P.polyval(s,den)),s) for s in rs]
    return sorted(vals,reverse=True,key=lambda x:x[0]) if detail else max(x[0] for x in vals)

def decode(x,u,symmetric=False):
    v=u*u+np.exp(x[0])
    k=0. if symmetric else np.sqrt((u*u+v)/2)*np.tanh(x[2])
    lower=2*(v*v-u**4)/(u*u+v-2*k*k)
    y=np.sqrt(lower+np.exp(x[1]))
    return v,y,k

if __name__=='__main__':
    out=[]
    for u in [1.01,1.1,1.5,2,3,5,10]:
      for symmetric in [True,False]:
        def obj(x):
            v,y,k=decode(x,u,symmetric)
            if k*k>=v:return 1e4+k*k-v
            return peak(v,y,k)
        bounds=[(-18,np.log(u*u*10)),(-18,np.log(u*u*20))]+([] if symmetric else [(-2,2)])
        res=differential_evolution(obj,bounds,popsize=12,maxiter=250,tol=1e-9,seed=31,polish=True)
        v,y,k=decode(res.x,u,symmetric)
        row=dict(u=u,symmetric=symmetric,T=res.fun,v=v,y=y,k=k,peaks=peak(v,y,k,True)[:4])
        out.append(row);print(json.dumps(row),flush=True)
    open(__file__.replace('explore_two_state.py','exploration.json'),'w').write(json.dumps(out,indent=2))

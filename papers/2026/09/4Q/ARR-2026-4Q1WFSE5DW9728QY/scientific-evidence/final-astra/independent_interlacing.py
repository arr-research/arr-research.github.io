from fractions import Fraction as F
from math import prod
from datetime import datetime,timezone
import numpy as np
print('UTC',datetime.now(timezone.utc).isoformat())
count=0;worst=0
for n in range(2,6):
 for m in range(n,n+6):
  a=[F((m-j)**2) for j in range(m)];a=[x/sum(a) for x in a]
  for k in range(1,m-n+2):
   tau=[sum(a[k+i::n]) for i in range(n)]
   for weight in [F(1,2),F(1)]:
    bsmall=[(1-weight)*tau[i]+weight*tau[i-1] for i in range(1,n)];b=[sum(a)-sum(bsmall)]+bsmall
    assert min(b)>0 and all(x>=y for x,y in zip(b,b[1:]))
    dvec=[-a[k-1]]+b[1:];s=sum(a[k-1:])-sum(b[1:]);assert s>0
    v2=[prod(x-dv for x in tau)/(s*prod(ot-dv for j,ot in enumerate(dvec) if j!=i)) for i,dv in enumerate(dvec)]
    assert min(v2)>=0 and sum(v2)==1
    # exact characteristic polynomial through N+1 distinct evaluation nodes off the diagonal poles
    for ell in range(n+1):
     x=F(-10-ell);lhs=prod(dv-x for dv in dvec)*(1+s*sum(vv/(dv-x) for vv,dv in zip(v2,dvec)));rhs=prod(t-x for t in tau);assert lhs==rhs
    # Construct rectangular shifts directly in layer coordinates.
    layers=[[-b[0]]]+[[x] for x in a[:k-1]]+[[a[k-1]]+[-x for x in b[1:]]]+[a[j:j+n] for j in range(k,m,n)]
    offsets=np.cumsum([0]+list(map(len,layers)));C=np.zeros((m+n,m+n));idx=lambda t:range(offsets[t],offsets[t+1])
    for t in range(1,k):C[offsets[t],offsets[t-1]]=np.sqrt(2*float(sum(a[t-1:])-sum(b[1:])))
    v=np.sqrt(np.array(list(map(float,v2))));C[np.ix_(list(idx(k)),list(idx(k-1)))]=np.sqrt(2*float(s))*v[:,None]
    mix=float(s)*np.outer(v,v)+np.diag(list(map(float,dvec)));ev,U=np.linalg.eigh(mix);order=np.argsort(ev)[::-1];ev=ev[order];U=U[:,order]
    r=len(layers[k+1]);M=np.diag(np.sqrt(np.maximum(0,2*ev[:r])))@U[:,:r].T;C[np.ix_(list(idx(k+1)),list(idx(k)))]=M
    for t in range(k+2,len(layers)):
     r=len(layers[t]);start=k+(t-k-1)*n
     for i in range(r):C[offsets[t]+i,offsets[t-1]+i]=np.sqrt(2*float(sum(a[start+i::n])))
    l=np.array([float(x) for L in layers for x in L]);err=np.max(abs(C@C.T-C.T@C-2*np.diag(l)));cost=sum(F(t)*sum(L) for t,L in enumerate(layers));err=max(err,abs(np.sum(C*C)/2-float(cost)))
    assert err<1e-11 and np.linalg.matrix_rank(C,tol=1e-9)==m;(count:=count+1);worst=max(worst,err)
print('PASS independent interlacing exact secular identities and whole matrix construction',count,'interior/upper-boundary cases n2..5 m=n..n+5; worst numerical residual',worst)
# Degenerate rank-one cases (the distinct-diagonal formula is not used).
for dv,v,s in [([2,2,1],[1,0,0],3),([1,1,1],[0,1,0],2),([3,2,2],[0,1,0],0)]:
 ev=np.linalg.eigvalsh(np.diag(dv)+s*np.outer(v,v))[::-1];assert all(ev[i]>=dv[i] for i in range(3)) and all(dv[i]>=ev[i+1] for i in range(2))
print('PASS three tied-diagonal or zero-update boundary controls')

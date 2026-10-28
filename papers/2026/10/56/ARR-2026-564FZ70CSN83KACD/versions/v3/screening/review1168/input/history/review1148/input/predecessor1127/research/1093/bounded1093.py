from pathlib import Path
from fractions import Fraction as Q
import numpy as np,json
P=Path(__file__).parent;rng=np.random.default_rng(1093)
def herm(n):
 g=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));return g@g.conj().T+np.eye(n)/5
def root(a):
 w,v=np.linalg.eigh(a);assert min(w)>0;return (v*np.sqrt(w))@v.conj().T
def vec(a):return a.reshape(-1,order='F')
def left(a):return np.kron(np.eye(len(a)),a)
def right(a):return np.kron(a.T,np.eye(len(a)))
def Fval(x,aa,bb):return x*(1-x)*sum((a-b)**2/(b+(a-b)*x) for a,b in zip(aa,bb))
def der(x,aa,bb):return sum((a-b)**2*((1-2*x)/(b+(a-b)*x)-x*(1-x)*(a-b)/(b+(a-b)*x)**2) for a,b in zip(aa,bb))
def bound(aa,bb):
 lo=Q(0);hi=Q(1)
 for _ in range(100):
  mid=(lo+hi)/2
  if der(mid,aa,bb)>0:lo=mid
  else:hi=mid
 mid=(lo+hi)/2;v=Fval(mid,aa,bb);upper=v+abs(der(mid,aa,bb))*(hi-lo)/2
 return float(upper),{'x_bracket':[str(lo),str(hi)],'c_bracket':[str(v),str(upper)]}
def petz(p,q,f):
 wp,up=np.linalg.eigh(p);wq,uq=np.linalg.eigh(q);assert min(wp)>0 and min(wq)>0
 overlap=np.abs(up.conj().T@uq)**2
 return float(np.sum(wq[None,:]*f(wp[:,None]/wq[None,:])*overlap))
funcs={'Umegaki':lambda x:x*np.log(x)-x+1,'reverse_Umegaki':lambda x:-np.log(x)+x-1,'Hellinger':lambda x:(np.sqrt(x)-1)**2,'power_1.5':lambda x:x**1.5-1-1.5*(x-1),'quadratic':lambda x:(x-1)**2}
rows=[];violations=[];orientation=[]
for n in (2,3,4):
 for m in (2,3,5):
  for repeat in range(3):
   ai=list(map(int,rng.integers(1,20,size=m)));bi=list(map(int,rng.integers(1,20,size=m)));aa=[Q(v,sum(ai)) for v in ai];bb=[Q(v,sum(bi)) for v in bi];c,certificate=bound(aa,bb)
   r=herm(n);r/=np.trace(r).real;rh=root(r)
   def effect():
    g=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));u,_=np.linalg.qr(g);return (u*rng.uniform(.025,.975,size=n))@u.conj().T
   p0=rh@effect()@rh;s0=rh@effect()@rh;pp=[p0,r-p0];ss=[s0,r-s0];z=p0-s0;v=vec(z)
   outp=[float(a)*pp[0]+float(b)*pp[1] for a,b in zip(aa,bb)];outs=[float(a)*ss[0]+float(b)*ss[1] for a,b in zip(aa,bb)]
   checks=[]
   for kind,u in [('resolvent',0),('resolvent',.001),('resolvent',.3),('resolvent',1),('resolvent',1000),('quadratic',None),('SLD',None)]:
    if kind=='quadratic':A,B=map(right,ss)
    elif kind=='SLD':A,B=[(left(t)+right(t))/2 for t in ss]
    else:A,B=[left(p)+u*right(s) for p,s in zip(pp,ss)]
    inp=np.linalg.inv(A)+np.linalg.inv(B);out=sum(float(a-b)**2*np.linalg.inv(float(a)*A+float(b)*B) for a,b in zip(aa,bb));gap=(c*inp-out);gap=(gap+gap.conj().T)/2
    mineig=float(np.linalg.eigvalsh(gap)[0]);ratio=float((np.vdot(v,out@v)/np.vdot(v,inp@v)).real)
    # Arbitrary complex HS direction, not restricted to vectorized Hermitian matrices.
    w=rng.normal(size=n*n)+1j*rng.normal(size=n*n);ws=float(np.vdot(w,gap@w).real)
    if mineig< -1e-9 or ratio>c+1e-10 or ws< -1e-8:violations.append([n,m,repeat,kind,u,mineig,ratio,c])
    item={'kind':kind,'u':u,'full_complex_HS_gap_min_eigenvalue':mineig,'arbitrary_complex_direction_gap':ws,'state_ratio':ratio}
    if kind=='resolvent':
     f=lambda x:(x-1)**2/(x+u)
     directin=sum(petz(p,s,f) for p,s in zip(pp,ss));directout=sum(petz(p,s,f) for p,s in zip(outp,outs));item['direct_spectral_identity_error']=max(abs(directin-np.vdot(v,inp@v).real),abs(directout-np.vdot(v,out@v).real))
     assert item['direct_spectral_identity_error']<1e-9
    checks.append(item)
   fr={name:sum(petz(p,s,f) for p,s in zip(outp,outs))/sum(petz(p,s,f) for p,s in zip(pp,ss)) for name,f in funcs.items()};assert all(0<=v<=c+1e-10 for v in fr.values())
   # Correct right multiplication uses transpose, not adjoint or no transpose.
   zz=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));orientation.append(float(np.linalg.norm(right(s0)@vec(zz)-vec(zz@s0))));assert orientation[-1]<1e-12
   rows.append({'n_reference':n,'n_output':m,'repeat':repeat,'a':list(map(str,aa)),'b':list(map(str,bb)),'coefficient_bound':certificate,'c_float':c,'checks':checks,'direct_finite_Petz_ratios':fr})
assert not violations
# Full quantum inputs for binary POVM, common quantum reference; factorization and DPI.
povm=[]
for d in (3,5):
 nr=2;N=d*nr;r=herm(nr);r/=np.trace(r).real;base=np.kron(np.eye(d)/d,r);emin=np.linalg.eigvalsh(base)[0]
 def state():
  g=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N));h=(g+g.conj().T)/2;h4=h.reshape(d,nr,d,nr);tr=sum(h4[j,:,j,:] for j in range(d));h-=np.kron(np.eye(d)/d,tr);return base+h*.7*emin/np.linalg.norm(h,2)
 rho=state();sigma=state();g=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));u,_=np.linalg.qr(g);eigs=np.linspace(.2,.9,d);F=(u*eigs)@u.conj().T;E=(F-.2*np.eye(d))/.7
 def block(e,t):return np.einsum('ji,iajb->ab',e,t.reshape(d,nr,d,nr))
 rp=[block(F,rho),block(np.eye(d)-F,rho)];sp=[block(F,sigma),block(np.eye(d)-F,sigma)];er=block(E,rho)
 err=float(np.linalg.norm(rp[0]-(.9*er+.2*(r-er))));assert err<1e-12
 ratios={name:sum(petz(p,s,f) for p,s in zip(rp,sp))/petz(rho,sigma,f) for name,f in funcs.items()};assert all(v<=.5+1e-10 for v in ratios.values())
 povm.append({'input_dimension':d,'reference_dimension':nr,'factorization_error':err,'finite_complex_coherent_ratios':ratios})
(P/'BOUNDED1093.json').write_text(json.dumps({'seed':1093,'precision':'IEEE float64 diagnostic only; no universal proof or exact PSD certificate','states':rows,'operator_checks':sum(len(r['checks']) for r in rows),'violations':violations,'right_multiplication_max_error':max(orientation),'POVM_coherent_cases':povm},indent=2)+'\n',encoding='utf-8');print('Bounded checks:',len(rows),'states;',sum(len(r['checks']) for r in rows),'full-HS gaps;2coherentPOVM; violations',len(violations))

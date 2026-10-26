"""Audit590: independent tensor-dilation, truncation and endpoint checks.
Finite floating-point diagnostics do not prove the infinite limits or code theorem.
"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import mpmath as mp
from scipy.stats import binom

ROOT=Path(__file__).resolve().parent
RNG=np.random.default_rng(590261026)
def H(p):
 p=np.asarray(p,float);assert p.min(initial=0)>-2e-10
 p=p[p>1e-15];return float(-np.dot(p,np.log2(p)))
def S(a):return H(np.linalg.eigvalsh((a+a.conj().T)/2))
def h(p):return H([p,1-p])
def b(u,v):
 e=lambda x:x*math.log2(x) if x>0 else 0.
 return e(u+v)-e(u)-e(v)
def g(x):return (math.log1p(x)+x*math.log1p(1/x))/math.log(2) if x>0 else 0.
def tail_entropy(c,n,E):
 if c==0:return 0.
 beta=math.log1p(1/E);mass=c*math.exp(-n*beta)
 return mass*(math.log2((E+1)/c)+(n+E)*beta/math.log(2))
def dilation(d,k):
 # V[b,l,n] with b+l=n. Constructed directly from number conservation.
 V=np.zeros((d,d,d))
 for n in range(d):
  for lost in range(n+1):
   V[n-lost,lost,n]=math.sqrt(math.comb(n,lost)*k**(n-lost)*(1-k)**lost)
 assert np.max(np.abs(V.reshape(d*d,d).T@V.reshape(d*d,d)-np.eye(d)))<1e-12
 return V
def channel(rho,V):
 be=np.einsum('bln,nm,ckm->blck',V,rho,V.conj(),optimize=True)
 return np.trace(be,axis1=1,axis2=3),np.trace(be,axis1=0,axis2=2)

signals=[];branches=[];detectors=[];entropy_dpi=[]
for E in [2.,6.,20.]:
 for d in [4,7]:
  for k in [.02,.3,.5,.500000001,.9,1-1e-10,1.]:
   for family in ['pure','mixed']:
    z=RNG.normal(size=(d,d))+1j*RNG.normal(size=(d,d))
    rho=z[:,:1]@z[:,:1].conj().T if family=='pure' else z@z.conj().T
    rho/=np.trace(rho);mu=float(np.dot(np.arange(d),rho.diagonal()).real)
    if mu>E:
     f=E/mu;rho*=f;rho[0,0]+=1-f
    mu=float(np.dot(np.arange(d),rho.diagonal()).real)
    vals,U=np.linalg.eigh(rho);root=(U*np.sqrt(np.maximum(vals,0)))@U.conj().T
    psi=root.T;V=dilation(d,k);out,env=channel(rho,V)
    amp=np.einsum('rn,bln->rbl',psi,V,optimize=True)
    rbamp=amp.reshape(d*d,d);omega=rbamp@rbamp.conj().T
    comp,_=channel(rho,dilation(d,1-k))
    assert np.max(np.abs(comp-env))<1e-11
    assert abs(S(omega)-S(env))<5e-10
    assert abs(float(np.dot(np.arange(d),out.diagonal()).real)-k*mu)<1e-10
    assert abs(float(np.dot(np.arange(d),env.diagonal()).real)-(1-k)*mu)<1e-10
    sr,sb,se=map(S,[rho,out,env]);C=g(E)+g(k*E)-g((1-k)*E)
    Kbound=max(0,g(k*E)-g((1-k)*E))
    margins={'reverse_information':g(E)-g((1-k)*E)-sr+se,
             'coherent_information':Kbound-sb+se,'EA_benchmark':C-sr-sb+se}
    assert min(margins.values())>-1e-9
    signals.append(dict(E=E,d=d,kappa=k,family=family,**margins))
    for t in [0.,.03,.4,1.]:
     thin,_=channel(rho,dilation(d,t));difference=sr-S(thin)
     envelope=g(E)-g(t*E)
     if t>0:
      coefficient=math.log1p(1/E)-t*math.log1p(1/(t*E))
      exact=(math.log((E+1)/(t*E+1))+mu*coefficient)/math.log(2)
      assert -1e-12<=coefficient
      assert difference<=exact+1e-9 and exact<=envelope+1e-9
     assert difference<=envelope+1e-9
     entropy_dpi.append(dict(E=E,t=t,margin=envelope-difference))
    r=float(vals.max());vac=float(out[0,0].real)
    assert vac<=r/k+1e-10
    p0=1/(1+k*E)
    geo=np.exp(-np.arange(d)*math.log1p(1/(k*E)))*p0
    cuts=sorted(set([0,1,d//2,math.ceil(math.sqrt(math.log1p(E))*(1-k)*E)]))
    Qs=[]
    for cut in cuts:
     columns=amp[:,:,:min(cut+1,d)].copy();columns[:,0,:]=0
     matrix=columns.reshape(d*d,-1)
     u,s,_=np.linalg.svd(matrix,full_matrices=False);rank=int(np.count_nonzero(s>1e-12))
     Q=u[:,:rank]@u[:,:rank].conj().T
     accept=float(np.trace(Q@omega).real)
     discarded=float(np.sum(np.abs(amp[:,:,min(cut+1,d):])**2))
     assert accept>=1-vac-discarded-1e-9
     assert discarded<=(1-k)*mu/(cut+1)+1e-9
     assert rank<=cut+1
     Qs.append((cut,rank,Q,accept,discarded))
    for lam in [.13,.5,.87]:
     q=1-lam
     for a in [0.,.35,1.]:
      tau=a*geo;tau[0]+=1-a
      reset=np.kron(rho.T,np.diag(tau))
      mixed=lam*out+q*np.diag(tau);joint=lam*omega+q*reset
      sbmix=S(mixed)+tail_entropy(q*a,d,k*E)
      srb=S(joint)+q*a*math.exp(-d*math.log1p(1/(k*E)))*sr+tail_entropy(q*a,d,k*E)
      stau=H([1-a+a*p0])+tail_entropy(a,1,k*E)
      I=sr+sbmix-srb;F=lam*(sr-se)+sbmix-q*stau-h(lam)
      upperF=lam*C-b(lam,q*a)+q*h(a*p0)
      assert F<=upperF+1e-9
      assert I<=lam*(sr+Kbound)+1e-9
      assert -1e-9<=I-F<=h(lam)+1e-9
      branches.append(dict(E=E,d=d,kappa=k,lam=lam,a=a,
                           F_margin=upperF-F,flagged_margin=lam*(sr+Kbound)-I))
      for cut,rank,Q,accept,discarded in Qs:
       false=float(np.trace(Q@reset).real)
       assert false<=a*rank*r*p0+1e-9
       error=lam*(1-accept)+q*false
       assert I-F<=h(min(1,max(0,error)))+1e-9
       detectors.append(dict(kappa=k,a=a,cut=cut,rank=rank,
                             reset_margin=a*rank*r*p0-false,
                             capture_margin=accept-(1-vac-discarded),
                             Fano_margin=h(min(1,max(0,error)))-(I-F)))

truncation=[]
for E in [2.,7.,25.]:
 M=E-1;L=math.ceil(4*E*math.log1p(E));logr=math.log1p(-1/E)
 eps=math.exp(L*logr);p=np.exp(np.arange(L)*logr)/(E*(1-eps))
 delta=h(eps)+eps*(g(M+L)+g(M))
 for k in [.02,.3,.8,1-1e-10,1.]:
  def thin(p,t):
   result=np.zeros(len(p))
   for n,pn in enumerate(p):result[:n+1]+=pn*binom.pmf(np.arange(n+1),n,t)
   return result
  out=thin(p,k);comp=thin(p,1-k)
  assert max(abs(H(p)-g(M)),abs(H(out)-g(k*M)),abs(H(comp)-g((1-k)*M)))<=delta+5e-10
  assert out.max()<=1/((1+k*M)*(1-eps))+1e-12
  I=H(p)+H(out)-H(comp);C=g(E)+g(k*E)-g((1-k)*E)
  bound=3*delta+2*math.log1p(1/M)/math.log(2)
  assert -1e-10<=C-I<=bound+5e-10
  truncation.append(dict(E=E,L=L,kappa=k,epsilon=eps,gap=C-I,uniform_bound=bound))

mp.mp.dps=260;ln2=mp.log(2)
def mg(x):return (mp.log1p(x)+x*mp.log1p(1/x))/ln2 if x else mp.mpf(0)
def mh(x):return -(x*mp.log(x)+(1-x)*mp.log1p(-x))/ln2 if 0<x<1 else mp.mpf(0)
def mb(u,v):
 e=lambda x:x*mp.log(x)/ln2 if x else mp.mpf(0)
 return e(u+v)-e(u)-e(v)
scalar=[];old_nonuniform=[];z_table=[];tol=mp.mpf('1e-150')
k0=mp.mpf('.02');constant=max(-mp.log(k0,2),1/ln2)
for es in ['2','10','1e6','1e30','1e100']:
 E=mp.mpf(es);A=mp.log1p(E)/ln2;Gmin=mg(k0*E)
 clip_error=min(1,1/Gmin+constant/A)
 kappas=[k0,mp.mpf('.1'),mp.mpf('.5'),mp.mpf('.9'),1-1/E,1-1/E**2,mp.mpf(1)]
 for k in kappas:
  G=mg(k*E);C=mg(E)+G-mg((1-k)*E);K=max(0,G-mg((1-k)*E))
  assert mg(E)-C+K<=-mp.log(k0,2)+tol
  assert abs(G-A)<=constant+tol
  assert 0<=C-(mg(E-1)+mg(k*(E-1))-mg((1-k)*(E-1)))+tol
  assert C-(mg(E-1)+mg(k*(E-1))-mg((1-k)*(E-1)))<=2*mp.log1p(1/(E-1))/ln2+tol
  for B in [mp.mpf(0),mp.mpf('.1'),1,A/2,A,G,G+1,100*max(G,A)]:
   t=min(1,B/A);a=min(1,max(0,(B-1)/G))
   assert abs(t-a)<=clip_error+tol
   assert a==0 or mh(a)+a*G<=B+tol
   scalar.append(dict(E=es,kappa=str(k),B=str(B),clip_difference=str(a-t),bound=str(clip_error)))
 for ls in ['.1','.5','.9']:
  lam=mp.mpf(ls);q=1-lam;D0=-mp.log(k0,2)+mh(lam)/lam
  rb=min(1,(D0+1)/A);t=mp.sqrt(mp.log1p(E))
  z=lam*(1/t+rb/k0)+q*rb*(t/k0+2/(1+k0*E))
  for k in kappas:
   cut=mp.ceil(t*(1-k)*E)
   tighter=lam*(1/t+rb/k)+q*(cut+1)*rb/(1+k*E)
   assert tighter<=z+tol
 for power in [1,2]:
  k=1-1/E**power
  loose=-mp.log(1-k,2)-mg(E)+mg((1-k)*E)
  old_nonuniform.append(dict(E=es,path_power=power,old_bracket=str(loose)))
for exponent in [100,10000,1000000,100000000]:
 E=mp.power(2,exponent);lam=mp.mpf('.5');q=1-lam
 rb=(1-mp.log(k0,2)+mh(lam)/lam)/exponent;t=mp.sqrt(mp.log1p(E))
 z=lam*(1/t+rb/k0)+q*rb*(t/k0+2/(1+k0*E))
 z_table.append(dict(log2_E=exponent,kappa0=str(k0),lambda_=str(lam),z=str(z)))

result={'status':'PASS','scope':'Independent finite and high-precision tests, not capacity optimization or proof',
 'seed':590261026,'precision_digits':mp.mp.dps,
 'counts':{'signal_cases':len(signals),'entropy_DPI_cases':len(entropy_dpi),'branch_cases':len(branches),
           'detector_cases':len(detectors),'thermal_truncations':len(truncation),'uniform_clipping_cases':len(scalar)},
 'signals':signals,'entropy_DPI':entropy_dpi,'branches':branches,'detectors':detectors,
 'truncation':truncation,'scalar':scalar,'superseded_bound_nonuniformity':old_nonuniform,'z_table':z_table,
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'independent_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k in ['status','scope','seed','precision_digits','counts','code_sha256']},indent=2))

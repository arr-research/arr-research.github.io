"""Noncommuting finite controls of the614 pinching bookkeeping, not its theorem."""
import numpy as np
import json
from pathlib import Path
rng=np.random.default_rng(61420261026)
ln2=np.log(2.0)
def entropy(a):
 s=np.linalg.eigvalsh(a);s=s[s>1e-14]
 return float(-np.sum(s*np.log(s))/ln2)
def logm(a):
 s,u=np.linalg.eigh(a);assert s.min()>0
 return (u*np.log(s))@u.conj().T/ln2
def relative(a,b):return float(-entropy(a)-np.trace(a@logm(b)).real)
def h(p):return float(-(p*np.log(p)+(1-p)*np.log1p(-p))/ln2)
rows=[]
for dr in [2,3,4]:
 for db in [3,5,8]:
  for sample in range(8):
   z=rng.normal(size=(dr*db,dr*db))+1j*rng.normal(size=(dr*db,dr*db))
   omega=z@z.conj().T;omega/=np.trace(omega)
   rr=np.einsum('ijkj->ik',omega.reshape(dr,db,dr,db))
   s,u=np.linalg.eigh(rr); inv=(u*(s**(-.5)))@u.conj().T
   white=np.kron(inv,np.eye(db));c=float(np.linalg.eigvalsh(white@omega@white).max())
   d0=entropy(rr)-entropy(omega);C0=np.log2(c)-d0
   assert C0>=-1e-9
   T=db-2;indices=[i*db+j for i in range(dr) for j in range(1,T+1)]
   block=omega[np.ix_(indices,indices)];p=float(np.trace(block).real);good=block/p
   dgood0=relative(good,np.kron(rr,np.eye(T)))
   bound=np.log2(c)-(C0+h(p))/p
   assert dgood0>=bound-1e-9
   M=float(db+sample/4);r=M/(M+1)
   weights=r**np.arange(1,T+1)/(M+1);v=float(weights.sum())
   sig=np.kron(rr,np.diag(weights/v));L=(c/p)*v*(M+1)*r**(-T)
   assert L>1
   order=float(np.linalg.eigvalsh(L*sig-good).min());assert order>=-1e-9
   D=relative(good,sig);distance=float(np.abs(np.linalg.eigvalsh(good-sig)).sum()/2)
   tre_bound=np.log2(L)/(1-1/L)*distance
   assert D<=tre_bound+1e-9
   direct_lower=np.log2(c*(M+1))+np.log2(v)-(C0+1)/p
   assert D>=direct_lower-1e-9
   mu=float(np.trace(good@np.kron(np.eye(dr),np.diag(np.arange(1,T+1)))).real)
   identity=dgood0+np.log2(M+1)+np.log2(1+1/M)*mu+np.log2(v)
   assert abs(D-identity)<1e-9
   rows.append({'R':dr,'B':db,'sample':sample,'p':p,'c':c,'conditional_deficit':C0,
    'D_good':D,'D_good0':dgood0,'pinching_lower':bound,'L':L,
    'order_min_eigenvalue':order,'trace_distance':distance,'TRE_upper':tre_bound,
    'thermal_cross_entropy_identity_error':abs(D-identity)})
out={'scope':'72 finite random noncommuting states, fixed seed; validates signs/weights/finite inequalities, not Gaussian capacity, infinite Choi form or a limit',
 'seed':61420261026,'cases':len(rows),'all_passed':True,'rows':rows}
Path(__file__).with_name('checks614.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'cases':len(rows),'all_passed':True,'max_identity_error':max(x['thermal_cross_entropy_identity_error'] for x in rows)}))

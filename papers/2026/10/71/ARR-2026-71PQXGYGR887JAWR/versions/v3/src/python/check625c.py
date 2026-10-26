"""Finite noncommuting controls only; not a proof or operational capacity."""
import numpy as np
import json
from pathlib import Path
rng=np.random.default_rng(62520261026)
ln2=np.log(2.)
def ent(x):
    z=np.linalg.eigvalsh((x+x.conj().T)/2)
    z=z[z>1e-15]
    return float(-np.sum(z*np.log(z))/ln2)
def sqrtm(x):
    z,u=np.linalg.eigh((x+x.conj().T)/2)
    return (u*np.sqrt(np.maximum(z,0)))@u.conj().T
def fid(x,y):
    s=sqrtm(x)
    return float(np.trace(sqrtm(s@y@s)).real)
def T(x,y):return float(np.abs(np.linalg.eigvalsh((x-y+x.conj().T-y.conj().T)/2)).sum()/2)
def state(d):
    z=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
    x=z@z.conj().T
    return x/np.trace(x)
def h(x):return float(-(x*np.log(x)+(1-x)*np.log1p(-x))/ln2)
rows=[]
for dr in [2,3,4]:
 for db in [2,3,5]:
  for s in range(8):
   o=state(dr*db)
   if s==0:
    z=np.zeros(dr*db,complex)
    for i in range(min(dr,db)):z[i*db+i]=1/np.sqrt(min(dr,db))
    o=np.outer(z,z.conj())
   if s==1:o=np.kron(state(dr),state(db))
   rr=np.einsum('ijkj->ik',o.reshape(dr,db,dr,db))
   rb=np.einsum('ijil->jl',o.reshape(dr,db,dr,db))
   c=max(0.,ent(rr)+ent(rb)-ent(o))
   aa=2**(-c/2);t=aa*aa/8
   fbase=fid(o,np.kron(rr,rb))
   assert fbase+2e-7>=aa
   for la in [.05,.2,.5,.8,.95]:
    q=1-la
    for mode in ['random','identical','near']:
     tau=state(db)
     if mode=='identical':tau=rb
     if mode=='near':tau=(1-t/4)*rb+t/4*tau
     reset=np.kron(rr,tau)
     z=la*o+q*reset
     zb=la*rb+q*tau
     cj=ent(z)-la*ent(o)-q*ent(reset)
     cb=ent(zb)-la*ent(rb)-q*ent(tau)
     loss=cj-cb
     imix=ent(rr)+ent(zb)-ent(z)
     eps=2*la*q*2**(-c)/(3*ln2)
     slack=h(la)-eps-loss
     assert abs(loss-(la*c-imix))<2e-11
     assert loss>=-2e-11 and slack>=-2e-11
     dist=T(rb,tau)
     ff=fid(o,reset)
     db2=2*max(0.,1-fid(rb,tau))
     assert cb+2e-7>=la*q*db2/ln2
     assert h(la)-cj+2e-7>=2*la*q*ff*ff/ln2
     gram=np.array([[la,np.sqrt(la*q)*ff],[np.sqrt(la*q)*ff,q]])
     assert cj<=ent(gram)+2e-7
     assert db2+2*ff*ff+2e-7>=2*fbase*fbase/3
     if dist>=t:
      assert cb+2e-11>=2*la*q*t*t/ln2
      case='far'
     else:
      assert ff+2e-7>=aa/2
      pg=.5*(1+np.abs(np.linalg.eigvalsh(la*o-q*reset)).sum())
      assert pg<=1-la*q*ff*ff+2e-7
      assert h(la)-cj+2e-7>=-np.log2(min(1,pg))
      case='near'
     rows.append(dict(dr=dr,db=db,sample=s,la=la,mode=mode,case=case,
      mutual_information=c,loss=loss,epsilon=eps,slack=slack))
result=dict(seed=62520261026,cases=len(rows),all_passed=True,
 min_slack=min(x['slack'] for x in rows),rows=rows,
 scope='Finite diagnostics only, no infinite-state/coding/asymptotic or priority proof')
Path(__file__).with_name('checks625c.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))

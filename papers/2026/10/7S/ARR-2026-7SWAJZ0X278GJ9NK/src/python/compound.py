from pathlib import Path
import numpy as np,itertools,math,json,hashlib,shutil,datetime
r=Path(__file__).parent;rng=np.random.default_rng(577)
def ent(p):
 p=np.asarray(p);p=p[p>1e-15];return float(-np.sum(p*np.log2(p)))
def se(a):return ent(np.linalg.eigvalsh(a))
def kron(xs):
 z=np.array([[1.]])
 for x in xs:z=np.kron(z,x)
 return z
types=[]
for counts in [(2,1),(1,1,1)]:
 p=np.array(counts)/sum(counts);k=sum(counts);dim=len(p)
 words=sorted(set(itertools.permutations(sum(([j]*n for j,n in enumerate(counts)),[]))))
 for rep in range(12):
  v,_=np.linalg.qr(rng.normal(size=(6,dim))+1j*rng.normal(size=(6,dim)))
  bs=[];es=[]
  for j in range(dim):
   a=v[:,j].reshape(3,2);bs.append(a@a.conj().T);es.append(a.conj().T@a)
  # The transpose convention of complementary basis outputs is immaterial
  # for the spectra/entropy and their product mixtures checked below.
  B=sum(p[j]*bs[j] for j in range(dim));E=sum(p[j]*es[j] for j in range(dim))
  BT=sum(kron([bs[j] for j in w]) for w in words)/len(words)
  ET=sum(kron([es[j] for j in w]) for w in words)/len(words)
  dk=k*ent(p)-math.log2(len(words))
  Ic=se(B)-se(E);IT=math.log2(len(words))+se(BT)-se(ET)
  ip=ent(p)+Ic;ict=se(BT)-se(ET)
  chi=se(B)-sum(p[j]*se(bs[j]) for j in range(dim))
  chit=se(BT)-k*sum(p[j]*se(bs[j]) for j in range(dim))
  slacks=[IT-k*ip+2*dk,ict-k*Ic+dk,chit-k*chi+dk]
  assert min(slacks)>-1e-10
  types.append(dict(counts=counts,slacks=slacks,entropy_loss=dk))
compression=[]
for rep in range(24):
 u,_=np.linalg.qr(rng.normal(size=(24,24))+1j*rng.normal(size=(24,24)))
 tau=(u[:,:3]*np.array([.6,.3,.1]))@u[:,:3].conj().T
 noise=np.zeros((13,13),complex);noise[:12,:12]=tau[:12,:12];noise[12,12]=np.trace(tau[12:,12:])
 tail=float(np.linalg.eigvalsh(noise)[:-3].sum());assert tail<=.1+1e-12
 sigma=np.diag([1/12]*12+[0.])
 for lam in (.2,.5,.8):
  q=1-lam;zeta=lam*3/12+q*.1
  hfb=ent([lam,q])+lam*se(sigma)+q*se(noise)-se(lam*sigma+q*noise)
  assert hfb<=ent([zeta,1-zeta])+1e-12
  compression.append(dict(lam=lam,tail=tail,conditional_branch_entropy=hfb,fano_upper=ent([zeta,1-zeta])))
out=dict(scope='Finite floating diagnostics of type information inequalities, spectral compression and branch loss; not a proof of universal codes',type_cases=types,compression_cases=compression,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(r/'compound-check577.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status="PASS",type_cases=len(types),compression_cases=len(compression))))

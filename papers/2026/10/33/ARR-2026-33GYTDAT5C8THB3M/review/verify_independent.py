from pathlib import Path
import sys,json,hashlib,itertools,math,time
from fractions import Fraction as F
sys.path.insert(0,r'C:\Users\lluis\AppData\Roaming\Python\Python312\site-packages')
import numpy as np
import sympy as sp
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
out={'method':'Independent exact Fraction Schur elimination and causal sums; independent numerical physical reconstruction','inputs':{}}
for name in ('candidate.txt','phase-certificate-Q.json','phase-certificate-R.json'):
 out['inputs'][name]=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
Q=[[F(t) for t in r] for r in json.loads((ROOT/'phase-certificate-Q.json').read_text())]
R=[[F(t) for t in r] for r in json.loads((ROOT/'phase-certificate-R.json').read_text())]
def psd(A):
 A=[row[:] for row in A]; n=len(A); piv=[]
 assert all(A[i][j]==A[j][i] for i in range(n) for j in range(n))
 for k in range(n):
  a=A[k][k]; assert a>=0,(k,'negative pivot')
  piv.append(a)
  if a==0:
   assert all(A[k][j]==0 for j in range(k+1,n)),(k,'zero pivot with nonzero row')
   continue
  for i in range(k+1,n):
   for j in range(i,n):
    A[i][j]-=A[i][k]*A[k][j]/a
    A[j][i]=A[i][j]
 return {'rank':sum(x>0 for x in piv),'pivots_exact':[str(x) for x in piv],'smallest_positive_pivot_float':min(float(x) for x in piv if x>0)}
out['psd']={}
for name,A in [('Q',Q),('R',R),('Q-R',[[Q[i][j]-R[i][j] for j in range(32)] for i in range(32)])]:
 out['psd'][name]=psd(A)
 print(name,'PSD rank',out['psd'][name]['rank'],flush=True)
levels={5:Q}; causal=[]
for k in range(5,0,-1):
 A=levels[k]; n=len(A)
 assert all(A[i][j]==0 for i in range(n) for j in range(n) if i%2!=j%2),k
 levels[k-1]=[[A[2*i][2*j]+A[2*i+1][2*j+1] for j in range(n//2)] for i in range(n//2)]
 causal.append({'depth':k,'last_symbol_orthogonality':'exact','partial_sum':'exact'})
assert levels[0]==[[F(1)]]
out['causal']=causal; out['Q0']='1'
weights=[i.bit_count() for i in range(32)]
assert all(sum(R[i][j] for j in range(32) if weights[j]==w)==0 for i in range(32) for w in range(6))
out['RV']='exact zero'
coeff=[sum(R[i][j] for i in range(32) for j in range(32) if (i^j).bit_count()==k) for k in range(6)]
expected=list(map(F,['1086981/1250000','3225799/50000000','-3784393/6250000','-585391/25000000','-103157/390625','-2055017/50000000']))
assert coeff==expected
eta=sp.symbols('eta',real=True)
success=sum(sp.Rational(c.numerator,c.denominator)*eta**k for k,c in enumerate(coeff))
betapar=(1+6*eta**2+3*eta**4)/10
cubic=2055017*eta**3-1795904*eta**2+3225799*eta-1520760
gap=sp.factor(success-(1-betapar))
assert sp.expand(gap-(1-eta**2)*cubic/50000000)==0
assert sp.discriminant(sp.diff(cubic,eta),eta)<0
out['success_coefficients']=[str(c) for c in coeff]
out['gap']=str(gap); out['derivative_discriminant']=str(sp.discriminant(sp.diff(cubic,eta),eta))
out['cubic_roots']=[str(x) for x in sp.nroots(cubic)]
out['eta_0_7']={'beta_parallel':str(betapar.subs(eta,sp.Rational(7,10))),'beta_certificate':str((1-success).subs(eta,sp.Rational(7,10))),'gap':str(gap.subs(eta,sp.Rational(7,10)))}
assert out['eta_0_7']['gap']=='28671035721/5000000000000'
# Numerical circuit reconstruction, independent of the author's circuit and SDP.
D=32; mem=16; Bs={0:np.eye(D,dtype=complex)[:,0:1]}; Us=[]
res=[]
for k in range(1,6):
 A=np.array(levels[k],dtype=float); B=np.zeros((D,2**k),dtype=complex)
 for a in (0,1):
  inds=np.arange(a,2**k,2); block=A[np.ix_(inds,inds)]
  lam,V=np.linalg.eigh(block)
  assert np.min(lam)>0
  factor=np.diag(np.sqrt(lam))@V.T
  B[a*mem:a*mem+len(inds),inds]=factor
 prev=Bs[k-1]; W=B[:,::2]+B[:,1::2]
 evals,evecs=np.linalg.eigh(np.array(levels[k-1],dtype=float))
 invsqrt=(evecs/np.sqrt(evals))@evecs.T
 X=prev@invsqrt; Y=W@invsqrt
 Xall=np.linalg.qr(X,mode='complete')[0]; Yall=np.linalg.qr(Y,mode='complete')[0]
 rank=X.shape[1]; U=Y@X.conj().T+Yall[:,rank:]@Xall[:,rank:].conj().T
 res.append({'k':k,'unitary_residual':float(np.linalg.norm(U.conj().T@U-np.eye(D))),'coefficient_residual':float(np.linalg.norm(U@prev-W)),'gram_residual':float(np.linalg.norm(B.conj().T@B-A))})
 Us.append(U); Bs[k]=B
B=Bs[5]; Bi=np.linalg.inv(B); M=Bi.conj().T@np.array(R,dtype=float)@Bi
out['circuit_reconstruction']=res
out['measurement_eigen_min_max']=[float(np.linalg.eigvalsh(M).min()),float(np.linalg.eigvalsh(M).max())]
rng=np.random.default_rng(948135)
null=[]; independent=[]; alt=[]
for trial in range(100):
 phases=rng.uniform(-np.pi,np.pi,2); v=Bs[0][:,0]
 for U in Us: v=np.repeat(np.exp(1j*phases),mem)*(U@v)
 null.append(float(abs(np.vdot(v,M@v))))
for trial in range(50):
 phases=rng.uniform(-np.pi,np.pi,(5,2)); v=Bs[0][:,0]
 for k,U in enumerate(Us):v=np.repeat(np.exp(1j*phases[k]),mem)*(U@v)
 mons=np.array([np.exp(1j*sum(phases[k,(i>>(4-k))&1] for k in range(5))) for i in range(32)])
 independent.append(float(np.linalg.norm(v-B@mons)))
for e in np.linspace(0,1,21):
 rho=Bs[0]@Bs[0].conj().T
 multiplier=np.kron(np.array([[1,e],[e,1]]),np.ones((mem,mem)))
 for U in Us:rho=multiplier*(U@rho@U.conj().T)
 actual=float(np.trace(M@rho).real); predicted=sum(float(c)*e**k for k,c in enumerate(coeff))
 alt.append(abs(actual-predicted))
out['physical_checks']={'static_trials':100,'max_static_reject':max(null),'independent_phase_trials':50,'max_vector_residual':max(independent),'iid_channel_trials':21,'max_success_residual':max(alt)}
# Parallel expressions checked directly for complex Schur Gram matrices and all n<=4 types.
vecs=[sp.Matrix([1,0]),sp.Matrix([sp.Rational(3,5),sp.Rational(4,5)]),sp.Matrix([sp.I*sp.Rational(3,5),sp.Rational(4,5)])]
C=sp.Matrix(3,3,lambda i,j:(vecs[j].conjugate().T*vecs[i])[0])
count=0
for n in range(1,5):
 groups={}
 for word in itertools.product(range(3),repeat=n):
  typ=tuple(word.count(a) for a in range(3));groups.setdefault(typ,[]).append(word)
 for typ,words in groups.items():
  x=words[0]
  rowsum=sum(math.prod(C[x[k],y[k]] for k in range(n)) for y in words)
  repeated=sp.Matrix(n,n,lambda i,j:C[x[i],x[j]])
  assert sp.simplify(rowsum/len(words)-repeated.per()/math.factorial(n))==0
  count+=1
out['parallel_complex_type_checks']=count
for n in range(1,21):
 for e in [F(0),F(1,5),F(7,10),F(1)]:
  vals=[sum(F(math.comb(w,j)*math.comb(n-w,j))*e**(2*j) for j in range(min(w,n-w)+1))/math.comb(n,w) for w in range(n+1)]
  assert vals[n//2]==min(vals)
out['central_type_checks']='n=1..20; eta=0,1/5,7/10,1 exact'
out['status']='PASS'
(HERE/'independent-checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='psd'},indent=2),flush=True)

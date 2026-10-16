"""Independent checks for amplified determinant paper; no author verifier imported.
Run: python -B verify_independent.py [source.tex]
All outputs beside this file. Dependencies: numpy, scipy, sympy.
Finite calculations are diagnostics, not all-dimensional proof certificates.
"""
from pathlib import Path
import sys, json, hashlib, math, itertools, time
from datetime import datetime, timezone
import numpy as np
import sympy as sp
from scipy.linalg import block_diag, expm
from scipy.optimize import minimize
BASE=Path(__file__).resolve().parent
SOURCE=Path(sys.argv[1]) if len(sys.argv)>1 else BASE/'source-reviewed-snapshot.tex'
SEED=2026101602
rng=np.random.default_rng(SEED)
t0=time.time()
R={'seed':SEED,'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'author_verifier_read_or_imported':False,'sections':{}}
def cnormal(shape): return rng.normal(size=shape)+1j*rng.normal(size=shape)
def energy(Y): return sum(np.vdot(x,x).real for x in Y)/Y[0].shape[0]
def normtuple(Y): return [x/np.sqrt(energy(Y)) for x in Y]
def matrix(K,Y): return sum(np.kron(k,y) for k,y in zip(K,Y))
def val(H):
 sign,log=np.linalg.slogdet(H)
 return 0. if abs(sign)==0 else float(np.exp(2*log/len(H)))
def unitary(m):
 q,r=np.linalg.qr(cnormal((m,m))); return q
A=[sp.Matrix(3,3,lambda a,b:sp.LeviCivita(i,a,b)) for i in range(3)]
K=[x/sp.sqrt(2) for x in A]
I=sp.eye(3)
assert sum((k.H*k for k in K),sp.zeros(3))==I
assert sum((k*k.H for k in K),sp.zeros(3))==I
for i,j in itertools.product(range(3),repeat=2):
 assert sp.trace(K[i].H*K[j])==int(i==j)
for i,j,k,l in itertools.product(range(3),repeat=4):
 assert sp.trace(K[i].H*K[j]*K[k].H*K[l])==sp.Rational(int(i==j and k==l)+int(i==l and j==k),4)
H3=sum((sp.kronecker_product(x,x) for x in K),sp.zeros(9))
assert H3.det()==-sp.Rational(1,256)
assert H3.eigenvals()=={sp.Integer(1):1,sp.Rational(-1,2):5,sp.Rational(1,2):3}
P=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.diag(1,-1)]
H2=sum((sp.kronecker_product(K[i],P[i]/sp.sqrt(3)) for i in range(3)),sp.zeros(6))
assert (H2.H*H2).eigenvals()=={sp.Rational(2,3):2,sp.Rational(1,6):4}
Bstar=2**(2/9)/4; b2=1/(3*2**(1/3))
R['sections']['exact_trace_and_witnesses']={'pair_checks':9,'four_trace_checks':81,'det_H3':str(H3.det()),'H3_eigenvalues':{str(k):v for k,v in H3.eigenvals().items()},'H2_squared_eigenvalues':{str(k):v for k,v in (H2.H*H2).eigenvals().items()},'Bstar':Bstar,'b2':b2}
Kn=[np.array(x.evalf(),complex) for x in K]
Pa=[np.array(x,complex) for x in P]
# Hermite contacts and sampled strict sign, including values near contacts.
x=sp.symbols('x',positive=True); u=sp.Rational(3,4)
poly=sp.log(u)+(x-u)/u+(sp.log(4)-3)/(3-u)**2*(x-u)**2
assert sp.simplify(poly.subs(x,u)-sp.log(u))==0
assert sp.simplify(sp.diff(poly,x).subs(x,u)-1/u)==0
assert sp.simplify(poly.subs(x,3)-sp.log(3))==0
xs=np.unique(np.r_[np.geomspace(1e-12,3,2000),np.linspace(.01,3,2000),.75,3])
gap=sp.lambdify(x,poly-sp.log(x),'numpy')(xs)
assert np.min(gap)>-1e-13
R['sections']['log_majorant']={'points':len(xs),'minimum_gap':float(min(gap)),'exact_contacts':True,'proof_used_separately':'Hermite third derivative 2/x^3 > 0 on (0,3]'}
# Noncommuting balanced examples and unbalanced samples.
maxmoment=maxnorm=maxvalue=0.; sampled=0
for m in range(2,11):
 for rep in range(30):
  w=rng.dirichlet(np.ones(3)); Y=[math.sqrt(wj)*unitary(m) for wj in w]
  H=matrix(Kn,Y); Q=H.conj().T@H
  err=max(abs(np.trace(Q).real/(3*m)-1/3),abs(np.trace(Q@Q).real/(3*m)-1/6))
  maxmoment=max(maxmoment,float(err)); maxnorm=max(maxnorm,float(np.linalg.norm(H,2)));maxvalue=max(maxvalue,val(H));sampled+=1
assert maxmoment<1e-12 and maxnorm<1+1e-12 and maxvalue<Bstar+1e-12
random_max=0.; normalization_resid=0.
for m in range(2,13):
 for rep in range(30):
  Y=normtuple([cnormal((m,m)) for _ in range(3)])
  H=matrix(Kn,Y); random_max=max(random_max,val(H))
  # Explicit normalized coefficients of E tensor D_m: Z_j=Y_j/sqrt(m).
  G=sum(np.kron(Kn[j],Y[j]/np.sqrt(m))/np.sqrt(m) for j in range(3))
  normalization_resid=max(normalization_resid,abs(m*m*val(G)-val(H)))
assert random_max<Bstar+1e-12 and normalization_resid<1e-12
R['sections']['sampled_bounds']={'balanced_samples':sampled,'balanced_max_moment_residual':maxmoment,'balanced_max_operator_norm':maxnorm,'balanced_max_objective':maxvalue,'unbalanced_samples':330,'unbalanced_max_objective':random_max,'amplification_normalization_max_residual':normalization_resid}
# Independent unconstrained optimization of homogeneous determinant/energy ratio.
opt=[]
for m in (2,3,4,5):
 shape=(3,m,m); count=3*m*m; N=3*m
 def unpack(v):return (v[:count]+1j*v[count:]).reshape(shape)
 def fg(v):
  Y=unpack(v); E=energy(Y); H=matrix(Kn,Y); sg,ld=np.linalg.slogdet(H)
  if abs(sg)==0:return 1e10,np.zeros_like(v)
  inv=np.linalg.inv(H).reshape(3,m,3,m)
  coeff=np.stack([np.einsum('pq,qbpa->ab',k,inv) for k in Kn])
  gr=2*coeff.conj()/N-2*Y/(m*E)
  return -2*ld/N+np.log(E),-np.r_[gr.real.ravel(),gr.imag.ravel()]
 vv=cnormal(shape);vv=np.r_[vv.real.ravel(),vv.imag.ravel()]
 f,g=fg(vv); idx=rng.choice(len(vv),8,replace=False); graderr=0.
 for ix in idx:
  h=1e-6;plus=vv.copy();minus=vv.copy();plus[ix]+=h;minus[ix]-=h
  graderr=max(graderr,abs((fg(plus)[0]-fg(minus)[0])/(2*h)-g[ix]))
 assert graderr<1e-6
 for trial in range(4):
  v=cnormal(shape);v=np.r_[v.real.ravel(),v.imag.ravel()]
  result=minimize(fg,v,jac=True,method='L-BFGS-B',options={'maxiter':500,'ftol':1e-13,'gtol':2e-8})
  Y=normtuple(unpack(result.x));obj=val(matrix(Kn,Y))
  bal=max(np.linalg.norm(sum(y.conj().T@y for y in Y)-np.eye(m)),np.linalg.norm(sum(y@y.conj().T for y in Y)-np.eye(m)))
  assert obj<=Bstar+1e-10
  opt.append({'m':m,'trial':trial,'objective':obj,'balance_residual':float(bal),'optimizer_success':bool(result.success),'iterations':int(result.nit),'gradient_check_error':graderr})
R['sections']['optimization_diagnostics']=opt
# Direct sums, including all small residue classes; lower value is not asserted optimal.
ds=[]
for m in range(2,31):
 rem={0:0,1:4,2:2}[m%3]
 blocks3=(m-rem)//3; blocks2=rem//2
 Y=[block_diag(*([Kn[j]]*blocks3+[Pa[j]/np.sqrt(3)]*blocks2)) for j in range(3)]
 actual=val(matrix(Kn,Y)); target=Bstar*(b2/Bstar)**(rem/m)
 assert abs(actual-target)<1e-12
 ds.append({'m':m,'objective':actual,'lower_formula':target,'is_equality_dimension':m%3==0})
R['sections']['direct_sums']=ds
# Reconstruct the cited Haagerup-Musat 5x5 skew unitary over M4 directly.
Q=sp.I
J=sp.diag(Q,-Q); C=sp.Matrix([[0,1],[-1,0]]); L=sp.Matrix([[0,Q],[Q,0]])
z2=sp.zeros(2); I2=sp.eye(2)
vs=[sp.diag(1,1,-1,-1),sp.BlockMatrix([[z2,I2],[I2,z2]]).as_explicit()]
vs += [sp.BlockMatrix([[z2,-T],[T,z2]]).as_explicit() for T in (J,C,L)]
alpha=(-1+sp.I*sp.sqrt(3))/2; beta=sp.conjugate(alpha)
sigma=sp.Matrix([[0,alpha,beta,beta,alpha],[alpha,0,alpha,beta,beta],[beta,alpha,0,alpha,beta],[beta,beta,alpha,0,alpha],[alpha,beta,beta,alpha,0]])/2
assert sp.simplify(sigma*sigma.H)==sp.eye(5)
U=sp.BlockMatrix([[sigma[i,j]*vs[i]*vs[j] for j in range(5)] for i in range(5)]).as_explicit()
assert sp.simplify(U*U.H)==sp.eye(20)
for i in range(5):
 for j in range(5):assert sp.simplify(U[4*i:4*i+4,4*j:4*j+4]+U[4*j:4*j+4,4*i:4*i+4])==sp.zeros(4)
Un=np.array(U.evalf(),complex)
nonexception=[]
for d in (2,4,6,8,5,7,9):
 m=1 if d%2==0 else 4
 V=block_diag(*([np.array([[0,1],[-1,0]],complex)]*(d//2))) if m==1 else block_diag(Un,*([np.kron(np.array([[0,1],[-1,0]],complex),np.eye(4))]*((d-5)//2)))
 H=np.sqrt(2/(d*(d-1)))*V
 assert np.linalg.norm(V.conj().T@V-np.eye(d*m))<1e-12
 assert abs(val(H)-2/(d*(d-1)))<1e-12
 nonexception.append({'d':d,'m':m,'objective':val(H)})
R['sections']['haagerup_musat_and_even_witnesses']={'exact_M5_tensor_M4_unitary_and_skew':True,'spectral_ceiling_examples':nonexception}
# Explicit lower-witness and upper inequalities for channels with certified ranks.
def replacer(d,r):
 K=[]
 for a in range(r):
  for b in range(d):
   k=np.zeros((d,d),complex);k[a,b]=1/np.sqrt(r);K.append(k)
 return K
cases=[]
for d in (2,3,4,5):
 for r in (1,d-1,d):cases.append((f'replacer_{d}_rank{r}',d,r,replacer(d,r)))
cases.append(('W3',3,3,Kn))
noise=[];lower_resid=0.;upper_ratio=0.;energy_resid=0.
for name,d,r,Ks in cases:
 for m in (1,2,3,5):
  Ys=normtuple([cnormal((m,m)) for k in Ks]);A=matrix(Ks,Ys);N=d*m
  q=(2 if m==1 else 3*m) if name=='W3' else r*m
  U,s,Vh=np.linalg.svd(A);assert np.sum(s>1e-9)==q
  theta=1-q/N;p=q/N
  if q<N:
   V0=U[:,q:]@Vh[q:,:];B=V0/(d*np.sqrt(theta))
   Z=[np.sqrt(d)*B[a*m:(a+1)*m,b*m:(b+1)*m] for a in range(d) for b in range(d)]
   energy_resid=max(energy_resid,abs(energy(Z)-1))
  for eps in (.5,.01,1e-4,1e-7):
   if q<N:
    H=np.sqrt((1-eps)*p)*A+np.sqrt(eps*theta)*B
    formula=((1-eps)*p)**p*np.exp(np.sum(np.log(s[:q]**2))/N)*(eps/d**2)**theta
   else:
    H=np.sqrt(1-eps)*A;formula=(1-eps)*val(A)
   obs=val(H);lower_resid=max(lower_resid,abs(obs-formula)/max(formula,1e-300))
   # Independent random feasible noisy tuple, both fixed and noncommutative upper bound.
   raw=normtuple([cnormal((m,m)) for _ in range(len(Ks)+d*d)])
   AA=matrix(Ks,raw[:len(Ks)]);BB=np.block([[raw[len(Ks)+a*d+b]/np.sqrt(d) for b in range(d)] for a in range(d)])
   HH=np.sqrt(1-eps)*AA+np.sqrt(eps)*BB;vv=val(HH)
   ss=np.linalg.svd(HH,compute_uv=False)
   assert np.sum(ss[q:]**2)<=eps*np.linalg.norm(BB,'fro')**2+1e-10
   for th in (theta,1-r/d):
    ub=(1/(1-th))**(1-th)*(eps/(d*d*th))**th if th>0 else 1.
    assert vv<=ub+1e-11;upper_ratio=max(upper_ratio,vv/ub)
   noise.append({'case':name,'m':m,'eps':eps,'rank':q,'theta_m':theta,'witness_value':obs,'lower_formula':float(formula)})
assert lower_resid<1e-6 and energy_resid<1e-12
R['sections']['noise_law']={'examples':noise,'max_relative_lower_formula_residual':lower_resid,'max_noise_coefficient_energy_residual':energy_resid,'largest_random_value_over_upper_bound':upper_ratio}
# Exact replacer formula at every tested m and mixed/pure noisy ranks.
reps=[]
for d in (2,3,4,6):
 for eps in (.5,.01,1e-5):
  lam=np.full(d,eps/d);lam[0]+=1-eps
  target=np.prod(lam)**(1/d)/d
  for m in (1,2,3,5):
   H=np.kron(np.diag(np.sqrt(lam)),np.eye(m))/np.sqrt(d)
   assert abs(val(H)-target)<1e-12
   reps.append({'d':d,'m':m,'epsilon':eps,'objective':val(H)})
R['sections']['replacer_formula']=reps
R['status']='PASS';R['elapsed_seconds']=time.time()-t0;R['completed_at']=datetime.now(timezone.utc).isoformat()
R['limitations']=['Random samples and local optimization are not a universal proof or a certificate of global optimality.','Rank values in noise examples are known for the chosen spaces; no general noncommutative-rank algorithm is implemented.','The manuscript proofs and cited primary theorems were audited separately.','No author verification code or development report was read.']
(BASE/'independent-checks.json').write_text(json.dumps(R,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':R['status'],'elapsed_seconds':R['elapsed_seconds'],'max_moment_residual':maxmoment,'noise_examples':len(noise),'lower_witness_max_relative_error':lower_resid,'optimization_maxima':{str(m):max(x['objective'] for x in opt if x['m']==m) for m in (2,3,4,5)}}))

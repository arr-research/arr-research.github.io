"""Independent checks of the frozen capacity-bridge manuscript.
Uses numpy/sympy/scipy; no author verification code is read or imported.
All created files resolve beside __file__. Finite diagnostics do not prove limits.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,math,time
import numpy as np
import sympy as sp
BASE=Path(__file__).resolve().parent
rng=np.random.default_rng(2026101607)
R={'source_sha256':hashlib.sha256((BASE/'source-reviewed-snapshot.tex').read_bytes()).hexdigest(),'seed':2026101607,'author_code_read':False,'sections':{}}
t0=time.time()
I=sp.I
A1=sp.Matrix([[2,1+I],[1-I,3]])
D=sp.diag(4,9)
A=[A1,D-A1,sp.Matrix([[0,-I],[I,0]])]
S=sp.diag(sp.Rational(1,2),sp.Rational(1,3))
At=[S*T*S for T in A]
b=[1,1,0];eps=sp.Rational(2,5)
Y=[sp.Matrix([[1,I],[2,0]]),sp.Matrix([[0,1],[I,1]]),sp.Matrix([[1+I,2],[0,-I]])]
N=2;d=2
H=sum((sp.kronecker_product(T,U) for T,U in zip(At,Y)),sp.zeros(4))
E=sp.simplify(sum(sp.trace(U*U.H) for U in Y)/N)
Z=[sp.BlockMatrix([[sp.zeros(N),U],[U.H,sp.zeros(N)]]).as_explicit()+I*eps*bi*sp.eye(2*N) for U,bi in zip(Y,b)]
energy=sp.simplify(sum(sp.trace(U*U.H) for U in Z)/(2*N))
assert energy==E+eps**2*sum(t*t for t in b)
L=sum((sp.kronecker_product(T,U) for T,U in zip(At,Z)),sp.zeros(8))
reg=H.H*H+eps**2*sp.eye(d*N)
detL=sp.simplify(L.det());detR=sp.simplify(reg.det())
assert sp.simplify(detL-(-1)**(d*N)*detR)==0
Q=sp.Matrix(len(Y),len(Y),lambda i,j:sp.trace(Y[i]*Y[j].H)/N)
assert Q==Q.H
assert any(sp.im(q)!=0 for q in Q)
X=sp.Matrix([[2,I],[-I,1]])
assert X.det()==1
HXH=H*sp.kronecker_product(X,sp.eye(N))*H.H
partial=sp.Matrix(d,d,lambda i,j:sum(HXH[i*N+k,j*N+k] for k in range(N))/N)
phi=sum((Q[i,j]*At[i]*X*At[j].H for i in range(3) for j in range(3)),sp.zeros(d))
assert sp.simplify(partial-phi)==sp.zeros(d)
# Negative control: conjugating covariance indices gives a different map here.
wrong=sum((sp.conjugate(Q[i,j])*At[i]*X*At[j].H for i in range(3) for j in range(3)),sp.zeros(d))
assert sp.simplify(phi-wrong)!=sp.zeros(d)
# Capacity scaling is checked pointwise under its determinant-one substitution.
c=D.det()**(-sp.Rational(1,d));Xorig=S*X*S/c
assert Xorig.det()==1
porig=sum((Q[i,j]*A[i]*Xorig*A[j].H for i in range(3) for j in range(3)),sp.zeros(d))
assert sp.simplify(phi.det()-D.det()**(-2)*porig.det())==0
Horig=sum((sp.kronecker_product(T,U) for T,U in zip(A,Y)),sp.zeros(4))
assert sp.simplify(H.det()-D.det()**(-N)*Horig.det())==0
R['sections']['exact_rational']={'d':d,'N':N,'E':str(E),'shift_energy':str(eps**2*sum(t*t for t in b)),'total_energy':str(energy),'regularized_determinant':str(detR),'dilation_identity':True,'complex_covariance_identity':True,'wrong_covariance_negative_control':True,'congruence_F':True,'congruence_capacity_substitution':True}

def cn(shape):return (rng.normal(size=shape)+1j*rng.normal(size=shape))/np.sqrt(2)
def herm(n):
 T=cn((n,n));return (T+T.conj().T)/2

def pencil(As,Ys):return sum(np.kron(A,Y) for A,Y in zip(As,Ys))
def energy_np(Ys):return sum(np.vdot(Y,Y).real for Y in Ys)/len(Ys[0])
def log_obj(H):return 2*np.linalg.slogdet(H)[1]/len(H)
def invsqrt(D):
 v,U=np.linalg.eigh(D);return (U/np.sqrt(v))@U.conj().T

def phi_np(As,Q,X):return sum(Q[i,j]*As[i]@X@As[j].conj().T for i in range(len(As)) for j in range(len(As)))
max_energy_error=max_det_error=max_scale_error=max_partial_error=max_jensen_excess=max_cp_error=max_dual_error=0.
negative_nonhermitian_gap=0.
for trial in range(160):
 d=1+trial%4;N=1+(trial//4)%5;s=3+(trial%2)
 T=cn((d,d));D=T@T.conj().T+np.eye(d)*(0.2+trial%3)
 As=[herm(d) for _ in range(s-1)]
 As.append(D-sum(As))
 b=np.ones(s);S=invsqrt(D);At=[S@A@S for A in As]
 assert np.linalg.norm(sum(At)-np.eye(d))<1e-10
 Ys=[cn((N,N)) for _ in range(s)]
 # Include many singular H, so the shift is genuinely needed.
 if trial%11==0:Ys=[np.zeros((N,N),complex) for _ in range(s)]
 E=energy_np(Ys);eps=10**rng.uniform(-3,0.5)
 Zs=[np.block([[np.zeros((N,N)),Y],[Y.conj().T,np.zeros((N,N))]])+1j*eps*bi*np.eye(2*N) for Y,bi in zip(Ys,b)]
 exact_energy=E+eps*eps*np.dot(b,b)
 max_energy_error=max(max_energy_error,abs(energy_np(Zs)-exact_energy)/exact_energy)
 H=pencil(At,Ys);L=pencil(At,Zs);sv=np.linalg.svd(H,compute_uv=False)
 reglog=float(np.mean(np.log(sv*sv+eps*eps)))
 left=log_obj(L)-np.log(exact_energy)
 right=reglog-np.log(exact_energy)
 max_det_error=max(max_det_error,abs(left-right))
 assert abs(left-right)<2e-9
 assert abs(energy_np([Z/np.sqrt(exact_energy) for Z in Zs])-1)<1e-12
 origlog=log_obj(pencil(As,Zs));newlog=log_obj(L)
 scale=-2*np.linalg.slogdet(D)[1]/d
 max_scale_error=max(max_scale_error,abs(newlog-origlog-scale));assert abs(newlog-origlog-scale)<1e-9
 if E==0:continue
 Yn=[Y/np.sqrt(E) for Y in Ys]
 Hn=pencil(As,Yn)
 Q=np.array([[np.trace(Y@V.conj().T)/N for V in Yn] for Y in Yn])
 assert np.linalg.eigvalsh(Q).min()>-1e-12 and abs(np.trace(Q)-1)<1e-12
 U=cn((d,d));X=U@U.conj().T+np.eye(d);X/=np.exp(np.linalg.slogdet(X)[1]/d)
 M=Hn@np.kron(X,np.eye(N))@Hn.conj().T
 partial=np.einsum('iaja->ij',M.reshape(d,N,d,N))/N
 PX=phi_np(As,Q,X)
 max_partial_error=max(max_partial_error,float(np.linalg.norm(partial-PX)/max(1,np.linalg.norm(PX))))
 jensen=log_obj(Hn)-np.linalg.slogdet(PX)[1]/d
 max_jensen_excess=max(max_jensen_excess,float(jensen));assert jensen<1e-9
 # Factorization Q=LL*: no reality restriction on covariance.
 vals,U=np.linalg.eigh(Q);Lf=U*np.sqrt(np.maximum(vals,0))
 Bs=[sum(Lf[i,j]*As[i] for i in range(s)) for j in range(s)]
 cp=sum(B@X@B.conj().T for B in Bs)
 max_cp_error=max(max_cp_error,float(np.linalg.norm(cp-PX)/max(1,np.linalg.norm(PX))))
 # Reviewer diagnostic: Hermitian coefficients give Phi_barQ=Phi_Q^*.
 dual=sum(Q[j,i]*As[i]@X@As[j] for i in range(s) for j in range(s))
 bar=phi_np(As,np.conjugate(Q),X)
 max_dual_error=max(max_dual_error,float(np.linalg.norm(dual-bar)))
 # The Hermiticity assumption is essential for this exact same construction.
 if trial<10 and d>=2:
  bad=list(At);bad[0]=bad[0]+1j*np.eye(d);bad[-1]=bad[-1]-1j*np.eye(d)
  HH=pencil(bad,Ys);LL=pencil(bad,Zs)
  badreg=np.mean(np.log(np.linalg.svd(HH,compute_uv=False)**2+eps**2))
  negative_nonhermitian_gap=max(negative_nonhermitian_gap,float(abs(log_obj(LL)-badreg)))
assert negative_nonhermitian_gap>1e-3
R['sections']['numerical_identities']={'cases':160,'dimensions_d':[1,2,3,4],'auxiliary_N':[1,2,3,4,5],'energy_max_relative_error':max_energy_error,'dilation_log_max_error':max_det_error,'congruence_log_max_error':max_scale_error,'partial_trace_max_relative_error':max_partial_error,'jensen_max_positive_excess':max_jensen_excess,'complex_covariance_cp_max_relative_error':max_cp_error,'dual_covariance_max_error':max_dual_error,'nonhermitian_negative_control_gap':negative_nonhermitian_gap}
# Exact counterexample to passing an unregularized determinant through bounded moments.
# diag(exp(-N),1,...,1) -> 1 in all moments, but squared determinant root = exp(-2).
R['sections']['order_of_limits_negative_control']={'matrices':'diag(exp(-N),1,...,1)','bounded_norm':1,'moment_limit':'1','unregularized_squared_determinant_root':'exp(-2)','limit_FK_squared':1,'regularized_first_then_epsilon_limit':1}
assert np.exp(-2)<1
# Uniform projections: the exact normalized optimum is prod_i (r_i/d)^(r_i/d).
projections=[]
for ranks in ([1,1],[1,2],[1,2,3],[2,2,1]):
 d=sum(ranks);As=[];start=0
 for rank in ranks:
  A=np.zeros((d,d));A[start:start+rank,start:start+rank]=np.eye(rank);As.append(A);start+=rank
 w=np.array(ranks)/d;expected=float(np.exp(np.sum(w*np.log(w))))
 for N in [1,3,5]:
  Ys=[np.sqrt(x)*np.eye(N) for x in w]
  assert abs(np.exp(log_obj(pencil(As,Ys)))-expected)<1e-12
 projections.append({'ranks':ranks,'exact_value':expected})
R['sections']['projection_examples']=projections
# Scalar circular reference: MP density with aspect ratio one has log integral -1.
# Elementary substitution t=4sin^2(theta), density dt=(4/pi)cos^2(theta)dtheta.
from scipy.integrate import quad
integral,error=quad(lambda th:(4/np.pi)*np.cos(th)**2*np.log(4*np.sin(th)**2),0,np.pi/2,epsabs=1e-11)
assert abs(integral+1)<1e-10
R['sections']['circular_constant']={'log_squared_determinant':integral,'expected':-1,'factor':float(np.exp(integral)),'quadrature_error_estimate':error}

# Added after the source revision: real covariance and normal same-size witnesses.
# These checks are separate from the initially frozen dilation/circular audit.
Qreal=(Q+Q.conjugate())/2 if isinstance(Q,sp.MatrixBase) else None
# Recreate rational objects because the numerical loops reuse variable names.
Ar=[sp.Matrix([[2,1+I],[1-I,3]]),sp.diag(4,9)-sp.Matrix([[2,1+I],[1-I,3]]),sp.Matrix([[0,-I],[I,0]])]
Sr=sp.diag(sp.Rational(1,2),sp.Rational(1,3));Atr=[Sr*T*Sr for T in Ar]
Yr=[sp.Matrix([[1,I],[-I,2]]),sp.Matrix([[3,1],[1,-1]]),sp.Matrix([[0,2*I],[-2*I,1]])]
br=[1,1,0];er=sp.Rational(2,5);nr=2
Hr=sum((sp.kronecker_product(T,U) for T,U in zip(Atr,Yr)),sp.zeros(4))
Wr=[U+I*er*bi*sp.eye(nr) for U,bi in zip(Yr,br)]
Er=sum(sp.trace(U*U.H)/nr for U in Yr)
assert all(sp.simplify(U*U.H-U.H*U)==sp.zeros(nr) for U in Wr)
assert sp.simplify(sum(sp.trace(U*U.H)/nr for U in Wr)-Er-er**2*sum(bi**2 for bi in br))==0
Lr=sum((sp.kronecker_product(T,U) for T,U in zip(Atr,Wr)),sp.zeros(4))
assert sp.simplify(Lr-Hr-I*er*sp.eye(4))==sp.zeros(4)
assert sp.simplify(Lr.det()*sp.conjugate(Lr.det())-(Hr**2+er**2*sp.eye(4)).det())==0
normal_energy_error=normal_log_error=normal_commutator_error=real_factor_error=0.
for trial in range(80):
 d=1+trial%4;N=1+(trial//4)%5;s=3+trial%2
 As=[herm(d) for _ in range(s-1)];As.append(np.eye(d)-sum(As));b=np.ones(s)
 V=cn((s,s));q=V@V.conj().T;q/=np.trace(q);qr=q.real
 assert np.linalg.eigvalsh(qr).min()>-1e-12 and abs(np.trace(qr)-1)<1e-12
 vals,U=np.linalg.eigh(qr);Lreal=U*np.sqrt(np.maximum(vals,0))
 real_factor_error=max(real_factor_error,float(np.linalg.norm(Lreal@Lreal.T-qr)))
 G=[herm(N) for _ in range(s)];Ys=[sum(Lreal[i,j]*G[j] for j in range(s)) for i in range(s)]
 E=energy_np(Ys);eps=10**rng.uniform(-3,0.5);cost=E+eps**2*np.dot(b,b)
 Ws=[(Y+1j*eps*bi*np.eye(N))/np.sqrt(cost) for Y,bi in zip(Ys,b)]
 H=pencil(As,Ys);Hshift=pencil(As,Ws)
 normal_energy_error=max(normal_energy_error,abs(energy_np(Ws)-1))
 for W in Ws:normal_commutator_error=max(normal_commutator_error,float(np.linalg.norm(W@W.conj().T-W.conj().T@W)))
 ev=np.linalg.eigvalsh(H);expected=float(np.mean(np.log(ev**2+eps**2))-np.log(cost))
 normal_log_error=max(normal_log_error,abs(log_obj(Hshift)-expected))
 assert normal_energy_error<1e-12 and normal_log_error<1e-9 and normal_commutator_error<1e-12
# Standard semicircle: s=2sin(theta); measure=(2/pi)cos(theta)^2 dtheta.
semilog,semierr=quad(lambda th:(4/np.pi)*np.cos(th)**2*np.log(4*np.sin(th)**2),0,np.pi/2,epsabs=1e-11)
assert abs(semilog+1)<1e-10
R['sections']['final_revision_normal_witnesses']={'exact_same_size_identity':True,'exact_normality':True,'cases':80,'real_covariance_factor_max_error':real_factor_error,'normal_energy_max_error':normal_energy_error,'normal_objective_log_max_error':normal_log_error,'normal_commutator_max_error':normal_commutator_error,'semicircular_log_squared_determinant':semilog,'semicircular_factor':float(np.exp(semilog)),'scope':'Added for the final source revision; capacity symmetrization is proved analytically, not certified by these tests.'}

R['status']='PASS';R['completed_at']=datetime.now(timezone.utc).isoformat();R['elapsed_seconds']=time.time()-t0
R['limitations']=['Exact finite identities and diagnostics do not prove Gaussian asymptotic freeness, the Mai-Speicher theorem, or an optimization over all covariance matrices.','The wrong-covariance and nonhermitian controls deliberately violate a convention or hypothesis; they are not counterexamples to the stated theorem.','No author verification script or other reviewer report was read.']
(BASE/'independent-checks.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':R['status'],'elapsed_seconds':R['elapsed_seconds'],'numeric':R['sections']['numerical_identities'],'circular':R['sections']['circular_constant']},ensure_ascii=False))

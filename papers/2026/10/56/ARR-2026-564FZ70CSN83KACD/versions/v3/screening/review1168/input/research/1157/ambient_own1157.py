"""Independent ambient construction: explicit Helmert frame, physical tensor outputs.
Deterministic bounded diagnostics, not interval or universal proof.
"""
import mpmath as m,json
from pathlib import Path
m.mp.dps=170;P=Path(__file__).parent
def tr(A):return sum(A[j,j] for j in range(A.rows))
def kron(A,B):return m.matrix(A.rows*B.rows,A.cols*B.cols,lambda i,j:A[i//B.rows,j//B.cols]*B[i%B.rows,j%B.cols])
# mpmath matrix does not support a callable constructor on every bundled version.
def kron(A,B):return m.matrix([[A[i//B.rows,j//B.cols]*B[i%B.rows,j%B.cols] for j in range(A.cols*B.cols)] for i in range(A.rows*B.rows)])
def pure(v):
 v=m.matrix(v);return v*v.H/tr(v*v.H)
def herm(A):return (A+A.H)/2
def eig(A):return m.eighe(herm(A))
def logmat(A):
 ds,U=eig(A);assert min(ds)>0;return U*m.diag([m.log(x) for x in ds])*U.H
def rel(A,B):return m.re(tr(A*(logmat(A)-logmat(B))))
def norm(A):return max(abs(x) for x in A)
def display(x):return m.nstr(x,70)
def one(name,ts,k,epsfactor=1,compress=False):
 n=len(ts);d=ts[0].rows;S=sum(ts,m.zeros(d));source_d=d
 if compress:
  ds,U=eig(S);inds=[i for i,x in enumerate(ds) if x>m.mpf('1e-150')];V=m.matrix([[U[a,j] for j in inds] for a in range(d)]);ts=[herm(V.H*t*V) for t in ts];d=len(inds);S=sum(ts,m.zeros(d))
 assert min(eig(S)[0])>0
 f=m.ones(n,1)/m.sqrt(n);F=f*f.H;PR=m.eye(n)-F;ps=[m.sqrt(m.mpf(n)/(n-1))*(m.eye(n)[:,i]-m.ones(n,1)/n) for i in range(n)]
 # Explicit orthonormal Helmert columns spanning f-perp.
 V=m.zeros(n,n-1)
 for j in range(1,n):
  for i in range(j):V[i,j-1]=1/m.sqrt(j*(j+1))
  V[j,j-1]=-j/m.sqrt(j*(j+1))
 assert norm(V.H*V-m.eye(n-1))<m.mpf('1e-160')
 beta=m.mpf(1)/(4*n*k);delta=m.mpf(2)**(-k);eps=epsfactor*beta*delta;alpha=m.mpf(1)/n-(n-2)*eps-beta;c=m.sqrt(alpha*beta*(1-delta))
 plus=[];minus=[]
 for psi in ps:
  base=alpha*psi*psi.H+eps*(PR-psi*psi.H)+beta*F;sg=c*(psi*f.H+f*psi.H);plus.append(herm(base+sg));minus.append(herm(base-sg))
 Di=sum(rel(a,b) for a,b in zip(plus,minus));Mp=sum([kron(a,t) for a,t in zip(plus,ts)],m.zeros(n*d));Mm=sum([kron(a,t) for a,t in zip(minus,ts)],m.zeros(n*d))
 T=sum([kron(V.H*p*p.H*V,t) for p,t in zip(ps,ts)],m.zeros((n-1)*d));Z=sum([kron(V.H*p,t) for p,t in zip(ps,ts)],m.zeros((n-1)*d,d));G=kron(m.eye(n-1),S);A=(alpha-eps)*T+eps*G
 X=c*(A**-1)*Z;H=m.zeros(n*d,d)
 for i in range((n-1)*d):
  for j in range(d):H[i,j]=X[i,j]
 for j in range(d):H[(n-1)*d+j,j]=1
 C=(m.eye(d)+X.H*X)**-1;Eb=H*C*H.H;U=V.copy();U=m.matrix([[V[i,j] if j<n-1 else f[i] for j in range(n)] for i in range(n)]);Uf=kron(U,m.eye(d));E=herm(Uf*Eb*Uf.H)
 p=m.re(tr(E*Mp));q=m.re(tr(E*Mm));Be=Z.H*(A**-1)*Z;Q=beta*S-c*c*Be
 Db=p*m.log(p/q)+(1-p)*m.log((1-p)/(1-q));Do=rel(Mp,Mm)
 reversed_db=q*m.log(q/p)+(1-q)*m.log((1-q)/(1-p))
 Efix=kron(F,m.eye(d));pf=tr(Efix*Mp);qf=tr(Efix*Mm)
 expected=m.zeros(n*d)
 for i in range(n*d):
  for j in range(n*d):
   expected[i,j]=A[i,j] if i<(n-1)*d and j<(n-1)*d else (c*Z[i,j-(n-1)*d] if i<(n-1)*d else (c*Z.H[i-(n-1)*d,j] if j<(n-1)*d else beta*S[i-(n-1)*d,j-(n-1)*d]))
 errors={'trace':abs(tr(Mp)-1),'common_R':norm(sum(plus,m.zeros(n))-sum(minus,m.zeros(n))),'projector':norm(E*E-E),'q_identity':abs(q-tr(C*Q)),'p_identity':abs(p-q-4*c*c*tr(C*Be)),'fixed_effect_no_signal':abs(pf-qf),'physical_block':norm(Uf.H*Mp*Uf-expected)}
 assert max(errors.values())<m.mpf('1e-100')
 assert 0<q<p<1 and Db<Do+ m.mpf('1e-100') and Do<Di+m.mpf('1e-100')
 return {'name':name,'n':n,'B_original':source_d,'B_support':d,'k':k,'epsfactor':epsfactor,'Dinput':display(Di),'Doutput':display(Do),'Dbinary':display(Db),'retention':display(Db/Di),'quantum_retention':display(Do/Di),'reverse_retention':display(reversed_db/Di),'p':display(p),'q':display(q),'p_scaled':display(p*k),'q_scaled':display(q*4*k*2**k),'min_output_eigenvalue':display(min(eig(Mp)[0])),'max_residual':display(max(errors.values())),'AinvZ_maxentry':display(norm((A**-1)*Z))}
families=[('binary_complex',[pure([1,0]),pure([1,m.j*2/3])],16,1,False),('mixed_1_2_1',[pure([1,0]),m.eye(2)/2,pure([1,1j])],64,1,False),('kernel_T_complex_B3',[pure([1,0,0]),pure([1,1,0]),pure([1,1j,1])],64,1,False),('duplicate_pure',[pure([1,0]),pure([1,0]),pure([1,1j])],64,1,False),('common_line_rank2',[(m.eye(3)-pure(v))/2 for v in [[1,0,0],[0,1,0],[1,1j,0]]],64,1,False),('singular_S_compressed',[pure([1,0,0]),pure([1,1j,0])],64,1,True),('alternate_polynomial_epsilon_beta_over_k',[pure([1,0]),m.eye(2)/2,pure([1,1j])],64,2**58,False)]
rows=[]
for args in families:
 rows.append(one(*args));(P/'AMBIENT_OWN1157.json').write_text(json.dumps({'precision':170,'certified':False,'rows':rows},indent=2)+'\n',encoding='utf-8');print(json.dumps(rows[-1]))

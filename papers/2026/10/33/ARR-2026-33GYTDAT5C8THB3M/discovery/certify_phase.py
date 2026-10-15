import numpy as np,sympy as s,json,math
from pathlib import Path
from fractions import Fraction
p=Path(__file__).parent;n=5;N=2**n;z=np.load(p/'phase-sdp-n5-eta0.7.npz')
P=s.eye(N)
for w in range(n+1):
 ids=[i for i in range(N) if i.bit_count()==w]
 for i in ids:
  for j in ids:P[i,j]-=s.Rational(1,len(ids))
alpha=s.Rational(1,100)
Pn=np.array(P,dtype=float)
Q0=(1-float(alpha))*z['Q']+float(alpha)*np.eye(N)/N
R0=(1-float(alpha))*z['R']+float(alpha)*Pn/(2*N)
def rat(M):return s.Matrix([[s.Rational(round(float((M[i,j]+M[j,i])/2)*10**7),10**7) for j in range(M.shape[1])] for i in range(M.shape[0])])
def causal(M):
 if M.rows==1:return s.ones(1)
 a=list(range(0,M.rows,2));b=list(range(1,M.rows,2));A=M.extract(a,a);B=M.extract(b,b);D=(causal(A+B)-A-B)/2
 O=s.zeros(M.rows)
 for i in range(len(a)):
  for j in range(len(a)):O[a[i],a[j]]=A[i,j]+D[i,j];O[b[i],b[j]]=B[i,j]+D[i,j]
 return O
Q=causal(rat(Q0));R=P*rat(R0)*P
C=[]
for w in range(n+1):
 ids=[i for i in range(N) if i.bit_count()==w]
 for i in ids[1:]:
  v=s.zeros(N,1);v[i]=1;v[ids[0]]=-1;C.append(v)
C=s.Matrix.hstack(*C)
def ldlt(M):
 A=M.copy();piv=[]
 for k in range(M.rows):
  a=A[k,k];assert a>0,(k,a);piv.append(a)
  for i in range(k+1,M.rows):
   for j in range(i,M.rows):A[j,i]=A[i,j]=A[i,j]-A[i,k]*A[j,k]/a
 return piv
cert={}
for name,M in [('Q',Q),('accept',Q-R),('reject_restricted',C.T*R*C)]:
 piv=ldlt(M);cert[name]={'size':M.rows,'positive_pivots':len(piv),'min_pivot_float':min(map(float,piv))}
 print(name,cert[name],flush=True)
eta=s.Symbol('eta');co=[sum(R[i,j] for i in range(N) for j in range(N) if (i^j).bit_count()==k) for k in range(n+1)]
rej=sum(co[k]*eta**k for k in range(n+1));parallel=(1+6*eta**2+3*eta**4)/10;gap=s.factor(parallel-1+rej)
print('coeffs',[str(c) for c in co]);print('gap',gap);print('roots',s.nroots(gap,maxsteps=100));print('gap7',gap.subs(eta,s.Rational(7,10)),float(gap.subs(eta,s.Rational(7,10))))
cert.update({'n':n,'eta':'7/10','rejection_coefficients':list(map(str,co)),'parallel_failure':'(1+6 eta^2+3 eta^4)/10','advantage_at_7_10':str(gap.subs(eta,s.Rational(7,10)))})
for name,M in [('Q',Q),('R',R)]:
 (p/f'phase-certificate-{name}.json').write_text(json.dumps([[str(e) for e in row] for row in M.tolist()]))
(p/'phase-certificate-summary.json').write_text(json.dumps(cert,indent=2))

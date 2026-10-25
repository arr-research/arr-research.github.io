"""Bounded exact diagnostics for269. No novelty or universal-proof claim."""
import sympy as s,json
from pathlib import Path
def frob2(A):return s.simplify(s.trace(A.conjugate().T*A))
def partialA(D,m,k):return s.Matrix(k,k,lambda i,j:sum(D[a*k+i,a*k+j] for a in range(m)))
def project(D,m,k):
 B=partialA(D,m,k)-s.trace(D)*s.eye(k)/k
 return s.kronecker_product(s.eye(m)/m,B)
att=cone=channels=tail=0
for m in range(2,7):
 for k in [2,3]:
  d=m*k
  for r in range(1,m):
   R=s.diag(*([s.Rational(1,r)]*r+[0]*(m-r)))
   pos=s.zeros(k);pos[0,0]=1
   neg=s.zeros(k);neg[1,1]=1
   for balanced in [False,True]:
    rho=s.kronecker_product(R,pos)
    sigma=s.kronecker_product(R if balanced else s.eye(m)/m,neg)
    D=rho-sigma;P=project(D,m,k)
    want=s.Rational(r,m) if balanced else s.Rational(2*r,m+r)
    assert frob2(P)==want*frob2(D)
    assert frob2(D-P)==frob2(D)-frob2(P)
    att+=1
   # Full Hermitian directions with prescribed inertias and nonproduct rotations.
   for neg_rank in sorted(set([1,r,d-r])):
    vals=[s.Rational(1,r)]*r+[-s.Rational(1,neg_rank)]*neg_rank+[0]*(d-r-neg_rank)
    D=s.diag(*vals)
    for i,j in [(0,d-1),(0,r)]:
     O=s.eye(d);O[i,i]=O[j,j]=s.Rational(3,5);O[i,j]=s.Rational(4,5);O[j,i]=-s.Rational(4,5)
     D=O*D*O.T
    assert s.trace(D)==0
    P=project(D,m,k)
    assert frob2(P)<=s.Rational(2*r,m+r)*frob2(D)
    if neg_rank<=r:assert frob2(P)<=s.Rational(r,m)*frob2(D)
    cone+=1
for m in [3,4]:
 k=m;K0=s.eye(m);K0[m-1,m-1]=s.Rational(3,5)
 K1=s.zeros(m);K1[0,m-1]=s.Rational(4,5)
 assert K0.T*K0+K1.T*K1==s.eye(m)
 def choi(Ks):
  J=s.zeros(m*m)
  for K in Ks:
   v=s.Matrix([K[b,a] for a in range(m) for b in range(m)])
   J+=v*v.conjugate().T/m
  return J
 J=choi([K0,K1]);assert J.rank()==2 and s.trace(J)==1
 # Input marginal of every TP Choi state is known exactly.
 ptrB=s.Matrix(m,m,lambda i,j:sum(J[i*m+a,j*m+a] for a in range(m)))
 assert ptrB==s.eye(m)/m
 for u in [0,1]:
  repl=s.zeros(m);repl[u,u]=1
  S=s.kronecker_product(s.eye(m)/m,repl)
  D=J-S;P=project(D,m,k)
  assert frob2(P)<=s.Rational(4,m+2)*frob2(D)
  channels+=1
for spectrum in [[s.Rational(1,2),s.Rational(1,3),s.Rational(1,6)], [s.Rational(2,5),s.Rational(3,10),s.Rational(1,5),s.Rational(1,10)]]:
 for r in range(1,len(spectrum)):
  tau=sum(spectrum[r:]);mass=1-tau
  eta2=sum((v-v/mass)**2 for v in spectrum[:r])+sum(v*v for v in spectrum[r:])
  assert eta2<=2*tau*tau;tail+=1
out={'status':'PASS_EXACT_BOUNDED_DIAGNOSTICS','attainer_cases':att,'coherent_inertia_cases':cone,'nonunital_TP_channel_comparisons':channels,'spectral_tail_cases':tail,'scope':'Rational exact finite controls, not a global proof or optimal channel-domain constant. No source statement or PDF modified, no score.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))

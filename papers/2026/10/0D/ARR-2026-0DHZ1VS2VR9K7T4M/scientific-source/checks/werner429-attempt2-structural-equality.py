from pathlib import Path
from itertools import product,combinations
import sympy as s
import json,time
r=Path(__file__).resolve().parent;start=time.time();Q=s.Rational
# Known six-vertex wheel graph: center0, outer1..5 cycle.
A=s.zeros(6)
for i in range(1,6):A[0,i]=A[i,0]=1;A[i,1+i%5]=A[1+i%5,i]=1
cuts=[]
for S in combinations(range(6),3):
 T=[i for i in range(6) if i not in S];det=A.extract(S,T).det();assert abs(det)==1;cuts.append({'S':S,'det':int(det)})
words=list(product(range(2),repeat=5));flat={v:i for i,v in enumerate(words)}
code=[]
for j in range(2):
 v=[]
 for x in words:
  phase=j*sum(x)+sum(x[i]*x[(i+1)%5] for i in range(5));v.append((-1)**phase)
 code.append(v)
assert s.Matrix.hstack(*[s.Matrix(v) for v in code]).T*s.Matrix.hstack(*[s.Matrix(v) for v in code])==32*s.eye(2)
coeff=[]
for k in range(6):
 G=s.SparseMatrix(64,64,{})
 for S in combinations(range(5),k):
  keep=[i for i in range(5) if i not in S];n=2**len(keep);entries={}
  for j,t,u in product(range(2),range(32),range(32)):
   if any(words[t][i]!=words[u][i] for i in S):continue
   a=sum(words[u][i]*2**(len(keep)-1-l) for l,i in enumerate(keep));b=sum(words[t][i]*2**(len(keep)-1-l) for l,i in enumerate(keep))
   key=(a*n+b,j*32+t);entries[key]=entries.get(key,0)+code[j][u]
  D=s.SparseMatrix(n*n,64,entries);G+=D.T*D/32
 coeff.append(G)
v=s.Matrix(code[0]+code[1]);P=v*v.T/64;I=s.eye(64)
def error_projection(errors):
 out=s.zeros(64,1)
 for idx,w in enumerate(product(range(2),repeat=6)):
  y=list(w);phase=1
  for slot,a,b in errors:phase*=(-1)**(b*w[slot]);y[slot]^=a
  k=sum(y[i]*2**(5-i) for i in range(6));out[k]=phase*v[idx]
 return out*out.T/64
paulis=[(1,0),(0,1),(1,1)]
Es={i:sum((error_projection([(i,a,b)]) for a,b in paulis),s.zeros(64)) for i in range(1,6)}
E1=sum(Es.values(),s.zeros(64));R=I-P-E1;Eij={}
for i,j in combinations(range(1,6),2):
 Eij[i,j]=sum((error_projection([(i,a,b),(j,c,e)]) for (a,b),(c,e) in product(paulis,repeat=2)),s.zeros(64))
 assert Eij[i,j]**2==Eij[i,j] and s.trace(Eij[i,j])==9 and R*Eij[i,j]==Eij[i,j]
for i in range(1,6):
 star=sum((v for key,v in Eij.items() if i in key),s.zeros(64));assert star**2==star and R*star==star
T=sum(Eij.values(),s.zeros(64))
assert coeff[0]==I and coeff[1]==Q(5,2)*I and coeff[2]==Q(5,2)*I
assert coeff[3]==(10*P+4*E1+T)/2 and coeff[4]==5*P+E1 and coeff[5]==2*P
Tspec=T.eigenvals();print('actual T spectrum',Tspec,flush=True)
assert sum(Tspec.values())==64 and sum(a*b for a,b in Tspec.items())==90
assert all(x>=0 and x<=s.Rational(5,2) for x in Tspec)
# Symbolic universal comparisons and monotonicity, not numeric interpolation.
d,t=s.symbols('d t',positive=True);alpha=1-5*t/d+10*t*t/d**2;eta=alpha-10*t**3/d+5*t**4-d*t**5
beta=alpha-4*t**3/d+t**4;gamma=alpha-Q(5,2)*t**3/d
assert s.simplify(beta-eta-t**3/d*((d*t-2)**2+2))==0
assert s.simplify(gamma-eta-t**3/d*((d*t-Q(5,2))**2+Q(5,4)))==0
assert s.simplify(s.diff(eta,t)+5*d*(t-1/d)**4+5*(d*d-1)/d**3)==0
assert s.factor(32*d*d*eta.subs(t,Q(1,2)))==-(d-2)*(d*d-40*d+40)
out={'status':'PASS_EXACT_FIVE_COPY_AME6_PRODUCER_CONTROLS','wheel_three_by_three_cut_determinants':cuts,'all_twenty_cuts_unimodular':True,'qubit_full_Gram_dimension':64,'all_six_parameter_coefficients_exact':True,'ten_pair_error_projections_rank':9,'five_star_sums_orthogonal_projections':True,'T_spectrum_qubit':{str(k):v for k,v in Tspec.items()},'symbolic_gap_comparisons_and_derivative':True,'endpoint_eta':{str(i):str(eta.subs({d:i,t:Q(1,2)})) for i in [2,3,5,13,38,39]},'scope':'General proof in429text, not inferred from one code. Graph/wheel/QEC ingredients prior. No new paper/importance or global rank2 claim.','seconds':time.time()-start}
(r/'werner429-ame6-controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)

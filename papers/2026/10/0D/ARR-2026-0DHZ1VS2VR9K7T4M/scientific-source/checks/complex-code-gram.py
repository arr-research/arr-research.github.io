"""Exact non-real-code conjugation control; no external files or network."""
from pathlib import Path
from itertools import product,combinations
import sympy as s
import json
r=Path(__file__).resolve().parent;words=list(product(range(3),repeat=3));flat={v:i for i,v in enumerate(words)};Q=s.Rational
code=[]
for j in range(3):
 v=s.zeros(27,1)
 for t in range(3):v[flat[t,(t+j)%3,(t+2*j)%3]]=s.I**(t+j)
 code.append(v)
assert s.Matrix.hstack(*code).H*s.Matrix.hstack(*code)==3*s.eye(3)
G=s.zeros(81)
for k in range(4):
 for sub in combinations(range(3),k):
  keep=[j for j in range(3) if j not in sub];n=3**len(keep);entries={}
  for i,t in product(range(3),range(27)):
   for u in range(27):
    if not code[i][u] or any(words[u][j]!=words[t][j] for j in sub):continue
    a=sum(words[u][j]*3**(len(keep)-1-l) for l,j in enumerate(keep));b=sum(words[t][j]*3**(len(keep)-1-l) for l,j in enumerate(keep))
    key=a*n+b,i*27+t;entries[key]=entries.get(key,0)+code[i][u]
  D=s.SparseMatrix(n*n,81,entries);G+=(-Q(1,2))**k*(D.H*D)/3
H={}
for i,j in product(range(3),repeat=2):
 out=s.zeros(27)
 for u,v in product(range(27),repeat=2):
  scalar=code[i][u]*s.conjugate(code[j][v])/3
  if not scalar:continue
  fs=[]
  for a,b in zip(words[u],words[v]):
   E=s.eye(3)*int(a==b);E[a,b]-=Q(1,2);fs.append(E)
  out+=scalar*s.kronecker_product(*fs)
 H[i,j]=out
J=s.BlockMatrix([[H[i,j] for j in range(3)] for i in range(3)]).as_explicit()
assert G==s.conjugate(J) and G!=J
bad=next((i,j) for i,j in product(range(81),repeat=2) if G[i,j]!=J[i,j])
assert G.eigenvals()=={Q(1,2):56,Q(3,4):24,Q(7,8):1}
out={'status':'PASS_EXACT_NONREAL_CODE_GRAM','code':'CGL code with physical first-slot and logical diagonal phases i^t and i^j; local unitaries preserve AME','correct_identity':'Gram(q(VB))=conjugate(J_LambdaV)','wrong_without_conjugation_falsifier':{'index':bad,'correct':str(G[bad]),'wrong':str(J[bad])},'dimension':81,'scope':'Exact transcription control for complex-code lemma, not a proof by samples or a novelty claim.'}
(r/'complex-code-gram.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)

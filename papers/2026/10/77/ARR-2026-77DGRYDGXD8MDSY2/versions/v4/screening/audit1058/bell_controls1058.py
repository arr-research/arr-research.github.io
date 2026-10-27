"""Own full ambient rational Bell control: channel and marginal normalization."""
from pathlib import Path
import sympy as s,json,traceback
P=Path(__file__).parent;rows=[]
try:
 d=2;n=4
 vectors=[s.Matrix(v) for v in [(1,0,0,1),(1,0,0,-1),(0,1,1,0),(0,1,-1,0)]]
 projectors=[v*v.T/2 for v in vectors]
 ptr=lambda m:s.Matrix(d,d,lambda r,t:sum(m[a*d+r,a*d+t] for a in range(d)))
 assert sum(projectors,s.zeros(n))==s.eye(n)
 assert all(ptr(v)==s.eye(d)/d for v in projectors)
 assert all(s.trace(u*v)==(1 if i==j else 0) for i,u in enumerate(projectors) for j,v in enumerate(projectors))
 probabilities=[s.Rational(1,10),s.Rational(2,10),s.Rational(3,10),s.Rational(4,10)]
 rho=sum([w*v for w,v in zip(probabilities,projectors)],s.zeros(n));B=s.kronecker_product(s.eye(d)/d,ptr(rho));assert B==s.eye(n)/n
 for lam in [-s.Rational(1,3),s.Rational(0),s.Rational(1,2),s.Rational(1)]:
  out=lam*rho+(1-lam)*B;weights=[lam*w+(1-lam)/n for w in probabilities]
  assert out==sum([w*v for w,v in zip(weights,projectors)],s.zeros(n)) and min(weights)>0 and s.trace(out)==1
  rows.append({'d':d,'lambda':str(lam),'shared_reference':'I_2/2','replacement':'I_4/4','output_probabilities':list(map(str,weights)),'full_matrix_identity':True})
 (P/'BELL_CONTROLS1058.json').write_text(json.dumps({'scope':'Full rational qubit matrices only; general Bell argument is analytic, not inferred from these controls. No phase cases added.','cases':rows},indent=2)+'\n',encoding='utf-8');print('Four rational full-ambient Bell channel and marginal controls passed.')
except Exception as ex:
 (P/'BELL_FAILURE1058.json').write_text(json.dumps({'error':repr(ex),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise

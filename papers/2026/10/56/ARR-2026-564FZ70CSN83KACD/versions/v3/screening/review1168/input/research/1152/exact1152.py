from pathlib import Path
import sympy as s,json,datetime
P=Path(__file__).parent

def pure(v):
 x=s.Matrix(v);return x*x.H/(x.H*x)[0]
def plane(v):return (s.eye(len(v))-pure(v))/2
cases=[('two_pure',[pure([1,0]),pure([1,1])],True),('three_complex',[pure([1,0]),pure([1,s.I]),pure([1,2+s.I])],True),('three_mixed',[plane([1,0,0]),plane([1,1,0]),plane([1,1,1])],True),('same_fullrank',[s.eye(2)/2,s.eye(2)/2],False)]
rows=[]
for name,ts,expect in cases:
 n=len(ts);d=ts[0].rows;T=s.zeros(n*d);Z=s.zeros(n*d,d);S=sum(ts,s.zeros(d));I=s.eye(n)
 for i,t in enumerate(ts):
  psi=I[:,i]-s.ones(n,1)/n;T+=s.kronecker_product(psi*psi.H,t);Z+=s.kronecker_product(psi,t)
 T=T.applyfunc(s.simplify);Z=Z.applyfunc(s.simplify);S=S.applyfunc(s.simplify)
 Y,params=T.gauss_jordan_solve(Z)
 Y=Y.subs({x:0 for x in params})
 assert (T*Y-Z).applyfunc(s.simplify)==s.zeros(n*d,d)
 R=(S-Z.H*Y).applyfunc(s.simplify)
 zero=R==s.zeros(d);assert zero==expect
 rows.append({'case':name,'n':n,'d':d,'rank_T':T.rank(),'residual':str(R),'zero_residual':zero,'expected_zero':expect})
(P/'EXACT1152.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'exact rational complex SymPy linear solve T Y=Z and quadratic residual; no interval claim','cases':rows},indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows))

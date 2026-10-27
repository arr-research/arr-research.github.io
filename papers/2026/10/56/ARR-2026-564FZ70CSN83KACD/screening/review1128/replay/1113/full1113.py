from pathlib import Path
from fractions import Fraction as F
import mpmath as m,json,hashlib,traceback
m.mp.dps=400
C=Path(__file__).parent
source=Path('C:/Trabajo/airr/2026-10-27_simplex1128-review/replay/1110')
control=json.loads((source/'CONTROL1110.json').read_text())
def rat(s):
 f=F(s);return m.mpf(f.numerator)/f.denominator
def tr(a):return sum(a[i,i] for i in range(a.rows))
def logmat(a):
 w,v=m.eigsy(a);assert w[0]>0
 return v*m.diag([m.log(x) for x in w])*v.T,w,v
def divergence(a,b):return tr(a*(logmat(a)[0]-logmat(b)[0]))
def in_iv(x,j):return m.mpf(j['lo_integer'])/(2**j['denominator_power_of_2'])<x<m.mpf(j['hi_integer'])/(2**j['denominator_power_of_2'])
rows=[]
try:
 for row in control['cases'][:3]:
  n=row['n'];k=row['k'];alpha=rat(row['alpha']);beta=rat(row['beta']);epsilon=rat(row['epsilon']);coh=m.sqrt(rat(row['coherence_squared']))
  f=m.matrix([1/m.sqrt(n)]*n);flag=f*f.T;P=m.eye(n)-flag
  plus=[];minus=[]
  for i in range(n):
   e=m.matrix(n,1);e[i]=1
   psi=m.sqrt(m.mpf(n)/(n-1))*(e-f/m.sqrt(n));proj=psi*psi.T
   base=alpha*proj+epsilon*(P-proj)+beta*flag;off=coh*(psi*f.T+f*psi.T)
   plus.append(base+off);minus.append(base-off)
  rp=sum(plus,m.zeros(n));rm=sum(minus,m.zeros(n));assert m.norm(rp-rm)<m.mpf('1e-380')
  def diag(blocks):
   out=m.zeros(n*n)
   for i,b in enumerate(blocks):
    for j in range(n):
     for l in range(n):out[i*n+j,i*n+l]=b[j,l]
   return out
  rho=diag(plus);sigma=diag(minus);orho=diag([(rp-b)/(n-1) for b in plus]);osigma=diag([(rm-b)/(n-1) for b in minus])
  assert abs(tr(rho)-1)<m.mpf('1e-380') and abs(tr(sigma)-1)<m.mpf('1e-380')
  di=divergence(rho,sigma);do=divergence(orho,osigma)
  _,w,v=logmat(osigma)
  # Entire9x9 output spectrum: select the n smallest eigenvectors, no block formula for E.
  E=sum((v[:,j]*v[:,j].T for j in range(n)),m.zeros(n*n))
  assert m.norm(E*E-E)<m.mpf('1e-380')
  p=tr(E*orho);q=tr(E*osigma);db=p*m.log(p/q)+(1-p)*m.log((1-p)/(1-q))
  values=dict(input_Umegaki=di,output_Umegaki=do,binary_D=db,p=p,q=q,measured_retention=db/di)
  checks={key:in_iv(value,row[key]) for key,value in values.items()};assert all(checks.values())
  rows.append({'n':n,'k':k,'ambient_dimension':n*n,'all_six_quantities_inside_directed_intervals':checks,'values_display_only':{key:m.nstr(value,60) for key,value in values.items()},'smallest_full_input_eigenvalue':m.nstr(logmat(rho)[1][0],60),'common_marginal_residual':m.nstr(m.norm(rp-rm),10)})
 (C/'FULLMATRIX1113.json').write_text(json.dumps({'method':'full ambient matrix construction and400decimal eigendecomposition diagnostic; not interval arithmetic proof or independent reviewer','source_manifest_sha256':hashlib.sha256((source/'MANIFEST1110.json').read_bytes()).hexdigest(),'cases':rows},indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'full_cases':len(rows),'all_match':True}))
except Exception as e:
 (C/'FAILURE1113.json').write_text(json.dumps({'error':repr(e),'traceback':traceback.format_exc(),'completed':rows},indent=2));raise

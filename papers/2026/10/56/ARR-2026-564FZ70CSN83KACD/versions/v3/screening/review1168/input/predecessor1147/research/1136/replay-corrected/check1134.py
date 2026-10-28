from pathlib import Path
from fractions import Fraction
import mpmath as m, json, traceback, datetime
m.mp.dps=140
C=Path(__file__).parent

def rat(x):
 f=Fraction(x);return m.mpf(f.numerator)/f.denominator

def tr(a):return sum(a[i,i] for i in range(a.rows))
def logmat(a):
 w,v=m.eigsy(a);assert min(w)>0
 return v*m.diag([m.log(x) for x in w])*v.T

def D(a,b):return tr(a*(logmat(a)-logmat(b)))

base3=[['0','1/3','2/5'],['3/4','0','3/5'],['1/4','2/3','0']]
base4=[['0','1/4','1/2','1/7'],['1/2','0','1/6','2/7'],['1/3','1/2','0','4/7'],['1/6','1/4','1/3','0']]
cases=[('asymmetric3',base3),('asymmetric4',base4)]
flagged=[[str(Fraction(x)*Fraction(9,10)) for x in row] for row in base3]+[['1/10']*3]
positive=[[str(Fraction(x)*Fraction(9,10)+Fraction(1,30)) for x in row] for row in base3]
cases += [('flagged_replacement_0.1',flagged),('fullsupport_noise_0.1',positive)]
rows=[]
try:
 for label,strings in cases:
  n=len(strings[0]);K=[[rat(x) for x in row] for row in strings]
  assert all(sum(row[i] for row in K)==1 for i in range(n))
  dob=sum(min(row) for row in K)
  for k in (16,64,128):
   beta=m.mpf(1)/(4*n*k);delta=m.mpf(2)**(-k);eps=beta*delta
   alpha=m.mpf(1)/n-(n-2)*eps-beta;c=m.sqrt(alpha*beta*(1-delta))
   f=m.matrix([1/m.sqrt(n)]*n);F=f*f.T;P=m.eye(n)-F
   plus=[];minus=[]
   for i in range(n):
    e=m.matrix(n,1);e[i]=1;psi=m.sqrt(m.mpf(n)/(n-1))*(e-f/m.sqrt(n));Pi=psi*psi.T
    a=alpha*Pi+eps*(P-Pi)+beta*F;o=c*(psi*f.T+f*psi.T)
    plus.append(a+o);minus.append(a-o)
   assert m.norm(sum(plus,m.zeros(n))-sum(minus,m.zeros(n)))<m.mpf('1e-130')
   di=sum(D(a,b) for a,b in zip(plus,minus));do=m.mpf(0);p=m.mpf(0);q=m.mpf(0)
   has_proper=any(any(w) and min(w)==0 for w in K)
   for w in K:
    if not any(w):continue
    a=sum((w[i]*plus[i] for i in range(n)),m.zeros(n));b=sum((w[i]*minus[i] for i in range(n)),m.zeros(n))
    do += D(a,b)
    if has_proper and min(w)>0:continue
    vals,vec=m.eigsy(b)
    overlaps=[abs((f.T*vec[:,j])[0])**2 for j in range(n)]
    j=max(range(n),key=lambda j:overlaps[j]);u=vec[:,j];E=u*u.T
    p+=tr(E*a);q+=tr(E*b)
   db=p*m.log(p/q)+(1-p)*m.log((1-p)/(1-q))
   assert -m.mpf('1e-120')<db<=do+m.mpf('1e-120')<=di+m.mpf('1e-120')
   assert do/di <= 1-dob+m.mpf('1e-120')
   rows.append(dict(label=label,n=n,k=k,channel=strings,doeblin=m.nstr(dob,30),input_D=m.nstr(di,60),output_D=m.nstr(do,60),binary_D=m.nstr(db,60),retention=m.nstr(db/di,60),p=m.nstr(p,60),q=m.nstr(q,60),method='full physical block spectra; choose eigenbranch of minus output with maximal f overlap; ordinary 140-digit diagnostic, not certificate'))
 result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'exploratory controls, not proof or review','cases':rows,'predictions_declared_before_run':{'asymmetric3':'retention->1','asymmetric4':'retention->1','flagged_replacement_0.1':'retention->0.9','fullsupport_noise_0.1':'retention->0 for this particular family, not optimum'},'no_parameter_search':True,'measurement_correction':'First all-output eigenbranch control failed predicted flagged retention: full-support replacement row adds order-beta background and masks rare q. Original script/results preserved. Second control sets effect zero on full-support outputs when proper-support outputs exist. Same channels/k/states; no grid search. Zero-Doeblin family unchanged.'}
 (C/'CONTROL1134.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps([{'label':r['label'],'k':r['k'],'retention':r['retention'][:18]} for r in rows]))
except Exception as e:
 (C/'FAILURE1134.json').write_text(json.dumps({'exception':repr(e),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise


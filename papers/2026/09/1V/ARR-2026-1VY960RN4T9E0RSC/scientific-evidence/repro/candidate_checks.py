"""Fresh, bounded checks for the corrected B3 candidate; no global numerical proof."""
import json,time
from datetime import datetime,timezone
from pathlib import Path
import sympy as sp
import mpmath as mp
from scan_ac import zeros
from scan_evenpart import run as even_run
started=datetime.now(timezone.utc).isoformat();t=time.monotonic();checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
k,b,l,R2,K1,D=sp.symbols('k b lambda R2 K1 D',positive=True)
check('Active ctilde derivative is R2 b²',sp.simplify((2*b*K1-R2*b*b).subs(K1,R2*b)-R2*b*b)==0)
check('Zero active radius gives zero ctilde derivative',(R2*b*b).subs(b,0)==0)
check('Envelope derivative is distortion minus D',sp.simplify(R2-D-R2*b*b-(R2*(1-b*b)-D))==0)
KB=sp.Function('K_B')
GZ=KB(4*l*b)-l*b*b;GB=KB(2*(2*l)*b)-(2*l)*sp.Rational(1,2)*b*b
check('Bessel G(lambda) equals Beta G(2lambda)',sp.simplify(GZ-GB)==0)
check('Bessel distortion twice Beta distortion',sp.simplify((1-b*b)-2*sp.Rational(1,2)*(1-b*b))==0)
C=sp.Function('c_B')
check('Bessel envelope equals Beta envelope at D/2',sp.simplify(l*(1-D)-C(2*l)-((2*l)*(sp.Rational(1,2)-D/2)-C(2*l)))==0)
for q,m,rhs in [(1,sp.coth(k)-1/k,lambda m:1-m*m-2*m/k),(2,sp.coth(k/2)-2/k,lambda m:(1-m*m)/2-2*m/k)]:
 check('Exceptional Riccati q='+str(q),sp.simplify((sp.diff(m,k)-rhs(m)).rewrite(sp.exp))==0)
mp.mp.dps=45;rows=[]
for aa in ['0.3','0.5','1','2','3','5']:
 for offset in ['-0.1','0','0.1']:
  a=mp.mpf(aa);c=2*a+mp.mpf(offset);r=zeros(a,c,15*c+50,ngrid=600);pred=int(c>2*a)
  assert len(r['H'])==len(r['F'])==pred and r['sign_large']>0
  assert r['grid_points']>600
  if pred:assert r['H'][0]<r['F'][0] and r['m_at_fold'][0]>=mp.mpf('.5')
  rows.append({'a':str(a),'c':str(c),'nH':len(r['H']),'nF':len(r['F']),'grid_points':r['grid_points'],'grid_min':r['grid_min'],'grid_max':r['grid_max'],'max_relative_variance_discrepancy':str(r['maxdiff_riccati'])})
  print(json.dumps(rows[-1]),flush=True)
ev=[]
for q in [1,2,3,4,10,60]:
 r=even_run(q,ngrid=600);pred=int(q>=4)
 assert len(r['H'])==len(r['F'])==pred and r['grid_points']>600
 ev.append({'q':q,'nH':len(r['H']),'nF':len(r['F']),'grid_points':r['grid_points'],'grid_min':r['grid_min'],'grid_max':r['grid_max'],'fold_identity_absolute_errors':r['Hprime_minus_Delta_at_zeros']})
 print(json.dumps(ev[-1]),flush=True)
result={'started_at':started,'finished_at':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t,'precision_digits':mp.mp.dps,'symbolic_checks':checks,'beta_cases':rows,'evenpart_cases':ev,'scope':'Eight exact correction identities; 18 Beta and six even-part corrected-grid diagnostics. Not a full rerun of the historical 744-case scan, a proof of global zero counts, or a model assessment.'}
Path('candidate_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('PASS: all bounded correction checks',flush=True)

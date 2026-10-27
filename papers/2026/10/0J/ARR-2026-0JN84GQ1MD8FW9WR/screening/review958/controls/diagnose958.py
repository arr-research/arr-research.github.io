"""Retains and diagnoses the one strict floating comparison failure of independent958."""
import json
from pathlib import Path
import mpmath as mp
from datetime import datetime,timezone
rows=[]
for digits in [390,600,900]:
  mp.mp.dps=digits;n=20;x=1/mp.mpf(n);r=mp.power(2,-n*n);e=r/n**2
  a=(1-x)*(1-r);b=x*r;lam=mp.mpf('.5')
  def D(a,b,e):
    u=(a+b+mp.sqrt((a-b)**2+4*e*e))/2;v=(a*b-e*e)/u
    return u*mp.log(u)+v*mp.log(v)-a*mp.log(a)-b*mp.log(b)
  q=D(lam*a,lam*b,lam*e)/D(a,b,e)
  rows.append(dict(dps=digits,ratio=mp.nstr(q,40),signed_difference=mp.nstr(q-lam,30),
       absolute_difference=mp.nstr(abs(q-lam),30)))
out=dict(utc=datetime.now(timezone.utc).isoformat(),original_failure='finite_family n=20 lambda=.5 a=b=0',
  reason='Strict q<=target compares an exactly equal analytic quantity using cancellation-prone high-precision floating arithmetic. The signed residual shrinks with increased precision.',
  exact_resolution='When tau has zero support on the two input levels, both the perturbed block and product block at output are lambda times their inputs; other levels are identical. Tr rho=Tr S on the block, so logarithmic lambda terms cancel and D(lambda rho || lambda S)=lambda D(rho||S). Hence q=lambda exactly. No manuscript counterexample.',
  original_attempt_preserved=True,precision_rows=rows)
Path(__file__).with_name('DIAGNOSE958.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))

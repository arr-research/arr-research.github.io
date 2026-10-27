from pathlib import Path
from fractions import Fraction as F
import mpmath as m,json,datetime
C=Path(__file__).parent;m.iv.dps=90
def iv(x):x=F(x);return m.iv.mpf(x.numerator)/x.denominator
def plane(d,p,e):
 a=d-1;q=a+e*e;A=1+(d*a-1)*p;FF=1+(d-1)*p
 tr=(A+FF*e*e)/(d*q);dt=e*e*(1-p)*(1+(d*d-1)*p)/(d*d*q*q)
 assert tr>0 and dt>0
 z=m.iv.sqrt(iv(tr*tr-4*dt));hi=(iv(tr)+z)/2;lo=iv(dt)/hi
 ell=(m.iv.log(hi)-m.iv.log(lo))/z
 return ell
rows=[]
for d in [3,4]:
 for e in [F(1,100),F(1,1000)]:
  theta=F(99,100);lam=-F(1,d*d-1);a=d-1;q=a+e*e
  ellin=plane(d,theta,e);ellout=plane(d,lam*theta,e)
  ratio=iv(lam*lam)*ellout/ellin
  bell=lam*lam*F(d*d,2)/(1+lam*(F(d*d,2)-1));gap=ratio-iv(bell)
  assert gap.a>0
  din=iv(4*theta*theta*e*e*a/(q*q))*ellin
  # Both states are related by a local reflection, preserving order exactly.
  # The channel output uses the legal local CP endpoint.
  K=1+(d*d-1)*theta
  rows.append(dict(d=d,e=str(e),theta=str(theta),lambda_=str(lam),phase='pi, exact local reflection',actual_order=str(K),input_relative_entropy=str(din),ratio=str(ratio),specific_bell_endpoint=str(bell),gap=str(gap),exact_binary_endpoints={k:[[str(vv) for vv in x] for x in z._mpi_] for k,z in [('ratio',ratio),('gap',gap),('input',din)]},scope='Outward interval certificate using mpmath.iv90digits; implementation not independently audited. Positivity follows rational plane determinant and untouched positive replacement modes.'))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),rows=rows,all_four_gaps_positive=True,prior_best_not_claimed=True,not_robustness_or_optimum_certificate=True)
(C/'INTERVAL1051.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('Four fixed finite-pi local-phase gaps over the specific Bell endpoint are interval-positive at e=1/100 and1/1000.')

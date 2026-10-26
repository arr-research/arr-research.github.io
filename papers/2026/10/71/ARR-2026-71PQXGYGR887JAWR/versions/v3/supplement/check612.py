"""Finite scalar checks of612; not an operator/capacity or asymptotic proof."""
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps=180
ln2=mp.log(2)
beta=lambda x:mp.log1p(1/x)/ln2
g=lambda x: (mp.log1p(x)+x*mp.log1p(1/x))/ln2
rows=[]
for kstr in ['0.2','0.5','0.8']:
 k=mp.mpf(kstr);delta=1-k
 for estr in ['1','100','1e6','1e20','1e60']:
  E=mp.mpf(estr)
  for n in [mp.mpf('0.01'),mp.mpf(1),E**mp.mpf('.25'),E**mp.mpf('.49'),E**mp.mpf('.9'),E]:
   v=delta*E+(k+1)*n+1;D=mp.sqrt(v*v-4*k*n*(n+1))
   ul=(D+delta*(E-n)-1)/2;us=(D-delta*(E-n)-1)/2
   r=(v/D-1)/2; a=delta*(beta(ul)+(beta(ul)+beta(us))*r)
   zeta=E*abs(beta(E)-a)
   Xi=(1+1/delta)/(2*E*ln2)+k*n/(delta*E*ln2)+2*k*(n+1)/(delta**2*E*ln2)
   tol=mp.mpf('1e-100')
   assert delta*E-tol<=ul<=delta*E+k*n+tol
   assert delta*n-tol<=us<=n+tol
   assert zeta<=Xi+tol
   M=k*E+delta*n;C=g(E)+g(M)-g(ul)-g(us)
   assert C>=g(E)+mp.log(k,2)-g(n)-tol
   deriv=beta(E)+k*beta(M)-a
   assert -tol<=deriv<=2/(E*ln2)+tol
   A=(E+1)/(n+1)**2
   rows.append({'k':kstr,'E':estr,'n':mp.nstr(n,25),
    'zeta':mp.nstr(zeta,25),'Xi':mp.nstr(Xi,25),'C':mp.nstr(C,25),
    'capacity_derivative':mp.nstr(deriv,25),'A':mp.nstr(A,25)})
value={'scope':'90 finite scalar checks,180 decimal digits; no capacity optimization, formal proof or asymptotic certification',
 'cases':len(rows),'all_passed':True,'rows':rows}
Path(__file__).with_name('checks612.json').write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'cases':len(rows),'digits':mp.mp.dps,'all_passed':True}))

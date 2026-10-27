from pathlib import Path
from fractions import Fraction as F
import json,traceback,hashlib
P=Path(__file__).parent;ns={'__file__':str(P/'integer_arithmetic1068.py')};exec((P/'integer_arithmetic1068.py').read_text(),ns)
iv,I,log,saved,S=ns['iv'],ns['I'],ns['log'],ns['saved'],ns['S'];rows=[]
def plane(d,p,x):
 q=d-1+x;tr=(1+(d*(d-1)-1)*p+(1+(d-1)*p)*x)/(d*q);det=x*(1-p)*(1+(d*d-1)*p)/(d*d*q*q)
 assert tr>0 and det>0
 z=iv(tr*tr-4*det).sqrt();hi=(iv(tr)+z)/2;lo=iv(det)/hi;return (log(hi)-log(lo))/z,hi,lo
source64=json.loads(Path(r'C:\Trabajo\airr\2026-10-27_polynomial-phase1064-controls\CONTROL1064.json').read_text())['cases']
source66=json.loads(Path(r'C:\Trabajo\airr\2026-10-27_phase-tradeoff1066\CONTROL1066.json').read_text())['cases']
cases=[]
for d in [2,3,4,5,6,7,8,16,32,64,128,256,1024,65536]:cases.append(('1063',d,F(1,d*d),F(1,d),None,None))
for t in [F(1),F(1,4)]:
 for beta in [2,4]:
  for d in [2,3,4,8,16,32,64,128]:cases.append(('1066',d,t/d,F(1,d**beta),t,beta))
for t,beta in [(F(1),2),(F(1,4),4)]:
 for power in [16,32,64]:
  d=2**power;cases.append(('large_dimension',d,t/d,F(1,d**beta),t,beta))
for k in [4,16,256]:
 d=k*k;cases.append(('noninteger_beta',d,F(3,2*d),F(1,k**3),F(3,2),'3/2'))
for d in [256,65536]:cases.append(('moving_t_scope_falsifier',d,F(1,d*d),F(1,d*d),F(1,d),2))
try:
 for family,d,x,delta,t,beta in cases:
  th=1-delta;lam=-F(1,d*d-1);q=d-1+x;ci=th*th*x*(d-1)/(q*q)
  ei,hi,li=plane(d,th,x);eo,ho,lo=plane(d,lam*th,x)
  ratio=iv(lam*lam)*eo/ei;gap=ratio-iv(F(1,d*d-1));din=4*iv(ci)*ei;dout=4*iv(lam*lam*ci)*eo
  minin=delta*min(F(1),x)/(d*q);cond=hi/iv(minin);maxout=(1-lam*th)*max(F(1),x)/(d*q);condout=iv(maxout)/lo
  checked={};ref=None
  if family=='1063':ref=next((v for v in source64 if v['d']==d),None)
  if family=='1066':ref=next(v for v in source66 if v['d']==d and v['t']==str(t) and v['beta']==beta)
  if ref:
   for key,value in [('ratio',ratio),('gap',gap),('input',din),('condition',cond)]:
    a=ref[key];den=1<<a['denominator_power_of_2'];checked[key]=F(int(a['lo_integer']),den)<=F(value.l,S)<=F(value.h,S)<=F(int(a['hi_integer']),den)
   assert all(checked.values())
  row={'family':family,'d':d,'x_e_squared':str(x),'delta':str(delta),'t':str(t) if t is not None else None,'beta':beta,'ratio':saved(ratio),'d_times_retention':saved(d*ratio),'gap':saved(gap),'positive_gap':gap.l>0,'negative_gap':gap.h<0,'input':saved(din),'output':saved(dout),'condition':saved(cond),'output_condition':saved(condout),'min_input_exact':str(minin),'order_exact':str(1+(d*d-1)*th),'inside_original_intervals':checked}
  if family=='1063':row['scaled_input']=saved(d**3*din/log(I.q(d)));row['scaled_condition']=saved(cond/(d**5))
  elif family in ['1066','large_dimension']:
   row['scaled_input']=saved(d*d*din/log(I.q(d)));row['scaled_condition']=saved(cond/(d**(beta+3)))
  rows.append(row)
 (P/'INTERVAL1068.json').write_text(json.dumps({'method':'1024-bit integer directed intervals;600-term atanh plus explicit rational tail. Primitives reused from own1058/1054; new driver and precision, not independent lineage.','cases':rows,'source_interval_cases_contained':sum(bool(r['inside_original_intervals']) for r in rows),'adverse_original1064':[r['d'] for r in rows if r['family']=='1063' and r['negative_gap'] and r['inside_original_intervals']],'adverse_all_1063_controls':[r['d'] for r in rows if r['family']=='1063' and r['negative_gap']],'adverse_original1066':[{'d':r['d'],'t':r['t'],'beta':r['beta']} for r in rows if r['family']=='1066' and r['negative_gap']]},indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'cases':len(rows),'contained':sum(bool(r['inside_original_intervals']) for r in rows),'large_dR':[(r['d'],r['t'],r['beta'],r['d_times_retention']['decimal_display_only'][0]) for r in rows if r['family'] in ['large_dimension','moving_t_scope_falsifier']]},indent=2))
except Exception as ex:
 (P/'INTERVAL_FAILURE1068.json').write_text(json.dumps({'error':repr(ex),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise

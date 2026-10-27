from pathlib import Path
from fractions import Fraction as F
import json,traceback
P=Path(__file__).parent;ns={'__file__':str(P/'integer_arithmetic1077.py')};exec((P/'integer_arithmetic1077.py').read_text(),ns)
iv,I,log,saved,S=ns['iv'],ns['I'],ns['log'],ns['saved'],ns['S'];rows=[]
def kl(p,q):return p*log(p/q)+(1-p)*log((1-p)/(1-q))
def plane(d,p,x):
 q=d-1+x;aa=(1+(d*(d-1)-1)*p)/(d*q);cc=(1+(d-1)*p)*x/(d*q);tr=aa+cc;det=x*(1-p)*(1+(d*d-1)*p)/(d*d*q*q);z=iv(tr*tr-4*det).sqrt();hi=(iv(tr)+z)/2;lo=iv(det)/hi;return hi,lo,z,(log(hi)-log(lo))/z,aa,cc
source=json.loads(Path(r'C:\Trabajo\airr\2026-10-27_binary-measurement1070\CONTROL1070.json').read_text())['cases']
cases=[('original',r['d'],F(r['t']),r['beta']) for r in source]
cases += [('large_dimension',2**power,t,beta) for t in [F(1),F(1,4)] for beta in [2,4,6] for power in [8,16,32]]
cases += [('critical_beta3',65536,F(1),3),('moving_t',256,F(1,256),2),('moving_t',65536,F(1,65536),2)]
try:
 for family,d,t,beta in cases:
  x=t/d;delta=F(1,d**beta);theta=1-delta;lam=-F(1,d*d-1);q=d-1+x;csq=theta*theta*x*(d-1)/(q*q)
  h,l,z,eo,aa,cc=plane(d,lam*theta,x);_,_,_,ei,_,_=plane(d,theta,x);b2=iv(lam*lam*csq);p0=l+4*b2/z;q0=l;assert 0<q0.l<q0.h<p0.l<p0.h<S
  db=kl(p0,q0);duo=4*b2*eo;dui=4*iv(csq)*ei;fraction=db/duo;gain=db/dui;gap=gain-iv(F(1,d*d-1));assert db.l>0 and fraction.h<S
  contained={}
  if family=='original':
   ref=next(r for r in source if r['d']==d and r['t']==str(t) and r['beta']==beta)
   for name,obj in [('p0',p0),('q0',q0),('binary_D',db),('fraction_of_quantum_output',fraction),('measured_output_over_quantum_input',gain),('gap_over_Bell',gap)]:
    old=ref[name];den=1<<old['denominator_power_of_2'];contained[name]=F(int(old['lo_integer']),den)<=F(obj.l,S)<=F(obj.h,S)<=F(int(old['hi_integer']),den)
   assert all(contained.values())
  # Two distinct alternatives: fixed limiting coefficients and finite-d endpoint kernel.
  b=iv(lam*theta/q)*iv((d-1)*x).sqrt();rl=I.q(1)+iv(t)
  qlim=(iv(t*aa+cc)+2*iv(t).sqrt()*b)/rl;plim=qlim-4*iv(t).sqrt()*b/rl;assert qlim.l>0 and plim.h<S
  dlim=kl(plim,qlim)
  qkernel=iv(delta*x/(q*(1+(d-1)*x)));pkernel=qkernel+iv(4*theta*(d-1)*x/((d*d-1)*q*(1+(d-1)*x)));dkernel=kl(pkernel,qkernel)
  reverse=kl(q0,p0)
  rows.append({'family':family,'d':d,'t':str(t),'beta':beta,'p0':saved(p0),'q0':saved(q0),'binary_D':saved(db),'fraction_of_quantum_output':saved(fraction),'measured_output_over_quantum_input':saved(gain),'d_times_measured_ratio':saved(d*gain),'gap_over_Bell':saved(gap),'positive':gap.l>0,'negative':gap.h<0,'strict_finite_DPI':fraction.h<S,'contained_in_original':contained,'limiting_vector_fraction':saved(dlim/duo),'endpoint_kernel_fraction':saved(dkernel/duo),'reverse_orientation_fraction':saved(reverse/duo),'limiting_vector_q0':saved(qlim),'endpoint_kernel_q0':saved(qkernel)})
 out={'method':'1024bit integer directed intervals,600term atanh with explicit tail. Own prior arithmetic reused; not independent lineage.','cases':rows,'original_cases_contained':sum(bool(r['contained_in_original']) for r in rows),'original_adverse':[{'d':r['d'],'t':r['t'],'beta':r['beta']} for r in rows if r['family']=='original' and r['negative']]}
 assert len(out['original_adverse'])==12
 (P/'INTERVAL1077.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'cases':len(rows),'contained':out['original_cases_contained'],'adverse':len(out['original_adverse']),'selected':[{k:r[k] for k in ['family','d','t','beta']}|{'exact_fraction':r['fraction_of_quantum_output']['decimal_display_only'][0],'limit_vector_fraction':r['limiting_vector_fraction']['decimal_display_only'][0],'kernel_fraction':r['endpoint_kernel_fraction']['decimal_display_only'][0],'dmeasured':r['d_times_measured_ratio']['decimal_display_only'][0]} for r in rows if r['family']=='moving_t' or (r['family']=='large_dimension' and r['d']==2**32 and r['t']=='1')]},indent=2))
except Exception as ex:
 (P/'INTERVAL_FAILURE1077.json').write_text(json.dumps({'error':repr(ex),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise

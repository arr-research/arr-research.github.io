"""Own finite binary CQ certificate using inherited exact integer interval primitives."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from integer_arithmetic1077 import iv,log,saved,LOG2
P=Path(__file__).parent
def KL(p,q):return p*(log(p)-log(q))+(1-p)*(log(1-p)-log(1-q))
def one(k,u,name):
 beta=F(1,8*k);delta=F(1,2**k);alpha=F(1,2)-beta;c2=alpha*beta*(1-delta);r=c2/alpha**2
 h=2*u*(1+r)/(u*(1+r)**2+4*r);q=beta*delta*h;p=beta*(4-3*delta)*h
 assert 0<q<p<1
 g=iv((alpha-beta)**2+4*c2).sqrt();hi=(iv(alpha+beta)+g)/2;lo=iv(alpha*beta*delta)/hi
 din=8*iv(c2)*(log(hi)-log(lo))/g;db=KL(iv(p),iv(q));reverse=KL(iv(q),iv(p));ratio=db/din;tv=iv(u/(1+u)).sqrt()
 return dict(name=name,k=k,u=str(u),p=str(p),q=str(q),h=str(h),Dinput=saved(din),Dbinary=saved(db),retention=saved(ratio),reverse_retention=saved(reverse/din),trace_coefficient=saved(tv),retention_minus_trace=saved(ratio-tv),strictly_exceeds_trace=ratio.l>tv.h,certified_0_db_lt_di=0<db.l<db.h<din.l)
rows=[one(k,F(4,9),'fixed_complex_parameter_2i_over_3') for k in [16,64,128]]+[one(k,F(1,k*k),'varying_channel_t_1_over_k') for k in [16,64,256]]+[one(64,F(1,2**128),'root_near_identical_adverse')]
assert all(r['certified_0_db_lt_di'] for r in rows)
assert all(r['strictly_exceeds_trace'] for r in rows[:3])
out={'method':'exact integer dyadic outward intervals, 1024 bits; 600-term atanh log plus explicit tail; decimal fields display only','primitive_lineage':'own 1077 library reused unchanged; not independent primitive verification','primitive_sha256':hashlib.sha256((P/'integer_arithmetic1077.py').read_bytes()).hexdigest(),'rows':rows,'finite_exact_geometry':'EXACT_OWN1157 n2 k16; algebraic formulas valid all k>=2,t!=0','no_claim':'No universal theorem from finite controls; varying-channel cases falsify uniform graph performance only.'}
(P/'INTERVAL_OWN1157.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'name':r['name'],'k':r['k'],'retention':r['retention']['decimal_display_only'],'trace':r['trace_coefficient']['decimal_display_only'],'reverse':r['reverse_retention']['decimal_display_only']} for r in rows],indent=2))

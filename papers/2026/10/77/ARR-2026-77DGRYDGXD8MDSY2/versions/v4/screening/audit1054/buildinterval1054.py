from pathlib import Path
import hashlib
P=Path(__file__).parent
prior=Path(r'C:\Trabajo\airr\2026-10-27_principal1044-audit\integer_intervals1044.py')
prefix=prior.read_text(encoding='utf-8').split('Z=I.q(0);ONE=I.q(1);ID=')[0]
prefix=prefix.replace('BITS=1600','BITS=768').replace('N=1000','N=400')
code=r'''
def iv(x):
 x=Fraction(x);return I.q(x.numerator,x.denominator)
def binary(t):
 sign,man,exp,bc=map(int,t)
 return Fraction((-1 if sign else 1)*man*(1<<exp),1) if exp>=0 else Fraction((-1 if sign else 1)*man,1<<(-exp))
def saved(x):
 with localcontext() as c:
  c.prec=50;display=[str(Decimal(x.l)/Decimal(S)),str(Decimal(x.h)/Decimal(S))]
 return {'lo_integer':str(x.l),'hi_integer':str(x.h),'denominator_power_of_2':BITS,'decimal_display_only':display}
def plane(d,p,e):
 a=d-1;q=a+e*e;A=1+(d*a-1)*p;F=1+a*p;tr=(A+F*e*e)/(d*q);det=e*e*(1-p)*(1+(d*d-1)*p)/(d*d*q*q)
 assert tr>0 and det>0
 z=iv(tr*tr-4*det).sqrt();hi=(iv(tr)+z)/2;lo=iv(det)/hi;ell=(log(hi)-log(lo))/z
 return ell,hi,lo,tr,det
rows=[]
source=json.loads(Path(r'D:\Proyectos\airr-investigacion\2026-10-27_local-phase1051\INTERVAL1051.json').read_text())['rows']
for d in [3,4]:
 for e in [Fraction(1,100),Fraction(1,1000)]:
  th=Fraction(99,100);lam=-Fraction(1,d*d-1);a=d-1;q=a+e*e;ci=th*th*e*e*a/(q*q)
  ei,hi,lo,ti,di=plane(d,th,e);eo,ho,lowo,to,do=plane(d,lam*th,e)
  ratio=iv(lam*lam)*eo/ei;bench=iv(Fraction(1,d*d-1));gap=ratio-bench;din=4*iv(ci)*ei;dout=4*iv(lam*lam*ci)*eo
  assert gap.l>0 and din.l>0 and dout.l>0
  # The exact smallest ambient eigenvalue is attained on off-Schmidt coordinates with R label0.
  emin=(1-th)*e*e/(d*q);condition=hi/iv(emin);distance=2*iv(th*e/q)*I.q(a).sqrt();sld=iv(4*ci/ti)
  ref=next(x for x in source if x['d']==d and x['e']==str(e));contained={}
  for key,value in [('ratio',ratio),('gap',gap),('input',din)]:
   l,h=map(binary,ref['exact_binary_endpoints'][key]);contained[key]=l<=Fraction(value.l,S)<=Fraction(value.h,S)<=h
  assert all(contained.values())
  rows.append({'d':d,'e':str(e),'theta':str(th),'lambda':str(lam),'phase':'pi','actual_order':str(1+(d*d-1)*th),'input':saved(din),'output':saved(dout),'ratio':saved(ratio),'gap':saved(gap),'benchmark':saved(bench),'input_BKM_metric':saved(din/2),'input_SLD_QFI':saved(sld),'input_trace_distance_phase_pi':saved(distance),'input_condition_number':saved(condition),'exact_min_input_eigenvalue':str(emin),'rational_plane_determinants':[str(di),str(do)],'inside_original_binary_intervals':contained})
  print(d,str(e),saved(ratio)['decimal_display_only'],saved(condition)['decimal_display_only'],flush=True)
(P/'INTEGER_INTERVAL1054.json').write_text(json.dumps({'method':'768-bit directed integer dyadic intervals;400-term atanh log plus explicit tail; no floating-point arithmetic for endpoints','inherited_arithmetic_from_own_audit1044':True,'source_code_sha2561044':PRIORHASH,'cases':rows,'all_four_positive_gaps':True},indent=2)+'\n',encoding='utf-8')
'''
code=code.replace('PRIORHASH',repr(hashlib.sha256(prior.read_bytes()).hexdigest()))
(P/'integer_intervals1054.py').write_text(prefix+code,encoding='utf-8')
print('Generated self-contained interval checker, reusing own1044 integer primitives.')

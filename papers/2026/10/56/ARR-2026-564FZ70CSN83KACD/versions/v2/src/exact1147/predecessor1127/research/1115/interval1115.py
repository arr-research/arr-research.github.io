from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,hashlib,traceback
P=Path(__file__).parent;source=Path(r'C:\Trabajo\airr\2026-10-27_binary1077-audit\integer_arithmetic1077.py');raw=source.read_bytes()
(P/'integer_arithmetic1115.py').write_text(raw.decode().replace('BITS=1024','BITS=2048').replace('N=600','N=1200'),encoding='utf-8')
sp=importlib.util.spec_from_file_location('iv1115',P/'integer_arithmetic1115.py');lib=importlib.util.module_from_spec(sp);sp.loader.exec_module(lib)
iv,log,sv,S=lib.iv,lib.log,lib.saved,lib.S
def plane(a,b,c2):
 tr=a+b;det=a*b-c2;assert det>0
 g=iv(tr*tr-4*det).sqrt();h=(iv(tr)+g)/2;l=iv(det)/h
 return h,l,g,(log(h)-log(l))/g
def kl(p,q):return p*log(p/q)+(1-p)*log((1-p)/(1-q))
def inside(v,o):
 sh=lib.BITS-o['denominator_power_of_2'];return (int(o['lo_integer'])<<sh)<=v.l<=v.h<=(int(o['hi_integer'])<<sh)
def sign(v):return 'positive' if v.l>0 else 'negative' if v.h<0 else 'unresolved'
old=json.loads((P/'replay1110'/'CONTROL1110.json').read_text());original={(r['n'],r['k']):r for r in old['cases']}
cases=list(original)+[(3,k) for k in [3,4,5,6,7,768]]+[(4,4),(10,10),(32,32),(100,100),(300,300)]
rows=[]
try:
 for n,k in cases:
  b=F(1,4*n*k);delta=F(1,2**k);eps=b*delta;a=F(1,n)-(n-2)*eps-b;c2=a*b*(1-delta);lam=-F(1,n-1)
  ap=(a+n*(n-2)*eps)/(n-1)**2;ep=(n*a+(n*n-3*n+1)*eps)/(n-1)**2
  hi,li,gi,ei=plane(a,b,c2);ho,lo,go,eo=plane(ap,b,lam*lam*c2)
  assert li.h<iv(eps).l<hi.l and lo.h<iv(eps).l and ho.h<iv(ep).l
  din=4*n*iv(c2)*ei;dout=4*n*iv(lam*lam*c2)*eo;q=n*lo;p=q+4*n*iv(lam*lam*c2)/go;dm=kl(p,q);rev=kl(q,p);ret=dm/din;qr=dout/din;gap=ret-iv(F(1,n-1))
  assert 0<q.l<q.h<p.l<p.h<S and (dout-dm).l>0 and (din-dout).l>0
  row=dict(n=n,k=k,input_D=sv(din),output_D=sv(dout),binary_D=sv(dm),measured_retention=sv(ret),quantum_retention=sv(qr),ordinary_gap=sv(gap),sign=sign(gap),q=sv(q),p=sv(p),normalized_input=sv(din/log(iv(2))),normalized_output=sv(dout/log(iv(2))),normalized_binary=sv(dm/log(iv(2))),normalized_condition=sv((hi/li)/(4*k*2**k)),normalized_TV=sv(2*n*iv(c2).sqrt()*iv(k).sqrt()),normalized_p=sv(k*p),normalized_q=sv(4*k*2**k*q),wrong_orientation_retention=sv(rev/din),reference_condition=str(F(4*k-1,n-1)),limit_flag_measurement_pq=str(n*b),limit_flag_divergence='0',output_condition=sv(iv(ep)/lo),same_n_as_k=(n==k))
  if (n,k) in original:
   orig=original[n,k];row['original_containment']=all(inside(v,orig[key]) for v,key in [(din,'input_Umegaki'),(dout,'output_Umegaki'),(dm,'binary_D'),(ret,'measured_retention')]);assert row['original_containment']
  rows.append(row)
 out=dict(method='2048bit directedinteger intervals,1200terms inherited1077; not an independent primitiveimplementation.',source_sha256=hashlib.sha256(raw).hexdigest(),cases=rows,original_containment_count=len(original),new_case_count=len(cases)-len(original))
 (P/'INTERVAL1115.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'cases':len(rows),'negative':[(r['n'],r['k']) for r in rows if r['sign']=='negative'],'all_original_contained':True}))
except Exception as e:
 (P/'INTERVAL_FAILURE1115.json').write_text(json.dumps(dict(error=repr(e),traceback=traceback.format_exc(),completed=rows),indent=2)+'\n');raise

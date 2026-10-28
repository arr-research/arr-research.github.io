from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,hashlib,traceback
P=Path(__file__).parent;src=Path(r'C:\Trabajo\airr\2026-10-27_binary1077-audit\integer_arithmetic1077.py')
raw=src.read_bytes();(P/'integer_arithmetic1136.py').write_bytes(raw)
spec=importlib.util.spec_from_file_location('integers1136',P/'integer_arithmetic1136.py');lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)
iv,log,sv=lib.iv,lib.log,lib.saved
def kl(p,q):return p*log(p/q)+(1-p)*log((1-p)/(1-q))
cases=[(2,2),(2,64),(3,3),(3,64),(3,128),(4,128),(5,256),(16,16),(16,256)];rows=[]
try:
 for n,k in cases:
  b=F(1,4*n*k);d=F(1,2**k);e=b*d;a=F(1,n)-(n-2)*e-b;c2=a*b*(1-d)
  B=c2*(n-1)**2/(a-e)**2
  qL=n*b*d/(1+B);qU=n*b*d;pL=qL+4*n*b*(1-d)/(1+B);pU=qU+4*n*b
  assert 0<qL<=qU<pL<=pU<1
  lo=kl(iv(pL),iv(qU));hi=kl(iv(pU),iv(qL))
  tr=a+b;det=a*b*d;gap=iv(tr*tr-4*det).sqrt();h=(iv(tr)+gap)/2;l=iv(det)/h
  din=4*n*iv(c2)*(log(h)-log(l))/gap;lowerret=lo/din
  row={'n':n,'k':k,'C_bound':str(B),'q_lower':str(qL),'q_upper':str(qU),'p_lower':str(pL),'p_upper':str(pU),'Dinput':sv(din),'binary_D_lower_enclosure':sv(lo),'binary_D_upper_enclosure':sv(hi),'retention_lower_enclosure':sv(lowerret),'bound_may_be_loose':True}
  if n==3:
   g=lowerret-iv(F(3,4));row['gap_over_asymmetric3_classical_Dobrushin_upper']=sv(g);row['certified_separation']=g.l>0
  rows.append(row)
 (P/'INTERVAL1136.json').write_text(json.dumps({'method':'Inherited1077 exactinteger directed1024bits/600terms, unchanged primitive; rational p/q bounds from own Schur proof, not numerically inferred eigenvalues','library_sha256':hashlib.sha256(raw).hexdigest(),'cases':rows},indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'cases':len(rows),'certified_asymmetric3_separation':[(r['n'],r['k']) for r in rows if r.get('certified_separation')],'lowerretentions':[(r['n'],r['k'],r['retention_lower_enclosure']['decimal_display_only'][0][:18]) for r in rows]}))
except Exception as e:
 (P/'INTERVAL_FAILURE1136.json').write_text(json.dumps({'exception':repr(e),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n');raise

from pathlib import Path
from fractions import Fraction as F
import json, importlib.util, hashlib, traceback
C=Path(__file__).parent
spec=importlib.util.spec_from_file_location('own_integer1077',C/'integer_arithmetic1077.py');lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)
iv,saved,S=lib.iv,lib.saved,lib.S
source=Path('C:/Trabajo/airr/2026-10-28_support1148-review/replay/predecessor-replay/1096/CONTROL1096.json')
original=json.loads(source.read_text())
cases=[dict(r,family='original1096') for r in original['rational_finite_cases']]
cases += [dict(n=3,xi='1/100',t='1/1000',noise='1/2',family='additional_predeclared'),dict(n=3,xi='1/100',t='1/1000',noise='-1/2',family='additional_predeclared')]
def ell(a,b,c2):
 tr=a+b;det=a*b-c2;assert det>0
 gap=iv(tr*tr-4*det).sqrt();hi=(iv(tr)+gap)/2;lo=iv(det)/hi
 return (lib.log(hi)-lib.log(lo))/gap
rows=[]
try:
 for r in cases:
  n=r['n'];xi=F(r['xi']);t=F(r['t']);lam=F(r['noise'])
  a=(1-xi)/n+xi/n**2;b=xi/n**2;ap=(1-xi)*(1+(n-2)*lam)/(n*(n-1))+xi/n**2;c2=t*t*(n-1)
  ei=ell(a,b,c2);eo=ell(ap,b,lam*lam*c2)
  din=4*n*iv(c2)*ei;dout=4*n*iv(lam*lam*c2)*eo;ratio=dout/din
  ordinary=F(n)*lam*lam/(2+(n-2)*lam);upper=F(n-1)*lam*lam/(1+(n-2)*lam)
  gap=ratio-iv(ordinary);upper_gap=iv(upper)-ratio
  assert din.l>0 and dout.l>0 and upper_gap.l>0
  sign='positive' if gap.l>0 else ('negative' if gap.h<0 else 'unresolved')
  assert sign!='unresolved'
  if r['family']=='original1096':
   ref=next(x for x in original['finite_Umegaki_diagnostics'] if all(str(x[k])==str(r[k]) for k in ['n','xi','t','noise']))
   center=F(ref['Umegaki_ratio']);tol=F(1,10**75)
   assert center-tol<=F(ratio.l,S)<=F(ratio.h,S)<=center+tol
  rows.append(dict(family=r['family'],n=n,xi=str(xi),t=str(t),noise=str(lam),Umegaki_input=saved(din),Umegaki_output=saved(dout),retention=saved(ratio),ordinary=str(ordinary),gap=saved(gap),sign=sign,harmonic_upper=str(upper),strict_upper_gap=saved(upper_gap),full_pair_faithful='exact active determinant positive and inactive diagonal positive',block_complement_included=True))
 assert sum(r['family']=='original1096' and r['sign']=='negative' for r in rows)==3
 out={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'method':'1024-bit integer directed intervals; square-root integer brackets; log600term atanh series plus explicit remainder, inherited1077 primitives. No floats establish any sign.','scope':'All8 original finite1096 pairs retained including3 negative gaps;2 extra cases declared in script before evaluation; no manuscript assessment, independent implementation claim or formal verification.','cases':rows}
 (C/'CERTIFICATES1099.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'cases':len(rows),'original_negative_preserved':3,'additional_positive':sum(r['family']=='additional_predeclared' and r['sign']=='positive' for r in rows)}))
except Exception as e:
 (C/'FAILURE1099.json').write_text(json.dumps({'error':repr(e),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise

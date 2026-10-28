from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,hashlib,traceback
P=Path(__file__).parent
src=Path(r'C:\Trabajo\airr\2026-10-27_binary1077-audit\integer_arithmetic1077.py')
raw=src.read_bytes();code=raw.decode().replace('BITS=1024','BITS=1152').replace('N=600','N=700')
(P/'integer_arithmetic1100.py').write_text(code,encoding='utf-8')
sp=importlib.util.spec_from_file_location('iv1100',P/'integer_arithmetic1100.py');lib=importlib.util.module_from_spec(sp);sp.loader.exec_module(lib)
iv,log,saved,S=lib.iv,lib.log,lib.saved,lib.S
def spec(a,b,c2):
 det=a*b-c2;assert det>0
 tr=a+b;g=iv(tr*tr-4*det).sqrt();h=(iv(tr)+g)/2;l=iv(det)/h
 return h,l,g,(log(h)-log(l))/g
def kl(p,q):return p*log(p/q)+(1-p)*log((1-p)/(1-q))
def sign(x):return 'positive' if x.l>0 else 'negative' if x.h<0 else 'unresolved'
def inner(x,old):
 sh=lib.BITS-int(old['denominator_power_of_2']);return (int(old['lo_integer'])<<sh)<=x.l<=x.h<=(int(old['hi_integer'])<<sh)
rows=[];extras=[];ud=[]
try:
 old=json.loads((P/'replay1101'/'MEASUREMENT1101.json').read_text())
 cases=[(r['n'],F(r['z']),'original',None,None,r) for r in old['cases']]
 # Parameters fixed before evaluation. Rational half exponent uses square n.
 cases += [(n,F(1,2),'fixed_z_half',None,None,None) for n in [4,16,256,65536]]
 cases += [(n,F(1),'fixed_z_one',None,None,None) for n in [3,16,256,65536]]
 cases += [(n,F(4),'epsilon_n6',F(1,n**6),None,None) for n in [10,100,10000,1000000]]
 cases += [(n,F(4),'epsilon_equals_beta',F(1,n**5),None,None) for n in [10,100,10000,1000000]]
 cases += [(n,None,'moving_z_delta_half',F(1,2*n**4),F(1,2),None) for n in [10,100,10000,1000000]]
 for n,z,kind,eps_override,delta_override,prior in cases:
  if delta_override is not None:delta=delta_override
  elif z.denominator==1:delta=F(1,n**int(z))
  else:
   root=lib.isqrt(n);assert root*root==n and z==F(1,2);delta=F(1,root)
  beta=F(1,n**5);eps=eps_override if eps_override is not None else delta/n**4
  a=F(1,n)-(n-2)*eps-beta;c2=a*beta*(1-delta);lam=-F(1,n-1)
  ap=(a+n*(n-2)*eps)/(n-1)**2;ep=(n*a+(n*n-3*n+1)*eps)/(n-1)**2
  hi,li,gi,ei=spec(a,beta,c2);ho,lo,go,eo=spec(ap,beta,lam*lam*c2)
  assert a>eps>0 and li.h<iv(eps).l and lo.h<iv(ep).l
  din=4*n*iv(c2)*ei;dout=4*n*iv(lam*lam*c2)*eo
  q=n*lo;p=q+4*n*iv(lam*lam*c2)/go
  assert 0<q.l<q.h<p.l<p.h<S
  db=kl(p,q);rev=kl(q,p);ret=db/din;qr=dout/din;gap=ret-iv(F(1,n-1))
  assert db.l>0 and (dout-db).l>0 and (din-dout).l>0
  row=dict(n=n,z=str(z),family=kind,epsilon=str(eps),beta=str(beta),delta=str(delta),input_Umegaki=saved(din),output_Umegaki=saved(dout),binary_D=saved(db),measured_retention=saved(ret),quantum_retention=saved(qr),gap=saved(gap),gap_sign=sign(gap),p=saved(p),q=saved(q),reverse_binary_over_forward=saved(rev/db),input_condition=saved(hi/li),output_condition=saved(iv(ep)/lo),epsilon_over_beta=str(eps/beta))
  if prior:
   row['contained_in_original_intervals']=all(inner(x,prior[k]) for x,k in [(din,'input_Umegaki'),(dout,'output_Umegaki'),(db,'binary_D'),(ret,'measured_retention')]);assert row['contained_in_original_intervals'];rows.append(row)
  else:
   if kind=='moving_z_delta_half':
    moving_formula=log(iv(2))/(4*log(iv(n))+log(iv(2)))
    row['retention_over_inapplicable_fixed_z_formula']=saved(ret/moving_formula)
   extras.append(row)
 oldud=json.loads((P/'replay1099'/'CERTIFICATES1099.json').read_text())
 for r in oldud['cases']:
  n=r['n'];xi=F(r['xi']);t=F(r['t']);lam=F(r['noise']);a=(1-xi)/n+xi/n**2;b=xi/n**2;ap=(1-xi)*(1+(n-2)*lam)/(n*(n-1))+b;c2=t*t*(n-1)
  ei=spec(a,b,c2)[3];eo=spec(ap,b,lam*lam*c2)[3];din=4*n*iv(c2)*ei;dout=4*n*iv(lam*lam*c2)*eo;ret=dout/din;gap=ret-iv(F(r['ordinary']))
  assert inner(ret,r['retention']) and sign(gap)==r['sign']
  ud.append(dict(n=n,xi=str(xi),t=str(t),noise=str(lam),family=r['family'],retention=saved(ret),gap=saved(gap),sign=sign(gap),contained_in_original=True))
 out=dict(method='Own recomputation, inherited1077 integer arithmetic upgraded to1152bits/700terms; not an independent arithmetic implementation. No floating point establishes signs.',source_library_sha256=hashlib.sha256(raw).hexdigest(),source_library=str(src),original1101=rows,adversarial=extras,original1099=ud)
 (P/'INTERVAL1100.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'original1101':len(rows),'original1099':len(ud),'adversarial':len(extras),'negative_adversarial':[(r['n'],r['family']) for r in extras if r['gap_sign']=='negative'],'original_negative':sum(r['sign']=='negative' for r in ud)}))
except Exception as e:
 (P/'INTERVAL_FAILURE1100.json').write_text(json.dumps(dict(error=repr(e),traceback=traceback.format_exc(),original1101=rows,adversarial=extras,original1099=ud),indent=2)+'\n',encoding='utf-8');raise

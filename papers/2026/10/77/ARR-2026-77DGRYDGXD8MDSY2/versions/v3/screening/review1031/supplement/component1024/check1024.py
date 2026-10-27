from pathlib import Path
import sympy as s,json,hashlib,shutil
P=Path(__file__).parent;Dout=Path(r'D:\Proyectos\airr-investigacion')/P.name
rows=[]
for d,K,kappa in [(2,s.Rational(199,100),s.Integer(2)),(3,s.Rational(449,100),s.Rational(9,2)),(4,s.Rational(799,100),s.Integer(8))]:
 n=d*d;a=K/n;b=(1-2*a)/(n-2);t=s.Rational(1,10**8)
 v=s.zeros(n,1);w=s.zeros(n,1)
 for i in range(d):v[i*d+i]=1;w[i*d+(i+1)%d]=1
 P0=v*v.T/d;P1=w*w.T/d;sig=b*s.eye(n)+(a-b)*(P0+P1);D=P0-P1;rho=sig+t*D
 ptr=lambda x:s.Matrix(d,d,lambda i,j:sum(x[h*d+i,h*d+j] for h in range(d)))
 assert ptr(sig)==s.eye(d)/d and ptr(D)==s.zeros(d)
 assert sig*D==a*D and a>b>0 and abs(t)<min(a,b,(kappa-K)/n)
 assert sig*rho==rho*sig
 if d==2:
  pt=lambda x:s.Matrix(n,n,lambda i,j:x[d*(j//d)+i%d,d*(i//d)+j%d])
  for x in [sig,rho]:assert all(pt(x)[:i,:i].det()>0 for i in range(1,n+1))
 for l in [-s.Rational(1,n-1),s.Rational(1,2)]:
  al=l*a+(1-l)/n;ratio=l*l*a/al;upper=l*l*kappa/(1+l*(kappa-1));assert ratio<=upper
  # Exact finite triangular Petz from the two commuting changed eigenvalues.
  tin=t*t/(2*a+t)+t*t/(2*a-t)
  tout=(l*t)**2/(2*al+l*t)+(l*t)**2/(2*al-l*t)
  assert tout/tin<=upper
  rows.append(dict(d=d,K=str(K),kappa=str(kappa),lambda_=str(l),local=str(ratio),triangular_finite=str(s.factor(tout/tin)),upper=str(upper),PPT_both_if_d2=d==2,passed=True))
out=dict(scope='6 exactBell controls nearcapd²/2; all-f assertion rests on analyticTaylorlimit, not sampling; no grade',rows=rows,all_passed=True)
(P/'CHECK1024.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
(P/'MANIFEST1024.json').write_text(json.dumps(dict(scope='Parent Bell synthesis from983/1018, pendingtechnicalreview',files=[dict(path=f.name,bytes=f.stat().st_size,sha256=sha(f)) for f in sorted(P.iterdir()) if f.is_file() and f.name!='MANIFEST1024.json']),indent=2)+'\n',encoding='utf-8')
Dout.mkdir(exist_ok=True)
for f in P.iterdir():
 if f.is_file():
  q=Dout/f.name
  if q.exists():assert sha(q)==sha(f)
  else:shutil.copyfile(f,q)
print(json.dumps(dict(cases=6,passed=True,manifest_sha256=sha(P/'MANIFEST1024.json'))))

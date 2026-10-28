from pathlib import Path
import sympy as s, mpmath as mp, json
C=Path(__file__).parent;Q=s.Rational
n,l=s.symbols('n l',positive=True)
w0=(1+(n-1)*l)/n;w=(1-l)/n
H=(n-1)*l*l/(1+(n-2)*l);B=n*l*l/(2+(n-2)*l)
assert s.factor(1-n*n/(1/w0+(n-1)/w)-H)==0
assert s.factor(H/B-(n-1)*(2+(n-2)*l)/(n*(1+(n-2)*l)))==0
rows=[];finite_ud=[];mp.mp.dps=100
def mpq(v):return mp.mpf(int(v.p))/int(v.q)
def ell_block(a,b,c2):
 gap=mp.sqrt((a-b)**2+4*c2);hi=(a+b+gap)/2;lo=(a*b-c2)/hi
 return mp.log(hi/lo)/gap
for n,xi,t in [(3,Q(1,100),Q(1,100)),(3,Q(1,1000),Q(1,1000)),(4,Q(1,10),Q(1,100)),(5,Q(1,10),Q(1,100))]:
 I=s.eye(n);u=s.ones(n,1);P=I-u*u.T/n
 vs=[I[:,i]-u/n for i in range(n)]
 S=[(1-xi)*v*v.T/(n-1)+xi*I/n**2 for v in vs]
 D=[u*v.T+v*u.T for v in vs]
 r=sum(S,s.zeros(n));assert r==(1-xi)*P/(n-1)+xi*I/n
 assert sum(D,s.zeros(n))==s.zeros(n)
 assert sum([v*v.T for v in vs],s.zeros(n))==P
 rho=[a+t*z for a,z in zip(S,D)];sigma=[a-t*z for a,z in zip(S,D)]
 assert all(all(m[:j,:j].det()>0 for j in range(1,n+1)) for m in rho+sigma)
 def triangle(a,b):
  z=a-b;vec=s.Matrix([z[i,j] for j in range(n) for i in range(n)])
  F=s.kronecker_product(I,a)+s.kronecker_product(b.T,I)
  return s.factor((vec.T*F.inv()*vec)[0])
 input_=sum(triangle(a,b) for a,b in zip(rho,sigma))
 alpha=(1-xi)/n+xi/n**2;beta=xi/n**2
 assert s.factor(input_-8*n*(n-1)*t*t/(alpha+beta))==0
 for lam in [Q(1,2),-Q(1,n-1)]:
  ro=[lam*a+(1-lam)*r/n for a in rho];so=[lam*a+(1-lam)*r/n for a in sigma]
  assert all(all(m[:j,:j].det()>0 for j in range(1,n+1)) for m in ro+so)
  output=sum(triangle(a,b) for a,b in zip(ro,so));actual=s.factor(output/input_)
  ap=(1-xi)*(1+(n-2)*lam)/(n*(n-1))+xi/n**2
  predicted=s.factor(lam**2*(alpha+beta)/(ap+beta));assert actual==predicted
  ordinary=n*lam**2/(2+(n-2)*lam);upper=(n-1)*lam**2/(1+(n-2)*lam)
  assert 0<actual<=upper
  rows.append(dict(n=n,xi=str(xi),t=str(t),noise=str(lam),input_triangle=str(input_),output_triangle=str(output),ratio_exact=str(actual),ordinary=str(ordinary),gap_to_ordinary=str(actual-ordinary),harmonic_upper=str(upper),input_and_output_faithful_exact=True,full_ambient_reference=True))
  c2=mpq(t*t*(n-1));li=ell_block(mpq(alpha),mpq(beta),c2);lo=ell_block(mpq(ap),mpq(beta),mpq(lam**2)*c2)
  uratio=mpq(lam**2)*lo/li;assert 0<uratio<=mpq(upper)+mp.mpf('1e-90')
  finite_ud.append(dict(n=n,xi=str(xi),t=str(t),noise=str(lam),Umegaki_input=mp.nstr(4*n*c2*li,80),Umegaki_ratio=mp.nstr(uratio,80),ordinary=str(ordinary),gap_to_ordinary=mp.nstr(uratio-mpq(ordinary),80),scope='100-digit direct finite2x2-block logarithm diagnostic, not interval certificate; same declared pairs as exact triangular controls'))
asymptotic=[]
for n in [3,4,8]:
 for lam in [mp.mpf('0.5'),-mp.mpf(1)/(n-1)]:
  for power in [4,12,40]:
   xi=mp.power(10,-power);a=(1-xi)/n+xi/n**2;b=xi/n**2;ap=(1-xi)*(1+(n-2)*lam)/(n*(n-1))+xi/n**2
   ell=lambda x,y:(mp.log(x)-mp.log(y))/(x-y)
   ratio=lam**2*ell(ap,b)/ell(a,b)
   target=(n-1)*lam**2/(1+(n-2)*lam)
   assert ratio<=target+mp.mpf('1e-90')
   asymptotic.append(dict(n=n,noise=mp.nstr(lam,80),xi_power=power,BKM_ratio=mp.nstr(ratio,80),target=mp.nstr(target,80),scope='100-digit numerical diagnostic, not interval certificate'))
out={'symbolic_harmonic_identity':True,'rational_finite_cases':rows,'BKM_diagnostics':asymptotic,'finite_Umegaki_diagnostics':finite_ud,'scope':'Root-derived candidate;8 direct finite triangular rational controls,18 BKM numerical diagnostics and8 finite Umegaki diagnostics; not external audit, full manuscript assessment, formal verification or priority certificate. All declared cases retained, including weak/nonseparating finite gaps.'}
(C/'CONTROL1096.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'finite_cases':len(rows),'BKM_diagnostics':len(asymptotic),'finite_positive_gaps':sum(bool(Q(x['gap_to_ordinary'])>0) for x in rows),'finite_Umegaki_positive':sum(mp.mpf(x['gap_to_ordinary'])>0 for x in finite_ud),'finite_Umegaki_nonseparating':sum(mp.mpf(x['gap_to_ordinary'])<=0 for x in finite_ud)}))

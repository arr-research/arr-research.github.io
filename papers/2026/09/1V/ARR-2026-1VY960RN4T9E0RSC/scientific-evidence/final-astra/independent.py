import sympy as s, mpmath as mp, json
from pathlib import Path
mp.mp.dps=100
m,mu,c,k=s.symbols('m mu c k',positive=True)
psi=(c+1)*(m-mu)/(m*(1-m)); G=k/(c*mu-c*m+k*m*(1-m))
delta=s.factor(s.diff(psi,m)-G.subs(k,psi))
assert s.factor(delta-(c+1)*(m-mu)*(2*m-1)/(m*(1-m))**2)==0
# At a hypothetical zero at m=1/2, D'=0 and hence D''=Delta'.
d2=s.factor(s.diff(delta,m).subs(m,s.Rational(1,2)))
assert s.simplify(d2-16*(c+1)*(1-2*mu))==0
print('EXACT transversality and tangency second derivative:',d2)
# Independent quadrature from the probability density, no supplied Kummer code.
rows=[]
for aa,cc,kk in [('0.5','1.5','2.178287975'),('1','3','3.232708836'),('2','6','5.277112966'),('1','2','3'),('0.25','1','2.8008995')]:
 a,c,k=map(mp.mpf,(aa,cc,kk)); mu=a/c
 J=[mp.quad(lambda x: x**(a-1+j)*(1-x)**(c-a-1)*mp.exp(k*x),[0,mp.mpf('.5'),1]) for j in range(3)]
 M=J[0]/mp.beta(a,c-a); m=J[1]/J[0]; v=J[2]/J[0]-m*m; H=m-mu-k*v
 Mh=mp.hyp1f1(a,c,k); mh=a/c*mp.hyp1f1(a+1,c+1,k)/Mh
 err=max(abs(M/Mh-1),abs(m-mh)); print(aa,cc,str(err),flush=True); assert err<mp.mpf('1e-14')
 assert abs(H)<mp.mpf('3e-8') if c>2*a else H>0
 rows.append(dict(a=aa,c=cc,k=kk,H=str(H),quadrature_relative_error=str(err)))
print(json.dumps(rows,indent=2)); print('PASS independent exact identities and five quadrature cases')

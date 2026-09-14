from mpmath import mp
from datetime import datetime,timezone
mp.dps=60
print('UTC',datetime.now(timezone.utc).isoformat())
for q in [2,3,4,5,10,30]:
 def L(k): return q*mp.quad(lambda x: mp.cosh(k*x)*(1-x)**(q-1),[0,1])
 def H(k):
  a=L(k); b=q*mp.quad(lambda x:x*mp.sinh(k*x)*(1-x)**(q-1),[0,1]); d=q*mp.quad(lambda x:x*x*mp.cosh(k*x)*(1-x)**(q-1),[0,1]); return b/a-k*(d/a-(b/a)**2)
 if q>=4:
  kl=mp.findroot(lambda k:L(k)-mp.mpf(q*(q-1))/8,(mp.mpf('0.01'),3*q),solver='bisect',maxsteps=250); kf=mp.findroot(H,(mp.mpf('1.2')*q,mp.mpf('2.2')*q)); assert kf>kl and mp.diff(H,kf)>0
  print(q,'kL',mp.nstr(kl,20),'kf',mp.nstr(kf,20),'Hprime',mp.nstr(mp.diff(H,kf),12))
 else:
  vals=[H(mp.mpf(x)) for x in ['0.01','0.1','1','3','10','30']]; assert min(vals)>0; print(q,'positive quadrature H at six points')
print('PASS: quadrature independent of supplied series/state implementation')


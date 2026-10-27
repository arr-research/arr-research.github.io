from pathlib import Path
import mpmath as mp,json
P=Path(__file__).parent;mp.mp.dps=90
fs={'triangular':lambda x:(x-1)**2/(x+1),'Umegaki':lambda x:x*mp.log(x),'reverse_Umegaki':lambda x:-mp.log(x),'quadratic':lambda x:(x-1)**2,'Hellinger':lambda x:(mp.sqrt(x)-1)**2,'resolvent7':lambda x:(x-1)**2/(x+7)}
rows=[]
for d in [2,3,4,5]:
 n=d*d;K=mp.mpf(n)/2-mp.mpf('0.01');a=K/n;b=(1-2*a)/(n-2);t=mp.mpf('1e-20')
 assert t<min(a,b,mp.mpf('0.01')/n)
 for l in [-mp.mpf(1)/(n-1),mp.mpf('.5')]:
  al=l*a+(1-l)/n;C=l*l*a/al
  for name,f in fs.items():
   di=a*(f(1+t/a)+f(1-t/a));do=al*(f(1+l*t/al)+f(1-l*t/al));ratio=do/di
   assert abs(ratio-C)<mp.mpf('1e-35')
   rows.append({'d':d,'K':str(K),'lambda':str(l),'f':name,'ratio':str(ratio),'limit':str(C),'difference':str(ratio-C)})
# This diagnostic concerns THIS rank-two tangent, not the optimal BKM coefficient.
def BKM(d,e,p):
 m=d-1;q=1+m*e*e;W=mp.matrix([[1+(d-1)*p,d*p*e*mp.sqrt(m)],[d*p*e*mp.sqrt(m),(2+(d*m-2)*p)*e*e]])/(2*d*q);T=mp.matrix([[0,mp.sqrt(m)],[mp.sqrt(m),2*e*m]])
 vs,U=mp.eigsy(W);Z=U.T*T*U;g=mp.mpf(0)
 for i in range(2):
  for j in range(2):g+=Z[i,j]**2*(1/vs[i] if i==j else (mp.log(vs[i])-mp.log(vs[j]))/(vs[i]-vs[j]))
 return g
diag=[];d=3;th=mp.mpf('0.79');l=mp.mpf('.5');L=d*(d+1)/2;lim=l*l*(1+(d-1)*th)/(1+(d-1)*l*th);sldlim=l*l*(1+(L-1)*th)/(1+(L-1)*l*th)
for estr in ['.1','.001','1e-8','1e-20','1e-35']:
 e=mp.mpf(estr);ratio=l*l*BKM(d,e,l*th)/BKM(d,e,th);diag.append({'e':estr,'BKM_this_tangent':str(ratio),'fixed_p_BKM_limit':str(lim),'SLD_limit':str(sldlim)})
out={'precision_decimal_digits':90,'Bell_Taylor_samples':rows,'ranktwo_BKM_diagnostic':diag,'scope':'Bounded high-precision diagnostics. BKM values concern a chosen tangent and do not upper-bound the complete BKM optimum.'}
(P/'LIMITS1025.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'Bell_cases':len(rows),'BKM_last':diag[-1],'all_passed':True}))

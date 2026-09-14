from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,datetime
from mpmath import mp
mp.dps=100
print('UTC',datetime.datetime.now(datetime.timezone.utc).isoformat())
def jac(n,a,t): return sum(F(comb(n+a,j)*comb(n,n-j))* (t-1)**(n-j)*t**j for j in range(n+1))
for d,K,expected,kmin in [(4,10,F(22018975,7340032),6),(3,13,F(77,45),4)]:
 vals={k:F(d*d,d+1)*(1+d*jac(k,d-2,F(1,d*d))/comb(k+d-2,k)) for k in range(2,K+1)}
 assert min(vals,key=vals.get)==kmin and vals[kmin]==expected
 tail=F(1)/(1-F(1,d*d))**(d-2)/comb(K+1+d-2,K+1)
 assert F(d*d,d+1)*(1-d*tail)>expected
 print('independent binomial exact d',d,'minimum',expected,'degree',kmin,'tail strict PASS')
spec=json.loads((Path(__file__).parent/'s6_refined_B_exact_den100000000.json').read_text()); ns=[[F(x) for x in n] for n in spec['n123']]; w=[F(x) for x in spec['w']]; s=[sum(n[j] for n in ns) for j in range(3)]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
assert all(dot(n,n)==1 for n in ns) and dot(s,w)==0
q=(1-dot(s,s)/4)/dot(w,w);assert q>0
conv=lambda x:mp.mpf(x.numerator)/x.denominator
n=[[conv(x) for x in n] for n in ns]+[[conv(-s[j]/2)+sign*mp.sqrt(conv(q))*conv(w[j]) for j in range(3)] for sign in [1,-1]]
assert max(abs(dot(v,v)-1) for v in n)<mp.mpf('1e-95')
ts=[mp.mpf(2)/9*(1+dot(n[i],n[j])) for i in range(5) for j in range(i+1,5)]
for k in [4,8,9,12,16]:
 ps=[sum(mp.mpf(comb(k+1,j)*comb(k,k-j))*(t-1)**(k-j)*t**j for j in range(k+1))/(k+1) for t in ts]
 g=mp.mpf(9)/25*(5+2*sum(ps));print('binomial 100dps k',k,'g',mp.nstr(g,60));assert g>mp.mpf('1.776009937964733')
print('PASS independently constructed feasibility and active-degree spectrum; no supplied recurrence imported')

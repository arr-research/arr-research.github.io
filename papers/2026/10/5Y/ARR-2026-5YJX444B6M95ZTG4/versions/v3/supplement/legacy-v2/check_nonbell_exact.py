from pathlib import Path
from fractions import Fraction as Q
import json
import mpmath as mp
ROOT=Path(__file__).resolve().parent

# Exact algebra at the Bell input.
a,b,k,x,p=Q(1,10),Q(3,10),Q(3,5),Q(1,10),Q(1,2)
t=a+k*p;L=p*(1-p)/(t*(1-t));ap=p*b/(1-t);bp=(1-p)*a/t;kp=L*k;xp=L*x
assert [ap,bp,kp,xp,xp-kp*kp]==[Q(1,4),Q(1,8),Q(5,8),Q(5,48),Q(-55,192)]
assert 2**6*3**9==1259712 and 7**7==823543 and 1259712>823543
mp.mp.dps=75
a,b,k,x=map(mp.mpf,['.1','.3','.6','.1'])
def h(p):return -p*mp.log(p)-(1-p)*mp.log(1-p)
def J(p):return h(p)+(1-p)*h(a)+p*h(b)-h(a+k*p)
def Jprime(p):return mp.log((1-p)/p)+h(b)-h(a)-k*mp.log((1-a-k*p)/(a+k*p))
p0=mp.findroot(Jprime,(mp.mpf('.5'),mp.mpf('.55')))
t0=a+k*p0;threshold=k*k*p0*(1-p0)/(t0*(1-t0))
d=Jprime(mp.mpf('.5'));d2=mp.log(mp.mpf(1259712)/823543)/10
assert abs(d-d2)<mp.mpf('1e-70') and threshold>x
result=dict(status='Exact rational identities and analytic positivity argument; high-precision numerical illustration only for optimizer/value',precision_digits=75,exact_Bell_reverse=dict(a='1/4',b='1/8',k='5/8',x='5/48',D='-55/192'),exact_derivative='ln(1259712/823543)/10 > 0',derivative=str(d),unique_maximizer=str(p0),plateau_sufficient_upper_x=str(threshold),chosen_x=str(x),G_Bell_bits=str(J(mp.mpf('.5'))/mp.log(2)),channel_cost_bits=str(J(p0)/mp.log(2)),strict_gap_bits=str((J(p0)-J(mp.mpf('.5')))/mp.log(2)),proof_notes=['J is concave as classical conditional entropy; explicitly J_second=-1/[p(1-p)]+k^2/[t(1-t)] <= 0 by total variance.','At the rational example, a,b are interior, J is strictly concave and its derivative has opposite infinite endpoint limits.','D=-55/192 at p=.5 persists strictly nearby; hence G=J in that neighborhood and positive derivative proves a strict gap without solving for p0.','The pure-output complement extension is a direct corollary of Tang support Thm4.1 applied to the Choi support and arbitrary local reference filters; reverse closure is valid but not needed.'])
(ROOT/'late-addenda-results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

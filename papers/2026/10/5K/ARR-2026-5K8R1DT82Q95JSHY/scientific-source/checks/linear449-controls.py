from fractions import Fraction as Q
from math import comb, ceil
import json

def f(n,L,z):
    return sum((Q(comb(n,j))*(-z)**j for j in range(L+1)),Q(0))

cases=[]
for n in range(3,62,2):
    m=(n+1)//2; L=m-1
    for t in (Q(1),Q(1,2),Q(2,3),Q(1,10)):
        for extra in (0,1,17):
            d=ceil(2*n/t)+extra; z=1/(d*t); a=f(n,L,t/d)
            deficit=Q(0)
            for r in range(1,L+1):
                coeff=(-1)**(n-r)*Q(d)**(1-r)*t**(n-r)*f(n-r,L-r,z)
                assert coeff*((-1)**(n-r))>0
                cover=Q(comb(n,r),comb(m,r))
                # Exact combinatorial multiplicity in the averaging proof.
                assert cover==Q(comb(n,m),comb(n-r,m-r))
                if coeff<0: deficit-=coeff*cover
            assert a-deficit>=Q(41,564),(n,d,t,a-deficit)
            assert f(n,L,t/d)>=f(n,L,z)>0
            cases.append({'n':n,'d':d,'t':str(t),'gap_lower':str(a-deficit)})

# Exact algebra used in the analytic constants, not a sampled replacement.
assert Q(1,2)+Q(3,28)-Q(1,48)==Q(197,336)>Q(7,12)
assert Q(7,12)-Q(24,47)==Q(41,564)
assert Q(1,2)/(1-Q(1,48))==Q(24,47)
print(json.dumps({'status':'PASS','cases':len(cases),'coverage':'Exact scalar and combinatorial controls only; operator result proved analytically, not tested on a full Choi matrix','minimum_sample_gap':str(min(Q(x['gap_lower']) for x in cases)),'cases_detail':cases},indent=2))

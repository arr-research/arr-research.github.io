"""Exact witness and high-precision diagnostics for the four-qubit criterion.

Author-context verification, not an independent referee or formal proof.
"""
import json
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mp
import sympy as sp

ROOT=Path(__file__).resolve().parent
mp.mp.dps=90

def h(p,alpha):
    if p==0: return mp.mpf(0)
    if p==mp.mpf('.5'): return mp.mpf(1)
    if alpha==1: return -(p*mp.log(p)+(1-p)*mp.log1p(-p))/mp.log(2)
    if alpha==mp.inf: return -mp.log1p(-p)/mp.log(2)
    return mp.log(mp.power(p,alpha)+mp.power(1-p,alpha))/((1-alpha)*mp.log(2))

# Fully exact alpha=3 midpoint certificate.
f=lambda p: 1-3*p+3*p*p
a,eps,b=Q(1,10),Q(1,20),Q(2,5)
product=f(a-eps)*f(a+eps)
exact_gap=f(a)**2-product
assert product==Q(84721,160000)
assert exact_gap==Q(543,160000)>0

# Exact reduced density matrices of each of the two four-qubit witnesses.
marginals=[]
for probabilities in [(a-eps,a+eps,b,b),(a+eps,a-eps,b,b)]:
    r=[sp.Rational(x.numerator,x.denominator) for x in probabilities]
    amps={1 << (3-i):sp.sqrt(r[i]) for i in range(4)}
    for axis in range(4):
        M=sp.zeros(2,8)
        for idx,amplitude in amps.items():
            bits=[(idx>>(3-i))&1 for i in range(4)]
            others=[bits[i] for i in range(4) if i!=axis]
            col=4*others[0]+2*others[1]+others[2]
            M[bits[axis],col]=amplitude
        rho=sp.simplify(M*M.T)
        assert rho==sp.diag(1-r[axis],r[axis])
        marginals.append([str(rho[0,0]),str(rho[1,1])])

zsmall=(h(mp.mpf(1)/20,3)+h(mp.mpf(3)/20,3))/2
zlarge=h(mp.mpf(2)/5,3)
xi=[zsmall/zlarge,zsmall/zlarge,mp.mpf(1),mp.mpf(1)]
inverse3=lambda y:(3-mp.sqrt(max(mp.mpf(0),12*mp.power(2,-2*y)-3)))/6
budget_at_mixture=sum(inverse3(z) for z in [zsmall,zsmall,zlarge,zlarge])
assert budget_at_mixture>1
lo,hi=mp.mpf(0),mp.mpf(1)
for _ in range(280):
    mid=(lo+hi)/2
    if sum(inverse3(mid*x) for x in xi)<=1:lo=mid
    else:hi=mid
assert hi<zlarge
alpha3={'exact_midpoint_product':str(product),'exact_polynomial_gap':str(exact_gap),
 'exact_marginal_checks':marginals,'xi_first':mp.nstr(xi[0],35),
 'original_log_radial_lower':mp.nstr(lo,35),'original_log_radial_upper':mp.nstr(hi,35),
 'convexified_log_radial_lower':mp.nstr(zlarge,35),
 'log_gap_lower_numeric':mp.nstr(zlarge-hi,35),
 'inverse_entropy_budget_at_convexified_witness':mp.nstr(budget_at_mixture,35),
 'scope':'Rational midpoint inequality and marginal matrices are exact; transcendental values are high-precision diagnostics, not interval certificates.'}

# Check the algebraic second-derivative identity for several integer orders.
p=sp.symbols('p',positive=True)
for order in [2,3,4,7]:
    F=p**order+(1-p)**order
    N=sp.expand((F*sp.diff(F,p,2)-sp.diff(F,p)**2)/order)
    target=-(p**(2*order-2)+(1-p)**(2*order-2))+(order-1)*(p**order*(1-p)**(order-2)+(1-p)**order*p**(order-2))+2*order*p**(order-1)*(1-p)**(order-1)
    assert sp.simplify(N-target)==0

# Positive-side concavity diagnostics, including alpha=2 exactly.
concave_cases=0
for order in ['.2','.5','.9','1','1.1','1.5','1.9','2']:
    alpha=mp.mpf(order)
    for point in ['.00001','.001','.05','.2','.4','.499']:
        second=mp.diff(lambda x:h(x,alpha),mp.mpf(point),2)
        assert second<0
        concave_cases+=1

# Counterexamples close to the threshold need arbitrarily small probabilities;
# increase precision explicitly, rather than silently rounding them to zero.
nonconcave=[]
for order in ['2.01','2.05','2.1','2.25','2.5','3','4','8','20']:
    alpha=mp.mpf(order)
    exponent=max(1,int(mp.ceil(4/(alpha-2))))
    with mp.workdps(2*exponent+90):
        alpha=mp.mpf(order)
        small=mp.power(10,-exponent)
        midpoint_gap=(h(small/2,alpha)+h(3*small/2,alpha))/2-h(small,alpha)
        assert midpoint_gap>0
        assert mp.diff(lambda x:h(x,alpha),small,2)>0
        nonconcave.append({'alpha':order,'a':'1e-'+str(exponent),
          'working_decimal_digits':2*exponent+90,
          'positive_midpoint_gap':mp.nstr(midpoint_gap,12)})

report={'status':'PASS','alpha3':alpha3,'symbolic_curvature_identities':4,
 'concavity_cases':concave_cases,'nonconcavity_cases':nonconcave,
 'scope':'Finite exact and numerical diagnostics in the authoring context. Universal criterion rests on the written proof; no novelty or significance rating is inferred.'}
(ROOT/'renyi-diagnostics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))

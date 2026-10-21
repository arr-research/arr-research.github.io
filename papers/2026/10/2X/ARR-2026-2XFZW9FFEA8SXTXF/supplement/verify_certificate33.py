"""Exact verification of the fixed degree-eight certificate and lower bounds.
No optimizer or search is used in this verifier.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sympy as s

b=Path(__file__).resolve().parent;output=b/'verification-33.json'
assert not output.exists()
x,y,t=s.symbols('x y t',real=True)
coeff=[216,-2260,12820,-45066,99726,-137242,113341,-51276,9784]
P=sum(v*x**(8-k)*y**k for k,v in enumerate(coeff))
rho=x*x+y*y;H=rho+s.Rational(3,5)*(x*x-y*y)
K=-s.Rational(3,4)*H+3*(x*x-y*y)
negative=s.expand(-s.diff(P,x)*(K*x-H*y)-s.diff(P,y)*(K*y+H*x))
expected=[2528,-28576,65016,322736,-1562236,1039608,5502688,-13799076,13740768,-6471612,1188936]
assert s.expand(5*negative-sum(v*x**(10-k)*y**k for k,v in enumerate(expected)))==0

def variation(signs):
    return sum(a!=b for a,b in zip(signs,signs[1:]))
def exact_sturm(poly):
    # Build our own signed Euclidean chain, without count_roots or sturm.
    f=s.Poly(poly,t,domain=s.QQ);chain=[f,f.diff()]
    while chain[-1].degree()>0:
        remainder=-chain[-2].rem(chain[-1])
        assert not remainder.is_zero
        # Positive normalization preserves the signs of the Sturm chain.
        denominator, primitive=remainder.clear_denoms(convert=True)
        content, primitive=primitive.primitive()
        if content<0:primitive=-primitive
        chain.append(s.Poly(primitive,t,domain=s.QQ))
    plus=[int(s.sign(f.LC())) for f in chain]
    minus=[a*(-1)**f.degree() for a,f in zip(plus,chain)]
    assert variation(minus)==variation(plus)
    assert chain[0].eval(0)>0
    return {'degrees':[f.degree() for f in chain],'minus_signs':minus,'plus_signs':plus,'variations':[variation(minus),variation(plus)]}
positive_check=exact_sturm(P.subs({x:t,y:1}))
lie_check=exact_sturm(negative.subs({x:t,y:1}))
assert P.subs({x:1,y:0})>0 and negative.subs({x:1,y:0})>0

data=json.loads((b/'degree-obstruction-33.json').read_text())
verified=[]
for record in data['records']:
    M=record['M'];variables=s.symbols('v:'+str(2*M+1),real=True)
    total=0
    for item in record['support']:
        w=s.Rational(item['weight']);assert w>0
        if item['t']=='infinity':z=s.Integer(-1)
        else:
            u=s.Rational(item['t']);z=(1+s.I*u)/(1-s.I*u)
        re=s.simplify(s.re(z))
        p=variables[0];dp=s.Integer(0)
        for k in range(1,M+1):
            zk=s.expand_complex(z**k)
            term=(variables[2*k-1]+s.I*variables[2*k])*zk
            p+=2*s.re(term);dp+=2*s.re(s.I*k*term)
        d=-M*(-s.Rational(3,4)+s.Rational(51,20)*re)*p-(1+s.Rational(3,5)*re)*dp
        evaluation=s.expand(p if item['kind']=='p' else d)
        assert [s.diff(evaluation,v) for v in variables]==[s.Rational(v) for v in item['row']]
        total+=w*evaluation
    assert s.expand(total+variables[0])==0
    verified.append({'degree':2*M,'positive_weights':len(record['support']),'exact_identity':True})
result={'at':datetime.now(timezone.utc).isoformat(),'P_sturm':positive_check,'negative_Lie_sturm':lie_check,'lower_degree_obstructions':verified,'minimum_polynomial_weak_degree':8,'certificate_strict':True,'scope':'Exact rational operations; no optimizer and no formal proof assistant. Separate implementation uses complex powers for witness rows and a signed Euclidean chain for positivity.'}
output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))

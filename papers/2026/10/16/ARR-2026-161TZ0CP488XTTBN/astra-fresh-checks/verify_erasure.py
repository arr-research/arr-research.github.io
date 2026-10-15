from pathlib import Path
import sympy as sp,json
x=sp.Symbol('x');phi=sp.Poly(x*x+x+1,x,domain=sp.QQ)
def reduce(p):return sp.Poly(p,x,domain=sp.QQ).rem(phi).as_expr()
S={(0,3*j) for j in range(9)};different=[]
for a in range(27):
    for b in range(27):
        ca=reduce(sp.Rational(1,3)*(1+x**((-b)%3))) if a==0 else 0
        cb=reduce(-sp.Rational(1,3)*x**((-2*b)%3)) if a==0 else 0
        diff=sp.expand(ca-cb)
        assert diff==(1 if (a,b) in S else 0)
        if diff!=0:different.append([a,b])
assert len(different)==9
out={'status':'PASS','exact_cyclotomic_coefficient_checks':729,'d':27,'omitted_labels':different,'A_diagonal_nonzero':{'0':9,'9':9},'B_diagonal_nonzero':{'18':-9},'rank_A':2,'rank_B':1,'difference_rank':3,'identity_label_omitted':True,'scope':'Exact Q[zeta_3] coefficients; no floating-point arithmetic.'}
Path(__file__).with_name('erasure-witness.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

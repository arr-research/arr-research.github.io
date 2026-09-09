"""New local checks for the received PDFs; not the author's missing repro code."""
from pathlib import Path
from fractions import Fraction
from math import comb
import json, platform
import sympy as s
import mpmath as mp

ROOT=Path(__file__).resolve().parent
out={'date':'2026-09-08','python':platform.python_version(),'sympy':s.__version__,'mpmath':mp.__version__,'scope':'Targeted checks, not a formal independent editorial audit'}

# Paper 1: compare every entry of U_s W and phase W_transformed U_s,
# using integer exponents modulo p (no floating point).
count=0
for p in [3,5,7,11]:
    inv2=pow(2,-1,p)
    for q in range(p):
        for a in range(p):
            for b in range(p):
                aa=-(q*a+b)%p
                phase=(-q*inv2*a*a-a*b)%p
                for j in range(p):
                    for k in range(p):
                        lhs=j*(k+a)+q*inv2*(k+a)**2+b*k
                        rhs=phase+a*(j-aa)+(j-aa)*k+q*inv2*k*k
                        assert (lhs-rhs)%p==0
                count+=1
# Multiplication by omega in Q[x]/(x^4+x^3+x^2+x+1).
W=s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
C=s.zeros(20)
for a,b,phase in [(0,0,0),(1,1,0),(2,4,2),(3,4,3),(4,1,0)]:
    for k in range(5):
        j=(k+a)%5
        C[j*4:(j+1)*4,k*4:(k+1)*4]+=W**((b*k+phase)%5)
rank=C.rank()
assert rank==12
out['paper1']={'clifford_identities_exact':count,'primes':[3,5,7,11],'parabola_regular_representation_rank':rank,'rank_over_Q_omega':rank//4,'nullity':2}
print('Paper 1: exact identities and parabola rank verified',flush=True)

# Paper 2: symbolic rational identities and the finite boundary checks.
d,M,k=s.symbols('d M k')
psi=d*(M-1)*(2*M+d-1)/(M*(M+d))
phi=lambda kk:kk/(kk*M-(d-1)*(M-1))
delta=d*(M-1)**2*(2*M-d*(d-1))/((d+1)*M**2*(M+d)**2)
assert s.factor(phi(psi)-s.diff(psi,M)-delta)==0
P=(k-d+1)*M+d-1
N=M*P/k-M*(k*M-(d-k)*P)/k+P**2/k-M**2/d
Nt=(k-2*d)*M**2+d*(k-d+3)*M+d*(d-1)
assert s.factor(N-(d-1)*Nt/(d*k))==0
assert s.factor(Nt-M*(M+d)*(k-psi))==0
boundaries=[]
for dd in range(3,36):
    for n in [2*dd-1,2*dd]:
        mm=n+1
        T=2*dd-2+mm
        u=comb(T-1,dd-2)
        win=sum(comb(T-1,j) for j in range(dd-1,dd-1+mm))
        coeff=(mm-2*dd-2)*win+Fraction(dd,dd-1)*mm*(mm+2*dd)*u
        actual=1 if coeff>0 else -1 if coeff<0 else 0
        expected=1 if dd in [3,4] and n==2*dd else -1
        assert actual==expected,(dd,n,actual,expected)
        boundaries.append({'d':dd,'n':n,'sign':actual})
mp.mp.dps=75
def vals(dd,xx):
    m0=mp.hyp1f1(1,dd,xx)
    m1=mp.hyp1f1(2,dd+1,xx)/dd
    m2=2*mp.hyp1f1(3,dd+2,xx)/(dd*(dd+1))
    kp=m1/m0-mp.mpf(1)/dd
    kpp=m2/m0-(m1/m0)**2
    K=mp.log(m0)-xx/dd
    return kp-xx*kpp,2*K-xx*kp,kp/(1-mp.mpf(1)/dd),K,kp
def bisect(fun,a,b):
    a,b=mp.mpf(a),mp.mpf(b)
    assert fun(a)*fun(b)<0
    for _ in range(260):
        mid=(a+b)/2
        if fun(a)*fun(mid)<=0:b=mid
        else:a=mid
    return (a+b)/2
table=[]
for dd in [3,5,17,100]:
    lo=mp.mpf(2)*(dd-2)*(dd+1)/dd
    kf=bisect(lambda xx:vals(dd,xx)[0],lo,2*dd)
    kc=bisect(lambda xx:vals(dd,xx)[1],kf,20*dd+50)
    bf=vals(dd,kf)[2]
    _,_,bc,K,kp=vals(dd,kc)
    row=dict(d=dd,kappa_f=mp.nstr(kf,20),lambda_min=mp.nstr(kf/(2*bf),20),kappa_c=mp.nstr(kc,20),b_c=mp.nstr(bc,20),lambda_c=mp.nstr(kc/(2*bc),20),D_c=mp.nstr((1-mp.mpf(1)/dd)*(1-bc**2),20),R_c=mp.nstr(kc*kp-K,20))
    table.append(row)
out['paper2']={'symbolic_rational_identities':3,'boundary_comparisons':len(boundaries),'boundary_results':boundaries,'numerical_precision_decimal_digits':75,'table':table}
print('Paper 2: symbolic identities, 66 finite comparisons and four numerical rows verified',flush=True)

# Paper 3: exact counterexample to the final iff assertion in Theorem 6.1.
z=s.symbols('z',nonzero=True)
S1=s.Matrix([[z+1,z-1],[z-1,z+1]])/2
S2=s.diag(1,z)*S1
sharp=lambda A:A.subs(z,1/z).T # coefficients are real
assert s.simplify(sharp(S1)*S1)==s.eye(2)
assert s.simplify(sharp(S2)*S2)==s.eye(2)
assert s.factor(S1.det())==z and s.factor(S2.det())==z**2
P=s.Matrix([z+1,z*(z-1)])
assert s.gcd(P[0],P[1])==1
assert s.simplify((sharp(P)*P)[0])==4
assert S1.subs(z,1)[:,0]==S2.subs(z,1)[:,0]
assert S1.subs(z,-1)[:,0][0]==S2.subs(z,-1)[:,0][0]==0
out['paper3']={'classification':'proved false: final iff in Theorem 6.1, page 8','nodes':[1,-1],'targets':['span(e1)','span(e2)'],'P':['z+1','z*(z-1)'],'gcd':1,'outer_factor':2,'S1_det':'z','S2_det':'z^2','minimum_degree':1,'degree_from_P':2,'corrected_condition':'fdeg(P)=delta_Gr AND no gcd zeros in the open unit disk'}
print('Paper 3: exact inner-matrix counterexample to the final iff in Theorem 6.1 verified',flush=True)
(ROOT/'checks-core.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')

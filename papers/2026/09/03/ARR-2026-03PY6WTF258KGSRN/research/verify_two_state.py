"""Exact algebraic replay for paper.md. Numeric exploration is not imported."""
from pathlib import Path
import hashlib
import json
import sympy as S

HERE=Path(__file__).resolve().parent
checks=[]
def check(name, condition, detail=None):
    if not bool(condition): raise AssertionError(name)
    checks.append(dict(name=name,status="PASS",detail=detail))
def zero(name, expression):
    value=S.factor(S.cancel(expression))
    check(name,value==0,str(value))
def psd(name,M):
    from itertools import combinations
    for k in range(1,M.rows+1):
        for I in combinations(range(M.rows),k):
            d=S.factor(M.extract(I,I).det())
            check(name+" principal "+str(I),d.is_nonnegative is True,str(d))

t,V,Y,K,d,m,T,lam=S.symbols('t V Y K d m T lam',real=True)
A=Y**2-2*V+2*d**2;B=Y**2*K;C=V**2+Y**2*K**2-d**4
q=t*t-d*d;h=t*t-V-S.I*Y*(t+K)
H=(t*t-V)**2+Y**2*(t+K)**2
N=Y*(1+(t+m)**2)*(t*t+2*K*t+V)
R=T*H-N
zero("power identity",h*S.conjugate(h)-q*q-(A*t*t+2*B*t+C))
zero("PSD determinant factorization",A*C-B*B-(V-d*d)*(Y*Y*(V+d*d-2*K*K)-2*(V*V-d**4)))
zero("delay derivative identity",S.im(S.diff(h,t)*S.conjugate(h))*(1+(t+m)**2)-N)
coeff=[T*(V*V+Y*Y*K*K)-Y*V*(m*m+1),2*T*Y*Y*K-2*Y*(m*V+K*(m*m+1)),T*(Y*Y-2*V)-Y*(V+4*m*K+m*m+1),-2*Y*(K+m),T-Y]
zero("all quartic coefficients",R-sum(c*t**j for j,c in enumerate(coeff)))
G=S.Matrix([[coeff[0],coeff[1]/2,lam],[coeff[1]/2,coeff[2]-2*lam,coeff[3]/2],[lam,coeff[3]/2,coeff[4]]])
z=S.Matrix([1,t,t*t]);zero("Gram coefficient identity",(z.T*G*z)[0]-R)

pa,pb,pc=S.symbols('pa pb pc',real=True)
p=pa*t+pb+S.I*pc
M=S.Matrix([[p,-q],[q,S.conjugate(p)]])
zero("completion off-diagonal",(S.conjugate(M.T)*M)[0,1])
zero("completion diagonal equality",(S.conjugate(M.T)*M)[0,0]-(S.conjugate(M.T)*M)[1,1])
zero("completion determinant",M.det()-q*q-p*S.conjugate(p))

stability_y,eta1,eta2,rr=S.symbols('stability_y eta1 eta2 rr',positive=True)
yy=eta1+eta2;vv=rr*rr+eta1*eta2;kk=rr*(eta1-eta2)/yy
zero("root stability factorization",vv-kk*kk-eta1*eta2*(1+4*rr*rr/yy**2))

for dd in [S.Rational(1,5),S.Rational(1,2),S.Rational(3,4),S.Integer(1)]:
    sub={d:dd,V:1,Y:2,K:0,m:0,T:2}
    psd("delay-two PSD d="+str(dd),S.Matrix([[A,B],[B,C]]).subs(sub))
    zero("delay-two global residual d="+str(dd),R.subs(sub))
    pp=S.sqrt(2+2*dd*dd)*t+S.I*S.sqrt(1-dd**4)
    zero("delay-two explicit factor d="+str(dd),H.subs(sub)-(t*t-dd*dd)**2-pp*S.conjugate(pp))

# Boundary failure: constant disk denominator (V,Y,K,m)=(1,2,0,0)
check("acute constant-delay obstruction",C.subs({d:S.Rational(5,4),V:1,Y:2,K:0})<0)

# Explicit asymmetric and symmetric double-pole feasibility and cap certificates.
for uu,vv in [(S.Rational(2),S.Rational(1)),(S.Rational(3),S.Rational(1,3)),(S.Rational(7,3),S.Rational(4,5)),(S.Rational(1,2),S.Rational(1,2))]:
    dd=(uu+vv)/2;mm=(vv-uu)/2
    sub={d:dd,V:dd*dd,Y:2*dd,K:0,m:mm}
    psd("double-pole powers u,v="+str((uu,vv)),S.Matrix([[A,B],[B,C]]).subs(sub))
    p0=(1+mm*mm+dd*dd)/(2*dd);cap=2*(p0+S.sqrt(p0*p0-1))
    # R=(t^2+d^2)*F with F a nonnegative quadratic of determinant zero.
    F=S.Poly(S.cancel(R.subs(sub).subs(T,cap)/(t*t+dd*dd)),t)
    FM=S.Matrix([[F.nth(2),F.nth(1)/2],[F.nth(1)/2,F.nth(0)]])
    psd("double-pole cap factor u,v="+str((uu,vv)),FM)
    zero("double-pole cap attained u,v="+str((uu,vv)),FM.det())

x,w=S.symbols('x w',positive=True)
poly=x**3-(4*w+1)*x*x-(w*w+4*w)*x+w*w
ystar=(x-w)/S.sqrt(x);tstar=(x+1)*(x+w)/(2*S.sqrt(x)*(x-w))
raw=S.Poly(S.expand((R.subs({V:w,Y:ystar,K:0,m:0,T:tstar})-(tstar-ystar)*(t*t-x)**2)*S.sqrt(x)),t)
for j,c in enumerate(reversed(raw.all_coeffs())):
    n,den=S.cancel(c).as_numer_denom()
    zero("cubic residue coefficient "+str(j),S.rem(n,poly,x))

r=S.symbols('r',positive=True)
wr=(r*r+4*r-1)/(r*(r*r-4*r-1));xr=r*wr
zero("cubic parametrization",poly.subs({x:xr,w:wr}))
zero("parameter derivative",S.diff(wr,r)+(r-1)**2*(r*r+10*r+1)/(r*r*(r*r-4*r-1)**2))
ts2=S.cancel(tstar**2)
gap=-(r*r-6*r+1)*(r**3+6*r*r+9*r-4)/(r*(r*r-4*r-1)*(r*r+4*r-1))
zero("strict improvement identity",(4*w-ts2).subs({x:xr,w:wr})-gap)

for rp in [S.Rational(17,4),S.Rational(9,2),S.Rational(19,4),S.Integer(5),S.Rational(21,4),S.Rational(11,2),S.Rational(23,4)]:
    wp=S.factor(wr.subs(r,rp));xp=rp*wp;yp=S.factor(ystar.subs({x:xp,w:wp}));tp=S.factor(tstar.subs({x:xp,w:wp}))
    check("acute parameter w>1 r="+str(rp),wp>1)
    check("acute positive Gram r="+str(rp),(tp-yp).is_positive is True)
    check("acute strict improvement r="+str(rp),(4*wp-tp*tp).is_positive is True)
    zero("acute exact square r="+str(rp),R.subs({V:wp,Y:yp,K:0,m:0,T:tp})-(tp-yp)*(t*t-xp)**2)

fixture=R.subs({V:S.Rational(11,5),Y:4*S.sqrt(11)/5,K:0,m:0,T:9/S.sqrt(11)})
zero("named 9/sqrt(11) fixture",fixture-(t*t-11)**2/(5*S.sqrt(11)))
check("named fixture reduction",S.N(100*(1-(9/S.sqrt(11))/(2*S.sqrt(S.Rational(11,5)))),30)>8)

eps,eta=S.symbols('eps eta',nonnegative=True)
gap_eps=(S.sqrt(9+8*eta)-3)/2
zero("Fourier gap quadratic",gap_eps**2+3*gap_eps-2*eta)

root4=next(z for z in S.nroots(poly.subs(w,4),n=55,maxsteps=100) if abs(S.im(z))<S.Rational(1,10)**40 and S.re(z)>4)
peak4=S.N(tstar.subs({x:root4,w:4}),45)
report={"status":"PASS","check_count":len(checks),"checks":checks,
        "source_sha256":hashlib.sha256((HERE/'paper.md').read_bytes()).hexdigest(),
        "verifier_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "numeric_supplement":{"d=2_cubic_peak":str(peak4),"named_fixture_peak":str(S.N(9/S.sqrt(11),45)),"named_fixture_percent_improvement":str(S.N(100*(1-(9/S.sqrt(11))/(2*S.sqrt(S.Rational(11,5)))),30))},
        "scope":"Universal symbolic identities and exact fixtures. Not formal proof verification; no numerical global-minimum claim."}
(HERE/'two_state_certificate.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))

"""No numerical solver: replay the rational residual inequalities from saved data."""
from pathlib import Path
import sympy as s,json
p=Path(__file__).parent
read=lambda f:json.loads((p/f).read_text())
matrix=lambda rows:s.Matrix([[s.sympify(z) for z in row] for row in rows])
real=lambda z:s.simplify(s.re(s.expand_complex(z)))
def pt(x):
    r=x.rows//2
    return s.Matrix(r,r,lambda i,j:sum(x[k*r+i,k*r+j] for k in range(2)))
v=read('PETZ-CERTIFICATE991.json');sigma=matrix(v['sigma']);delta=matrix(v['delta']);step=s.sympify(v['step']);rho=sigma+step*delta
a=s.Matrix([s.Rational(1,2),0,0,0,1,0]);b=s.Matrix([0,1,0,0,0,s.Rational(1,2)])
assert sigma==s.Rational(999,1000)*(a*a.T+b*b.T)/s.Rational(5,2)+s.eye(6)/6000
assert s.trace(sigma)==1 and pt(delta)==s.zeros(3) and delta==delta.conjugate().T
assert all(real(z*s.conjugate(z))<4 for z in delta)
assert s.Rational(1,6000)-12*step>s.Rational(1,12000)
channel=lambda x:x/2+s.kronecker_product(s.eye(2),pt(x))/4
def bounds(a,b,d,y):
    qy=a*y+y*b;res=d-qy
    low=real(2*s.trace(d.conjugate().T*y)-s.trace(y.conjugate().T*qy))
    er=real(s.trace(res.conjugate().T*res));assert er>=0
    return low,low+6000*er
li,ui=bounds(rho,sigma,delta,matrix(v['input_approximate_solution']))
lo,uo=bounds(channel(rho),channel(sigma),channel(delta),matrix(v['output_approximate_solution']))
assert [li,ui]==[s.sympify(z) for z in v['input_scaled_interval']]
assert [lo,uo]==[s.sympify(z) for z in v['output_scaled_interval']]
assert li>0 and lo-ui/3>0
w=read('VARIANCE-CERTIFICATE991.json');G=matrix(w['G']);H=matrix(w['H']);B=matrix(w['B_approximate']);n=G.rows;r=n//2
sigma2=s.Rational(99999,100000)*(G*G.conjugate().T)/s.trace(G*G.conjugate().T)+s.eye(n)/(100000*n)
assert pt(H)==s.zeros(r) and H==H.conjugate().T and B==B.conjugate().T
ref=pt(sigma2);C=pt((sigma2*H+H*sigma2)/2);QB=(ref*B+B*ref)/2;res=C-QB
upper=real(2*s.trace(C*B)-s.trace(B*QB))+50000*n*real(s.trace(res.conjugate().T*res))
vl=real(s.trace(sigma2*H*H))-upper;ve=real(s.trace(s.kronecker_product(s.eye(2)/2,ref)*H*H))
assert vl==s.sympify(w['variance_lower']) and ve==s.sympify(w['variance_E']) and vl-2*ve>0
result=dict(rational_certificates_checked=2,failures=0,petz_ratio_lower=str(s.N(lo/ui,25)),variance_ratio_lower=str(s.N(vl/ve,25)),scope='Exact rational residual inequalities checked from stored witness matrices without optimization/numerical solvers. Analytical resolvent representation and spectral-floor reasoning stated in NOTE991; not Lean formalization or independent review.')
(p/'VERIFIED991.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))

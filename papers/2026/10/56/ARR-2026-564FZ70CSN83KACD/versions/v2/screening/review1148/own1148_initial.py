from pathlib import Path
from fractions import Fraction as F
import sympy as s,mpmath as mp,json,traceback
P=Path(__file__).resolve().parent;rows=[]
mp.mp.dps=260
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def num(x):return mp.mpf(x.numerator)/x.denominator if isinstance(x,F) else mp.mpf(str(x))
def fmt(x):return mp.nstr(x,50)
def trace(a):return sum(a[j,j] for j in range(a.rows))
def logm(a):
    e,u=mp.eighe(a);assert min(e)>0
    return u*mp.diag([mp.log(x) for x in e])*u.H
def rel(a,b):return mp.re(trace(a*(logm(a)-logm(b))))
def kl(p,q):return p*mp.log(p/q)+(1-p)*mp.log((1-p)/(1-q))
try:
 # Exact Gram-coordinate tests use the correct inner product, including very small row weights.
 for n,m in [(2,1),(4,2),(5,3),(7,6)]:
    G=(n*s.eye(m)-s.ones(m,m))/s.Integer(n-1);one=s.ones(m,1)
    w=s.Matrix([s.Rational(1,37**j*2**(40*j)) for j in range(m)]);W=s.diag(*w);t=sum(w)
    v=G.inv()*one
    assert (one.T*G.inv()*one)[0]==s.Rational(m*(n-1),n-m)
    assert W*G*v==w and (w.T*G*v)[0]==t
    k=n+5;b=s.Rational(1,4*n*k);d=s.Rational(1,2**k);e=b*d;a=s.Rational(1,n)-(n-2)*e-b;c2=a*b*(1-d)
    M=(a-e)*W*G+e*t*s.eye(m)
    H0=s.factor(b*t-c2*(w.T*G*M.inv()*w)[0])
    HE=s.factor(b*t-e*t-c2*(w.T*G*(M-e*t*s.eye(m)).inv()*w)[0])
    assert H0>=b*t*d>0 and HE==-t*b*e*(1-d)/(a-e)<0
    rows.append(dict(name='proper_support_exact_new_weights',n=n,m=m,k=k,inverse_norm2=str((one.T*G.inv()*one)[0]),min_weight=str(min(w)),Schur0_lower_pass=True,Schur_endpoint_identity_pass=True))
 # A real minor scope flaw: absent n=2 modes do not justify a scalar positivity assertion.
 n=2;a=s.Rational(1,4);b=a;e=s.Integer(1);d=s.Rational(1,2)
 unused=(n*a+(n*n-3*n+1)*e)/(n-1)**2
 assert unused==-s.Rational(1,2)
 rows.append(dict(name='minor_n2_inactive_output_scalar',n=2,alpha=str(a),beta=str(b),epsilon=str(e),delta=str(d),printed_eprime=str(unused),inactive_multiplicity=0,actual_active_determinant=str(a*b*d),conclusion='The p6 claim eprime>0 is not valid for arbitrary n2 parameters, but no such eigenmode exists. Main theorems unaffected; qualify scalar statement to n>=3.'))
 x=s.symbols('x',real=True);p=s.Rational(1,5)+s.Rational(7,10)*x
 Fx=s.factor(s.Rational(49,100)*x*(1-x)/(p*(1-p)))
 gap=s.factor(s.Rational(1,2)-Fx)
 assert s.simplify(gap-(7*x-4)**2/(2*(7*x+2)*(8-7*x)))==0
 assert Fx.subs(x,s.Rational(4,7))==s.Rational(1,2)
 rows.append(dict(name='binary_counterexample_to_general_Doeblin_equality',Doeblin='3/10',one_minus_Doeblin='7/10',exact_coefficient='1/2',maximizer='4/7',exact_gap_to_half=str(gap)))

 def check(label,K,k):
    n=len(K[0]);assert all(sum(row[i] for row in K)==1 for i in range(n))
    d=sum(min(row) for row in K)
    beta=F(1,4*n*k);delta=F(1,2**k);eps=beta*delta;alpha=F(1,n)-(n-2)*eps-beta
    a,b,e,de=map(num,[alpha,beta,eps,delta]);c=mp.sqrt(a*b*(1-de))
    f=mp.ones(n,1)/mp.sqrt(n);FF=f*f.H;PP=mp.eye(n)-FF
    U=mp.eye(n);U[0,0]=mp.mpf(3)/5;U[0,1]=4j/5;U[1,0]=4j/5;U[1,1]=mp.mpf(3)/5
    # Enter the rational complex rotation at high precision, without binary float4/5.
    U[0,1]=mp.j*4/5;U[1,0]=mp.j*4/5
    assert mp.norm(U*U.H-mp.eye(n))<mp.mpf('1e-250')
    plus=[];minus=[]
    for i in range(n):
      psi=mp.sqrt(mp.mpf(n)/(n-1))*(mp.eye(n)[:,i]-mp.ones(n,1)/n);Pi=psi*psi.H
      base=a*Pi+e*(PP-Pi)+b*FF;coh=c*(psi*f.H+f*psi.H)
      plus.append(U*(base+coh)*U.H);minus.append(U*(base-coh)*U.H)
    assert mp.norm(sum(plus,mp.zeros(n))-sum(minus,mp.zeros(n)))<mp.mpf('1e-245')
    Di=sum(rel(u,v) for u,v in zip(plus,minus));Do=mp.mpf(0);p=mp.mpf(0);q=mp.mpf(0);pF=mp.mpf(0);qF=mp.mpf(0)
    B=c*c*(n-1)**2/(a-e)**2;checked=0
    for wr in K:
      t=sum(wr)
      if t==0:continue
      rplus=sum((num(w)*u for w,u in zip(wr,plus)),mp.zeros(n));rminus=sum((num(w)*u for w,u in zip(wr,minus)),mp.zeros(n))
      Do+=rel(rplus,rminus)
      if min(wr)>0:continue # explicitly omit full-support row from this lower test only
      ev,V=mp.eighe(rminus);ell=ev[0];z=V[:,0];effect=z*z.H;ss=abs((z.H*U*f)[0])**2
      assert b*num(t)*de/(1+B)<=ell+mp.mpf('1e-220') and ell<b*num(t)*de+mp.mpf('1e-220')
      assert ss>=1/(1+B)-mp.mpf('1e-220')
      py=mp.re(trace(effect*rplus));qy=mp.re(trace(effect*rminus))
      assert abs((py-qy)-4*ss*(b*num(t)-ell))<mp.mpf('1e-215')
      p+=py;q+=qy;effF=U*FF*U.H;pF+=mp.re(trace(effF*rplus));qF+=mp.re(trace(effF*rminus));checked+=1
    if p==q:Db=mp.mpf(0);rev=mp.mpf(0)
    else:Db=kl(p,q);rev=kl(q,p)
    assert abs(pF-qF)<mp.mpf('1e-240')
    assert -mp.mpf('1e-210')<=Db<=Do+mp.mpf('1e-210')<=num(1-d)*Di+mp.mpf('1e-210')
    if d==0:
      qL=n*b*de/(1+B);qU=n*b*de;pL=qL+4*n*b*(1-de)/(1+B);pU=qU+4*n*b
      assert qL<=q+mp.mpf('1e-215')<=qU+mp.mpf('1e-214') and pL<=p+mp.mpf('1e-215')<=pU+mp.mpf('1e-214')
      low=kl(pL,qU)/Di if pL>qU else mp.mpf(0)
      assert low<=Db/Di+mp.mpf('1e-210')
    else:low=None
    out=dict(name=label,n=n,k=k,outputs=len(K),proper_nonzero_rows=checked,Doeblin=str(d),Di=fmt(Di),Do=fmt(Do),Db=fmt(Db),measured_ratio=fmt(Db/Di),reverse_Bernoulli_ratio=fmt(rev/Di),p=fmt(p),q=fmt(q),uniform_lower=fmt(low) if low is not None else None,DPI_and_Doeblin_upper_pass=True,row_root_bounds_pass=True,limit_F_zero=True,complex_rotation=True,numeric_not_interval=True)
    rows.append(out);return out
 check('n2_disjoint_split_and_zero',[[F(1,3),F(0)],[F(2,3),F(0)],[F(0),F(1)],[F(0),F(0)]],9)
 for k in [6,12,24]:
    th=F(1,2**(k*k));base=[[F(0),th,1-th],[1-th,F(0),th],[th,1-th,F(0)]]
    K=[[v/k for v in row] for row in base for _ in range(k)]+[[F(0)]*3]
    check('K_k_tiny_weights_and_growing_output_alphabet',K,k)
 cycle=[[F(1,2) if i in [j,(j+1)%4] else F(0) for i in range(4)] for j in range(4)]
 check('cycle4_complex',cycle,19)
 marked=[[F(9,10)*v for v in row] for row in cycle]+[[F(1,10)]*4]
 check('marked_replacement_effect_omitted',marked,19)
 check('replacement_d1',[[F(2,7)]*3,[F(5,7)]*3,[F(0)]*3],11)
 put('OWN1148.json',dict(all_passed=True,precision_digits=260,records=rows,scope='Exact new rational Gram/Schur cases plus fixed complex block-spectrum diagnostics. No optimizer, resampling, universal numerical proof or independent interval-library claim.'))
 print(json.dumps(dict(all_passed=True,records=len(rows),minor_scope_counterexample_retained=True)))
except Exception as ex:
 put('OWN-FAILURE1148.json',dict(error=repr(ex),traceback=traceback.format_exc(),completed=rows));raise

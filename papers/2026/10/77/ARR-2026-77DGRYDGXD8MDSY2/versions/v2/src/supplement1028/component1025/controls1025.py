"""Own rank-two construction and ambient rational Sylvester solves.
Does not import the candidate checker or its connected-block solver.
"""
from pathlib import Path
import sympy as s,json,traceback
P=Path(__file__).parent;R=s.Rational;rows=[]
def record(name,**data):
 rows.append({'name':name,**data});(P/'EXACT1025.json').write_text(json.dumps({'records':rows},indent=2,default=lambda x:bool(x))+'\n',encoding='utf-8');print(name,flush=True)
def ptr(x,d,r):return s.Matrix(r,r,lambda i,j:sum(x[a*r+i,a*r+j] for a in range(d)))
def E(x,d,r):return s.kronecker_product(s.eye(d)/d,ptr(x,d,r))
def fullform(a,b,z):
 n=a.rows;Q=s.SparseMatrix(s.kronecker_product(a,s.eye(n))+s.kronecker_product(s.eye(n),b.T));rhs=s.SparseMatrix(n*n,1,{(i,0):v for i,v in enumerate(z) if v!=0});y=Q.inv()*rhs;Y=s.Matrix(n,n,list(y));assert a*Y+Y*b==z
 return s.factor(s.trace(z.T*Y))
def positive(a):
 l,d=a.LDLdecomposition(hermitian=False);assert l*d*l.T==a;piv=list(d.diagonal());assert all(v>0 for v in piv);return [str(v) for v in piv]
def construct(d,e):
 r=d+1;n=d*r;A=s.zeros(n,2);F=s.zeros(n,2)
 for i in range(2):
  A[i*r+i,i]=1
  for k in range(1,d):
   ix=((i+k)%d)*r+k+1;A[ix,i]=e;F[ix,i]=(-1)**i
 q=1+(d-1)*e*e;sig=A*A.T/(2*q);D=A*F.T+F*A.T
 return sig,D,A,F
try:
 # Symbolic inverse from Cayley-Hamilton, rather than solving entries.
 d=s.symbols('d',integer=True,positive=True);e,p=s.symbols('e p',positive=True);m=d-1;L=d*(d+1)/2;q=1+m*e*e
 W=s.Matrix([[1+(d-1)*p,d*p*e*s.sqrt(m)],[d*p*e*s.sqrt(m),(2+(d*m-2)*p)*e*e]])/(2*d*q);T=s.Matrix([[0,s.sqrt(m)],[s.sqrt(m),2*e*m]])
 Y=(T+W.det()*W.inv()*T*W.inv())/s.trace(W)
 assert s.simplify(W*Y+Y*W-2*T)==s.zeros(2)
 G=s.factor(s.trace(T*Y));limit=s.factor(s.limit(G,e,0)/(8*m));assert s.factor(limit-L/(1+(L-1)*p))==0
 assert s.factor(W.det()-e*e*(1-p)*(1+(L-1)*p)/(2*d*d*q*q))==0
 record('symbolic_Cayley_Hamilton',G=str(G),normalized_limit=str(limit),residual_zero=True,determinant_correct=True)
 # Exact ambient decomposition and Gram; non-normalized plane bases avoid radicals.
 for dd in range(2,7):
  ee=R(2,9);r=dd+1;n=dd*r;sig,D,A,F=construct(dd,ee);B=E(sig,dd,r);qq=1+(dd-1)*ee*ee;cap=R(dd*(dd+1),2);Pr=2*sig
  assert A.T*B.inv()*A/(2*qq)==cap*s.eye(2)
  assert s.trace(sig)==1 and ptr(D,dd,r)==s.zeros(r) and Pr*Pr==Pr and (s.eye(n)-Pr)*D*(s.eye(n)-Pr)==s.zeros(n)
  boundary=4*s.trace(D*D)-2*s.trace((Pr*D*Pr)**2);assert boundary==16*(dd-1)*qq
  pp=-R(1,2*(dd*dd-1));S=(1-pp)*B+pp*sig;plane_facts=[]
  for i in range(2):
   u=s.zeros(n,1);u[i*r+i]=1;v=(-1)**i*F[:,i];H=s.Matrix.hstack(u,v);gram=H.T*H
   # Coordinate operator on main/uniform-center plane, plus orthogonal projection residual.
   mat=gram.inv()*H.T*S*H;td=gram.inv()*H.T*D*H
   assert S*H==H*mat and D*H==H*td
   expected=s.Matrix([[1+(dd-1)*pp,dd*pp*ee*(dd-1)],[dd*pp*ee,(2+(dd*(dd-1)-2)*pp)*ee*ee]])/(2*dd*qq)
   assert mat==expected
   assert td==(-1)**i*s.Matrix([[0,dd-1],[1,2*ee*(dd-1)]])
   coords=[((i+k)%dd)*r+k+1 for k in range(1,dd)]
   for j in range(1,len(coords)):
    z=s.zeros(n,1);z[coords[0]]=1;z[coords[j]]=-1
    assert D*z==s.zeros(n,1) and S*z==ee*ee*(1-pp)/(dd*qq)*z
   Q=s.zeros(n)
   for ix in [i*r+i]+coords:Q[ix,ix]=1
   assert Q*S==S*Q and s.trace(Q*D)==(-1)**i*2*ee*(dd-1)
   plane_facts.append(True)
  record('full_structure',d=dd,R=r,dimension=n,L=str(cap),boundary_SLD=str(boundary),planes_and_orthogonal_modes_checked=True)
 # Reproduce a genuinely non-Bell-range finite certificate using full144x144 inverses.
 dd=3;r=4;ee=R(1,10);kap=R(5);th=R(79,100);ll=-R(1,8);tt=R(1,10**8)
 sig0,D,A,F=construct(dd,ee);B=E(sig0,dd,r);sig=(1-th)*B+th*sig0;rho=sig+tt*D
 op=lambda x:ll*x+(1-ll)*E(x,dd,r);os=op(sig);orr=op(rho)
 checks={key:positive(x) for key,x in {'sigma':sig,'rho':rho,'sigma_order_slack':kap*B-sig,'rho_order_slack':kap*B-rho,'out_sigma':os,'out_rho':orr}.items()}
 gin=2*fullform(sig,sig,D);gout=2*fullform(os,os,ll*D);local=s.factor(gout/gin)
 tin=fullform(rho,sig,tt*D);tout=fullform(orr,os,ll*tt*D);tri=s.factor(tout/tin)
 ref=json.loads(Path(r'D:\Proyectos\airr-investigacion\2026-10-27_ranktwo1021\CHECK1021.json').read_text())['matrices'][1]['finite_pairs'][0]
 assert local==s.sympify(ref['local']) and tri==s.sympify(ref['triangular'])
 bellcap=R(1,8);assert local>bellcap and tri>bellcap
 record('ambient144_ranktwo',d=dd,R=r,kappa=str(kap),theta=str(th),lambda_=str(ll),e=str(ee),t=str(tt),SLD=str(local),finite_triangle=str(tri),upper=str(R(5,32)),Bell_family_cap=str(bellcap),SLD_gap_over_Bell=str(local-bellcap),triangle_gap_over_Bell=str(tri-bellcap),Gin=str(gin),Gout=str(gout),LDL_positive_pivots=checks,matches_input=True)
 # Independent full rational qubit PPT plus explicit separable decomposition.
 I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
 for K,kap in [(R(149,100),R(3,2)),(R(199,100),R(2))]:
  a=K/4;b=(1-2*a)/2;tt=R(1,10**8);v=s.Matrix([1,0,0,1]);w=s.Matrix([0,1,1,0]);P0=v*v.T/2;P1=w*w.T/2;D=P0-P1;sig=b*s.eye(4)+(a-b)*(P0+P1);rho=sig+tt*D
  pt=lambda x:s.Matrix(4,4,lambda i,j:x[2*(j//2)+i%2,2*(i//2)+j%2])
  facts={name:positive(x) for name,x in {'sigma':sig,'rho':rho,'sigma_PPT':pt(sig),'rho_PPT':pt(rho),'sigma_slack':kap*s.eye(4)/4-sig,'rho_slack':kap*s.eye(4)/4-rho}.items()}
  cs=[K-1,-2*tt,2*tt];weights=[abs(x) for x in cs];res=1-sum(weights);assert res>0
  sep=res*s.eye(4)/4
  for c,w0,pauli in zip(cs,weights,[X,Y,Z]):sep+=w0*(s.eye(4)+s.sign(c)*s.kronecker_product(pauli,pauli))/4
  assert sep==rho
  ratios=[]
  for ll in [-R(1,3),R(1,2)]:
   op=lambda x:ll*x+(1-ll)*E(x,2,2);os=op(sig);orr=op(rho);tr=s.factor(fullform(orr,os,orr-os)/fullform(rho,sig,rho-sig));al=ll*a+(1-ll)/4
   direct=s.factor(((ll*tt)**2/(2*al+ll*tt)+(ll*tt)**2/(2*al-ll*tt))/(tt**2/(2*a+tt)+tt**2/(2*a-tt)))
   assert tr==direct
   ratios.append({'lambda':str(ll),'finite_triangle':str(tr),'local':str(ll*ll*a/al)})
  record('Bell_qubit_explicit_SEP_PPT',K=str(K),kappa=str(kap),t=str(tt),correlations=[str(c) for c in cs],separable_axis_weights=[str(w0) for w0 in weights],identity_weight=str(res),exact_LDL=facts,ratios=ratios)
 record('complete',passed=True)
except Exception as ex:
 record('ERROR',error=repr(ex),traceback=traceback.format_exc());raise

from pathlib import Path
import sympy as s,mpmath as mp,json,traceback
P=Path(__file__).parent;R=s.Rational;rows=[]
def record(name,**data):
 rows.append({'name':name,**data});(P/'FULLMATRIX1044.json').write_text(json.dumps({'records':rows},indent=2,default=lambda v:bool(v))+'\n',encoding='utf-8');print(name,flush=True)
def ptr(x,d,r):return s.Matrix(r,r,lambda i,j:sum(x[a*r+i,a*r+j] for a in range(d)))
def E(x,d,r):return s.kronecker_product(s.eye(d)/d,ptr(x,d,r))
def construct(d,e):
 a=d-1;r=2*d-1;n=d*r;V=s.zeros(n,2);F=s.zeros(n,2)
 for j in range(a):V[(j+1)*r+j,0]=1;V[j*r+a+j,1]=1
 V[2*a,0]=e;F[2*a,0]=1;V[(d-1)*r+2*a,1]=e;F[(d-1)*r+2*a,1]=-1
 return V*V.T/(2*(a+e*e)),V*F.T+F*V.T,V,F
def form(A,B,Z):
 n=A.rows;Q=s.SparseMatrix(s.kronecker_product(A,s.eye(n))+s.kronecker_product(s.eye(n),B.T));rhs=s.SparseMatrix(n*n,1,{(i,0):v for i,v in enumerate(Z) if v!=0});Y=s.Matrix(n,n,list(Q.inv()*rhs));assert A*Y+Y*B==Z;return s.factor(s.trace(Z.T*Y))
def pos(A):
 l,d=A.LDLdecomposition(hermitian=False);assert l*d*l.T==A;p=list(d.diagonal());assert all(v>0 for v in p);return [str(v) for v in p]
try:
 d,e,p=s.symbols('d e p',positive=True);a=d-1;q=a+e*e;M=d*(2*d-1)/2
 W=s.Matrix([[1+(d*a-1)*p,d*p*e*s.sqrt(a)],[d*p*e*s.sqrt(a),(2+(d-2)*p)*e*e]])/(2*d*q);T=s.Matrix([[0,s.sqrt(a)],[s.sqrt(a),2*e]])
 Y=(T+W.det()*W.inv()*T*W.inv())/s.trace(W);assert s.simplify(W*Y+Y*W-2*T)==s.zeros(2);G=s.factor(s.trace(T*Y));limit=s.factor(s.limit(G,e,0))
 assert s.factor(limit-8*a*M/(1+(M-1)*p))==0
 assert s.factor(W.det()-e*e*(1-p)*(1+(M-1)*p)/(2*d*d*q*q))==0
 # BKM leading logarithmic coefficient from high eigenvalue and crossed tangent.
 high0=(1+(d*a-1)*p)/(2*d*a);bkmlead=s.factor(4*a/high0);assert s.factor(bkmlead-8*d*a*a/(1+(d*a-1)*p))==0
 record('symbolic',SLD_G=str(G),SLD_limit=str(limit),BKM_log_coefficient=str(bkmlead),residual_zero=True)
 for dd in range(2,6):
  ee=R(2,11);aa=dd-1;r=2*dd-1;n=dd*r;sig,D,V,F=construct(dd,ee);B=E(sig,dd,r);qq=aa+ee*ee;cap=R(dd*(2*dd-1),2);Pr=2*sig
  assert s.trace(sig)==1 and ptr(D,dd,r)==s.zeros(r) and V.T*B.inv()*V/(2*qq)==cap*s.eye(2)
  assert Pr*Pr==Pr and (s.eye(n)-Pr)*D*(s.eye(n)-Pr)==s.zeros(n)
  assert 4*s.trace(D*D)-2*s.trace((Pr*D*Pr)**2)==16*qq
  pp=-R(1,2*(dd*dd-1));base=(1-pp)*B+pp*sig
  for i in range(2):
   z=(-1)**i*F[:,i];u=V[:,i]-ee*z;H=s.Matrix.hstack(u,z);gram=H.T*H
   mat=gram.inv()*H.T*base*H;td=gram.inv()*H.T*D*H
   expected=s.Matrix([[1+(dd*aa-1)*pp,dd*pp*ee],[dd*pp*ee*aa,(2+(dd-2)*pp)*ee*ee]])/(2*dd*qq)
   assert mat==expected and base*H==H*mat and D*H==H*td and td==(-1)**i*s.Matrix([[0,1],[aa,2*ee]])
   indices=[(j+1)*r+j if i==0 else j*r+aa+j for j in range(aa)]
   for j in range(1,aa):
    v=s.zeros(n,1);v[indices[0]]=1;v[indices[j]]=-1;assert D*v==s.zeros(n,1) and base*v==(1-pp)/(2*dd*qq)*v
   Q=s.zeros(n)
   for k in indices+[int(2*aa if i==0 else (dd-1)*r+2*aa)]:Q[k,k]=1
   assert Q*base==base*Q and s.trace(Q*D)==(-1)**i*2*ee
  record('ambient_geometry',d=dd,R=r,dimension=n,M=str(cap),all_passed=True)
 dd=3;r=5;ee=R(1,100);th=R(1187,1300);kap=R(7);ll=-R(1,8);tt=R(1,10**8);sig0,D,V,F=construct(dd,ee);B=E(sig0,dd,r);sig=(1-th)*B+th*sig0;rho=sig+tt*D;op=lambda x:ll*x+(1-ll)*E(x,dd,r);os=op(sig);orr=op(rho)
 checks={k:pos(v) for k,v in {'sigma':sig,'rho':rho,'sigma_slack':kap*B-sig,'rho_slack':kap*B-rho,'output_sigma':os,'output_rho':orr}.items()}
 gin=2*form(sig,sig,D);gout=2*form(os,os,ll*D);local=s.factor(gout/gin);tri=s.factor(form(orr,os,ll*tt*D)/form(rho,sig,tt*D))
 ref=json.loads(Path(r'D:\Proyectos\airr-investigacion\2026-10-27_principal1033\CHECK1033.json').read_text())['matrices'][1]['finite'][0]
 assert local==s.sympify(ref['SLD']) and tri==s.sympify(ref['triangular']);assert gin==2*G.subs({d:dd,e:ee,p:th}) and gout==2*ll*ll*G.subs({d:dd,e:ee,p:ll*th})
 record('ambient225_rational',SLD=str(local),triangular=str(tri),Gin=str(gin),Gout=str(gout),both_absolute_scales_match=True,matches_original=True,SLD_gap_over_1021_endpoint=str(local-R(1,4)),LDL_pivots=checks)
 # Full15x15 spectral matrix functions at moderate conditioning; do not reuse candidate BKM implementation.
 mp.mp.dps=90
 mm=lambda A:mp.matrix([[mp.mpf(str(x.p))/mp.mpf(str(x.q)) for x in A.row(i)] for i in range(A.rows)])
 sig0,D,_,_=construct(3,R(1,5));B=E(sig0,3,5);sig=R(3,5)*sig0+R(2,5)*B;tt=R(1,10000);rho=sig+tt*D;ll=R(1,2);os=ll*sig+(1-ll)*B;orr=ll*rho+(1-ll)*B
 def entropy(A,B):
  va,ua=mp.eigsy(A);vb,ub=mp.eigsy(B);c=ub.T*A*ub;assert min(va)>0 and min(vb)>0
  return sum(va[i]*mp.log(va[i])-c[i,i]*mp.log(vb[i]) for i in range(len(va)))
 def metric(A,Z):
  v,U=mp.eigsy(A);z=U.T*Z*U;tot=mp.mpf(0)
  for i in range(len(v)):
   for j in range(len(v)):
    dif=v[i]-v[j];ker=1/v[i] if dif==0 else mp.log1p(dif/v[j])/dif;tot+=z[i,j]**2*ker
  return tot
 DU=entropy(mm(rho),mm(sig));DO=entropy(mm(orr),mm(os));rev=entropy(mm(sig),mm(rho));gm=metric(mm(os),mm(ll*D))/metric(mm(sig),mm(D))
 # Plane logarithms by generic eigsy in rational similar coordinates is unnecessary: use orthonormal restriction directly from exact full matrices.
 h0=s.zeros(15,2);h0[5,0]=1/s.sqrt(2);h0[11,0]=1/s.sqrt(2);h0[4,1]=1
 def mpany(A):return mp.matrix([[mp.mpf(str(s.N(A[i,j],95))) for j in range(A.cols)] for i in range(A.rows)])
 wp=mpany(h0.T*sig*h0);tp=mpany(h0.T*D*h0);op=mpany(h0.T*os*h0);t=mp.mpf(1)/10000
 planeDU=sum(entropy(wp+sign*t*tp,wp) for sign in [-1,1]);planeDO=sum(entropy(op+sign*t*tp/2,op) for sign in [-1,1])
 assert abs(DU-planeDU)<mp.mpf('1e-80') and abs(DO-planeDO)<mp.mpf('1e-80') and DU!=rev
 record('full15_spectral_Umegaki_BKM',parameters='d3,R5,e1/5,theta3/5,t1/10000,lambda1/2',forward_input=str(DU),reverse_input=str(rev),forward_output=str(DO),finite_ratio=str(DO/DU),BKM_ratio=str(gm),full_vs_subnormalized_planes_difference=str(DU-planeDU),orientation_distinguished=True,full_trace_rho=str(s.trace(rho)),partial_trace_D_zero=True)
 record('complete',passed=True)
except Exception as ex:record('ERROR',error=repr(ex),traceback=traceback.format_exc());raise

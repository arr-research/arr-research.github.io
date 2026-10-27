from pathlib import Path
import sympy as s,mpmath as mp,json,traceback,hashlib
P=Path(__file__).resolve().parent;rows=[];mp.mp.dps=85
def put(name,x):(P/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def zero(M):return all(s.simplify(x)==0 for x in M)
def pt(M,d):return s.Matrix(d,d,lambda j,k:sum(M[i*d+j,i*d+k] for i in range(d)))
def mat(M):return mp.matrix([[mp.mpc(str(s.re(x).evalf(90)),str(s.im(x).evalf(90))) for x in M.row(i)] for i in range(M.rows)])
def tr(M):return sum(M[i,i] for i in range(M.rows))
def logmat(M):
 ev,V=mp.eighe(M);assert min(ev)>0
 return V*mp.diag([mp.log(ev[i]) for i in range(M.rows)])*V.H
def rel(A,B):return mp.re(tr(A*(logmat(A)-logmat(B))))
def metric(B,Z,mode):
 ev,V=mp.eighe(B);T=V.H*Z*V;tot=mp.mpf(0)
 for i in range(B.rows):
  for j in range(B.rows):
   if mode=='SLD':k=2/(ev[i]+ev[j])
   elif abs(ev[i]-ev[j])<mp.mpf('1e-70')*max(ev[i],ev[j]):k=1/ev[i]
   else:k=(mp.log(ev[i])-mp.log(ev[j]))/(ev[i]-ev[j])
   tot+=abs(T[i,j])**2*k
 return tot
def triangle(A,B):
 ea,U=mp.eighe(A);eb,V=mp.eighe(B);C=U.H*V
 return sum(abs(C[i,j])**2*(ea[i]-eb[j])**2/(ea[i]+eb[j]) for i in range(A.rows) for j in range(A.rows))
def close(a,b):return abs(a-b)<=mp.mpf('1e-60')*max(abs(a),abs(b),mp.mpf('1e-50'))
def ell(W):
 W=mat(W) if isinstance(W,s.MatrixBase) else W
 ev,_=mp.eighe(W)
 return (mp.log(ev[1])-mp.log(ev[0]))/(ev[1]-ev[0]) if ev[1]!=ev[0] else 1/ev[0]
try:
 # Direct rational identities independent of replay source code.
 d,x,p,delta=s.symbols('d x p delta',positive=True);a=d-1;q=a+x
 W=s.Matrix([[1+(d*a-1)*p,d*p*s.sqrt(a*x)],[d*p*s.sqrt(a*x),(1+a*p)*x]])/(d*q)
 assert s.factor(W.det()-x*(1-p)*(1+(d*d-1)*p)/(d*d*q*q))==0
 K=s.Matrix([[a*x,s.sqrt(a*x)],[s.sqrt(a*x),1]])/(1+a*x);V=s.diag(1,-1);lam=-1/(d*d-1)
 assert zero(W.subs(p,lam)*K)
 wb=W.subs(p,lam*(1-delta));qb=s.factor(s.trace(K*wb));pb=s.factor(s.trace(K*V*wb*V))
 assert s.factor(qb-delta*x/(q*(1+a*x)))==0
 assert s.factor(pb-qb-4*(1-delta)*a*x/((d*d-1)*q*(1+a*x)))==0
 # beta=3/2 is realized through d=n^2; no floating exponent is used.
 n,t=s.symbols('n t',positive=True)
 ti=s.trace(W.subs(p,1-delta));di=W.det().subs(p,1-delta);to=s.trace(wb);do=wb.det()
 sub={d:n*n,x:t/(n*n),delta:n**-3}
 limits=[s.limit(s.factor(z.subs(sub)),n,s.oo) for z in [ti,d**s.Rational(9,2)*di,d**3*to,d**s.Rational(13,2)*do]]
 assert [s.simplify(z) for z in limits]==[1,t,1+t,t]
 rows.append({'name':'general_phase_kernel_and_fractional_beta','determinant_identity':True,'q_exact':str(qb),'p_minus_q_exact':str(s.factor(pb-qb)),'beta_3_2_rational_path_limits':list(map(str,limits)),'analytical_log_deduction':'nu=9/2, alpha=1/[9(1+t)]; binary leading output coefficient=2t/(1+t). Fixed t>0.'})
 # Full ambient matrices, no dependence on old plane solver for their construction.
 for dd,ee,th,angle in [(2,s.Rational(1,2),s.Rational(3,4),-1),(3,s.Rational(2,5),s.Rational(5,6),-1),(4,s.Rational(3,7),s.Rational(7,9),-1),(3,s.Rational(2),s.Rational(2,3),s.Rational(3,5)-4*s.I/5)]:
  N=dd*dd;aa=dd-1;xx=ee*ee;qq=aa+xx;ll=-s.Rational(1,N-1)
  v=s.zeros(N,1);v[0]=ee
  for j in range(1,dd):v[j*dd+j]=1
  base=v*v.T/qq;r=pt(base,dd);B=s.kronecker_product(s.eye(dd)/dd,r)
  S=(1-th)*B+th*base;U=s.diag(*([1]*dd+[angle]*(N-dd)));rho=U*S*U.conjugate().T
  dep=lambda Z:s.simplify(ll*Z+(1-ll)*s.kronecker_product(s.eye(dd)/dd,pt(Z,dd)))
  SO=dep(S);RO=dep(rho)
  assert s.trace(S)==s.trace(rho)==s.trace(SO)==s.trace(RO)==1
  assert zero(pt(S,dd)-r) and zero(pt(rho,dd)-r) and zero(pt(SO,dd)-r)
  assert s.factor((v.T*B.inv()*v)[0]/qq)==N
  assert zero(SO-((1-ll*th)*B+ll*th*base))
  HH=s.kronecker_product(s.diag(0,*([1]*(dd-1))),s.eye(dd));Z=-s.I*(HH*S-S*HH)
  assert zero(pt(Z,dd))
  mm=[mat(z) for z in [S,rho,SO,RO,Z]];SM,RM,SOM,ROM,ZM=mm
  wp=lambda pp:s.Matrix([[1+(dd*aa-1)*pp,dd*pp*ee*s.sqrt(aa)],[dd*pp*ee*s.sqrt(aa),(1+aa*pp)*xx]])/(dd*qq)
  c2=th*th*xx*aa/(qq*qq);ang=1-s.re(angle)
  din,dout=rel(RM,SM),rel(ROM,SOM)
  pred=2*mp.mpf(str(c2))*ell(wp(th))*mp.mpf(str(ang))
  rpred=mp.mpf(str(ll*ll))*ell(wp(ll*th))/ell(wp(th))
  assert close(din,pred) and close(dout/din,rpred)
  bkmi=metric(SM,ZM,'BKM');bkmo=metric(SOM,mp.mpf(str(ll))*ZM,'BKM')
  sldi=metric(SM,ZM,'SLD');sldo=metric(SOM,mp.mpf(str(ll))*ZM,'SLD')
  tri=triangle(RM,SM);trio=triangle(ROM,SOM)
  assert close(bkmo/bkmi,rpred) and close(trio/tri,sldo/sldi)
  rec={'name':'full_ambient_phase','d':dd,'e':str(ee),'theta':str(th),'unitary_phase':str(angle),'exact_order':str(1+(N-1)*th),'marginal_and_geometry_exact':True,'Umegaki_input':mp.nstr(din,45),'retention':mp.nstr(dout/din,45),'BKM_retention':mp.nstr(bkmo/bkmi,45),'SLD_retention':mp.nstr(sldo/sldi,45),'finite_triangular_retention':mp.nstr(trio/tri,45),'numerical_not_interval':True}
  if angle==-1:
   k=s.zeros(N,1);k[0]=1
   for j in range(1,dd):k[j*dd+j]=ee
   Pi=k*k.T/(1+aa*xx);assert zero(Pi*Pi-Pi) and s.trace(Pi)==1
   qk=s.factor(s.trace(Pi*SO));pk=s.factor(s.trace(Pi*RO))
   assert qk==(1-th)*xx/(qq*(1+aa*xx))
   assert pk-qk==4*th*aa*xx/((N-1)*qq*(1+aa*xx))
   pm,qm=mp.mpf(str(pk)),mp.mpf(str(qk));db=pm*mp.log(pm/qm)+(1-pm)*mp.log((1-pm)/(1-qm))
   rev=qm*mp.log(qm/pm)+(1-qm)*mp.log((1-qm)/(1-pm))
   assert 0<db<dout
   classical_end=s.factor(ll+(1-ll)*s.trace(Pi*B))
   rec.update({'kernel_projector_exact':True,'p_exact':str(pk),'q_exact':str(qk),'binary_fraction':mp.nstr(db/dout,45),'reverse_fraction':mp.nstr(rev/dout,45),'quantum_input_denominator_retention':mp.nstr(db/din,45),'classical_affine_extrapolation_at_1':str(classical_end),'false_global_classical_channel':classical_end<0})
  rows.append(rec)
 # A new rational Bell bound test checks all directions in sum-zero subspace, not sampled z.
 for nn,la,r in [(5,-s.Rational(1,4),[s.Rational(7,10)]+[s.Rational(3,40)]*4),(5,s.Rational(2,3),[s.Rational(49,100)]*2+[s.Rational(1,150)]*3),(7,-s.Rational(1,12),[s.Rational(1,7)]*7)]:
  cc=(1-la)/nn;bound=la*la/(la+2*cc);Q=s.zeros(nn,nn-1)
  for j in range(nn-1):Q[j,j]=1;Q[nn-1,j]=-1
  F=Q.T*s.diag(*[bound/ri-la*la/(la*ri+cc) for ri in r])*Q
  assert F.is_positive_semidefinite
  rows.append({'name':'new_full_classical_tangent_form','n':nn,'lambda':str(la),'r':list(map(str,r)),'bound':str(bound),'positive_semidefinite_exact':True})
 # Exact local Doeblin certificate and a distinct-weight Pauli rational identity.
 vv=s.Matrix([1,0,0,-1]);G=2*s.eye(4)/3-vv*vv.T/3;Y=vv*vv.T
 assert zero(pt(Y,2)-s.eye(2)) and s.trace(G*Y)==0 and G.is_positive_semidefinite
 w=[s.Rational(1,10),s.Rational(1,5),s.Rational(3,10),s.Rational(2,5)];A=w[0]+w[3];B=w[1]+w[2];uu=w[0]-w[3];vvv=w[1]-w[2];U=uu*uu/A;Vv=vvv*vvv/B;k0=1-U-Vv
 value=s.factor(U+Vv+(A-B-U+Vv)**2/k0);assert value==1-16/sum(1/z for z in w)
 rows.append({'name':'core_certificates','Doeblin_alpha_zero_ordinary_trace_one_third':True,'Pauli_weights':list(map(str,w)),'exact_harmonic_value':str(value)})
 put('OWN1084.json',{'all_passed':True,'precision_digits':85,'records':rows,'proof_limit':'Finite controls do not replace the analytical reconstruction; shared environment and prior knowledge, no independence claim.'})
 print('All own symbolic, exact ambient geometry and85-digit full-matrix controls passed.')
except Exception as ex:
 put('OWN_FAILURE1084.json',{'error':repr(ex),'traceback':traceback.format_exc(),'completed':rows});raise

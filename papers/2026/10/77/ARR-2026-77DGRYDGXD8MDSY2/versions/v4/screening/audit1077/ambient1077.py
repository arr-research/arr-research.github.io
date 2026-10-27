from pathlib import Path
import sympy as s,mpmath as mp,json,traceback
P=Path(__file__).parent;mp.mp.dps=100;rows=[]
def zero(m):return all(s.simplify(x)==0 for x in m)
def val(x):return mp.mpf(str(s.N(x,110)))
def mm(M):return mp.matrix([[val(M[i,j]) for j in range(M.cols)] for i in range(M.rows)])
def tr(M):return sum(M[j,j] for j in range(M.rows))
def logm(M):
 ev,V=mp.eigh(M);assert min(ev)>0;return V*mp.diag([mp.log(v) for v in ev])*V.T
def kl(p,q):return p*mp.log(p/q)+(1-p)*mp.log((1-p)/(1-q))
try:
 for d,t,beta in [(2,s.Rational(1,4),4),(3,s.Rational(1),2),(4,s.Rational(1,4),4),(5,s.Rational(1),2)]:
  n=d*d;a=d-1;x=t/d;e=s.sqrt(x);q=a+x;delta=s.Rational(1,d**beta);th=1-delta;lam=-s.Rational(1,n-1);p=lam*th
  v=s.zeros(n,1);v[0]=e;u=s.zeros(n,1);v0=s.zeros(n,1);v0[0]=1
  for j in range(1,d):v[j*d+j]=1;u[j*d+j]=1/s.sqrt(a)
  pure=v*v.T/q;r=s.diag(x,*([1]*a))/q;B=s.kronecker_product(s.eye(d)/d,r);S=delta*B+th*pure;U=s.kronecker_product(s.diag(1,*([-1]*a)),s.eye(d));rho=U*S*U
  So=lam*S+(1-lam)*B;Ro=lam*rho+(1-lam)*B;Q=u*u.T+v0*v0.T
  Aa=s.simplify((u.T*So*u)[0]);Cc=s.simplify((v0.T*So*v0)[0]);bb=s.simplify((u.T*So*v0)[0]);g=s.sqrt((Aa-Cc)**2+4*bb**2);ell=(Aa+Cc-g)/2;high=(Aa+Cc+g)/2
  # Eigenvector construction, distinct from(hQ-W)/(h-l) used by1073.
  w=-bb*u+(Aa-ell)*v0;Pi=s.simplify(w*w.T/(w.T*w)[0]);assert zero(Pi*Pi-Pi) and zero(Pi-Pi.T) and s.simplify(s.trace(Pi)-1)==0
  assert zero(So*Pi-ell*Pi) and zero(Pi-Q*Pi*Q)
  q0=s.simplify(s.trace(Pi*So));p0=s.simplify(s.trace(Pi*Ro));assert s.simplify(q0-ell)==0 and s.simplify(p0-q0-4*bb**2/g)==0
  assert s.simplify(s.trace((s.eye(n)-Pi)*So)-(1-q0))==0 and s.simplify(s.trace((s.eye(n)-Pi)*Ro)-(1-p0))==0
  kin=s.sqrt(a*x)*u+v0;Pk=kin*kin.T/(1+a*x);qk=s.simplify(s.trace(Pk*So));pk=s.simplify(s.trace(Pk*Ro));assert s.simplify(qk-delta*x/(q*(1+a*x)))==0 and s.simplify(pk-qk-4*th*a*x/((n-1)*q*(1+a*x)))==0
  qs=s.simplify(s.trace(Pi*S));ps=s.simplify(s.trace(Pi*rho));rb=s.simplify(s.trace(Pi*B));aff=s.simplify(lam+(1-lam)*rb)
  assert s.simplify(q0-lam*qs-(1-lam)*rb)==0 and s.simplify(p0-lam*ps-(1-lam)*rb)==0
  si,ri,so,ro=map(mm,[S,rho,So,Ro]);Dout=tr(ro*(logm(ro)-logm(so)));Din=tr(ri*(logm(ri)-logm(si)));db=kl(val(p0),val(q0));dbin=kl(val(ps),val(qs));T=s.trace(Q*So)
  assert 0<val(q0)<val(p0)<1 and db>0 and db<=Dout and dbin>0
  assert abs(Dout/(4*val(bb**2)*(mp.log(val(high))-mp.log(val(ell)))/val(g))-1)<mp.mpf('1e-75')
  assert val(aff)<0
  wrong=kl(val(p0/T),val(q0/T));reverse=kl(val(q0),val(p0));assert val(high/g)>1
  rows.append({'d':d,'t':str(t),'beta':beta,'full_ambient_dimension':n,'projector_eigenvector_construction':True,'p0_exact':str(p0),'q0_exact':str(q0),'input_p_measured':str(ps),'input_q_measured':str(qs),'complement_mass_exact':True,'endpoint_kernel_probabilities_exact':[str(pk),str(qk)],'quantum_Dinput':str(Din),'quantum_Doutput':str(Dout),'binary_Doutput':str(db),'fraction_output':str(db/Dout),'measured_output_over_quantum_input':str(db/Din),'classical_input_D':str(dbin),'different_measured_output_over_measured_input':str(db/dbin),'negative_affine_binary_transition_entry':str(val(aff)),'block_mass':str(T),'unweighted_conditional_D_over_quantum_output':str(wrong/Dout),'reverse_D_over_quantum_output':str(reverse/Dout),'wrong_full_identity_outside_eigenvalue':str(val(high/g))})
  print(d,'ambient identities and denominator falsifier passed',flush=True)
 (P/'AMBIENT1077.json').write_text(json.dumps({'method':'Full matrices first; eigenvector projector, exact complements/probabilities;100digit ambient matrix logarithms. Own control, shared mathematical context.','cases':rows},indent=2)+'\n',encoding='utf-8')
except Exception as ex:
 (P/'AMBIENT_FAILURE1077.json').write_text(json.dumps({'error':repr(ex),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise

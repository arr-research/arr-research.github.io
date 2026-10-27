from pathlib import Path
import sympy as s,mpmath as m,json,traceback
P=Path(__file__).resolve().parent;m.mp.dps=100;rows=[]
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf-8')
def zm(A):return all(s.simplify(x)==0 for x in A)
def mm(A):return m.matrix([[m.mpc(str(s.re(x).evalf(110)),str(s.im(x).evalf(110))) for x in A.row(i)] for i in range(A.rows)])
def tr(A):return sum(A[i,i] for i in range(A.rows))
def logmat(A):
 ev,V=m.eighe(A);assert min(ev)>0
 return V*m.diag([m.log(x) for x in ev])*V.H
def rel(A,B):return m.re(tr(A*(logmat(A)-logmat(B))))
def err(a,b):return abs(a-b)/max(1,abs(a),abs(b))
def rotate(n):
 V=s.eye(n);V[0,0]=V[1,1]=s.Rational(3,5);V[0,1]=V[1,0]=4*s.I/5;assert zm(V.H*V-s.eye(n));return V
try:
 # General rational identities, without numerical optimizers.
 n,k,al,be,de,ep=s.symbols('n k alpha beta delta epsilon',positive=True)
 ap=(al+n*(n-2)*ep)/(n-1)**2;c2=al*be*(1-de)
 assert s.factor(ap*be-c2/(n-1)**2-be*(al*de+n*(n-2)*ep)/(n-1)**2)==0
 x=s.symbols('x',positive=True)
 F=2*x/(1+2*x);assert s.limit(F,x,1)==s.Rational(2,3) and s.simplify(s.Rational(2,3)-F-2*(1-x)/(3*(2*x+1)))==0
 rows.append({'name':'general_determinant_and_boundary_scalar','all_exact':True,'binary_Z_channel_sup':'2/3 approached at x=1, not attained for faithful x'})
 # Complex operator pencils, including zeros: verify whole operator inequality.
 A=s.Matrix([[2,s.Rational(1,3)+s.I/5],[s.Rational(1,3)-s.I/5,1]])
 B=s.Matrix([[1,-s.I/4],[s.I/4,3]])
 assert A.is_positive_definite and B.is_positive_definite and not zm(A*B-B*A)
 for name,aa,bb,cap in [('erasure',[s.Rational(2,5),0,s.Rational(3,5)],[0,s.Rational(2,5),s.Rational(3,5)],s.Rational(2,5)),('Z',[1,0],[s.Rational(1,3),s.Rational(2,3)],s.Rational(2,3)),('asymmetric',[s.Rational(4,5),s.Rational(1,5)],[s.Rational(1,5),s.Rational(4,5)],s.Rational(9,25))]:
  gap=cap*(A.inv()+B.inv())
  for a,b in zip(aa,bb):gap-=(a-b)**2*(a*A+b*B).inv()
  gap=gap.applyfunc(s.simplify);assert zm(gap-gap.H)
  minors=[s.simplify(gap[0,0]),s.simplify(gap[1,1]),s.factor(gap.det())];assert all(v>=0 for v in minors)
  rows.append({'name':'complex_full_operator_bound','channel':name,'cap':str(cap),'all_principal_minors':list(map(str,minors)),'equality_preserved':zm(gap)})
 # Exact simplex marginal/output for different n, including both stochastic endpoints.
 for nn,xi,la in [(2,s.Rational(2,9),-1),(3,s.Rational(2,7),-s.Rational(1,2)),(4,s.Rational(1,11),s.Rational(2,5)),(5,s.Rational(3,50),-s.Rational(1,8))]:
  V=rotate(nn);u=s.ones(nn,1);F0=u*u.T/nn;P0=s.eye(nn)-F0
  bases=[];ds=[]
  for j in range(nn):
   vv=s.eye(nn)[:,j]-u/nn;b=(1-xi)*vv*vv.T/(nn-1)+xi*s.eye(nn)/nn**2;z=u*vv.T+vv*u.T
   bases.append(V*b*V.H);ds.append(V*z*V.H)
  ref=sum(bases,s.zeros(nn));assert zm(ref-V*((1-xi)*P0/(nn-1)+xi*s.eye(nn)/nn)*V.H) and zm(sum(ds,s.zeros(nn)))
  aa=(1-xi)/nn+xi/nn**2;bb=xi/nn**2;ao=(1-xi)*(1+(nn-2)*la)/(nn*(nn-1))+bb
  ratio=s.factor(la**2*(aa+bb)/(ao+bb));upper=s.factor((nn-1)*la**2/(1+(nn-2)*la))
  for j in range(nn):
   O=la*bases[j]+(1-la)*ref/nn
   dsm=mm(ds[j]);ev,W=m.eighe(mm(bases[j]));T=W.H*dsm*W;gin=sum(2*abs(T[a,b])**2/(ev[a]+ev[b]) for a in range(nn) for b in range(nn))
   ev,W=m.eighe(mm(O));T=W.H*(la*dsm)*W;gout=sum(2*abs(T[a,b])**2/(ev[a]+ev[b]) for a in range(nn) for b in range(nn))
   assert err(gout/gin,m.mpf(str(ratio)))<m.mpf('1e-85')
  assert ratio<=upper
  rows.append({'name':'new_simplex_complex_cases','n':nn,'xi':str(xi),'lambda':str(la),'ratio_exact':str(ratio),'H_exact':str(upper),'marginal_and_zero_sum_exact':True,'SLD_full_block_numeric_match':True})
 # Full ambient logarithms and actual conditional effect, different finite pairs.
 for nn,kk in [(3,7),(4,9),(5,10)]:
  nnq=s.Integer(nn);beta=1/(4*nnq*kk);delta=s.Rational(1,2)**kk;epsilon=beta*delta;alpha=1/nnq-(nnq-2)*epsilon-beta;cc=s.sqrt(alpha*beta*(1-delta))
  V=rotate(nn);u=s.ones(nn,1);f=u/s.sqrt(nn);F=V*(f*f.T)*V.H;PP=s.eye(nn)-F
  plus=[];minus=[]
  for j in range(nn):
   psi=V*(s.sqrt(nnq/(nnq-1))*(s.eye(nn)[:,j]-u/nnq));ff=V*f;Pi=psi*psi.H
   base=alpha*Pi+epsilon*(PP-Pi)+beta*F;coh=cc*(psi*ff.H+ff*psi.H)
   plus.append(base+coh);minus.append(base-coh)
  rp=sum(plus,s.zeros(nn));rm=sum(minus,s.zeros(nn));assert zm(rp-rm) and s.simplify(s.trace(rp))==1
  A=s.diag(*plus);B=s.diag(*minus)
  OA=s.diag(*[(rp-b)/(nn-1) for b in plus]);OB=s.diag(*[(rm-b)/(nn-1) for b in minus])
  MA,MB,MOA,MOB=map(mm,[A,B,OA,OB]);di=rel(MA,MB);do=rel(MOA,MOB)
  # E from complete reference blocks in physical complex coordinates, no plane eigenvector formula.
  E=m.zeros(nn*nn)
  for j in range(nn):
   ev,W=m.eighe(MOB[j*nn:(j+1)*nn,j*nn:(j+1)*nn]);w=W[:,0];E[j*nn:(j+1)*nn,j*nn:(j+1)*nn]=w*w.H
  assert m.norm(E*E-E)<m.mpf('1e-85')
  p=m.re(tr(E*MOA));q=m.re(tr(E*MOB));db=p*m.log(p/q)+(1-p)*m.log((1-p)/(1-q));rev=q*m.log(q/p)+(1-q)*m.log((1-q)/(1-p))
  aa=m.mpf(str(alpha));bb=m.mpf(str(beta));epm=m.mpf(str(epsilon));c2m=m.mpf(str(s.factor(cc**2)));lam=-m.mpf(1)/(nn-1);apo=(aa+nn*(nn-2)*epm)/(nn-1)**2
  def spec(a,b,c2):
   gap=m.sqrt((a-b)**2+4*c2);hi=(a+b+gap)/2;lo=(a*b-c2)/hi;return hi,lo,gap
  hi,li,gi=spec(aa,bb,c2m);ho,lo,go=spec(apo,bb,lam**2*c2m)
  diref=4*nn*c2m*m.log(hi/li)/gi;doref=4*nn*lam**2*c2m*m.log(ho/lo)/go
  pref=nn*(lo+4*lam**2*c2m/go);qref=nn*lo
  assert max(err(di,diref),err(do,doref),err(p,pref),err(q,qref))<m.mpf('1e-85')
  assert 0<db<do<di
  EL=mm(s.diag(*([F]*nn)));pl=m.re(tr(EL*MOA));ql=m.re(tr(EL*MOB));assert err(pl,ql)<m.mpf('1e-90')
  rows.append({'name':'new_full_ambient_complex','n':nn,'k':kk,'dimension':nn*nn,'Di':m.nstr(di,50),'Do':m.nstr(do,50),'Db':m.nstr(db,50),'retention':m.nstr(db/di,50),'reverse_ratio':m.nstr(rev/di,50),'p':m.nstr(p,50),'q':m.nstr(q,50),'limit_effect_gives_zero':True,'quantum_input_denominator':True,'numeric_not_interval':True})
 # No use of exponential scale is hidden in the theorem: a different analytic path.
 rows.append({'name':'analytic_adverse_polynomial_delta','n':'fixed >=3','beta':'1/(4 n k)','delta':'k^(-s), s>0 fixed','epsilon':'beta delta','Di_leading':'(s+1) log(k)/k','Db_leading':'s log(k)/k','binary_retention_limit':'s/(s+1), not1','status':'Analytical exponent reconstruction, no new numerical proof claim.'})
 put('OWN1128.json',{'all_passed':True,'records':rows,'precision_digits':100,'scope':'Fixed symbolic/exact controls and highprecision ambient checks; no optimizer, no universal numerical proof, no independent model/library claim.'})
 print('Own exact identities, complex operator gaps and ambient100digit controls passed.')
except Exception as ex:
 put('OWN-FAILURE1128.json',{'error':repr(ex),'traceback':traceback.format_exc(),'completed':rows});raise

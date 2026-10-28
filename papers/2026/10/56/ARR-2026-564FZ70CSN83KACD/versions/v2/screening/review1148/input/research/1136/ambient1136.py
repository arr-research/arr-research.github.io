from pathlib import Path
from fractions import Fraction as F
import mpmath as mp,json,traceback
P=Path(__file__).parent;mp.mp.dps=160
def v(x):
 x=F(x);return mp.mpf(x.numerator)/x.denominator
def tr(a):return mp.re(sum(a[i,i] for i in range(a.rows)))
def norm(a):return mp.norm(a)
def logarithm(a):
 w,U=mp.eighe(a);assert w[0]>0
 return U*mp.diag([mp.log(x) for x in w])*U.H
def D(a,b):return tr(a*(logarithm(a)-logarithm(b)))
def KL(p,q):
 if p==q:return mp.mpf(0)
 return p*mp.log(p/q)+(1-p)*mp.log((1-p)/(1-q))
def direct(blocks):
 d=blocks[0].rows;M=mp.zeros(d*len(blocks))
 for j,b in enumerate(blocks):
  for r in range(d):
   for c in range(d):M[j*d+r,j*d+c]=b[r,c]
 return M
base3=[['0','1/3','2/5'],['3/4','0','3/5'],['1/4','2/3','0']]
cycle4=[[F(int((j-i)%4 in [1,3]),2) for i in range(4)] for j in range(4)]
ex16=[[F(int(i!=j),15) for i in range(16)] for j in range(16)]
h=F(1,10**40)
ill=[[0,h,1-h],[1-h,0,h],[h,1-h,0]]
flag=[[F(x)*F(9,10) for x in row] for row in base3]+[[F(1,10)]*3]
positive=[[F(x)*F(9,10)+F(1,30) for x in row] for row in base3]
cases=[('binary_identity_zero_row',[[1,0],[0,1],[0,0]],2,1),('binary_erasure',[[F(4,5),0],[0,F(4,5)],[F(1,5)]*2],64,1),('asymmetric3_complex_full',base3,64,1),('asymmetric3_tiny_weight',ill,64,1),('flagged_replacement',flag,64,1),('all_fullsupport',positive,64,1),('cycle4_original',cycle4,64,1),('cycle4_slow_regularizer',cycle4,128,F(1,2)),('cycle4_fast_regularizer',cycle4,64,2),('exclusion16_smallk_wrong_max_overlap',ex16,16,1)]
rows=[]
try:
 for name,strings,k,power in cases:
  n=len(strings[0]);K=[[v(x) for x in row] for row in strings]
  assert all(sum(F(row[i]) for row in strings)==1 for i in range(n))
  beta=mp.mpf(1)/(4*n*k);delta=mp.mpf(2)**(-k);eps=beta*delta**v(power);alpha=mp.mpf(1)/n-(n-2)*eps-beta;c=mp.sqrt(alpha*beta*(1-delta))
  U=mp.eye(n);U[0,0]=U[1,1]=mp.mpf(3)/5;U[0,1]=U[1,0]=mp.j*4/5
  f=U*mp.matrix([1/mp.sqrt(n)]*n);FF=f*f.H;PP=mp.eye(n)-FF;plus=[];minus=[]
  for i in range(n):
   e=mp.matrix(n,1);e[i]=1;psi=U*(mp.sqrt(mp.mpf(n)/(n-1))*(e-mp.matrix([mp.mpf(1)/n]*n)));Pi=psi*psi.H
   a=alpha*Pi+eps*(PP-Pi)+beta*FF;o=c*(psi*f.H+f*psi.H)
   plus.append(a+o);minus.append(a-o)
  assert norm(sum(plus,mp.zeros(n))-sum(minus,mp.zeros(n)))<mp.mpf('1e-145')
  assert abs(sum(tr(a) for a in plus)-1)<mp.mpf('1e-145')
  di=sum(D(a,b) for a,b in zip(plus,minus));do=mp.mpf(0);pm=qm=pf=qf=mp.mpf(0);detail=[];outp=[];outm=[];effects=[]
  hasproper=any(any(w) and min(w)==0 for w in K)
  for j,w in enumerate(K):
   if not any(w):
    detail.append({'row':j,'zero_row_removed':True});continue
   a=sum((w[i]*plus[i] for i in range(n)),mp.zeros(n));b=sum((w[i]*minus[i] for i in range(n)),mp.zeros(n));outp.append(a);outm.append(b)
   do+=D(a,b);ev,V=mp.eighe(b);overlaps=[abs((f.H*V[:,i])[0])**2 for i in range(n)];jf=max(range(n),key=lambda i:overlaps[i])
   if min(w)>0 and hasproper:
    effects.append(mp.zeros(n));detail.append({'row':j,'fullsupport_effect_zero':True});continue
   Em=V[:,0]*V[:,0].H;Ef=V[:,jf]*V[:,jf].H;effects.append(Em)
   qm+=tr(Em*b);pm+=tr(Em*a);qf+=tr(Ef*b);pf+=tr(Ef*a)
   r={'row':j,'minimum_index':0,'max_flag_overlap_index':jf,'min_flag_overlap':mp.nstr(overlaps[0],40),'max_flag_overlap':mp.nstr(overlaps[jf],40),'minimum_eigenvalue':mp.nstr(ev[0],40)}
   if min(w)==0 and power==1:
    C=c*c*(n-1)**2/(alpha-eps)**2;ratio=ev[0]/(beta*delta*sum(w));assert 1/(1+C)-mp.mpf('1e-90')<=ratio<=1+mp.mpf('1e-90');r['rational_bound_verified']=True
   detail.append(r)
  dm=KL(pm,qm);df=KL(pf,qf);tol=mp.mpf('1e-90')
  assert -tol<=dm<=do+tol and -tol<=df<=do+tol and do<=di+tol
  Bdob=sum(min(w) for w in K);assert do<=(1-Bdob)*di+tol
  row={'label':name,'n':n,'k':k,'epsilon_exponent':str(power),'channel':[[str(F(x)) for x in r] for r in strings],'Dinput':mp.nstr(di,60),'Doutput':mp.nstr(do,60),'binary_minimum_retention':mp.nstr(dm/di,60),'binary_max_overlap_retention':mp.nstr(df/di,60),'p_min':mp.nstr(pm,60),'q_min':mp.nstr(qm,60),'d':mp.nstr(Bdob,40),'all_DPI_pass':True,'rows':detail}
  if name=='asymmetric3_complex_full':
   RP,RM=direct(plus),direct(minus);OP,OM=direct(outp),direct(outm);E=direct(effects)
   errors=[abs(D(RP,RM)-di),abs(D(OP,OM)-do),norm(E*E-E),abs(tr(E*OP)-pm),abs(tr(E*OM)-qm)]
   assert max(errors)<mp.mpf('1e-110');row['full9x9_errors']=[mp.nstr(x,20) for x in errors]
  rows.append(row)
 (P/'AMBIENT1136.json').write_text(json.dumps({'precision':160,'all_complex_reference_rotation':True,'cases':rows,'finite_diagnostics_not_interval_proofs':True},indent=2)+'\n',encoding='utf-8')
 print(json.dumps([{'label':r['label'],'minimum_retention':r['binary_minimum_retention'][:18],'max_overlap_retention':r['binary_max_overlap_retention'][:18]} for r in rows]))
except Exception as e:
 (P/'AMBIENT_FAILURE1136.json').write_text(json.dumps({'exception':repr(e),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise

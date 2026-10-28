"""Predeclared, bounded falsification controls; own assembly, shared standard libraries.
No optimization, no universal numerical proof, no inherited interval primitives.
"""
from pathlib import Path
import json,datetime,traceback
import mpmath as mp
import sympy as sp
R=Path(__file__).resolve().parent
mp.mp.dps=120
tol=mp.mpf('1e-95')
rows=[]
def dump(name,obj): (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sm(m): return m.applyfunc(sp.simplify)
def outer(v): return v*v.conjugate().T/(v.conjugate().T*v)[0]
def exact_case(label,taus):
 n=len(taus);d=taus[0].rows;u=sp.ones(n,1);psi=[sp.sqrt(sp.Rational(n,n-1))*(sp.eye(n)[:,i]-u/n) for i in range(n)]
 T=sum((sp.kronecker_product(v*v.T,t) for v,t in zip(psi,taus)),sp.zeros(n*d))
 Z=sum((sp.kronecker_product(v,t) for v,t in zip(psi,taus)),sp.zeros(n*d,d));S=sum(taus,sp.zeros(d))
 Y,params=T.gauss_jordan_solve(Z);Y=Y.subs({x:0 for x in params});defect=sm(S-Z.conjugate().T*Y)
 assert sm(T*Y-Z)==sp.zeros(n*d,d)
 expected_zero=label!='common_line'
 assert (defect==sp.zeros(d))==expected_zero
 row={'kind':'exact_geometry','case':label,'n':n,'d':d,'ranks':[t.rank() for t in taus],
      'rank_T':T.rank(),'kernel_T_on_PR':(n-1)*d-T.rank(),'sum_prepared_ranks':sum(t.rank() for t in taus),
      'range_inclusion':True,'S_minus_Zstar_solution':str(defect),'zero_defect_expected':expected_zero,'pass':True}
 rows.append(row)
def mm(s):return mp.matrix([[mp.mpc(str(sp.re(x).evalf(125)),str(sp.im(x).evalf(125))) for x in list(s.row(i))] for i in range(s.rows)])
def tr(a):return sum(a[i,i] for i in range(a.rows))
def norm(a):return max(abs(x) for x in a)
def kron(a,b):return mp.matrix(a.rows*b.rows,a.cols*b.cols,lambda i,j:a[i//b.rows,j//b.cols]*b[i%b.rows,j%b.cols])
def diag(vals):
 o=mp.zeros(len(vals))
 for i,v in enumerate(vals):o[i,i]=v
 return o
def herm(a):return (a+a.H)/2
def logm(a):
 vals,U=mp.eighe(herm(a));assert min(vals)>0
 return U*diag([mp.log(x) for x in vals])*U.H,min(vals)
def rel(a,b):
 la,_=logm(a);lb,_=logm(b);z=tr(a*(la-lb));assert abs(mp.im(z))<tol
 return mp.re(z)
def real(z):assert abs(mp.im(z))<tol;return mp.re(z)
def bern(p,q):return p*mp.log(p/q)+(1-p)*mp.log((1-p)/(1-q))
def num_case(label,taus,k,epsilon_mode='sealed',common_weight=None):
 n=len(taus);d=taus[0].rows;taus=list(map(mm,taus));I=mp.eye(n);f=mp.ones(n,1)/mp.sqrt(n);F=f*f.H;P=I-F
 beta=1/mp.mpf(4*n*k);delta=mp.power(2,-k);eps=beta*delta if epsilon_mode=='sealed' else beta/k
 alpha=1/mp.mpf(n)-(n-2)*eps-beta;c=mp.sqrt(alpha*beta*(1-delta))
 psi=[mp.sqrt(mp.mpf(n)/(n-1))*(I[:,i]-f/mp.sqrt(n)) for i in range(n)]
 plus=[];minus=[]
 for v in psi:
  base=alpha*v*v.H+eps*(P-v*v.H)+beta*F;cross=c*(v*f.H+f*v.H)
  plus.append(base+cross);minus.append(base-cross)
 assert norm(sum(plus,mp.zeros(n))-sum(minus,mp.zeros(n)))<tol
 assert max(abs(tr(x)-1/mp.mpf(n)) for x in plus+minus)<tol
 Mp=sum((kron(s,t) for s,t in zip(plus,taus)),mp.zeros(n*d));Mm=sum((kron(s,t) for s,t in zip(minus,taus)),mp.zeros(n*d))
 U=mp.zeros(n)
 for j in range(1,n):
  for i in range(j):U[i,j-1]=1/mp.sqrt(j*(j+1))
  U[j,j-1]=-j/mp.sqrt(j*(j+1))
 for i in range(n):U[i,n-1]=f[i]
 K=kron(U,mp.eye(d));pm=K.H*Mp*K;mn=K.H*Mm*K;cut=(n-1)*d
 A=mn[:cut,:cut];Z=-mn[:cut,cut:]/c;S=mn[cut:,cut:]/beta
 X=c*A**-1*Z;H=mp.zeros(n*d,d)
 H[:cut,:]=X;H[cut:,:]=mp.eye(d)
 C=(mp.eye(d)+X.H*X)**-1;E0=H*C*H.H;E=K*E0*K.H
 assert norm(E*E-E)<tol and norm(E-E.H)<tol
 p=real(tr(E*Mp));q=real(tr(E*Mm));assert 0<q<p<1
 Be=Z.H*A**-1*Z;Q=beta*S-c*c*Be
 assert abs(q-real(tr(C*Q)))<tol and abs(p-q-4*c*c*real(tr(C*Be)))<tol
 Di=sum(rel(x,y) for x,y in zip(plus,minus));Do=rel(Mp,Mm);Db=bern(p,q)
 assert Db<=Do+tol and Do<=Di+tol
 hi=(alpha+beta+mp.sqrt((alpha-beta)**2+4*c*c))/2;lo=alpha*beta*delta/hi
 formula=4*n*c*c*mp.log(hi/lo)/(hi-lo)
 assert abs(Di-formula)<tol
 fixed=kron(F,mp.eye(d));fixed_p=real(tr(fixed*Mp));fixed_q=real(tr(fixed*Mm));assert abs(fixed_p-fixed_q)<tol
 if common_weight is not None:assert Do<=(1-mp.mpf(common_weight))*Di+tol
 # Numerical diagnostic of the graph-effect partial transpose, no separability theorem from positive eigenvalues.
 pt=mp.matrix(n*d,n*d)
 for i in range(n):
  for j in range(n):
   for a in range(d):
    for b in range(d):pt[i*d+a,j*d+b]=E[i*d+b,j*d+a]
 mineig=min(mp.eighe(herm(pt),eigvals_only=True))
 row={'kind':'ambient_high_precision','case':label,'n':n,'d':d,'k':k,'epsilon_mode':epsilon_mode,
      'Di':mp.nstr(Di,60),'Do':mp.nstr(Do,60),'Db':mp.nstr(Db,60),'Db_over_Di':mp.nstr(Db/Di,60),
      'Do_over_Di':mp.nstr(Do/Di,60),'p':mp.nstr(p,60),'q':mp.nstr(q,60),
      'reverse_binary_ratio':mp.nstr(bern(q,p)/Di,40),'fixed_F_probability_difference':mp.nstr(fixed_p-fixed_q,10),
      'projector_max_entry_residual':mp.nstr(norm(E*E-E),10),'PT_min_eigenvalue_diagnostic':mp.nstr(mineig,40),
      'A_inverse_max_entry':mp.nstr(norm(A**-1),20),'A_inverse_Z_max_entry':mp.nstr(norm(A**-1*Z),20),
      'common_component_lower_bound':common_weight,'pass':True}
 rows.append(row)
def main():
 e0=sp.Matrix([1,0]);e1=sp.Matrix([0,1]);complex_pair=[outer(e0),outer(sp.Matrix([1,sp.I*sp.Rational(2,3)]))]
 mixed_kernel=[outer(e0),sp.eye(2)/2,outer(sp.Matrix([1,sp.I])),outer(sp.Matrix([1,1]))]
 common=[sp.diag(sp.Rational(1,3),sp.Rational(2,3),0),sp.diag(sp.Rational(1,3),0,sp.Rational(2,3)),
         sp.diag(sp.Rational(1,3),0,0)+sp.Rational(2,3)*outer(sp.Matrix([0,1,sp.I]))]
 duplicate=[outer(e0),outer(e0),outer(e1)]
 plan={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'dps':120,'tolerance':str(tol),
       'exact_cases':['complex_pair','mixed_kernel','duplicate','common_line'],
       'ambient_cases':[['complex_pair',k] for k in [8,16,32]]+[['mixed_kernel',k] for k in [8,16,32]]+[['common_line',32],['mixed_kernel_alternate_epsilon',32]],
       'scope':'Own direct tensor assembly; standard sympy/mpmath reused. No optimizer, no independent arithmetic claim, no universal numerical proof.'}
 dump('OWN-PLAN1168.json',plan)
 for label,taus in [('complex_pair',complex_pair),('mixed_kernel',mixed_kernel),('duplicate',duplicate),('common_line',common)]:exact_case(label,taus)
 for k in [8,16,32]:num_case('complex_pair',complex_pair,k)
 for k in [8,16,32]:num_case('mixed_kernel',mixed_kernel,k)
 num_case('common_line',common,32,common_weight='0.3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333')
 num_case('mixed_kernel_alternate_epsilon',mixed_kernel,32,epsilon_mode='beta_over_k')
 dump('OWN1168.json',{'status':'pass','rows':rows,'controls':len(rows),'scope':plan['scope']})
 print(json.dumps({'status':'pass','controls':len(rows),'retentions':[{key:r[key] for key in ['case','k','Db_over_Di','Do_over_Di']} for r in rows if r['kind']=='ambient_high_precision']},indent=2))
if __name__=='__main__':
 try:main()
 except Exception as e:
  dump('OWN-FAILURE1168.json',{'error':repr(e),'traceback':traceback.format_exc(),'completed_rows':rows});raise

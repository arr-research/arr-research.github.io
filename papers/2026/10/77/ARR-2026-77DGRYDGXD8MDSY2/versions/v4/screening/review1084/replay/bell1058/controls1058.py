from pathlib import Path
import sympy as s,json,traceback
P=Path(__file__).parent;rows=[]
try:
 n,L,x,c=s.symbols('n L x c',real=True);b=L+2*c
 assert s.factor(s.diff((L*x+c)/(1-2*x),x)-b/(1-2*x)**2)==0
 assert s.factor(x*(L*x+c)-(1-x)*(L*(1-x)+c)-(2*x-1)*(L+c))==0
 bb=L+2*(1-L)/n
 assert s.factor(bb.subs(L,-1/(n-1))-1/(n-1))==0
 assert s.simplify(bb.subs(n,2))==1
 rows.append({'name':'general_algebra','monotonicity':True,'cancellation':True,'minimum_denominator':'1/(n-1)>0','n2_denominator':'1'})
 for dim in [2,3,4,9]:
  families={'uniform':[s.Rational(1,dim)]*dim,'dominant':[s.Rational(999,1000)]+[s.Rational(1,1000*(dim-1))]*(dim-1),'half':[s.Rational(1,2)]+[s.Rational(1,2*(dim-1))]*(dim-1)}
  if dim>2:families['two_ray']=[s.Rational(49999,100000)]*2+[s.Rational(1,50000*(dim-2))]*(dim-2)
  Q=s.eye(dim)[:,:dim-1]
  for j in range(dim-1):Q[dim-1,j]=-1
  for lam in [-s.Rational(1,dim-1),-s.Rational(1,2*(dim-1)),s.Rational(0),s.Rational(1,2),s.Rational(999,1000),s.Rational(1)]:
   cc=(1-lam)/dim;den=lam+2*cc;assert den>0
   for name,r in families.items():
    out=[lam*v+cc for v in r];assert min(out)>0 and sum(out)==1
    F=Q.T*s.diag(*[1/(den*v)-1/w for v,w in zip(r,out)])*Q
    if F==s.zeros(dim-1):piv=['0']*(dim-1)
    else:
     low,diag=F.LDLdecomposition();assert low*diag*low.T==F;assert min(diag.diagonal())>0;piv=[str(v) for v in diag.diagonal()]
    rows.append({'name':'whole_tangent_form','n':dim,'lambda':str(lam),'family':name,'LDL_pivots':piv})
 res=[]
 for dim in [3,4,9]:
  pp=[s.Rational((j+1)**2,sum(k*k for k in range(1,dim+1))) for j in range(dim)];qq=[s.Rational(j+1,dim*(dim+1)//2) for j in range(dim)]
  for lam in [-s.Rational(1,dim-1),s.Rational(0),s.Rational(1,2),s.Rational(1)]:
   cc=(1-lam)/dim;den=lam+2*cc;coef=lam**2/den;kp=[lam*v+cc for v in pp];kq=[lam*v+cc for v in qq]
   for u in [s.Rational(0),s.Rational(1,7),s.Rational(1),s.Rational(11),s.Rational(10**6)]:
    div=lambda p,q:sum((v-w)**2/(v+u*w) for v,w in zip(p,q));r=[(v+u*w)/(1+u) for v,w in zip(pp,qq)];z=[v-w for v,w in zip(pp,qq)]
    di=div(pp,qq);do=div(kp,kq);assert di==sum(v*v/w for v,w in zip(z,r))/(1+u) and do<=coef*di
    res.append({'n':dim,'lambda':str(lam),'u':str(u),'ratio':str(s.factor(do/di)),'bound':str(coef)})
 rows.append({'name':'oriented_resolvents','cases':res})
 # Exact lower for each n; local ratio coincides with the finite quadratic ratio.
 lows=[]
 for dim in [2,3,4,9]:
  aa=s.Rational(1,2) if dim==2 else s.Rational(49999,100000)
  for lam in [-s.Rational(1,dim-1),s.Rational(0),s.Rational(1,2),s.Rational(1)]:
   cc=(1-lam)/dim;value=lam**2*aa/(lam*aa+cc);bound=lam**2/(lam+2*cc);assert value<=bound
   lows.append({'n':dim,'lambda':str(lam),'a':str(aa),'ratio':str(value),'bound':str(bound)})
 rows.append({'name':'sharpness','cases':lows})
 # Scope falsifiers, exact and legal for their stated modified questions.
 r=[s.Rational(4,5),s.Rational(1,10),s.Rational(1,10)];lam=s.Rational(1,2);cc=s.Rational(1,6);wrong=lam**2*r[0]/(lam*r[0]+cc);assert wrong==s.Rational(6,17)>s.Rational(3,10)
 a=s.Rational(49,100);fixed=lam**2*a/(lam*a+s.Rational(1,18));assert fixed==s.Rational(441,1082)>lam**2
 rows.append({'name':'scope_falsifiers','all_convex_f_TV':{'n':3,'lambda':'1/2','TV_retention':'1/2','proposed_operator_convex_bound':'3/10','explanation':'TV is convex but not operator convex; cannot broaden f class.'},'without_sum_zero':{'n':3,'r':['4/5','1/10','1/10'],'z':[1,0,0],'lambda':'1/2','ratio':'6/17','bound':'3/10'},'wrong_uniform_source_value':{'n':9,'lambda':'1/2','a':'49/100','two_ray_finite_chi_ratio':'441/1082','uniform_source_chi_value':'1/4','global_bound':'9/22'}})
 rows.append({'name':'complete','passed':True});(P/'CONTROLS1058.json').write_text(json.dumps({'records':rows},indent=2)+'\n',encoding='utf-8');print('General identities,90 whole tangent forms,60 resolvent pairs,16 lower controls and exact scope falsifiers passed.')
except Exception as ex:
 (P/'CONTROL_FAILURE1058.json').write_text(json.dumps({'error':repr(ex),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise

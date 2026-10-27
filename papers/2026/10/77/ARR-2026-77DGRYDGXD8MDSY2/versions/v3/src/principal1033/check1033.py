from pathlib import Path
import sympy as s,json
P=Path(__file__).parent;d=s.symbols('d',integer=True,positive=True);a=d-1;e=s.symbols('e',positive=True);p=s.symbols('p',real=True);q=a+e*e;M=d*(2*d-1)/2
W=s.Matrix([[1+(d*a-1)*p,d*p*e*s.sqrt(a)],[d*p*e*s.sqrt(a),(2+(d-2)*p)*e*e]])/(2*d*q)
T=s.Matrix([[0,s.sqrt(a)],[s.sqrt(a),2*e]])
x,y,z=s.symbols('x y z');Y=s.Matrix([[x,y],[y,z]]);eq=W*Y+Y*W-2*T
sol=s.solve([eq[0,0],eq[0,1],eq[1,1]],[x,y,z]);G=s.factor(s.trace(T*Y.subs(sol)))
checks=dict(determinant=s.factor(W.det()-e**2*(1-p)*(1+(M-1)*p)/(2*d*d*q*q))==0,limit=s.factor(G.subs(e,0)-8*a*M/(1+(M-1)*p))==0)
assert all(checks.values());rows=[]
for n in [2,3,4]:
 aa=n-1;r=2*aa+1;N=n*r;ee=s.Rational(1,100);qq=aa+ee*ee;vec=[];bs=[]
 for i in [0,1]:
  v=s.zeros(N,1);b=s.zeros(N,1)
  for j in range(aa):v[((j+1) if i==0 else j)*r+(j if i==0 else aa+j)]=1
  center=(0 if i==0 else n-1)*r+2*aa;v[center]=ee;b[center]=1 if i==0 else -1
  vec.append(v);bs.append(b)
 sig=sum((v*v.T for v in vec),s.zeros(N))/(2*qq);D=sum((v*b.T+b*v.T for v,b in zip(vec,bs)),s.zeros(N))
 ptr=lambda A:s.Matrix(r,r,lambda i,j:sum(A[h*r+i,h*r+j] for h in range(n)))
 B=s.diag(*[ptr(sig) for _ in range(n)])/n;cap=s.Rational(n*(2*n-1),2)
 assert s.trace(sig)==1 and ptr(D)==s.zeros(r)
 gram=s.Matrix.hstack(*vec).T*B.inv()*s.Matrix.hstack(*vec)/(2*qq);assert gram==cap*s.eye(2)
 support=2*sig;assert support*support==support and (s.eye(N)-support)*D*(s.eye(N)-support)==s.zeros(N)
 assert s.factor(4*s.trace(D*D)-2*s.trace((support*D*support)**2)-16*qq)==0
 row=dict(d=n,R=r,joint_dimension=N,Gram=str(cap)+' I2',partial_trace_zero=True,support_form=str(16*qq),finite=[])
 if n>2:
  kappa=cap-s.Rational(1,2);theta=(kappa-1)/(cap-1)-s.Rational(1,100);t=s.Rational(1,10**8)
  sigt=(1-theta)*B+theta*sig;rho=sigt+t*D
  def positive(A):
   L,dd=A.LDLdecomposition(hermitian=False);assert L*dd*L.T==A
   assert all(dd[j,j]>0 for j in range(N));return min(dd[j,j] for j in range(N))
  pivots={k:str(positive(A)) for k,A in [('sigma',sigt),('rho',rho),('sigma_slack',kappa*B-sigt),('rho_slack',kappa*B-rho)]}
  unseen=set(range(N));blocks=[]
  while unseen:
   component={unseen.pop()};todo=list(component)
   while todo:
    i=todo.pop();nbr={j for j in unseen if sigt[i,j]!=0 or D[i,j]!=0};unseen-=nbr;component|=nbr;todo+=list(nbr)
   blocks.append(sorted(component))
  def form(A,Bb,Z):
   full=s.zeros(N)
   for ix in blocks:
    zz=Z.extract(ix,ix)
    if zz==s.zeros(len(ix)):continue
    u=s.symbols('u:'+str(len(ix)**2));yy=s.Matrix(len(ix),len(ix),u);al=A.extract(ix,ix);bl=Bb.extract(ix,ix)
    solution=next(iter(s.linsolve(list(al*yy+yy*bl-zz),u)));yy=s.Matrix(len(ix),len(ix),solution)
    for i,ii in enumerate(ix):
     for j,jj in enumerate(ix):full[ii,jj]=yy[i,j]
   assert A*full+full*Bb==Z
   return s.trace(Z*full)
  for lam in [-s.Rational(1,n*n-1),s.Rational(1,2)]:
   out=lambda A:lam*A+(1-lam)*B
   os=out(sigt);orr=out(rho);opivots=[str(positive(os)),str(positive(orr))]
   local=s.factor(form(os,os,lam*D)/form(sigt,sigt,D));tri=s.factor(form(orr,os,lam*t*D)/form(rho,sigt,t*D));upper=lam*lam*kappa/(1+lam*(kappa-1))
   assert local<=upper and tri<=upper
   old=s.Rational(n*(n+1),2);old_endpoint=lam*lam*old/(1+lam*(old-1))
   assert local>old_endpoint and tri>old_endpoint
   row['finite'].append(dict(lambda_=str(lam),kappa=str(kappa),theta=str(theta),t=str(t),e=str(ee),SLD=str(local),triangular=str(tri),upper=str(upper),prior1021_endpoint=str(old_endpoint),SLD_gap=str(local-old_endpoint),triangular_gap_positive=True,SLD_decimal=str(s.N(local,20)),minimum_LDL_pivots=pivots,output_minimum_LDL_pivots=opivots,full_ambient_Sylvester_residuals_zero=True))
 rows.append(row)
out=dict(scope='Exploratory principal-rich ranktwo candidate1033, not technically audited and not a manuscript score. Comparison is to the previously certified endpoint formula, not an upper on all old-family finite pairs.',symbolic=checks,aligned_SLD=str(G),limit=str(s.factor(G.subs(e,0))),matrices=rows,all_passed=True)
(P/'CHECK1033.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(symbolic=checks,dimensions=[2,3,4],rational_finite_pairs=4,all_passed=True)))

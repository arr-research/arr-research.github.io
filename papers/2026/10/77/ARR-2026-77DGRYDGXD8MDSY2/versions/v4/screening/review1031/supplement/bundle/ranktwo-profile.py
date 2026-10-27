from pathlib import Path
import sympy as s,json
P=Path(__file__).parent;d=s.symbols('d',positive=True,integer=True);e=s.symbols('e',positive=True);p=s.symbols('p',real=True);m=d-1;L=d*(d+1)/2
W=s.Matrix([[1+(d-1)*p,d*p*e*s.sqrt(m)],[d*p*e*s.sqrt(m),(2+(d*m-2)*p)*e*e]])/(2*d*(1+m*e*e))
T=s.Matrix([[0,s.sqrt(m)],[s.sqrt(m),2*e*m]])
x,y,z=s.symbols('x y z');Y=s.Matrix([[x,y],[y,z]]);eq=W*Y+Y*W-2*T
sol=s.solve([eq[0,0],eq[0,1],eq[1,1]],[x,y,z]);G=s.factor(s.trace(T*Y.subs(sol)));limit=s.factor(G.subs(e,0)/(8*m))
checks=dict(block_limit=s.factor(limit-L/(1+(L-1)*p))==0,block_det=s.factor(W.det()-2*e*e*(1-p)*(1+(L-1)*p)/(4*d*d*(1+m*e*e)**2))==0)
rows=[]
for n in [2,3,4]:
 r=n+1;N=n*r;ee=s.Rational(1,10);vec=[];bvec=[]
 for i in [0,1]:
  a=s.zeros(N,1);b=s.zeros(N,1);a[i*r+i]=1
  for k in range(1,n):a[((i+k)%n)*r+k+1]=ee;b[((i+k)%n)*r+k+1]=1 if i==0 else -1
  vec.append(a);bvec.append(b)
 sig=(vec[0]*vec[0].T+vec[1]*vec[1].T)/(2*(1+(n-1)*ee*ee))
 D=sum((b*a.T+a*b.T for a,b in zip(vec,bvec)),s.zeros(N))
 ptr=lambda a:s.Matrix(r,r,lambda i,j:sum(a[h*r+i,h*r+j] for h in range(n)))
 B=s.diag(*[ptr(sig) for _ in range(n)])/n
 gram=s.Matrix.hstack(*vec).T*B.inv()*s.Matrix.hstack(*vec)/(2*(1+(n-1)*ee*ee))
 cap=s.Rational(n*(n+1),2)
 assert gram==cap*s.eye(2) and ptr(D)==s.zeros(r)
 support=sum((a*a.T/(1+(n-1)*ee*ee) for a in vec),s.zeros(N));assert (s.eye(N)-support)*D*(s.eye(N)-support)==s.zeros(N)
 row=dict(d=n,R=r,whitened_gram=str(cap)+' I2',partial_trace_zero=True,kernel_tangent_zero=True)
 if n>2:
  kappa=cap-1;theta=(kappa-1)/(cap-1)-s.Rational(1,100);t=s.Rational(1,10**8)
  op=lambda a,l:l*a+(1-l)*s.diag(*[ptr(a) for _ in range(n)])/n
  sigt=op(sig,theta);rho=sigt+t*D
  positive=lambda a:all(a[:i,:i].det()>0 for i in range(1,N+1))
  assert positive(sigt) and positive(rho) and positive(kappa*B-sigt) and positive(kappa*B-rho)
  # Connected blocks are derived from the FULL matrices, not prescribed
  # by the reduced sqrt(d-1)2x2 formula.
  unseen=set(range(N));blocks=[]
  while unseen:
   block={unseen.pop()};todo=list(block)
   while todo:
    i=todo.pop();nbr={j for j in unseen if sigt[i,j]!=0 or D[i,j]!=0};unseen-=nbr;block|=nbr;todo+=list(nbr)
   blocks.append(sorted(block))
  def form(a,b,z):
   total=0
   for ix in blocks:
    aa=a.extract(ix,ix);bb=b.extract(ix,ix);zz=z.extract(ix,ix)
    if zz==s.zeros(len(ix)):continue
    ys=s.symbols('y:'+str(len(ix)**2));yy=s.Matrix(len(ix),len(ix),ys);ss=next(iter(s.linsolve(list(aa*yy+yy*bb-zz),ys)));yy=s.Matrix(len(ix),len(ix),ss)
    assert aa*yy+yy*bb==zz;total+=s.trace(zz*yy)
   return total
  finite=[]
  for l in [-s.Rational(1,n*n-1),s.Rational(1,2)]:
   os=op(sigt,l);orr=op(rho,l);assert positive(os) and positive(orr)
   local=s.factor(form(os,os,l*D)/form(sigt,sigt,D));tri=s.factor(form(orr,os,l*t*D)/form(rho,sigt,t*D));bound=l*l*kappa/(1+l*(kappa-1))
   assert local<=bound and tri<=bound
   finite.append(dict(lambda_=str(l),kappa=str(kappa),local=str(local),triangular=str(tri),upper=str(bound),ratio_decimal=str(s.N(local,20)),faithful_both_order_slacks=True))
  row['finite_pairs']=finite
 rows.append(row)
assert all(checks.values())
out=dict(scope='Parent exploratory improvement of1017, not covered by1018 input: rank2 ladder raises candidate exact-order range to1<kappa<=d(d+1)/2. No unrestricted d>2 coefficient or grade claimed.',checks=checks,SLD_aligned_block=str(G),normalized_limit=str(limit),matrices=rows,failures=0)
(P/'CHECK1021.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(symbolic=checks,full_dimensions=[2,3,4],finite_pairs=4,all_passed=True)))

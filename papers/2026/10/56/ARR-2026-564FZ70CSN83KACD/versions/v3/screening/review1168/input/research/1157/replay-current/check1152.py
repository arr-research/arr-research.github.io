from pathlib import Path
import mpmath as m,json,datetime,traceback
m.mp.dps=180
P=Path(__file__).parent

def kron(a,b):
 c=m.zeros(a.rows*b.rows,a.cols*b.cols)
 for i in range(a.rows):
  for j in range(a.cols):
   for u in range(b.rows):
    for v in range(b.cols):c[i*b.rows+u,j*b.cols+v]=a[i,j]*b[u,v]
 return c

def logmat(a):
 w,v=m.eighe(a);assert min(w)>0
 return v*m.diag([m.log(x) for x in w])*v.H

def tr(a):return m.re(sum(a[i,i] for i in range(a.rows)))
def D(a,b):return tr(a*(logmat(a)-logmat(b)))
def KL(p,q):return p*m.log(p/q)+(1-p)*m.log((1-p)/(1-q))
def pure(xs):
 v=m.matrix(xs);v=v/m.sqrt(tr(v*v.H));return v*v.H
rows=[]
def plane(xs):return (m.eye(len(xs))-pure(xs))/2
cases=[('two_nonorthogonal_pure',[pure([1,0]),pure([1,1])]),('three_trine_real',[pure([1,0]),pure([1,1]),pure([1,-2])]),('three_complex',[pure([1,0]),pure([1,1j]),pure([1,2+1j])])]
try:
 cases.append(('three_noncommuting_ranktwo',[plane([1,0,0]),plane([1,1,0]),plane([1,1,1])]))
 for name,ts in cases:
  n=len(ts);d=ts[0].rows;f=m.matrix([1/m.sqrt(n)]*n);F=f*f.H;Q=m.eye(n)-F;ps=[]
  for i in range(n):
   e=m.zeros(n,1);e[i]=1;ps.append(m.sqrt(m.mpf(n)/(n-1))*(e-f/m.sqrt(n)))
  # Inverse on P: express in an orthonormal eigenbasis of P.
  ew,ev=m.eigh(Q);V=ev[:,1:n]
  S=sum(ts,m.zeros(d));T=m.zeros((n-1)*d);Z=m.zeros((n-1)*d,d)
  for psi,t in zip(ps,ts):
   u=V.H*psi;T+=kron(u*u.H,t);Z+=kron(u,t)
  G=kron(m.eye(n-1),S)
  for k in [16,64,128]:
   beta=m.mpf(1)/(4*n*k);delta=m.power(2,-k);eps=beta*delta;alpha=m.mpf(1)/n-(n-2)*eps-beta;c=m.sqrt(alpha*beta*(1-delta))
   plus=[];minus=[]
   for psi in ps:
    pi=psi*psi.H;off=psi*f.H+f*psi.H;base=alpha*pi+eps*(Q-pi)+beta*F
    plus.append(base+c*off);minus.append(base-c*off)
   Di=sum(D(a,b) for a,b in zip(plus,minus))
   op=sum((kron(a,t) for a,t in zip(plus,ts)),m.zeros(n*d));om=sum((kron(b,t) for b,t in zip(minus,ts)),m.zeros(n*d))
   A=(alpha-eps)*T+eps*G;X=c*(A**-1)*Z
   H=m.matrix((n-1)*d+d,d)
   for i in range((n-1)*d):
    for j in range(d):H[i,j]=X[i,j]
   for i in range(d):H[(n-1)*d+i,i]=1
   E=H*((H.H*H)**-1)*H.H
   # Convert to [P-basis,F]-ordered physical coordinates.
   U=m.matrix(n*d,n*d);Vp=kron(V,m.eye(d));Fp=kron(f,m.eye(d))
   for i in range(n*d):
    for j in range((n-1)*d):U[i,j]=Vp[i,j]
    for j in range(d):U[i,(n-1)*d+j]=Fp[i,j]
   effect=U*E*U.H;p=tr(effect*op);q=tr(effect*om);Db=KL(p,q);Do=D(op,om)
   assert 0<q<p<1 and 0<Db<=Do+m.mpf('1e-100') and Do<=Di+m.mpf('1e-100')
   rows.append({'case':name,'n':n,'d':d,'k':k,'Di':m.nstr(Di,45),'Do':m.nstr(Do,45),'Db':m.nstr(Db,45),'retention':m.nstr(Db/Di,45),'q_over_beta_delta':m.nstr(q/(beta*delta),45),'p_over_beta':m.nstr(p/beta,45),'minimum_output_eigenvalue':m.nstr(min(m.eigh(om,eigvals_only=True)),30)})
 out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mp_dps':m.mp.dps,'status':'pass','cases':rows,'new_hypothesis_only':True,'no_grade':True}
except Exception as e:
 out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'failed','error':repr(e),'traceback':traceback.format_exc(),'completed':rows};(P/'FAILURE1152.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');raise
(P/'CONTROL1152.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))

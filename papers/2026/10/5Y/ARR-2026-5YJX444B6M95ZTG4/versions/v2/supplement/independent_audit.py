"""Independent falsification/consistency checks, NOT a proof or priority certificate."""
from pathlib import Path
import hashlib,json,datetime
import numpy as np
from scipy.optimize import differential_evolution, minimize_scalar

R=Path(__file__).parent
rng=np.random.default_rng(177031993)
tol=2e-11
def entropy(a):
 eig=np.linalg.eigvalsh((a+a.conj().T)/2)
 if eig.min() < -tol: raise ValueError(('nonPSD',eig.min()))
 return float(-np.sum(eig[eig>0]*np.log(eig[eig>0])))
def h(p):
 p=np.clip(p,0,1);q=1-p
 return -np.where(p>0,p*np.log(np.maximum(p,1e-300)),0)-np.where(q>0,q*np.log(np.maximum(q,1e-300)),0)
def g(u): return h((1+np.sqrt(np.maximum(0,1-4*u)))/2)
def complex_random(shape):return rng.normal(size=shape)+1j*rng.normal(size=shape)
def normal(a):return a/np.linalg.norm(a)
def block(X,Y,c,K):
 a,b,e,d=c;xx=X@X.conj().T;yy=Y@Y.conj().T;xy=X@Y.conj().T
 return np.block([[a*xx+b*yy,K*xy],[K*xy.conj().T,e*xx+d*yy]])
def gap(X,Y,c,K):
 a,b,e,d=c;u=(a+b)*(e+d)-K*K
 return entropy(block(X,Y,c,K))-(a+e)*entropy(X@X.conj().T)-(b+d)*entropy(Y@Y.conj().T)-g(u)

counts={};mins={};maxerrs={};failures=[]
def record(group,value,case):
 counts[group]=counts.get(group,0)+1
 if group not in mins or value<mins[group]['value']: mins[group]={'value':float(value),'case':case}
 if value < -tol:failures.append({'group':group,'value':float(value),'case':case})
def error(group,value):maxerrs[group]=max(maxerrs.get(group,0),float(value))
for j in range(9000):
 d,e=[(1,1),(1,4),(4,1),(2,2),(2,5),(5,2),(5,7),(7,4),(8,8)][j%9]
 X=normal(complex_random((d,e)));Y=normal(complex_random((d,e)))
 mode=(j//9)%5
 if mode==1:Y=X.copy()
 if mode==2:Y=normal(X+10**rng.uniform(-12,-2)*complex_random((d,e)))
 if mode==3:
  X=normal(np.outer(complex_random(d),complex_random(e)))
  Y=normal(np.outer(complex_random(d),complex_random(e)))
 if mode==4:
  X=np.zeros((d,e),complex);Y=X.copy();X[0,0]=1;Y[-1,-1]=1
 U0=float(rng.beta(.35,.35));U1=1-U0
 r=float(rng.choice([0,1,rng.random(),1-1e-10]))
 K=r*np.sqrt(U0*U1);u=U0*U1-K*K
 w=rng.dirichlet([.3,.3,.3])
 if j%11==0:w=np.eye(3)[j%3]
 # Stable equivalent coordinates, including u=0.
 beta=U0*(1-r*r)*w[0];eta=U1*(1-r*r)*w[1]
 c=np.array([U0-beta,beta,eta,U1-eta])
 case={'index':j,'shape':[d,e],'mode':mode,'coefficients':c.tolist(),'K':float(K)}
 record('matrix',gap(X,Y,c,K),case)
 if mode==1:error('exact_X_equals_Y',abs(gap(X,Y,c,K)))
 if U0>1e-14 and U1>1e-14:
  A=np.array([K*K/U1,u/U1,0,U1]);B=np.array([U0,0,u/U0,K*K/U0]);C=np.array([U0,0,0,U1])
  error('coefficient_reconstruction',np.max(abs(c-(w[0]*A+w[1]*B+w[2]*C))))
  MA=np.block([[np.sqrt(max(0,A[0]))*X,np.sqrt(max(0,A[1]))*Y],[np.sqrt(U1)*Y,np.zeros_like(Y)]])
  MB=np.block([[np.sqrt(U0)*X,np.zeros_like(X)],[np.sqrt(max(0,B[3]))*Y,np.sqrt(max(0,B[2]))*X]])
  error('A_factorization',np.linalg.norm(MA@MA.conj().T-block(X,Y,A,K)))
  error('B_factorization',np.linalg.norm(MB@MB.conj().T-block(X,Y,B,K)))
  record('C_SSA_vertex',gap(X,Y,C,K),case)
  for name,V in [('A_triangular',A),('B_triangular',B)]:record(name,gap(X,Y,V,K),case)
for U0 in [0.,1.]:
 for b in [0.,.2,.7,1.]:
  X=normal(complex_random((4,3)));Y=normal(complex_random((4,3)))
  c=[U0*(1-b),U0*b,(1-U0)*(1-b),(1-U0)*b]
  record('row_zero',gap(X,Y,c,0),{'U0':U0,'split':b})

def phi(rho,a,b,lam):
 return np.array([[(1-a)*rho[0,0]+b*rho[1,1],lam*rho[0,1]],[lam*rho[1,0],a*rho[0,0]+(1-b)*rho[1,1]]])
def phi_kraus(a,b,lam):
 k=1-a-b;gam=a+b;nu=a/gam if gam else 0
 G=[np.sqrt(1-nu)*np.diag([1,np.sqrt(k)]),np.array([[0,np.sqrt(b)],[0,0]]),np.sqrt(nu)*np.diag([np.sqrt(k),1]),np.array([[0,0],[np.sqrt(a),0]])]
 r=lam/np.sqrt(k) if k else 0
 D=[np.sqrt((1+r)/2)*np.eye(2),np.sqrt((1-r)/2)*np.diag([1,-1])]
 return [d@gm for d in D for gm in G]
def kraus_random(di,do,env):
 Q=np.linalg.qr(complex_random((do*env,di)))[0]
 return Q.reshape(do,env,di).transpose(1,0,2)
for j in range(300):
 di,do,env=[(2,3,4),(3,2,5),(4,5,3),(5,4,6)][j%4]
 N=kraus_random(di,do,env)
 a,b,k=rng.dirichlet([.7,.7,.7]);lam=np.sqrt(k)*rng.random()
 psis=[normal(complex_random((2,di))) for _ in range(4)]
 weights=rng.dirichlet(np.ones(4));outs=[];pops=[];branch_costs=[];branches=[];branch_weights=[]
 for q,psi in zip(weights,psis):
  p=np.linalg.norm(psi[1])**2;X=np.column_stack([L@psi[0]/np.sqrt(1-p) for L in N]);Y=np.column_stack([L@psi[1]/np.sqrt(p) for L in N])
  c=[(1-p)*(1-a),p*b,(1-p)*a,p*(1-b)];K=lam*np.sqrt(p*(1-p));T=block(X,Y,c,K)
  direct=np.zeros_like(T)
  for F in phi_kraus(a,b,lam):
   for L in N:
    v=(F@psi@L.T).ravel();direct+=np.outer(v,v.conj())
  error('channel_block_equals_direct_kraus',np.linalg.norm(T-direct))
  t=a+k*p;ep=g(t*(1-t)-lam*lam*p*(1-p));bc=(1-p)*entropy(X@X.conj().T)+p*entropy(Y@Y.conj().T)
  record('arbitrary_partner_pure_input',entropy(T)-ep-bc,{'index':j,'dims':[di,do,env],'a':a,'b':b,'lambda':lam,'p':p})
  outs.append(T);pops.append(p);branch_costs.append(bc)
  branches.extend([X@X.conj().T,Y@Y.conj().T]);branch_weights.extend([q*(1-p),q*p])
 mean=sum(q*T for q,T in zip(weights,outs));Nmean=sum(q*T for q,T in zip(branch_weights,branches))
 error('N_ensemble_average_is_marginal',np.linalg.norm(Nmean-mean[:do,:do]-mean[do:,do:]))
 chi=entropy(mean)-sum(q*entropy(T) for q,T in zip(weights,outs))
 branch_chi=entropy(Nmean)-sum(q*bc for q,bc in zip(weights,branch_costs))
 scalar=h(a+k*np.dot(weights,pops))-sum(q*g((a+k*p)*(1-a-k*p)-lam*lam*p*(1-p)) for q,p in zip(weights,pops))
 record('Holevo_before_convex_envelope',scalar+branch_chi-chi,{'index':j,'dims':[di,do,env]})

def envelope_case(a,b,l2):
 k=1-a-b;p=np.linspace(0,1,4001);t=a+k*p;e=g(t*(1-t)-l2*p*(1-p));hull=[]
 for i in range(len(p)):
  while len(hull)>=2:
   q,r=hull[-2:]
   if (e[r]-e[q])*(p[i]-p[r]) >= (e[i]-e[r])*(p[r]-p[q]):hull.pop()
   else:break
  hull.append(i)
 f=np.interp(p,p[hull],e[hull]);i=int(np.argmax(h(t)-f));m=p[i]
 def neg_obj(x):
  p0,p1,w=x;mean=w*p0+(1-w)*p1
  def ee(z):return g((a+k*z)*(1-a-k*z)-l2*z*(1-z))
  return -(h(a+k*mean)-w*ee(p0)-(1-w)*ee(p1))
 opt=differential_evolution(neg_obj,[(0,1)]*3,seed=7203,tol=1e-10,popsize=12,maxiter=350,polish=True)
 p0,p1,w=opt.x;mean=w*p0+(1-w)*p1
 signals=[];qs=[]
 for z,q in [(p0,w),(p1,1-w)]:
  for sign in [-1,1]:
   v=np.array([np.sqrt(1-z),sign*np.sqrt(z)]);signals.append(phi(np.outer(v,v),a,b,np.sqrt(l2)));qs.append(q/2)
 realized=entropy(sum(q*s for q,s in zip(qs,signals)))-sum(q*entropy(s) for q,s in zip(qs,signals))
 return dict(a=a,b=b,k=k,lambda_squared=l2,grid_capacity_bits=float((h(t)-f)[i]/np.log(2)),continuous_four_state_bits=float(-opt.fun/np.log(2)),optimizer_success=bool(opt.success),max_envelope_gap=float(np.max(e-f)),attainment_error_nats=float(realized+opt.fun),populations=[float(p0),float(p1)],first_weight=float(w),mean_population=float(mean),grid_convex_vertices=len(hull))
envelopes=[envelope_case(*v) for v in [(0.1,0.3,.5),(.1,.3,.2),(.1,.3,.395),(.2,.2,.36),(.1,.3,.6),(0,0,1),(0,.4,.3),(.3,.7,0)]]

def adversarial(z):
 X=z[:4].reshape(2,2);Y=z[4:8].reshape(2,2)
 if np.linalg.norm(X)<1e-12 or np.linalg.norm(Y)<1e-12:return 1
 X=normal(X);Y=normal(Y);U0=z[8];r=z[9];wa=z[10];wb=(1-wa)*z[11]
 U1=1-U0;beta=U0*(1-r*r)*wa;eta=U1*(1-r*r)*wb
 return gap(X,Y,[U0-beta,beta,eta,U1-eta],r*np.sqrt(U0*U1))
opt=differential_evolution(adversarial,[(-1,1)]*8+[(.0001,.9999),(0,1),(0,1),(0,1)],seed=132098,popsize=8,maxiter=130,polish=True,tol=1e-9)
record('differential_evolution_real_2x2',opt.fun,{'evaluations':int(opt.nfev),'iterations':int(opt.nit),'success':bool(opt.success),'message':str(opt.message)})
res=dict(status='numerical adversarial screen only; not proof, no manuscript grade',seed=177031993,tolerance=tol,counts=counts,minima=mins,max_absolute_errors=maxerrs,failures=failures,envelope_checks=envelopes,checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(R/'independent-results.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
print(json.dumps(res,indent=2))

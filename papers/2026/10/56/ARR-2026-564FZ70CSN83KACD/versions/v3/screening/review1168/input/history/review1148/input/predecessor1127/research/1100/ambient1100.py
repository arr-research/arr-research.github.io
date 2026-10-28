from pathlib import Path
import mpmath as m,json
m.mp.dps=90;P=Path(__file__).parent
tr=lambda a:sum(a[i,i] for i in range(a.rows))
def norm(a):return max(abs(x) for x in a)
def outer(v):return v*v.H
def blockdiag(bs):
 n=bs[0].rows;out=m.zeros(n*len(bs))
 for j,b in enumerate(bs):
  for a in range(n):
   for c in range(n):out[j*n+a,j*n+c]=b[a,c]
 return out
def logm(a):
 w,v=m.eighe(a);assert w[0]>0
 return v*m.diag([m.log(x) for x in w])*v.H,w
def rel(p,q):
 lp,wp=logm(p);lq,wq=logm(q);return m.re(tr(p*(lp-lq)))
def tri(p,q):
 wp,up=m.eighe(p);wq,uq=m.eighe(q);ov=up.H*uq
 return sum(wq[j]*((wp[i]/wq[j]-1)**2/(wp[i]/wq[j]+1))*abs(ov[i,j])**2 for i in range(p.rows) for j in range(p.rows))
def basis(n):
 U=m.eye(n);U[0,0]=U[1,1]=m.mpf(3)/5;U[0,1]=U[1,0]=4j/m.mpf(5);f=U*m.matrix([1/m.sqrt(n)]*n);F=outer(f);PP=m.eye(n)-F
 psis=[m.sqrt(m.mpf(n)/(n-1))*(U[:,i]-f/m.sqrt(n)) for i in range(n)]
 return f,F,PP,psis
rows=[]
for n,z in [(3,m.mpf(4)),(3,m.mpf(12)),(4,m.mpf('.5')),(4,m.mpf(4))]:
 f,F,PP,vs=basis(n);beta=m.mpf(n)**-5;eps=m.mpf(n)**(-z-4);delta=m.mpf(n)**-z;alpha=1/m.mpf(n)-(n-2)*eps-beta;c=m.sqrt(alpha*beta*(1-delta));I=m.eye(n)
 plus=[];minus=[]
 for v in vs:
  pi=outer(v);off=v*f.H+f*v.H;base=alpha*pi+eps*(PP-pi)+beta*F;plus.append(base+c*off);minus.append(base-c*off)
 r=sum(plus,m.zeros(n));assert norm(r-sum(minus,m.zeros(n)))<m.mpf('1e-85')
 po=[sum((plus[i] for i in range(n) if i!=j),m.zeros(n))/(n-1) for j in range(n)];so=[sum((minus[i] for i in range(n) if i!=j),m.zeros(n))/(n-1) for j in range(n)]
 # Find reference-projector eigenvectors from full n-dimensional output matrices.
 Es=[]
 for b in so:
  vals,vecs=m.eighe(b);Es.append(outer(vecs[:,0]))
 E=blockdiag(Es);rho=blockdiag(plus);sigma=blockdiag(minus);ro=blockdiag(po);ss=blockdiag(so);assert norm(E*E-E)<m.mpf('1e-80')
 din=rel(rho,sigma);dout=rel(ro,ss);p=m.re(tr(E*ro));q=m.re(tr(E*ss));db=p*m.log(p/q)+(1-p)*m.log((1-p)/(1-q))
 lam=-1/m.mpf(n-1);ap=(alpha+n*(n-2)*eps)/(n-1)**2;g=m.sqrt((ap-beta)**2+4*lam**2*c*c);h=(ap+beta+g)/2;lo=(ap*beta-lam**2*c*c)/h
 assert abs(q-n*lo)<m.mpf('1e-80') and abs(p-n*(lo+4*lam**2*c*c/g))<m.mpf('1e-80')
 gi=m.sqrt((alpha-beta)**2+4*c*c);hi=(alpha+beta+gi)/2;li=(alpha*beta-c*c)/hi;pred=4*n*c*c*m.log(hi/li)/gi
 assert abs(din-pred)<m.mpf('1e-75') and 0<db<dout<din
 rows.append({'n':n,'z':str(z),'ambient_dimension':n*n,'complex_rotation':True,'full_matrix_log_input':m.nstr(din,65),'full_matrix_log_output':m.nstr(dout,65),'full_matrix_measured_retention':m.nstr(db/din,65),'gap_to_ordinary':m.nstr(db/din-1/m.mpf(n-1),65),'sign':'positive' if db/din>1/m.mpf(n-1) else 'negative','projector_idempotent_error':m.nstr(norm(E*E-E),8),'same_R_marginal':True,'q':m.nstr(q,65),'p':m.nstr(p,65),'reference_only_and_label_only_equal':True,'no_postselection':True})
tris=[]
for n,lam in [(3,m.mpf('.5')),(3,-m.mpf('.5')),(4,-m.mpf(1)/3),(4,m.mpf('1'))]:
 f,F,PP,vs=basis(n);xi=m.mpf('0.02');t=m.mpf('0.001');alpha=(1-xi)/n+xi/n**2;beta=xi/n**2;co=t*m.sqrt(n-1)
 plus=[alpha*outer(v)+beta*(m.eye(n)-outer(v))+co*(v*f.H+f*v.H) for v in vs];minus=[alpha*outer(v)+beta*(m.eye(n)-outer(v))-co*(v*f.H+f*v.H) for v in vs];r=sum(plus,m.zeros(n));po=[lam*b+(1-lam)*r/n for b in plus];so=[lam*b+(1-lam)*r/n for b in minus]
 di=tri(blockdiag(plus),blockdiag(minus));do=tri(blockdiag(po),blockdiag(so));ap=(1-xi)*(1+(n-2)*lam)/(n*(n-1))+beta;predict=lam**2*(alpha+beta)/(ap+beta);assert abs(do/di-predict)<m.mpf('1e-75')
 tris.append({'n':n,'lambda':str(lam),'complex_full_ambient_Petz_triangle':m.nstr(do/di,65),'formula_error':m.nstr(abs(do/di-predict),8)})
(P/'AMBIENT1100.json').write_text(json.dumps({'precision_digits':90,'method':'Full complex ambient matrices, fullmatrixlogs and spectralPetz; outputmeasurement eigenvectors from fullreferenceblocks, not2x2formula','measurement_cases':rows,'triangle_cases':tris,'passed':True},indent=2)+'\n',encoding='utf-8');print('Fullambient4measurement+4triangle passed;measurement signs',[r['sign'] for r in rows])

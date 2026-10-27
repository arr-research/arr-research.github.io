"""Independent checks of exact PDF 96d340e8...; finite evidence, not universal proof."""
import json, math, pathlib, hashlib, datetime
import numpy as np
import scipy.linalg as la
import sympy as sp
import mpmath as mp

OUT=pathlib.Path(__file__).resolve().parent
rng=np.random.default_rng(92320261027)
results={'seed':92320261027,'pdf_sha256':'96d340e882102bc26c35e3085d99ce9b8e985ef0895ef7d5b2ae63d91d5362c0'}
def basis(n):
    b=[]
    for i in range(n):
        x=np.zeros((n,n),complex);x[i,i]=1;b.append(x)
    for i in range(n):
        for j in range(i+1,n):
            x=np.zeros((n,n),complex);x[i,j]=x[j,i]=1/math.sqrt(2);b.append(x)
            x=np.zeros((n,n),complex);x[i,j]=1j/math.sqrt(2);x[j,i]=-1j/math.sqrt(2);b.append(x)
    return b
def channel(ks,x):return sum(k@x@k.conj().T for k in ks)
def amplify(ks,r):return [np.kron(k,np.eye(r)) for k in ks]
def density(n):
    z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));s=z@z.conj().T+np.eye(n)*.2
    return s/np.trace(s)
def gram(s,ys):
    w,u=la.eigh(s);assert min(w)>0
    lm=np.empty((len(w),len(w)))
    for i in range(len(w)):
        for j in range(len(w)):
            lm[i,j]=1/w[i] if abs(w[i]-w[j])<1e-13*w[i] else np.log(w[i]/w[j])/(w[i]-w[j])
    t=np.array([u.conj().T@y@u for y in ys]);a=t.reshape((len(ys),-1))
    return ((a.conj()*lm.reshape(-1))@a.T).real
def relative(r,s):
    w,u=la.eigh(r);v,z=la.eigh(s);assert min(v)>0
    return float(sum(x*math.log(x) for x in w if x>1e-14)-np.trace(r@(z@np.diag(np.log(v))@z.conj().T)).real)
def ad(p):return [np.diag([1,math.sqrt(1-p)]),np.array([[0,math.sqrt(p)],[0,0]])]
exact={}
p1,p2=sp.symbols('p1 p2',positive=True);s1=1-p1;s2=1-p2
J=sp.Matrix([[0,1],[0,0]]);K0=sp.diag(1,sp.sqrt(s1));K1=sp.sqrt(p1)*J
F=sp.diag(1,sp.sqrt(s2/s1));a=(p2-p1)/s1;c=s1/p1
# Matrix-unit identities are compared entrywise, with the admissible positive-root relation.
def smap(ks,x):return sum((k*x*k.T for k in ks),sp.zeros(x.rows))
exact['ad_domination_matrix_units']=all(sp.simplify(c*smap([K0,K1],sp.eye(2)[:,i]*sp.eye(2)[j,:])-J*smap([K0,K1],sp.eye(2)[:,i]*sp.eye(2)[j,:])*J.T-c*K0*(sp.eye(2)[:,i]*sp.eye(2)[j,:])*K0.T)==sp.zeros(2) for i in range(2) for j in range(2))
# Rational instances avoid spurious symbolic square-root branch assumptions.
ad_id=[]
for aa,bb in [(sp.Rational(1,4),sp.Rational(1,2)),(sp.Rational(1,10),sp.Rational(9,10)),(sp.Rational(1,100),sp.Rational(99,100))]:
    ka=[sp.diag(1,sp.sqrt(1-aa)),sp.sqrt(aa)*J];kb=[sp.diag(1,sp.sqrt(1-bb)),sp.sqrt(bb)*J];ff=sp.diag(1,sp.sqrt((1-bb)/(1-aa)))
    for i in range(2):
        for j in range(2):
            e=sp.eye(2)[:,i]*sp.eye(2)[j,:];y=smap(ka,e)
            ad_id.append(sp.simplify(ff*(y+(bb-aa)/(1-aa)*J*y*J.T)*ff-smap(kb,e))==sp.zeros(2))
exact['ad_factorization_12_units']=all(ad_id)
b,aa=sp.symbols('b aa',positive=True);J3=sp.Matrix([[0,1,0],[0,0,1],[0,0,0]])
db=sp.diag(1,1/sp.sqrt(1+b),1/sp.sqrt(1+b+b*b));km=[db,sp.sqrt(b)*J3*db,b*J3**2*db]
exact['qutrit_trace_preserving']=sp.simplify(sum((k.T*k for k in km),sp.zeros(3)))==sp.eye(3)
exact['qutrit_filter_trace_identity']=sp.simplify(sp.diag(1,1-aa,1-aa+aa**2)+aa*J3.T*sp.diag(1,1-aa,1-aa+aa**2)*J3)==sp.eye(3)
exact['qutrit_domination_9_units']=all(sp.simplify(smap(km,sp.eye(3)[:,i]*sp.eye(3)[j,:])/b-J3*smap(km,sp.eye(3)[:,i]*sp.eye(3)[j,:])*J3.T-db*(sp.eye(3)[:,i]*sp.eye(3)[j,:])*db/b)==sp.zeros(3) for i in range(3) for j in range(3))
exact['nilpotency']=(J**2==sp.zeros(2) and J3**3==sp.zeros(3))
exact['ad_constant_1']=str(sp.simplify(sp.Rational(1,3)/(1+1/sp.sqrt(3))**2))
exact['ad_constant_2']=str(sp.Rational(1,81)/(1+sp.Rational(8,3))**2)
exact['qutrit_constant']=str(sp.Rational(1,2)/((1+50)*(1+5+25)**2))
exact['rational_witnesses']=[]
for n in [3,4,5,10,20]:
    x=sp.Rational(1,n);r=sp.Rational(1,2)**(n*n);e=r/(n*n)
    diag=[(1-x)*(1-r),(1-x)*r,x*(1-r),x*r]
    det=diag[0]*diag[3]-e*e
    xx=sp.Matrix([[0,1],[1,0]]);rr=sp.diag(*diag)+e*sp.kronecker_product(xx,xx)
    pt=sp.Matrix(4,4,lambda i,j:rr[2*(i//2)+j%2,2*(j//2)+i%2])
    exact['rational_witnesses'].append({'n':n,'two_positive_block_determinants':bool(det>0),'ppt_equals_original':pt==rr,'t_squared_lt_one':bool(e*e/(x*(1-x)*r*(1-r))<1),'minS_equals_r_over_n':min(diag)==r/n,'nonclassical_commutator_nonzero':bool(e*(1-2*r)!=0)})
results['exact']=exact

numeric=[]
for family,param,ks0,ks1,c,a,m,k in [
    ('AD',[.25,.5],ad(.25),ad(.5),3,1/3,2/3,2),
    ('AD',[.1,.9],ad(.1),ad(.9),9,8/9,1/9,2),
    ('AD',[.01,.99],ad(.01),ad(.99),99,98/99,1/99,2)]:
    for r in [1,2,3]:
        A=amplify(ks0,r);B=amplify(ks1,r);bb=basis(2*r);lam=m/((1+a*c)*sum((a*math.sqrt(c))**j for j in range(k))**2)
        for trial in range(3):
            s=density(2*r);S=channel(A,s);T=channel(B,s)
            G=gram(S,[channel(A,y) for y in bb]);H=gram(T,[channel(B,y) for y in bb]);vals=la.eigvalsh(H,G)
            rho=density(2*r);dr=relative(channel(B,rho),T)/relative(channel(A,rho),S)
            numeric.append({'family':family,'parameters':param,'R':r,'trial':trial,'whole_Hermitian_dimension':len(bb),'lambda':lam,'minimum_metric_ratio':float(min(vals)),'relative_entropy_ratio':dr,'passed':bool(min(vals)>=lam-1e-10 and dr>=lam-1e-10)})
for b0,a0 in [(.01,.5),(.2,.9),(2,.25)]:
    j=np.array(J3).astype(float);d=np.diag([1,1/math.sqrt(1+b0),1/math.sqrt(1+b0+b0*b0)]);f=np.diag([1,math.sqrt(1-a0),math.sqrt(1-a0+a0*a0)])
    km=[d,math.sqrt(b0)*j@d,b0*j@j@d];kn=[f@t for t in km]+[math.sqrt(a0)*f@j@t for t in km]
    lam=(1-a0)/((1+a0/b0)*(1+a0/math.sqrt(b0)+a0*a0/b0)**2)
    for r in [1,2,3]:
        A=amplify(km,r);B=amplify(kn,r);bb=basis(3*r)
        s=density(3*r);S=channel(A,s);T=channel(B,s);G=gram(S,[channel(A,y) for y in bb]);H=gram(T,[channel(B,y) for y in bb]);v=la.eigvalsh(H,G)
        numeric.append({'family':'qutrit','parameters':[b0,a0],'R':r,'whole_Hermitian_dimension':len(bb),'lambda':lam,'minimum_metric_ratio':float(min(v)),'passed':bool(min(v)>=lam-1e-10)})
results['whole_tangent_checks']=numeric

# High precision finite MI from independent 2x2 block eigenvalues, not Hessians.
def ent(vals):return -sum(v*mp.log(v) for v in vals)
def mi(q,r,e):
    diag=[(1-q)*(1-r),(1-q)*r,q*(1-r),q*r];eig=[]
    for i,j in [(0,3),(1,2)]:
        lo,hi=diag[i],diag[j];large=(lo+hi+mp.sqrt((lo-hi)**2+4*e*e))/2;small=(lo*hi-e*e)/large;eig += [large,small]
    return ent(diag)-ent(eig)
def h(q,r):
    def ell(a,b):return (mp.log(a)-mp.log(b))/(a-b)
    return ell((1-q)*(1-r),q*r)+ell((1-q)*r,q*(1-r))
mis=[]
for n in [3,5,10,20,40]:
    mp.mp.dps=int(2*n*n*math.log10(2))+100
    x=mp.mpf(1)/n;r=mp.power(2,-n*n);eps=r/(n*n);ii=mi(x,r,eps);gg=2*h(x,r)
    for pp in ['0.1','0.5','0.9','0.999']:
        s=1-mp.mpf(pp);oo=mi(s*x,r,mp.sqrt(s)*eps);gr=s*h(s*x,r)/h(x,r);lower=(n-1)/(n+1)*gr;ratio=oo/ii
        mis.append({'n':n,'p':pp,'decimal_precision':mp.mp.dps,'MI_ratio':mp.nstr(ratio,25),'metric_ratio':mp.nstr(gr,25),'proven_finite_lower':mp.nstr(lower,25),'MI_in':mp.nstr(ii,12),'MI_in_over_claimed_asymptotic':mp.nstr(ii/(mp.log(2)*mp.power(2,-2*n*n)/n),20),'passed':bool(lower<=ratio<=1 and eps*eps*gg/(2*(1+mp.mpf(1)/n))<=ii<=eps*eps*gg/(2*(1-mp.mpf(1)/n)))})
results['finite_MI_high_precision']=mis
mp.mp.dps=90
results['metric_joint_asymptotic']=[{'n':n,'p':'0.999','ratio':mp.nstr(mp.mpf('.001')*h(mp.mpf('.001')/n,mp.power(2,-n*n))/h(mp.mpf(1)/n,mp.power(2,-n*n)),25)} for n in [100,1000,10000]]
results['status']='PASS' if all(x['passed'] for x in numeric+mis) and all(exact[k] for k in ['ad_domination_matrix_units','ad_factorization_12_units','qutrit_trace_preserving','qutrit_filter_trace_identity','qutrit_domination_9_units','nilpotency']) else 'FAIL'
results['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(OUT/'CONTROLS923.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps({'status':results['status'],'tangent_checks':len(numeric),'finite_MI_checks':len(mis),'metric_asymptotic':results['metric_joint_asymptotic'],'exact':exact},indent=2))

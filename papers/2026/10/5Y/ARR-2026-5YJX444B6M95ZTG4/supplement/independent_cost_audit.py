"""Independent diagnostics for the separate complementary-channel cost dossiers.
No finite experiment establishes additivity; analytic arguments are in the report.
"""
from pathlib import Path
import hashlib,json,math,sys
from fractions import Fraction as Q
import numpy as np
import scipy
from scipy.special import xlogy
from scipy.optimize import linprog
import mpmath as mp
ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(20261018019)

def phi(r,a,b,x):
    return np.array([[(1-a)*r[0,0]+b*r[1,1],math.sqrt(x)*r[0,1]],
                     [math.sqrt(x)*r[1,0],a*r[0,0]+(1-b)*r[1,1]]])
def rev(a,b,x,p):
    t=a+(1-a-b)*p
    return p*b/(1-t),(1-p)*a/t,x*p*(1-p)/(t*(1-t)),t
def entprob(v):return float(-np.sum(xlogy(v,v)))
def pure_e(q,a,b,x):
    t=a+(1-a-b)*q
    d=np.clip(t*(1-t)-x*q*(1-q),0,.25)
    u=(1+np.sqrt(1-4*d))/2
    return -xlogy(u,u)-xlogy(1-u,1-u)
def roof_grid(a,b,x,q,N=3000,return_hull=False):
    xs=np.linspace(0,1,N+1);ys=pure_e(xs,a,b,x);stack=[]
    for j in range(N+1):
        while len(stack)>1:
            i,k=stack[-2:]
            if (ys[k]-ys[i])*(j-k)<(ys[j]-ys[k])*(k-i):break
            stack.pop()
        stack.append(j)
    val=float(np.interp(q,xs[stack],ys[stack]))
    if return_hull:return val,xs,ys,stack
    return val
def G(a,b,x,p,N=3000):
    if p==0 or p==1:return 0.
    t=a+(1-a-b)*p
    if t==0 or t==1:return entprob(np.array([p,1-p]))
    ap,bp,xp,t=rev(a,b,x,p)
    return roof_grid(ap,bp,xp,t,N)

maxerr=dict(isometry=0.,normalized_reverse=0.,Petz=0.,state_reconstruction=0.,involution=0.,population=0.,ab_scaling=0.,HU_scaling=0.,determinant=0.)
minslack=1.
for case in range(512):
    a,b,k=rng.dirichlet([.8,.8,.8]);x=k*rng.random();p=.003+.994*rng.random()
    C=np.array([[1-a,0,0,math.sqrt(x)],[0,a,0,0],[0,0,b,0],[math.sqrt(x),0,0,1-b]])
    vals,vecs=np.linalg.eigh(C)
    Kraus=np.stack([math.sqrt(max(0,v))*vecs[:,j].reshape(2,2).T for j,v in enumerate(vals)])
    # Deliberately change the environmental basis by a random complex unitary.
    U,_=np.linalg.qr(rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)))
    Kraus=np.einsum('ef,fbr->ebr',U,Kraus)
    V=np.transpose(Kraus,(1,0,2));psi=V*np.sqrt([1-p,p])[None,None,:]
    ap,bp,xp,t=rev(a,b,x,p);L=p*(1-p)/(t*(1-t));kp=1-ap-bp
    W=np.transpose(psi,(2,1,0))/np.sqrt([1-t,t])[None,None,:];Wm=W.reshape(8,2)
    maxerr['isometry']=max(maxerr['isometry'],float(np.max(np.abs(Wm.conj().T@Wm-np.eye(2)))))
    pm=psi.transpose(2,1,0).reshape(8,2)
    maxerr['state_reconstruction']=max(maxerr['state_reconstruction'],float(np.max(np.abs(pm@pm.conj().T-Wm@np.diag([1-t,t])@Wm.conj().T))))
    M=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));r=M@M.conj().T;r/=np.trace(r)
    out=np.einsum('rei,ij,sej->rs',W,r,W.conj())
    maxerr['normalized_reverse']=max(maxerr['normalized_reverse'],float(np.max(np.abs(out-phi(r,ap,bp,xp)))))
    Dr=np.diag(np.sqrt([1-p,p]));Dt=np.diag(1/np.sqrt([1-t,t]))
    petz=sum((Dr@K.conj().T@Dt)@r@(Dt@K@Dr) for K in Kraus)
    maxerr['Petz']=max(maxerr['Petz'],float(np.max(np.abs(petz-phi(r,ap,bp,xp)))))
    ar,br,xr,pr=rev(ap,bp,xp,t)
    maxerr['involution']=max(maxerr['involution'],abs(ar-a),abs(br-b),abs(xr-x))
    maxerr['population']=max(maxerr['population'],abs(pr-p))
    maxerr['ab_scaling']=max(maxerr['ab_scaling'],abs(ap*bp-L*a*b))
    c=(math.sqrt(k+a*b)-math.sqrt(a*b))**2
    cp=(math.sqrt(max(0,kp+ap*bp))-math.sqrt(ap*bp))**2
    maxerr['HU_scaling']=max(maxerr['HU_scaling'],abs(cp-L*c))
    maxerr['determinant']=max(maxerr['determinant'],abs((ap+kp*t)*(1-ap-kp*t)-xp*t*(1-t)-p*(1-p)*(1-x)))
    minslack=min(minslack,kp-xp)
assert max(maxerr.values())<2e-11 and minslack>-2e-12

# Independently compare the monotone-chain hull against a finite moment LP.
lperr=0.;mingap=1.;concave_records=[]
for case in range(36):
    a,b,k=rng.dirichlet([2,2,2]);x=k*rng.random();p=.02+.96*rng.random()
    ap,bp,xp,t=rev(a,b,x,p)
    value,qs,es,hull=roof_grid(ap,bp,xp,t,1800,True)
    lp=linprog(es,A_eq=np.array([np.ones_like(qs),qs]),b_eq=[1,t],bounds=(0,None),method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    assert lp.success
    lperr=max(lperr,abs(value-lp.fun))
    p1,p2=rng.uniform(.03,.97,2);w=rng.uniform(.1,.9)
    gap=G(a,b,x,w*p1+(1-w)*p2)-w*G(a,b,x,p1)-(1-w)*G(a,b,x,p2)
    mingap=min(mingap,gap)
    concave_records.append(gap)
assert lperr<2e-8 and mingap>-2e-7

# Exactly rational lower bounds on determinants produce a conservative
# Lipschitz constant, independent of any optimized contact classification.
# If m >= 1/100000 and |v'| <= 1, then g'(m) < 12 and L_e <= 12.
mp.mp.dps=70
def qstr(q):return f'{q.numerator}/{q.denominator}'
certificate=[]
a=Q(1,50);b=Q(3,10);x=Q(8041,15625) # .514624
for p in [Q(1,2),Q(14,25)]:
    t=a+(1-a-b)*p;ap=p*b/(1-t);bp=(1-p)*a/t;xp=x*p*(1-p)/(t*(1-t));kp=1-ap-bp
    A=ap*(1-ap);B=kp*(1-2*ap)-xp;D=xp-kp*kp
    candidates=[A,A+B+D]
    if D>0 and 0<-B/(2*D)<1:candidates.append(A-B*B/(4*D))
    m=min(candidates);maxvp=max(abs(B),abs(B+2*D))
    assert m>=Q(1,100000) and maxvp<=1
    N=60000
    gn,qs,es,hull=roof_grid(float(ap),float(bp),float(xp),float(t),N,True)
    # Recompute every sampled entropy at high precision is unnecessary for
    # the diagnostic claim; the global discretization bound is analytic.
    certificate.append(dict(p=qstr(p),determinant_min_exact=qstr(m),max_derivative_polynomial_exact=qstr(maxvp),conservative_entropy_L=12,N=N,grid_formation_nats=gn,grid_formation_bits=gn/math.log(2),discretization_bound_bits=12/(2*N*math.log(2))))
gp=2*mp.atanh(mp.sqrt(1-4*mp.mpf('0.00001')))/mp.sqrt(1-4*mp.mpf('0.00001'))
assert gp<12
gain=certificate[1]['grid_formation_bits']-certificate[0]['grid_formation_bits']
lower_gain= gain-certificate[1]['discretization_bound_bits']
assert lower_gain>0.004

boundary=[]
for a,b,x,label,expected in [
    (0,0,1,'identity original',0),
    (0,0,.4,'pure dephasing original',0),
    (.3,.7,0,'constant mixed original',math.log(2)),
    (0,1,0,'constant pure zero original',math.log(2)),
    (1,0,0,'constant pure one original',math.log(2)),
    (.2,.2,.04,'unital strong dephasing',entprob(np.array([.8,.2]))),
    (.2,.2,.36,'epolarizing boundary',entprob(np.array([.8,.2]))),
    (.2,.2,.5,'unital high transverse',entprob(np.array([(1+math.sqrt(.5))/2,(1-math.sqrt(.5))/2]))),
]:
    actual=G(a,b,x,.5,6000)
    assert abs(actual-expected)<1e-10
    boundary.append(dict(label=label,a=a,b=b,x=x,value_nats=actual,expected_nats=expected))

repro=[]
for name in ['reverse-channel-results.json','closed-form-results.json']:
    old=ROOT.parent/'input'/name;new=ROOT/'reproduce'/name
    if new.exists():repro.append(dict(file=name,byte_identical=old.read_bytes()==new.read_bytes(),semantic_identical=json.loads(old.read_text())==json.loads(new.read_text()),sha256=hashlib.sha256(new.read_bytes()).hexdigest()))
result=dict(status='Analytic audit supplemented by floating point diagnostics; no interval-arithmetic or formal-proof claim',seed=20261018019,runtime=dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,mpmath=mp.__version__),new_matrix_cases=512,max_errors=maxerr,min_Davies_slack=minslack,moment_LP_cases=36,max_hull_LP_error=lperr,scalar_concavity_cases=36,min_sampled_concavity_gap_nats=mingap,non_Bell_example=dict(parameters=dict(a='.02',b='.3',x='.514624'),calculations=certificate,gprime_at_1e_minus5=str(gp),grid_gain_bits=gain,analytical_discretization_adjusted_lower_gain_bits=lower_gain,qualification='The Lipschitz/truncation bound is analytic and uses exact rational parameters; function evaluations are floating point, so this is not a machine-verified interval certificate. The margin is greater than 0.004 ebits.'),boundary_checks=boundary,reproduction=repro)
(ROOT/'independent-cost-results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

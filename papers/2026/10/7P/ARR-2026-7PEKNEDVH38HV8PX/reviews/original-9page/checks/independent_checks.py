"""Review checks written independently of verify_sampling.py.
All output stays beside this file; no manuscript is modified.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib, itertools, json, math
import numpy as np
import mpmath as mp
from scipy.linalg import expm
from scipy.optimize import differential_evolution

ROOT=Path(__file__).resolve().parent
mp.mp.dps=75
checks={}

def atan_interval(x, n=180):
    # A different identity from the supplied Machin implementation:
    # pi = 4*(atan(1/2)+atan(1/3)), by the tangent addition formula.
    s=Q(0)
    for j in range(n): s+=(-1)**j*x**(2*j+1)/Q(2*j+1)
    v=s+(-1)**n*x**(2*n+1)/Q(2*n+1)
    return min(s,v),max(s,v)

def exp_interval(x, n=180):
    # Direct alternating Taylor polynomial, with the Lagrange remainder.
    # Unlike the supplied code, no reciprocal of a positive exp sum is used.
    term=Q(1); s=term
    for j in range(1,n+1):
        term*=(-x)/j; s+=term
    v=s+term*(-x)/(n+1)
    return min(s,v),max(s,v)

pa,pb=atan_interval(Q(1,2)); pc,pd=atan_interval(Q(1,3))
pl,ph=4*(pa+pc),4*(pb+pd)
assert pl<ph and ph-pl<Q(1,10**108)
nlist=range(1,40,2)
ss=sum((Q(1,n*n) for n in nlist),Q(0))
ll=hh=Q(0)
for n in nlist:
    al,ah=exp_interval(Q(13*n,100)); bl,bh=exp_interval(Q(52*n,100))
    assert 0<al<ah and 0<bl<bh
    ll+=(2*al-bh+3)/n**2
    hh+=(2*ah-bl+3)/n**2
gl=4*ll/ph-2*ph; gh=4*hh/pl-2*pl
al=12*ss/ph; ah=12*ss/pl
bl=pl/2-4*ss/pl; bh=ph/2-4*ss/ph
assert Q('0.11365')<gl<gh<Q('0.11366')
assert Q('4.66465243')<al<ah<Q('4.66465244')
assert Q('0.01591218')<bl<bh<Q('0.01591219')
expo=Q(40500)*gl**2/(8*ah**2)
assert expo>3
assert sum((Q(3)**j/Q(math.factorial(j)) for j in range(11)),Q(0))>20
checks['independent_rational']={
    'pi_identity':'4*(atan(1/2)+atan(1/3))',
    'exp_method':'direct alternating Taylor polynomials, Lagrange remainder',
    'g':float(gl),'A':float(ah),'b20':float(bl),
    'exponent_lower':float(expo),'each_error_upper_numeric':math.exp(-float(expo)),
    'eta_B10_strict_upper_numeric':float(gl/(ah*14)),
    'all_exact_interval_assertions':True}
certificate={'pi_lower':str(pl),'pi_upper':str(ph),
             'g_lower':str(gl),'g_upper':str(gh),'A_lower':str(al),'A_upper':str(ah),
             'b20_lower':str(bl),'b20_upper':str(bh),'exponent_lower':str(expo)}
(ROOT/'independent-rational-certificate.json').write_text(json.dumps(certificate,indent=2),encoding='utf8')

F=lambda s: mp.pi/2-4/mp.pi*(mp.polylog(2,mp.exp(-s))-mp.polylog(2,mp.exp(-2*s))/4) if s else mp.mpf(0)
asym=[]
for e in (2,4,8,16,30):
    delta=mp.mpf(10)**(-e)
    asym.append({'Delta':str(delta),'scaled_triangle_function':str(mp.pi*(F(4*delta)-2*F(delta))/(2*delta*mp.log(1/delta)))})
checks['small_spacing_limit_to_2']=asym

# Verify the cut integral with adversarial coincident, antipodal and collinear phases.
phase_sets=[[0,0,0],[0,math.pi,0,math.pi],[0,math.pi/2,math.pi,3*math.pi/2],[-7,0,0,11,2*math.pi]]
cuterr=0.
for phases in phase_sets:
    p=np.mod(phases,2*np.pi); d=len(p)
    knots=np.unique(np.r_[0,2*np.pi,p,np.mod(p+np.pi,2*np.pi)])
    acc=np.zeros((d,d))
    for a,b in zip(knots[:-1],knots[1:]):
        flag=(np.mod(p-(a+b)/2,2*np.pi)<np.pi).astype(int)
        acc+=(b-a)/2*np.abs(flag[:,None]-flag[None,:])
    target=np.abs(np.mod(p[:,None]-p[None,:]+np.pi,2*np.pi)-np.pi)
    cuterr=max(cuterr,float(np.max(abs(acc-target))))
assert cuterr<1e-12
checks['circle_boundary_cases_max_error']=cuterr

# Search the actual truncated null statistic over all qutrit phases numerically.
odd=np.arange(1,40,2)
def rk(x): return np.pi/2-4/np.pi*np.sum(np.cos(odd*x)/odd**2)
def stat(v): return rk(v[0]+v[1])-rk(v[0])-rk(v[1])
opt=differential_evolution(lambda v:-stat(v),[(-np.pi,np.pi)]*2,seed=791,maxiter=400,popsize=25,tol=1e-10)
checks['qutrit_null_numerical_optimization']={'max_found':float(-opt.fun),'paper_upper':float(3*bh),'status':'numerical search, not a global proof'}
assert -opt.fun<=3*float(bh)+1e-10

# Independent Fourier quadrature of the full 4-level density, not only qutrit.
# A rational grid example with pair r's all small; Haar gauge theta_4=0.
L=48
mesh=np.meshgrid(*([2*np.pi*np.arange(L)/L]*3),indexing='ij')
theta=np.stack([*mesh,np.zeros_like(mesh[0])],axis=-1)
pairs=list(itertools.combinations(range(4),2))
rs=[.01,.02,.03,.04,.05,.06]
q=np.ones(theta.shape[:-1])
for (i,j),r in zip(pairs,rs):
    x=theta[...,i]-theta[...,j]
    q+=(1-r*r)/(1-2*r*np.cos(x)+r*r)-1
lower=1-sum(2*r/(1+r) for r in rs)
assert lower>0 and q.min()>=lower-1e-12
momenterr=0.
for (i,j),r in zip(pairs,rs):
    for n in (1,2,3,5,9):
        v=np.mean(q*np.exp(-1j*n*(theta[...,i]-theta[...,j])))
        momenterr=max(momenterr,float(abs(v-r**n)))
assert abs(q.mean()-1)<1e-12 and momenterr<1e-12
checks['four_level_grid_density']={'min_numeric':float(q.min()),'analytic_lower':lower,'mean':float(q.mean()),'moments_max_error':momenterr}

# Independent physical estimator for generic nonunital CPTP channels.
rng=np.random.default_rng(74359)
phase_error=0.; surrogate_error=0.; clock_excess=-1.
for d in (2,3,5):
    for trial in range(12):
        # Isometry defines Kraus matrices including population transitions.
        raw=rng.normal(size=(3*d,d))+1j*rng.normal(size=(3*d,d))
        iso=np.linalg.qr(raw)[0]; ks=[iso[r*d:(r+1)*d,:] for r in range(3)]
        channel=lambda z: sum((k@z@k.conj().T for k in ks))
        hraw=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)); H=(hraw+hraw.conj().T)/2
        vals,vecs=np.linalg.eigh(H); t=float(rng.uniform(.1,3)); eps=.0007
        U=expm(-1j*t*H); U2=expm(-1j*(t+eps)*H)
        for i,j in itertools.combinations(range(d),2):
            E=np.zeros((d,d),complex); E[i,j]=1
            P=np.zeros((d,d),complex); P[i,i]=P[j,j]=1
            X=E+E.conj().T; Y=-1j*(E-E.conj().T)
            m=sum(s*np.trace(A@channel((P+s*A)/2)).real/4 for A in (X,Y) for s in (-1,1))
            phase_error=max(phase_error,abs(m-channel(E)[i,j].real))
            spectral=sum(abs(vecs[i,a])**2*abs(vecs[j,b])**2*np.exp(-1j*t*(vals[a]-vals[b])) for a in range(d) for b in range(d))
            direct=(U@E@U.conj().T)[i,j]
            surrogate_error=max(surrogate_error,float(abs(spectral-direct)))
            direct2=(U2@E@U2.conj().T)[i,j]
            clock_excess=max(clock_excess,abs(direct2.real-direct.real)-(vals[-1]-vals[0])*eps)
assert phase_error<1e-12 and surrogate_error<1e-12 and clock_excess<=1e-12
checks['general_channels']={'nonunital_phase_max_error':phase_error,'surrogate_explicit_joint_sum_error':surrogate_error,'width_Lipschitz_max_excess':clock_excess}

checks['hashes']={name:hashlib.sha256((ROOT.parent/name).read_bytes()).hexdigest() for name in ['sampling-arithmetic.pdf','sampling-arithmetic.tex']}
checks['status']='PASS'
(ROOT/'independent-results.json').write_text(json.dumps(checks,indent=2),encoding='utf8')
print(json.dumps(checks,indent=2))

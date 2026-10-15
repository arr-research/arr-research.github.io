"""Reproduce the finite arithmetic certificate and numerical cross-checks.
Exact claims use fractions.Fraction; floating checks are explicitly labelled.
Run: python verify_sampling.py --out DIRECTORY
Dependencies for numerical checks: numpy, scipy.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse, json, math, hashlib, sys
sys.set_int_max_str_digits(200000)
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog

ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).parent)
OUT=ap.parse_args().out;OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def check(name,ok,**details):
    assert bool(ok), (name,details)
    checks.append(dict(name=name,status='PASS',**details))

def atan_bounds(x,n):
    s=sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(n)),Q(0))
    t=(-1)**n*x**(2*n+1)/Q(2*n+1)
    return min(s,s+t),max(s,s+t)
lo5,hi5=atan_bounds(Q(1,5),100);lo239,hi239=atan_bounds(Q(1,239),30)
pi_lo,pi_hi=16*lo5-4*hi239,16*hi5-4*lo239
check('Machin bracket width',0<pi_hi-pi_lo<Q(1,10**130))

def expneg_bounds(x,n=160):
    term=Q(1);s=term
    for j in range(1,n+1):term*=x/j;s+=term
    nxt=term*x/(n+1)
    ratio=x/(n+2)
    assert ratio<1
    return 1/(s+nxt/(1-ratio)),1/s

odd=range(1,40,2);S=sum((Q(1,n*n) for n in odd),Q(0))
Flo=Fhi=Q(0)
for n in odd:
    a,b=expneg_bounds(Q(13*n,100));c,d=expneg_bounds(Q(52*n,100))
    Flo+=(2*a-d+3)/(n*n);Fhi+=(2*b-c+3)/(n*n)
glo=4*Flo/pi_hi-2*pi_hi;ghi=4*Fhi/pi_lo-2*pi_lo
Alo=12*S/pi_hi;Ahi=12*S/pi_lo
blo=pi_lo/2-4*S/pi_lo;bhi=pi_hi/2-4*S/pi_hi
check('exact qutrit margin enclosure',Q(11365,100000)<glo<ghi<Q(11366,100000),lower=float(glo),upper=float(ghi))
check('exact amplitude enclosure',Q('4.66465243')<Alo<Ahi<Q('4.66465244'))
check('exact Fourier tail enclosure',Q('0.01591218')<blo<bhi<Q('0.01591219'))
exponent=40500*glo*glo/(8*Ahi*Ahi)
check('40500-shot exponent exceeds three',exponent>3,lower=float(exponent))
check('exp(3) exceeds 20',sum((Q(3)**k/math.factorial(k) for k in range(11)),Q(0))>20)
check('coarse-grid positivity rational certificate',1-Q(4,5)-Q(2,257)==Q(247,1285))
exact={'method':'exact rational arithmetic, Machin alternating sums and exponential Taylor/geometric tails',
       'pi_lower':str(pi_lo),'pi_upper':str(pi_hi),'g_lower':str(glo),'g_upper':str(ghi),
       'A_upper':str(Ahi),'shot_exponent_lower':str(exponent)}
(OUT/'exact-certificate.json').write_text(json.dumps(exact,indent=2),encoding='utf8')

# Exact bounded-uniform-time extension, h=1/20, eta=1/10000.
h=Q(1,20);eta=Q(1,10000);delta=Q(13,100)
def ch_bounds(n,gamma):
    al,au=expneg_bounds(n*gamma*(delta-h));bl,bu=expneg_bounds(n*gamma*(delta+h))
    den=2*n*gamma*h
    return (al-bu)/den,(au-bl)/den
Tlo=Thi=Q(0)
for n in range(1,40,2):
    al,au=ch_bounds(n,Q(1));bl,bu=ch_bounds(n,Q(4))
    Tlo+=(2*al-bu+3)/(n*n);Thi+=(2*au-bl+3)/(n*n)
Llo=12/(pi_hi*h)*sum((Q(1,n**3) for n in range(1,40,2)),Q(0))
Lhi=12/(pi_lo*h)*sum((Q(1,n**3) for n in range(1,40,2)),Q(0))
dither_lo=4*Tlo/pi_hi-2*pi_hi-eta*(Lhi+4*Ahi)
dither_hi=4*Thi/pi_lo-2*pi_lo-eta*(Llo+4*Alo)
check('exact dither gap enclosure',Q('0.09992')<dither_lo<dither_hi<Q('0.09993'),lower=float(dither_lo),upper=float(dither_hi))
check('53000-shot dither exponent exceeds three',53000*dither_lo**2/(8*Ahi**2)>3,lower=float(53000*dither_lo**2/(8*Ahi**2)))
exact.update(dither_gap_lower=str(dither_lo),dither_gap_upper=str(dither_hi),dither_L_upper=str(Lhi))
(OUT/'exact-certificate.json').write_text(json.dumps(exact,indent=2),encoding='utf8')

rng=np.random.default_rng(20261015)
# Direct matrix evolution: surrogate and four physical preparation/readout phases.
for d in range(2,7):
    err_sur=err_phase=0.
    for repetition in range(8):
        raw=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));H=(raw+raw.conj().T)/2
        t=float(rng.uniform(0,4));U=expm(-1j*t*H);val,V=np.linalg.eigh(H)
        weights=np.abs(V)**2;phi=weights@np.exp(-1j*t*val)
        for i in range(d):
            for j in range(i+1,d):
                E=np.zeros((d,d),complex);E[i,j]=1
                target=(U@E@U.conj().T)[i,j]
                err_sur=max(err_sur,abs(target-phi[i]*phi[j].conjugate()))
                X=E+E.conj().T;Y=-1j*E+1j*E.conj().T
                P=np.zeros((d,d));P[i,i]=P[j,j]=1
                mean=0.
                for A in (X,Y):
                    for sign in (-1,1):
                        rho=(P+sign*A)/2
                        outcome=np.trace(A@U@rho@U.conj().T).real
                        assert abs(outcome)<=1+1e-12
                        mean+=sign*outcome/4
                err_phase=max(err_phase,abs(mean-target.real))
    check(f'physical phase estimator and surrogate, d={d}',max(err_sur,err_phase)<1e-12,
          surrogate_max_error=err_sur,phase_max_error=err_phase)

# Exact Fourier coefficients checked independently by periodic trapezoidal integration.
L=512;theta=2*np.pi*np.arange(L)/L
x=theta[:,None];y=theta[None,:]
def poisson(r,z):return (1-r*r)/(1-2*r*np.cos(z)+r*r)
q=poisson(.25,x-y)+poisson(1/256,x)+poisson(.25,y)-2
check('grid density normalizes numerically',abs(q.mean()-1)<1e-12,mean=float(q.mean()))
check('grid density positive numerically',q.min()>float(Q(247,1285))-1e-12,minimum=float(q.min()))
err=0.
for z,r in [(x-y,.25),(x,1/256),(y,.25)]:
    for n in range(1,21):err=max(err,abs(np.mean(q*np.exp(-1j*n*z))-r**n))
check('all three grid marginals, first twenty harmonics',err<1e-12,max_error=float(err))

# Circular cut integral, piecewise exact in floating phase endpoints.
for d in [3,5,9]:
    phase=rng.uniform(0,2*np.pi,d)
    knots=np.sort(np.r_[0,2*np.pi,phase,(phase+np.pi)%(2*np.pi)])
    cut_sum=np.zeros((d,d))
    for a,b in zip(knots[:-1],knots[1:]):
        s=((phase-(a+b)/2)%(2*np.pi)<np.pi).astype(float)
        cut_sum+=(b-a)/2*np.abs(s[:,None]-s[None,:])
    exact_rho=np.abs((phase[:,None]-phase[None,:]+np.pi)%(2*np.pi)-np.pi)
    check(f'circle cut integral, d={d}',np.max(abs(cut_sum-exact_rho))<1e-12)

# Uniform Fourier-tail and triangle-functional bound over a dense phase grid.
K=20;n=np.arange(1,2*K,2,dtype=float)
theta=np.linspace(-np.pi,np.pi,4001)
rhoK=np.pi/2-4/np.pi*np.sum(np.cos(theta[:,None]*n)/n**2,axis=1)
b=np.pi/2-4/np.pi*np.sum(1/n**2)
check('uniform triangular-wave approximation on mesh',np.max(abs(rhoK-abs(theta)))<=b+1e-12,
      maximum_error=float(np.max(abs(rhoK-abs(theta)))))
for z in range(8):
    phase=rng.uniform(-np.pi,np.pi,(1000,3));p=np.array([[0,1],[1,2],[0,2]])
    diff=phase[:,p[:,0]]-phase[:,p[:,1]]
    D=np.pi/2-4/np.pi*np.sum(np.cos(diff[:,:,None]*n)/n**2,axis=2)
    stat=D[:,2]-D[:,0]-D[:,1]
    check(f'finite static-null inequality random phases batch {z}',np.max(stat)<=3*b+1e-12)

# A genuine shared static energy mixture fits two incommensurate times.
times=np.array([.13,.13*np.sqrt(2)])
Gamma=np.array([[0,1,4],[1,0,1],[4,1,0]],float);pairs=[(0,1),(0,2),(1,2)]
energies=np.vstack([np.zeros((1,3)),np.c_[rng.normal(size=(12000,2))*3,np.zeros(12000)],
                   np.c_[rng.uniform(-1500,1500,(12000,2)),np.zeros(12000)]])
rows=[np.ones(len(energies))];rhs=[1.]
for t in times:
    for i,j in pairs:
        phase=t*(energies[:,i]-energies[:,j]);rows.extend([np.cos(phase),np.sin(phase)])
        rhs.extend([np.exp(-t*Gamma[i,j]),0.])
mat=np.array(rows);rhs=np.array(rhs)
fit=linprog(np.zeros(len(energies)),A_eq=mat,b_eq=rhs,bounds=(0,None),method='highs',
            options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
check('finite-menu LP feasible',fit.success,message=fit.message)
idx=np.flatnonzero(fit.x>1e-10);weights=fit.x[idx]
res=np.max(abs(mat[:,idx]@weights-rhs))
check('finite-menu shared mixture residual',res<1e-8 and len(idx)<=13,
      residual=float(res),atoms=len(idx),maximum_spectral_width=float(np.ptp(energies[idx],axis=1).max()))
(OUT/'two-time-alias.json').write_text(json.dumps({'times':times.tolist(),'rates':Gamma.tolist(),
    'weights':weights.tolist(),'energies':energies[idx].tolist(),'residual':float(res),
    'status':'floating-point illustration; the exact existence theorem is in the manuscript'},indent=2),encoding='utf8')

report={'status':'PASS','assertion_groups':len(checks),'checks':checks,
        'rigorous_numeric_claim':'20-time, 40500-shot constants certified with exact rational arithmetic',
        'limitations':'Numerical grid and LP checks do not prove the general theorems. No proof-assistant claim.',
        'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'verification.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps({'status':'PASS','assertion_groups':len(checks),'g':float(glo),'A':float(Ahi),
                  'exponent_lower':float(exponent),'LP_atoms':len(idx),'LP_residual':float(res)},indent=2))

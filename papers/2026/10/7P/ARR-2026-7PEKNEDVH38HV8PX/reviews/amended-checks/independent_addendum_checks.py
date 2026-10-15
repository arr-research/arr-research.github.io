"""Independent checks for the added uniform-clock results; no manuscript edits."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib, json, math
import numpy as np

P=Path(__file__).resolve().parent
def atan_bounds(x,n=180):
    s=sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(n)),Q())
    t=s+(-1)**n*x**(2*n+1)/Q(2*n+1)
    return min(s,t),max(s,t)

def exp_bounds(x,n=220):
    assert 0 <= x < n+1  # The omitted alternating tail decreases in magnitude.
    t=Q(1); s=t
    for j in range(1,n+1):
        t*=-x/j; s+=t
    v=s+t*(-x)/(n+1)
    return min(s,v),max(s,v)

la,ha=atan_bounds(Q(1,2)); lb,hb=atan_bounds(Q(1,3))
pl,ph=4*(la+lb),4*(ha+hb)
delta=Q(13,100); h=Q(1,20); eta=Q(1,10000)
ns=list(range(1,40,2)); s2=sum((Q(1,n*n) for n in ns),Q()); s3=sum((Q(1,n**3) for n in ns),Q())
al,ah=12*s2/ph,12*s2/pl
ul,uh=3*pl/2-12*s2/pl,3*ph/2-12*s2/ph
ll,lh=12*s3/(ph*h),12*s3/(pl*h)
def ch_bounds(n,gamma):
    if gamma==0:return Q(1),Q(1)
    p,q=exp_bounds(n*gamma*(delta-h)); r,s=exp_bounds(n*gamma*(delta+h))
    return (p-s)/(2*n*gamma*h),(q-r)/(2*n*gamma*h)
tl=th=Q()
for n in ns:
    l1,h1=ch_bounds(n,Q(1)); l4,h4=ch_bounds(n,Q(4))
    tl+=(2*l1-h4)/n**2; th+=(2*h1-l4)/n**2
assert 0 < tl < th  # Needed for monotonicity of the quotient in pi below.
vl,vh=-ph/2+4*tl/ph,-pl/2+4*th/pl
gl,gh=vl-uh-eta*(lh+4*ah),vh-ul-eta*(ll+4*al)
assert Q('0.09992')<gl<gh<Q('0.09993')
exponent=53000*gl**2/(8*ah**2)
assert exponent>3
assert sum((Q(3)**k/Q(math.factorial(k)) for k in range(11)),Q())>20
cert={'pi_lower':str(pl),'pi_upper':str(ph),'Vh_lower':str(vl),'Vh_upper':str(vh),
      'U_lower':str(ul),'U_upper':str(uh),'Lh_lower':str(ll),'Lh_upper':str(lh),
      'g_lower':str(gl),'g_upper':str(gh),'exponent_lower':str(exponent)}
(P/'independent-dither-rational-certificate.json').write_text(json.dumps(cert,indent=2),encoding='utf8')

# Closed-form averaged phase under a deterministic offset, with arbitrarily high frequencies.
# Uniform time law on [n(delta-h),n(delta+h)] has characteristic function
# exp(i*n*delta*x)*sinc(n*h*x). The real parts test each physical two-level coherence.
worst_excess=-1.
for n in (1,3,9,39):
    for shift in (0.,float(eta),-float(eta),.001,.1):
        freq=np.r_[0.,np.geomspace(1e-4,1e12,30000)]
        ideal=np.cos(n*float(delta)*freq)*np.sinc(n*float(h)*freq/np.pi)
        actual=np.cos((n*float(delta)+shift)*freq)*np.sinc(n*float(h)*freq/np.pi)
        tv=min(1.,abs(shift)/(2*n*float(h)))
        worst_excess=max(worst_excess,float(np.max(abs(actual-ideal))-2*tv))
assert worst_excess<=1e-12

# Rounding violates independence from S and can produce order-one bias with tiny errors.
# This is a counterexample to extending the theorem beyond its stated assumptions,
# not to the theorem itself. Use period 2*eta and frequency pi/eta.
period=2*float(eta); x=2*np.pi/period
t=np.linspace(float(delta-h),float(delta+h),100003)
rounded=np.round(t/period)*period
actual=np.cos(x*rounded).mean()
ideal=math.cos(float(delta)*x)*np.sinc(float(h)*x/np.pi)
rounding_bias=abs(actual-ideal)
assert np.max(abs(rounded-t))<=float(eta)+1e-12 and rounding_bias>.99

# Preserve a fingerprint of the original report; this script never modifies it.
old=P.parent.parent/'astra-packet'/'astra-review.txt'
data={
 'status':'PASS',
 'tex_sha256':hashlib.sha256((P.parent/'sampling-arithmetic.tex').read_bytes()).hexdigest(),
 'original_report_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),
 'g':float(gl),'A':float(ah),'Lh':float(lh),'Vh':float(vl),'U':float(uh),
 'null_upper_with_error':float(uh+eta*lh),'reference_lower_with_error':float(vl-eta*4*ah),
 'midpoint_threshold':float((uh+eta*lh+vl-eta*4*ah)/2),
 'shot_exponent_lower':float(exponent),'each_error_bound_numeric':math.exp(-float(exponent)),
 'actual_time_lower':float(delta-h-eta),'actual_time_upper':float(39*(delta+h)+eta),
 'uniform_shift_cosine_check_max_excess':worst_excess,
 'excluded_rounding_example':{'max_timing_error':float(np.max(abs(rounded-t))),'coherence_bias':float(rounding_bias),'nominal_independent_shift_bound':float(eta/h),'status':'outside theorem assumptions, deliberately retained'},
 'energy_cost_example_eta_0_0001':float(Q('0.11365')/(ah*eta)-4),
 'limitation':'Numerical checks are not universal proofs. Rational certificate bounds constants only.'
}
(P/'independent-addendum-results.json').write_text(json.dumps(data,indent=2),encoding='utf8')
print(json.dumps(data,indent=2))

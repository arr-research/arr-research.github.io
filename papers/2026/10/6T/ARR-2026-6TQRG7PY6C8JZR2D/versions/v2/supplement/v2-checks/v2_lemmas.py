# Checks for Lemmas A-C of version 2 (baseline gaps, pair-factor inequality, Theorem 11 construction)
import numpy as np, mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps = 60
s = np.linspace(0,1,2000001)
# Lemma A(i): H_{1/2}(s)=(1-s)^4(1-4s)^2 <= e^{-3s}
H = (1-s)**4*(1-4*s)**2
print("A(i) max H e^{3s} =", np.max(H*np.exp(3*s)))
# A(ii): c in [0.4,0.6]: H_c <= e^{-2s}
worst=0
for c in np.linspace(0.4,0.6,201):
    Hc=(1-s)**4*(1-2*s/(1-c))**2
    worst=max(worst,np.max(Hc*np.exp(2*s)))
print("A(ii) max H_c e^{2s} =", worst)
# secondary max formula
for c in [0,0.25,0.5,0.75]:
    Hc=(1-s)**4*(1-2*s/(1-c))**2
    mask=s>(1-c)/2
    print("c=",c," numeric sec max",Hc[mask].max()," formula",(1+c)**6/(729*(1-c)**2), " s*",s[mask][Hc[mask].argmax()],(2-c)/3)
# f(c) increasing, value at 3/4
print("(7/4)^6*16/729 =", Fr(7,4)**6*16/729, float(Fr(7,4)**6*16/729))
# pair-factor identity (exact), random tests
rng=np.random.default_rng(1)
bad=0
for _ in range(100000):
    x=rng.uniform(-3,6); y=rng.uniform(0,6); th=rng.uniform(-np.pi,np.pi)
    v=complex(x,y); z=np.exp(1j*th); sv=np.sin(th/2)**2
    lhs=abs(1+v*(z-1))**2*abs(1+np.conj(v)*(z-1))**2
    U=x*x+y*y; V=(x-1)**2+y*y
    rhs=1+8*(x*x-x-y*y)*sv+16*U*V*sv**2
    ub=np.exp(4*(U+V)*sv)
    if abs(lhs-rhs)>1e-8*max(1,abs(rhs)) or lhs>ub*(1+1e-12): bad+=1
print("pair identity/bound failures:",bad)
# A(iii) Theorem 11 baseline: sup_{s>=0.1} H<=? at centre and perturbed
a0,c0=-2/3,3/4
ss=s[s>=0.1]
def H11(a,c,ss): return (1-2*ss/(1-a))**30*(1-2*ss/(1-c))**4
print("centre sup_{s>=.1}H=",H11(a0,c0,ss).max(), " (3/4)^30(2/3)^4=",0.75**30*(2/3)**4)
w=0
for da in np.linspace(-0.02,0.02,21):
  for dc in np.linspace(-0.02,0.02,21):
    w=max(w,H11(a0+da,c0+dc,ss).max())
print("perturbed |da|,|dc|<=0.02 sup_{s>=.1}H =",w)
# Theorem 11 construction at huge n (mpmath)
def build(n):
    n=mp.mpf(n); 
    nn=int(n)
    v=mp.findroot(lambda v: v**3-1.5*v**2-(n-1)/4, (n/4)**(mp.mpf(1)/3)+1)
    m,k=divmod(nn-1,34)
    d=(v**2/(v-1)-mp.mpf(k)/2)/m; t=(-v**2-mp.mpf(k)/4)/m
    L=(51+d)/2; U=17-t
    X=(U*L+221+mp.sqrt((U*L-289)*(U*L-169)))/(30*U); Y=(L-15*X)/2
    return nn,m,k,v,X,Y,d,t
for n in [10**4+7, 10**6+3, 10**9+33, 10**15+1]:
    nn,m,k,v,X,Y,d,t=build(n)
    a=1-X;c=1-Y
    D=-30*a-4*c-17; T=-15*a/(1-a)-2*c/(1-c)
    print(nn,"k=",k," D-d=",mp.nstr(D-d,3)," T-t=",mp.nstr(T-t,3)," a=",mp.nstr(a,8)," c=",mp.nstr(c,8)," |1-a|<1",abs(a)<1,abs(c)<1)

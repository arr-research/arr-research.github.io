from mpmath import mp, mpf, mpc, exp, cos, sin, sqrt, pi, polyroots, fabs
import random
mp.dps=50
random.seed(1)
mx=0
for _ in range(200):
    x=mpf(random.uniform(0.6,30)); y=mpf(random.uniform(0.0,30)); s=mpf(random.uniform(0,1)); v=mpf(random.uniform(1.01,40))
    th=2*mp.asin(sqrt(s)); z=exp(1j*th)
    # real
    be=1-1/v; f=lambda z:1-z/be
    mx=max(mx,fabs(fabs(f(z))**2/f(1)**2-(1+4*v*(v-1)*s)))
    # pair
    V=mpc(x,y); b=1-1/V; bc=b.conjugate()
    g=lambda z:(1-z/b)*(1-z/bc)
    Y=y*y;U=x*x+Y;Vv=(x-1)**2+Y
    lhs=fabs(g(z))**2/fabs(g(1))**2
    mx=max(mx,fabs(lhs-(1+8*(x*x-x-Y)*s+16*U*Vv*s*s)))
    mx=max(mx,fabs(U*Vv-(x*x-x-Y)**2-(2*x-1)**2*Y))
    B=lambda z:(1+z)**4*(1-z+z*z)
    mx=max(mx,fabs(fabs(B(z))**2/256-(1-s)**4*(1-4*s)**2))
    mx=max(mx,fabs(fabs(B(z))**2/256-cos(th/2)**6*cos(3*th/2)**2))
print('max err',mx)
# b_j via roots
rts=polyroots([1,-1+0j,1][::-1] if False else [1,-1,1])  # z^2-z+1
print([ (1/(1-r)) for r in rts])
for j in range(1,6):
    print(j, 4*mpf(1)/2**j+sum((1/(1-r))**j for r in rts))
# max of (1-s)^4(1-4s)^2 e^{3s}
mxv=max((1-s)**4*(1-4*s)**2*exp(3*s) for s in [mpf(i)/20000 for i in range(20001)])
print('max Bratio*e^{3s}',mxv)

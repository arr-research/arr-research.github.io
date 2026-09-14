"""Relative margin of the key inequality Var J > E J on (0, kappa_L]:  R(kappa) = (Var J - E J)/E J,
and the same for the crude geometric-type bounds, for a range of q (mpmath, series)."""
import sys, json
from mpmath import mp, mpf, sqrt, findroot
mp.dps = 30
def Sk(q, k, N=None):
    k = mpf(k); z = k*k
    if N is None: N = int(k) + 80
    S0 = S1 = S2 = mpf(0); w = mpf(1)
    for j in range(N):
        S0 += w; S1 += j*w; S2 += j*j*w
        w = w*z/((q+2*j+1)*(q+2*j+2))
    return S0, S1, S2
def R(q, k):
    S0, S1, S2 = Sk(q, k)
    E = S1/S0; V = S2/S0 - E*E
    return (V - E)/E, E, V, 1/S0
out = []
for q in [int(a) for a in sys.argv[1:]] or [4,5,6,8,10,15,20,30,50,80,120,200]:
    kL = findroot(lambda x: Sk(q, x)[0] - mpf(q*(q-1))/8, (mpf('0.01'), mpf(4*q+100)), solver='bisect', tol=mpf('1e-15'))
    grid = [kL*i/400 for i in range(1, 401)]
    vals = [(float(R(q, g)[0]), float(g)) for g in grid]
    mn = min(vals)
    # also margin at kappa = q/2, q, kappa_L and the r0 = kappa^2/((q+1)(q+2)) values
    r = dict(q=q, kappa_L=float(kL), kL_over_q=float(kL/q), minR=mn[0], argmin=mn[1], argmin_over_q=mn[1]/q,
             R_at_q2=float(R(q, q/2)[0]) if q/2 < kL else None, R_at_q=float(R(q, q)[0]) if q < kL else None,
             R_at_kL=float(R(q, kL)[0]), p0_at_q=float(R(q, q)[3]) if q < kL else None,
             R_small=[(float(g), float(R(q, g)[0])) for g in [kL/400, kL/100, kL/20, kL/5]])
    print(json.dumps(r)); sys.stdout.flush(); out.append(r)
json.dump(out, open('margins.json', 'w'), indent=1)

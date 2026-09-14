"""Numerical sanity check of the intermediate claims of the two-sided Lyapunov argument (not part of the proof):
  Q := T - (q - 1/2) h along the trajectory.
  (a) Q < 0 on (0, kappa_L];  (b) d(e^{c tau} Q)/dtau <= 0 on (0, kappa_L]  (identity: = e^{c tau}[X^2(8 - q(q-1)u) + h B], B >= 0);
  (c) Q > 0 on [kappa_f, Kmax];  (d) d(e^{c tau} Q)/dtau > 0 on [kappa_f, Kmax];  (e) h < 0 on (0,kappa_L], h > 0 on (kappa_f, Kmax];
  (f) for q = 2, 3 with c = 2, q-1/2: h > 0 and Q > 0 on (0, Kmax] (no fold).
Also compares the identity-based derivative with a finite difference."""
from mpmath import mp, mpf, findroot, diff
mp.dps = 30
from num_phi import Sk, state
def Q_of(q, k, c):
    s = state(q, k); return s['T'] - c*s['h'] if 'h' in s else s['T'] - c*k*s['H']
def dQe(q, k, c):
    s = state(q, k); X, u, h = s['X'], s['u'], k*s['H']
    B = (2*c-4)*X + c*(2*q-1-c) - q*(q-1)*u
    return k**c*(X**2*(8 - q*(q-1)*u) + h*B), B
for q in [4, 5, 6, 10, 30, 60]:
    c = q - mpf(1)/2
    kL = findroot(lambda x: Sk(q, x)[0] - mpf(q*(q-1))/8, (mpf('0.01'), mpf(4*q+100)), solver='bisect', tol=mpf('1e-15'))
    Kmax = 4*q + 40
    grid = [mpf(i)/200*Kmax for i in range(1, 201)]
    kf = findroot(lambda x: state(q, x)['H'], (kL, mpf(Kmax)), solver='bisect', tol=mpf('1e-15'))
    pre = [g for g in grid if g <= kL] + [kL]
    post = [kf] + [g for g in grid if g > kf]
    a = all(Q_of(q, g, c) < 0 for g in pre)
    b = all(dQe(q, g, c)[0] <= 0 for g in pre)
    cc = all(Q_of(q, g, c) > 0 for g in post)
    d = all(dQe(q, g, c)[0] > 0 for g in post)
    e = all(state(q, g)['H'] < 0 for g in pre) and all(state(q, g)['H'] > 0 for g in post[1:])
    Bmin = min(dQe(q, g, c)[1] for g in grid)
    # finite-difference check of the identity at two points
    def Qe(k): return k**c*Q_of(q, k, c)
    fd = max(abs(diff(Qe, k0)*k0 - dQe(q, k0, c)[0])/abs(dQe(q, k0, c)[0]) for k0 in [kL/2, kf, kf+3])
    print("q=%d kL=%.4f kf=%.4f  (a)Q<0 pre:%s (b)dQe<=0 pre:%s (c)Q>0 post:%s (d)dQe>0 post:%s (e)signs h:%s  minB=%.3f  identity vs FD rel.err=%.1e"
          % (q, kL, kf, a, b, cc, d, e, Bmin, fd))
for q, c in [(2, mpf(2)), (3, mpf(5)/2)]:
    grid = [mpf(i)/200*60 for i in range(1, 201)]
    print("q=%d c=%s: h>0 all:%s  Q>0 all:%s  dQe>0 all:%s  minB=%.3f" % (q, c, all(state(q, g)['H'] > 0 for g in grid),
          all(Q_of(q, g, c) > 0 for g in grid), all(dQe(q, g, c)[0] > 0 for g in grid), min(dQe(q, g, c)[1] for g in grid)))

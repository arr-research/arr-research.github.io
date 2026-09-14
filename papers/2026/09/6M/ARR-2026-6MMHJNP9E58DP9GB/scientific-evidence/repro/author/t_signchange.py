"""Sign change kappa_T of T along the trajectory (T = kappa^2 Delta - (X+2) h) versus kappa_L, and the
maximum of u*X = P(K=q|A) E[K-q|A] on (0, kappa_L] (numerical remarks for the report)."""
from mpmath import mp, mpf, findroot
mp.dps = 30
from num_phi import Sk, state
for q in [4,5,6,7,8,10,15,20,30,40,60]:
    kL = findroot(lambda x: Sk(q, x)[0] - mpf(q*(q-1))/8, (mpf('0.01'), mpf(4*q+100)), solver='bisect', tol=mpf('1e-15'))
    grid = [mpf(i)/100 for i in range(1, int(4*q*100)+1)]
    Tv = [state(q, g)['T'] for g in grid]
    ch = [grid[i] for i in range(1, len(grid)) if Tv[i-1]*Tv[i] < 0]
    uX = max(state(q, g)['u']*state(q, g)['X'] for g in grid if g <= kL)
    print("q=%d kappa_L=%.4f  sign changes of T along trajectory at %s ; max uX on (0,kappa_L] = %.4f" % (q, kL, [float(c) for c in ch], uX))

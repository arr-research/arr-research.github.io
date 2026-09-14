"""(a) numerical check of [kappa^4] Phi_q = -4(2q+5)(q^2-q-8)/((q+1)^2(q+2)^2(q+3)(q+4)) (reviewer's [kappa^2]Delta);
(b) Lemma C: Var J > E J whenever 2*gamma*(1+r0)*(1-gamma*r0)^4 > 1; report the covered range r0 <= r0max(q)
    and confirm Var J - E J > 0 there (and the lower bound used) on a grid."""
from mpmath import mp, mpf, findroot
mp.dps = 40
from num_phi import Phi, Sk
for q in [4, 5, 10, 30]:
    c = -4*(2*q+5)*(q*q-q-8)/mpf((q+1)**2*(q+2)**2*(q+3)*(q+4))
    for k in [mpf('0.01'), mpf('0.001')]:
        print("q=%d kappa=%s Phi/kappa^4 = %s   predicted %s" % (q, k, mp.nstr(Phi(q, k)/k**4, 12), mp.nstr(c, 12)))
print()
for q in [4, 5, 6, 8, 10, 20, 50, 100, 1000, 10**5]:
    gam = mpf((q+1)*(q+2))/((q+3)*(q+4))
    f = lambda r: 2*gam*(1+r)*(1-gam*r)**4 - 1
    r0max = findroot(f, (mpf('1e-6'), mpf('0.9')), solver='bisect', tol=mpf('1e-20'))
    # verify the inequality chain on a grid of r0 in (0, r0max]
    worst = None
    for i in range(1, 41):
        r0 = r0max*i/40
        z = r0*(q+1)*(q+2); k = mp.sqrt(z)
        S0, S1, S2 = Sk(q, k, N=200)
        E = S1/S0; V = S2/S0 - E*E
        p0 = 1/S0; r1 = gam*r0
        lb = p0*r0*(2*r1 - p0*r0/(1-r1)**4)
        assert V - E >= lb > 0, (q, r0, V-E, lb)
        rel = (V-E)/E
        worst = rel if worst is None else min(worst, rel)
    print("q=%d  Lemma C covers r0 <= %.5f  i.e. kappa <= %.4f = %.4f q ; min (VarJ-EJ)/EJ on it = %.3e" % (q, r0max, mp.sqrt(r0max*(q+1)*(q+2)), mp.sqrt(r0max*(q+1)*(q+2))/q, worst))

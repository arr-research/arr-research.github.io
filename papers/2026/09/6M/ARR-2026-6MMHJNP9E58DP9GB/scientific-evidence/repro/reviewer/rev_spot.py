"""Spot-check of the q=4 certificate: chaining of nodes, and the mean-value bound at the two tightest nodes and one middle node,
recomputed with plain mpmath at 80 digits (independent of mpmath.iv)."""
import json
from mpmath import mp, mpf, sqrt
from fractions import Fraction
mp.dps = 80
steps = json.load(open('rev_steps_q4.json'))
q = 4
print("nsteps", len(steps), "first a", steps[0][0], "last b", steps[-1][1])
# chaining
gaps = [steps[i+1][0] - steps[i][1] for i in range(len(steps)-1)]
print("max |a_{i+1} - b_i| (floats from json):", max(abs(g) for g in gaps))
c2 = Fraction(q*q - q - 8, (q+3)*(q+4)); y0 = c2/(64 + 4*c2); z0 = y0*(q+1)*(q+2)
print("exact z0 =", z0, float(z0), " first node a <= z0:", steps[0][0] <= float(z0))
def Sr(z, N=400):
    z = mpf(z); S = [mpf(0)]*4; w = mpf(1)
    for j in range(N):
        for r in range(4): S[r] += (j**r)*w
        w = w*z/((q+2*j+1)*(q+2*j+2))
    return S
def G(z):
    S0, S1, S2, S3 = Sr(z); return S0*S1 - S0*S2 + S1**2
def Gp(z):
    S0, S1, S2, S3 = Sr(z); return (S1**2 + S0*S2 + S1*S2 - S0*S3)/mpf(z)
def M(a, b):
    S0, S1, S2, S3 = Sr(b); return (S0*S2 + S1**2 + S0*S3 + 3*S1*S2)/mpf(a)
# tightest node (max Ga), a middle node, the last node
idx = [max(range(len(steps)), key=lambda i: steps[i][2]), len(steps)//2, len(steps)-1, 0]   # REPRO: the review session's copy assigned this list to '_', leaving idx empty; restored so the node checks run
for i in idx:
    a, b, Ga = steps[i]
    a = mpf(a); b = mpf(b)
    g_exact = G(a)
    print("node %d: a=%s b=%s  Ga(cert)=%.6e  G(a) 80-digit=%.6e  Ga>=G(a): %s" % (i, mp.nstr(a, 12), mp.nstr(b, 12), Ga, float(g_exact), Ga >= g_exact - mpf('1e-60')))
    Mb = M(a, b)
    # true sup |G'| on [a,b] by sampling
    sup = max(abs(Gp(a + (b-a)*t/50)) for t in range(51))
    mv = g_exact + (b-a)*Mb
    worst = max(G(a + (b-a)*t/50) for t in range(51))
    print("     M(b)=%.6e  sup|G'| sampled=%.6e  M>=sup: %s   G(a)+(b-a)M = %.6e <0: %s   max G on [a,b] sampled = %.6e" % (float(Mb), float(sup), Mb >= sup, float(mv), mv < 0, float(worst)))
# Lemma S bound check on (0, z0] for q = 4 and 10
for qq in [4, 10]:
    q = qq
    c2 = Fraction(q*q - q - 8, (q+3)*(q+4)); y0 = c2/(64 + 4*c2); z0 = y0*(q+1)*(q+2)
    worst = None
    for t in range(1, 40):
        z = mpf(z0.numerator)/mpf(z0.denominator)*t/40; y = z/((q+1)*(q+2))
        bound = -(mpf(c2.numerator)/mpf(c2.denominator))*y**2 + (4*y)**3/(1-4*y)
        ratio = G(z)/bound   # both negative; need G <= bound  i.e. G/bound >= 1
        ok = G(z) <= bound and bound < 0
        worst = ok if worst is None else (worst and ok)
    print("q=%d: Lemma S bound G(z) <= -c2 y^2 + (4y)^3/(1-4y) < 0 on (0,z0], 40 points: %s ; z0=%.5f" % (q, worst, float(z0)))
# zL_plus check: S0(zL_plus) > q(q-1)/8 at 80 digits, and z_L itself
q = 4
zLp = mpf('12.034318975905613')
print("S0(zL_plus) - q(q-1)/8 =", mp.nstr(Sr(zLp)[0] - mpf(q*(q-1))/8, 10))

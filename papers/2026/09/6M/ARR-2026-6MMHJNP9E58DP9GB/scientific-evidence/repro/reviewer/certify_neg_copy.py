"""Rigorous (interval-arithmetic) certificate that  G_q(z) < 0  on  (0, z_L^+],  where
   G_q(z) = S0*S1 - S0*S2 + S1^2,   S_r(z) = sum_{j>=0} j^r z^j/(q+1)_{2j},   z = kappa^2,
   and  z_L^+  is a certified upper bound of the point where S0 = L_q = q(q-1)/8.
Since  kappa*H_q = 4 (E J - Var J) = 4 G_q / S0^2  (J with law P(J=j) ∝ w_j),  this certifies
   H_q < 0 on (0, kappa_L],  i.e. the hypothesis of Lemma B (first fold after kappa_L).

Method.
 (i)  Small z:  G(z) = sum_{r>=2} g_r z^r with  g_2 = -(q^2-q-8)/((q+1)^2 (q+2)^2 (q+3)(q+4))  (exact, sympy)
      and |g_r| <= r (r+1)^2 ((q+1)(q+2))^{-r} <= 4^r ((q+1)(q+2))^{-r}  for r >= 3.  Hence with
      y = z/((q+1)(q+2)):  G(z) <= -c2 y^2 + (4y)^3/(1-4y),  c2 = (q^2-q-8)/((q+3)(q+4)),
      which is < 0 for  y < y0 := c2/(64 + 4 c2).   [exact rational arithmetic]
 (ii) Continuation on [z0, z_L^+]:  rigorous enclosures of S_r(a) (partial sums in interval arithmetic
      + explicit tail bound), and the mean-value bound  G(z) <= G(a) + (z-a) * M(b)  on [a,b], with
      M(b) := (S0 S2 + S1^2 + S0 S3 + 3 S1 S2)(b) / a  >=  sup_{[a,b]} |G'|   (S_r' = S_{r+1}/z, S_r increasing).
      Steps chosen adaptively; the certificate is the list of intervals with certified negative upper bounds.
Everything uses mpmath.iv (outward rounding); Python ints/Fractions where exact.
"""
import sys, json, time
from fractions import Fraction
from mpmath import iv, mp, mpf

iv.dps = 40
mp.dps = 40

def UP(x):
    return mpf(iv.mpf(x).b)   # plain mpf upper endpoint
def LO(x):
    return mpf(iv.mpf(x).a)

def tail_bound(q, zb, N, r):
    """upper bound for sum_{j>=N} j^r w_j at z = zb (iv upper), r<=3, requires ratio_N <= 1/16."""
    rho = zb/((q+2*N+1)*(q+2*N+2))
    assert UP(rho) <= mpf(1)/16, "increase N"
    # (N+i)^r <= N^r (1+i)^r <= N^r 8^i ; sum (8 rho)^i <= 1/(1-8rho) <= 2
    return 2*iv.mpf(N)**r

def S_encl(q, z, N):
    """interval enclosures of S0..S3 at interval z (monotone in z: evaluate at endpoints)."""
    z = iv.mpf(z)
    S = [iv.mpf(0)]*4
    w = iv.mpf(1)
    for j in range(N):
        for r in range(4):
            S[r] += (j**r)*w
        w = w*z/((q+2*j+1)*(q+2*j+2))
    # w now = w_N (as interval); add tail [0, w_N * tail_bound]
    out = []
    for r in range(4):
        tb = w*tail_bound(q, UP(z), N, r)
        out.append(S[r] + iv.mpf([0, UP(tb)]))
    return out

def choose_N(q, zb):
    N = 1
    while zb/((q+2*N+1)*(q+2*N+2)) > mpf(1)/16:
        N += 1
    return N + 2

def G_upper(S):
    S0, S1, S2, S3 = S
    return UP(S0*S1 - S0*S2 + S1**2)

def M_upper(S, a):
    S0, S1, S2, S3 = S
    return UP((S0*S2 + S1**2 + S0*S3 + 3*S1*S2)/a)

def certify(q, verbose=True):
    t0 = time.time()
    c2 = Fraction(q*q - q - 8, (q+3)*(q+4))
    assert c2 > 0
    y0 = c2/(64 + 4*c2)
    z0 = y0*(q+1)*(q+2)                # rational; G<0 on (0, z0] by (i)
    z0 = (mpf(z0.numerator)/mpf(z0.denominator))*(1 - mpf('1e-30'))   # rounded DOWN: the continuation starts strictly below the exact z0 covered by Lemma S
    # certified upper bound z_L^+ for z_L:  need lower bound of S0(z) >= q(q-1)/8
    target = mpf(q*(q-1))/8
    lo, hi = mpf(z0), mpf(4*q*q + 100)
    def S0_low(zz):
        N = choose_N(q, mpf(zz)); return LO(S_encl(q, iv.mpf(zz), N)[0])
    assert S0_low(hi) > target
    for _ in range(60):
        mid = (lo+hi)/2
        if S0_low(mid) > target: hi = mid
        else: lo = mid
    zLp = hi                             # S0(zLp) >= its lower bound > target  =>  z_L <= zLp
    # continuation
    a = mpf(z0); steps = []; ok = True
    while a < zLp:
        N = choose_N(q, zLp)
        Sa = S_encl(q, iv.mpf(a), N)
        Ga = G_upper(Sa)
        if not Ga < 0:
            ok = False; break
        # first guess of step from M at a, then verify with M at b
        Ma = M_upper(Sa, iv.mpf(a))
        step = (-Ga)/(2*Ma)
        b = min(a + step, zLp)
        for _ in range(60):
            Sb = S_encl(q, iv.mpf(b), N)
            Mb = M_upper(Sb, iv.mpf(a))
            if Ga + (b - a)*Mb < 0:
                break
            b = a + (b - a)/2
        else:
            ok = False; break
        steps.append((float(a), float(b), float(Ga)))
        a = b
    res = dict(q=q, ok=ok, z0=float(z0), zL_plus=float(zLp), kappa_L_plus=float(mp.sqrt(zLp)),
               nsteps=len(steps), min_G_upper=float(min(s[2] for s in steps)) if steps else None,
               max_G_upper=float(max(s[2] for s in steps)) if steps else None, time=round(time.time()-t0, 1))
    if verbose: print(json.dumps(res)); sys.stdout.flush()
    return res, steps

if __name__ == '__main__':
    qs = [int(a) for a in sys.argv[1:]] or list(range(4, 21))
    allres = []
    for q in qs:
        r, steps = certify(q)
        allres.append(r)
    with open('certify_neg_%s.json' % ('_'.join(map(str, qs)) if len(qs) <= 4 else 'range'), 'w') as f:
        json.dump(allres, f, indent=1)

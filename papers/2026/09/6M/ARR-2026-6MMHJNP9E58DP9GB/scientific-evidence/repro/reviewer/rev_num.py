"""Reviewer numerics (mpmath 50 digits): kappa_L < kappa_f, the proof's inequalities along trajectories, q=2,3 corollary,
asymptotics of kappa_L, H -> 1, table values."""
import sys, json
from mpmath import mp, mpf, findroot, sqrt, log, exp
mp.dps = 50
def S(q, k):
    k = mpf(k); z = k*k; N = int(k) + 80
    S0 = S1 = S2 = mpf(0); w = mpf(1)
    for j in range(N):
        S0 += w; S1 += j*w; S2 += j*j*w
        w = w*z/((q+2*j+1)*(q+2*j+2))
    return S0, S1, S2
def st(q, k):
    k = mpf(k); S0, S1, S2 = S(q, k)
    u = 1/S0; X = 2*S1/S0
    h = X**2 + (2*q+1)*X + q*(q-1)*(1-u) - k**2
    # independent H from the J-law: kappa H = 4(EJ - VarJ)
    E = S1/S0; V = S2/S0 - E*E
    h2 = 4*(E - V)
    T = 2*X**2 + q*(q-1)*u*X - 2*q*(q-1)*(1-u)
    return dict(u=u, X=X, h=h, h2=h2, T=T, H=h/k)
def kappa_L(q):
    return findroot(lambda x: S(q, x)[0] - mpf(q*(q-1))/8, (mpf('0.05'), mpf(4*q+100)), solver='bisect', tol=mpf('1e-30'))
def kappa_f(q, kL):
    return findroot(lambda x: st(q, x)['H'], (kL, mpf(4*q+100)), solver='bisect', tol=mpf('1e-30'))
qs = [int(a) for a in sys.argv[1:]] or list(range(4, 61)) + [80, 100, 150, 200, 400]
out = []
worst_hh2 = mpf(0)
for q in qs:
    c = q - mpf(1)/2
    kL = kappa_L(q); kf = kappa_f(q, kL)
    # grid checks
    pre = [kL*i/300 for i in range(1, 301)]
    post = [kf + (4*q+60-kf)*i/200 for i in range(0, 201)]
    ok_pre_h = ok_pre_Q = ok_pre_dQ = True; ok_post_h = ok_post_Q = ok_post_dQ = True; minB = None
    for idx, g in enumerate(pre + post):
        is_pre = idx < len(pre)
        s = st(q, g)
        worst_hh2 = max(worst_hh2, abs(s['h'] - s['h2'])/max(abs(s['h']), mpf('1e-40')))
        B = (2*c-4)*s['X'] + c*(2*q-1-c) - q*(q-1)*s['u']
        minB = B if minB is None else min(minB, B)
        Q = s['T'] - c*s['h']
        dQe = s['X']**2*(8 - q*(q-1)*s['u']) + s['h']*B     # (e^{c tau}Q)' / e^{c tau}
        if is_pre:
            ok_pre_h &= s['h'] < 0; ok_pre_Q &= Q < 0; ok_pre_dQ &= dQe <= 0
        else:
            ok_post_h &= s['h'] >= 0; ok_post_Q &= Q > 0; ok_post_dQ &= dQe > 0
    sf = st(q, kf)
    # H'(kappa_f) by finite difference
    d = mpf('1e-12'); Hp = (st(q, kf+d)['H'] - st(q, kf-d)['H'])/(2*d)
    # any other zero of H on a fine grid up to 4q+60? count sign changes
    grid = [mpf(i)/40 for i in range(1, int((4*q+60)*40))]
    vals = [st(q, g)['H'] for g in grid]
    nch = sum(1 for i in range(1, len(vals)) if vals[i-1]*vals[i] < 0)
    Hend = vals[-1]
    r = dict(q=q, kL=float(kL), kf=float(kf), kL_lt_kf=bool(kL < kf), u_f=float(sf['u']), margin8=float(8 - q*(q-1)*sf['u']),
             T_f=float(sf['T']), Hp_f=float(Hp), T_eq_k2Hp=float(abs(sf['T'] - kf**2*Hp)),
             pre=[ok_pre_h, ok_pre_Q, ok_pre_dQ], post=[ok_post_h, ok_post_Q, ok_post_dQ], minB=float(minB),
             nsignchanges_H=nch, H_end=float(Hend), kL_asym=float(q + sqrt(3*q*log(q))), kL_over_q=float(kL/q))
    print(json.dumps(r)); sys.stdout.flush(); out.append(r)
print("max rel diff between (C1)-h and 4(EJ-VarJ):", worst_hh2)
# q = 2, 3 corollary: H > 0, Q > 0, dQe > 0 on (0, 80]
for q, c in [(2, mpf(2)), (3, mpf(5)/2)]:
    ok = True; mn = None
    for i in range(1, 801):
        g = mpf(i)/10; s = st(q, g)
        B = (2*c-4)*s['X'] + c*(2*q-1-c) - q*(q-1)*s['u']; Q = s['T'] - c*s['h']
        dQe = s['X']**2*(8 - q*(q-1)*s['u']) + s['h']*B
        ok &= (s['h'] > 0) and (Q > 0) and (dQe > 0) and (B >= 0)
        mn = s['H'] if mn is None else min(mn, s['H'])
    print("q=%d: h>0, Q>0, dQe>0, B>=0 on (0,80]: %s ; min H = %s" % (q, ok, mp.nstr(mn, 6)))
# E[K(K-1)|A] = kappa^2 + q(q-1) u check (Poisson conditioned on A)
from mpmath import factorial
for q, k in [(4, mpf('2.5')), (7, mpf('11')), (10, mpf('0.3'))]:
    tot = mpf(0); mom = mpf(0); pq = None
    for kk in range(q, q + 400, 2):
        p = k**kk/factorial(kk); tot += p; mom += kk*(kk-1)*p
        if kk == q: pq = p
    lhs = mom/tot; rhs = k**2 + q*(q-1)*pq/tot
    print("q=%d kappa=%s: E[K(K-1)|A] - (kappa^2 + q(q-1)P(K=q|A)) = %s ; P(K=q|A) - 1/L = %s" % (q, k, mp.nstr(lhs-rhs, 5), mp.nstr(pq/tot - 1/S(q,k)[0], 5)))

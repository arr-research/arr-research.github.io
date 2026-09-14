from mpmath import mp, mpf, findroot, sqrt, log
mp.dps = 30
def S(q, k):
    k = mpf(k); z = k*k; N = int(k) + 60
    S0 = S1 = S2 = mpf(0); w = mpf(1)
    for j in range(N):
        S0 += w; S1 += j*w; S2 += j*j*w
        w = w*z/((q+2*j+1)*(q+2*j+2))
    return S0, S1, S2
def H(q, k):
    S0, S1, S2 = S(q, k); E = S1/S0; V = S2/S0 - E*E; return 4*(E - V)/mpf(k)
allok = True
for q in list(range(4, 61)) + [80, 100, 150, 200, 400, 1000]:
    kL = findroot(lambda x: S(q, x)[0] - mpf(q*(q-1))/8, (mpf('0.05'), mpf(3*q+100)), solver='bisect', tol=mpf('1e-20'))
    kf = findroot(lambda x: H(q, x), (kL, mpf(3*q+100)), solver='bisect', tol=mpf('1e-20'))
    HL = H(q, kL)
    ok = kL < kf and HL < 0
    allok &= ok
    if q in (4,5,6,10,20,30,40,60,80,100,150,200,400,1000):
        print("q=%4d kappa_L=%12.6f kappa_f=%14.8f  kL/q=%.3f kf/q=%.5f  H(kL)=%.3e  q+sqrt(3q log q)=%.1f" % (q, kL, kf, kL/q, kf/q, HL, q + sqrt(3*q*log(q))))
print("kappa_L < kappa_f and H(kappa_L) < 0 for all q in 4..60, 80,100,150,200,400,1000:", allok)
for q in [2, 3]:
    mn = min(H(q, mpf(i)/10) for i in range(1, 1201))
    print("q=%d: min H on (0,120] grid = %.3e" % (q, mn))

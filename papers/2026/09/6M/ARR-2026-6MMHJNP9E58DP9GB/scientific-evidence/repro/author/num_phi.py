"""Numerics for the (X,u,kappa) reduction (mpmath, 30 digits).

For each q: kappa_f (zero of H), kappa_L (L_q = q(q-1)/8), kappa_Phi (last sign change of
Phi(kappa) = T(X_+(kappa), u(kappa))), min of Phi on (0, kappa_L], values of T at the fold,
u at the fold, and the margin 8 - q(q-1) u(kappa_f).
"""
import sys, json
from mpmath import mp, mpf, sqrt, findroot, cosh, sinh, factorial, exp

mp.dps = 60

def Lq(q, k):
    # closed form: q! kappa^{-q} * (tail of cosh or sinh series)
    k = mpf(k)
    if k < mpf('1e-6'):
        return 1 + k**2/((q+1)*(q+2))
    if q % 2 == 0:
        s = cosh(k) - sum(k**j/factorial(j) for j in range(0, q, 2))
    else:
        s = sinh(k) - sum(k**j/factorial(j) for j in range(1, q, 2))
    return factorial(q)*k**(-q)*s

def Lq_d(q, k):
    # L' = (q! k^{-q} C_q)' with C_q' = C_{q-1}:  L' = q! k^{-q} C_{q-1} - q L / k
    k = mpf(k)
    q1 = q-1
    if q1 % 2 == 0:
        s = cosh(k) - sum(k**j/factorial(j) for j in range(0, q1, 2))
    else:
        s = sinh(k) - sum(k**j/factorial(j) for j in range(1, q1, 2))
    return factorial(q)*k**(-q)*s - q*Lq(q, k)/k

def Lq_series(q, k, N=200):
    k = mpf(k)
    return sum(k**(2*j)/mp.rf(q+1, 2*j) for j in range(N))

def Sk(q, k, N=None):
    """partial sums S_r = sum_j j^r w_j, w_j = kappa^{2j}/(q+1)_{2j}, r = 0,1,2 (series, positive terms)."""
    k = mpf(k); z = k*k
    if N is None: N = int(k) + 60
    S0 = S1 = S2 = mpf(0); w = mpf(1)
    for j in range(N):
        S0 += w; S1 += j*w; S2 += j*j*w
        w = w*z/((q+2*j+1)*(q+2*j+2))
    return S0, S1, S2

def state(q, k):
    k = mpf(k)
    S0, S1, S2 = Sk(q, k)
    L = S0; u = 1/L
    X = 2*S1/S0
    m = X/k
    # H from (C1): kappa H = X^2 + (2q+1)X + q(q-1)(1-u) - kappa^2
    h = X**2 + (2*q+1)*X + q*(q-1)*(1-u) - k**2
    H = h/k
    T = 2*X**2 + q*(q-1)*u*X - 2*q*(q-1)*(1-u)
    Delta = (T + (X+2)*h)/k**2
    return dict(L=L, m=m, u=u, X=X, H=H, T=T, Delta=Delta)

def Xplus(q, k, u):
    return (-(2*q+1) + sqrt((2*q+1)**2 + 4*k**2 - 4*q*(q-1)*(1-u)))/2

def Phi(q, k):
    k = mpf(k)
    u = 1/Sk(q, k)[0]
    X = Xplus(q, k, u)
    return 2*X**2 + q*(q-1)*u*X - 2*q*(q-1)*(1-u)

def signchanges(f, grid):
    vals = [f(x) for x in grid]
    ch = []
    for i in range(1, len(grid)):
        if vals[i-1]*vals[i] < 0:
            ch.append(findroot(f, (grid[i-1], grid[i]), solver='bisect', tol=mpf("1e-18")))
    return ch, vals

def analyse(q):
    kmax = 4*q + 40
    grid = [mpf(i)/50 for i in range(1, int(kmax*50)+1)]
    # consistency check of closed form vs series at a few points
    for kk in [mpf(q), mpf(2*q)]:
        assert abs(Lq(q, kk)/Sk(q, kk)[0] - 1) < mpf('1e-20'), (q, kk)
    Hz, Hv = signchanges(lambda x: state(q, x)['H'], grid)
    Pz, Pv = signchanges(lambda x: Phi(q, x), grid)
    Dz, Dv = signchanges(lambda x: state(q, x)['Delta'], grid)
    kL = findroot(lambda x: Sk(q, x)[0] - mpf(q*(q-1))/8, (mpf('0.01'), mpf(kmax)), solver='bisect', tol=mpf("1e-18"))
    st = state(q, Hz[-1]) if Hz else None
    # min of Phi on (0, kappa_L]
    gridL = [g for g in grid if g <= kL]
    maxPhi_L = max(Phi(q, g) for g in gridL)
    # check T along trajectory is increasing after the fold: sample
    Tvals_after = [state(q, g)['T'] for g in grid if Hz and g >= Hz[-1]]
    T_monotone_after = all(Tvals_after[i] <= Tvals_after[i+1] for i in range(len(Tvals_after)-1))
    Tvals_all = [state(q, g)['T'] for g in grid]
    T_monotone_all = all(Tvals_all[i] <= Tvals_all[i+1] for i in range(len(Tvals_all)-1))
    out = dict(q=q, nH=len(Hz), kappa_f=[float(z) for z in Hz], nPhi=len(Pz), kappa_Phi=[float(z) for z in Pz],
               nDelta=len(Dz), kappa_Delta=[float(z) for z in Dz], kappa_L=float(kL),
               maxPhi_on_0_kL=float(maxPhi_L), T_fold=float(st['T']) if st else None,
               u_fold=float(st['u']) if st else None, L_fold=float(st['L']) if st else None,
               m_fold=float(st['m']) if st else None,
               g_margin_fold=float(8 - q*(q-1)*st['u']) if st else None,
               T_monotone_after_fold=T_monotone_after, T_monotone_all=T_monotone_all,
               Phi_first_positive_grid=float(min([g for g in grid if Phi(q, g) > 0], default=mpf(-1))))
    return out

if __name__ == '__main__':
    qs = [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 30, 40, 60]
    res = []
    for q in qs:
        r = analyse(q)
        res.append(r)
        print(json.dumps(r))
        sys.stdout.flush()
    with open('num_phi.json', 'w') as f:
        json.dump(res, f, indent=1)

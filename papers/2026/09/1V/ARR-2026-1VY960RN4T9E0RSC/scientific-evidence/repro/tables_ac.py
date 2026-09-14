"""Section 9 tables: fold, contact and bounds for selected (a,c), in the manuscript's
conventions (X ~ Beta(a,c-a), mu = a/c, R^2 = 1-mu, K = log 1F1(a;c;k) - mu k,
b = K'/R^2, lambda = k/(2b), H = K' - k K'', F = 2K - k K').  mpmath, 40 digits,
200-step bisection.  Independent of the scan scripts (Kummer-derivative route only)."""
import mpmath as mp, sys, time
mp.mp.dps = 40
t0 = time.time()

def objs(a, c, k):
    M = mp.hyp1f1(a, c, k)
    m = a/c*mp.hyp1f1(a+1, c+1, k)/M
    V = a*(a+1)/(c*(c+1))*mp.hyp1f1(a+2, c+2, k)/M - m**2
    mu = a/c
    K = mp.log(M) - mu*k
    return dict(M=M, m=m, V=V, K=K, Kp=m-mu, H=(m-mu)-k*V, F=2*K-k*(m-mu))

def bisect(f, lo, hi, steps=200):
    flo = f(lo)
    for _ in range(steps):
        mid = (lo+hi)/2
        if f(mid)*flo > 0: lo, flo = mid, f(mid)
        else: hi = mid
    return (lo+hi)/2

def bracket(f, lo, hi, n=4000):
    ks = [lo + (hi-lo)*i/n for i in range(n+1)]
    v = [f(k) for k in ks]
    return [(ks[i], ks[i+1]) for i in range(n) if v[i]*v[i+1] < 0]

def analyse(a, c):
    a, c = mp.mpf(a), mp.mpf(c)
    mu = a/c; R2 = 1-mu; lam0 = c*(c+1)/(2*a)
    kmax = 20*c + 60
    Hf = lambda k: objs(a, c, k)['H']; Ff = lambda k: objs(a, c, k)['F']
    lo = mp.mpf('1e-3')
    zH = bracket(Hf, lo, kmax); zF = bracket(Ff, lo, kmax)
    res = dict(a=a, c=c, mu=mu, R2=R2, lam0=lam0, nH=len(zH), nF=len(zF))
    # min of H on a coarse grid (for no-fold rows)
    grid = [lo + (kmax-lo)*i/2000 for i in range(2001)]
    res['Hmin'] = min(Hf(k) for k in grid)
    if zH:
        kf = bisect(Hf, *zH[0]); o = objs(a, c, kf)
        bf = o['Kp']/R2
        res.update(kf=kf, mf=o['m'], bf=bf, lam_min=kf/(2*bf))
        res['k1'] = 2*(c+1)*(c-2*a)/c
        res['ub'] = c*(a+1); res['m_u'] = a*(c+1)/(c*(a+1))
    if zF:
        kc = bisect(Ff, *zF[0]); o = objs(a, c, kc)
        bc = o['Kp']/R2; lamc = kc/(2*bc)
        res.update(kc=kc, bc=bc, lam_c=lamc, Dc_rel=1-bc**2, Rc=kc*o['Kp']-o['K'])
        res['Rc_alt'] = lamc*R2*bc**2
    return res

def s(x, n=10): return mp.nstr(x, n)
def frac(t):
    return mp.mpf(t.split('/')[0])/mp.mpf(t.split('/')[1]) if '/' in t else mp.mpf(t)

fold_rows = [('1/2', '3/2', 'RP^2'), ('1/2', '2', ''), ('1/2', '5/2', 'RP^4'), ('1/2', '5', 'RP^9'),
             ('1', '3', 'CP^2'), ('1', '5', 'CP^4'), ('1', '17', 'CP^16'), ('3/2', '9/2', ''),
             ('2', '6', 'HP^2'), ('2', '10', 'HP^4'), ('3', '9', ''), ('5', '15', ''), ('5', '65', ''),
             ('1', '2.001', ''), ('1/2', '1.01', '')]
nofold_rows = [('1', '2', 'S^2'), ('2', '4', 'S^4'), ('1/2', '1', 'S^1'), ('3/10', '3/5', ''), ('3', '5', ''), ('1', '1.5', '')]

print("Table 1 (fold): (a,c) | source | kappa_1 | kappa_f | c(a+1) | m_f | m_u | b_f | lambda_min")
for a, c, src in fold_rows:
    r = analyse(frac(a), frac(c))
    assert r['nH'] == 1 and r['nF'] == 1, (a, c, r['nH'], r['nF'])
    assert r['kf'] >= r['k1'] and r['mf'] >= mp.mpf(1)/2 and r['kf'] < r['kc'], (a, c)
    if r['a'] >= 1: assert r['kf'] < r['ub'] and r['mf'] < r['m_u'], (a, c)
    assert r['lam_min'] < r['lam_c'] < r['lam0'], (a, c)
    assert abs(r['Rc']-r['Rc_alt']) < mp.mpf('1e-30'), (a, c)
    ub = s(r['ub'], 6) if r['a'] >= 1 else '-'
    mu_ = s(r['m_u'], 8) if r['a'] >= 1 else '-'
    print(f"| ({a},{c}) | {src} | {s(r['k1'],8)} | {s(r['kf'],10)} | {ub} | {s(r['mf'],8)} | {mu_} | {s(r['bf'],8)} | {s(r['lam_min'],10)} |")
    globals().setdefault('RES', {})[(a, c)] = r

print()
print("Table 2 (contact): (a,c) | kappa_c | b_c | lambda_c | lambda_0 | D_c/R^2 | R_c")
for a, c, src in fold_rows:
    r = RES[(a, c)]
    print(f"| ({a},{c}) | {s(r['kc'],10)} | {s(r['bc'],8)} | {s(r['lam_c'],10)} | {s(r['lam0'],6)} | {s(r['Dc_rel'],8)} | {s(r['Rc'],8)} |")

print()
print("Table 3 (no fold, c <= 2a): (a,c) | source | zeros of H | zeros of F | min H on grid | lambda_0")
for a, c, src in nofold_rows:
    r = analyse(frac(a), frac(c))
    assert r['nH'] == 0 and r['nF'] == 0 and r['Hmin'] > 0, (a, c, r)
    print(f"| ({a},{c}) | {src} | {r['nH']} | {r['nF']} | {s(r['Hmin'],3)} | {s(r['lam0'],6)} |")

# counterexamples to the a>=1 bounds for a<1
print()
print("Table 4 (a<1): (a,c) | kappa_f | c(a+1) | ratio")
for a, c in [('1/4', '1'), ('1/2', '2'), ('1/2', '10'), ('3/4', '3')]:
    A = frac(a); C = frac(c)
    r = analyse(A, C)
    print(f"| ({a},{c}) | {s(r['kf'],8)} | {s(C*(A+1),6)} | {s(r['kf']/(C*(A+1)),5)} |")
print("runtime s:", round(time.time()-t0, 1))

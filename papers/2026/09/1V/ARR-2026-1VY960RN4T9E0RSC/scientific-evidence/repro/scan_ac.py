"""Numerical scan: count positive zeros of the fold numerator H_{a,c} and of the
coexistence function F_{a,c} for M = 1F1(a;c;k), K = log M - (a/c) k.
H = (m - a/c) - k m', F = 2K - k K'.  m computed two independent ways
(Kummer derivatives vs Riccati) and compared.  mpmath, 30 digits."""
import mpmath as mp, sys, time, json
mp.mp.dps = 30

def funcs(a, c, k):
    M  = mp.hyp1f1(a, c, k)
    M1 = a/c*mp.hyp1f1(a+1, c+1, k)
    M2 = a*(a+1)/(c*(c+1))*mp.hyp1f1(a+2, c+2, k)
    m  = M1/M
    mp_ = M2/M - m**2                      # tilted variance, independent route
    mp_ric = (a - (c-k)*m - k*m**2)/k       # Riccati route
    mu = a/c
    H = (m - mu) - k*mp_
    F = 2*(mp.log(M) - mu*k) - k*(m - mu)
    return H, F, m, mp_, mp_ric

def zeros(a, c, kmax, ngrid=1500):
    # grid: geometric near 0 then linear
    ks = [mp.mpf(kmax)*mp.mpf(10)**(-6 + 6*i/300) for i in range(301)]
    ks += [mp.mpf(kmax)*(i/ngrid) for i in range(1, ngrid+1)]
    ks = sorted(set(ks))
    vals = [funcs(a, c, k) for k in ks]
    maxdiff = max(abs(v[3]-v[4])/abs(v[3]) for v in vals)
    out = {'grid_points':len(ks),'grid_min':str(ks[0]),'grid_max':str(ks[-1])}
    for idx, name in [(0, 'H'), (1, 'F')]:
        zs = []
        for i in range(len(ks)-1):
            if vals[i][idx]*vals[i+1][idx] < 0:
                f = lambda k: funcs(a, c, k)[idx]
                zs.append(mp.findroot(f, (ks[i], ks[i+1]), solver='bisect', tol=1e-25))
        out[name] = zs
    out['sign_small'] = mp.sign(vals[0][0])
    out['sign_large'] = mp.sign(vals[-1][0])
    out['maxdiff_riccati'] = maxdiff
    out['m_at_fold'] = [funcs(a, c, z)[2] for z in out['H']]
    return out

if __name__ == '__main__':
    t0 = time.time()
    A = [mp.mpf('0.5'), 1, mp.mpf('1.5'), 2, 3, 5]
    results = []
    anomalies = []
    for a in A:
        cs = [a + mp.mpf(j)/2 for j in range(1, 121)]           # c in (a, a+60]
        cs += [2*a - mp.mpf('0.5'), 2*a - mp.mpf('0.1'), 2*a, 2*a + mp.mpf('0.1'), 2*a + mp.mpf('0.01'), 2*a + mp.mpf('0.001')]
        cs = sorted(set(c for c in cs if c > a))
        for c in cs:
            kmax = 15*c + 50
            r = zeros(a, c, kmax)
            nH, nF = len(r['H']), len(r['F'])
            pred = 1 if c > 2*a else 0
            row = dict(a=float(a), c=float(c), nH=nH, nF=nF, pred=pred,
                       kf=[float(z) for z in r['H']], kc=[float(z) for z in r['F']],
                       m_fold=[float(x) for x in r['m_at_fold']],
                       riccati_maxreldiff=float(r['maxdiff_riccati']))
            results.append(row)
            ok = (nH == pred) and (nF == pred) and (r['sign_large'] > 0)
            if pred == 1:
                ok = ok and r['H'][0] < r['F'][0] and r['m_at_fold'][0] >= 0.5 and r['H'][0] >= 2*(c+1)*(c-2*a)/c
            if not ok:
                anomalies.append(row)
            print(f"a={float(a):4.1f} c={float(c):7.3f} nH={nH} nF={nF} pred={pred} "
                  f"kf={row['kf']} kc={row['kc']} m_f={row['m_fold']} ricc={row['riccati_maxreldiff']:.1e}", flush=True)
    json.dump(dict(results=results, anomalies=anomalies), open('scan_ac.json', 'w'), indent=1)
    print("ANOMALIES:", len(anomalies))
    for r in anomalies: print(r)
    print("runtime s:", time.time()-t0)

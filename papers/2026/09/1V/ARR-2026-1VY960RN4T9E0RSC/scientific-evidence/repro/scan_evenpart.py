"""Even part L_q(k) = (M_{q+1}(k)+M_{q+1}(-k))/2 (7H9F normalizer).  Count zeros of
H = m - k m' and F = 2 log L - k m; evaluate the zero-set derivative
Delta(m,k) = -k m (1-m^2) + (2q+5) m^2 - 2 + (q+1)(q+2) m/k  (= H' wherever H = 0,
from the third-order ODE) along the trajectory, and locate where Delta(m(k),k) < 0."""
import mpmath as mp, time, json
mp.mp.dps = 30

def L_and_derivs(q, k):
    d = q + 1
    E  = mp.hyp1f1(1, d, k);  O = mp.hyp1f1(1, d, -k)
    E1 = mp.hyp1f1(2, d+1, k)/d;  O1 = -mp.hyp1f1(2, d+1, -k)/d
    E2 = 2*mp.hyp1f1(3, d+2, k)/(d*(d+1)); O2 = 2*mp.hyp1f1(3, d+2, -k)/(d*(d+1))
    L, L1, L2 = (E+O)/2, (E1+O1)/2, (E2+O2)/2
    return L, L1, L2

def HF(q, k):
    L, L1, L2 = L_and_derivs(q, k)
    m = L1/L; V = L2/L - m**2
    H = m - k*V
    F = 2*mp.log(L) - k*m
    Delta = -k*m*(1-m**2) + (2*q+5)*m**2 - 2 + (q+1)*(q+2)*m/k
    return H, F, m, V, Delta

def run(q, kmax=None, ngrid=1500):
    kmax = kmax or 15*q + 60
    ks = [mp.mpf(kmax)*mp.mpf(10)**(-6 + 6*i/300) for i in range(301)]
    ks += [mp.mpf(kmax)*(i/ngrid) for i in range(1, ngrid+1)]
    ks = sorted(set(ks)); vals = [HF(q, k) for k in ks]
    out = {'grid_points':len(ks),'grid_min':str(ks[0]),'grid_max':str(ks[-1])}
    for idx, name in [(0, 'H'), (1, 'F')]:
        zs = []
        for i in range(len(ks)-1):
            if vals[i][idx]*vals[i+1][idx] < 0:
                zs.append(mp.findroot(lambda k: HF(q, k)[idx], (ks[i], ks[i+1]), solver='bisect', tol=1e-25))
        out[name] = zs
    # Delta sign along trajectory
    neg = [ks[i] for i in range(len(ks)) if vals[i][4] < 0]
    out['Delta_neg_range'] = (float(min(neg)), float(max(neg))) if neg else None
    out['H_sign_small'] = int(mp.sign(vals[0][0]))
    # check Delta = H' at the fold (numerical derivative)
    chk = []
    for z in out['H']:
        Hp = mp.diff(lambda k: HF(q, k)[0], z)
        chk.append(float(Hp - HF(q, z)[4]))
    out['Hprime_minus_Delta_at_zeros'] = chk
    out['m_at_fold'] = [float(HF(q, z)[2]) for z in out['H']]
    return out

if __name__ == '__main__':
    t0 = time.time(); res = {}
    for q in list(range(1, 21)) + [25, 30, 40, 50, 60]:
        r = run(q)
        res[q] = dict(nH=len(r['H']), nF=len(r['F']), kf=[float(z) for z in r['H']], kc=[float(z) for z in r['F']],
                      m_fold=r['m_at_fold'], Delta_neg=r['Delta_neg_range'], Hsign0=r['H_sign_small'], chk=r['Hprime_minus_Delta_at_zeros'])
        print(q, res[q], flush=True)
    json.dump(res, open('scan_evenpart.json', 'w'), indent=1)
    print("runtime s:", time.time()-t0)

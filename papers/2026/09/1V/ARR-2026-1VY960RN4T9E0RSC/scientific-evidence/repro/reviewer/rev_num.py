import mpmath as mp
mp.mp.dps = 30
def funcs(a,c,k):
    M = mp.hyp1f1(a,c,k); M1 = a/c*mp.hyp1f1(a+1,c+1,k); M2 = a*(a+1)/(c*(c+1))*mp.hyp1f1(a+2,c+2,k)
    m = M1/M; V = M2/M - m**2; mu = a/c
    H = (m-mu) - k*V; F = 2*(mp.log(M)-mu*k) - k*(m-mu)
    return H,F,m,V
def count(a,c,kmax=None,n=2500):
    a=mp.mpf(a); c=mp.mpf(c); kmax = kmax or 20*c+60
    ks = [kmax*mp.mpf(10)**(-6+6*i/300) for i in range(301)] + [kmax*i/n for i in range(1,n+1)]
    ks = sorted(set(ks)); vals=[funcs(a,c,k) for k in ks]
    out={}
    for idx,name in [(0,'H'),(1,'F')]:
        zs=[]
        for i in range(len(ks)-1):
            if vals[i][idx]*vals[i+1][idx]<0:
                zs.append(mp.findroot(lambda k: funcs(a,c,k)[idx],(ks[i],ks[i+1]),solver='bisect',tol=1e-24))
        out[name]=zs
    out['Hmin'] = min(v[0] for v in vals); out['H0sign']=mp.sign(vals[0][0]); out['Hinf']=vals[-1][0]
    out['m_f'] = [funcs(a,c,z)[2] for z in out['H']]
    return out
print("=== (6) independent grid ===")
for a in [0.3,0.7,1,2.5,4]:
    for dc in [-1,-0.1,0.1,1,10,40]:
        c = 2*a+dc
        if c <= a: print(f"a={a} c={c}: SKIP (c<=a)"); continue
        r = count(a,c)
        pred = 1 if c>2*a else 0
        lb = 2*(c+1)*(c-2*a)/c if c>2*a else None
        ub = c*(a+1)
        flag = "OK" if (len(r['H'])==pred and len(r['F'])==pred) else "MISMATCH"
        print(f"a={a} c={c:.2f} nH={len(r['H'])} nF={len(r['F'])} pred={pred} kf={[mp.nstr(z,8) for z in r['H']]} kc={[mp.nstr(z,8) for z in r['F']]} m_f={[mp.nstr(x,6) for x in r['m_f']]} lb={lb} ub={ub} Hmin={mp.nstr(r['Hmin'],4)} {flag}")
print("=== boundary c=2a ===")
for a,c in [(1,2),(2,4),(0.5,1),(3,6),(0.3,0.6),(10,20)]:
    r = count(a,c)
    print(f"a={a} c={c}: nH={len(r['H'])} nF={len(r['F'])} Hmin over grid={mp.nstr(r['Hmin'],6)} H(inf)={mp.nstr(r['Hinf'],6)} 1-mu={1-a/c}")
    # small k check of cubic coefficient
    for k in [mp.mpf('0.01'),mp.mpf('0.1')]:
        Hk = funcs(mp.mpf(a),mp.mpf(c),k)[0]; pred = k**3/(8*(2*a+1)**2*(2*a+3))
        print(f"   k={k}: H={mp.nstr(Hk,8)} cubic pred={mp.nstr(pred,8)} ratio={mp.nstr(Hk/pred,8)}")
print("=== c slightly above 2a ===")
for a in [0.5,1,3]:
    for eps in [1e-3,1e-2]:
        c = 2*a+eps; r = count(a,c)
        print(f"a={a} c={c}: nH={len(r['H'])} kf={[mp.nstr(z,8) for z in r['H']]} lb={2*(c+1)*(c-2*a)/c} m_f={[mp.nstr(x,6) for x in r['m_f']]}")
print("=== T3 counterexample a=1/2,c=2 and bound checks ===")
for a,c in [(0.5,2),(0.5,1.5),(0.5,3),(0.25,1),(0.5,10),(1,3),(2,6),(5,65)]:
    r = count(a,c); kf = r['H'][0]
    print(f"a={a} c={c}: kf={mp.nstr(kf,8)} c(a+1)={c*(a+1)} ratio={mp.nstr(kf/(c*(a+1)),4)} m_f={mp.nstr(r['m_f'][0],6)} m_u={a*(c+1)/(c*(a+1))} lb={2*(c+1)*(c-2*a)/c} kc={mp.nstr(r['F'][0],8)}")
# kappa(1-m) <= c-a check
print("=== kappa(1-m) - (c-a) sup ===")
for a in [0.25,0.5,0.75,1,2]:
    worst=-mp.inf
    for c in [a+j/2 for j in range(1,41)]:
        for k in [mp.mpf(10)**e for e in [-1,0,0.5,1,1.5,2,2.5,3]]:
            m = funcs(mp.mpf(a),mp.mpf(c),k)[2]; worst=max(worst,k*(1-m)-(c-a))
    print(f"a={a}: sup = {mp.nstr(worst,6)}")

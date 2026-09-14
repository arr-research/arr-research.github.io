import mpmath as mp
mp.mp.dps = 30
def Lq(q,k):
    d=q+1
    E=mp.hyp1f1(1,d,k); O=mp.hyp1f1(1,d,-k)
    E1=mp.hyp1f1(2,d+1,k)/d; O1=-mp.hyp1f1(2,d+1,-k)/d
    E2=2*mp.hyp1f1(3,d+2,k)/(d*(d+1)); O2=2*mp.hyp1f1(3,d+2,-k)/(d*(d+1))
    return (E+O)/2,(E1+O1)/2,(E2+O2)/2
def HD(q,k):
    L,L1,L2=Lq(q,k); m=L1/L; V=L2/L-m**2
    H=m-k*V; D=-k*m*(1-m**2)+(2*q+5)*m**2-2+(q+1)*(q+2)*m/k
    return H,D,m,L
# verify third-order ODE numerically for q=4 at a few k (via 1F2 mp.hyper derivative)
for q in [2,4,7]:
    for k in [mp.mpf('0.7'),mp.mpf(3),mp.mpf(11)]:
        L = lambda x: mp.hyper([1],[(q+1)/mp.mpf(2),(q+2)/mp.mpf(2)],x**2/4)
        L0=L(k); L1=mp.diff(L,k); L2=mp.diff(L,k,2); L3=mp.diff(L,k,3)
        r2 = k**2*L2+2*q*k*L1-(k**2-q*(q-1))*L0-q*(q-1)
        r3 = k**2*L3+(2*q+2)*k*L2+(q*(q+1)-k**2)*L1-2*k*L0
        Lc,_,_ = Lq(q,k)
        print(f"q={q} k={k}: 1F2 vs evenpart diff={mp.nstr(L0-Lc,3)} ode2={mp.nstr(r2,3)} ode3={mp.nstr(r3,3)}")
# identity H' + (3m+(2q+2)/k)H = Delta numerically
for q in [2,4,10]:
    for k in [mp.mpf(1),mp.mpf(5),mp.mpf(20)]:
        Hp = mp.diff(lambda x: HD(q,x)[0], k); H,D,m,_ = HD(q,k)
        print(f"q={q} k={k}: identity residual={mp.nstr(Hp+(3*m+(2*q+2)/k)*H-D,3)}")
# sign changes of Delta along trajectory and zeros of H for q=1..5,10,30
def scan(q,n=4000):
    kmax=15*q+60
    ks=[kmax*mp.mpf(10)**(-5+5*i/500) for i in range(501)]+[kmax*i/n for i in range(1,n+1)]
    ks=sorted(set(ks)); vals=[HD(q,k) for k in ks]
    Hz=[(ks[i],ks[i+1]) for i in range(len(ks)-1) if vals[i][0]*vals[i+1][0]<0]
    Dz=[(ks[i],ks[i+1]) for i in range(len(ks)-1) if vals[i][1]*vals[i+1][1]<0]
    Dmin=min(v[1] for v in vals)
    return Hz,Dz,Dmin,vals[0][1],vals[-1][1]
for q in [1,2,3,4,5,10,30]:
    Hz,Dz,Dmin,D0,Dinf=scan(q)
    kf=[mp.findroot(lambda x: HD(q,x)[0],z,solver='bisect',tol=1e-24) for z in Hz]
    kD=[mp.findroot(lambda x: HD(q,x)[1],z,solver='bisect',tol=1e-24) for z in Dz]
    print(f"q={q}: H zeros={[mp.nstr(z,10) for z in kf]}, Delta sign changes={[mp.nstr(z,8) for z in kD]}, Delta min={mp.nstr(Dmin,5)}, D(0+)={mp.nstr(D0,4)}, D(inf)={mp.nstr(Dinf,4)}")
# 0F1 with c<1/2: m in (0,1)? increasing? H>0?
print("=== 0F1(;c;k^2/4) small c ===")
for c in [mp.mpf('0.1'),mp.mpf('0.3'),mp.mpf('0.5'),mp.mpf('1'),mp.mpf('1.5')]:
    Z=lambda k: mp.hyper([],[c],k**2/4)
    mm=lambda k: mp.diff(Z,k)/Z(k)
    ks=[mp.mpf(x)/10 for x in range(1,400)]
    ms=[mm(k) for k in ks]
    Hs=[ms[i]-ks[i]*mp.diff(mm,ks[i]) for i in range(len(ks))]
    print(f"c={c}: max m={mp.nstr(max(ms),6)}, m monotone={all(ms[i]<ms[i+1] for i in range(len(ms)-1))}, min H={mp.nstr(min(Hs),6)}, m(40)={mp.nstr(ms[-1],6)}")

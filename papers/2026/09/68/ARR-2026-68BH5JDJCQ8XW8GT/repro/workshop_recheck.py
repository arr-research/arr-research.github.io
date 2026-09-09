# Re-verification of the AIRR workshop checks (TALLER-0002, 2026-09-08) by routes independent of the paper's scripts:
#  (A) the 66 boundary signs of Theorem 6.1 recomputed from the THREE-TERM definition (2.4) of N_d (no closed form (3.3));
#  (B) kappa_f, kappa_c, lambda_min, lambda_c, b_c, D_c, R_c for d = 3, 5, 17, 100 at 70 digits via the Kummer-derivative
#      route M'=1F1(2;d+1;k)/d, M''=2 1F1(3;d+2;k)/(d(d+1)) (no use of Lemma 3.1 or Psi_d), compared with the workshop's
#      20-digit values (embedded below) and with chain_values_50digits.txt (Psi route);
#  (C) residuals of H_d and F_d at those roots by direct quadrature of the tilted Beta(1,d-1) moments (45 digits).
from fractions import Fraction as Fr
import mpmath as mp, pathlib, time
def coeffs_N(d,nmax):
    a=[Fr(1)]
    for j in range(1,nmax+3): a.append(a[-1]/(d+j-1))
    Mc=a[:nmax+1]; M1=[(j+1)*a[j+1] for j in range(nmax+1)]; M2=[(j+2)*(j+1)*a[j+2] for j in range(nmax+1)]
    def mul(x,y):
        out=[Fr(0)]*(nmax+1)
        for i,xi in enumerate(x):
            for j in range(nmax+1-i): out[i+j]+=xi*y[j]
        return out
    MM1=mul(Mc,M1); MM2=mul(Mc,M2); M1M1=mul(M1,M1); MM=mul(Mc,Mc)
    return [MM1[n]-(MM2[n-1] if n else 0)+(M1M1[n-1] if n else 0)-MM[n]/d for n in range(nmax+1)]
t0=time.time(); ok=True; cnt=0
for d in range(3,36):
    c=coeffs_N(d,2*d+2); nd=2*d-1 if d in (3,4) else 2*d
    for n in (2*d-1,2*d):
        cnt+=1; ok&=((c[n]<0)==(n<=nd)) and c[n]!=0
    ok&=(c[0]==0 and c[1]==0 and all(c[n]<0 for n in range(2,nd+1)) and all(c[n]>0 for n in range(nd+1,2*d+3)))
print(f"(A) {cnt} boundary signs from the three-term definition, pattern of Theorem 6.1 for 3<=d<=35, n<=2d+2: {ok}  ({time.time()-t0:.1f}s)")
assert ok and cnt==66, "three-term coefficient signs"
workshop={3:dict(kappa_f="3.2327088362697960797",lambda_min="5.3587282768761663649",kappa_c="4.3442853030973276154",b_c="0.40033153600186345466",lambda_c="5.4258594594919770812",D_c="0.55982310752159246978",R_c="0.57971813607309136683"),
5:dict(kappa_f="8.4315508759981191491",lambda_min="9.6895511914568267945",kappa_c="11.644088051752538554",b_c="0.57349103909694187064",lambda_c="10.151935477569199929",D_c="0.53688642246040791261",R_c="2.6711120624543395136"),
17:dict(kappa_f="33.907100295950713143",lambda_min="33.99087520889086761",kappa_c="52.471451516607007792",b_c="0.67601429987287462466",lambda_c="38.80942424329953748",D_c="0.51106321540459966422",R_c="16.692447793088269072"),
100:dict(kappa_f="199.9999999999903193",lambda_min="199.99999999999981203",kappa_c="340.64385837032881889",b_c="0.7064382711069294205",lambda_c="241.09952157360367205",D_c="0.49593551942429796423",R_c="119.11870989331276535")}
mp.mp.dps=70
def KK(d,x):
    m0=mp.hyp1f1(1,d,x); m1=mp.hyp1f1(2,d+1,x)/d; m2=2*mp.hyp1f1(3,d+2,x)/(d*(d+1))
    kp=m1/m0-mp.mpf(1)/d; return mp.log(m0)-x/d, kp, m2/m0-(m1/m0)**2
def bis(f,a,b,it=240):
    a,b=mp.mpf(a),mp.mpf(b); fa=f(a); assert fa*f(b)<0
    for _ in range(it):
        m=(a+b)/2; fm=f(m)
        if fa*fm<=0: b=m
        else: a,fa=m,fm
    return (a+b)/2
def KKq(d,x):  # quadrature route, variable s=1-t, integrand (d-1) s^(d-2) e^{-x s}, split around its peak
    w=lambda s:(d-1)*s**(d-2)*mp.exp(-x*s)
    sp=mp.mpf(d-2)/x; sig=mp.sqrt(d-2)/x
    pts=sorted(set([mp.mpf(0)]+[min(max(sp+k*sig,mp.mpf(0)),mp.mpf(1)) for k in range(-8,9)]+[mp.mpf(1)]))
    Z=mp.quad(w,pts); m1=1-mp.quad(lambda s:s*w(s),pts)/Z; m2=mp.quad(lambda s:(1-s)**2*w(s),pts)/Z
    return mp.log(Z)+x-x/d, m1-mp.mpf(1)/d, m2-m1**2
chain={}
for blk in pathlib.Path(__file__).with_name("chain_values_50digits.txt").read_text().split("d=")[1:]:
    ls=blk.strip().split("\n"); chain[int(ls[0])]={l.split()[0]:mp.mpf(l.split()[1]) for l in ls[1:]}
keys=['kappa_f','lambda_min','kappa_c','b_c','lambda_c','D_c','R_c']
for d in (3,5,17,100):
    lo=mp.mpf(2*(d-2)*(d+1))/d
    kf=bis(lambda x:(lambda r:r[1]-x*r[2])(KK(d,x)),lo,2*d); kc=bis(lambda x:(lambda r:2*r[0]-x*r[1])(KK(d,x)),kf,20*d+50)
    R0=1-mp.mpf(1)/d; _,kpf,_=KK(d,kf); bf=kpf/R0; Kc,kpc,_=KK(d,kc); bc=kpc/R0
    me=dict(kappa_f=kf,lambda_min=kf/(2*bf),kappa_c=kc,b_c=bc,lambda_c=kc/(2*bc),D_c=R0*(1-bc**2),R_c=kc*kpc-Kc)
    dw=max(abs(mp.mpf(workshop[d][k])-me[k])/abs(me[k]) for k in keys)
    dc=max(abs(chain[d][k]-me[k])/abs(me[k]) for k in keys)
    assert dw<mp.mpf("1e-18") and dc<mp.mpf("1e-49"), (d,dw,dc)
    mp.mp.dps=45; K,kp,kpp=KKq(d,kf); K2,kp2,_=KKq(d,kc); Hq=kp-kf*kpp; Fq=2*K2-kc*kp2; mp.mp.dps=70
    print(f"(B) d={d}: max rel diff vs workshop (20 digits) {mp.nstr(dw,3)}; vs chain_values_50digits.txt (Psi route) {mp.nstr(dc,3)}")
    print(f"(C) d={d}: quadrature-route residuals H_d(kappa_f)={mp.nstr(Hq,3)}, F_d(kappa_c)={mp.nstr(Fq,3)}")
    print(f"    kappa_f={mp.nstr(kf,52)}\n    kappa_c={mp.nstr(kc,52)}")

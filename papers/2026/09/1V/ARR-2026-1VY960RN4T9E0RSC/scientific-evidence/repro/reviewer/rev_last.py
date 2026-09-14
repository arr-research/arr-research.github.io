import sympy as sp, mpmath as mp
k,q = sp.symbols('kappa q', positive=True)
# small-k expansion of Delta_q(m(k),k) and of H for L_q = sum k^{2j}/(q+1)_{2j}
L = sum(k**(2*j)/sp.rf(q+1,2*j) for j in range(6))
m = sp.series(sp.diff(L,k)/L, k, 0, 8).removeO()
Dq = sp.series(-k*m*(1-m**2) + (2*q+5)*m**2 - 2 + (q+1)*(q+2)*m/k, k, 0, 5).removeO()
Dq = sp.expand(Dq)
print("Delta_q small-k: [k^0]=", sp.simplify(Dq.coeff(k,0)), " [k^2]=", sp.factor(sp.simplify(Dq.coeff(k,2))))
H = sp.expand(sp.series(m - k*sp.diff(m,k), k, 0, 6).removeO())
print("H_q small-k: [k^1]=", sp.simplify(H.coeff(k,1)), " [k^3]=", sp.factor(sp.simplify(H.coeff(k,3))))
mp.mp.dps=30
def Lq(q,k):
    d=q+1
    E=mp.hyp1f1(1,d,k); O=mp.hyp1f1(1,d,-k)
    E1=mp.hyp1f1(2,d+1,k)/d; O1=-mp.hyp1f1(2,d+1,-k)/d
    E2=2*mp.hyp1f1(3,d+2,k)/(d*(d+1)); O2=2*mp.hyp1f1(3,d+2,-k)/(d*(d+1))
    return (E+O)/2,(E1+O1)/2,(E2+O2)/2
def HF(q,k):
    L,L1,L2=Lq(q,k); m=L1/L; V=L2/L-m**2
    return m-k*V, 2*mp.log(L)-k*m, m
q=4
kc = mp.findroot(lambda x: HF(q,x)[1], (5,6), solver='bisect', tol=1e-24)
print("q=4 kappa_c =", mp.nstr(kc,10), " H(200)=", mp.nstr(HF(4,mp.mpf(200))[0],8), " H(60) q=30:", mp.nstr(HF(30,mp.mpf(600))[0],8))
# small-k check of H = -(mu3/2) k^2 for (a,c)=(1,3) and (0.3,1.6)
for a,c in [(1,3),(0.3,1.6)]:
    a=mp.mpf(a); c=mp.mpf(c); k=mp.mpf('0.01')
    M=mp.hyp1f1(a,c,k); m=a/c*mp.hyp1f1(a+1,c+1,k)/M; V=a*(a+1)/(c*(c+1))*mp.hyp1f1(a+2,c+2,k)/M-m**2
    H=(m-a/c)-k*V; mu3=2*a*(c-a)*(c-2*a)/(c**3*(c+1)*(c+2))
    print(f"(a,c)=({a},{c}) H(0.01)/(-mu3/2 k^2) =", mp.nstr(H/(-mu3/2*k**2),8))

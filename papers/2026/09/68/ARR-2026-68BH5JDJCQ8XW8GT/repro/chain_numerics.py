# Numerics for the chain (normalized O(1) functions): fold kappa_f = zero of h(k)=k-Psi(M(k)); contact kappa_c = zero of F=2K-kappa K'.
# Prints the wide diagnostic table (14 values of d), then the four narrow Markdown tables of Section 7 (12 significant digits),
# and writes chain_values_50digits.txt with every quantity at 50 significant digits.
import mpmath as mp, pathlib
mp.mp.dps=60
def objs(d,k):
    M=mp.hyp1f1(1,d,k); b=1-d*(M-1)/(k*M); K=mp.log(M)-k/d; K1=(k*(d-1)/d-(d-1)+(d-1)/M)/k
    return M,b,K,K1
def h(d,k):
    M=mp.hyp1f1(1,d,k); return k-d*(M-1)*(2*M+d-1)/(M*(M+d))
def F(d,k):
    M,b,K,K1=objs(d,k); return 2*K-k*K1
def bisect(f,a,b,it=220):
    # plain bisection, 220 halvings: the bracket shrinks by 2^-220 < 1e-66 (mpmath's findroot(...,'bisect') stops at |f|^2 < tol, which is too early for 50 digits)
    a,b=mp.mpf(a),mp.mpf(b); fa=f(a); assert fa*f(b)<0
    for _ in range(it):
        m=(a+b)/2; fm=f(m)
        if fa*fm<=0: b=m
        else: a,fa=m,fm
    return (a+b)/2
rows={}
print("d | kappa_f | kappa_1=2(d-2)(d+1)/d | 2d | M(kappa_f) | d(d-1)/2 | lambda_min | kappa_c | b_c | lambda_c | lambda_0 | D_c/R0^2 | R_c")
for d in [3,4,5,6,7,8,10,12,15,17,20,30,50,100]:
    k1=mp.mpf(2*(d-2)*(d+1))/d
    kf=bisect(lambda k:h(d,k),k1,mp.mpf(2*d))
    kc=bisect(lambda k:F(d,k),kf*(1+mp.mpf('1e-12')),mp.mpf(20*d+50))
    Mf,bf,_,_=objs(d,kf); Mc,bc,Kc,K1c=objs(d,kc)
    lam_min=kf/(2*bf); lam_c=kc/(2*bc); R0sq=mp.mpf(d-1)/d
    Dc=R0sq*(1-bc**2); Rc=kc*K1c-Kc
    assert h(d,k1)<=0 and h(d,2*d)>0 and F(d,kf)<0 and lam_c<d*(d+1)/2 and Mf>=d*(d-1)/2 and bf<mp.mpf(1)/2 and lam_min<lam_c
    rows[d]=dict(kappa_1=k1,kappa_f=kf,two_d_minus_kappa_f=2*d-kf,M_f=Mf,M_1=mp.mpf(d*(d-1))/2,b_f=bf,lambda_min=lam_min,kappa_c=kc,b_c=bc,lambda_c=lam_c,lambda_0=mp.mpf(d*(d+1))/2,D_c=Dc,R_c=Rc)
    print(d, mp.nstr(kf,10), mp.nstr(k1,8), 2*d, mp.nstr(Mf,8), d*(d-1)/2, mp.nstr(lam_min,10), mp.nstr(kc,10), mp.nstr(bc,8), mp.nstr(lam_c,10), d*(d+1)/2, mp.nstr(Dc/R0sq,8), mp.nstr(Rc,10))
# --- Section 7 tables (rows d = 3, 5, 17, 100), 12 significant digits
def s(x,n=12): return mp.nstr(x,n)
sel=[3,5,17,100]
print("\nTable 1 (fold: bounds)")
print("| d | kappa_1 | kappa_f | 2d - kappa_f |\n|---|---|---|---|")
for d in sel: r=rows[d]; print(f"| {d} | {s(r['kappa_1'])} | {s(r['kappa_f'],14)} | {s(r['two_d_minus_kappa_f'],6)} |")
print("\nTable 2 (fold: radius and multiplier)")
print("| d | M_d(kappa_f) | d(d-1)/2 | b_d(kappa_f) | lambda_min |\n|---|---|---|---|---|")
for d in sel: r=rows[d]; print(f"| {d} | {s(r['M_f'],8)} | {s(r['M_1'],6)} | {s(r['b_f'],12)} | {s(r['lambda_min'],14)} |")
print("\nTable 3 (contact)")
print("| d | kappa_c | b_c | lambda_c | lambda_0,d |\n|---|---|---|---|---|")
for d in sel: r=rows[d]; print(f"| {d} | {s(r['kappa_c'])} | {s(r['b_c'])} | {s(r['lambda_c'])} | {s(r['lambda_0'],6)} |")
print("\nTable 4 (contact point of the rate-distortion function)")
print("| d | D_c | R_c | lambda_c/d |\n|---|---|---|---|")
for d in sel: r=rows[d]; print(f"| {d} | {s(r['D_c'])} | {s(r['R_c'])} | {s(r['lambda_c']/d,8)} |")
out=["# 50-significant-digit values (mpmath, dps=60; 220-step bisection). Columns: quantity value","# quantities: kappa_1=2(d-2)(d+1)/d, kappa_f (fold), M_f=M_d(kappa_f), b_f=b_d(kappa_f), lambda_min, kappa_c (contact), b_c, lambda_c, lambda_0=d(d+1)/2, D_c, R_c"]
for d,r in rows.items():
    out.append(f"d={d}")
    for k,v in r.items(): out.append(f"  {k} {mp.nstr(v,50)}")
pathlib.Path(__file__).with_name("chain_values_50digits.txt").write_text("\n".join(out)+"\n")
print("\nwrote chain_values_50digits.txt")

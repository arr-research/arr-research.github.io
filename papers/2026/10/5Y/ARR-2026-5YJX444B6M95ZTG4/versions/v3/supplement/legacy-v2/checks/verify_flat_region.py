import sympy as sp, random, math
a,b,x=sp.symbols('a b x',positive=True)
k=1-a-b
A=a*(1-a); B=k*(1-2*a)-x; D=x-k**2
Q=sp.expand(4*A*D-B**2)       # >=0 <=> 4AD>=B^2
c=k+2*a*b-2*sp.sqrt(a*b*(k+a*b))
# Q is -(x-c)(x-c') ; c' = k+2ab+2sqrt(ab(k+ab))
cp=k+2*a*b+2*sp.sqrt(a*b*(k+a*b))
print("Q + (x-c)(x-c') =", sp.simplify(sp.expand(Q+(x-c)*(x-cp))))
print("c*c' - (k+2ab)^2 + ... product check:", sp.simplify(sp.expand(c*cp-(k**2))))   # expect c c' = k^2 ?
random.seed(1)
bad=0
for _ in range(20000):
    av=random.random(); bv=random.random()*(1-av); kv=1-av-bv
    cv=kv+2*av*bv-2*math.sqrt(av*bv*(kv+av*bv)); cpv=kv+2*av*bv+2*math.sqrt(av*bv*(kv+av*bv))
    # claims: k^2 <= c <= k <= c'
    if not (kv*kv-1e-12<=cv<=kv+1e-12<=cpv+1e-12): bad+=1
print("violations of k^2<=c<=k<=c' in 20000 random (a,b):",bad)

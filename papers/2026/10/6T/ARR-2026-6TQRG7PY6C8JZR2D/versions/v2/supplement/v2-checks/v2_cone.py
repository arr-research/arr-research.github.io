# Lemma 10 (finite positive moment cone): explicit exact rational weights for K=3,4,5
import sympy as sp, itertools
def colvec(x,y,K):
    z=x+sp.I*y
    if y==0: return sp.Matrix([x**j for j in range(2,K+1)])
    return sp.Matrix([sp.expand(2*sp.re(sp.expand(z**j))) for j in range(2,K+1)])
def exact_weights(K):
    reals=[sp.Integer(r) for r in range(1,K+1)]
    cands=[(sp.Rational(a,2),sp.Rational(b,2)) for a in [1,2,3] for b in [1,2,3,4]]
    base=sum([colvec(r,0,K) for r in reals],sp.zeros(K-1,1))
    tgt=sp.Matrix([0,sp.Rational(3,2)]+[0]*(K-3))
    rhs=tgt-base
    best=None
    for comb in itertools.combinations(cands,K-1):
        M=sp.Matrix.hstack(*[colvec(x,y,K) for x,y in comb])
        if M.det()==0: continue
        sol=M.LUsolve(rhs)
        if all(s>0 for s in sol):
            den=sp.ilcm(*[sp.Rational(s).q for s in sol])
            if best is None or den<best[0]: best=(den,comb,list(sol))
    return reals,best
if __name__=="__main__":
    for K in [3,4,5]:
        reals,best=exact_weights(K)
        print("K",K,"real nodes",[int(r) for r in reals],"weights 1 each")
        if best: print("  Q=",best[0],"complex nodes",[(str(c[0]),str(c[1])) for c in best[1]],"weights",[str(s) for s in best[2]])
        else: print("  none with weight-1 reals in this family")

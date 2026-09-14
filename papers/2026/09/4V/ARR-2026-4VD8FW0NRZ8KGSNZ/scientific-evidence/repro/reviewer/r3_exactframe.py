# Independent high-precision evaluation of gamma for the exact frame B (spec json) and for the 40-digit point B
import mpmath as mp, json
from fractions import Fraction as Fr
from math import comb
mp.mp.dps=60
import os  # REPRO: package-relative path to the author's data
W=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","author")+"/"
spec=json.load(open(W+"s6_refined_B_exact_den100000000.json"))
n123=[[Fr(c) for c in v] for v in spec['n123']]; w=[Fr(c) for c in spec['w']]
for v in n123: assert sum(c*c for c in v)==1
s=[sum(v[c] for v in n123) for c in range(3)]
assert sum(a*b for a,b in zip(w,s))==0
q=(1-sum(c*c for c in s)/4)/sum(c*c for c in w); assert q>0
print("q=",float(q))
sq=mp.sqrt(mp.mpf(q.numerator)/q.denominator)
n=[[mp.mpf(c.numerator)/c.denominator for c in v] for v in n123]
sm=[mp.mpf(c.numerator)/c.denominator for c in s]; wm=[mp.mpf(c.numerator)/c.denominator for c in w]
n.append([-sm[c]/2+sq*wm[c] for c in range(3)]); n.append([-sm[c]/2-sq*wm[c] for c in range(3)])
print("check norms:", [mp.nstr(sum(c*c for c in v)-1,5) for v in n], "sum:", [mp.nstr(sum(v[c] for v in n),5) for c in range(3)])
def Qseq(t,K):
    a,b=1,0; x=2*t-1
    P=[mp.mpf(1),(a+1)+mp.mpf(a+b+2)/2*(x-1)]
    for m in range(1,K):
        c1=2*(m+1)*(m+a+b+1)*(2*m+a+b); c2=(2*m+a+b+1)*(a*a-b*b)
        c3=(2*m+a+b)*(2*m+a+b+1)*(2*m+a+b+2); c4=2*(m+a)*(m+b)*(2*m+a+b+2)
        P.append(((c2+c3*x)*P[m]-c4*P[m-1])/c1)
    return [P[k]/comb(k+1,k) for k in range(K+1)]
def gamma_of(n,K):
    pairs=[(i,j) for i in range(5) for j in range(i+1,5)]
    ts=[mp.mpf(2)/9*(1+sum(a*b for a,b in zip(n[i],n[j]))) for i,j in pairs]
    Qs=[Qseq(t,K) for t in ts]
    g={k: mp.mpf(9)/25*(5+2*sum(Q[k] for Q in Qs)) for k in range(2,K+1)}
    S=sum(1/(1-t) for t in ts)
    return g,S,ts
g,S,ts=gamma_of(n,600)
kmin=min(g,key=lambda k:g[k])
print("exact frame B: min g_k over 2..600 at k=",kmin," value",mp.nstr(g[kmin],20))
print("smallest:",[(k,mp.nstr(g[k],16)) for k in sorted(g,key=lambda k:g[k])[:7]])
print("S=",mp.nstr(S,8)," tail bound k>600:",mp.nstr(mp.mpf(9)/25*(5-2*S/602),8))
print("max overlap t:",mp.nstr(max(ts),8))
# 40-digit numerical point B
B=json.load(open(W+"s6_refined_B.json"))
nB=[[mp.mpf(c) for c in v] for v in B['n']]
print("point B norms/sum:", [mp.nstr(sum(c*c for c in v)-1,3) for v in nB], [mp.nstr(sum(v[c] for v in nB),3) for c in range(3)])
gB,SB,_=gamma_of(nB,2000)
kB=min(gB,key=lambda k:gB[k]); print("point B: min at k=",kB, mp.nstr(gB[kB],30), " reported gamma", B['gamma'][:32])
print("ties:",[(k,mp.nstr(gB[k],18)) for k in sorted(gB,key=lambda k:gB[k])[:8]])
# tail for B beyond 2000 by Lemma T
print("B tail k>2000 >=", mp.nstr(mp.mpf(9)/25*(5-2*SB/2002),8))

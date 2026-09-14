"""(a) kappa(1-m) <= c-a  for a>=1 (lemma), and its failure for a<1;
   the identity  c-a = [a=1]/Z + (a-1) E_k[(1-X)/X] + kappa E_k[1-X]  (a>=1), Z = int x^{a-1}(1-x)^{c-a-1}e^{kx}dx;
(b) sampled sign changes of Delta_q(k) = -k m(1-m^2) + (2q+5)m^2 - 2 + (q+1)(q+2)m/k along the L_q trajectory;
(c) tilted variance V(k) = K''(k) unimodality check for L_q (numerical, informative only)."""
import mpmath as mp, json
mp.mp.dps = 30
from scan_evenpart import HF

# (a)
print("--- (a) kappa(1-m) <= c-a")
for a in [mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('0.75'), 1, mp.mpf('1.5'), 2, 3, 5]:
    worst = -mp.inf
    for c in [a + mp.mpf(j)/2 for j in range(1, 41)]:
        for k in [mp.mpf(10)**e for e in [-2, -1, 0, 0.5, 1, 1.5, 2, 2.5, 3]]:
            M = mp.hyp1f1(a, c, k); m = a/c*mp.hyp1f1(a+1, c+1, k)/M
            worst = max(worst, k*(1-m) - (c-a))
    print(f"a={float(a):5.2f}: max over c,k of [k(1-m) - (c-a)] = {mp.nstr(worst, 8)}  ({'holds' if worst <= 0 else 'FAILS'})")
print("identity check (a>=1):")
for a, c, k in [(1, 3, 2), (1, 7, 15), (2, 5, 3), (mp.mpf('2.5'), 9, 20), (5, 30, 60)]:
    a = mp.mpf(a); c = mp.mpf(c); k = mp.mpf(k)
    f = lambda x: x**(a-1)*(1-x)**(c-a-1)*mp.exp(k*x)
    Z = mp.quad(f, [0, 1])
    E1mX = mp.quad(lambda x: f(x)*(1-x), [0, 1])/Z
    E_ratio = mp.quad(lambda x: f(x)*(1-x)/x, [0, 1])/Z if a > 1 else 0
    rhs = (1/Z if a == 1 else 0) + (a-1)*E_ratio + k*E1mX
    print(f"  a={float(a)} c={float(c)} k={float(k)}: c-a={float(c-a)}  rhs={mp.nstr(rhs, 15)}")

# (b)
print("--- (b) sign changes of Delta_q along the trajectory")
def signchanges(q, kmax=None, n=6000):
    kmax = kmax or 15*q + 60
    ks = [mp.mpf(kmax)*mp.mpf(10)**(-5 + 5*i/1000) for i in range(1001)]
    ks += [mp.mpf(kmax)*i/n for i in range(1, n+1)]
    ks = sorted(set(ks))
    print("GRID",q,len(ks),str(ks[0]),str(ks[-1]))
    D = [HF(q, k)[4] for k in ks]
    ch = [(float(ks[i]), float(ks[i+1])) for i in range(len(ks)-1) if D[i]*D[i+1] < 0]
    return ch, int(mp.sign(D[0])), int(mp.sign(D[-1]))
res = {}
for q in list(range(1, 13)) + [16, 20, 30, 40, 60]:
    ch, s0, s1 = signchanges(q)
    r = HF(q, 1)  # dummy
    from scan_evenpart import run
    res[q] = dict(changes=ch, sign0=s0, sign_inf=s1)
    print(f"q={q}: Delta sign at 0+: {s0}, at large k: {s1}, sign changes at {ch}")
json.dump(res, open('delta_signchanges.json', 'w'), indent=1)

# (c)
print("--- (c) tilted variance V(k) of L_q: number of local extrema on the grid")
for q in [3, 4, 5, 8, 12, 20, 40]:
    kmax = 15*q + 60
    ks = [mp.mpf(kmax)*i/3000 for i in range(1, 3001)]
    V = [HF(q, k)[3] for k in ks]
    ext = sum(1 for i in range(1, len(V)-1) if (V[i]-V[i-1])*(V[i+1]-V[i]) < 0)
    print(f"q={q}: local extrema of V on grid: {ext}; V(0+)={mp.nstr(V[0],6)}, max V={mp.nstr(max(V),6)} at k={mp.nstr(ks[V.index(max(V))],5)}")

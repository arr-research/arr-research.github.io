# s4iv: rigorous interval-arithmetic certificate (mpmath iv, outward rounding) for gamma(F) of an exact N=5 frame in C^3.
#   Configuration exactly as in s4: n1,n2,n3 rational unit vectors, s = n1+n2+n3, w rational with w.s = 0,
#   n4,5 = -s/2 +- sqrt(q) w, q = (1-|s|^2/4)/|w|^2 (rational). Exactness of the frame is checked with Fractions (s4.build).
#   t_ij = (2/9)(1 + n_i.n_j) = a_ij + b_ij sqrt(q) with a_ij, b_ij exact rationals; sqrt(q) is enclosed by iv.sqrt.
#   g_k = (9/25)[5 + 2 sum_{i<j} Q_{k,3}(t_ij)] via the three-term recurrence entirely in interval arithmetic (dps = PREC),
#   lower bound L_k = lower endpoint. Tail k > K0 by Lemma T: g_k >= (9/25)[5 - 2 S/(K0+2)], S = sum (1-t_ij)^{-1} (upper end).
#   Certified: gamma(F) >= min( min_{2<=k<=K0} L_k , tail ).  All rounding is outward, so the bound is rigorous.
from fractions import Fraction as Fr
import mpmath as mp, sys, json, time
from s4_d3_exact_certificate import build, Qs

def certify_iv(n123, w, K0=2000, PREC=120, verbose=True):
    t0 = time.time()
    n, q = build(n123, w)                      # exact; asserts unit norms and zero sum
    iv = mp.iv; iv.dps = PREC
    def I(fr): return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)
    sq = iv.sqrt(I(q))
    pairs = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    tq = [Fr(2, 9) * (1 + sum((a * b for a, b in zip(n[i], n[j])), Qs(0))) for i, j in pairs]     # exact a + b sqrt(q)
    t = [I(z.a) + I(z.b) * sq for z in tq]
    x = [2 * ti - 1 for ti in t]
    a, b = 1, 0
    Pm = [iv.mpf(1)] * 10; Pc = [iv.mpf(a + 1) + iv.mpf(a + b + 2) / 2 * (xi - 1) for xi in x]
    L = {}; W = {}
    for nn in range(1, K0):
        c1 = 2 * (nn + 1) * (nn + a + b + 1) * (2 * nn + a + b); c2 = (2 * nn + a + b + 1) * (a * a - b * b)
        c3 = (2 * nn + a + b) * (2 * nn + a + b + 1) * (2 * nn + a + b + 2); c4 = 2 * (nn + a) * (nn + b) * (2 * nn + a + b + 2)
        Pn = [((iv.mpf(c2) + iv.mpf(c3) * x[p]) * Pc[p] - iv.mpf(c4) * Pm[p]) / c1 for p in range(10)]
        Pm, Pc = Pc, Pn
        k = nn + 1
        g = iv.mpf(9) / 25 * (5 + 2 * sum(Pc, iv.mpf(0)) / (k + 1))
        L[k] = mp.mpf(g.a); W[k] = mp.mpf(g.delta)
    kmin = min(L, key=lambda k: L[k])
    S_hi = mp.mpf(sum((1 / (1 - ti) for ti in t), iv.mpf(0)).b)
    tail = mp.mpf((iv.mpf(9) / 25 * (5 - 2 * iv.mpf(S_hi) / (K0 + 2))).a)
    cert = min(L[kmin], tail)
    if verbose:
        srt = sorted(L, key=lambda k: L[k])[:7]
        print(f"q = {q}  (den digits {len(str(q.denominator))}); interval precision {PREC} digits; max enclosure width over k: {mp.nstr(max(W.values()), 3)}")
        print(f"min over 2<=k<={K0}: k={kmin}, lower bound {mp.nstr(L[kmin], 20)}")
        print("smallest degrees:", [(k, mp.nstr(L[k], 14)) for k in srt])
        print(f"tail k>{K0}: g_k >= {mp.nstr(tail, 10)}  (S <= {mp.nstr(S_hi, 6)})")
        print(f"CERTIFIED: gamma(F) >= {mp.nstr(cert, 25)}   [{time.time()-t0:.0f}s]")
    return cert, kmin, L

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1])); K0 = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    PREC = int(sys.argv[3]) if len(sys.argv) > 3 else 120
    certify_iv(spec['n123'], spec['w'], K0=K0, PREC=PREC)

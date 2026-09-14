# s1: exact rational spectra g_k of the regular (d+1)-simplex seed and the ONB in d = 3, 4.
# Q_{k,d}(t) = P_k^{(d-2,0)}(2t-1) / C(d+k-2,k), computed by the exact three-term recurrence in Fractions.
# g_k^simp(d) = d^2/(d+1) * (1 + d Q_{k,d}(1/d^2));  g_k^ONB(d) = d [1 + (d-1)(-1)^k / C(d+k-2,k)].
# Also: the tail-bound threshold used in the report:  |Q_{k,d}(t)| <= (1-t)^{-(d-2)} / C(k+d-2,k)  (Lemma T in report).
from fractions import Fraction as Fr
from math import comb
import sys, time

def jacobi_seq(alpha, beta, x, K):
    """P_n^{(alpha,beta)}(x), n = 0..K, exact (x Fraction). Standard recurrence (Szego 4.5.1)."""
    a, b = alpha, beta
    P = [Fr(1)]
    P.append(Fr(a + 1) + Fr(a + b + 2, 2) * (x - 1))
    for n in range(1, K):
        c1 = 2 * (n + 1) * (n + a + b + 1) * (2 * n + a + b)
        c2 = (2 * n + a + b + 1) * (a * a - b * b)
        c3 = (2 * n + a + b) * (2 * n + a + b + 1) * (2 * n + a + b + 2)
        c4 = 2 * (n + a) * (n + b) * (2 * n + a + b + 2)
        P.append(((c2 + c3 * x) * P[n] - c4 * P[n - 1]) / c1)
    return P

def Q_seq(d, t, K):
    P = jacobi_seq(d - 2, 0, 2 * Fr(t) - 1, K)
    return [P[k] / comb(d + k - 2, k) for k in range(K + 1)]

if __name__ == "__main__":
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    t0 = time.time()
    for d in (3, 4):
        Q = Q_seq(d, Fr(1, d * d), K)
        gS = [Fr(d * d, d + 1) * (1 + d * Q[k]) for k in range(K + 1)]
        gO = [d * (1 + (d - 1) * Fr((-1) ** k, comb(d + k - 2, k))) for k in range(K + 1)]
        kS = min(range(2, K + 1), key=lambda k: gS[k]); kO = min(range(2, K + 1), key=lambda k: gO[k])
        print(f"d={d}: ONB min_{{2<=k<={K}}} g_k = {gO[kO]} = {float(gO[kO]):.9f} at k={kO}; d-6/(d+1) = {Fr(d)-Fr(6,d+1)}")
        print(f"      simplex min_{{2<=k<={K}}} g_k = {gS[kS]} = {float(gS[kS]):.9f} at k={kS}; limit d^2/(d+1) = {float(Fr(d*d,d+1)):.6f}")
        print(f"      Q_{{{kS},{d}}}(1/{d*d}) = {Q[kS]} = {float(Q[kS]):.9f}")
        print("      g_k^simp, k=2..16:")
        for k in range(2, 17):
            print(f"         k={k:2d}: {str(gS[k]):>40s} = {float(gS[k]):.9f}   Q={float(Q[k]):+.9f}")
        # second-smallest, to document the margin
        srt = sorted(range(2, K + 1), key=lambda k: gS[k])
        print(f"      two smallest simplex values: k={srt[0]} ({float(gS[srt[0]]):.9f}), k={srt[1]} ({float(gS[srt[1]]):.9f})")
        # tail-bound check: for which k does the Lemma-T bound already force g_k > g_{kS}?
        t = Fr(1, d * d)
        need = -Q[kS]  # need Q_k > Q_kS i.e. |Q_k| < -Q_kS
        kk = next(k for k in range(2, K + 1) if Fr(1, (1 - t) ** (d - 2)) / comb(k + d - 2, k) < need)
        print(f"      Lemma-T bound (1-t)^-(d-2)/C(k+d-2,k) < {float(need):.9f} holds for all k >= {kk} (monotone); exact check covers 2<=k<{kk}")
        # verify: for every 2<=k<=K, k != kS: g_k > g_kS  (exact)
        assert all(gS[k] > gS[kS] for k in range(2, K + 1) if k != kS)
        print(f"      exact: g_k^simp > g_{kS}^simp for all 2<=k<={K}, k!={kS}  [OK]")
    print(f"runtime {time.time()-t0:.1f}s")

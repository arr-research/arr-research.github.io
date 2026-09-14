# s4int: EXACT, gcd-free certificate for gamma(F) of an exact N=5 frame in C^3 (configuration as in s4: n1,n2,n3 rational unit,
#   s = n1+n2+n3, w rational with w.s=0, n4,5 = -s/2 +- sqrt(q) w, q = (1-|s|^2/4)/|w|^2 rational; exactness asserted by s4.build).
#   Write q = qn/qd, rho := sqrt(qn*qd) (irrational or integer), so sqrt(q) = rho/qd and every overlap is t_ij = (Ta + Tb rho)/Dt
#   with integers Ta,Tb,Dt (common Dt). Jacobi recurrence for P_k^{(1,0)}(x), x = 2t-1 = (Xa + Xb rho)/Dt, in integer-scaled form:
#   P_k = (A_k + B_k rho)/M_k, M_{k+1} = c1(k) Dt M_k, all A,B,M integers (no gcd ever taken).
#   Lower bound: g_k = (9/25)[5 + 2 sum_p P_k(x_p)/(k+1)] >= (9/25)[5 + 2 (SA + SB rho)/((k+1)M_k)] with rho replaced by an integer
#   enclosure rho_lo <= rho <= rho_hi (isqrt); result floored to 10^-30 (floor = rigorous lower bound). Tail k > K0: Lemma T.
from fractions import Fraction as Fr
from math import isqrt
import sys, json, time
sys.set_int_max_str_digits(0)
from s4_d3_exact_certificate import build, Qs, sqrt_enclosure

def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)

def certify_int(n123, w, K0=600, verbose=True):
    t0 = time.time()
    n, q = build(n123, w)                                   # exact Fractions; asserts unit norms, zero sum
    qn, qd = q.numerator, q.denominator; Nq = qn * qd       # sqrt(q) = rho/qd, rho = sqrt(Nq)
    pairs = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    tq = [Fr(2, 9) * (1 + sum((a * b for a, b in zip(n[i], n[j])), Qs(0))) for i, j in pairs]   # a + b sqrt(q)
    xq = [(2 * t.a - 1, 2 * t.b / qd) for t in tq]         # x = xa + xb*rho, rationals
    Dt = 1
    for xa, xb in xq: Dt = lcm(lcm(Dt, xa.denominator), xb.denominator)
    X = [(int(xa * Dt), int(xb * Dt)) for xa, xb in xq]     # x_p = (Xa + Xb rho)/Dt
    # recurrence, a=1, b=0.  P_0 = 1 = (1 + 0 rho)/1 ; P_1^{(1,0)}(x) = 2 + (3/2)(x-1) = (3x+1)/2 = (3Xa + Dt + 3Xb rho)/(2Dt)
    a, b = 1, 0
    Am = [1] * 10; Bm = [0] * 10; Mm = 1
    Ac = [3 * X[p][0] + Dt for p in range(10)]; Bc = [3 * X[p][1] for p in range(10)]; Mc = 2 * Dt
    m = 40; R = isqrt(Nq * 10 ** (2 * m)); rho_lo, rho_hi = R, R + 1          # rho_lo/10^m <= rho <= rho_hi/10^m
    assert rho_lo ** 2 <= Nq * 10 ** (2 * m) < rho_hi ** 2
    SCALE = 10 ** 30
    lower = {}
    def lb(A, B, M, k):
        SA = sum(A); SB = sum(B)
        num_rho = SA * 10 ** m + SB * (rho_lo if SB >= 0 else rho_hi)   # lower bound of (SA + SB rho) * 10^m
        # g >= (9/25)(5 + 2 num_rho / ((k+1) M 10^m))
        den = 25 * (k + 1) * M * 10 ** m
        num = 9 * (5 * (k + 1) * M * 10 ** m + 2 * num_rho)
        return (num * SCALE) // den                              # floor(g_lo * SCALE)
    for nn in range(1, K0):
        c1 = 2 * (nn + 1) * (nn + a + b + 1) * (2 * nn + a + b); c2 = (2 * nn + a + b + 1) * (a * a - b * b)
        c3 = (2 * nn + a + b) * (2 * nn + a + b + 1) * (2 * nn + a + b + 2); c4 = 2 * (nn + a) * (nn + b) * (2 * nn + a + b + 2)
        ratio = Mc // Mm; assert ratio * Mm == Mc
        An = []; Bn = []
        for p in range(10):
            Xa, Xb = X[p]
            u, v = c2 * Dt + c3 * Xa, c3 * Xb              # (u + v rho)
            # (u + v rho)(Ac + Bc rho) = u Ac + v Bc Nq + (u Bc + v Ac) rho
            An.append(u * Ac[p] + v * Bc[p] * Nq - c4 * Dt * ratio * Am[p])
            Bn.append(u * Bc[p] + v * Ac[p] - c4 * Dt * ratio * Bm[p])
        Mn = c1 * Dt * Mc
        Am, Bm, Mm, Ac, Bc, Mc = Ac, Bc, Mc, An, Bn, Mn
        k = nn + 1
        lower[k] = lb(Ac, Bc, Mc, k)
    kmin = min(lower, key=lambda k: lower[k])
    # tail: S = sum (1 - t_ij)^{-1} upper bound with sqrt(q) enclosure (Fractions on 10 small numbers only)
    l, u = sqrt_enclosure(q)
    S_hi = sum(1 / (1 - t.bounds(l, u)[1]) for t in tq)
    tail = Fr(9, 25) * (5 - 2 * S_hi / (K0 + 2))
    cert = min(Fr(lower[kmin], SCALE), tail)
    if verbose:
        srt = sorted(lower, key=lambda k: lower[k])[:7]
        print(f"digits: Dt {len(str(Dt))}, Nq {len(str(Nq))}, final M_K0 {len(str(Mc))};  K0 = {K0}")
        print(f"min over 2<=k<={K0}: k={kmin}, g_k >= {lower[kmin]}/{SCALE} (exact rational)")
        print("smallest degrees (lower bounds):", [(k, round(lower[k] / SCALE, 14)) for k in srt])
        print(f"tail k>{K0}: g_k >= {float(tail):.8f}  (S <= {float(S_hi):.5f})")
        print(f"CERTIFIED: gamma(F) >= {float(cert):.15f}  (exact rational {cert.numerator}/{cert.denominator})   [{time.time()-t0:.0f}s]")
    return cert, kmin, lower

if __name__ == "__main__":
    if len(sys.argv) > 1:
        spec = json.load(open(sys.argv[1])); K0 = int(sys.argv[2]) if len(sys.argv) > 2 else 600
        certify_int(spec['n123'], spec['w'], K0=K0)
    else:
        certify_int([["0","0","1"], ["0","0","-1"], ["1","0","0"]], ["0","1","0"], K0=400)   # bipyramid test: 1.545185185185

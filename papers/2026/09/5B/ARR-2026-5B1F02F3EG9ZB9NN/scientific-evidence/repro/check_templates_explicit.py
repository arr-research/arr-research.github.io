"""check_templates_explicit.py -- second, independent check of the all-d certificates certs/alld_lower_*.json.

 (1) every support template is instantiated in EXPLICIT dimensions d = d0, ..., d0+8 and tested for Horn membership
     (I,J,K) in T^d_r directly from Horn's recursive definition (sum condition + all (F,G,H) in T^r_q, q<r) -- no
     symbolic slope argument, no reuse of the generator's stability test;
 (2) at each explicit d the certified inequality is re-assembled on s in R^d:  sum_r y_r [sum_K lambda_K <= sum_I s_i
     - sum_J s_{d+1-j}]  (+ ordering multipliers)  must give  sum_i c_i s_i >= bound with every c_i <= 1;
 (3) convention test: random Hermitian A, B in d = 6, 7: every Horn inequality sum_K gamma <= sum_I alpha + sum_J beta,
     (I,J,K) in T^d_r, holds for alpha = spec A, beta = spec B, gamma = spec(A+B) (decreasing) -- the necessity half of
     Horn's theorem in the convention used by all certificates.
Usage: python check_templates_explicit.py
"""
import sys, os, json, itertools, time
from fractions import Fraction as Q
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))

_T = {}
def horn_T(r, n):
    if (r, n) in _T: return _T[(r, n)]
    subs = list(itertools.combinations(range(1, n + 1), r)); out = []
    inner = [(q, horn_T(q, r)) for q in range(1, r)]
    for I in subs:
        for J in subs:
            sIJ = sum(I) + sum(J)
            for K in subs:
                if sIJ != sum(K) + r * (r + 1) // 2: continue
                if is_member_inner(I, J, K, inner): out.append((I, J, K))
    _T[(r, n)] = out
    return out

def is_member_inner(I, J, K, inner):
    for q, Tq in inner:
        for F, G, H in Tq:
            if sum(I[f - 1] for f in F) + sum(J[g - 1] for g in G) > sum(K[h - 1] for h in H) + q * (q + 1) // 2:
                return False
    return True

def is_horn_triple(I, J, K, r):
    I, J, K = tuple(sorted(I)), tuple(sorted(J)), tuple(sorted(K))
    if not (len(I) == len(J) == len(K) == r): return False
    if len(set(I)) < r or len(set(J)) < r or len(set(K)) < r: return False
    if sum(I) + sum(J) != sum(K) + r * (r + 1) // 2: return False
    return is_member_inner(I, J, K, [(q, horn_T(q, r)) for q in range(1, r)])

def inst(S, L, d): return tuple(sorted(list(S) + [d + 1 - t for t in L]))

def check_cert(fn, extra=8):
    C = json.load(open(fn)); N, M, d0 = C['N'], C['M'], C['d0']
    a = [Q(x) for x in C['a']]; b = [Q(x) for x in C['b']]; bound = Q(C['bound'])
    w = [Q(x) for x in C['order_multipliers']]
    ok_all = True
    for d in range(d0, d0 + extra + 1):
        lam = [list(a) + [Q(0)] * (d - 2 * N) + [-x for x in reversed(b)], list(b) + [Q(0)] * (d - 2 * N) + [-x for x in reversed(a)]]
        c = [Q(0)] * d; total = Q(0)
        for T in C['templates']:
            I = inst(T['I0'], T['I1'], d); J = inst(T['J0'], T['J1'], d); K = inst(T['K0'], T['K1'], d); r = T['r']; y = Q(T['y'])
            if not is_horn_triple(I, J, K, r) or y < 0:
                print(f"  FAIL d={d}: template {T} not a Horn triple / y<0"); ok_all = False; continue
            for i in I: c[i - 1] += y
            for j in J: c[d - j] -= y            # beta_j = -s_{d+1-j}
            total += y * sum(lam[T['refl']][k - 1] for k in K)
        # ordering multipliers (rows: s_{k+1}-s_k <= 0 for k<M ; s_{d-k}-s_{d+1-k} ... as in the generator)
        order = []
        for k in range(M - 1):
            e = [Q(0)] * d; e[k] = -1; e[k + 1] = 1; order.append(e)                    # s_{k+2} - s_{k+1} <= 0
        for k in range(M - 1):
            e = [Q(0)] * d; e[d - 1 - k] = 1; e[d - 2 - k] = -1; order.append(e)        # s_{d-k} - s_{d-k-1} <= 0
        e = [Q(0)] * d; e[d - M] = 1; e[M - 1] = -1; order.append(e)                    # s_{d+1-M} - s_M <= 0
        for wk, row in zip(w, order):
            if wk < 0: ok_all = False
            for i in range(d): c[i] -= wk * row[i]
        if any(ci > 1 for ci in c) or total != bound:
            print(f"  FAIL d={d}: combined coefficients {[str(x) for x in c]} total {total}"); ok_all = False
    print(f"  {os.path.basename(fn)}: N={N} M={M} d0={d0} bound={bound}: {len(C['templates'])} templates checked at d={d0}..{d0+extra}: {'OK' if ok_all else 'FAIL'}")
    return ok_all

def convention_test(d, ntrial, rng):
    T = [(r, t) for r in range(1, d) for t in horn_T(r, d)]
    worst = -1e9
    for _ in range(ntrial):
        def rh():
            X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)); return (X + X.conj().T) / 2
        A = rh(); B = rh()
        al = np.sort(np.linalg.eigvalsh(A))[::-1]; be = np.sort(np.linalg.eigvalsh(B))[::-1]; ga = np.sort(np.linalg.eigvalsh(A + B))[::-1]
        for r, (I, J, K) in T:
            worst = max(worst, sum(ga[k - 1] for k in K) - sum(al[i - 1] for i in I) - sum(be[j - 1] for j in J))
    print(f"  convention test d={d}: {len(T)} triples x {ntrial} random Hermitian pairs: max violation = {worst:.2e} (must be <= ~1e-12)")
    return worst < 1e-9

if __name__ == '__main__':
    t0 = time.time(); ok = True
    for fn in sorted(os.listdir(os.path.join(HERE, 'certs'))):
        if fn.startswith('alld_lower_') and fn.endswith('.json'):
            ok &= check_cert(os.path.join(HERE, 'certs', fn))
    rng = np.random.default_rng(2026)
    ok &= convention_test(6, 100, rng); ok &= convention_test(7, 30, rng)
    print(f"ALL OK: {ok}  [{time.time()-t0:.1f}s]")

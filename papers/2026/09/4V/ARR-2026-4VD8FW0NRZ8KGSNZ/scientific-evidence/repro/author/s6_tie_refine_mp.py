# s6: high-precision refinement of the d=3, N=5 optimum as the isolated solution of the tie system
#     g_5 = g_6 = g_8 = g_12 = g_18  (4 equations, 4 intrinsic dof; 7 redundant angle parameters -> Gauss-Newton with pseudo-inverse),
#     then KKT check: exists lambda >= 0, sum lambda = 1, sum_k lambda_k grad g_k = 0 (first-order condition for a local max of min_k g_k),
#     and a check that no other degree k <= 3000 falls below the tied value.
import mpmath as mp, json, sys
mp.mp.dps = 40
src = sys.argv[1] if len(sys.argv) > 1 else 's3_best_seed2.json'
ACT = [int(k) for k in sys.argv[2].split(',')] if len(sys.argv) > 2 else [5, 6, 8, 12, 18]
OUT = sys.argv[3] if len(sys.argv) > 3 else 's6_refined.json'
p = [mp.mpf(x) for x in json.load(open(src))['p']]

def bloch(p):
    n = []
    for i in range(3):
        th, ph = p[2 * i], p[2 * i + 1]
        n.append([mp.sin(th) * mp.cos(ph), mp.sin(th) * mp.sin(ph), mp.cos(th)])
    s = [sum(v[c] for v in n) for c in range(3)]
    s2 = sum(c * c for c in s)
    ax = [0, 0, 0]; ax[min(range(3), key=lambda c: abs(s[c]))] = 1
    e = [s[1] * ax[2] - s[2] * ax[1], s[2] * ax[0] - s[0] * ax[2], s[0] * ax[1] - s[1] * ax[0]]
    ne = mp.sqrt(sum(c * c for c in e)); e = [c / ne for c in e]
    f = [s[1] * e[2] - s[2] * e[1], s[2] * e[0] - s[0] * e[2], s[0] * e[1] - s[1] * e[0]]
    nf = mp.sqrt(sum(c * c for c in f)); f = [c / nf for c in f]
    rho = mp.sqrt(1 - s2 / 4); psi = p[6]
    v = [rho * (mp.cos(psi) * e[c] + mp.sin(psi) * f[c]) for c in range(3)]
    n.append([-s[c] / 2 + v[c] for c in range(3)]); n.append([-s[c] / 2 - v[c] for c in range(3)])
    return n

def spectrum(n, K):
    pairs = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    x = [2 * (mp.mpf(2) / 9 * (1 + sum(a * b for a, b in zip(n[i], n[j])))) - 1 for i, j in pairs]
    a, b = 1, 0
    Pm = [mp.mpf(1)] * 10; Pc = [(a + 1) + mp.mpf(a + b + 2) / 2 * (xi - 1) for xi in x]
    g = [mp.mpf(9), mp.mpf(9) / 25 * (5 + 2 * sum(Pc) / 2)]
    for nn in range(1, K):
        c1 = 2 * (nn + 1) * (nn + a + b + 1) * (2 * nn + a + b); c2 = (2 * nn + a + b + 1) * (a * a - b * b)
        c3 = (2 * nn + a + b) * (2 * nn + a + b + 1) * (2 * nn + a + b + 2); c4 = 2 * (nn + a) * (nn + b) * (2 * nn + a + b + 2)
        Pn = [((c2 + c3 * x[q]) * Pc[q] - c4 * Pm[q]) / c1 for q in range(10)]
        Pm, Pc = Pc, Pn
        g.append(mp.mpf(9) / 25 * (5 + 2 * sum(Pc) / (nn + 2)))
    return g

def F(p):
    g = spectrum(bloch(p), max(ACT))
    return [g[ACT[i]] - g[ACT[i + 1]] for i in range(len(ACT) - 1)]

def jac(fun, p, m):
    h = mp.mpf(10) ** (-15); J = mp.matrix(m, len(p))
    for j in range(len(p)):
        pp = list(p); pp[j] += h; fp = fun(pp); pm = list(p); pm[j] -= h; fm = fun(pm)
        for i in range(m): J[i, j] = (fp[i] - fm[i]) / (2 * h)
    return J

if __name__ == '__main__':
    for it in range(12):
        r = F(p); J = jac(F, p, len(ACT) - 1)
        U, S, V = mp.svd_r(J)
        # minimum-norm Gauss-Newton step: dp = -J^+ r
        dp = mp.matrix(len(p), 1)
        for k in range(len(S)):
            if S[k] > mp.mpf(10) ** (-12):
                coef = sum(U[i, k] * r[i] for i in range(len(r))) / S[k]
                for j in range(len(p)): dp[j] -= coef * V[k, j]
        p = [p[j] + dp[j] for j in range(len(p))]
        print(f"iter {it}: |F| = {mp.nstr(mp.norm(mp.matrix(F(p))), 5)}")
    n = bloch(p); g = spectrum(n, 3000)
    val = g[ACT[0]]
    print(f"tied value g_{ACT[0]} = ", mp.nstr(val, 35))
    print("tie residuals:", [mp.nstr(g[k] - val, 5) for k in ACT])
    others = sorted(((g[k], k) for k in range(2, 3001) if k not in ACT))[:6]
    print("next smallest non-active degrees:", [(k, mp.nstr(v, 12)) for v, k in others])
    G = [[mp.nstr(sum(a * b for a, b in zip(n[i], n[j])), 20) for j in range(5)] for i in range(5)]
    print("Gram (20 digits):"); [print("  ", row) for row in G]
    # KKT: gradients of the active g_k wrt the 7 angles; find lambda>=0, sum=1, with sum lambda_k grad g_k = 0
    def Gk(pp): 
        gg = spectrum(bloch(pp), max(ACT)); return [gg[k] for k in ACT]
    JG = jac(Gk, p, len(ACT))       # 5 x 7
    A = mp.matrix(len(ACT), len(ACT))  # solve: JG^T lambda = 0 with sum lambda = 1  -> least squares on [JG^T; 1...1]
    M = mp.matrix(8, 5)
    for i in range(7):
        for k in range(5): M[i, k] = JG[k, i]
    for k in range(5): M[7, k] = 1
    rhs = mp.matrix(8, 1); rhs[7] = 1
    lam = mp.lu_solve(M.T * M, M.T * rhs)
    res = M * lam - rhs
    print(f"KKT multipliers lambda (k={','.join(map(str, ACT))}):", [mp.nstr(lam[k], 10) for k in range(5)], " residual", mp.nstr(mp.norm(res), 3))
    json.dump({'p': [mp.nstr(x, 40) for x in p], 'n': [[mp.nstr(c, 40) for c in v] for v in n], 'gamma': mp.nstr(val, 40),
               'G': [[mp.nstr(sum(a * b for a, b in zip(n[i], n[j])), 40) for j in range(5)] for i in range(5)]}, open(OUT, 'w'), indent=1)

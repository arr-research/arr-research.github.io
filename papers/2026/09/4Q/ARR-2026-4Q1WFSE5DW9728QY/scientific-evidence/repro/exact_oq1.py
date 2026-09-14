"""Exact-arithmetic upgrade of the refutation of Open question 1 of the (m,2) paper (manuscript Section 6), run from repro/.

Uses the REVIEWER's independent Horn machinery (reviewer/myhorn.py: own Fulton recursion T^d_r, own LR counter, own Horn LP)
and the AUTHOR's LR counter (author/lr.py) as a second implementation.  Everything printed as "EXACT" is computed with
fractions.Fraction / integers; floating point is used only to *find* points and vertices.

Part A.  The two chamber points of reviewer/test_oq1.py are reproduced (same RNG seed and loops), rationalised (denominators
         <= 2000, trace restored), and at each rational point an exact primal-feasible vertex of the restricted Horn LP is
         reconstructed and verified against EVERY selected inequality.  If its objective is < g(lambda) exactly, weak duality
         shows that NO nonnegative combination of the selected tiles (with any multipliers, together with the ordering and
         nonnegativity constraints) can certify g.
           g1 = (3,1,1,2,2;-2,-1,0): tiles with box <= 3 (box = min(|lambda(I)|,|lambda(J)|)); this class contains every
                triple "adding n-1 = 3 boxes to a rectangle".
           g2 = (1,1,2,3,4;-2,-1,0): box <= 3, and separately the class "box 0 or lambda(I) or lambda(J) a single row or a
                single column (any length)", a superset of the Pieri-shaped tiles of Conjecture 5.3 of the report.
Part B.  The two certificates quoted in the manuscript are verified exactly: membership of every tile in the reviewer's T^9_r,
         LR coefficient by two implementations, s-coefficients <= 1 with each s_t (t <= m) once, and the integer identity
         "sum of right sides = g" after eliminating b_4 = a_1+...+a_5-b_1-b_2-b_3.
"""
import os, sys, json, time, itertools
import numpy as np
from fractions import Fraction as Q
from scipy.optimize import linprog
from scipy.sparse import csr_matrix

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "reviewer")); sys.path.insert(0, os.path.join(HERE, "author"))
from myhorn import HornLP, horn_T, part, strip, lr_coeff, spec      # reviewer's code
import lr as author_lr                                              # author's LR counter

m, n, z = 5, 4, 0; d = 9
rng = np.random.default_rng(11)          # same seed as reviewer/test_oq1.py

def canon(grad):
    alpha = np.array(grad[:m], float); beta = np.array([-grad[d - i] for i in range(1, n + 1)]); t = -beta[n - 1]
    return np.concatenate([alpha - t, beta[:n - 1] + t])

def form_val(f, a, b): return float(np.dot(f[:m], a) + np.dot(f[m:m + n - 1], b[:n - 1]))

def rand_point(law):
    if law == 'exp': a = rng.exponential(size=m); b = rng.exponential(size=n)
    elif law == 'unif': a = rng.uniform(size=m); b = rng.uniform(size=n)
    elif law == 'sq': a = rng.normal(size=m) ** 2; b = rng.normal(size=n) ** 2
    elif law == 'dom': a = rng.exponential(size=m); a[0] += 3 * a.sum(); b = 1 + 0.2 * rng.uniform(size=n)
    a = np.sort(a)[::-1]; b = np.sort(b)[::-1]
    return a / a.sum(), b / b.sum()

def find_point(H, S, g):
    """same search as reviewer/test_oq1.py: 40000 samples, keep the strict-chamber point of g with the largest margin."""
    best = None
    for it in range(40000):
        a, b = rand_point(['exp', 'unif', 'sq', 'dom'][it % 4]); lam = spec(a, b, z)
        vals = sorted(((form_val(f, a, b), f) for f in S), reverse=True)
        if vals[0][1] != g: continue
        margin = vals[0][0] - vals[1][0]
        if min(b[0] - b[1], min(np.diff(-a)), min(np.diff(-b))) < 1e-4: continue
        if best is None or margin > best[0]:
            r = H.solve(lam, want_dual=True); f = canon(r['grad'])
            if np.max(np.abs(f - np.array(g))) < 1e-6: best = (margin, a, b, r['val'])
    return best

def rationalise(a, b):
    aq = [Q(x).limit_denominator(2000) for x in a]; bq = [Q(x).limit_denominator(2000) for x in b]
    bq[0] = sum(aq) - sum(bq[1:])
    assert all(aq[i] >= aq[i + 1] for i in range(m - 1)) and all(bq[i] >= bq[i + 1] for i in range(n - 1)) and bq[-1] > 0
    return aq, bq, aq + [-x for x in bq[::-1]]

def gauss_solve(rows, rhs):
    """exact solve of a square system (list of int rows, list of Fractions); returns None if singular."""
    N = len(rows); M = [[Q(x) for x in r] + [Q(v)] for r, v in zip(rows, rhs)]
    for c in range(N):
        piv = next((r for r in range(c, N) if M[r][c] != 0), None)
        if piv is None: return None
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]; M[c] = [x / pv for x in M[c]]
        for r in range(N):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [M[r][N] for r in range(N)]

def exact_vertex(H, sel, lamq, label, tries=30):
    """Float LP over the selected rows (dual simplex, slightly perturbed objective if needed) -> active rows -> exact vertex ->
    exact feasibility for all selected rows, ordering and nonnegativity.  Returns (s exact, objective) or None."""
    lamf = np.array([float(x) for x in lamq]); idx = np.nonzero(sel)[0]
    A = np.vstack([-H.A[idx], H.ord]); ub = np.concatenate([-(H.B[idx] @ lamf), np.zeros(d - 2)])
    rhsQ_all = [sum(int(H.B[k][kk]) * lamq[kk] for kk in range(d)) for k in idx]     # exact right sides
    prng = np.random.default_rng(1)
    for attempt in range(tries):
        c = np.ones(d - 1) if attempt == 0 else np.ones(d - 1) + 1e-7 * prng.random(d - 1)
        res = linprog(c, A_ub=csr_matrix(A), b_ub=ub, bounds=[(0, None)] * (d - 1), method='highs-ds')
        assert res.status == 0, res.message
        s = res.x
        cand = []   # (int row, exact rhs)
        for j, k in enumerate(idx):
            if abs(H.A[k] @ s - float(rhsQ_all[j])) < 1e-7: cand.append(([int(x) for x in H.A[k]], rhsQ_all[j]))
        for t in range(d - 2):
            if abs(s[t] - s[t + 1]) < 1e-9: row = [0] * (d - 1); row[t] = 1; row[t + 1] = -1; cand.append((row, Q(0)))
        for t in range(d - 1):
            if abs(s[t]) < 1e-9: row = [0] * (d - 1); row[t] = 1; cand.append((row, Q(0)))
        order = list(range(len(cand))) if attempt == 0 else list(prng.permutation(len(cand)))
        rows, rhs = [], []
        for i in order:
            trial = rows + [cand[i][0]]
            if np.linalg.matrix_rank(np.array(trial, float)) > len(rows): rows.append(cand[i][0]); rhs.append(cand[i][1])
            if len(rows) == d - 1: break
        if len(rows) < d - 1: continue
        sq = gauss_solve(rows, rhs)
        if sq is None: continue
        feas = all(sum(int(H.A[k][t]) * sq[t] for t in range(d - 1)) >= rhsQ_all[j] for j, k in enumerate(idx))
        feas = feas and all(sq[t] >= sq[t + 1] for t in range(d - 2)) and sq[-1] >= 0
        if feas:
            print(f"   EXACT [{label}]: primal-feasible vertex s = {[str(x) for x in sq]} (attempt {attempt}); float LP value {res.fun:.6f}")
            return sq, sum(sq)
        print(f"   ({label}: attempt {attempt}: exact vertex candidate not feasible, retrying)")
    return None

def tile_sform(I, J, K):
    coef = [0] * (d - 1)
    for i in I:
        if i < d: coef[i - 1] += 1
    for j in J:
        if j > 1: coef[d - j] -= 1
    rhs = [0] * d
    for k in K: rhs[k - 1] += 1
    return coef, rhs

def rhs_in_ab(rhs):
    """coefficient vector of sum_{k in K} lambda_k in (a_1..a_5, b_1..b_4): lambda_j = a_j (j<=5), lambda_{10-i} = -b_i."""
    v = [0] * (m + n)
    for k in range(1, d + 1):
        if k <= m: v[k - 1] += rhs[k - 1]
        else: v[m + (d + 1 - k) - 1] -= rhs[k - 1]
    return v

def canon_ab(v):
    """eliminate b_4 = sum a - b_1 - b_2 - b_3 -> (alpha_1..alpha_5; beta_1..beta_3)."""
    c4 = v[m + n - 1]
    return tuple(v[j] + c4 for j in range(m)) + tuple(v[m + i] - c4 for i in range(n - 1))

if __name__ == "__main__":
    t0 = time.time()
    H = HornLP(d); print(f"reviewer's T^9: {H.ntri} triples ({time.time()-t0:.0f}s)")
    S = [tuple(json.loads(k)) for k in json.load(open(os.path.join(HERE, "author", "forms_m5_n4_z0.json"))) if not k.startswith('_')]
    print(f"author's S(5,4,0): {len(S)} forms")
    pieri = np.array([inf['box'] == 0 or len(inf['lI']) == 1 or all(x == 1 for x in inf['lI'])
                      or len(inf['lJ']) == 1 or all(x == 1 for x in inf['lJ']) for inf in H.info])
    print(f"Pieri-type class (box 0, or lambda(I) or lambda(J) a single row or column, any length): {pieri.sum()} of {H.ntri} triples")
    g1 = (3, 1, 1, 2, 2, -2, -1, 0); g2 = (1, 1, 2, 3, 4, -2, -1, 0)
    for g in (g1, g2):
        print(f"\n=== form g = {g} ===")
        best = find_point(H, S, g); assert best is not None
        margin, a, b, kap = best
        print(f"float chamber point: a={np.round(a,5)}, b={np.round(b,5)}; kappa={kap:.6f}; g(lambda)={form_val(g,a,b):.6f}; margin {margin:.4f}")
        aq, bq, lamq = rationalise(a, b)
        gq = sum(g[j] * aq[j] for j in range(m)) + sum(g[m + i] * bq[i] for i in range(n - 1))
        lamf = np.array([float(x) for x in lamq])
        print(f"EXACT rational point: a = {[str(x) for x in aq]}; b = {[str(x) for x in bq]}")
        print(f"   g(lambda_q) = {gq} = {float(gq):.6f}; full Horn LP kappa(lambda_q) (float) = {H.solve(lamf)['val']:.6f}; "
              f"restricted values box<=B, B=0..5: {[round(H.solve(lamf, Bmax=B)['val'], 6) for B in range(6)]}")
        classes = [("box<=3", H.box <= 3)]
        if g == g2: classes.append(("Pieri-type", pieri))
        for label, sel in classes:
            out = exact_vertex(H, sel, lamq, label)
            if out is None: print(f"   [{label}] no exact vertex found"); continue
            sq, tot = out
            print(f"   EXACT [{label}]: objective sum s = {tot} = {float(tot):.6f}; g(lambda_q) = {gq} = {float(gq):.6f}; "
                  f"sum s < g(lambda_q): {tot < gq}  ->  no certificate of g from the class '{label}' exists (weak duality)")
    # ---------------- Part B: the two certificates ----------------
    T9 = horn_T(9)
    def in_T9(I, J, K):
        r = len(I); return any(tuple(tuple(int(x) for x in row) for row in tri) == (I, J, K) for tri in T9[r])
    certs = {
        g1: [((1,), (1,), (1,)), ((1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 5, 6, 8, 9), (1, 2, 3, 4, 5, 6, 8, 9)),
             ((1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 5, 7, 8, 9), (1, 2, 3, 4, 5, 7, 8, 9)), ((1, 2, 5, 6), (1, 2, 3, 9), (1, 4, 5, 9))],
        g2: [((5,), (1,), (5,)), ((1, 5), (1, 5), (4, 5)), ((1, 2, 5, 6), (1, 2, 5, 9), (3, 4, 5, 9)),
             ((1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 5, 6, 8, 9), (1, 2, 3, 4, 5, 6, 8, 9)),
             ((1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 5, 7, 8, 9), (1, 2, 3, 4, 5, 7, 8, 9))]}
    for g, tiles in certs.items():
        print(f"\n=== certificate of g = {g} (Part B) ===")
        tot_coef = [0] * (d - 1); tot_rhs = [0] * (m + n)
        for (I, J, K) in tiles:
            lI, lJ, lK = strip(part(I)), strip(part(J)), strip(part(K))
            c_rev = lr_coeff(part(I), part(J), part(K)); c_auth = author_lr.lr(part(I), part(J), part(K))
            coef, rhs = tile_sform(I, J, K); v = rhs_in_ab(rhs)
            tot_coef = [x + y for x, y in zip(tot_coef, coef)]; tot_rhs = [x + y for x, y in zip(tot_rhs, v)]
            print(f"   I={I} J={J} K={K}: lambda(I)={lI} lambda(J)={lJ} lambda(K)={lK}; box={min(sum(lI),sum(lJ))}; in T^9: {in_T9(I,J,K)}; "
                  f"LR (reviewer, author) = ({c_rev}, {c_auth}); sum cond {sum(I)+sum(J)} == {sum(K)+len(I)*(len(I)+1)//2}; "
                  f"s-coef (s_1..s_8) = {coef}; RHS coef (a_1..a_5, b_1..b_4) = {v}")
        print(f"   SUM: s-coefficients {tot_coef} (each s_t, t<=5, once; max coefficient {max(tot_coef)}); "
              f"RHS in canonical coordinates {canon_ab(tot_rhs)} == g: {canon_ab(tot_rhs) == g}")
    print(f"\ndone ({time.time()-t0:.0f}s)")

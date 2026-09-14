"""Reviewer tests (d): Open question 1 refutation; (e): exposed-form counts (3,3,0), (4,4,0); d=8 example.
Own Horn LP with box filter.  Box(I,J,K) = min(|lambda(I)|, |lambda(J)|).
"""
import numpy as np, json, itertools, time
from fractions import Fraction as Q
from myhorn import HornLP, part, strip, lr_coeff, spec

rng = np.random.default_rng(11)
import os
WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author") + os.sep  # REPRO: was the absolute path of cycle3/work/A5_general_mn/

def canon(grad, m, n, z):
    d = m + z + n
    alpha = np.array(grad[:m], float)
    beta = np.array([-grad[d - i] for i in range(1, n + 1)])
    t = -beta[n - 1]
    return np.concatenate([alpha - t, beta[:n - 1] + t])

def form_val(f, a, b):
    m = len(a); n = len(b)
    return float(np.dot(f[:m], a) + np.dot(f[m:m + n - 1], b[:n - 1]))

def rand_point(m, n, law):
    if law == 'exp': a = rng.exponential(size=m); b = rng.exponential(size=n)
    elif law == 'unif': a = rng.uniform(size=m); b = rng.uniform(size=n)
    elif law == 'sq': a = rng.normal(size=m) ** 2; b = rng.normal(size=n) ** 2
    elif law == 'dom': a = rng.exponential(size=m); a[0] += 3 * a.sum(); b = 1 + 0.2 * rng.uniform(size=n)
    elif law == 'tie': a = rng.integers(1, 4, size=m).astype(float); b = rng.integers(1, 4, size=n).astype(float)
    a = np.sort(a)[::-1]; b = np.sort(b)[::-1]
    return a / a.sum(), b / b.sum()

def collect_forms(m, n, z, N):
    """integer forms from own-LP dual gradients at N random points."""
    d = m + n + z; H = HornLP(d); found = {}
    for it in range(N):
        a, b = rand_point(m, n, ['exp', 'unif', 'sq', 'dom'][it % 4])
        r = H.solve(spec(a, b, z), want_dual=True); f = canon(r['grad'], m, n, z)
        fi = np.round(f)
        if np.max(np.abs(f - fi)) < 1e-6:
            key = tuple(int(x) for x in fi); found[key] = found.get(key, 0) + 1
    return H, found

def validity_and_exposed(H, forms, m, n, z, N=400):
    """valid: f <= kappa at N random points (numerically); exposed: some sampled point where f is the strict max of the set and f == kappa."""
    forms = list(forms); F = np.array(forms, float)
    valid = {f: True for f in forms}; exposed = {f: False for f in forms}
    for it in range(N):
        a, b = rand_point(m, n, ['exp', 'unif', 'sq', 'dom', 'tie'][it % 5]); kap = H.solve(spec(a, b, z))['val']
        vals = np.array([form_val(f, a, b) for f in F])
        for k, f in enumerate(forms):
            if vals[k] > kap + 1e-7: valid[f] = False
        order = np.argsort(-vals)
        if vals[order[0]] - vals[order[1]] > 1e-6 and abs(vals[order[0]] - kap) < 1e-7: exposed[forms[order[0]]] = True
    return valid, exposed

if __name__ == "__main__":
    # ------------- (d) Open question 1 -------------
    m, n, z = 5, 4, 0; d = 9; H = HornLP(d)
    S = [tuple(json.loads(k)) for k in json.load(open(WORK + "forms_m5_n4_z0.json")) if not k.startswith('_')]
    print(f"author's S(5,4,0) has {len(S)} forms")
    for g in [(3, 1, 1, 2, 2, -2, -1, 0), (1, 1, 2, 3, 4, -2, -1, 0)]:
        # find a point where own LP gradient == g (chamber interior), with margin over the other author forms
        best = None
        for it in range(40000):
            a, b = rand_point(m, n, ['exp', 'unif', 'sq', 'dom'][it % 4]); lam = spec(a, b, z)
            vals = sorted(((form_val(f, a, b), f) for f in S), reverse=True)
            if vals[0][1] != g: continue
            margin = vals[0][0] - vals[1][0]
            if min(b[0] - b[1], min(np.diff(-a)), min(np.diff(-b))) < 1e-4: continue
            if best is None or margin > best[0]:
                r = H.solve(lam, want_dual=True); f = canon(r['grad'], m, n, z)
                if np.max(np.abs(f - np.array(g))) < 1e-6:
                    best = (margin, a, b, r['val'])
        if best is None:
            print(f"form g={g}: no strict-chamber point found among 40000 samples (skipped)"); continue
        margin, a, b, kap = best
        print(f"form g={g}: point a={np.round(a,5)}, b={np.round(b,5)}: kappa={kap:.6f} = g(lambda)={form_val(g,a,b):.6f}; margin over next form {margin:.4f}; own-LP gradient == g")
        lam = spec(a, b, z)
        vals = [H.solve(lam, Bmax=B)['val'] for B in range(0, 6)]
        print(f"   restricted LP values, box <= B for B=0..5: {[round(v,6) for v in vals]}  (full {kap:.6f}); gaps {[round(kap - v, 6) for v in vals]}")
        # tiles of the returned full certificate
        r = H.solve(lam, want_dual=True)
        act = sorted(r['active'], key=lambda t: -t[1])
        print("   active tiles of the full-LP dual (multiplier, box, lI, lJ, lK, I,J,K):")
        for k, y in act:
            inf = H.info[k]
            if inf['box'] > 0 or y > 0.5:
                print(f"      y={y:.4f} box={inf['box']} lI={inf['lI']} lJ={inf['lJ']} lK={inf['lK']} I={inf['I']} J={inf['J']} K={inf['K']} rectK={len(set(inf['lK']))<=1}")
        # exact check that no box<=3 certificate reaches kappa at a nearby RATIONAL point: rationalise the point, solve restricted LP (box<=3),
        # take the primal s, and verify (exactly, in Fractions) that s is feasible for all box<=3 triples and ordering after rounding UP slightly.
        aq = [Q(x).limit_denominator(2000) for x in a]; bq = [Q(x).limit_denominator(2000) for x in b]
        bq[0] = sum(aq) - sum(bq[1:])   # restore trace
        lamq = aq + [-x for x in bq[::-1]]
        lamf = np.array([float(x) for x in lamq]); kapq = H.solve(lamf)['val']; gq = sum(g[j] * aq[j] for j in range(m)) + sum(g[m + i] * bq[i] for i in range(n - 1))
        r3 = H.solve(lamf, Bmax=3); s3 = r3['x'] if 'x' in r3 else r3['s']
        # exact feasibility for box<=3 triples: find minimal uniform lift eps such that s + eps*(1,...,1) ... not valid (negative coefficients).
        # Instead: exact vertex reconstruction: active constraints -> solve exactly.
        sel = np.nonzero(H.box <= 3)[0]
        A = np.vstack([H.A[sel], -H.ord]); rhs = np.concatenate([H.B[sel] @ lamf, np.zeros(d - 2)])
        slack = A @ s3 - rhs
        act_rows = np.nonzero(np.abs(slack) < 1e-7)[0]
        # pick d-1 independent active rows exactly
        rowsQ = []; rhsQ = []
        Msel = []
        import sympy
        for i in act_rows:
            if i < len(sel):
                row = [int(x) for x in H.A[sel[i]]]; val = sum(int(H.B[sel[i]][k]) * lamq[k] for k in range(d))
            else:
                j = i - len(sel); row = [0] * (d - 1); row[j] = 1; row[j + 1] = -1; val = Q(0)
            cand = sympy.Matrix(rowsQ + [row])
            if cand.rank() > len(rowsQ):
                rowsQ.append(row); rhsQ.append(val)
            if len(rowsQ) == d - 1: break
        if len(rowsQ) == d - 1:
            Mq = sympy.Matrix(rowsQ); sq = Mq.LUsolve(sympy.Matrix([sympy.Rational(v.numerator, v.denominator) for v in rhsQ]))
            sq = [Q(int(x.p), int(x.q)) for x in sq]
            # exact feasibility check for ALL box<=3 triples and ordering, nonnegativity
            feas = all(sum(int(H.A[k][t]) * sq[t] for t in range(d - 1)) >= sum(int(H.B[k][kk]) * lamq[kk] for kk in range(d)) for k in sel)
            feas = feas and all(sq[t] >= sq[t + 1] for t in range(d - 2)) and sq[-1] >= 0
            tot = sum(sq)
            print(f"   EXACT: rational point (den<=2000); box<=3 vertex s = {[str(x) for x in sq]}; feasible for all box<=3 triples: {feas}; sum s = {tot} = {float(tot):.6f} < g(lambda) = {gq} = {float(gq):.6f}: {tot < gq}; full LP kappa(float) = {kapq:.6f}")
        else:
            print("   (exact vertex reconstruction did not find d-1 independent active rows)")
    # the claimed tile
    I, J, K = (1, 2, 5, 6), (1, 2, 3, 9), (1, 4, 5, 9)
    from myhorn import horn_T
    T9 = horn_T(9); inT = any(tuple(tuple(int(x) for x in row) for row in tri) == (I, J, K) for tri in T9[4])
    print(f"tile I={I} J={J} K={K}: lambda(I)={strip(part(I))} lambda(J)={strip(part(J))} lambda(K)={strip(part(K))}; in own T^9_4: {inT}; own LR = {lr_coeff(part(I), part(J), part(K))}; sum cond {sum(I)+sum(J)} == {sum(K)+10}")
    # s-form of the tile
    coef = np.zeros(8, int)
    for i in I:
        if i < 9: coef[i - 1] += 1
    for j in J:
        if j > 1: coef[9 - j] -= 1
    print(f"   s-form coefficients (s_1..s_8): {coef}; RHS = lambda_1+lambda_4+lambda_5+lambda_9 = a1+a4+a5-b1")
    # (5,3,0): does B_min reach 3 (> n-1 = 2)?  take the author's forms with B_min=3 and check at a chamber point
    m, n, z = 5, 3, 0; d = 8; H8 = HornLP(8)
    S53 = [tuple(json.loads(k)) for k in json.load(open(WORK + "forms_m5_n3_z0.json")) if not k.startswith('_')]
    hist = {}
    for g in S53:
        best = None
        for it in range(1500):
            a, b = rand_point(m, n, ['exp', 'unif', 'sq'][it % 3])
            vals = sorted(((form_val(f, a, b), f) for f in S53), reverse=True)
            if vals[0][1] != g: continue
            margin = vals[0][0] - vals[1][0]
            if best is None or margin > best[0]: best = (margin, a, b)
        if best is None: hist.setdefault('notfound', []).append(g); continue
        margin, a, b = best; lam = spec(a, b, z); kap = H8.solve(lam)['val']
        if abs(kap - form_val(g, a, b)) > 1e-7: hist.setdefault('mismatch', []).append(g); continue
        Bmin = next(B for B in range(0, 6) if H8.solve(lam, Bmax=B)['val'] >= kap - 1e-9)
        hist.setdefault(Bmin, []).append(g)
    print(f"(5,3,0): B_min histogram over author's {len(S53)} forms (own LP, own chamber points): { {k: len(v) for k, v in hist.items()} }; B_min=3 forms: {hist.get(3)}")
    # ------------- (e) exposed forms (3,3,0), (4,4,0) -------------
    for (m, n, z, N) in [(3, 3, 0, 1500), (4, 4, 0, 4000)]:
        t0 = time.time(); H, found = collect_forms(m, n, z, N)
        valid, exposed = validity_and_exposed(H, found, m, n, z)
        Sauth = set(tuple(json.loads(k)) for k in json.load(open(WORK + f"forms_m{m}_n{n}_z{z}.json")) if not k.startswith('_'))
        mine = set(f for f in found if valid[f] and exposed[f])
        print(f"(m,n,z)=({m},{n},{z}): integer dual forms found at {N} points: {len(found)}; valid & exposed (own criteria): {len(mine)}; author's list: {len(Sauth)}; "
              f"mine - author's: {sorted(mine - Sauth)}; author's - mine: {sorted(Sauth - mine)}; {time.time()-t0:.0f}s")
        if (m, n) == (3, 3): print("   own exposed set:", sorted(mine))
    # ------------- d=8 example -------------
    H8 = HornLP(8); lam = np.array([5, 1, 1, 1, -2, -2, -2, -2.]); r = H8.solve(lam, want_dual=True); kap = r['val']
    mins = [H8.min_coord_on_optimal_face(lam, t, kap) for t in range(5, 8)]
    S44 = [tuple(json.loads(k)) for k in json.load(open(WORK + "forms_m4_n4_z0.json")) if not k.startswith('_')]
    a = lam[:4]; b = -lam[4:][::-1]
    tied = [f for f in S44 if abs(form_val(f, a, b) - kap) < 1e-9]
    print(f"d=8 example (5,1,1,1,-2^4): kappa_8 = {kap:.6f}; optimal s = {np.round(r['s'],6)}; min s_5,s_6,s_7 on optimal face = {np.round(mins,6)} -> r_* = {4 + sum(1 for x in mins if x > 1e-9)}; "
          f"forms of author's S(4,4,0) attaining kappa: {tied}; own dual gradient {np.round(r['grad'],4)}")
    # also: is kappa_8 = 13 exactly? rational check via the optimal vertex
    print(f"   forms tied (own check of the two claimed): (3,1,1,2;-2,-1,0) -> {form_val((3,1,1,2,-2,-1,0),a,b)}, (4,1,2,2;-3,-2,-1) -> {form_val((4,1,2,2,-3,-2,-1),a,b)}")

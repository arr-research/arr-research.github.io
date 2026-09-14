"""verify_certificates.py -- independent, LP-free replay of the exact certificates in certs/.

Only Python stdlib (fractions) is used, plus geometry.py (54Q's exact construction of the finite set W_N,
copied verbatim from ARR-2026-54Q3HMFJ0Z8CZB4T) to regenerate the candidate sets.

What is checked (everything in exact rational arithmetic):
  gamma_N{N}.json[.gz]  : (a) the certified pairs are exactly the pairs of W_N with D_*>0 and the stored D_* is
                          right; (b) every stored hive is a genuine order-2N hive with boundary (s, -s^rev, lambda),
                          lambda = (a, -b^rev), s decreasing >= 0  => kappa <= sum s; (c) (H_N - sum s)/D_* >= gamma
                          for every pair; (d) at every listed minimizer a dual certificate proves kappa >= sum s,
                          so the ratio equals gamma there.  Conclusion: gamma_{N,2N} = gamma (54Q Theorem A).
  AB_costs.json         : every entry has a hive primal and a hive dual with equal value => exact kappa_d.
  kappa6_certificate.json: (a) 522 Horn triples regenerated from Horn's recursion; (b) for each of the 22 forms,
                          the extreme rays of its dominance chamber are recomputed by brute force and must match;
                          the chamber has full rank; (c) each ray carries an exact feasible s with sum s = q.rho
                          (upper bound on the chamber by conic combination); (d) a nonnegative Horn multiplier
                          vector proves sum s >= q.g for all feasible s (global lower bound).
                          Conclusion: kappa_6 = max_r q_r . g on the ordered chamber, all 22 forms exposed.
Hive convention (definition, not checked): order-d hive h on {(i,j): i,j>=0, i+j<=d}; for every unit rhombus
  h(obtuse_1)+h(obtuse_2) >= h(acute_1)+h(acute_2); edge (0,0)->(d,0) increments s_1..s_d; edge (d,0)->(0,d)
  increments -s_d..-s_1; edge (0,0)->(0,d) increments lambda_1..lambda_d.  Knutson-Tao: such a hive exists iff
  (s, -s^rev, lambda) is Horn-feasible, i.e. iff exist Hermitian R, S with spec R = spec S = s and R - S = F.
Usage: python verify_certificates.py [certs_dir]
"""
import sys, os, json, gzip, itertools, time
from fractions import Fraction as Q
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import geometry as G

FAIL = []
def check(cond, msg):
    if not cond:
        FAIL.append(msg); print("  FAIL:", msg)
    return cond

def load(fn):
    if fn.endswith('.gz'):
        with gzip.open(fn, 'rt', encoding='utf-8') as f: return json.load(f)
    with open(fn, encoding='utf-8') as f: return json.load(f)

# ------------------------------------------------------------------ hives (independent enumeration) ----------
def hive_points(d):
    return [(i, j) for i in range(d + 1) for j in range(d + 1 - i)]

def unit_rhombi(d):
    """Unit rhombi as (frozenset(obtuse pair), frozenset(acute pair)).  Parallelograms p+{0,u,v,u+v} with
    (u,v) in {((1,0),(0,1)) [60 deg at p]: obtuse p+u,p+v ; ((1,0),(-1,1)), ((0,1),(1,-1)) [120 deg at p]: obtuse p,p+u+v}."""
    inside = lambda p: p[0] >= 0 and p[1] >= 0 and p[0] + p[1] <= d
    out = set()
    for p in hive_points(d):
        for (u, v), acute_at_p in ((((1, 0), (0, 1)), True), (((1, 0), (-1, 1)), False), (((0, 1), (1, -1)), False)):
            pu = (p[0] + u[0], p[1] + u[1]); pv = (p[0] + v[0], p[1] + v[1]); puv = (pu[0] + v[0], pu[1] + v[1])
            if not all(inside(x) for x in (p, pu, pv, puv)): continue
            if acute_at_p: out.add((frozenset((pu, pv)), frozenset((p, puv))))
            else: out.add((frozenset((p, puv)), frozenset((pu, pv))))
    return out

def hive_from_cert(d, s, lam, h_den, h_int):
    pts = hive_points(d)
    if len(h_int) != len(pts): return None
    h = {p: Q(v, h_den) for p, v in zip(pts, h_int)}
    return h

def check_hive(d, s, lam, h, R):
    ok = True
    ok &= all(x >= 0 for x in s) and all(s[k] >= s[k + 1] for k in range(d - 1))
    ok &= h[(0, 0)] == 0
    ok &= all(h[(i, 0)] - h[(i - 1, 0)] == s[i - 1] for i in range(1, d + 1))
    ok &= all(h[(d - k, k)] - h[(d - k + 1, k - 1)] == -s[d - k] for k in range(1, d + 1))
    ok &= all(h[(0, j)] - h[(0, j - 1)] == lam[j - 1] for j in range(1, d + 1))
    if not ok: return False
    for ob, ac in R:
        if sum(h[p] for p in ob) < sum(h[p] for p in ac): return False
    return True

def check_hive_dual(d, lam, dual, R):
    """dual: {'y': [[o1,o2,a1,a2,val],...], 'z': [...], 'mu': [origin, A_1..A_d, B_1..B_d, C_1..C_d], 'value'}.
    Verifies stationarity of the Lagrangian of  min sum s  s.t. rhombus rows <= 0 (mult y>=0), ordering rows
    s_{k+1}-s_k <= 0 (mult z>=0), boundary equalities (mult mu), s >= 0 (mult = residual, must be >= 0).
    Returns the certified lower bound -mu.b (b = lambda on the C edge, 0 elsewhere) or None."""
    res_h = {p: Q(0) for p in hive_points(d)}; res_s = [Q(1)] * d
    for o1, o2, a1, a2, v in dual['y']:
        v = Q(v)
        if v < 0: return None
        key = (frozenset((tuple(o1), tuple(o2))), frozenset((tuple(a1), tuple(a2))))
        if key not in R: return None
        for p in key[1]: res_h[p] += v
        for p in key[0]: res_h[p] -= v
    z = [Q(v) for v in dual['z']]
    if len(z) != d - 1 or any(v < 0 for v in z): return None
    for k in range(d - 1):
        res_s[k] -= z[k]; res_s[k + 1] += z[k]
    mu = [Q(v) for v in dual['mu']]
    if len(mu) != 3 * d + 1: return None
    res_h[(0, 0)] += mu[0]
    for i in range(1, d + 1):                     # h(i,0)-h(i-1,0)-s_i = 0
        m = mu[i]; res_h[(i, 0)] += m; res_h[(i - 1, 0)] -= m; res_s[i - 1] -= m
    for k in range(1, d + 1):                     # h(d-k,k)-h(d-k+1,k-1)+s_{d+1-k} = 0
        m = mu[d + k]; res_h[(d - k, k)] += m; res_h[(d - k + 1, k - 1)] -= m; res_s[d - k] += m
    val = Q(0)
    for j in range(1, d + 1):                     # h(0,j)-h(0,j-1) = lambda_j
        m = mu[2 * d + j]; res_h[(0, j)] += m; res_h[(0, j - 1)] -= m; val -= m * lam[j - 1]
    if any(v != 0 for v in res_h.values()) or any(v < 0 for v in res_s): return None
    return val

# ------------------------------------------------------------------ gamma_N files ---------------------------
def verify_gamma(fn):
    t = time.time(); C = load(fn); N = C['N']; d = C['d']; H = Q(N + 1, 2); gamma = Q(C['gamma'])
    print(f"[gamma] {os.path.basename(fn)}: N={N} d={d} claimed gamma_{{N,{d}}} = {gamma}")
    check(Q(C['H']) == H, "H_N mismatch")
    W, _, _ = G.cut_vertices(N)
    expected = {(tuple(a), tuple(b)): G.D(a, b) for (a, b) in W if G.D(a, b) > 0}
    R = unit_rhombi(d)
    seen = {}
    worst = None; n_dual = 0
    for idx, P in enumerate(C['pairs']):
        a = tuple(Q(x) for x in P['a']); b = tuple(Q(x) for x in P['b'])
        key = (a, b)
        if not check(key in expected, f"pair {idx} not in W_N or has D_*=0"): continue
        Dst = expected[key]
        check(Q(P['Dstar']) == Dst, f"pair {idx}: D_* mismatch")
        seen[key] = True
        lam = list(a) + [Q(0)] * (d - 2 * N) + [-x for x in reversed(b)]
        s = [Q(x) for x in P['s']]
        h = hive_from_cert(d, s, lam, P['h_den'], P['h'])
        if not check(h is not None and check_hive(d, s, lam, h, R), f"pair {idx}: hive primal invalid"): continue
        cost = sum(s)
        check(Q(P['kappa_upper']) == cost, f"pair {idx}: stored kappa_upper != sum s")
        ratio = (H - cost) / Dst
        check(ratio >= gamma, f"pair {idx}: ratio {ratio} < gamma")
        if worst is None or ratio < worst[0]: worst = (ratio, idx)
        if P.get('dual'):
            val = check_hive_dual(d, lam, P['dual'], R)
            if check(val is not None, f"pair {idx}: dual invalid"):
                check(val == Q(P['dual']['value']), f"pair {idx}: dual value mismatch")
                check(val <= cost, f"pair {idx}: dual value exceeds primal cost")
                if val == cost: n_dual += 1
                if P.get('kappa') is not None: check(Q(P['kappa']) == val == cost, f"pair {idx}: stored kappa not certified")
    missing = [k for k in expected if k not in seen]
    check(not missing, f"{len(missing)} pairs of W_N with D_*>0 are not certified")
    check(len(seen) == len(C['pairs']), "duplicate pairs in certificate")
    mins = C['minimizers']
    for i in mins:
        P = C['pairs'][i]; a = tuple(Q(x) for x in P['a']); b = tuple(Q(x) for x in P['b'])
        lam = list(a) + [Q(0)] * (d - 2 * N) + [-x for x in reversed(b)]
        val = check_hive_dual(d, lam, P['dual'], R) if P.get('dual') else None
        cost = sum(Q(x) for x in P['s'])
        ok = check(val is not None and val == cost, f"minimizer {i}: no matching dual certificate")
        if ok: check((H - cost) / expected[(a, b)] == gamma, f"minimizer {i}: ratio != gamma")
    print(f"        pairs in W_N with D_*>0: {len(expected)}; certified: {len(seen)}; min ratio (from primals) = {worst[0]} at pair {worst[1]}; "
          f"duals matching primal: {n_dual}; minimizers with dual: {len(mins)}  [{time.time()-t:.1f}s]")
    if not any(m.startswith(f"pair") or m.startswith("minimizer") or 'W_N' in m for m in FAIL):
        print(f"        => PROVED (computer-assisted, exact): gamma_{{{N},{d}}} = {gamma}; minimizing pairs: " +
              "; ".join(f"a={C['pairs'][i]['a']} b={C['pairs'][i]['b']} kappa={C['pairs'][i]['kappa']}" for i in mins))

# ------------------------------------------------------------------ AB_costs ----------------------------------
def verify_AB(fn):
    t = time.time(); C = load(fn); Rs = {}
    print(f"[AB] {os.path.basename(fn)}: {len(C['entries'])} entries")
    for E in C['entries']:
        d = E['d']
        if d not in Rs: Rs[d] = unit_rhombi(d)
        lam = [Q(x) for x in E['lam']]; s = [Q(x) for x in E['s']]
        h = hive_from_cert(d, s, lam, E['h_den'], E['h'])
        okp = h is not None and check_hive(d, s, lam, h, Rs[d])
        val = check_hive_dual(d, lam, E['dual'], Rs[d])
        kap = Q(E['kappa'])
        ok = check(okp and val is not None and val == sum(s) == kap, f"AB entry {E['label']}: certificate invalid")
        extra = ''
        if 'conjectured' in E:
            extra = f"  conjectured {E['conjectured']} -> {'OK' if Q(E['conjectured']) == kap else 'MISMATCH'}"
            check(Q(E['conjectured']) == kap, f"AB entry {E['label']}: conjectured value differs")
        print(f"        {E['label']:>20}: kappa = {kap}{extra}   [{'ok' if ok else 'FAIL'}]")
    print(f"        [{time.time()-t:.1f}s]")

# ------------------------------------------------------------------ Horn triples (own implementation) --------
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
                good = True
                for q, Tq in inner:
                    for F, Gs, Hs in Tq:
                        if sum(I[f - 1] for f in F) + sum(J[g - 1] for g in Gs) > sum(K[h - 1] for h in Hs) + q * (q + 1) // 2:
                            good = False; break
                    if not good: break
                if good: out.append((I, J, K))
    _T[(r, n)] = out
    return out

def nullvec(rows, n):
    M = [list(r) for r in rows]; piv = []; rr = 0
    for c in range(n):
        p = next((i for i in range(rr, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[rr], M[p] = M[p], M[rr]; M[rr] = [x / M[rr][c] for x in M[rr]]
        for i in range(len(M)):
            if i != rr and M[i][c] != 0:
                f = M[i][c]; M[i] = [x - f * y for x, y in zip(M[i], M[rr])]
        piv.append(c); rr += 1
        if rr == len(M): break
    if rr != n - 1: return None
    free = [c for c in range(n) if c not in piv][0]
    v = [Q(0)] * n; v[free] = Q(1)
    for i, c in enumerate(piv): v[c] = -M[i][free]
    den = 1
    for x in v: den = den * x.denominator // gcd(den, x.denominator)
    iv = [int(x * den) for x in v]; g = 0
    for x in iv: g = gcd(g, abs(x))
    return tuple(x // g for x in iv)

def rank(rows):
    M = [list(map(Q, r)) for r in rows]; r = 0
    if not M: return 0
    for c in range(len(M[0])):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]; M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
    return r

def verify_kappa6(fn):
    t = time.time(); C = load(fn); d = 6; n = d - 1
    print(f"[kappa6] {os.path.basename(fn)}: {C['n_forms']} forms")
    T = [t3 for r in range(1, d) for t3 in horn_T(r, d)]
    check(len(T) == 522 == C['horn_triple_count'], f"Horn triple count {len(T)} != 522")
    Tset = set(T)
    def coefs(I, J, K):
        a = [Q(0)] * n
        for i in I:
            if i <= n: a[i - 1] += 1
        for j in J:
            if j >= 2: a[d - j] -= 1
        return a
    rows = [(coefs(I, J, K), K) for (I, J, K) in T]
    forms = [tuple(Q(x) for x in ch['q']) for ch in C['chambers']]
    check(len(set(forms)) == len(forms) == C['n_forms'], "form list has duplicates or wrong length")
    check(all(tuple(reversed(q)) in set(forms) for q in forms), "form list not closed under reversal")
    total_rays = 0
    for r, ch in enumerate(C['chambers']):
        q = forms[r]
        Hrep = [tuple(Q(int(i == k)) for k in range(n)) for i in range(n)]
        Hrep += [tuple(q[i] - qj[i] for i in range(n)) for j, qj in enumerate(forms) if j != r]
        rays = set()
        for sub in itertools.combinations(range(len(Hrep)), n - 1):
            v = nullvec([Hrep[i] for i in sub], n)
            if v is None: continue
            for cand in (v, tuple(-x for x in v)):
                if all(sum(h[i] * cand[i] for i in range(n)) >= 0 for h in Hrep): rays.add(cand)
        listed = [tuple(x) for x in ch['rays']]
        check(set(listed) == rays and len(listed) == len(rays), f"chamber {r}: extreme rays differ from recomputation")
        check(rank(listed) == n, f"chamber {r}: not full-dimensional")
        check(len(ch['witness_s']) == len(listed), f"chamber {r}: witness count")
        for rho, sw in zip(listed, ch['witness_s']):
            s = [Q(x) for x in sw]
            lam = [sum(Q(x) for x in rho[j:]) for j in range(n)] + [Q(0)]
            m = sum(lam) / d; lam = [x - m for x in lam]
            okp = all(x >= 0 for x in s) and all(s[k] >= s[k + 1] for k in range(n - 1))
            okp = okp and all(sum(lam[k - 1] for k in K) <= sum(a[i] * s[i] for i in range(n)) for a, K in rows)
            check(okp, f"chamber {r}: witness at ray {rho} infeasible")
            check(sum(s) == sum(q[i] * rho[i] for i in range(n)), f"chamber {r}: witness cost != q.rho at {rho}")
        # dual
        coef = [Q(0)] * n; w = [Q(0)] * d; okd = True
        for I, J, K, v in ch['dual_y']:
            v = Q(v); tri = (tuple(I), tuple(J), tuple(K))
            if v < 0 or tri not in Tset: okd = False; break
            a = coefs(*tri)
            for i in range(n): coef[i] += v * a[i]
            for k in K: w[k - 1] += v
        z = [Q(x) for x in ch['dual_z']]
        okd = okd and len(z) == n - 1 and all(x >= 0 for x in z)
        if okd:
            for k in range(n - 1): coef[k] += z[k]; coef[k + 1] -= z[k]
            okd = all(c <= 1 for c in coef)
            Wc = list(itertools.accumulate(w)); tot = Wc[-1]
            qg = tuple(Wc[j - 1] - Q(j, d) * tot for j in range(1, d))
            okd = okd and qg == q
        check(okd, f"chamber {r}: dual certificate invalid")
        total_rays += len(listed)
        print(f"        form {r:2d} q={[str(x) for x in q]}: {len(listed)} rays, full rank, witnesses ok, dual ok ({len(ch['dual_y'])} triples)")
    if not any('chamber' in m or 'form' in m or 'Horn' in m for m in FAIL):
        print(f"        => PROVED (computer-assisted, exact): kappa_6 = max of the {len(forms)} forms on the ordered chamber; every form exposed (full-dimensional chamber). total rays {total_rays}  [{time.time()-t:.1f}s]")


# ------------------------------------------------------------------ all-d lower bounds (windowed templates) ----
def verify_alld(fn):
    """Certificate: templates (I0,I1,J0,J1,K0,K1,r,refl,y) and ordering multipliers w.  Checks, independently of the
    generator: (1) each template is a Horn triple in EVERY dimension d >= d0 (sum condition with zero d-slope; every
    recursive condition (F,G,H) in T^r_q, q<r, has d-slope <= 0 and holds at d = d0); (2) the inequality it induces on
    x = (s_1..s_M, s'_1..s'_M), s'_t = s_{d+1-t}, after dropping nothing (all terms are kept as variables);
    (3) sum_r y_r coef_r - sum_k w_k order_k <= 1 componentwise with y, w >= 0; hence for every d >= d0 and every
    feasible s: kappa_d >= sum_i s_i + sum_t s'_t >= sum_r y_r val_r = bound."""
    t = time.time(); C = load(fn); N = C['N']; M = C['M']; d0 = C['d0']
    a = [Q(x) for x in C['a']]; b = [Q(x) for x in C['b']]; bound = Q(C['bound'])
    print(f"[all-d] {os.path.basename(fn)}: N={N} M={M} d0={d0} claimed kappa_d >= {bound} for all d >= {d0}")
    check(d0 >= 2 * M and M >= N, "window/d0 inconsistent")
    lam_small = [[a[k - 1] if k <= N else Q(0) for k in range(1, M + 1)], [b[k - 1] if k <= N else Q(0) for k in range(1, M + 1)]]
    bvals = [[b[t - 1] if t <= N else Q(0) for t in range(1, M + 1)], [a[t - 1] if t <= N else Q(0) for t in range(1, M + 1)]]
    nv = 2 * M; coef = [Q(0)] * nv; total = Q(0)
    for T in C['templates']:
        I0, I1, J0, J1, K0, K1, r, refl, y = T['I0'], T['I1'], T['J0'], T['J1'], T['K0'], T['K1'], T['r'], T['refl'], Q(T['y'])
        ok = y >= 0 and len(I0) + len(I1) == len(J0) + len(J1) == len(K0) + len(K1) == r and len(I1) + len(J1) == len(K1)
        ok = ok and all(1 <= i <= M for i in I0 + I1 + J0 + J1 + K0 + K1) and len(set(I0)) == len(I0) and len(set(I1)) == len(I1)              and len(set(J0)) == len(J0) and len(set(J1)) == len(J1) and len(set(K0)) == len(K0) and len(set(K1)) == len(K1)
        sym = lambda S, L: [(0, j) for j in sorted(S)] + [(1, 1 - t) for t in sorted(L, reverse=True)]   # (slope, const): index = slope*d + const
        I, J, K = sym(I0, I1), sym(J0, J1), sym(K0, K1)
        # sum condition: sum I + sum J = sum K + r(r+1)/2 identically in d
        ok = ok and sum(x[0] for x in I) + sum(x[0] for x in J) == sum(x[0] for x in K)              and sum(x[1] for x in I) + sum(x[1] for x in J) == sum(x[1] for x in K) + r * (r + 1) // 2
        for q in range(1, r):
            for F, Gs, Hs in horn_T(q, r):
                sl = sum(I[f - 1][0] for f in F) + sum(J[g - 1][0] for g in Gs) - sum(K[h - 1][0] for h in Hs)
                c = sum(I[f - 1][1] for f in F) + sum(J[g - 1][1] for g in Gs) - sum(K[h - 1][1] for h in Hs) - q * (q + 1) // 2
                if sl > 0 or sl * d0 + c > 0: ok = False
        if not check(ok, f"template {T} is not a Horn triple for all d >= {d0}"): continue
        # induced inequality  val <= coef_T . x   (alpha_i = s_i, alpha_{d+1-t} = s'_t, beta_j = -s'_j, beta_{d+1-t} = -s_t,
        # gamma_k = lam_k (k<=M, refl-dependent), gamma_{d+1-t} = -b_t)
        cT = [Q(0)] * nv
        for i in I0: cT[i - 1] += 1
        for tt in I1: cT[M + tt - 1] += 1
        for j in J0: cT[M + j - 1] -= 1
        for tt in J1: cT[tt - 1] -= 1
        val = sum(lam_small[refl][k - 1] for k in K0) - sum(bvals[refl][tt - 1] for tt in K1)
        for i in range(nv): coef[i] += y * cT[i]
        total += y * val
    w = [Q(x) for x in C['order_multipliers']]
    order = []
    for k in range(M - 1):
        e = [Q(0)] * nv; e[k] = -1; e[k + 1] = 1; order.append(e)        # s_{k+2} - s_{k+1} <= 0
    for k in range(M - 1):
        e = [Q(0)] * nv; e[M + k] = 1; e[M + k + 1] = -1; order.append(e)  # s'_{k+1} - s'_{k+2} <= 0
    e = [Q(0)] * nv; e[2 * M - 1] = 1; e[M - 1] = -1; order.append(e)      # s'_M - s_M <= 0 (valid since d+1-M > M)
    check(len(w) == len(order) and all(x >= 0 for x in w), "ordering multipliers invalid")
    for k, wk in enumerate(w):
        for i in range(nv): coef[i] -= wk * order[k][i]
    check(all(c <= 1 for c in coef), "combined coefficients exceed 1")
    check(total == bound, f"combination gives {total}, claimed {bound}")
    if not any('template' in m or 'multipliers' in m or 'coefficients' in m or 'combination' in m or 'window' in m for m in FAIL):
        print(f"        => PROVED (computer-assisted, exact): kappa_d(a,0^(d-2N),-b^rev) >= {bound} for EVERY d >= {d0}  ({len(C['templates'])} templates)  [{time.time()-t:.1f}s]")

if __name__ == '__main__':
    cdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'certs')
    t0 = time.time()
    for N in range(2, 20):
        for ext in ('.json', '.json.gz'):
            fn = os.path.join(cdir, f'gamma_N{N}{ext}')
            if os.path.exists(fn): verify_gamma(fn)
    fn = os.path.join(cdir, 'AB_costs.json')
    if os.path.exists(fn): verify_AB(fn)
    fn = os.path.join(cdir, 'kappa6_certificate.json')
    if os.path.exists(fn): verify_kappa6(fn)
    for fn in sorted(os.listdir(cdir)):
        if fn.startswith('alld_lower_') and fn.endswith('.json'): verify_alld(os.path.join(cdir, fn))
    print(f"\nTOTAL: {len(FAIL)} failures  [{time.time()-t0:.1f}s]")
    sys.exit(1 if FAIL else 0)

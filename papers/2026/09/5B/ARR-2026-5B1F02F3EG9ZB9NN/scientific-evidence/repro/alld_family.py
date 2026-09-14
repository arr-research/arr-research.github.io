"""alld_family.py -- dimension-independent lower bounds for kappa_d(a, 0^(d-2N), -b^rev), all d >= 2M, from a
STRUCTURED family of windowed Horn templates (same LP / dual / certificate format as stable_templates.py, so the
certificates are checked by verify_certificates.verify_alld, which re-derives Horn membership for all d >= d0 from
Horn's recursion for every template in the support):

  (G) every stable template with r <= r_gen (generic enumeration of stable_templates.templates; default r_gen = 2);
  (L) Lidskii-type templates for every r <= M:  I = [r], J = K  (I0 = [r], I1 = {}, J0 = K0, J1 = K1)  and the
      mirror  J = [r], I = K;  all (K0, K1) with |K0| + |K1| = r.  These are Horn triples in every dimension
      (Lidskii--Wielandt); they are NOT pre-filtered here -- the verifier re-checks each one used in the support.
Both orientations (a,b) and the reflected (b,a) are used (same feasible set of s, see stable_templates.py).

Usage: python alld_family.py N [M] [r_gen] [AB|UZ] [--tag NAME] [--k1max K] [--lean] [--k0 1,2,3]   (K = max number of large indices in the Lidskii K; --lean: for r >= 3 only I=[r] Lidskii, orientation refl=0)
"""
import sys, os, itertools, time, json
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from stable_templates import templates as generic_templates, exact_dual, fr
from gen_AB_costs import A_N, B_N, u3, z_N

def family(M, r_gen, k1max=None, lean=False, k0fix=None):
    seen = set()
    for T in generic_templates(M, r_gen):
        if T not in seen:
            seen.add(T); yield T
    idx = list(range(1, M + 1))
    for r in range(1, M + 1):
        R = tuple(range(1, r + 1))
        for k1 in range(0, r + 1):
            for K0 in itertools.combinations(idx, r - k1):
                if k1max is not None and k1 > k1max: continue
                if k0fix is not None and r >= 3 and K0 != k0fix: continue
                for K1 in itertools.combinations(idx, k1):
                    for T in (((R, (), K0, K1, K0, K1, r),) if (lean and r >= 3) else ((R, (), K0, K1, K0, K1, r), (K0, K1, R, (), K0, K1, r))):
                        if T not in seen:
                            seen.add(T); yield T

def build_lp(N, a, b, M, r_gen, k1max=None, lean=False, k0fix=None):
    t0 = time.time()
    ls = [[a[k - 1] if k <= N else Q(0) for k in range(1, M + 1)], [b[k - 1] if k <= N else Q(0) for k in range(1, M + 1)]]
    bs = [[b[t - 1] if t <= N else Q(0) for t in range(1, M + 1)], [a[t - 1] if t <= N else Q(0) for t in range(1, M + 1)]]
    nv = 2 * M; rows = []; rhs = []; tmpl = []
    for (I0, I1, J0, J1, K0, K1, r) in family(M, r_gen, k1max, lean, k0fix):
        coef = [0] * nv
        for i in I0: coef[i - 1] += 1
        for t in I1: coef[M + t - 1] += 1
        for j in J0: coef[M + j - 1] -= 1
        for t in J1: coef[t - 1] -= 1
        for refl in ((0,) if (lean and r >= 3) else (0, 1)):
            val = sum(ls[refl][k - 1] for k in K0) - sum(bs[refl][t - 1] for t in K1)
            rows.append(coef); rhs.append(val); tmpl.append((I0, I1, J0, J1, K0, K1, r, refl))
    print(f"  N={N} M={M} r_gen={r_gen}: {len(rows)} template rows  [{time.time()-t0:.1f}s]", flush=True)
    A = -np.array(rows, dtype=float); ub = -np.array([float(v) for v in rhs])
    order = []
    for k in range(M - 1):
        e = [0.0] * nv; e[k] = -1; e[k + 1] = 1; order.append(e)
    for k in range(M - 1):
        e = [0.0] * nv; e[M + k] = 1; e[M + k + 1] = -1; order.append(e)
    e = [0.0] * nv; e[2 * M - 1] = 1; e[M - 1] = -1; order.append(e)
    A = np.vstack([A, np.array(order)]); ub = np.concatenate([ub, np.zeros(len(order))])
    res = linprog(np.ones(nv), A_ub=A, b_ub=ub, bounds=[(0, None)] * nv, method='highs-ds')
    assert res.status == 0, res.message
    print(f"  LP lower bound = {res.fun:.10f} ~ {Q(res.fun).limit_denominator(10**6)}  x = {[str(Q(v).limit_denominator(10**4)) for v in res.x]}  [{time.time()-t0:.1f}s]", flush=True)
    return res, rows, rhs, tmpl, order

if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if not x.startswith('--')]
    N = int(args[0]); M = int(args[1]) if len(args) > 1 else N
    r_gen = int(args[2]) if len(args) > 2 else 2
    fam = args[3] if len(args) > 3 else 'AB'
    tag = sys.argv[sys.argv.index('--tag') + 1] if '--tag' in sys.argv else 'fam'
    k1max = int(sys.argv[sys.argv.index('--k1max') + 1]) if '--k1max' in sys.argv else None
    lean = '--lean' in sys.argv
    k0fix = tuple(int(x) for x in sys.argv[sys.argv.index('--k0') + 1].split(',')) if '--k0' in sys.argv else None
    a, b = (A_N(N), B_N(N)) if fam == 'AB' else (u3(N), z_N(N))
    print(f"target ({fam}) N={N}: a={[str(x) for x in a]} b={[str(x) for x in b]}")
    res, rows, rhs, tmpl, order = build_lp(N, a, b, M, r_gen, k1max, lean, k0fix)
    ed = exact_dual(res, rows, rhs, tmpl, order, 2 * M)
    if ed is None:
        print("  exact dual rationalization failed"); sys.exit(1)
    y, w, bound = ed
    print(f"  EXACT dimension-independent lower bound (all d >= {2*M}): kappa_d >= {bound}; support {len(y)} templates:")
    for r, v in sorted(y.items(), key=lambda kv: -kv[1]):
        print(f"     y={str(v):>8}  r={tmpl[r][6]} refl={tmpl[r][7]}  I0={tmpl[r][0]} I1={tmpl[r][1]} J0={tmpl[r][2]} J1={tmpl[r][3]} K0={tmpl[r][4]} K1={tmpl[r][5]}   val={rhs[r]}")
    out = {'family': fam, 'N': N, 'M': M, 'r_gen': r_gen, 'lidskii_family': True, 'k1max': k1max, 'lean': lean, 'k0fix': k0fix, 'd0': 2 * M, 'a': [fr(x) for x in a], 'b': [fr(x) for x in b], 'bound': fr(bound),
           'templates': [{'I0': list(tmpl[r][0]), 'I1': list(tmpl[r][1]), 'J0': list(tmpl[r][2]), 'J1': list(tmpl[r][3]), 'K0': list(tmpl[r][4]), 'K1': list(tmpl[r][5]), 'r': tmpl[r][6], 'refl': tmpl[r][7], 'y': fr(v)} for r, v in sorted(y.items()) if v != 0],
           'order_multipliers': [fr(v) for v in w]}
    fn = os.path.join(HERE, 'certs', f'alld_lower_{fam}_N{N}_{tag}.json')
    with open(fn, 'w') as f: json.dump(out, f)
    print(f"  wrote {fn}")

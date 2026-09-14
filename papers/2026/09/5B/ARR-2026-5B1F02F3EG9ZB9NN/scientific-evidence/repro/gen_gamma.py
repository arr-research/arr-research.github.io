"""gen_gamma.py N [N ...] -- exact certificates for the balanced-inertia stability constant

    gamma_{N,2N} = min_{(a,b) in W_N, D_*(a,b)>0} (H_N - kappa_{2N}(a, -b^rev)) / D_*(a,b)      (54Q Theorem A)

For every pair of the finite rational set W_N (54Q Lemma 2, geometry.cut_vertices) an exact hive primal
(upper bound on kappa) is stored; for every pair an exact hive dual (lower bound) is also computed so that
kappa is known exactly, and the duals are stored for the minimizing pairs (and, optionally, for all pairs
with --all-duals).  Output: certs/gamma_N{N}.json[.gz].

Certificate format (all rationals as strings "p/q"):
  {"N", "d", "H", "gamma", "minimizers": [pair indices], "hive_order": "points (i,j), i=0..d, j=0..d-i, lexicographic",
   "mu_order": "[origin, A_1..A_d, B_1..B_d, C_1..C_d]",
   "pairs": [{"a", "b", "Dstar", "s", "h_den", "h" (integers, h = h_int/h_den), "kappa" (exact, = primal cost = dual value),
              "ratio", "dual": null | {"y": [[o1,o2,a1,a2,"val"],...], "z": [...], "mu": [...], "value"}}]}
"""
import sys, json, gzip, time, os
from fractions import Fraction as Q
from math import lcm
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import geometry as G
from hive_exact import HiveLP, hive_points

def fr(x): return str(Q(x))

def pack_h(h, pts):
    den = 1
    for p in pts: den = lcm(den, h[p].denominator)
    return den, [int(h[p] * den) for p in pts]

def dual_json(M, dual):
    y = [[list(M.R[r][0]), list(M.R[r][1]), list(M.R[r][2]), list(M.R[r][3]), fr(v)] for r, v in sorted(dual['y'].items()) if v != 0]
    return {'y': y, 'z': [fr(v) for v in dual['z']], 'mu': [fr(v) for v in dual['mu']], 'value': fr(dual['value'])}

def run(N, all_duals=False, outdir='certs'):
    t0 = time.time()
    d = 2 * N; H = Q(N + 1, 2)
    W, cells, extra = G.cut_vertices(N)
    M = HiveLP(d); pts = hive_points(d)
    pairs = []; ratios = []
    n_dual_fail = 0; n_primal_support = 0; n_dual_support = 0
    for (a, b) in W:
        Dst = G.D(a, b)
        if Dst == 0:
            continue
        lam = list(a) + [Q(0)] * (d - 2 * N) + [-x for x in reversed(b)]
        c = M.certify(lam, want_dual=True)
        assert c['primal'] is not None, (a, b)
        if c['primal']['den_used'] == 'support': n_primal_support += 1
        kap_up = c['primal']['cost']
        if c['dual'] is None:
            n_dual_fail += 1; kap = None
        else:
            if c['dual']['den_used'] == 'support': n_dual_support += 1
            assert c['dual']['value'] == kap_up, (a, b, c['dual']['value'], kap_up)
            kap = kap_up
        den, hint = pack_h(c['primal']['h'], pts)
        rec = {'a': [fr(x) for x in a], 'b': [fr(x) for x in b], 'Dstar': fr(Dst),
               's': [fr(x) for x in c['primal']['s']], 'h_den': den, 'h': hint,
               'kappa_upper': fr(kap_up), 'kappa': None if kap is None else fr(kap),
               'ratio_lower': fr((H - kap_up) / Dst), '_dual': c['dual']}
        pairs.append(rec); ratios.append((H - kap_up) / Dst)
    gamma = min(ratios)
    mins = [i for i, r in enumerate(ratios) if r == gamma]
    for i, rec in enumerate(pairs):
        if (all_duals or i in mins) and rec['_dual'] is not None:
            rec['dual'] = dual_json(M, rec['_dual'])
        else:
            rec['dual'] = None
        del rec['_dual']
    out = {'N': N, 'd': d, 'H': fr(H), 'gamma': fr(gamma), 'n_pairs_W': len(W), 'n_pairs_certified': len(pairs),
           'minimizers': mins, 'hive_order': 'points (i,j), i=0..d, j=0..d-i, lexicographic; h = h_int/h_den',
           'mu_order': '[origin, A_1..A_d, B_1..B_d, C_1..C_d]',
           'conventions': 'edge A (0,0)->(d,0) carries s_1..s_d; edge B (d,0)->(0,d) carries -s_d..-s_1; edge C (0,0)->(0,d) carries lambda_1..lambda_d; rhombus: h(o1)+h(o2)>=h(a1)+h(a2); lambda = (a, 0^(d-2N), -b^rev)',
           'pairs': pairs, 'runtime_s': round(time.time() - t0, 1),
           'stats': {'dual_rationalization_failed': n_dual_fail, 'primal_support_resolve': n_primal_support, 'dual_support_resolve': n_dual_support}}
    txt = json.dumps(out)
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, f'gamma_N{N}.json')
    if len(txt) > 2_500_000:
        fn += '.gz'
        with gzip.open(fn, 'wt', encoding='utf-8') as f: f.write(txt)
    else:
        with open(fn, 'w', encoding='utf-8') as f: f.write(txt)
    print(f"N={N}: |W_N|={len(W)} certified={len(pairs)} gamma_{{N,{d}}} = {gamma} = {float(gamma):.8f}  "
          f"minimizers={[(pairs[i]['a'], pairs[i]['b'], pairs[i]['kappa']) for i in mins]}  "
          f"stats={out['stats']}  file={fn} ({len(txt)/1e6:.2f} MB raw)  [{time.time()-t0:.1f}s]", flush=True)
    return out

if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if not x.startswith('--')]
    all_duals = '--all-duals' in sys.argv
    for N in map(int, args):
        run(N, all_duals=all_duals)

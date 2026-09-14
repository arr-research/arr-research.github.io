"""gen_AB_costs.py -- exact hive primal+dual certificates for

  (i)  the (A_N, B) cost law, N = 3..14, d = 2N:
         A_N = ((3N-2)/(4N), ((N+2)/(4N(N-1)))^(N-1)),  B = (1/2, 1/2, 0^(N-2)),
         conjectured  kappa_{2N}(A_N, -B^rev) = 3/2 + m_N (N+2)/(4N(N-1)),  m_N = floor((N-2)^2/4) - 1;
  (ii) the (u_3, z_N) family, N = 6..12, d = 2N:
         u_3 = (1/3,1/3,1/3,0^(N-3)),  z_N = ((4N-3)/(9N), (4N-3)/(9N), ((N+6)/(9N(N-2)))^(N-2));
  (iii) zero-padding stability: the same targets in d = 2N+1, 2N+2, 2N+3 (exact kappa_d, both bounds).
Output: certs/AB_costs.json (self-describing; same primal/dual format as gamma_N*.json).
"""
import sys, os, json, time
from fractions import Fraction as Q
from math import lcm
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hive_exact import HiveLP, hive_points
from gen_gamma import fr, pack_h, dual_json

def A_N(N): return [Q(3 * N - 2, 4 * N)] + [Q(N + 2, 4 * N * (N - 1))] * (N - 1)
def B_N(N): return [Q(1, 2), Q(1, 2)] + [Q(0)] * (N - 2)
def u3(N): return [Q(1, 3)] * 3 + [Q(0)] * (N - 3)
def z_N(N): return [Q(4 * N - 3, 9 * N)] * 2 + [Q(N + 6, 9 * N * (N - 2))] * (N - 2)
def m_N(N): return (N - 2) ** 2 // 4 - 1

def cert_entry(M, a, b, d, N, label):
    lam = list(a) + [Q(0)] * (d - 2 * N) + [-x for x in reversed(b)]
    t = time.time(); c = M.certify(lam)
    assert c['primal'] is not None and c['dual'] is not None, label
    assert c['primal']['cost'] == c['dual']['value']
    den, hint = pack_h(c['primal']['h'], hive_points(d))
    return {'label': label, 'N': N, 'd': d, 'a': [fr(x) for x in a], 'b': [fr(x) for x in b],
            'lam': [fr(x) for x in lam], 's': [fr(x) for x in c['primal']['s']], 'h_den': den, 'h': hint,
            'kappa': fr(c['primal']['cost']), 'dual': dual_json(M, c['dual']), 'time_s': round(time.time() - t, 2)}

if __name__ == '__main__':
    out = {'hive_order': 'points (i,j), i=0..d, j=0..d-i, lexicographic; h = h_int/h_den',
           'mu_order': '[origin, A_1..A_d, B_1..B_d, C_1..C_d]', 'entries': []}
    models = {}
    def model(d):
        if d not in models: models[d] = HiveLP(d)
        return models[d]
    t0 = time.time()
    for N in range(3, 15):
        d = 2 * N
        e = cert_entry(model(d), A_N(N), B_N(N), d, N, f'(A_{N},B) d={d}')
        conj = Q(3, 2) + m_N(N) * Q(N + 2, 4 * N * (N - 1))
        e['conjectured'] = fr(conj); e['matches_conjecture'] = (Q(e['kappa']) == conj)
        out['entries'].append(e)
        print(f"N={N:2d} d={d:2d} (A_N,B): kappa = {e['kappa']:>8}  conj 3/2+m_N a_2 = {conj} m_N={m_N(N)}  match={e['matches_conjecture']}  s={e['s'][:N+2]}  [{e['time_s']}s]", flush=True)
    for N in range(6, 13):
        d = 2 * N
        e = cert_entry(model(d), u3(N), z_N(N), d, N, f'(u_3,z_{N}) d={d}')
        out['entries'].append(e)
        print(f"N={N:2d} d={d:2d} (u_3,z_N): kappa = {e['kappa']:>8}  s={e['s'][:N+2]}  [{e['time_s']}s]", flush=True)
    # padding stability at the minimizing pairs
    for N, (a, b, lab) in {6: (A_N(6), B_N(6), '(A_6,B)'), 7: (u3(7), z_N(7), '(u_3,z_7)'), 8: (u3(8), z_N(8), '(u_3,z_8)'),
                           9: (u3(9), z_N(9), '(u_3,z_9)'), 10: (u3(10), z_N(10), '(u_3,z_10)')}.items():
        for d in (2 * N + 1, 2 * N + 2, 2 * N + 3):
            e = cert_entry(model(d), a, b, d, N, f'{lab} d={d}')
            out['entries'].append(e)
            print(f"N={N:2d} d={d:2d} {lab} padded: kappa = {e['kappa']:>8}  s={e['s'][:N+2]}  [{e['time_s']}s]", flush=True)
    out['runtime_s'] = round(time.time() - t0, 1)
    with open(os.path.join('certs', 'AB_costs.json'), 'w') as f: json.dump(out, f)
    print('total', out['runtime_s'], 's')

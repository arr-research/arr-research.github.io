"""Export the exact witnesses computed by ../scratch_D2/grassmann_degree_exact.py (stored in witnesses.pkl)
and the lower-bound certificates recorded in its log (../scratch_D2/exact_rerun.log) to human-readable
JSON files, one per instance.  Run from this directory:  python export_witnesses.py
All numbers are exact elements of Q(i) written as SymPy strings (I = sqrt(-1), z = the variable)."""
import pickle, json, re, os
from sympy import sympify, Matrix, expand, Poly, symbols, I
z = symbols('z')
pkl = pickle.load(open('../scratch_D2/witnesses.pkl', 'rb'))
log = open('../scratch_D2/exact_rerun.log', encoding='utf-8').read().split('\n')
# split the log into instances (in the same order as the pickle keys)
blocks, cur = [], None
for line in log:
    if line.startswith('==='):
        if line.startswith('=== base-point'): continue
        cur = {'header': line, 'tuples': []}; blocks.append(cur)
    m = re.match(r'\s*\(e1,e2\)=\((\d+),(\d+)\) dimV=(\d+),(\d+) full-rank pair exists: (True|False)', line)
    if m and cur is not None:
        cur['tuples'].append({'e': [int(m.group(1)), int(m.group(2))], 'dimV': [int(m.group(3)), int(m.group(4))],
                              'full_rank_pair_exists': m.group(5) == 'True'})
assert len(blocks) == len(pkl), (len(blocks), len(pkl))
names = {'random1': 'random seed 1 (N=4, L=4)', 'random2': 'random seed 2 (N=4, L=4)', 'random3': 'random seed 3 (N=4, L=4)',
         'embedded5': 'seed 1 embedded in C^5', 'curve12': '(1,2)-curve data, L=4', 'curve12_L5': '(1,2)-curve data, L=5',
         'genericL3': 'generic L=3', 'genericL5': 'generic L=5', 'genericL6': 'generic L=6', 'genericL7': 'generic L=7'}
for (key, (Fs, delta, coldeg, Wstrs, zstrs)), blk in zip(pkl.items(), blocks):
    F = sympify(Fs); Ws = [sympify(w).applyfunc(expand) for w in Wstrs]; zetas = [sympify(s) for s in zstrs]
    N, k = Ws[0].shape
    cols = [[str(expand(F[a, j])) for a in range(N)] for j in range(k)]
    out = {'instance': key, 'description': names[key], 'source': 'scratch_D2/grassmann_degree_exact.py, rerun 2026-09-07',
           'N': N, 'k': k, 'L': len(zetas), 'nodes': [str(zt) for zt in zetas],
           'frames_rows': [[[str(W[a, b]) for b in range(k)] for a in range(N)] for W in Ws],
           'delta_Gr': delta, 'column_degrees': list(coldeg),
           'witness_columns': cols,
           'lower_bound_certificate': {'note': 'every column-degree pair (e1<=e2) with e1+e2 < delta_Gr fails: a zero V_e or a wedge form that is the zero matrix',
                                       'tuples': blk['tuples']}}
    fn = f'{key}.json'
    json.dump(out, open(fn, 'w', encoding='utf-8'), indent=1)
    print('wrote', fn, 'delta', delta, 'coldeg', coldeg, 'tuples', len(blk['tuples']))

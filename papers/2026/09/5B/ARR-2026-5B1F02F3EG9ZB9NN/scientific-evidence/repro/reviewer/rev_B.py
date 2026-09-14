"""rev_B.py -- (B) own verifier of gamma_N*.json[.gz] and AB_costs.json (exact Fractions)."""
import sys, os, time
from fractions import Fraction as Q
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # (repro copy: was the reviewer's scratchpad path)
from rev_lib import *
AUTH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')  # (repro copy: was the author's working directory)
sys.path.insert(0, AUTH)
import geometry as G   # byte-identical to the 54Q record (checked with diff); used only to regenerate W_N

def A_N(N): return [Q(3 * N - 2, 4 * N)] + [Q(N + 2, 4 * N * (N - 1))] * (N - 1)
def B_N(N): return [Q(1, 2), Q(1, 2)] + [Q(0)] * (N - 2)
def u3(N): return [Q(1, 3)] * 3 + [Q(0)] * (N - 3)
def z_N(N): return [Q(4 * N - 3, 9 * N)] * 2 + [Q(N + 6, 9 * N * (N - 2))] * (N - 2)

def verify_gamma(fn):
    t = time.time(); C = load_json(fn); N = C['N']; d = C['d']; H = Q(N + 1, 2); gamma = Q(C['gamma'])
    probs = []
    if d != 2 * N: probs.append('d != 2N')
    if Q(C['H']) != H: probs.append('H')
    W, _, _ = G.cut_vertices(N)
    # my own D_* on W_N
    expected = {}
    for (a, b) in W:
        a = tuple(Q(x) for x in a); b = tuple(Q(x) for x in b)
        if abs(sum(a) - 1) or abs(sum(b) - 1) or any(x < 0 for x in a + b) or any(a[i] < a[i+1] for i in range(N-1)) or any(b[i] < b[i+1] for i in range(N-1)):
            probs.append(f'W_N element not in ordered simplex {a} {b}')
        Dst = Dstar(a, b)
        if Dst > 0: expected[(a, b)] = Dst
    if len(W) != C['n_pairs_W']: probs.append('n_pairs_W')
    R = rhombi(d); seen = set(); ratios = []
    for idx, P in enumerate(C['pairs']):
        a = tuple(Q(x) for x in P['a']); b = tuple(Q(x) for x in P['b'])
        if (a, b) not in expected: probs.append(f'pair {idx} not in W_N with D_*>0'); continue
        if Q(P['Dstar']) != expected[(a, b)]: probs.append(f'pair {idx} Dstar')
        seen.add((a, b))
        lam = list(a) + [Q(0)] * (d - 2 * N) + [-x for x in reversed(b)]
        s = [Q(x) for x in P['s']]
        h = hive_from_json(d, P['h_den'], P['h'])
        ok, why = check_hive_primal(d, lam, s, h, R)
        if not ok: probs.append(f'pair {idx} primal: {why}'); continue
        cost = sum(s)
        if Q(P['kappa_upper']) != cost: probs.append(f'pair {idx} kappa_upper')
        ratio = (H - cost) / expected[(a, b)]
        if Q(P['ratio_lower']) != ratio: probs.append(f'pair {idx} ratio_lower')
        ratios.append((ratio, idx))
        if P.get('dual') is not None:
            val, why = check_hive_dual(d, lam, P['dual'], R)
            if val is None: probs.append(f'pair {idx} dual: {why}')
            else:
                if val != Q(P['dual']['value']): probs.append(f'pair {idx} dual value stored mismatch')
                if val > cost: probs.append(f'pair {idx} dual > primal (impossible)')
                if P.get('kappa') is not None and Q(P['kappa']) != val: probs.append(f'pair {idx} kappa != dual value')
        elif idx in C['minimizers']:
            probs.append(f'minimizer {idx} without dual')
    if seen != set(expected): probs.append(f'{len(set(expected) - seen)} pairs of W_N (D_*>0) missing')
    if len(seen) != len(C['pairs']): probs.append('duplicates')
    m = min(r for r, _ in ratios)
    if m != gamma: probs.append(f'min ratio {m} != gamma {gamma}')
    mins = [i for r, i in ratios if r == m]
    if sorted(mins) != sorted(C['minimizers']): probs.append(f'minimizer list {C["minimizers"]} vs mine {mins}')
    for i in mins:
        P = C['pairs'][i]
        if P.get('dual') is None or Q(P['dual']['value']) != sum(Q(x) for x in P['s']): probs.append(f'minimizer {i} dual not tight')
    # identify minimizers
    names = []
    for i in mins:
        a = tuple(Q(x) for x in C['pairs'][i]['a']); b = tuple(Q(x) for x in C['pairs'][i]['b'])
        nm = 'other'
        if (list(a), list(b)) == (A_N(N), B_N(N)): nm = '(A_N,B)'
        if (list(a), list(b)) == (B_N(N), A_N(N)): nm = '(B,A_N)'
        if (list(a), list(b)) == (u3(N), z_N(N)): nm = '(u3,z_N)'
        if (list(a), list(b)) == (z_N(N), u3(N)): nm = '(z_N,u3)'
        names.append((nm, str(Q(C['pairs'][i]['kappa'])), str(Q(C['pairs'][i]['Dstar']))))
    print(f"{os.path.basename(fn)}: N={N} d={d} |W|={len(W)} pairs D*>0 {len(expected)} certified {len(seen)}; gamma={gamma} ; my min ratio {m}; minimizers {names}; problems: {probs if probs else 'NONE'}  [{time.time()-t:.1f}s]", flush=True)
    return not probs

def verify_AB(fn):
    t = time.time(); C = load_json(fn); probs = []; Rs = {}
    for E in C['entries']:
        d = E['d']; N = E['N']
        if d not in Rs: Rs[d] = rhombi(d)
        lam = [Q(x) for x in E['lam']]; s = [Q(x) for x in E['s']]
        a = [Q(x) for x in E['a']]; b = [Q(x) for x in E['b']]
        if lam != a + [Q(0)] * (d - 2 * N) + [-x for x in reversed(b)]: probs.append(f'{E["label"]}: lam inconsistent')
        lab = E['label']
        if lab.startswith('(A_'):
            if (a, b) != (A_N(N), B_N(N)): probs.append(f'{lab}: (a,b) != (A_N,B)')
            conj = Q(3, 2) + ((N - 2) ** 2 // 4 - 1) * Q(N + 2, 4 * N * (N - 1))
            if Q(E['kappa']) != conj: probs.append(f'{lab}: kappa {E["kappa"]} != law {conj}')
        else:
            if (a, b) != (u3(N), z_N(N)): probs.append(f'{lab}: (a,b) != (u3,z_N)')
        h = hive_from_json(d, E['h_den'], E['h'])
        ok, why = check_hive_primal(d, lam, s, h, Rs[d])
        if not ok: probs.append(f'{lab}: primal {why}'); continue
        val, why = check_hive_dual(d, lam, E['dual'], Rs[d])
        if val is None or val != sum(s) or val != Q(E['kappa']): probs.append(f'{lab}: dual {why} {val} vs {sum(s)} vs {E["kappa"]}')
        print(f"   {lab:>18}: kappa = {E['kappa']:>9}  primal ok, dual = primal: {val == sum(s)}")
    print(f"AB_costs.json: {len(C['entries'])} entries; problems: {probs if probs else 'NONE'}  [{time.time()-t:.1f}s]", flush=True)

if __name__ == '__main__':
    which = sys.argv[1:] or ['3', '4', '5', '6', '7', '8', 'AB']
    for w in which:
        if w == 'AB': verify_AB(os.path.join(AUTH, 'certs', 'AB_costs.json'))
        else:
            for ext in ('.json', '.json.gz'):
                fn = os.path.join(AUTH, 'certs', f'gamma_N{w}{ext}')
                if os.path.exists(fn): verify_gamma(fn)

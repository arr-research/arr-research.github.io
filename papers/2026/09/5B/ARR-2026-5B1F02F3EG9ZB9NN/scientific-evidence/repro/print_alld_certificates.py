"""print_alld_certificates.py -- writes out every all-d certificate certs/alld_lower_*.json as a list of
human-readable Horn inequalities (Section 5 of the manuscript), re-assembles the certified combination with
exact Fractions, and asserts (i) the multiplied inequalities sum to  sum_i c_i s_i >= bound  with every c_i <= 1,
(ii) the value of each inequality's left side is what is printed.  Written for the manuscript; it does not reuse
the author's or the reviewer's checkers (the symbolic instantiation below is its own).

Notation: s_i (i <= N) are the leading entries of the common spectrum, s'_t := s_{d+1-t} the trailing ones
(the certificate is valid for every d >= 2N, where the two windows do not overlap).  alpha = s, beta = -s^rev,
lambda = (a, 0^(d-2N), -b^rev) for refl = 0 and (b, 0^(d-2N), -a^rev) for refl = 1.
Usage: python print_alld_certificates.py [file ...]   (default: all certs/alld_lower_*.json)
"""
import sys, os, json
from fractions import Fraction as Q
HERE = os.path.dirname(os.path.abspath(__file__))

def inst(T, N, a, b):
    """Return (lhs_terms, lhs_value, coeffs) for one template: lhs_terms is a list of strings naming the lambda
    entries, coeffs maps ('s',i)/('sp',t) -> Fraction."""
    lam_small = (b if T['refl'] else a); lam_large = (a if T['refl'] else b)
    ls, lb = ('b', 'a') if T['refl'] else ('a', 'b')
    terms = []; val = Q(0); co = {}
    for k in T['K0']:
        if k <= N: terms.append(f"{ls}_{k}"); val += lam_small[k - 1]
        else: terms.append("0")
    for t in T['K1']:
        if t <= N: terms.append(f"-{lb}_{t}"); val -= lam_large[t - 1]
        else: terms.append("0")
    for i in T['I0']: co[('s', i)] = co.get(('s', i), 0) + 1
    for t in T['I1']: co[('sp', t)] = co.get(('sp', t), 0) + 1
    for j in T['J0']: co[('sp', j)] = co.get(('sp', j), 0) - 1
    for t in T['J1']: co[('s', t)] = co.get(('s', t), 0) - 1
    return terms, val, co

def fmt_co(co):
    out = []
    for key in sorted(co, key=lambda k: (k[0] == 'sp', k[1])):
        c = co[key]
        if c == 0: continue
        name = f"s_{key[1]}" if key[0] == 's' else f"s'_{key[1]}"
        out.append((("+" if c > 0 else "-") + (str(abs(c)) if abs(c) != 1 else "") + name))
    s = " ".join(out)
    return s[1:] if s.startswith("+") else s

def sets(T):
    def f(S0, S1): return "{" + ", ".join([str(x) for x in S0] + [f"d+1-{t}" if t != 1 else "d" for t in S1]) + "}"
    return f(T['I0'], T['I1']), f(T['J0'], T['J1']), f(T['K0'], T['K1'])

def main(files):
    for fn in files:
        C = json.load(open(fn)); N = C['N']; a = [Q(x) for x in C['a']]; b = [Q(x) for x in C['b']]
        bound = Q(C['bound']); total = Q(0); coef = {}
        print(f"\n### {os.path.basename(fn)}: N = {N}, d >= {C['d0']}, a = {C['a']}, b = {C['b']}, bound {bound}")
        for T in C['templates']:
            y = Q(T['y']); terms, val, co = inst(T, N, a, b); I, J, K = sets(T)
            kind = "Weyl" if T['r'] == 1 else ("Lidskii-Wielandt" if (T['I0'] == list(range(1, T['r'] + 1)) and not T['I1'] and T['J0'] == T['K0'] and T['J1'] == T['K1']) else f"r = {T['r']}")
            print(f"- y = {y}, {'refl, ' if T['refl'] else ''}{kind}, I = {I}, J = {J}, K = {K}:  "
                  f"{' + '.join(terms).replace('+ -', '- ')} = {val}  <=  {fmt_co(co)}")
            total += y * val
            for k, c in co.items(): coef[k] = coef.get(k, 0) + y * c
        assert all(c <= 1 for c in coef.values()), coef
        assert total == bound, (total, bound)
        assert not C.get('order_multipliers') or all(Q(z) == 0 for z in C['order_multipliers'])
        print(f"  Sum: {fmt_co(coef)} >= {total} = bound; all coefficients <= 1, hence sum_all s >= {bound}.  OK")
    print("\nALL OK")

if __name__ == '__main__':
    files = sys.argv[1:] or sorted(os.path.join(HERE, 'certs', f) for f in os.listdir(os.path.join(HERE, 'certs')) if f.startswith('alld_lower_'))
    main(files)

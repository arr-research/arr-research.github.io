"""Independent check of the JSON witness files (exact arithmetic over Q(i), SymPy).  Run from this directory:
    python verify_witness.py            # about 15 s
For each file it verifies (1) nodes on the unit circle, distinct; frames of rank k; (2) the witness pencil P
interpolates: Q_i P(zeta_i) = 0 and rank P(zeta_i) = k at every node; (3) fdeg(P) = delta_Gr and the k x k minors
are coprime (so P is a minimal basis and a curve of degree delta_Gr through the data: upper bound); (4) the
lower-bound certificate: for every (e1<=e2) with e1+e2 < delta_Gr, the recorded dim V_{e1}, dim V_{e2} are
recomputed, and when both are positive every wedge form is recomputed and one of them is shown to be zero
(Lemma A, last form).  Final line: 'ALL WITNESS FILES VERIFIED'."""
import sys, json, glob, time, itertools
sys.path.insert(0, '../scratch_D2')
from sympy import sympify, Matrix, expand, symbols, I, Abs, simplify
import grassmann_degree_exact as G
z = symbols('z')
ok_all = True
for fn in sorted(glob.glob('*.json')):
    t0 = time.time(); d = json.load(open(fn, encoding='utf-8'))
    N, k, L, delta = d['N'], d['k'], d['L'], d['delta_Gr']
    zetas = [sympify(s) for s in d['nodes']]
    assert all(simplify(zt * zt.conjugate() - 1) == 0 for zt in zetas) and len(set(zetas)) == L
    Ws = [Matrix([[sympify(x) for x in row] for row in W]) for W in d['frames_rows']]
    assert all(W.rank() == k for W in Ws)
    Qs = [G.left_annihilator(W) for W in Ws]
    P = Matrix.hstack(*[Matrix([sympify(s) for s in col]) for col in d['witness_columns']])
    G.check_data(P, Qs, zetas, Ws, k)                       # interpolation and rank at nodes
    fd, g = G.forney_degree(P, N, k)
    assert fd == delta and g.degree() == 0, (fd, g)
    coldeg = [max(G.Poly(P[a, j], z).degree() for a in range(N) if P[a, j] != 0) for j in range(k)]
    assert coldeg == d['column_degrees'], coldeg
    # lower bound
    tuples = {tuple(t['e']): t for t in d['lower_bound_certificate']['tuples']}
    Vc = {}
    def V(e):
        if e not in Vc: Vc[e] = G.V_space(N, e, Qs, zetas)
        return Vc[e]
    for e1 in range(0, delta):
        for e2 in range(e1, delta - e1):
            t = tuples[(e1, e2)]; assert not t['full_rank_pair_exists']
            d1, d2 = V(e1).shape[1], V(e2).shape[1]
            assert [d1, d2] == t['dimV'], (fn, e1, e2, d1, d2, t)
            if d1 > 0 and d2 > 0:
                assert any(G.wedge_form(N, e1, e2, V(e1), V(e2), zetas[i], Ws[i]).is_zero_matrix for i in range(L)), (fn, e1, e2)
    print(f'{fn}: N={N} k={k} L={L} delta_Gr={delta} column degrees {coldeg} fdeg={fd} gcd={g.as_expr()} lower-bound tuples checked={sum(1 for e1 in range(delta) for e2 in range(e1, delta-e1))}  ({time.time()-t0:.1f}s)')
print('ALL WITNESS FILES VERIFIED')

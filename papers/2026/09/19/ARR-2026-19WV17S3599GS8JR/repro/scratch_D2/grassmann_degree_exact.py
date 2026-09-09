"""Exact computation of the Grassmannian interpolation degree delta_Gr.

Data: distinct boundary nodes zeta_i in T (Gaussian rationals on the unit circle),
target k-planes Y_i in C^N given by frames W_i (N x k) over Q(i).

delta_Gr = min { e_1+...+e_k : exists polynomial N x k matrix F, col j of degree <= e_j,
                 Q_i F(zeta_i) = 0 and rank F(zeta_i) = k for all i }.
By the minimal-basis argument (report, Lemma B) this equals the least Plucker degree of a
base-point-free rational curve P^1 -> Gr(k,H) through the data.

For k = 2 the existence test at a column-degree pair (e1,e2) is exact: the bilinear map
(f1,f2) -> f1(zeta_i) ^ f2(zeta_i) in Lambda^2 Y_i = C is a matrix B_i on V_{e1} x V_{e2};
a pair with rank 2 at every node exists iff every B_i is a nonzero matrix (product of
nonzero polynomials is nonzero).
"""
import sys, time, random, itertools, pickle
from sympy import Matrix, I, Rational, symbols, Poly, eye, zeros
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix

z = symbols('z')

# rational points on the unit circle
CIRCLE = [Rational(3,5)+Rational(4,5)*I, Rational(5,13)+Rational(12,13)*I,
          Rational(8,17)+Rational(15,17)*I, Rational(7,25)+Rational(24,25)*I,
          Rational(20,29)+Rational(21,29)*I, Rational(9,41)+Rational(40,41)*I,
          Rational(12,37)+Rational(35,37)*I, 1, I, -1, -I]

def dm(M):
    return DomainMatrix.from_Matrix(Matrix(M).applyfunc(lambda x: x.expand())).convert_to(QQ_I)

def nullspace(M):
    """columns = basis of right nullspace, as sympy Matrix over Q(i)"""
    D = dm(M)
    ns = D.nullspace().to_Matrix()   # rows are basis vectors
    return ns.T

def left_annihilator(W):
    return nullspace(Matrix(W).T).T   # rows q with q W = 0

def eval_matrix(N, e, zeta):
    """matrix of f -> f(zeta) on coefficient vector (c_0,...,c_e), each c_s in C^N"""
    return Matrix.hstack(*[zeta**s * eye(N) for s in range(e+1)])

def V_space(N, e, Qs, zetas):
    """basis (columns) of {f in C[z]^N, deg<=e : Q_i f(zeta_i)=0}; coefficient vectors."""
    rows = [Matrix(Q) * eval_matrix(N, e, zt) for Q, zt in zip(Qs, zetas)]
    A = Matrix.vstack(*rows)
    return nullspace(A)

def coeffs_to_poly_vec(c, N, e):
    return Matrix([sum(c[s*N+a]*z**s for s in range(e+1)) for a in range(N)])

def wedge_form(N, e1, e2, V1, V2, zeta, Wfr):
    """B_i: bilinear form (f1,f2) -> f1(zeta)^f2(zeta) in Lambda^2 Y (k=2), as matrix
    of size dim V1 x dim V2.  Coordinates of f(zeta) in the frame W (2 coords)."""
    E1 = eval_matrix(N, e1, zeta) * V1   # N x dimV1, values at zeta
    E2 = eval_matrix(N, e2, zeta) * V2
    W = Matrix(Wfr)
    Wl = (W.H * W).inv() * W.H
    C1 = Wl * E1; C2 = Wl * E2        # 2 x dim
    B = zeros(C1.shape[1], C2.shape[1])
    for a in range(C1.shape[1]):
        for b in range(C2.shape[1]):
            B[a,b] = (C1[0,a]*C2[1,b] - C1[1,a]*C2[0,b]).expand()
    return B

def forney_degree(F, N, k):
    """Plucker degree of the curve defined by polynomial N x k matrix F: max degree of
    the k x k minors after removing their gcd.  Also returns the gcd."""
    minors = []
    for rows in itertools.combinations(range(N), k):
        m = F.extract(list(rows), list(range(k))).det()
        m = Poly(m.expand(), z, domain=QQ_I)
        minors.append(m)
    nz = [m for m in minors if not m.is_zero]
    if not nz:
        return None, None
    g = nz[0]
    for m in nz[1:]:
        g = g.gcd(m)
    maxdeg = max(m.degree() for m in nz)
    return maxdeg - g.degree(), g

def delta_gr_k2(N, Qs, zetas, Ws, emax=8, verbose=True):
    """exact delta_Gr for k=2 by enumeration of column-degree pairs e1<=e2 in increasing sum"""
    L = len(zetas)
    Vcache = {}
    def V(e):
        if e not in Vcache:
            Vcache[e] = V_space(N, e, Qs, zetas)
        return Vcache[e]
    table = []
    for total in range(0, 2*emax+1):
        for e1 in range(0, total//2+1):
            e2 = total - e1
            V1, V2 = V(e1), V(e2)
            d1, d2 = V1.shape[1], V2.shape[1]
            ok = d1 > 0 and d2 > 0
            if ok:
                for i in range(L):
                    B = wedge_form(N, e1, e2, V1, V2, zetas[i], Ws[i])
                    if B.is_zero_matrix:
                        ok = False; break
            table.append(((e1,e2), d1, d2, ok))
            if verbose:
                print(f"  (e1,e2)=({e1},{e2}) dimV={d1},{d2} full-rank pair exists: {ok}")
            if ok:
                return total, (e1,e2), V1, V2, table
    return None

def random_pair(V1, V2, N, e1, e2, seed=0):
    rng = random.Random(seed)
    c1 = V1 * Matrix([rng.randint(-3,3) for _ in range(V1.shape[1])])
    c2 = V2 * Matrix([rng.randint(-3,3) for _ in range(V2.shape[1])])
    f1 = coeffs_to_poly_vec(c1, N, e1); f2 = coeffs_to_poly_vec(c2, N, e2)
    return Matrix.hstack(f1, f2)

def check_data(F, Qs, zetas, Ws, k):
    """verify Q_i F(zeta_i)=0 and rank F(zeta_i)=k"""
    for Q, zt, W in zip(Qs, zetas, Ws):
        Fz = F.subs(z, zt)
        assert (Matrix(Q)*Fz).expand().is_zero_matrix, "annihilator fails"
        assert Fz.rank() == k, "rank drops at node"
    return True

def span_dim(Ws):
    return Matrix.hstack(*[Matrix(W) for W in Ws]).rank()

def detector_bound_k2_N4(Ws, Qs):
    """52B6 Theorem 5.2 detector bound Delta for k=2 in C^4, L nodes, each node its own
    target (occupancy 1): max over admissible D (2x4, some rank(D W_i)=2) of
    sum_i (2 - rank(D W_i)).  Lower witnesses:
      - rank(D W_i)=0 forces D = G Q_i (annihilator); evaluate the others.
      - rank<=1 at a set J of nodes and rank 2 at the rest: for fixed d_1,
        det(D W_i)=0 (i in J) is linear in d_2; random d_1 gives an existence witness."""
    L = len(Ws)
    best = 0; witness = None
    for i in range(L):
        D = Matrix(Qs[i])
        ranks = [(D*Matrix(W)).rank() for W in Ws]
        s = sum(2 - r for r in ranks)
        if max(ranks) == 2 and s > best: best, witness = s, ('annihilator', i, ranks)
    rng = random.Random(1)
    for size in range(L-1, 0, -1):
        for J in itertools.combinations(range(L), size):
            found = False
            for trial in range(6):
                d1 = Matrix([[rng.randint(-5,5)+rng.randint(-5,5)*I for _ in range(4)]])
                rows = []
                for i in J:
                    W = Matrix(Ws[i]); a = d1*W   # 1x2
                    rows.append(a[0]*W[:,1].T - a[1]*W[:,0].T)
                A = Matrix.vstack(*rows)
                ns = nullspace(A)
                if ns.shape[1] == 0: continue
                d2 = (ns * Matrix([rng.randint(-3,3) for _ in range(ns.shape[1])])).T
                D = Matrix.vstack(d1, d2)
                ranks = [(D*Matrix(W)).rank() for W in Ws]
                if max(ranks) == 2:
                    s = sum(2-r for r in ranks)
                    if s > best: best, witness = s, ('pattern', J, ranks)
                    found = True; break
        if best >= size: break
    return best, witness

def instance_random(N, k, L, seed):
    rng = random.Random(seed)
    zetas = CIRCLE[:L]
    Ws = []
    for i in range(L):
        while True:
            W = Matrix(N, k, lambda a,b: rng.randint(-3,3)+rng.randint(-3,3)*I)
            if W.rank() == k: break
        Ws.append(W)
    Qs = [left_annihilator(W) for W in Ws]
    return zetas, Ws, Qs

def instance_from_curve(N, k, L, coldeg, seed):
    """targets generated by a random polynomial N x k matrix with given column degrees"""
    rng = random.Random(seed)
    zetas = CIRCLE[:L]
    while True:
        cols = []
        for j in range(k):
            cols.append(Matrix([sum((rng.randint(-3,3)+rng.randint(-3,3)*I)*z**s
                                    for s in range(coldeg[j]+1)) for a in range(N)]))
        P0 = Matrix.hstack(*cols)
        fd, g = forney_degree(P0, N, k)
        if fd is None: continue
        lead = Matrix(N, k, lambda a,j: Poly(P0[a,j], z).coeff_monomial(z**coldeg[j]) if P0[a,j] != 0 else 0)
        if fd == sum(coldeg) and g.degree() == 0 and lead.rank() == k:
            break
    Ws = [P0.subs(z, zt) for zt in zetas]
    assert all(W.rank() == k for W in Ws)
    Qs = [left_annihilator(W) for W in Ws]
    return zetas, Ws, Qs, P0

def report_instance(name, N, k, zetas, Ws, Qs):
    t0 = time.time()
    L = len(zetas)
    print(f"=== {name}: N={N} k={k} L={L}")
    r = span_dim(Ws)
    print(f"  span dim r={r}; span bound r-k={r-k}; universal k(L-1)={k*(L-1)}")
    res = delta_gr_k2(N, Qs, zetas, Ws)
    total, (e1,e2), V1, V2, table = res
    F = random_pair(V1, V2, N, e1, e2, seed=7)
    check_data(F, Qs, zetas, Ws, k)
    fd, g = forney_degree(F, N, k)
    print(f"  delta_Gr = {total} attained by column degrees {(e1,e2)}; random pair: Forney degree {fd}, gcd of minors = {g.as_expr()}")
    assert fd == total
    if N == 4 and k == 2:
        db, wit = detector_bound_k2_N4(Ws, Qs)
        print(f"  52B6 detector bound Delta >= {db}  (witness: {wit})")
        allfull = all((Matrix(Qs[i])*Matrix(Ws[j])).rank()==2 for i in range(L) for j in range(L) if i!=j)
        print(f"  rank(Q_i W_j)=2 for all i!=j: {allfull}  (then a zero-rank node forces the other ranks to 2, so Delta <= max(2, L-1))")
    print("  polynomial witness F (columns):")
    for j in range(k):
        print("   ", [F[a,j].expand() for a in range(N)])
    print(f"  time {time.time()-t0:.1f}s")
    sys.stdout.flush()
    return F, total, (e1,e2), Ws, zetas

if __name__ == '__main__':
    out = {}
    for seed in [1,2,3]:
        zetas, Ws, Qs = instance_random(4, 2, 4, seed)
        out[f'random{seed}'] = report_instance(f"random seed {seed}", 4, 2, zetas, Ws, Qs)
    zetas, Ws, Qs = instance_random(4, 2, 4, 1)
    Ws5 = [Matrix.vstack(W, zeros(1,2)) for W in Ws]
    Qs5 = [left_annihilator(W) for W in Ws5]
    out['embedded5'] = report_instance("random seed 1 embedded in C^5 (H = C^4 proper)", 5, 2, zetas, Ws5, Qs5)
    zetas, Ws, Qs, P0 = instance_from_curve(4, 2, 4, (1,2), seed=5)
    print("generating curve P0 columns:", [[P0[a,j].expand() for a in range(4)] for j in range(2)])
    out['curve12'] = report_instance("structured (1,2)-curve data, L=4", 4, 2, zetas, Ws, Qs)
    zetas, Ws, Qs, P0 = instance_from_curve(4, 2, 5, (1,2), seed=6)
    print("generating curve P0 columns:", [[P0[a,j].expand() for a in range(4)] for j in range(2)])
    out['curve12_L5'] = report_instance("structured (1,2)-curve data, L=5", 4, 2, zetas, Ws, Qs)
    Fb = Matrix.hstack(P0[:,0], (z - Rational(1,2))*P0[:,1])
    fd, g = forney_degree(Fb, 4, 2)
    print(f"=== base-point example: column degrees (1,3), naive minor degree 4, gcd = {g.as_expr()}, Forney degree = {fd}")
    for L in [3,5,6,7]:
        zetas, Ws, Qs = instance_random(4, 2, L, 11+L)
        out[f'genericL{L}'] = report_instance(f"generic k=2 N=4 L={L}", 4, 2, zetas, Ws, Qs)
    with open('witnesses.pkl','wb') as fh:
        pickle.dump({kk:(str(v[0]), v[1], v[2], [str(W) for W in v[3]], [str(zt) for zt in v[4]]) for kk,v in out.items()}, fh)
    print("done")

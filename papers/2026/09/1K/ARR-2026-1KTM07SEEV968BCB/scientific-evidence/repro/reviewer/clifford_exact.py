"""Exact verification (in Z[omega_{2d}] for p=2, Z[omega_d] for odd p) that
   U_s = F' Q_s          and     V_s = F'^{-1} Q_s F'
conjugate every Weyl W_(a,b) = X^a Z^b to  phase * W_{M(a,b)}  with phase a 2d-th (resp. d-th) root of unity,
and that the first coordinates of the label maps cover every primitive direction of (Z/d)^2.
  p odd: Q_s = diag(omega^{s 2^{-1} j^2}), s in Z/d.       p = 2: Q_s = diag(omega_{2d}^{s j^2}), s in Z/d.
We compute d * U W U^{-1} = F' Q_s W Q_s^* F'^*  and  d^2 * V W V^{-1} = F'^* Q_s F' W F'^* Q_s^* F'   exactly.
usage: python clifford_exact.py d [d ...]
"""
import sys
from math import gcd
from cyclo import Cyclo

def factor_pk(d):
    p = 2
    while d % p: p += 1
    k = 0; dd = d
    while dd % p == 0: dd //= p; k += 1
    assert dd == 1
    return p, k

def run(d):
    p, k = factor_pk(d)
    N = 2*d if p == 2 else d           # field Z[omega_N]
    F = Cyclo(N)
    om = lambda t: F.root_pow(t * (N // d))       # omega_d^t
    omN = lambda t: F.root_pow(t)                 # omega_N^t
    def matmul(A, B):
        n = len(A)
        C = [[F.zero() for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for l in range(n):
                if F.is_zero(A[i][l]): continue
                for j in range(n):
                    if F.is_zero(B[l][j]): continue
                    C[i][j] = F.add(C[i][j], F.mul(A[i][l], B[l][j]))
        return C
    def weyl(a, b):
        W = [[F.zero() for _ in range(d)] for _ in range(d)]
        for j in range(d):
            W[(j+a) % d][j] = om(b*j)
        return W
    def diag(vals):
        return [[vals[i] if i == j else F.zero() for j in range(d)] for i in range(d)]
    Fp = [[om(i*j) for j in range(d)] for i in range(d)]
    Fps = [[om(-i*j) for j in range(d)] for i in range(d)]  # F'^* (conjugate transpose; F' symmetric)
    if p == 2:
        Q = lambda s: diag([omN(s*j*j) for j in range(d)])
        Qs = lambda s: diag([omN(-s*j*j) for j in range(d)])
    else:
        inv2 = pow(2, -1, d)
        Q = lambda s: diag([om(s*inv2*j*j) for j in range(d)])
        Qs = lambda s: diag([om(-s*inv2*j*j) for j in range(d)])
    Wall = {(a, b): weyl(a, b) for a in range(d) for b in range(d)}
    roots = [omN(t) for t in range(N)]
    def match(A, scale, target):
        """A == scale * root * target for some root of unity in mu_N ?  return root index or None"""
        # find a nonzero entry of target
        for i in range(d):
            for j in range(d):
                if not F.is_zero(target[i][j]):
                    for t in range(N):
                        R = F.mul(F.scal(scale, roots[t]), target[i][j])
                        if F.eq(R, A[i][j]):
                            # verify whole matrix
                            ok = all(F.eq(A[x][y], F.mul(F.scal(scale, roots[t]), target[x][y])) for x in range(d) for y in range(d))
                            return t if ok else None
                    return None
    directions = set()
    def prim_dir(alpha, beta):
        # normalise (alpha, beta) up to units of Z/d
        for u in range(1, d):
            if gcd(u, d) == 1:
                a, b = (u*alpha) % d, (u*beta) % d
                if a == 1 or (a % p == 0 and b == 1):
                    return (a, b)
        raise ValueError
    nbad = 0; nchk = 0
    # identity -> first coordinate a : direction (1,0)
    directions.add((1, 0))
    for s in range(d):
        U = matmul(Fp, Q(s))              # F' Q_s
        Uinv_scaled = matmul(Qs(s), Fps)  # d * U^{-1}
        V = matmul(matmul(Fps, Q(s)), Fp)          # d * V,  V = F'^{-1} Q_s F'
        Vinv = matmul(matmul(Fps, Qs(s)), Fp)      # d * V^{-1}
        for (a, b), W in Wall.items():
            A = matmul(matmul(U, W), Uinv_scaled)  # d * U W U^{-1}
            tgt = Wall[((-(s*a+b)) % d, a % d)]
            t = match(A, d, tgt); nchk += 1
            if t is None:
                nbad += 1; print("  U_s failure", d, s, (a, b))
            if s % p == 0:
                B = matmul(matmul(V, W), Vinv)     # d^2 * V W V^{-1}
                tgt2 = Wall[((a - s*b) % d, b % d)]
                t2 = match(B, d*d, tgt2); nchk += 1
                if t2 is None:
                    nbad += 1; print("  V_s failure", d, s, (a, b))
        directions.add(prim_dir((-s) % d, (-1) % d))   # lambda_s(a,b) = -(s a + b)
        if s % p == 0:
            directions.add(prim_dir(1, (-s) % d))      # lambda'_s(a,b) = a - s b
    expected = p**(k-1)*(p+1)
    print(f"d={d} (p={p},k={k}): {nchk} conjugation identities checked exactly in Z[omega_{N}], failures={nbad}; "
          f"primitive directions realised = {len(directions)} of {expected}")

for a in sys.argv[1:]:
    run(int(a))

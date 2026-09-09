"""Reviewer's check of the side finding: p = 5, general-position 5-set with nullity 2 (refuting nullity <= maxcollinear-1).
(1) Own alternating-minimisation search for nullity 2 on both general-position orbits (author's rep and the parabola).
(2) The parabola {(t,t^2)} has the Clifford/Weyl symmetry Phi(C) = W_(1,1) Q_2 C Q_2^{-1} which permutes its five Weyls
    cyclically; every eigenvector of Phi on span{W_g} has all coefficients nonzero. Check numerically whether one of
    the five eigen-C's has nullity 2 (then an exact certificate in Z[omega_25] follows in part 3 of the review).
"""
import numpy as np, itertools, cmath
p = 5; w = np.exp(2j*np.pi/p)
X = np.roll(np.eye(p), 1, axis=0)        # X|j> = |j+1>
Z = np.diag(w**np.arange(p))
def W(a, b): return np.linalg.matrix_power(X, a % p) @ np.linalg.matrix_power(Z, b % p)

def collinear3(S):
    for A, B, Cc in itertools.combinations(S, 3):
        if ((B[0]-A[0])*(Cc[1]-A[1]) - (B[1]-A[1])*(Cc[0]-A[0])) % p == 0: return True
    return False

def search(S, k, restarts, rng, iters=400):
    Ws = [W(*g) for g in S]; best = (np.inf, None)
    for _ in range(restarts):
        c = rng.normal(size=len(S)) + 1j*rng.normal(size=len(S)); c /= np.linalg.norm(c)
        for _ in range(iters):
            C = sum(ci*Wi for ci, Wi in zip(c, Ws))
            _, _, Vh = np.linalg.svd(C); V = Vh[-k:].conj().T          # p x k
            M = np.stack([(Wi @ V).ravel() for Wi in Ws], axis=1)     # (p k) x l
            _, s, Vh2 = np.linalg.svd(M); c = Vh2[-1].conj()
            c /= np.linalg.norm(c)
        C = sum(ci*Wi for ci, Wi in zip(c, Ws)); sv = np.linalg.svd(C, compute_uv=False)
        if sv[p-k] < best[0]: best = (sv[p-k], c.copy())
    return best

rng = np.random.default_rng(5)
for S in [[(0,0),(1,0),(0,1),(1,1),(2,3)], [(t, t*t % p) for t in range(p)]]:
    assert not collinear3(S)
    val, c = search(S, 2, 40, rng)
    C = sum(ci*W(*g) for ci, g in zip(c, S)); sv = np.linalg.svd(C, compute_uv=False)
    print(f"S={S}: min sigma_4 = {val:.2e}; singular values {np.round(sv,6)}; |c| = {np.round(np.abs(c),4)}")
    print("   phases of c/c0 (in units of 2pi/25):", np.round(np.angle(c/c[0])/(2*np.pi/25), 3))
    print("   |c_i/c_0|:", np.round(np.abs(c/c[0]), 5))

# (2) symmetry of the parabola
S = [(t, t*t % p) for t in range(p)]
inv2 = pow(2, -1, p); s = 2
Q = np.diag(w**((s*inv2*np.arange(p)**2) % p))
Phi = lambda C: W(1, 1) @ Q @ C @ Q.conj().T
Ws = [W(*g) for g in S]
M = np.array([[np.trace(Wh.conj().T @ Phi(Wg))/p for Wg in Ws] for Wh in Ws])   # matrix of Phi in the basis
assert np.allclose(Phi(Ws[0]), sum(M[i,0]*Ws[i] for i in range(p)))
print("\nPhi permutes the parabola Weyls cyclically; nonzero pattern of its matrix:\n", np.round(np.abs(M), 3))
vals, vecs = np.linalg.eig(M)
for lam, v in zip(vals, vecs.T):
    C = sum(v[i]*Ws[i] for i in range(p)); sv = np.linalg.svd(C, compute_uv=False)
    print(f"eigenvalue {lam:.4f} (arg/(2pi/25) = {np.angle(lam)/(2*np.pi/25):.3f}): |c| = {np.round(np.abs(v),4)}, singular values {np.round(sv,6)}")

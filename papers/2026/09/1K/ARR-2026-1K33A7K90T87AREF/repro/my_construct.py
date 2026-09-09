"""Reviewer's own 2x2-block weighted-shift constructor (layers of size 1 or 2, may contain zeros).
Forward pass: exact interval recursion (own derivation). Backward pass: pick sigma_2 in the feasible fibre.
Build R_t by rotating diag(s1,s2) by angle with cos^2 = x solving det(R-D) = tau1*tau2.  Return C, residual, cost."""
from fractions import Fraction as Q
import numpy as np, math

def forward(layers):
    """returns list of (Tr_t, lo_t, hi_t) for t=1..T (state of S_t) or None if infeasible."""
    L0 = layers[0]; T = len(layers) - 1
    Tr = -sum(L0)
    if len(L0) == 1: lo = hi = Q(0)
    else: lo = hi = min(-x for x in L0)
    st = [(Tr, lo, hi)]
    for t in range(1, T + 1):
        L = layers[t]
        if t == T:
            if len(L) == 1:
                ok = (lo <= 0 <= hi) and Tr == L[0]
            else:
                ok = (lo <= min(L) <= hi) and Tr == sum(L)
            return st if ok else None
        if len(L) == 1:
            if not (lo <= 0 <= hi): return None
            Tr = Tr - L[0]
            if Tr < 0: return None
            lo = hi = Q(0); st.append((Tr, lo, hi)); continue
        dl, ds = max(L), min(L)
        dom_lo, dom_hi = max(lo, ds), min(hi, Tr - dl)     # sigma_2 must lie in [ds, Tr-dl] for tau_2 >= 0
        if dom_lo > dom_hi: return None
        u = lambda s: min(Tr - s - dl, s - ds)
        mstar = (Tr - dl + ds) / 2
        nhi = u(min(max(mstar, dom_lo), dom_hi))
        nlo = max(Q(0), dom_lo - dl)
        Tr = Tr - dl - ds; lo, hi = nlo, nhi
        st.append((Tr, lo, hi))
    return st

def build(layers):
    st = forward(layers); assert st is not None
    T = len(layers) - 1
    # backward choice of sigma_2 for S_t, t = T..1
    sig = [None] * (T + 1)
    LT = layers[T]; sig[T] = Q(0) if len(LT) == 1 else min(LT)
    for t in range(T - 1, 0, -1):
        L = layers[t]; Tr, lo, hi = st[t - 1]   # state of S_t
        if len(L) == 1: sig[t] = Q(0); continue
        dl, ds = max(L), min(L); tau = sig[t + 1]
        # need sigma in [lo,hi] with max(0, sigma-dl) <= tau <= min(Tr-sigma-dl, sigma-ds)
        a_ = max(lo, tau + ds, Q(0)); b_ = min(hi, Tr - dl - tau, tau + dl)
        assert a_ <= b_, (t, a_, b_)
        sig[t] = (a_ + b_) / 2
    # matrices
    sizes = [len(L) for L in layers]; off = np.cumsum([0] + sizes); n = off[-1]
    C = np.zeros((n, n))
    S = np.diag([-float(x) for x in layers[0]])
    for t in range(1, T + 1):
        L = layers[t]; Tr, lo, hi = st[t - 1]
        D = np.diag([float(x) for x in L])
        if t == T: R = D.copy()
        elif len(L) == 1: R = np.array([[float(Tr)]])
        else:
            s1, s2 = float(Tr - sig[t]), float(sig[t]); dl, ds = float(max(L)), float(min(L))
            tau2 = float(sig[t + 1]); tau1 = float(Tr - max(L) - min(L)) - tau2
            target = tau1 * tau2
            base = (s2 - dl) * (s1 - ds); slope = (s1 - s2) * (dl - ds)
            x = 0.5 if abs(slope) < 1e-14 else (target - base) / slope
            x = min(1.0, max(0.0, x))
            c, s_ = math.sqrt(x), math.sqrt(1 - x)
            p = int(np.argmax([float(v) for v in L])); q = 1 - p     # eigenvector for s1 has cos in the delta-slot
            U = np.zeros((2, 2)); U[p, 0] = c; U[q, 0] = s_; U[p, 1] = -s_; U[q, 1] = c
            R = U @ np.diag([s1, s2]) @ U.T
        # M with M M^* = 2R, M^* M = 2S  (nonzero spectra must match)
        wR, VR = np.linalg.eigh(R); wS, VS = np.linalg.eigh(S)
        k = min(len(wR), len(wS)); iR = np.argsort(-wR)[:k]; iS = np.argsort(-wS)[:k]
        assert np.allclose(np.sort(wR[iR]), np.sort(wS[iS]), atol=1e-9), (t, wR, wS)
        M = VR[:, iR] @ np.diag(np.sqrt(2 * np.maximum(wR[iR], 0))) @ VS[:, iS].T
        C[off[t]:off[t + 1], off[t - 1]:off[t]] = M
        S = R - D
        assert np.min(np.linalg.eigvalsh(S)) > -1e-9, (t, np.linalg.eigvalsh(S))
    lam = np.array([float(x) for L in layers for x in L])
    resid = np.linalg.norm(C @ C.T - C.T @ C - 2 * np.diag(lam))
    return C, resid, 0.5 * np.sum(C * C)

if __name__ == "__main__":
    # counterexample to Theorem C for z >= 1: m=3, z=1, G_3 chamber, layering with the zero inside a layer
    b1, b2 = Q(3), Q(5, 2); a = [Q(2), Q(2), Q(3, 2)]
    for lay in ([[-b2], [-b1, a[0]], [a[1], Q(0)], [a[2]]], [[-b2], [-b1, a[0]], [a[1]], [a[2]], [Q(0)]]):
        C, resid, cost = build(lay)
        sv = np.linalg.svd(C, compute_uv=False)
        print("layering", lay, "\n  resid=%.2e cost=%.6f rank=%d  common spectrum s=%s" % (resid, cost, np.linalg.matrix_rank(C, tol=1e-9), np.round(sv**2 / 2, 4)))
    np.set_printoptions(precision=4, suppress=True, linewidth=150)
    C, resid, cost = build([[-b2], [-b1, a[0]], [a[1], Q(0)], [a[2]]])
    print("C (real, basis ordered -b2, -b1, a1, a2, 0, a3):\n", C)

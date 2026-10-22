"""Version-2 numerical sanity checks (floating point / mpmath; NOT proofs).
Run:  python check_v2.py   (prints a JSON summary, also writes check_v2_output.json
next to the script unless it already exists)."""
import json, sys
from pathlib import Path
import numpy as np
import mpmath as mp
mp.mp.dps = 40
out = {}

def setup(c):
    c = mp.mpf(c); s = mp.sqrt(1+c*c); eta = (c+1j)/s
    M = lambda z: c*c-1+2j*c*(1+eta*z)/(1-eta*z)
    def f(z):            # analytic root with values in the first quadrant
        m = M(z)
        if abs(m.imag) < mp.mpf(10)**(-30):      # boundary: Im M = 0, choose the first-quadrant root
            return mp.sqrt(m.real) if m.real > 0 else 1j*mp.sqrt(-m.real)
        return mp.sqrt(m)               # principal root: arg in (0,pi/2) since Im M>0
    q = lambda z: 1-c**4 + s**3/2*((c-1j)*z+(c+1j)/z)
    a0, b0 = c**3, s**3
    h = lambda z: 1j*a0-1j*b0/2*(z+1/z)+1j*q(z)/f(z)
    return c, s, eta, M, f, q, h, a0, b0

# A. Lemma 3 --------------------------------------------------------------
A = []
for cval in ['0.125', '0.5', '1', '2.5', '8']:
    c, s, eta, M, f, q, h, a0, b0 = setup(cval)
    row = {'c': cval}
    # h(0)=1 : evaluate at tiny z
    row['h(1e-15)-1'] = float(abs(h(mp.mpf('1e-15'))-1))
    # f(0)=c+i, f'(0)=2ic/s
    row['f0_err'] = float(abs(f(mp.mpf('1e-30'))-(c+1j)))
    # Re h >= 0 on a polar grid of the closed disc (excluding r=0), plus boundary
    minre = mp.inf
    for r in [0.02, 0.2, 0.5, 0.8, 0.95, 0.999, 0.999999, 1.0]:
        for k in range(720):
            z = mp.mpf(r)*mp.e**(1j*mp.pi*(k+0.37)/360)
            if abs(z) == 1 and (abs(z-eta**3) < 1e-12 or abs(z-eta.conjugate()) < 1e-12):
                continue
            minre = min(minre, h(z).real)
    row['min_Re_h_on_grid'] = float(minre)
    # boundary: w>=0, complementarity
    minw = mp.inf; maxcomp = 0
    for k in range(2000):
        phi = 2*mp.pi*(k+0.4)/2000; z = mp.e**(1j*phi)
        hv = h(z); w = a0-b0*mp.cos(phi)-hv.imag
        minw = min(minw, w); maxcomp = max(maxcomp, abs(hv.real*w))
    row['min_w_boundary'] = float(minw); row['max_u_times_w'] = float(maxcomp)
    # algebraic identity (qfactor) at random interior points
    z = mp.mpf('0.31')+0.4j
    row['qfactor_err'] = float(abs(q(z)+s**2/2*M(z)*(1-eta*z)*(1-eta.conjugate()/z)))
    # order of vanishing of q/f at the exceptional points (radial approach)
    def slope(z0, direction):
        e1, e2 = mp.mpf('1e-8'), mp.mpf('1e-10')
        def g(e):
            z = z0*(1-e*direction)
            return abs(q(z)/f(z))
        return float(mp.log(g(e1)/g(e2))/mp.log(e1/e2))
    row['order_at_zero_of_M (expect 0.5)'] = slope(eta**3, 1)
    row['order_at_pole_of_M (expect 1.5)'] = slope(eta.conjugate(), 1)
    A.append(row)
out['lemma3'] = A

# B. Corollary 6, independent Cartesian evaluation ---------------------------
def quantile_alphas(a, b, sigma, N, Ngrid=1<<17):
    """quantile nodes of the critical measure for (|b|), a0=(b^{2/3}-1)_+^{3/2}"""
    phi = 2*np.pi*(np.arange(Ngrid)+.5)/Ngrid; z = np.exp(1j*phi)
    if b > 1:
        cc = np.sqrt(b**(2/3)-1); ss = np.sqrt(1+cc*cc); ee = (cc+1j)/ss
        mm = cc*cc-1+2j*cc*(1+ee*z)/(1-ee*z)
        ff = np.sqrt(np.maximum(mm.real, 0))+1j*np.sqrt(np.maximum(-mm.real, 0))
        qq = 1-cc**4+ss**3*np.real((cc-1j)*z)
        hh = 1j*cc**3-1j*ss**3/2*(z+1/z)+1j*qq/ff
        dens = np.maximum(hh.real, 0)
    else:
        dens = 1+b*np.sin(phi)           # Re(1 - i b e^{it}) = 1 + b sin t
    cdf = np.cumsum(dens); cdf /= cdf[-1]
    ix = np.searchsorted(cdf, (np.arange(N)+.5)/N)
    return sigma*np.exp(-1j*phi[ix])

def check_cor6(k, a, b, omega, sigma, N):
    al = quantile_alphas(a/abs(omega), abs(b)/abs(omega), sigma, N)
    if b < 0: al = al*np.exp(1j*np.pi)        # rotation by pi/(2k): cos(2k th)->-cos
    if omega < 0: al = np.conj(al)            # reflection th->-th
    th = np.linspace(0, 2*np.pi, 20001)
    x, y = np.cos(th), np.sin(th)
    zc = x+1j*y
    # f(x,y) from the Cartesian formula in the manuscript
    pre = -a+b*np.real(zc**(2*k))
    f1 = pre*x - omega*y; f2 = pre*y + omega*x       # r=1 on the circle
    # Q_j = (1+|al|^2)(x^2+y^2)^k - 2 Re[al (x+iy)^{2k}] ; grad on r=1 :
    # d/dx (x^2+y^2)^k = 2k x ; d/dx Re[al z^{2k}] = Re[al 2k z^{2k-1}], d/dy -> Re[al 2k z^{2k-1} i]
    w = zc**(2*k)
    LQ = np.zeros_like(th)
    A_ = al[:, None]
    Q = (1+abs(A_)**2) - 2*np.real(A_*w[None, :])
    dQx = (1+abs(A_)**2)*2*k*x[None, :] - 2*np.real(A_*2*k*zc[None, :]**(2*k-1))
    dQy = (1+abs(A_)**2)*2*k*y[None, :] - 2*np.real(A_*2*k*zc[None, :]**(2*k-1)*1j)
    # P = prod_j Q_j (already homogeneous of degree 2kN), so L_f P / P = sum_j (grad Q_j . f)/Q_j
    LP_over_P = np.sum((dQx*f1[None, :]+dQy*f2[None, :])/Q, axis=0)
    return dict(k=k, a=a, b=b, omega=omega, sigma=sigma, N=N, degree=2*k*N,
                max_LfP_over_P_on_circle=float(LP_over_P.max()),
                normalized_max=float(LP_over_P.max()/(2*k*N)))
B = []
for (k, a, b, om) in [(1, 1.2, 2.0, 1.0), (2, 1.2, -2.0, -1.0), (3, 2.4, 4.0, 2.0), (2, 0.6, 0.8, 1.0), (2, 0.5, 0.0, 1.0)]:
    B.append(check_cor6(k, a, b, om, 0.98, 1024))
out['cor6_cartesian_products'] = B

# C. Pairing identities for k=2 (F+HG=c, <G cos k phi> = sigma c/s) -----------
C = []
for k in (1, 2, 3):
    c = 1.3; s = np.sqrt(1+c*c); sig = 0.9
    c_, s_, eta, M, f, q, h, a0, b0 = setup(c)
    n = 4096; phi = 2*np.pi*np.arange(n)/n
    vals = np.array([complex(f(sig*mp.e**(1j*k*p))) for p in phi])
    F, G = vals.real, vals.imag
    Hs = lambda v: np.real(np.fft.ifft(-1j*np.sign(np.fft.fftfreq(n, 1/n))*np.fft.fft(v)))  # H cos=sin
    C.append(dict(k=k, meanF=F.mean(), meanG=G.mean(), Gcos=float(np.mean(G*np.cos(k*phi))), expected=sig*c/s,
                  max_F_plus_HG_minus_c=float(np.max(abs(F+Hs(G)-c))), minF=F.min(), minG=G.min()))
out['pairing_identities'] = C
txt = json.dumps(out, indent=1, default=float)
print(txt)
p = Path(__file__).resolve().parent/'check_v2_output.json'
if not p.exists(): p.write_text(txt+'\n', encoding='utf-8')

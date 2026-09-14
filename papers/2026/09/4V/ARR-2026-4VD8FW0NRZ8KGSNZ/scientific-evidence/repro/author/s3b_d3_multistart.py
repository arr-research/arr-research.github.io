# s3b: quick multi-start Nelder-Mead/Powell on the exact N=5 parametrisation of s3 (independent of the DE runs).
import numpy as np, time, json, sys
from scipy.optimize import minimize
from s3_d3_N5_global import gamma, bloch, spectrum
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 11)
t0 = time.time(); results = []
for trial in range(int(sys.argv[2]) if len(sys.argv) > 2 else 40):
    p0 = np.array([rng.uniform(0, np.pi), rng.uniform(0, 2*np.pi), rng.uniform(0, np.pi), rng.uniform(0, 2*np.pi), rng.uniform(0, np.pi), rng.uniform(0, 2*np.pi), rng.uniform(0, 2*np.pi)])
    if gamma(p0) > 100: continue
    p = p0
    for it in range(3):
        p = minimize(gamma, p, method='Nelder-Mead', options={'maxiter': 20000, 'xatol': 1e-12, 'fatol': 1e-14, 'adaptive': True}).x
        p = minimize(gamma, p, method='Powell', options={'maxiter': 20000, 'xtol': 1e-12, 'ftol': 1e-14}).x
    results.append((-gamma(p), p))
    gs_ = spectrum(bloch(p), 400); act_ = sorted(int(k) for k in (np.argsort(gs_[2:])[:6] + 2) if gs_[k] - gs_[2:].min() < 1e-7)
    print(f"start {trial}: gamma = {-gamma(p):.10f} active = {act_}", flush=True)
results.sort(key=lambda r: -r[0])
print(f"{len(results)} feasible starts, {time.time()-t0:.0f}s; top values:", [round(r[0], 8) for r in results[:10]])
g, p = results[0]; n = bloch(p); gs = spectrum(n, 2000); order = np.argsort(gs[2:])[:8] + 2
np.set_printoptions(precision=8, suppress=True, linewidth=150)
print("best gamma =", repr(g), " active:", [(int(k), round(float(gs[k]), 10)) for k in order])
print("Gram:\n", n @ n.T); print("n:\n", n)
json.dump({'gamma': g, 'p': p.tolist(), 'n': n.tolist()}, open('s3b_best.json', 'w'), indent=1)

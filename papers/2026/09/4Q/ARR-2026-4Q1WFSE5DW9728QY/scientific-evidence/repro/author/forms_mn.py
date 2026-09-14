"""Experiment 2: exposed forms of kappa_d on the (m,n,z) stratum from hive-LP duals; classification of their level
layerings (ordered a's? full capacity? b-schedule, b-inversions, max layer size); validity (joint LP) and exposedness
(radius LP) of every integer form found; coverage check (max of the found forms = kappa at fresh points).
Usage: python forms_mn.py m n z N [seed]   -> forms_m{m}_n{n}_z{z}.json"""
import sys, json, time, numpy as np
from fractions import Fraction as Q
from mn_tools import *
from joint_lp import JointLP, radius

if __name__ == "__main__":
    m, n, z, N = [int(x) for x in sys.argv[1:5]]; seed = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    d = m + n + z; M = HiveLP(d); rng = np.random.default_rng(seed + 1000 * m + 100 * n + z); t0 = time.time()
    found = {}; bad = 0
    for i in range(N):
        a, b = rand_ab(m, n, rng, LAWS[i % len(LAWS)]); lam = spec(a, b, z); r = M.solve(lam)
        if r is None: bad += 1; continue
        f = canon(r['grad'], m, n, z)
        key = tuple(rat(x, 2000) for x in f)
        if any(k.denominator != 1 for k in key): bad += 1; continue
        key = tuple(int(k) for k in key)
        if abs(form_val(np.array(key, float), a, b) - r['val']) > 1e-7: bad += 1; continue
        found[key] = found.get(key, 0) + 1
    forms = sorted(found)
    # validity and exposedness
    J = JointLP(m, n, z); valid = {}; expo = {}
    for f in forms:
        v, _ = J.validity(f); valid[f] = v
    good = [f for f in forms if valid[f] is not None and valid[f] >= -1e-9]
    for f in good:
        rr, _ = radius(f, [g for g in good if g != f], m, n); expo[f] = rr
    exposed = [f for f in good if expo[f] is not None and expo[f] > 1e-9]
    # coverage at fresh points
    rng2 = np.random.default_rng(777 + m * 10 + n); err = 0.0; missing = 0
    for i in range(300):
        a, b = rand_ab(m, n, rng2, LAWS[i % len(LAWS)]); lam = spec(a, b, z); r = M.solve(lam)
        v = max(form_val(np.array(f, float), a, b) for f in exposed)
        if r['val'] - v > 1e-7: missing += 1
        err = max(err, abs(v - r['val']))
    # classification
    OF = ordered_forms(m, n)
    cls = {}
    for f in exposed:
        L = level_layering(f, m, n); c = classify_layering(L, m, n); c['layering'] = show(L); c['count'] = found[f]
        c['is_ordered_form'] = f in OF
        cls[f] = c
    nO = sum(1 for f in exposed if cls[f]['is_ordered_form'])
    nord = sum(1 for f in exposed if cls[f]['ordered'])
    nfull = sum(1 for f in exposed if cls[f]['ordered'] and cls[f]['full'])
    maxsize = max(cls[f]['maxsize'] for f in exposed)
    size_hist = {}
    for f in exposed: size_hist[cls[f]['maxsize']] = size_hist.get(cls[f]['maxsize'], 0) + 1
    binv_hist = {}
    for f in exposed: binv_hist[cls[f]['binv']] = binv_hist.get(cls[f]['binv'], 0) + 1
    lastb = sum(1 for f in exposed if cls[f]['last_has_b']); l0 = sum(1 for f in exposed if not cls[f]['layer0_pure_b'])
    print(f"(m,n,z)=({m},{n},{z}) d={d}: {N} samples ({bad} discarded), {len(forms)} integer forms, {len(good)} valid, "
          f"{len(exposed)} exposed; fresh-point check: max|maxforms-kappa|={err:.1e}, points with kappa>max forms: {missing}; "
          f"ordered full-capacity (Theorem 1 class): {nO}; level layering with a's in order: {nord} (of which full: {nfull}); "
          f"max layer size {maxsize}, histogram {dict(sorted(size_hist.items()))}; b-inversion histogram {dict(sorted(binv_hist.items()))}; "
          f"last layer has a b: {lastb}; layer 0 not pure-b: {l0}; {time.time()-t0:.0f}s", flush=True)
    out = {str(list(f)): dict(validity=valid[f], radius=expo[f], **cls[f]) for f in exposed}
    out['_summary'] = dict(m=m, n=n, z=z, N=N, n_forms=len(forms), n_valid=len(good), n_exposed=len(exposed), err=err, missing=missing,
                           n_ordered_forms=nO, n_ordered_level=nord, n_full=nfull, maxsize=maxsize, size_hist=size_hist, binv_hist=binv_hist)
    json.dump(out, open(f"forms_m{m}_n{n}_z{z}.json", "w"), indent=1)
    for f in sorted(exposed, key=lambda f: -found[f]):
        c = cls[f]
        print(f"   {list(f)} n={found[f]} rad={expo[f]:.3f} {'ORD' if c['is_ordered_form'] else ('ord-a' if c['ordered'] else '   ')} sched={c['sched']} binv={c['binv']} sizes={c['sizes']}  {c['layering']}")

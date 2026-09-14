"""Task (a): independent verification of tiling certificates from certs_m{m}_z{z}.json.
For each sampled form: (i) every tile (I,J,K) satisfies the sum condition, own LR >= 1, own T^d_r membership (d<=9),
its s-form is +s[U]-s[N], its rhs is sum_{k in K} lambda_k; (ii) tiles sum exactly (integers, mod sum a = sum b) to the form;
(iii) each s_t (t<d) has total coefficient <= 1; (iv) dimension-free instantiation of each tile at z' in {0,1,3} (d'<=9):
search for a Horn triple in dimension d' with the same signature (Ka, Kb, U, Noff) -- K' = Ka + (subset of zeros) + b-indices,
I = U + W (+ d'), J = {d'+1-t : t in W + N'} (+ 1) -- with own LR >= 1 (and own T membership when d'<=9)."""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, itertools, random, time
sys.path.insert(0, AUTHOR_DIR)
from horn_own import T, lr_own, part
W = AUTHOR_DIR
random.seed(2026)
Tsets = {}
def inT(I, J, K, d):
    r = len(I)
    if (r, d) not in Tsets: Tsets[(r, d)] = set(T(r, d))
    return (tuple(I), tuple(J), tuple(K)) in Tsets[(r, d)]

def rhs_vec(K, m, z, d):
    v = [0] * (m + 3)
    for k in K:
        if k <= m: v[k - 1] += 1
        elif k > m + z: v[m + (d - k)] -= 1
    return v
def canon(v, m):
    t = -v[m + 2]; return tuple(x - t for x in v[:m]) + (v[m] + t, v[m + 1] + t)
def s_form(I, J, d):
    c = [0] * (d + 1)
    for i in I:
        if i < d: c[i] += 1
    for j in J:
        if j > 1: c[d + 1 - j] -= 1
    return c

def instantiate(Ka, Kb, U, Noff, m, zp):
    """Search for a valid Horn triple realising the tile in dimension d' = m+zp+3. Returns (I,J,K) or None."""
    d = m + zp + 3; zeros = list(range(m + 1, m + zp + 1)); bidx = {1: d, 2: d - 1, 3: d - 2}
    N = tuple(sorted(d - o for o in Noff)); U = tuple(U)
    if any(n <= 0 or n >= d for n in N) or any(u <= 0 or u >= d for u in U) or set(U) & set(N): return None
    for nz in range(len(zeros), -1, -1):
        for Z in itertools.combinations(zeros, nz):
            K = tuple(sorted(list(Ka) + list(Z) + [bidx[i] for i in Kb])); r = len(K)
            if len(set(K)) < r: continue
            for use_d in (False, True):
                for use_1 in (False, True):
                    nW = r - len(U) - use_d
                    if nW < 0 or nW + len(N) + use_1 != r: continue
                    pool = [t for t in range(1, d) if t not in U and t not in N]
                    for Wc in itertools.combinations(pool, nW):
                        I = tuple(sorted(U + Wc + ((d,) if use_d else ())))
                        J = tuple(sorted(((1,) if use_1 else ()) + tuple(d + 1 - t for t in Wc + N)))
                        if len(set(J)) < r or len(set(I)) < r: continue
                        if sum(I) + sum(J) != sum(K) + r * (r + 1) // 2: continue
                        if lr_own(part(I), part(J), part(K)) >= 1:
                            if d <= 9: assert inT(I, J, K, d)
                            return (I, J, K)
    return None

if __name__ == "__main__":
    files = [(m, z) for m in range(3, 10) for z in range(0, 4) if m + z + 3 <= 12 and (m, z) != (9, 1)]
    files = [(m, z) for (m, z) in files if f"certs_m{m}_z{z}.json" in __import__('os').listdir(W)]
    sample = []
    for m, z in files:
        C = json.load(open(f"{W}/certs_m{m}_z{z}.json"))
        forms = list(C.keys())
        k = 2 if m + z + 3 <= 9 else 1
        for g in random.sample(forms, min(k, len(forms))): sample.append((m, z, g, C[g]))
    # always include the z=0-only forms and a few at largest d
    for m, z, g in [(4, 0, "[1, 2, 3, 4, -2, -1]"), (5, 0, "[1, 2, 3, 3, 4, -2, -1]"), (7, 0, "[1, 2, 2, 3, 3, 4, 5, -2, -1]"), (8, 0, "[1, 2, 2, 3, 3, 4, 4, 5, -2, -1]")]:
        C = json.load(open(f"{W}/certs_m{m}_z{z}.json")); sample.append((m, z, g, C[g]))
    print(f"{len(sample)} certificates sampled from {len(files)} files")
    nok = 0; ntiles = 0; dimfree = {0: [0, 0], 1: [0, 0], 3: [0, 0]}; fails = []
    t0 = time.time()
    for m, z, g, cert in sample:
        d = m + z + 3; form = tuple(json.loads(g)); tot = [0] * (m + 3); sc = [0] * (d + 1); ok = True; msgs = []
        for t in cert['tiles']:
            I, J, K = tuple(t['I']), tuple(t['J']), tuple(t['K']); r = len(I); ntiles += 1
            if not (len(J) == r == len(K)) or sum(I) + sum(J) != sum(K) + r * (r + 1) // 2: ok = False; msgs.append(f"sum condition {I,J,K}")
            c = lr_own(part(I), part(J), part(K))
            if c < 1: ok = False; msgs.append(f"LR={c} for {I,J,K}")
            if d <= 9 and not inT(I, J, K, d): ok = False; msgs.append(f"not in T^{d}: {I,J,K}")
            sf = s_form(I, J, d); exp = [0] * (d + 1)
            for u in t['U']: exp[u] += 1
            for n in t['N']: exp[n] -= 1
            if sf != exp: ok = False; msgs.append(f"s-form mismatch {I,J} vs U={t['U']} N={t['N']}")
            sc = [x + y for x, y in zip(sc, sf)]
            tot = [x + y for x, y in zip(tot, rhs_vec(K, m, z, d))]
            # dimension-free instantiation
            Ka = tuple(t['Ka']); Kb = tuple(t['Kb']); Noff = tuple(t['Noff'])
            assert Ka == tuple(k for k in K if k <= m) and tuple(d - n for n in t['N']) == Noff
            for zp in (0, 1, 3):
                if m + zp + 3 > 9: continue
                res = instantiate(Ka, Kb, t['U'], Noff, m, zp)
                dimfree[zp][0] += 1
                if res is not None: dimfree[zp][1] += 1
                else: fails.append((m, z, form, (Ka, Kb, tuple(t['U']), Noff), zp))
        if canon(tot, m) != form: ok = False; msgs.append(f"tile sum {canon(tot, m)} != form {form}")
        if any(sc[t] > 1 for t in range(1, d)): ok = False; msgs.append(f"s-coefficient > 1: {sc}")
        if ok: nok += 1
        else: print(f"  FAIL m={m} z={z} form {form}: {msgs}")
    print(f"certificates fully verified: {nok}/{len(sample)} ({ntiles} tiles)  ({time.time()-t0:.0f}s)")
    for zp in (0, 1, 3): print(f"dimension-free instantiation at z'={zp}: {dimfree[zp][1]}/{dimfree[zp][0]} tiles realisable (d'<=9 only)")
    for f in fails: print("  not realisable:", f)

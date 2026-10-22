# Independent, deliberately naive verifier (no SAT, no shared code with the solvers).
# Reads g37/witnesses37.json ({"k":..,"N":..,"A":[..]} list) and g27/witnesses27.json ({"p":..,"A":[..]}).
import json, sys
def ok37(A, N, k):
    A = sorted(set(A))
    for d in range(1, N+1):
        found = False
        for a in A:
            good = True
            for j in range(k):
                if (a + j*d) not in A: good = False; break
            if good: found = True; break
        if not found: return False
    return True
def ok27(A, p):
    A = sorted(set(x % p for x in A))
    if len(A) < 2: return False
    reps = {}
    for i in range(len(A)):
        for j in range(i, len(A)):
            s = (A[i] + A[j]) % p
            reps.setdefault(s, []).append((A[i], A[j]))
    return all(len(v) >= 2 for v in reps.values())
bad = 0
for r in json.load(open('g37/witnesses37.json')):
    v = ok37(r['A'], r['N'], r['k']); bad += (not v)
    print('g37', r['k'], r['N'], len(set(r['A'])), r.get('tag',''), 'OK' if v else 'FAIL')
for r in json.load(open('g27/witnesses27.json')):
    v = ok27(r['A'], r['p']); bad += (not v)
    print('g27', r['p'], len(set(r['A'])), 'OK' if v else 'FAIL')
print('failures:', bad); sys.exit(1 if bad else 0)

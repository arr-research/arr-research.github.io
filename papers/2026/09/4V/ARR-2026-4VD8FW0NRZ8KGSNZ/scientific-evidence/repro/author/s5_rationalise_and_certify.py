# s5: take a numerical optimum (5 Bloch vectors, json from s3/s3b), build a nearby EXACT frame:
#   n1,n2,n3 -> rational unit vectors via stereographic rational points  n = (2a, 2b, 1-a^2-b^2)/(1+a^2+b^2),
#   w -> rational vector orthogonal to s = n1+n2+n3 (rationalised numerical v, projected onto s^perp),
#   n4,5 = -s/2 +- sqrt(q) w,  q = (1-|s|^2/4)/|w|^2.   Then certify with s4 (exact arithmetic in Q(sqrt q)).
import numpy as np, json, sys
from fractions import Fraction as Fr
from s4int_d3_exact_certificate import certify_int as certify

def stereo_rational(v, den):
    x, y, z = v
    if z < 0:  # project from the other pole for stability: flip sign convention
        a = Fr(round(den * x / (1 - z)), den); b = Fr(round(den * y / (1 - z)), den)
        r2 = a * a + b * b
        return [2 * a / (1 + r2), 2 * b / (1 + r2), -(1 - r2) / (1 + r2)]
    a = Fr(round(den * x / (1 + z)), den); b = Fr(round(den * y / (1 + z)), den)
    r2 = a * a + b * b
    return [2 * a / (1 + r2), 2 * b / (1 + r2), (1 - r2) / (1 + r2)]

def build_spec(n, den=10 ** 6, wden=10 ** 6):
    n = np.asarray(n, float)
    # choose which three vectors are "free": any three; take the ordering given
    n123 = [stereo_rational(n[i], den) for i in range(3)]
    s = [sum(v[c] for v in n123) for c in range(3)]
    v_num = n[3] + np.array([float(c) for c in s]) / 2          # numerical v
    wr = [Fr(round(wden * c), wden) for c in v_num]
    ws = sum(a * b for a, b in zip(wr, s)); ss = sum(a * a for a in s)
    w = [wr[c] - ws * s[c] / ss for c in range(3)]                # exact projection onto s^perp
    return {'n123': [[str(c) for c in v] for v in n123], 'w': [str(c) for c in w]}

if __name__ == "__main__":
    src = sys.argv[1]; K0 = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    den = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 6
    n = json.load(open(src))['n']
    spec = build_spec(n, den, den); spec['K0'] = K0
    out = src.replace('.json', f'_exact_den{den}.json'); json.dump(spec, open(out, 'w'), indent=1)
    print("exact spec written to", out)
    cert, kmin, lower = certify(spec['n123'], spec['w'], K0=K0)
    print("certified rational lower bound:", cert, "=", float(cert))

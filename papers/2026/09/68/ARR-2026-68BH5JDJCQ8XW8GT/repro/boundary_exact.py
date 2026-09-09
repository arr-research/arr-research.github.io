# The 66 boundary comparisons of Theorem 6.1 as explicit exact rationals: for 3 <= d <= 35 and m in {2d, 2d+1}
# (i.e. n = m-1 in {2d-1, 2d}) prints q_m = W_{m-1}/u_m, g_m = d m (m+2d)/((d-1)(2d+2-m)), and chat_{d,m} from (3.3).
# Writes boundary_exact.txt. Pure integer/rational arithmetic (math.comb, fractions.Fraction).
from fractions import Fraction as Fr
from math import comb
import pathlib
lines=["# d m n=m-1 | q_m (exact) | g_m (exact) | chat_{d,m} (exact) | sign chat_{d,m} = sign c_{d,n}"]
pattern_ok=True
for d in range(3,36):
    for m in (2*d,2*d+1):
        T=2*d-2+m; u=comb(T-1,d-2); W=sum(comb(T-1,k) for k in range(d-1,d-1+m))
        q=Fr(W,u); g=Fr(d*m*(m+2*d),(d-1)*(2*d+2-m))
        chat=(m-2*d-2)*W+Fr(d,d-1)*m*(m+2*d)*u
        sgn='+' if chat>0 else '-' if chat<0 else '0'
        expected='+' if (d in (3,4) and m==2*d+1) else '-'
        pattern_ok&=(sgn==expected)
        assert (q>g)==(chat<0)
        lines.append(f"{d} {m} {m-1} | {q} | {g} | {chat} | {sgn}")
assert pattern_ok, "boundary sign mismatch"
pathlib.Path(__file__).with_name("boundary_exact.txt").write_text("\n".join(lines)+"\n")
print("boundary comparisons:",2*33,"; sign pattern of Theorem 6.1 at the boundary indices:",pattern_ok)
print("wrote boundary_exact.txt")

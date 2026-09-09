# (i) verify exact recursion q_{n+1} = 2(d+n)(q_n+1)/(2d-2+n), q_n = W_{n-1}/u_n
# (ii) cases n=2d, 2d+1: q_n > g_n = d n (n+2d)/((d-1)(2d+2-n)) via central-term bound and exact integers
from fractions import Fraction as Fr
from math import comb, floor
def q(d,n):
    T1=2*d-3+n
    return Fr(sum(comb(T1,k) for k in range(d-1,d-2+n+1)),comb(T1,d-2))
def g(d,n): return Fr(d*n*(n+2*d),(d-1)*(2*d+2-n))
ok=True
for d in range(3,30):
    for n in range(3,2*d+2):
        if q(d,n+1)!=2*(d+n)*(q(d,n)+1)/(2*d-2+n): ok=False
assert ok, "recursion mismatch"
print("recursion exact:",ok)
print("d | q_2d>g_2d | q_2d+1>g_2d+1 | central-term bound n=2d+1: C(4d-2,2d-1)/C(4d-2,d-2) > g_2d+1 | (5/3)^(floor(d/2)+1) > g_2d+1 | (5/3)^(floor(d/2)+1) > 9d^2")
for d in range(3,61):
    c1=q(d,2*d)>g(d,2*d); c2=q(d,2*d+1)>g(d,2*d+1)
    assert c1 and c2==(d>=5), (d,c1,c2)
    P=Fr(comb(4*d-2,2*d-1),comb(4*d-2,d-2)); P2=Fr(comb(4*d-3,2*d-2),comb(4*d-3,d-2))
    crude=Fr(5,3)**(d//2+1)
    print(d, c1, c2, P>g(d,2*d+1), P2>g(d,2*d), crude>g(d,2*d+1), crude>9*d*d, " sign chat_{2d+1}:", '+' if (2*d+1-2*d-2)*sum(comb(4*d-2,k) for k in range(d-1,3*d))+Fr(d,d-1)*(2*d+1)*(4*d+1)*comb(4*d-2,d-2)>0 else '-')

"""Symbolic identification of the twelve d=5 terms of ARR-2026-37B8R0QTA894GTFF (eq. (8), spectral version of the
gap forms q_1..q_6 and their reversals) on the (3,2) stratum lambda=(a1,a2,a3,-b2,-b1), b1 = a1+a2+a3-b2.
Prints each term as (form) + (nonpositive correction) with form in {F0,F1,F2,G1,G3}."""
import sympy as sp
a1,a2,a3,b2 = sp.symbols('a1 a2 a3 b2', positive=True); b1 = a1+a2+a3-b2
l = [a1,a2,a3,-b2,-b1]; g = [l[i]-l[i+1] for i in range(4)]
Q = {'q1':(2,0,-1,-1),'q2':(6,7,3,-1),'q3':(2,9,1,-2),'q4':(8,6,-1,-3),'q5':(4,8,2,1),'q6':(4,3,7,1)}
den = {'q1':1,'q2':5,'q3':5,'q4':5,'q5':5,'q6':5}
F0 = a1+a2+2*a3; F1 = b1+a2+a3; F2 = b1+(a2+a3-b2)+a3; G1 = b2+a1+a3; G3 = b2+a2+2*a3+a3
forms = {'F0':F0,'F1':F1,'F2':F2,'G1':G1,'G3':G3}
for name,q in Q.items():
    for rev in (False,True):
        qq = q[::-1] if rev else q
        term = sp.expand(sum(sp.Rational(qq[i],den[name])*g[i] for i in range(4)))
        best = None
        for fn,f in forms.items():
            diff = sp.expand(term - f)
            # accept if diff is a nonpositive combination of a's and b2 (coefficients <= 0)
            coeffs = sp.Poly(diff, a1,a2,a3,b2).coeffs() if diff != 0 else []
            if all(c <= 0 for c in coeffs):
                best = (fn, diff); break
        print(('rho ' if rev else '    ')+name, '=', term, '  ->', best)

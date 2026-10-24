"""Symbolic exploration of a possible exact canonical four-erasure condition law."""
import sympy as s,json
from pathlib import Path
root=Path(__file__).resolve().parent
x,Lam=s.symbols('x Lam',real=True)
a,b,c,e=s.symbols('a b c e',real=True)
v=s.Matrix([a,b,c,e]);K=a*a+a*b+b*b+c*c+c*e+e*e
length=a+b+c+e;z=x-1
# Traceless rank-r/r dual energy, n scaled to1; theta minimizes the shift.
results={}
for name,u,w in [('same',a,b),('cross',a,e)]:
    W=x*length**2/2-z*length*(u+w)+z*(u*u+w*w)-z*z*(w-u)**2/(2*x)
    N=s.simplify(s.hessian(W,v)/2)
    D=s.hessian(2*K,v)/2
    det=s.factor((N-Lam*D).det())
    results[name]={'pencil_determinant':str(det),'N':str(N),'D':str(D)}
    print(name,det)
    # Reflection exchanges the two extreme cells, preserving each branch.
    P=s.Matrix([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
    print('reflection commutes',s.simplify(P*N*P-N)==s.zeros(4))
    if s.simplify(P*N*P-N)==s.zeros(4):
        S=s.Matrix([[1,0],[0,1],[0,1],[1,0]])
        A=s.Matrix([[1,0],[0,1],[0,-1],[-1,0]])
        for block,Q in [('sym',S),('antisym',A)]:
            piece=s.factor((Q.T*(N-Lam*D)*Q).det())
            results[name][block]=str(piece)
            print(block,piece)
(root/'capacity239-condition-pencil.json').write_text(json.dumps(results,indent=2),encoding='utf-8')

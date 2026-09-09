# Symbolic verification of the ODE reduction and the transversality algebra.
import sympy as sp
k,d,M,Mp,Mpp,b=sp.symbols('kappa d M Mp Mpp b',positive=True)
# ODE for M=1F1(1;d;kappa): kappa M' = (kappa-d+1) M + (d-1);  Kummer: kappa M'' + (d-kappa) M' - M = 0
Mp_expr=((k-d+1)*M+(d-1))/k
Mpp_expr=(M-(d-k)*Mp)/k
N=M*Mp-k*M*Mpp+k*Mp**2-M**2/d
N=N.subs(Mpp,Mpp_expr).subs(Mp,Mp_expr)
Ntilde=k*M*(M+d)-d*(M-1)*(2*M+d-1)
print("N == (d-1)/d * Ntilde/kappa :", sp.simplify(N-(d-1)/d*Ntilde/k)==0)
# check Kummer eq consistent with first-order ODE (differentiate first-order ODE)
lhs=sp.diff(k*sp.Function('M')(k),k)
# b = 1 - d(M-1)/(kappa M) ; check b = (d m -1)/(d-1) with m = Mp/M
m=Mp_expr/M
print("b identity:", sp.simplify((d*m-1)/(d-1)-(1-d*(M-1)/(k*M)))==0)
# Lambda = (2b-1)M + (d-1)b + 1 vs Ntilde/(kappa M)
bexpr=1-d*(M-1)/(k*M)
print("Lambda*kappa*M == Ntilde :", sp.simplify(((2*bexpr-1)*M+(d-1)*bexpr+1)*k*M-Ntilde)==0)
# Psi(M): Ntilde>0 <=> kappa > Psi(M)
Psi=d*(M-1)*(2*M+d-1)/(M*(M+d))
print("Ntilde == M(M+d)(kappa-Psi):", sp.simplify(Ntilde-M*(M+d)*(k-Psi))==0)
# trajectory slope F(M,kappa)=dkappa/dM = 1/M' = kappa/((kappa-d+1)M+d-1)
F=k/((k-d+1)*M+(d-1))
Fon=sp.simplify(F.subs(k,Psi))
print("F on curve:", sp.factor(Fon))
Delta=sp.simplify(Fon-sp.diff(Psi,M))
print("Delta factor:", sp.factor(Delta))
print("Psi' factor:", sp.factor(sp.diff(Psi,M)))
print("Psi(M1), M1=d(d-1)/2:", sp.factor(Psi.subs(M,d*(d-1)/2)))
print("dF/dkappa:", sp.factor(sp.diff(F,k)))
print("denominator on curve:", sp.factor(sp.simplify(((k-d+1)*M+(d-1)).subs(k,Psi))))
# first coefficient: Ntilde_3 via chat_3 formula
n=sp.symbols('n')
print("chat_3 = ", sp.factor(-(2*d+1)*(d-2)/((d+1)*(d+2))))

assert sp.simplify(N-(d-1)/d*Ntilde/k)==0
assert sp.simplify((d*m-1)/(d-1)-(1-d*(M-1)/(k*M)))==0
assert sp.simplify(((2*bexpr-1)*M+(d-1)*bexpr+1)*k*M-Ntilde)==0
assert sp.simplify(Ntilde-M*(M+d)*(k-Psi))==0
assert sp.simplify(Delta-d*(M-1)**2*(2*M-d*(d-1))/((d+1)*M**2*(M+d)**2))==0

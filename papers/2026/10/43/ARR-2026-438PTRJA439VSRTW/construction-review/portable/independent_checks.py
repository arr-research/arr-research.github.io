"""Independent review checks. No imports from the author's construction.

Exact coefficient checks use Fraction; exact complex gate checks use SymPy.
Floating-point tests are diagnostics, not substitutes for the proof.
All files created by this script stay in its own review directory.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path
import hashlib, itertools, json, math, shutil
import numpy as np
import scipy.linalg as la
import sympy as sp

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'candidate-proof-reviewed.txt'
EXPECTED = '73e4cfca4fd371f56b9539c232e64daf6c25feb4d0e8653b35286f811496f13e'
A, B, C = F(3, 5), F(4, 5), F(12, 25)
SEED = 202610172359
RNG = np.random.default_rng(SEED)
records = []

def require(ok, message):
    if not bool(ok):
        raise AssertionError(message)

def record(name, **details):
    records.append(dict(name=name, **details))

def coefficient_block(gate):
    u, v, w, z, sign = gate
    slots = [(0, 0, u, A), (0, 1, w, sign * B),
             (1, 0, z, B), (1, 1, v, -A)]
    coeff = {}
    for row, col, label, scalar in slots:
        coeff.setdefault(label, [[F(0) for _ in range(2)] for _ in range(2)])
        coeff[label][row][col] += scalar
    return coeff

def local_exact(gate):
    coeff = coefficient_block(gate)
    left = [[sum(mat[i][k]*mat[j][k] for mat in coeff.values() for k in range(2))
             for j in range(2)] for i in range(2)]
    right = [[sum(mat[k][i]*mat[k][j] for mat in coeff.values() for k in range(2))
              for j in range(2)] for i in range(2)]
    ident = [[F(int(i == j)) for j in range(2)] for i in range(2)]
    weights = {label: sum(x*x for row in mat for x in row) for label, mat in coeff.items()}
    labels = list(coeff)
    cross = {(i,j):sum(coeff[i][r][c]*coeff[j][r][c] for r in range(2) for c in range(2))
             for i in labels for j in labels if i != j}
    return left == ident and right == ident, weights, all(v == 0 for v in cross.values())

def compile_words(n, words):
    """words = [(tuple(generator indices), sign)], before fresh t,t padding."""
    z, t = 0, n + 1
    labels = list(range(n + 2))
    prepared = [(tuple(j+1 for j in word)+(t,t), sign) for word,sign in words]
    prepared.append(((t,t), 1))
    gates = []
    locations = []
    for r, (word,sign) in enumerate(prepared):
        u = word[0]
        loc = []
        for j in range(1,len(word)):
            final = j == len(word)-1
            w = z if final else len(labels)
            if not final:
                labels.append(w)
            loc.append(len(gates))
            gates.append((u,word[j],w,z,sign if final else 1))
            u = w
        locations.append(loc)
    q = {i:F(1) for i in labels}
    for gate in gates:
        stochastic, weights, disjoint = local_exact(gate)
        require(stochastic and disjoint, f'Invalid coefficient gate {gate}')
        for label,w in weights.items():
            q[label] += 25*w
    require(all(v.denominator == 1 for v in q.values()), 'Noninteger squared coefficient weights')
    mass = max(q.values())
    singles = {i:1+int(mass-q[i]) for i in labels}
    dimension = sum(singles.values())+50*len(gates)
    require(dimension == len(labels)*mass, 'Balanced dimension identity')
    final_q = {i:F(singles[i]) for i in labels}
    for gate in gates:
        for label,w in local_exact(gate)[1].items():
            final_q[label] += 25*w
    require(all(v == mass for v in final_q.values()), 'Equal Gram diagonal')
    return dict(n=n, s=len(labels), D=dimension, M=int(mass),
                gates=gates, singles=singles, prepared=prepared, locations=locations)

def haar(m):
    z = RNG.normal(size=(m,m)) + 1j*RNG.normal(size=(m,m))
    q,r = la.qr(z)
    return q @ np.diag(np.diag(r)/np.abs(np.diag(r)))

def norm2(x):
    return float(la.norm(x, 'fro')/math.sqrt(x.shape[0]))

def polar(x):
    u,_,vh=la.svd(x)
    return u@vh

def gate_matrix(gate, labels):
    u,v,w,z,sign=gate
    return np.block([[float(A)*labels[u], sign*float(B)*labels[w]],
                     [float(B)*labels[z], -float(A)*labels[v]]])

def pencil_block_data(spec, labels):
    blocks = [(labels[i],mult) for i,mult in spec['singles'].items()]
    blocks += [(gate_matrix(g,labels),25) for g in spec['gates']]
    return blocks

def aggregate(spec, labels):
    blocks=pencil_block_data(spec,labels)
    m=labels[0].shape[0]
    hs2=sum(mult*float(la.norm(block,'fro')**2) for block,mult in blocks)/(spec['D']*m)
    logdet=sum(mult*float(np.linalg.slogdet(block)[1])*2 for block,mult in blocks)/(spec['D']*m)
    op=max(float(la.norm(block,2)) for block,_ in blocks)
    defect2=sum(mult*float(la.norm(block@block.conj().T-np.eye(len(block)),'fro')**2)
                for block,mult in blocks)/(spec['D']*m)
    delta2=sum(mult*float(la.norm(block-polar(block),'fro')**2) for block,mult in blocks)/(spec['D']*m)
    return dict(hs2=hs2,logdet=logdet,op=op,defect2=defect2,delta2=delta2)

def extend_prefix(spec, generators, reference=None):
    m=generators[0].shape[0] if generators else (reference.shape[0] if reference is not None else 1)
    ref=np.eye(m,dtype=complex) if reference is None else reference
    labels={0:ref, spec['n']+1:ref}
    labels.update({i+1:gen@ref for i,gen in enumerate(generators)})
    for u,v,w,z,sign in spec['gates']:
        if w != 0:
            labels[w] = labels[u]@ref.conj().T@labels[v]
    return labels

def exact_gate_checks():
    i=sp.I
    u=sp.Matrix([[sp.Rational(3,5),4*i/5],[4*i/5,sp.Rational(3,5)]])
    v=sp.diag(1,i)
    z=sp.Matrix([[sp.Rational(5,13),12*i/13],[12*i/13,sp.Rational(5,13)]])*sp.diag(i,1)
    w=u*z.H*v
    h=(sp.Rational(3,5)*u).row_join(sp.Rational(4,5)*w).col_join(
        (sp.Rational(4,5)*z).row_join(-sp.Rational(3,5)*v))
    require(sp.simplify(h*h.H-sp.eye(4)) == sp.zeros(4), 'Exact complex multiplication block')
    require(sp.simplify(u*z.H*v*z.H-w*z.H) == sp.zeros(2), 'Right gauge orientation')
    wrong=v*z.H*u
    require(sp.simplify(u*z.H-wrong*v.H) != sp.zeros(2), 'Reversed product should be detected')
    require(sp.simplify(u*z.T-w*v.H) != sp.zeros(2), 'Transpose replacement should be detected')
    scalar=sp.Matrix([[sp.Rational(3,5),-sp.Rational(4,5)],[sp.Rational(4,5),-sp.Rational(3,5)]])
    require(set((scalar*scalar.T).eigenvals()) == {sp.Rational(1,25),sp.Rational(49,25)}, 'Sharp endpoint spectrum')
    require(abs(scalar.det()) == sp.Rational(7,25), 'Endpoint determinant')
    symmetric=sp.Matrix([[1,-1],[1,-1]])/sp.sqrt(2)
    require(symmetric.det() == 0, 'Equal-coefficient negative control')
    record('exact_complex_orientation_and_spectral_endpoints', passed=True,
           endpoint_eigenvalues=['1/25','49/25'], endpoint_abs_determinant='7/25',
           reversed_product_rejected=True, transpose_rejected=True, equal_coefficient_control_singular=True)

def construction_checks():
    patterns=[(1,2,3,0,1),(1,1,3,0,1),(1,2,0,0,1),
              (1,2,0,0,-1),(1,1,0,0,1),(1,1,0,0,-1)]
    for p in patterns:
        ok,weights,disjoint=local_exact(p)
        require(ok and disjoint, f'Allowed pattern failed {p}')
    # Deliberately violate the distinct-label condition. It really is needed.
    illegal=(1,2,1,0,1)
    require(not local_exact(illegal)[0], 'Forbidden repeated output should fail bistochasticity')
    fixtures=[(0,[]),(0,[((),1)]),(0,[((),-1)]),
              (1,[((0,),1),((0,),-1)]),(1,[((0,0),1)]),
              (2,[((0,1,0,1),1),((0,0),1),((1,1),1)]),
              (3,[((0,1,2),-1),((1,),-1),((0,0,0),1)])]
    specs=[compile_words(n,words) for n,words in fixtures]
    for trial in range(160):
        n=int(RNG.integers(1,8))
        words=[]
        for r in range(int(RNG.integers(0,15))):
            length=int(RNG.integers(0,11))
            words.append((tuple(int(j) for j in RNG.integers(0,n,size=length)),int(RNG.choice([-1,1]))))
        compile_words(n,words)
    record('exact_rational_balancing', passed=True, allowed_collision_patterns=len(patterns),
           forbidden_collision_rejected=True, fixed_cases=[{k:s[k] for k in ('n','s','D','M')} for s in specs],
           seeded_random_presentations=160)
    return specs

def numerical_gate_checks():
    maximum_identity_error=0.0
    maximum_log_error=0.0
    maximum_log_ratio=0.0
    minimum_sigma=10.0
    maximum_sigma=0.0
    for trial in range(360):
        m=(1,2,3,5,8)[trial%5]
        u,v,w,z=(haar(m) for _ in range(4))
        h=np.block([[float(A)*u,float(B)*w],[float(B)*z,-float(A)*v]])
        residual=u@z.conj().T-w@v.conj().T
        target=np.block([[np.eye(m),float(C)*residual],[float(C)*residual.conj().T,np.eye(m)]])
        err=norm2(h@h.conj().T-target)
        maximum_identity_error=max(maximum_identity_error,err)
        require(err < 1e-12, 'HH* offdiagonal identity')
        singular=la.svdvals(h)
        minimum_sigma=min(minimum_sigma,float(singular.min()))
        maximum_sigma=max(maximum_sigma,float(singular.max()))
        require(singular.min() >= .2-1e-12 and singular.max() <=1.4+1e-12, 'Uniform spectral bound')
        deficit=-float(np.linalg.slogdet(h)[1])/m
        spectral_deficit=-float(np.log(1-float(C*C)*la.svdvals(residual)**2).sum())/(2*m)
        maximum_log_error=max(maximum_log_error,abs(deficit-spectral_deficit))
        require(abs(deficit-spectral_deficit)<2e-12, 'Exact log determinant formula numerically')
        ratio=deficit/(norm2(residual)**2)
        maximum_log_ratio=max(maximum_log_ratio,ratio)
        require(ratio <=72/49+1e-12, '72/49 log upper bound')
    record('random_complex_gate_diagnostics', passed=True, cases=360,
           max_identity_error=maximum_identity_error,max_log_formula_error=maximum_log_error,
           max_observed_log_ratio=maximum_log_ratio, min_observed_sigma=minimum_sigma,
           max_observed_sigma=maximum_sigma)

def aggregate_checks():
    spec=compile_words(2,[((0,0),1),((1,1),1),((0,1,0,1),1),((0,1),1)])
    m=3
    max_forward_violation=-1e99
    max_reverse_ratio=0.0
    eps_values=[]
    for trial in range(48):
        scale=10**(-1-trial%5)
        # Perturb a consistent all-identity solution by genuinely complex matrices.
        generators=[]
        for j in range(2):
            raw=RNG.normal(size=(m,m))+1j*RNG.normal(size=(m,m))
            herm=(raw+raw.conj().T)/2
            generators.append(la.expm(1j*scale*herm))
        labels=extend_prefix(spec,generators,haar(m))
        data=aggregate(spec,labels)
        require(abs(data['hs2']-1)<1e-11, 'Balanced HS norm for unitary labels')
        relations=[]
        gauged={j:labels[j]@labels[0].conj().T for j in labels}
        for word,sign in spec['prepared']:
            product=np.eye(m,dtype=complex)
            for j in word:
                product=product@gauged[j]
            relations.append(norm2(product-sign*np.eye(m)))
        eta=max(relations)
        violation=-data['logdet']-(72/49)*eta*eta
        max_forward_violation=max(max_forward_violation,violation)
        require(violation<1e-10, 'Aggregate forward logarithmic bound')
        # Make coefficients non-unitary and highly unequal in their singular values.
        perturbed={j:x+scale*(RNG.normal(size=(m,m))+1j*RNG.normal(size=(m,m))) for j,x in labels.items()}
        normalization=math.sqrt(sum(norm2(x)**2 for x in perturbed.values())/spec['s'])
        rawlabels={j:x/normalization for j,x in perturbed.items()}
        rawdata=aggregate(spec,rawlabels)
        require(abs(rawdata['hs2']-1)<1e-10, 'Coefficient normalization')
        epsilon=-math.expm1(rawdata['logdet'])
        require(0<epsilon<1, 'Positive determinant objective needed')
        delta=math.sqrt(rawdata['delta2'])
        require(delta*delta <=2*(1-math.sqrt(1-epsilon))+2e-11, 'Polar AMGM extraction')
        rounded={j:polar(x) for j,x in rawlabels.items()}
        avgd2=sum(norm2(rawlabels[j]-rounded[j])**2 for j in rawlabels)/spec['s']
        require(avgd2 <= spec['D']*delta*delta+1e-10, 'Singleton extraction Gram bound')
        roundeddata=aggregate(spec,rounded)
        require(math.sqrt(roundeddata['defect2']) <=(12/5)*(math.sqrt(spec['D'])+1)*delta+1e-10,
                'Rounded BB*-I bound')
        bound=5*math.sqrt(spec['D']/2)*(math.sqrt(spec['D'])+1)*delta
        for u,v,w,z,sign in spec['gates']:
            residual=rounded[u]@rounded[z].conj().T-sign*rounded[w]@rounded[v].conj().T
            require(norm2(residual)<=bound+1e-10, 'Individual reverse residual bound')
            max_reverse_ratio=max(max_reverse_ratio,norm2(residual)/bound)
        eps_values.append(epsilon)
    record('forward_reverse_aggregate_diagnostics',passed=True,cases=48,
           s=spec['s'],D=spec['D'],M=spec['M'],
           largest_forward_lhs_minus_rhs=max_forward_violation,
           largest_gate_error_over_extraction_bound=max_reverse_ratio,
           smallest_objective_deficit=min(eps_values),largest_objective_deficit=max(eps_values))

def exact_noncommutative_word_example():
    # Pauli anti-commutation: (XZ)^2=-I. This is a signed-word fixture,
    # not asserted to be a binary-system row whose entries commute.
    x=sp.Matrix([[0,1],[1,0]])
    z=sp.diag(1,-1)
    ref=sp.Matrix([[sp.Rational(3,5),4*sp.I/5],[4*sp.I/5,sp.Rational(3,5)]])
    spec=compile_words(2,[((0,0),1),((1,1),1),((0,1,0,1),-1)])
    labels={0:ref,1:x*ref,2:z*ref,3:ref}
    for u,v,w,r,sign in spec['gates']:
        if w!=0:
            labels[w]=sp.simplify(labels[u]*ref.H*labels[v])
        residual=sp.simplify(labels[u]*ref.H-sign*labels[w]*labels[v].H)
        require(residual==sp.zeros(2),'Exact noncommutative word gate')
    require(all(sp.simplify(v*v.H)==sp.eye(2) for v in labels.values()),'Unitary prefix labels')
    # No scalar assignment can solve x^2=z^2=1 and xzxz=-1.
    require(all((a*b*a*b)!=-1 for a,b in itertools.product((-1,1),repeat=2)), 'Scalar negative check')
    record('exact_noncommutative_word_fixture',passed=True,s=spec['s'],D=spec['D'],M=spec['M'],
           gate_count=len(spec['gates']),complex_nontrivial_reference=True,
           scalar_sign_assignments_rejected=4,solution_dimension=2)

def main():
    data=SOURCE.read_bytes()
    actual=hashlib.sha256(data).hexdigest()
    require(actual==EXPECTED,'Candidate version changed before independent checks')
    (ROOT/'candidate-proof-reviewed.txt').write_bytes(data)
    text=data.decode('utf-8-sig')
    (ROOT/'candidate-proof-numbered.txt').write_text(''.join(f'{i:4d}: {line}\n' for i,line in enumerate(text.splitlines(),1)),encoding='utf-8')
    exact_gate_checks()
    construction_checks()
    numerical_gate_checks()
    aggregate_checks()
    exact_noncommutative_word_example()
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest()==EXPECTED,'Candidate modified during checks')
    output=dict(status='all checks passed', source=str(SOURCE), sha256=actual,source_bytes=len(data),
                random_seed=SEED, tests=records,
                qualification='Exact finite checks plus floating-point diagnostics; not a formal proof of undecidability or universal estimates.')
    (ROOT/'independent-checks.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output,ensure_ascii=True,indent=2))

if __name__=='__main__':
    main()

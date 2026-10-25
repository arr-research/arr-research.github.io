"""Author cross-check from sparse polynomial-evaluation AME states.

Does not use the Choi error-space expansion to compute expectations.
Cyclotomic character sums are reduced exactly over prime fields.
No dense d^6-by-d^6 matrix is constructed.
"""
from collections import defaultdict,Counter
from fractions import Fraction as Q
from itertools import product,combinations
import json

def run(d):
    assert d in (7,13)
    words=[tuple((a+b*x+c*x*x)%d for x in range(6))
           for a,b,c in product(range(d),repeat=3)]
    assert len(set(words))==d**3
    # Every three coordinates give all d^3 values once. The complementary
    # three also distinguish all words, proving off-diagonal cancellation.
    for T in combinations(range(6),3):
        assert len({tuple(w[i] for i in T) for w in words})==d**3
    ref=Counter((w[0],w[1]) for w in words)
    assert len(ref)==d*d and set(ref.values())=={d}
    # Physical four-tuples distinguish all words. Thus the R density of
    # both Psi and w=Z_output0 Psi is exactly I/d^2, Schmidt rank d^2.
    assert len({w[2:] for w in words})==d**3
    terms=[]
    for u in range(5):
        for sites in combinations(range(2,6),u):
            remaining=tuple(i for i in range(6) if i not in sites)
            groups=defaultdict(list)
            for w in words:
                groups[tuple(w[i] for i in remaining)].append(
                    (tuple(w[i] for i in sites),w[2]))
            # G[a,s] = <Psi_a,w_s> times d^3; coefficients count powers
            # of zeta_d exactly. Only pairs sharing untraced coordinates
            # contribute. This implements Tr_sites(Psi Psi*) tensor I.
            gram=defaultdict(Counter)
            for entries in groups.values():
                for a,_ in entries:
                    for s,phase in entries:
                        gram[(a,s)][phase]+=1
            cyclic=[0]*d
            for coeff in gram.values():
                for h,c in coeff.items():
                    for j,e in coeff.items():cyclic[(h-j)%d]+=c*e
            # For these symmetric full-reference vectors all nonzero
            # coefficients coincide. sum_{h=1}^{d-1}zeta_d^h=-1.
            assert len(set(cyclic[1:]))==1,(d,sites,cyclic)
            theta=Q(cyclic[0]-cyclic[1],d**6)
            assert theta>=0
            terms.append({'traced_physical_sites':[i-2 for i in sites],
                          'partial_trace_expectation':str(theta),
                          'raw_character_coefficients':cyclic})
    direct=d*d*sum(((-Q(1,2))**(4-len(r['traced_physical_sites']))*
                   Q(r['partial_trace_expectation']) for r in terms),Q(0))
    predicted=Q(7,4)-Q(2,d)-Q(d,8)
    assert direct==predicted,(d,direct,predicted)
    return {'d':d,'codewords':len(words),'AME_three_site_checks':20,
            'normalized_vector':'Z on physical site 0 applied to Psi',
            'Schmidt_rank':d*d,'direct_Choi_Rayleigh':str(direct),
            'predicted':str(predicted),'terms':terms}

r=[run(d) for d in (7,13)]
assert r[1]['direct_Choi_Rayleigh']=='-3/104'
print(json.dumps({'status':'PASS','method':'Exact sparse partial-trace contraction and prime cyclotomic reduction, separately from error-space expansion','scope':'Author cross-check of two explicit codes and selected full-rank vectors; not proof of all low-Schmidt-rank positivity, not an independent referee audit','cases':r},indent=2))

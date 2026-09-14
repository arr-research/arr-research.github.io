"""coset_meshulam_vs_omega.py -- (i) for supports inside a coset of the p^j-torsion T_j with 2j <= k the Weyl operators commute
and nullity = p^{k-2j} * #{chi in dual(T_j) : c-hat(chi) = 0}; Meshulam's inequality on the abelian group (Z/p^j)^2 (consecutive
divisors p^a <= l <= p^{a+1}) gives #zeros <= p^{2j} - ceil(p^{2j-2a-1}(p^a + p^{a+1} - l)).  Check that
      p^{k-2j} * (p^{2j} - ceil(...)) <= Omega_k(l)   for all p in {2,3,5,7}, k <= 7 (p^k <= 2401), 1 <= j <= k/2, 1 <= l <= p^{2j},
and report where equality holds.  (ii) Gap table: for each d = p^k list the sparsities l for which Conjecture C
(dim ker C <= Omega_k(l)) is NOT implied by Theorem B (l <= 2p-1) nor by the field-free bound rank >= ceil(d/l) nor trivial (l >= d).
"""
import math

def w(r, p):
    out = 1
    while r: out *= (r % p) + 1; r //= p
    return out

def omega(p, k, m):
    best = 0
    for r in range(p**k):
        if w(r, p) <= m: best = r
    return best

def meshulam_max_zeros(p, j, l):
    n = p**(2*j)
    divs = [p**a for a in range(2*j+1)]
    for d1, d2 in zip(divs, divs[1:]):
        if d1 <= l <= d2:
            return n - math.ceil(n*(d1 + d2 - l)/(d1*d2))
    return n - 1

viol = 0; eq = 0; tot = 0
for p in (2, 3, 5, 7):
    for k in range(2, 8):
        d = p**k
        if d > 2401: break
        for j in range(1, k//2 + 1):
            for l in range(1, p**(2*j) + 1):
                bound = p**(k-2*j) * meshulam_max_zeros(p, j, l)
                om = omega(p, k, l)
                tot += 1
                if bound > om:
                    viol += 1; print("VIOLATION", p, k, j, l, bound, om)
                elif bound == om: eq += 1
print(f"(i) coset-of-T_j Meshulam bound vs Omega_k(l): {tot} cases, violations={viol}, equalities={eq}")
print("(ii) gap table (Conjecture C not implied by Theorem B / multiplicative bound / triviality):")
for p in (2, 3, 5, 7):
    for k in range(2, 8):
        d = p**k
        if d > 2401: break
        gaps = []
        for l in range(1, d):
            om = omega(p, k, l)
            if l <= 2*p - 1: continue
            if d - math.ceil(d/l) <= om: continue
            gaps.append((l, om))
        rngs = []
        for l, om in gaps:
            if rngs and rngs[-1][1] == l-1 and rngs[-1][2] == om: rngs[-1][1] = l
            else: rngs.append([l, l, om])
        print(f"  d={d}: gaps (l range -> Omega_k(l), i.e. required rank >= d - Omega): " +
              ("; ".join(f"[{a},{b}] -> {om} (rank >= {d-om})" for a, b, om in rngs) if rngs else "none  => Conjecture C is a THEOREM for this d"))
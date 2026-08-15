# Exact entanglement-spectrum and architecture laws for complete unitary-error ensembles

## Scope

This memo supplies a genuinely input-dependent multitime channel theorem that
can strengthen Paper 21 without changing its abstract matroid theorem.  It is
an exact application, not a claim that unitary-error bases, dense coding, or
parallel optimality for independent unitary channels are new.

Let `A` have dimension `D`, and let

```text
U_1,...,U_(D^2)
```

be a complete unitary error basis (UEB): every `U_g` is unitary and
`Tr(U_g^* U_h)=D delta_(g,h)`.  The unknown, uniformly distributed channel is
`Phi_g=Ad_(U_g)`.  A pure probe `psi in A tensor R` has reference marginal
`rho_R=Tr_A |psi><psi|`.

## Theorem A: exact entanglement-spectrum law

For one use of the complete UEB ensemble, the optimal one-label success
probability for the fixed probe `psi` is

```text
P_opt(psi) = (Tr sqrt(rho_R))^2 / D
           = exp(H_(1/2)(rho_R)) / D.
```

Consequently, among probes of Schmidt rank at most `r<=D`,

```text
max P_opt = r/D,
```

and equality holds exactly when the nonzero Schmidt coefficients are all
`1/r`.  Classical mixtures do not improve this value: after conditioning on
the classical flag, every component obeys the same cap.

For lists of size at most `ell`, the same fixed probe obeys the sharper
entanglement-spectrum bound

```text
P_list(psi) <= min(1, ell (Tr sqrt(rho_R))^2/D).
```

Indeed, from a list POVM `{M_L}`, the subnormalised effects
`N_g=ell^(-1) sum_(L containing g) M_L` sum to at most the identity.
Completing them to a one-label POVM shows
`P_guess>=P_list/ell`, and Theorem A applies.  Equality holds for the
unreferenced standard-Weyl construction up to `ell=D`, and trivially for a
full Bell reference, but need not hold at intermediate Schmidt rank.

### Proof

Write `psi_g=(U_g tensor I)psi` and

```text
S = sum_g |psi_g><psi_g|.
```

Completeness of the Hilbert--Schmidt orthogonal operator basis gives the
depolarising identity

```text
sum_g U_g X U_g^* = D Tr(X) I_A.
```

Equivalently, the Choi matrix of the left side is
`sum_g |U_g>><<U_g|=D I_(A tensor A)`.  Hence, on
`K=A tensor supp(rho_R)`,

```text
S = D I_A tensor rho_R.
```

Set

```text
c = <psi_g|S^(-1/2)|psi_g>
  = Tr sqrt(rho_R)/sqrt(D),
```

which is independent of `g`.  The square-root measurement

```text
M_g=S^(-1/2)|psi_g><psi_g|S^(-1/2)
```

sums to `I_K` and has average success `c^2`.

For optimality, use the minimum-error dual SDP.  The operator

```text
Y=(c/D^2) S^(1/2)
```

obeys `Y >= |psi_g><psi_g|/D^2` for every `g`.  Indeed, the rank-one
domination criterion says that
`c S^(1/2)>=|psi_g><psi_g|` iff

```text
<psi_g|(c S^(1/2))^(-1)|psi_g> = c/c = 1.
```

Moreover

```text
Tr Y=(Tr sqrt(rho_R))^2/D=c^2.
```

Primal and dual values agree, proving the formula.  Finally,
`(sum_j sqrt(lambda_j))^2 <= r sum_j lambda_j=r`, with equality precisely
for the flat nonzero Schmidt spectrum.  This proves the rank statement.

## Corollary B: independent multitime UEBs

Let time slot `t` have dimension `d_t` and a complete UEB.  The tensor-product
ensemble is itself a complete UEB on dimension

```text
D=product_t d_t.
```

Theorem A therefore holds for an arbitrary parallel probe, including probes
entangled across different input times.  In particular:

1. With no retained reference, every pure parallel input has exactly
   `P_opt=1/D`; cross-time input entanglement cannot change the value.
2. With a global reference and Schmidt-rank budget `r`, the exact optimum is
   `min(r,D)/D`.
3. For product probes with local reference marginals `rho_t`, the optimum
   factorises:

   ```text
   P_opt=product_t [(Tr sqrt(rho_t))^2/d_t].
   ```

These claims concern the specified independent complete-UEB ensemble.  They
do not assert that a Schmidt-rank constraint is preserved under arbitrary
adaptive comb dilations.

## Theorem C: exact list architecture trichotomy for Weyl histories

Fix `n>=1`, a carrier dimension `d>=2`, and independent uniform Weyl labels
`(a_t,b_t) in Z_d^2` at the `n` times.  There are `M=d^(2n)` channel-history
hypotheses.  Compare the following explicitly delimited architectures.

* `SER_0`: one `d`-dimensional coherent carrier is reused; known unitary
  controls may be inserted, but there is no side memory, intermediate
  measurement, or retained transcript, and only a final list measurement is
  made.
* `PAR_0`: `n` fresh `d`-dimensional inputs are used in parallel; their joint
  pure input may be arbitrarily entangled, but no reference is retained.
* `PAR_Bell`: each input is paired with a `d`-dimensional Bell reference.

For a reported list of size at most `ell`, the exact optima are

```text
P_SER0^(ell)    = min(1, ell/d^(2n-1)),
P_PAR0^(ell)    = min(1, ell/d^n),
P_PARBell^(ell) = 1.
```

Thus, before saturation, parallelising the input registers gains the exact
factor `d^(n-1)` over a carrier-only coherent serial wiring, while Bell
references gain the further factor `d^n/ell` over unreferenced parallel use.

### Proof

For any uniform ensemble of `M` pure output states in a Hilbert space of
dimension `q`, the list-support inequality gives

```text
P_list <= min(1, ell q/M).
```

Every `SER_0` strategy has only a `d`-dimensional terminal quantum system,
even after known interleaving unitaries, so `q=d`.  This proves its upper
bound.  It is attained without interleavings: projective Weyl multiplication
maps the `n` labels to the net label

```text
(A,B)=(sum_t a_t, sum_t b_t) mod d,
```

and every net label has `d^(2n-2)` histories.  On input `|0>`, measuring the
computational basis reveals `A`; exactly `d^(2n-1)` histories remain uniformly
possible.  Reporting any `ell` of them attains the first formula.

Every `PAR_0` output lies in dimension `q=d^n`; this proves its upper bound,
even for an entangled input across slots.  The product input `|0>^tensor n`
and a computational-basis measurement reveal the entire shift vector
`(a_1,...,a_n)`, leaving exactly `d^n` equiprobable phase histories.  This
attains the second formula.  Finally, local Bell inputs turn the Weyl outputs
into an orthonormal product Bell basis and give one-label certainty.

## Exact fixture and a necessary warning about intermediate list ranks

Take the one-slot Weyl ensemble with `D=4` and the canonical rank-two probe

```text
|Phi_2>=(|0,0>+|1,1>)/sqrt(2).
```

The sixteen outputs split into four mutually orthogonal shift sectors.  In
each sector the four phase states are

```text
|phi_b>=(|0>+i^b|1>)/sqrt(2),  b=0,1,2,3.
```

For lists of size two their exact optimum is

```text
P_list=(1+1/sqrt(2))/2=(2+sqrt(2))/4 < 1.
```

To prove this, use the four adjacent lists `{b,b+1}`.  Their reward operators
`rho_b+rho_(b+1)` have top eigenvalue `1+1/sqrt(2)`, and the corresponding
top eigenvectors form a tight frame.  Half their projectors form a POVM and
attain `(1+1/sqrt(2))/2`.  Conversely the covariant dual

```text
Y=[1+1/sqrt(2)] I/4
```

dominates every two-label reward operator divided by four (opposite pairs
have smaller top eigenvalue `1`).  Orthogonal-sector pinching transfers the
same optimum to all sixteen channel outputs for this fixed probe.

This fixture forbids the tempting overclaim that the coarse cap
`min(1,ell r/D)` is always attained at intermediate Schmidt rank when
`ell>1`: here that cap equals one but the canonical flat rank-two probe is
strictly below one.  It does **not** prove that no other rank-two probe can do
better, so no resource-optimised list claim is made.

## Architecture counterexamples and claim boundary

* Intermediate measurements with retained classical outcomes are excluded
  from `SER_0`; they enlarge the terminal information space and can simulate
  fresh-input protocols.  The serial formula must not be advertised for
  adaptive combs.
* The exact spectrum law uses a complete `D^2`-element UEB.  Removing labels,
  changing priors, or replacing the UEB by a nonorthogonal unitary family
  destroys the depolarising frame identity.
* The multitime parallel theorem treats independent UEB labels.  Repetition
  of one common unknown unitary is a different hypothesis space.
* The rank-two list fixture is fixed-probe optimality only.

## Priority audit

Primary context that must be cited before manuscript integration:

1. G. Chiribella, G. M. D'Ariano, and P. Perinotti, *Memory Effects in
   Quantum Channel Discrimination*, Phys. Rev. Lett. 101, 180501 (2008):
   parallel optimality for independent unitary-channel discrimination in the
   unrestricted architecture class.
2. J. Bavaresco, M. Murao, and M. T. Quintino, *Unitary channel
   discrimination beyond group structures*, arXiv:2105.13369: group ensembles
   and distinctions among parallel, sequential, and general strategies.  The
   final journal metadata must be checked before bibliography insertion.
3. S. Wu, S. M. Cohen, Y. Sun, and R. B. Griffiths, *Deterministic and
   Unambiguous Dense Coding*, Phys. Rev. A 73, 042311 (2006),
   arXiv:quant-ph/0512169: partial-entanglement and Schmidt-rank constraints
   in dense coding.
4. M. F. Sacchi, *Optimal discrimination of quantum operations*, Phys. Rev.
   A 71, 062340 (2005): minimum-error discrimination of unitary/random-unitary
   operations.
5. Q. Zhuang and S. Pirandola, *Ultimate Limits for Multiple Quantum Channel
   Discrimination*, Phys. Rev. Lett. 125, 080505 (2020): symmetric multiple
   channel-discrimination bounds and attainability under symmetry.

The safe novelty target is the combined theorem package: the exact
entanglement-spectrum formula for every complete UEB probe, its tensorised
multitime resource law, and the closed list architecture trichotomy.  A broad
search did not locate this combined statement, but that is not a priority
proof.  The dense-coding and group-discrimination ingredients are established
and must not be individually claimed as new.

## Gates

* `U1` algebraic UEB twirl and SDP primal/dual proof: **PASS**.
* `U2` Schmidt-rank equality conditions: **PASS**.
* `U3` tensor-product/multitime reduction: **PASS**.
* `U4` serial/parallel/full-reference list constructions and dimension
  converses: **PASS**, within the stated architecture definitions.
* `U5` exact `D=4,r=2,ell=2` fixed-probe fixture: **PASS**; replay required.
* `U6` primary-source novelty audit: **PARTIAL**.  Primary context identified,
  but a full citation-level priority comparison is still mandatory before a
  novelty claim or submission.
* `U7` integration/no-salami gate: **OPEN**.  Integrate only as a major
  channel theorem, together with the scalable adaptive EB family, or reserve
  it for a separate broader architecture paper; do not append it as cosmetic
  length.

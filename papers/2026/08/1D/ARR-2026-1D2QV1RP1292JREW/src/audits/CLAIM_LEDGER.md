# Claim ledger

## Scope

The target is a finite-dimensional nonzero traceless Hermitian matrix `F`.
The norm is the unnormalized Hilbert--Schmidt norm. Set

```
P(F)=||F||_1/2,  rho=rank(F).
```

## Analytic claims

| ID | Claim | Status | Proof location | Replay role |
|---|---|---|---|---|
| C1 | `kappa_d(F)=1/2 min ||C||_HS^2` over `[C,C*]=2F`; the minimum is attained | Proved | Lemma 2.1 | Symbolic convention check only |
| C2 | Exact sign-cut leakage identity for `kappa_d(F)-P(F)` | Proved | Theorem 2.2 | None; direct trace identity |
| C3 | `kappa_d(F)>=P(F)`; equality iff `spec(F)=-spec(F)` with multiplicity | Proved | Proposition 3.1 | Paired constructor algebra |
| C4 | `kappa_d(F)<=rho P(F)/2` | Proved | Lemmas 4.1-4.2 | Shift identity and exact permutation averages |
| C5 | Upper equality forces flat sign blocks and one sign multiplicity one | Proved | Proposition 5.1 | Adjacent-swap rational checks |
| C6 | Zero-padded one-spike spectra attain `rho P(F)/2` | Proved | Proposition 6.2 | Exact Horn-sum arithmetic at every rank through dimension 20; the manuscript writes out the subset-to-partition convention and LR unit coefficient |
| C7 | Fixed-rank supremum is `rho/2`; full-dimensional supremum is `d/2` | Proved | Corollary 1.2 | Consequence of C4 and C6 |
| C8 | Relative tax `<=epsilon` gives total optimal sign-cut leakage `<=2 epsilon P(F)` | Proved | Corollary 2.3 | Direct consequence of C2 |

## Imported classical results

| ID | Input | Use |
|---|---|---|
| I1 | Trace-zero and self-commutator existence | Historical context; feasibility is also constructed directly |
| I2 | Horn--Littlewood--Richardson spectral-sum inequalities | Only the `rho-1` explicit triples in the one-spike lower certificate |
| I3 | Weighted shifts from nonnegative partial sums | Classical construction pattern; averaged optimization is the new use |
| I4 | Weiss's inverse HS--HS problem for unrestricted factors | Explicitly separated from the Hermitian-factor optimization; the four-level spike has unrestricted cost `4/3` but Hermitian cost `2` |
| I5 | Beltiță--Patnaik--Weiss weighted-shift and spike discussion | Construction and energy antecedents only; no rank-adaptive minimum or equality classification is attributed to it |
| I6 | Fong; Maher; Filonov--Safarov; Zhang | Nearby norm, approximation, operator-comparison, and Aluthge-transform results; cited and separated from the prescribed-target inverse minimum |

## Novelty boundary

The paper does **not** claim the first self-commutator representation, the Horn
theorem, weighted shifts, or a forward Frobenius commutator inequality.
It also does not identify its Hermitian-factor cost with Weiss's distinct
unrestricted-factor cost.

The claimed theorem package is:

- the sharp rank-adaptive inverse HS--HS tax `rho/2`;
- the exact fixed-rank worst targets;
- complete equality classifications at both endpoints;
- the exact sign-cut leakage representation of the trace tax.

Priority language is explicitly qualified by the literature search described
in the paper. No exhaustive-priority claim is made.

## Explicit nonclaims

- No infinite-factor or unbounded-operator theorem.
- No operator-norm optimization.
- No graph-local, gate-local, or fixed-control-algebra result.
- No full closed formula for interior spectra in arbitrary dimension.
- No quantitative stability modulus at the upper one-spike endpoint.
- No formal proof-assistant verification of Horn's theorem.
- No laboratory energy or duration model.

## Independent audit corrections incorporated

- Lower equality uses `rho=2m`, not `rho` positive pairs.
- The Horn subset size is `ell`; its residual telescopes to `p_ell`.
- Attainment is justified by finite-dimensional compactness.
- Removal of `p_d` is realized through the polar decomposition and subtraction
  of the common positive floor.
- Zero padding is kept explicitly throughout the one-spike certificate.
- The convention-sensitive Horn triple is made self-contained through the
  explicit subset-to-partition map and `c_{0,lambda}^{lambda}=1`.
- The replay is standard-library only, uses explicit checks, writes atomically,
  and rejects optimized Python.

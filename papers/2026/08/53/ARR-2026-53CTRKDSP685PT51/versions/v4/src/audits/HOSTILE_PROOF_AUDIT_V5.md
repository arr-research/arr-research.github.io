# Hostile proof audit V5

**Manuscript:** `work/neuron_paper_v2/src/main.tex`  
**Verifier:** `work/neuron_paper_v2/repro/verify_saturation_law.py`  
**Verdict:** **REVISE**

No advertised formula was falsified. The spherical coefficient, finite-scale constants, all-`p` coefficients, empirical block bounds, probability count, Loewner normalization, eigenspace decomposition, logistic envelopes, and empty-slab lower bound all survive independent derivation. Two proof-completeness/scope fixes remain mandatory before acceptance. A third fix is a displayed-formula typo.

## Mandatory fixes

### [P1] The logistic angle corollary needs a quantitative empirical gap, not merely `G>0`

Corollary 7.2 (lines 750--785) states the angle rate

\[
\sin\angle(\widehat u,u)
=O_p\!\left(
\sqrt{\frac{d+\log(1/\delta)}{nr}}
+\frac{\sqrt{[d+\log(1/\delta)]\log(1/\delta)}}{n}
\right)
\]

“once `G>0`.” Positivity alone is insufficient for that big-`O` conclusion: Theorem 7.1 only gives

\[
\tan\angle(\widehat u,u)\le q_n/G.
\]

If `G` is arbitrarily small but positive, `q_n/G` need not be bounded by the displayed rate with a `p`-dependent constant. The proof says that increasing `C_p` “gives the angle bound,” but it never states or derives the quantitative denominator needed.

The repair is immediate but must be explicit. Choose the same `C_p` in (samplesufficient) large enough that

\[
e_T+e_R\le\frac{\alpha-\beta}{2}.
\]

Then

\[
G\ge\frac{\alpha-\beta}{2}
\ge\frac{\varphi(0)m_0(p)}{4r},
\]

and substituting the displayed bound for `q_n` proves the claimed angle rate. Either add this conclusion to the corollary and proof, or retain only the exact `q_n/G` statement. The current phrase “once `G>0`” overstates what follows.

### [P1] The all-`p` endpoint proof uses local `O` expansions under unbounded integrals without stating domination

The coefficients in Theorem 6.2 are correct, but lines 592--599 are not proof-complete as written.

For the small-`r` expansion, the displayed pointwise Taylor series

\[
h_p(t)=4^{-p}[1+a_2t^2+a_4t^4+a_6t^6+O(t^8)]
\]

cannot simply be inserted at `t=rZ`, because `Z` is unbounded and a local `O(t^8)` does not by itself dominate the Gaussian expectation. The required fact is true: for each fixed `p>0`, every derivative of
`h_p(t)=4^{-p}sech^{2p}(t/2)` is bounded. Taylor's theorem with bounded eighth derivative therefore supplies the global remainder

\[
|R_8(rZ)|\le \|h_p^{(8)}\|_\infty r^8|Z|^8/8!,
\]

which is integrable both for `alpha` and, after multiplying by `Z^2`, for `beta`. State this argument.

For the large-`r` refinement, obtaining an `O(r^{-2})` remainder after the constant term requires, in particular, the finite sixth sensitivity moment in the expansion of `beta`. Logistic powers have all moments finite, but the proof cites only Lemma 6.1 through `m_4` and says “one further term.” State explicitly that `m_6(p)<infinity` (indeed all moments are finite) and bound the exponential remainder. Without these two domination statements, the formal coefficients are right but the asserted remainder orders have not been proved.

### [P2] Correct the malformed Taylor display

Line 491 contains

```tex
g'(\delta)=...+R_1,quad
```

rather than `R_1,\quad`. It compiles as four unintended mathematical variables and should be corrected before publication.

## Findings that passed hostile verification

### Spherical bridge

For isotropic spherical `X=RU`,

\[
E Z^4=\frac{3ER^4}{d(d+2)}=3q_X,
\qquad
E[Z^2(v^TX)^2]=\frac{ER^4}{d(d+2)}=q_X.
\]

The fourth-derivative remainder in `h_p(rZ)`, multiplied by the quadratic matrix factor, uses moments of total degree six; the stated `E||X||^6<infinity` is exactly sufficient. The ratio coefficient is therefore `-q_X h_p''(0)/h_p(0)=-q_XpSg(0)`. The standard Gaussian has `q_X=1`; the radius-`sqrt(d)` sphere has `q_X=d/(d+2)`, matching the verifier.

### Explicit finite-scale bridge

The Gaussian remainders are exact:

\[
|R_\alpha|\le \frac{M_4}{24}r^4EZ^4=\frac{M_4}{8}r^4,
\qquad
|R_\beta|\le \frac{M_4}{24}r^4EZ^6=\frac{5M_4}{8}r^4.
\]

The `r_0` condition makes `beta>=a/2`. Direct algebra gives precisely

\[
C_h=\frac{3M_4}{2a}+3(b/a)^2
+\frac{5|b|M_4}{4a^2}r_0^2.
\]

For the Loewner determinant, with `V=(g(delta)-g(0))/delta`,

\[
\det L_g(0,\delta)=A[g'(\delta)-A]-2A(V-A)-(V-A)^2.
\]

The cubic coefficient is `Ad_4/12`; the fifth-derivative remainders contribute
`7AM_5 delta_0/120`, and `|V-A|<=K|delta|^2` contributes `delta_0K^2`. Thus the displayed `D_g` and all signs in (quantloewner)--(directfinitebridge) are correct.

### All-power moments, monotonicity, and coefficients

The beta transform gives

\[
\widehat h_p(k)=B(p+ik,p-ik),
\]

and differentiation gives exactly

\[
m_2=2\psi_1(p)m_0,qquad
m_4=(12\psi_1(p)^2+2\psi_3(p))m_0.
\]

The MLR derivative is strictly negative for every real `p>0`, so global strict monotonicity is valid. Independent symbolic division confirms

\[
\kappa_p(r)=1+\frac p2r^2-\frac p8r^4+rac{p(p+1)}{16}r^6+O(r^8).
\]

Expanding the scaled large-`r` integrals confirms

\[
\kappa_p(r)=\frac{r^2}{2\psi_1(p)}
+1+\frac{\psi_3(p)}{4\psi_1(p)^2}+O(r^{-2}).
\]

Only the domination/remainder explanation identified above is missing.

### Empirical block concentration and probability count

The block representation is correct. Conditional on the radial scores, the tangential block is a weighted Wishart matrix and the cross block is exactly isotropic Gaussian. The constants in `e_T,e_R,q_n` are consistent with scalar Bernstein, the exact centered-chi-square mgf, a `1/4`-net of size `9^m`, and the Gaussian norm tail.

The failure allocation is:

| Event | Failure bound |
|---|---:|
| scalar `Wbar-alpha` | `2e^{-t}` |
| upper bound for `sum W_i^2` | `e^{-t}` |
| conditional net | `2e^{-t}` |
| radial Bernstein | `2e^{-t}` |
| upper bound for `sum W_i^2Z_i^2` | `e^{-t}` |
| Gaussian cross norm | `e^{-t}` |

The total is `9e^{-t}=3delta/4<delta` for `t=log(12/delta)`.

Conjugating by the population square root gives a normalized diagonal error bounded by
`max(e_T/alpha,e_R/beta)` and an off-diagonal norm `q_n/sqrt(alpha beta)`, exactly yielding `epsilon_n`. The relative Loewner bound is correct. Interlacing, the block eigenvector equation, and the Schur complement give the unique low eigenvalue, `tan(angle)<=q_n/G`, and `|betahat-beta|<=e_R+q_n^2/G` with the stated `G`.

### Logistic envelopes and sample scaling

The elementary exponential envelope yields exactly

\[
H=4^{-p},\quad K_1\le e^{-2}/(p^2r^2),\quad
K_2\le4e^{-2}/(p^2r^2),
\]

and

\[
\gamma_0\le\varphi(0)/(pr),\quad
\gamma_1\le\varphi(0)/(2p^3r^3),\quad
\gamma_2\le3\varphi(0)/(2p^5r^5).
\]

The definition of `R_p` indeed implies

\[
\alpha\ge\frac{\varphi(0)m_0(p)}{2r},\quad
\beta\ge\frac{\varphi(0)m_2(p)}{2r^3},\quad
\alpha-\beta\ge\frac{\varphi(0)m_0(p)}{2r}.
\]

Thus a finite `p`-dependent constant gives the advertised
`n=O_p(r[d+log(1/delta)]/epsilon^2)` relative-Gram threshold. The gap clarification above is the only missing step for the displayed angle rate.

### Empty-slab lower bound

Let `q=P{|Z|<=a_p/r}`. Under the stated radius condition, `q<=1/2` and

\[
(1-q)^n\ge e^{-2nq}
\ge e^{-4\varphi(0)a_pn/r}.
\]

The tail integral is at most `beta/8`; conditioning outside the slab divides by at most `1-q>=1/2`, so the conditional radial-entry mean is at most `beta/4`. Markov then makes that entry smaller than `beta/2` with probability at least `1/2`, and `lambda_min(Hhat)<=u^THhat u` transfers the event to the smallest eigenvalue. Both (lower) and (lowern) are correct. The manuscript also correctly refuses to infer a matching `Omega(rd)` or a minimax parameter-estimation lower bound.

## Replay and final gate

The verifier completed successfully:

- figure SHA-256: `093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97`;
- certificate SHA-256: `a5442d5840a08ed1394e21f8f4d82f7947ba35ba7bd6cc5e9cf00d4df0c3618a`.

The manuscript compiled successfully to 17 pages. The replay is appropriately diagnostic; its fixed-seed empirical successes are not used as proofs.

After the quantitative-gap statement, endpoint-remainder justification, and `\quad` typo are repaired, the verdict becomes **ACCEPT**.

## Final fix verification addendum

**Recheck date:** 2026-08-29  
**Final verdict:** **ACCEPT**

The three mandatory V5 fixes are correctly implemented in the current `src/main.tex`:

1. **Quantitative angular gap:** Corollary 7.2 now requires the sample constant to be large enough that
   `e_T+e_R <= (alpha-beta)/2`, derives
   `G >= (alpha-beta)/2 >= phi(0)m_0(p)/(4r)`, and only then substitutes `q_n` into the exact angle inequality. This closes the denominator gap and proves the displayed rate with a finite `p`-dependent constant.
2. **Endpoint remainders:** the large-`r` proof now states `m_6(p)<infinity` and displays expansions with the required remainder orders. The small-`r` proof now invokes the bounded eighth derivative of `h_p`, obtains the global Taylor bound `||h_p^(8)||_infinity |t|^8/8!`, and uses the Gaussian tenth moment for the `beta_p` integral. Both interchanges and both asserted `O` terms are justified.
3. **Taylor-display typo:** `R_1,quad` is corrected to `R_1,\quad`.

No new objection is introduced by these edits. The V5 publication gate is closed: **ACCEPT**.

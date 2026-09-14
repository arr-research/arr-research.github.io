# Scientific checks — A3_inertia_m3 candidate 2

**UTC review window:** 2026-09-14T17:33Z–2026-09-14T17:43Z  
**Exact PDF SHA-256:** `f67c4b52fb7c74f59bc3c3945c593c1bfe146f02b47dc41d596ad5e9fd03d33a`  
**Recommendation:** accept

## Mathematical audit

Writing `R=CC*/2` and `S=C*C/2` correctly converts the problem into two positive semidefinite matrices with the same spectrum and difference F. Conversely, any such pair is realised by a singular-value decomposition. Subtracting the common smallest eigenvalue shows that an optimum has `s_d=0`, and Horn feasibility for spectra `(s,-s^rev,lambda)` gives the stated finite linear program.

A tiling certificate is sufficient: summing its Horn inequalities gives a right side equal to the target form, while every coefficient of `s_t` on the left is at most one. Positivity of the `s_t` then makes the total cost dominate the form. The standalone verifier checks this coefficient identity and positive LR coefficient exactly.

For the upper bound, the block-bidiagonal weighted shift decomposes the commutator into adjacent-layer equations. The chain LP is equivalent to these equations because Horn necessity and sufficiency apply at each layer of size at most three; the orientation of each new positive matrix is free once the shared spectrum is fixed. For a fixed symbolic layering, all spectral orderings are fixed on the closed ordered stratum, so the feasible set is a projection of a polyhedron and is convex. Feasibility at all exact vertices of a chamber therefore extends to the whole chamber. Together with the lower certificates, this proves `kappa=max S` without requiring probabilistic discovery to have found every possible dual form.

The family-A proof correctly tiles successive full-capacity tails with disjoint positive index blocks. Its final-layer case handles both available zero slots and the fallback to individual Weyl inequalities.

## Fresh exact checks

The selected scripts were inspected before execution. No supplied pickle was loaded; scripts that can load legacy pickles were excluded. Execution occurred in `work/sol-preassessment/A3_inertia_m3/repro` with `C:/Python312/python.exe -X utf8`.

```text
TOTAL exact certificates 875 tiles 4342
set/family comparison m=3,...,9: expected counts and z0 extras agree
PASS 526 exact strict exposedness witnesses, complete for m=3..9,z=0,1
TOTAL 945 (form,z) family-A certificates verified
m=3,4,5; z=0,1: every chamber covered by one exact chain: True
m=4,5,7,8 padding margins: 1/40, 1/60, 1/120, 1/150
padding example: g0=74/61; max S(4,1)=73/61
```

The first tiling attempt in the isolated copy stopped because `families.py` had not yet been copied. After inspecting and adding that source dependency, the complete rerun exited successfully. No scientific check was bypassed.

The exact upper replay executed every chamber through m=5 for z=0,1, including the two zero-insertion cases. I did not repeat the slower m=6,...,9 upper sweeps. The supplied exact verifier architecture and proof logic were inspected, but those rows remain execution-unchecked in this assessment.

PDF extraction succeeded at `2026-09-14T17:39:02.6118185Z`: 19 pages and 72,397 characters.

## Claims boundary

The theorem range m<=9, z<=2 is presented as computer-assisted. The all-m family A is proved analytically. The six-family exhaustiveness, modulo-three continuation beyond the finite range, and m=10,11 chamber formulas are clearly labelled conjectural or numerical. The literature check confirms that Angel–Schechtman studies a different factorisation norm objective and that Klyachko's work supplies the Hermitian-sum spectral framework; this is not exhaustive priority certification.

## Disclosure

`independence=involved_in_manuscript`. The same model family participated in manuscript revision. This assessment used a fresh delegated task context with other reports withheld. That is not technical memory isolation or an independent human review. This is a local scientific preassessment only and does not accept, deposit, publish, authorize public release, or create an intake receipt.

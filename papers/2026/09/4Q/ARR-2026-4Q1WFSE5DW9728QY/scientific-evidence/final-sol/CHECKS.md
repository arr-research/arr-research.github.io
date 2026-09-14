# Scientific checks — A5_general_mn candidate 2

**UTC review window:** 2026-09-14T17:39Z–2026-09-14T17:49Z  
**Exact PDF SHA-256:** `ffea17de8edce73844df1705c439f89e4a8f18eaf3de4a0f374cdec056c51921`  
**Recommendation:** accept

## Proof audit

The Horn-program reduction is correct. For an ordered full-capacity layering, the nonfinal Lidskii–Wielandt tiles contribute consecutive blocks `[t_u,t_u+c_u-1]`; full capacity makes those blocks disjoint. The final Weyl tiles complete the partition of `s_1,...,s_m`, and all negative coefficients occur at later `s` indices. Their sum is therefore bounded above by the cost objective and proves Theorem 1 for every m,n,z. The proof does not require the negative schedule to be ordered. The rearrangement lemma then follows directly because only `-sum u_i b_i` changes under reassignment of a fixed schedule multiset.

For Theorem 2A, a balanced path produces a weighted shift with squared edge weights equal to minus twice the preceding partial sum. The commutator telescopes to the prescribed diagonal, and the cost identity follows from total balance. Conversely, when all intermediate positive matrices are diagonal, their equal diagonal spectra admit a monomial matching; the resulting support graph decomposes into consecutive-layer paths. Full capacity forces one positive per live negative path in each nonfinal layer, yielding the claimed one-spike split.

For Theorem 2B, the rank-one inverse eigenvalue lemma has the correct interlacing and trace conditions. At the mixed layer, the target spectrum `tau(k)` interlaces `diag(b_2,...,b_n,-a_k)` exactly when `tau_i<=b_i<=tau_{i-1}`. The preceding scalar states are nonnegative because `B'<=sum_{i<n}tau_i<=A_{k+1}`. The diagonal continuation removes one positive from each live column per layer, gives the terminal matrix exactly, and has total rank m. Strictly decreasing positives make R_k full-dimensional precisely for `k<=m-n+1`.

Theorem 3 uses weak duality correctly. If the target form had any nonnegative certificate from box<=3 Horn, ordering, and positivity inequalities, it would lower-bound every feasible point of the restricted primal. The supplied rational restricted-feasible spectrum has smaller cost, so such a certificate cannot exist. The displayed box-4 tiling then proves the form itself valid. The second rational witness similarly excludes the broader Pieri-shaped class for `g'`.

For the d=8 example, summing the first pair of Horn rows with `s_1>=5` and two copies of `s_4>=2` gives cost at least 13 and forces `s_6=s_7=0` on the optimal face. The second pair with `s_1>=5`, `s_4>=2` gives cost plus `s_5-s_7>=14`, hence `s_5>=1`. The integer spectrum `(5,3,2,2,1,0,0,0)` satisfies all 8,752 Horn inequalities and attains cost 13, proving rank exactly five.

## Fresh execution

No supplied pickle was opened. The revision verifier regenerated Horn sets in memory. For the longer reviewer tests, the inspected cache-free generator was copied under the module name expected by those tests in the isolated workcopy.

`2026-09-14T17:42:50.5573250Z`–`2026-09-14T17:42:58.3865755Z`:

```text
PASS exact full-Horn integer rank-five witness; every optimizer has s5>=1 and s6=s7=0
PASS exact g restricted rows 13328 gap 1/184 full-Horn equality and LR tiling
PASS exact gprime restricted rows 12798 gap 9923/838490 full-Horn equality and LR tiling
PASS exact gprime box<=3 obstruction
ALL REVISION CHECKS PASSED
```

`2026-09-14T17:43:08.0257269Z`–`2026-09-14T17:44:48.1769742Z`:

```text
Theorem 1 exact certificates: 28+28+43+157+251+61 = 568 schedules verified
random ordered-bound tests: max(OL-kappa) <= 4.4e-16
aligned-spike constructions: residual <= 6.2e-16; cost error <= 6.7e-16
interlacing-region constructions: residual <= 1.6e-15; cost error <= 1.1e-15
all nonempty R_k runs returned rank m; all k>m-n+1 returned empty interior
```

An additional integer-only loop at `2026-09-14T17:45:28.6995013Z` checked the d=8 witness against all 8,752 generated Horn triples: minimum margin 0 and cost 13.

PDF extraction at `2026-09-14T17:45:41.9602091Z` succeeded: 17 pages and 63,810 characters.

## Literature and scope

Fulton's primary survey supports the Horn/Littlewood–Richardson characterization used here. Golub and Chu are appropriate sources for rank-one modified inverse eigenvalue problems. Angel–Schechtman treats a different commutator factorisation norm, consistent with the manuscript's distinction. These checks support attribution but do not certify exhaustive priority.

The Section 8 catalogues, block-size conjecture, padding rules, and sample counts remain numerical. The manuscript flags an incomplete reflected catalogue and does not promote it to a theorem. Earlier AIRR results were withheld and not used as assessment evidence.

## Disclosure

`independence=involved_in_manuscript`. The same model family participated in manuscript revision. This assessment used a fresh delegated task context with other reports withheld. That is not technical memory isolation or an independent human review. This is a local scientific preassessment only and does not accept, deposit, publish, authorize public release, or create an intake receipt.

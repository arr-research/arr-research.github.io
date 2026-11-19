      What would establish a lower cost per surviving mangrove?
           A finite-population audit of a restoration plan
                                                 Lluis Eriksson
                                               19 November 2026


                                                      Abstract
         We use a proposed 20-hectare restoration budget in Muara Sekampung to ask what future observations
     would certify a lower initial cost per established plant. A verified count of 81,619 established plants
     from the self-managed nursery suffices even against perfect establishment of purchased seedlings. One of
     the five proposed configurations could supply this count alone. We obtain sharp finite-population error
     probabilities for audits that select the same number of positions but use different spatial sampling designs.
     Under a stated equal-capacity frame, 13 successes from 13 distinct random hectares give a worst-case
     false certification probability of 0.04882 or less. Thirteen successes from one random hectare can have
     probability above 0.75 under the same null. We derive an exact rule for unequal capacities and show
     separately how fixed costs affect the published density comparison. These are design calculations for
     future monitoring.


1    The decision and the missing observation
Hafidhin, Kusmana and Rusdiana [1] estimated the initial cost of two ways to provide the same N = 125,269
seedlings. Their Table 8 gives A = 401,564,900 Indonesian rupiah for a self-managed nursery and B =
616,326,000 for external procurement. These totals include the same initial planting cost of 217,269,000
rupiah. Long-term maintenance and replacement lie outside the published budget. Their Table 7 assigns
102,960 positions to cluster planting over 16 hectares. Four other designs contain 4,356, 10,201, 5,151 and
2,601 positions. The authors explicitly describe proposed configurations awaiting field evaluation. Field
research elsewhere has documented that planting targets and established plants can diverge [2].
    Fix one horizon, an establishment criterion and one identifiable original position per seedling. Let X, Y
denote the numbers established under the full nursery and purchasing scenarios. These are alternative
outcomes for the same planning scale. For positive counts the nursery has a strictly lower initial cost per
established plant exactly when BX − AY > 0. We hold the two budgets fixed. The analysis does not estimate
the procurement effect on survival. If a scenario produces no established plant its unit cost is undefined; a
nursery with positive establishment still dominates zero output at positive cost.


2    What a single census can certify
Since Y ≤ N , verifying X > K = ⌊AN/B⌋ = 81,618 is sufficient against any purchasing outcome. It is
necessary for a uniform conclusion if only a lower count for X is known: at or below K one can set Y = N
and X to that count. A census confined to the four smaller designs can verify at most 22,309 establishments.
Even full observation of both alternatives in those designs cannot certify an advantage uniformly: their best
possible contribution is B(22,309) and the unobserved large configuration can contribute −A(102,960).
    The large configuration alone can certify the sign. For example, if both full-scale scenarios yielded exactly
s establishments there, the worst remaining contribution is −A(22,309). Then (B − A)s > A(22,309) first
holds at s = 41,714. This two-scenario sensitivity calculation is distinct from the observable one-nursery
threshold. We use the latter to construct a prospective test that requires access only to the implemented
nursery.



                                                          1
3     The spatial design changes the error rate
Under the null X ≤ K, a randomly audited position is scored as one only if establishment at the chosen
horizon is verified. Unknowns must not be silently removed from the draw. Preselect the design and sample
size and certify only when every sampled position scores one. All probability statements are over random
selection from a fixed finite landscape. With a uniform sample withoutreplacement    from the full frame of N
positions, the maximal probability of certification under the null is K     N
                                                                                at sample size k. The first k at
                                                                              
                                                                       k /  k
which it falls below 0.05 is seven. If only the H = 102,960 positions in the large configuration are accessible,
replace N by H: the worst case places all K survivors there. The first qualifying k is 13. These fixed-sample
guarantees cannot be reused at each of a sequence of chosen stopping times; time-uniform methods for finite
populations are available [3].
    For an explicit comparison suppose that the large configuration can be registered as g = 16 blocks of
M = 6,435 positions each. The published planting density is an average; this equal-capacity register would
need field verification. Write xj for the fixed number established in block j. The worst-case sum of the xj is
K. Define ek as the sum of the products over all k-element subsets, with e0 = 1.
    • Choose k distinct blocks uniformly, then independently         choose one uniform position per selected block.
      The probability of all successes is ek (x)/[ kg M k ]. It is maximized by balancing counts to within one. For
                                                     

      two components a, b with the others z, the numerator is ek (z) + (a + b)ek−1 (z) + ab ek−2 (z) (out-of-range
      terms are zero). Transferring a unit from the larger to the smaller when their difference exceeds one
      cannot decrease the product. The maximum is achieved with two counts of 5,102 and fourteen of 5,101.
    • Choose one blockP uniformly   and sample k distinct positions   uniformly
                                                                                inside it. The probability of
      all successes is j xkj /[g M    ]. The first difference of x
                                                                     equals k−1 and increases weakly with x.
                                                                             x
                                                                  
                                  k                              k
      Transferring a unit toward a larger non-full block cannot decrease this sum. The maximum is attained
      by twelve full blocks, one with 4,398 establishments, and three empty blocks.
For k = 13 the two sharp probabilities are 0.048812 and 0.750441 respectively (rounded). The uniform
position sample in the large configuration gives 0.048802. The concentrated design retains a false-certification
probability of at least 12/16 even if every position in the selected block is examined. These are upper error
rates for the all-success rule, not estimates of its power. Dispersing visits can entail substantial travel costs
which the monitoring calculation does not price.


4     An exact rule for unequal block sizes
Let the registered capacities be positive integers m1 , . . . , mg . Select a k-subset I with probability i∈I mi /ek (m)
                                                                                                         Q
and then sample one uniform position from each selected block. The product-weight subset law is classical [4].
Each admissible set of positions in distinct blocks is equally likely, giving the exact all-success probability
ek (x)/ek (m). Drawing successive blocks in proportion to remaining size need not implement the specified
subset law. One implementation draws uniform k-subsets of positions and repeats the draw if two selected
positions share a block,
                     P before observing any outcomes.
    For total K ≤       mi , find the largest integer a ≤ max mi with i min(mi , a) ≤ K. Start at xi =
                                                                                  P
min(mi , a), then distribute the remaining units among distinct unsaturated components. This vector
maximizes the numerator: the pair transfer above increases balance whenever a smaller block has spare
capacity and another exceeds it by at least two. The sum of squares strictly decreases at each transfer,
so the procedure terminates at the described profile up to ties. All bounds are attained by actual integer
configurations.
    For g = 16, fix the total H = 16M , with each mi between M − d and M + d. While M − d ≥ ⌈K/16⌉,
the balanced maximizing numerator is feasible for every frame. The denominator is smallest at eight copies
of each endpoint. Indeed, increasing the larger of two non-endpoint coordinates at the expense of the smaller
cannot increase ek . Iteration reaches endpoints, with at most one intermediate coordinate. The fixed sum
forces that coordinate to an endpoint as well. Hence the two extremes are simultaneously attainable. Exact
evaluation gives the largest symmetric tolerance for a uniform five-percent guarantee with 13 dispersed visits
as 437 positions on either side of 6,435. At the next integer the extremal frame fails. Wider tolerances
include that same counterexample. For a known frame the direct ratio remains available.


                                                          2
5    A separate sensitivity in the spending comparison
Table 9 of the planning study compares costs at 5,000 seedlings per hectare. As an arithmetic normalization
this scales the unit price. Interpreting it as expenditure at a new density additionally requires a model of which
items change. Keep area fixed at 20 hectares and let h = 100,000/N . If F rupiah of the purchasing budget
remain fixed and the rest scales proportionally, the hypothetical expenditure per hectare is [hB + (1 − h)F ]/20.
It crosses the Table 9 reference of 24,879,600 rupiah per hectare at approximately 27.712 million rupiah of
fixed costs. Holding only the 20 million planting transport cost fixed stays below this figure; holding only the
72 million planting labour cost fixed takes the re-budgeted estimate to 25.326 million rupiah per hectare.
Both models match the original total exactly. These hypotheses illustrate sensitivity and do not identify
actual contracts. The reference amount is attributed to the published table. Its administrative scope has not
been independently established.

Scope and reproducibility. The field paper supplies planning quantities and costs. No survival census,
randomized audit, replacement policy or measured budget response is available for this proposed planting. A
real audit needs a complete sampling frame, inclusion of failed positions, a fixed horizon and an unambiguous
establishment criterion. Uncertain expenditure would also change K. The calculations use exact rational
arithmetic. The companion files include the digitized quantities, all 32 selections of planting configurations,
exhaustive small-frame checks of both spatial extremizers, and the two integer tolerance endpoints. No
third-party article or field data are redistributed.

Model assessments and review context. OpenAI Codex participated in development, checking and
drafting in the author’s context. Any version-specific assessment of the PDF is recorded separately. The
author operates AIRR.


References
[1] D. Hafidhin, C. Kusmana and O. Rusdiana. An integrated species–site suitability, planting design, and
    cost assessment framework for mangrove rehabilitation in Muara Sekampung, Indonesia. Jurnal Penelitian
    Pendidikan IPA 12 (2026), 64–78. https://doi.org/10.29303/jppipa.v12i11.15691.
[2] D. C. J. Wodehouse and M. B. Rayment. Mangrove area and propagule number planting targets produce
    sub-optimal rehabilitation and afforestation outcomes. Estuarine, Coastal and Shelf Science 222 (2019),
    91–102. https://doi.org/10.1016/j.ecss.2019.04.003.

[3] I. Waudby-Smith and A. Ramdas. Confidence sequences for sampling without re-
    placement.     NeurIPS      (2020).     https://proceedings.neurips.cc/paper/2020/hash/
    e96c7de8f6390b1e6c71556e4e0a4959-Abstract.html.
[4] X.-H. Chen, A. P. Dempster and J. S. Liu. Weighted finite population sampling to maximize entropy.
    Biometrika 81 (1994), 457–469. https://doi.org/10.1093/biomet/81.3.457.




                                                        3

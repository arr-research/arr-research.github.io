 Prices and unused volume in Britain’s demand flexibility auctions
                                             Lluis Eriksson

                                          20 November 2026


                                                Abstract
         Britain’s National Energy System Operator publishes the volumes it seeks, each bid it accepts
     or rejects, and the volumes it later settles. We match these records for 620 live half-hours in
     July–September 2026. In 206 demand-reduction windows across 40 events, some positive bids
     were rejected even though the published requirement exceeded procurement and other bids
     were accepted. Every one contained a whole rejected bid that fit both the residual national
     requirement and its zonal cap. In all 206, however, the lowest rejected price exceeded the
     highest accepted price across all zones. The smallest gap was £0.20/MWh. These observations
     distinguish uncontracted volume from an inversion of bid prices. They leave the operator’s
     internal valuation and the value of additional delivery unidentified.


1    What does an unfilled requirement tell us?
A buyer seeking 300 MW accepts 13.1 MW and rejects a further 2 MW. On 30 September 2026 this
happened in event 137 of Britain’s Demand Flexibility Service (DFS) from 15:30 to 16:00 UTC.
The rejected offer fit within the residual published requirement and the remaining cap in its own
zone. Was a cheaper resource passed over? Answering that narrower question requires prices and a
comparison among offers in the same procurement window.
    NESO introduced bidirectional flexibility and zonal procurement in April 2026 [2]. Its pro-
curement rules call for ranking valid submissions by price. They allow adjustments for system
conditions and uneconomic procurement, discretion at a zonal boundary and full acceptance of
individual submissions [3, pars. 12.2–12.4, 14.3–14.4]. The operator already reports offered and
accepted volumes in its winter reviews [4]. We test a more specific empirical proposition: whether
posted prices strictly separate the two decisions where published volume limits leave room for at
least one further bid. This is a test of observable decisions, conditional on the specified cohort.


2    Cohort and tests
We use three separately published tables from the same operator [1]. The key is the event identifier,
delivery date, direction and both UTC endpoints. We retain live half-hours from 1 July through
30 September 2026 with a positive published requirement. Missing settlement does not exclude a
window from the auction analysis. Each of the 620 summary windows matches one requirement.
The summary’s procured MW reconcile exactly to the sum of accepted unit bids in every window.
The bid ledger contains 7,281 accepted and 2,908 rejected rows for these windows. We restrict price
comparisons to positive-volume offers.
    For a demand-reduction window let R be required MW, P total accepted MW, Cz the published
cap in zone z and Az accepted MW there. A rejected bid of volume q in z fits the published limits
with accepted volumes fixed if q ≤ R − P and q ≤ Cz − Az . We test individual whole bids. For the

                                                    1
separate price test define L as the largest accepted price and U as the smallest rejected price, over
all zones in the half-hour. Accepting exactly the offers priced at or below t reproduces all observed
positive-volume decisions precisely when L ≤ t < U . The interval exists if and only if L < U : every
accepted offer requires t ≥ L, and every rejected offer requires t < U . We also compare each fitting
rejected bid to every accepted bid in its own zone and check the result using price extrema and ties.


3    Observed price intervals
Of 518 demand-reduction windows, 206 meet the three conditions 0 < P < R, a positive accepted
bid and a positive rejected bid. None of the 102 demand-increase windows had positive procurement.
The following counts describe the 206 mixed windows.

            Observation                                                       Half-hours
            A whole rejected bid fits both remaining limits                         206
            A fitting rejected bid and an accepted bid share a zone                 205
            A fitting rejection undercuts or ties an acceptance in its zone           0
            Highest acceptance below lowest rejection across all zones              206

    The one window without a same-zone comparator remains informative in the all-zone test. The
all-zone gap U − L ranges from £0.20 to £1,322.39 per MWh. The narrowest interval occurred in
event 107 on 31 August, 19:00–19:30 UTC: L = 165.00 and U = 165.20. In this window any t from
£165.00 inclusive to £165.20 exclusive per MWh reproduces the observed decisions. Nothing in
that calculation establishes which price NESO would have accepted for an unsubmitted offer. The
windows belong to 40 events; we do not treat half-hours within each event as independent draws.


4    How much volume and what was delivered?
Let Jz be the total rejected MW in zone z. Relaxing indivisibility gives the greatest increment
allowed by the two published volume constraints alone:
                                                                   !
                                             X
                               min R − P,         min(Cz − Az , Jz ) .
                                              z

The inner bound is attainable zone by zone for divisible offers; stopping at the national residual
gives the outer minimum. Across the 206 windows this relaxation totals 1,653.70 MWh. Choosing a
single largest fitting whole bid in each window gives 614.85 MWh. These are windowwise volume
calculations. Actual additional dispatch would also require an economic decision and operational
feasibility.
    Settlement answers a different question. Among the 518 reduction windows only 262 report
settled volume. For those windows the signed difference between required and procured energy
totals 58,368.45 MWh, and the difference between procured and settled energy totals 2,992.81 MWh.
We multiply MW by one half-hour before summing and retain seven negative settled entries. Across
all 518 windows the first difference is known, 112,668.95 MWh. Total procurement is 8,731.05 MWh
and observed settlement is 1,738.74 MWh. If x is the missing aggregate signed settlement, the
second difference equals the first at x = −105,676.64 MWh. This sensitivity calculation assigns no
values to the 256 unreported windows. A difference from a published procurement requirement
cannot be interpreted as unserved electricity.

                                                  2
5    Scope and reproducibility
The results establish strict price ordering in a defined quarter and cohort. They do not establish
efficient dispatch, explain particular rejections, or attribute a service to data centres. The operator
can revise its economic need. Bid validity, unit availability, network restrictions and alternative
balancing actions may matter. A half-hour price interval is fitted after observing decisions. Testing
whether an interval from one half-hour predicts decisions in another requires a separate, prospective
rule.
     The source package supplies the frozen tables, their digests, the window-level results and an
offline reproduction script. Supported by National Energy SO Open Data [5].

Model assessments and review context. OpenAI Codex assisted with the data analysis and
drafting. The exact-version assessment and its context are separate records. The author administers
AIRR. No independent peer assessment is claimed.


References
[1] NESO. Demand Flexibility Service data portal. Requirements, utilisation report and utilisation
    report summary, snapshot 19 November 2026 UTC.

[2] NESO. Demand Flexibility Service, service design effective 9 April 2026.

[3] NESO. Demand Flexibility Service Procurement Rules, published 18 May 2026.

[4] NESO. Demand Flexibility Service winter 2024/25 review.

[5] NESO. National Energy SO Open Data Licence v1.0.




                                                  3

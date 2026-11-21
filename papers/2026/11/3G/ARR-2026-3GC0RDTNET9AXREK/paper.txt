 What monthly photovoltaic summaries can identify about sensors
                      and missing days
                                                 Lluis Eriksson
                                                November 2026


                                                     Abstract
         We audit four columns of eight monthly summaries from an industrial rooftop photovoltaic system.
     Under the usual linear reference-yield model with common days and weights, the implied capacity in-
     tervals for May and June 2026 are disjoint even after rounding. Two positive daily records reproduce
     all four columns at their published precision: one retains every date and offsets the June irradiation
     reading; the other uses an unbiased sensor and omits one June irradiation reading. In May the printed
     performance ratio also differs from the quotient of mean yields. If it is a mean of daily ratios, we give a
     sharp lower bound on the product of daily reference-yield variability and performance-ratio dispersion.
     The constructive results identify which additional records could distinguish the explanations.


1    A check on a common set of dates
Nugroho and Saputra [1] report monthly means for a plant with 409 modules rated at 550 Wp, giving
C = 224.95 kWp. Tables 1 and 2 cover September–December 2025 and May–August 2026. Let T be daily
theoretical yield (kWh), H daily irradiation in the reference plane (kWh/m2 ), E generation (kWh), and
r = E/T . With standard reference irradiance of 1 kW/m2 , the usual reference-yield model gives T = CH
numerically in these units [2]. Averaging preserves this identity for the same dates and weights.
   We interpret the commas in the second table’s generation column as decimal separators. This choice is
needed for the performance-ratio check. The capacity check uses only T and H. With bars denoting means
and half a final printed unit allowed on either side of each value, a common capacity must lie in
                                                                               
                             (T̄ − .005)/(H̄ + .0005), (T̄ + .005)/(H̄ − .0005) .

               Month         Printed T̄     Printed H̄    Capacity interval (kWp)       Printed PR
               May 2026          965.13          4.290         [224.9446, 224.9994]           54.4%
               June 2026         920.02          4.095         [224.6405, 224.6978]           53.7%

The exact endpoints are separated by 0.24687985 kWp. Seven of the eight rows admit the stated nameplate;
June is the exception. A single constant multiplicative recalibration of one column would merely rescale the
common capacity and cannot close the gap. The paper reports platform exports. It does not establish that
the two columns use one irradiance input, reference plane, or completeness rule.




                                                         1
2    Two daily records with the same monthly output
Take every calendar day in each month. In June, put true irradiation at 4.095 on 29 days and 30(920.02/224.95)−
29(4.095) = 3.94159924 . . . on the other. Set T = CH daily. In the first record add 4.095 − 920.02/224.95 =
0.00511336 . . . kWh/m2 to each June irradiation reading and retain all 30 readings. In the second record use
true irradiation and omit the lower reading only from the irradiation mean. Both report 4.095 and the same
theoretical mean of 920.02. In both, generation and performance ratio use all dates.
    For months other than May and June, constant H = T̄ /C and r = Ē/T̄ reproduce all four rounded
columns; the same constant-ratio rule works in June. In May only, split the 31 dates into groups of 15 and
16. Let z be 16/31 on the first group and −15/31 on the second. Choose

                                                                     Ē/C − (T̄ /C)(.544)
                       H = T̄ /C + 0.5z,   r = .544 + bz,       b=                          .
                                                                            0.5 z 2
With Ē = 523.323 this yields the displayed means and CHr = Ē exactly. Every constructed daily irradiation
is positive and every performance ratio lies between zero and one. Thus the two synthetic explanations agree
on all four audited columns in all eight months. Neither implies that the site actually missed a reading or
suffered a sensor fault. The daily log in Table 5 covers August 2025, outside both monthly windows, and
cannot distinguish these constructions.


3    A sharp variability requirement in May
The ratio of the two displayed mean yields in May is 54.2231%. Even allowing rounding, its largest possible
value is 54.2234%, below the lower endpoint 54.35% for the printed PR. If the latter is the unweighted daily
mean r̄, the identity
                                         Ē/T̄ − r̄ = Cov(T, r)/T̄
forces negative covariance. Using population moments over the days and Cauchy–Schwarz gives the following
bound in fractional PR units:
                                                            523.3235     2793
                               CV(T ) SD(r) ≥ .5435 −                =         .
                                                            965.125    2206000
Equivalently, the product is at least 0.126609 percentage points when PR dispersion is expressed in percentage
points. This is sharp: set T̄ = 965.125, Ē = 523.3235 and r̄ = .5435 in the two-level construction. Its centered
ratio and yield are proportional with opposite signs, attaining equality in closed rounding bins. Moving the
means into the bins gives the same infimum for tie-breaking conventions that exclude an endpoint. Day-level
yields, sensor identifiers and the date masks actually used by each export could test these mechanisms. The
calculation does not identify soiling losses or an optimal cleaning schedule.

Model assessments and review context. AI assisted with the analysis and writing. Assessments of this
PDF are recorded separately by version and checksum. The accompanying scripts reconstruct the results
from the publisher’s PDF using rational arithmetic.

References. [1] D. Nugroho and P. P. S. Saputra, Assessment of Performance Ratio Variation in a 225
kWp Rooftop PV System Exposed to Industrial Fly Ash at PT Jaya Energi (2026), doi:10.25077/aijaset.v6i3.378.
   [2] B. Marion et al., Performance Parameters for Grid-Connected PV Systems (2005), NREL/CP-520-
37358.




                                                       2

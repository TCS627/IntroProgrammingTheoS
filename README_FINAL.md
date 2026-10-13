# Molecular asymmetry analysis (PRA2003)

## Introduction and research questions

We analyze simulated molecular/particle production events to investigate:
the mean count of each species per event, the difference between each
particle pair, and whether this difference changes with momentum.

## Data and method

- **Data:** 10 subsamples containing 4,617,993 events in total.
- **Pairs:** 211/−211, 321/−321, 2212/−2212, 3122/−3122, 3312/−3312, and 3334/−3334.
- **Mean counts:** Number of particles divided by the number of events; events with zero occurrences are included.
- **Per-subsample uncertainty:** Standard error of the event-level mean (sample standard deviation divided by √number of events).
- **Overall mean:** Arithmetic mean of the ten subsample means, matching the presentation workflow.
- **Overall count uncertainty:** Sample standard deviation of the ten subsample means (as in the class presentation).
- **Difference:** For each subsample, mean count for the positive ID minus mean count for the negative ID; final difference is the arithmetic mean of those ten differences (particles/event).
- **Difference uncertainty:** Sample standard deviation of the ten subsample-by-subsample differences (as in the supplied Python code).
- **Sigma score:** Absolute overall difference divided by its difference uncertainty. This is a course-style spread-based score, not a formal hypothesis-test p-value.
- **Momentum magnitude:** The Euclidean norm of the first three values on each particle row, calculated as √(px² + py² + pz²).
- **Momentum plots:** 20 logarithmic momentum bins (10⁻²³ kgm/s). Each point is the arithmetic mean of the ten RAW frequency differences (count of positive ID minus count of negative ID); each error bar is their sample standard deviation.
- **Plot limits:** In presentation mode, bins run from 0 to 20 and particles outside that range are not plotted but are included in all overall mean counts. In log mode, exact zero momentum cannot be plotted but is included in overall mean counts.

## Results

### Pair 211 and -211: Carbon monoxide / Carbon-13 monoxide

| Subsample | ID 211: average ± uncertainty | ID -211: average ± uncertainty |
|:--|--:|--:|
| 1 | 20.01012993 ± 0.02683736 | 19.98216162 ± 0.02681897 |
| 2 | 19.95795252 ± 0.02672348 | 19.92051707 ± 0.02669687 |
| 3 | 19.93137605 ± 0.02676029 | 19.90074968 ± 0.02673918 |
| 4 | 19.97056441 ± 0.02678209 | 19.93345261 ± 0.02675464 |
| 5 | 19.91651781 ± 0.02677824 | 19.88535164 ± 0.02674852 |
| 6 | 19.91764731 ± 0.02671080 | 19.88698880 ± 0.02669333 |
| 7 | 19.93260874 ± 0.02674008 | 19.89572607 ± 0.02671311 |
| 8 | 19.96316447 ± 0.02678717 | 19.92930367 ± 0.02675162 |
| 9 | 19.91187826 ± 0.02674886 | 19.88864878 ± 0.02672769 |
| 10 | 19.98328387 ± 0.02680778 | 19.94925593 ± 0.02678204 |
| **All subsamples** | **19.94951234 ± 0.03274619** | **19.91721559 ± 0.03187334** |

*Table: Particle averages are counts per event. Individual rows show mean ± standard error; the last row shows the arithmetic mean ± sample standard deviation of the ten subsample means.*

**Average difference (positive minus negative):** 0.03229675 particles/event  
**Difference uncertainty (SD across subsamples):** 0.00451870 particles/event  
**Sigma score:** 7.15σ  
**Interpretation:** A difference at or above 3σ under the class's spread-based convention.

![Momentum-dependent count difference for IDs 211 and -211](figures/asymmetry_211.png)

*Figure: Frequency difference between 211 and -211 in each momentum bin, averaged over ten subsamples. Error bars show the sample SD across the ten subsamples; the dashed line marks zero difference.*

### Pair 321 and -321: Nitric oxide / Ionised nitric oxide

| Subsample | ID 321: average ± uncertainty | ID -321: average ± uncertainty |
|:--|--:|--:|
| 1 | 2.51428305 ± 0.00409897 | 2.51469674 ± 0.00411062 |
| 2 | 2.50894367 ± 0.00409049 | 2.50426018 ± 0.00408233 |
| 3 | 2.50728782 ± 0.00409420 | 2.49989494 ± 0.00409407 |
| 4 | 2.51215978 ± 0.00409732 | 2.50584163 ± 0.00409805 |
| 5 | 2.50670460 ± 0.00409768 | 2.50040814 ± 0.00409679 |
| 6 | 2.50601158 ± 0.00408742 | 2.49967859 ± 0.00408346 |
| 7 | 2.50247905 ± 0.00408642 | 2.50004330 ± 0.00409186 |
| 8 | 2.50708067 ± 0.00409545 | 2.50340448 ± 0.00409495 |
| 9 | 2.50745192 ± 0.00409179 | 2.49639584 ± 0.00408549 |
| 10 | 2.51908372 ± 0.00411282 | 2.50995126 ± 0.00410770 |
| **All subsamples** | **2.50914859 ± 0.00477369** | **2.50345751 ± 0.00550369** |

*Table: Particle averages are counts per event. Individual rows show mean ± standard error; the last row shows the arithmetic mean ± sample standard deviation of the ten subsample means.*

**Average difference (positive minus negative):** 0.00569108 particles/event  
**Difference uncertainty (SD across subsamples):** 0.00329367 particles/event  
**Sigma score:** 1.73σ  
**Interpretation:** No clear asymmetry under the class's 2σ comparison convention.

![Momentum-dependent count difference for IDs 321 and -321](figures/asymmetry_321.png)

*Figure: Frequency difference between 321 and -321 in each momentum bin, averaged over ten subsamples. Error bars show the sample SD across the ten subsamples; the dashed line marks zero difference.*

### Pair 2212 and -2212: Water / Heavy water

| Subsample | ID 2212: average ± uncertainty | ID -2212: average ± uncertainty |
|:--|--:|--:|
| 1 | 1.21202033 ± 0.00227000 | 1.18553349 ± 0.00222190 |
| 2 | 1.20649799 ± 0.00226069 | 1.18447497 ± 0.00222453 |
| 3 | 1.20787548 ± 0.00226229 | 1.18355677 ± 0.00222214 |
| 4 | 1.21049371 ± 0.00226972 | 1.18712935 ± 0.00222848 |
| 5 | 1.20724179 ± 0.00226806 | 1.18086942 ± 0.00221935 |
| 6 | 1.20839349 ± 0.00226356 | 1.18171744 ± 0.00221351 |
| 7 | 1.20741334 ± 0.00226387 | 1.18313378 ± 0.00221881 |
| 8 | 1.20661368 ± 0.00225946 | 1.18681247 ± 0.00222704 |
| 9 | 1.20582599 ± 0.00226750 | 1.18133630 ± 0.00222040 |
| 10 | 1.20796707 ± 0.00226470 | 1.18704863 ± 0.00222221 |
| **All subsamples** | **1.20803429 ± 0.00189633** | **1.18416126 ± 0.00241216** |

*Table: Particle averages are counts per event. Individual rows show mean ± standard error; the last row shows the arithmetic mean ± sample standard deviation of the ten subsample means.*

**Average difference (positive minus negative):** 0.02387302 particles/event  
**Difference uncertainty (SD across subsamples):** 0.00237277 particles/event  
**Sigma score:** 10.06σ  
**Interpretation:** A difference at or above 3σ under the class's spread-based convention.

![Momentum-dependent count difference for IDs 2212 and -2212](figures/asymmetry_2212.png)

*Figure: Frequency difference between 2212 and -2212 in each momentum bin, averaged over ten subsamples. Error bars show the sample SD across the ten subsamples; the dashed line marks zero difference.*

### Pair 3122 and -3122: Methane / Methyl ion

| Subsample | ID 3122: average ± uncertainty | ID -3122: average ± uncertainty |
|:--|--:|--:|
| 1 | 0.27806308 ± 0.00085775 | 0.27343237 ± 0.00084936 |
| 2 | 0.27757749 ± 0.00085998 | 0.27280089 ± 0.00084740 |
| 3 | 0.27645393 ± 0.00085493 | 0.27144160 ± 0.00084514 |
| 4 | 0.27756311 ± 0.00085955 | 0.27160668 ± 0.00084471 |
| 5 | 0.27626682 ± 0.00085863 | 0.27145353 ± 0.00084487 |
| 6 | 0.27661923 ± 0.00085662 | 0.27185325 ± 0.00084579 |
| 7 | 0.27482625 ± 0.00085298 | 0.27114340 ± 0.00084601 |
| 8 | 0.27609111 ± 0.00085466 | 0.27061579 ± 0.00084250 |
| 9 | 0.27512250 ± 0.00085224 | 0.27017260 ± 0.00084376 |
| 10 | 0.27740279 ± 0.00085797 | 0.27244016 ± 0.00084780 |
| **All subsamples** | **0.27659863 ± 0.00107440** | **0.27169603 ± 0.00098538** |

*Table: Particle averages are counts per event. Individual rows show mean ± standard error; the last row shows the arithmetic mean ± sample standard deviation of the ten subsample means.*

**Average difference (positive minus negative):** 0.00490260 particles/event  
**Difference uncertainty (SD across subsamples):** 0.00058316 particles/event  
**Sigma score:** 8.41σ  
**Interpretation:** A difference at or above 3σ under the class's spread-based convention.

![Momentum-dependent count difference for IDs 3122 and -3122](figures/asymmetry_3122.png)

*Figure: Frequency difference between 3122 and -3122 in each momentum bin, averaged over ten subsamples. Error bars show the sample SD across the ten subsamples; the dashed line marks zero difference.*

### Pair 3312 and -3312: Ethylene / Ionised ethylene

| Subsample | ID 3312: average ± uncertainty | ID -3312: average ± uncertainty |
|:--|--:|--:|
| 1 | 0.03927217 ± 0.00029688 | 0.03964904 ± 0.00029781 |
| 2 | 0.03935821 ± 0.00029647 | 0.03932140 ± 0.00029662 |
| 3 | 0.03978027 ± 0.00029778 | 0.03918243 ± 0.00029523 |
| 4 | 0.03967198 ± 0.00029777 | 0.03868430 ± 0.00029402 |
| 5 | 0.03961269 ± 0.00029773 | 0.03853224 ± 0.00029347 |
| 6 | 0.03888751 ± 0.00029506 | 0.03883123 ± 0.00029449 |
| 7 | 0.03925130 ± 0.00029610 | 0.03888540 ± 0.00029483 |
| 8 | 0.03943138 ± 0.00029714 | 0.03839001 ± 0.00029258 |
| 9 | 0.03933508 ± 0.00029597 | 0.03914669 ± 0.00029586 |
| 10 | 0.03981155 ± 0.00029749 | 0.03938265 ± 0.00029747 |
| **All subsamples** | **0.03944121 ± 0.00028368** | **0.03900054 ± 0.00040248** |

*Table: Particle averages are counts per event. Individual rows show mean ± standard error; the last row shows the arithmetic mean ± sample standard deviation of the ten subsample means.*

**Average difference (positive minus negative):** 0.00044067 particles/event  
**Difference uncertainty (SD across subsamples):** 0.00048793 particles/event  
**Sigma score:** 0.90σ  
**Interpretation:** No clear asymmetry under the class's 2σ comparison convention.

![Momentum-dependent count difference for IDs 3312 and -3312](figures/asymmetry_3312.png)

*Figure: Frequency difference between 3312 and -3312 in each momentum bin, averaged over ten subsamples. Error bars show the sample SD across the ten subsamples; the dashed line marks zero difference.*

### Pair 3334 and -3334: Ozone / Superoxide anion

| Subsample | ID 3334: average ± uncertainty | ID -3334: average ± uncertainty |
|:--|--:|--:|
| 1 | 0.00128655 ± 0.00005284 | 0.00117825 ± 0.00005049 |
| 2 | 0.00117358 ± 0.00005057 | 0.00112161 ± 0.00004925 |
| 3 | 0.00115669 ± 0.00005003 | 0.00120435 ± 0.00005104 |
| 4 | 0.00117612 ± 0.00005072 | 0.00112631 ± 0.00004936 |
| 5 | 0.00118871 ± 0.00005098 | 0.00123634 ± 0.00005171 |
| 6 | 0.00112764 ± 0.00004938 | 0.00117743 ± 0.00005064 |
| 7 | 0.00119081 ± 0.00005084 | 0.00106957 ± 0.00004829 |
| 8 | 0.00120375 ± 0.00005111 | 0.00111498 ± 0.00004920 |
| 9 | 0.00120175 ± 0.00005107 | 0.00111081 ± 0.00004902 |
| 10 | 0.00116539 ± 0.00005021 | 0.00117622 ± 0.00005054 |
| **All subsamples** | **0.00118710 ± 0.00004168** | **0.00115159 ± 0.00005079** |

*Table: Particle averages are counts per event. Individual rows show mean ± standard error; the last row shows the arithmetic mean ± sample standard deviation of the ten subsample means.*

**Average difference (positive minus negative):** 0.00003551 particles/event  
**Difference uncertainty (SD across subsamples):** 0.00006854 particles/event  
**Sigma score:** 0.52σ  
**Interpretation:** No clear asymmetry under the class's 2σ comparison convention.

![Momentum-dependent count difference for IDs 3334 and -3334](figures/asymmetry_3334.png)

*Figure: Frequency difference between 3334 and -3334 in each momentum bin, averaged over ten subsamples. Error bars show the sample SD across the ten subsamples; the dashed line marks zero difference.*

## Conclusion

Under the course's 2σ spread-based comparison, the pairs at or above 2σ are: 211/-211 (7.15σ), 2212/-2212 (10.06σ), 3122/-3122 (8.41σ).
The momentum-dependent plots should also be inspected for bins whose error bars exclude zero. Because many momentum bins are examined, isolated departures should be interpreted cautiously; they are not automatically proof of a physical asymmetry.

## Reproducing the analysis

Run `generate_asymmetry_readme.py` with the original 10 subsample files. Install `numpy` and `matplotlib` first. The raw simulation files need not be committed to GitHub.

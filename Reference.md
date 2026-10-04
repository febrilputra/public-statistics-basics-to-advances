# References and reading connections

This course uses the sources below for its learning sequence, statistical definitions, inference conventions, and software APIs. Explanations, examples, synthetic datasets, exercises, code, and generated figures were written for this repository. Source books and their artwork are not part of the course distribution. Website references were consulted on 4 October 2026; software is pinned separately in [requirements.txt](requirements.txt).

## SQ: StatQuest

Starmer, Josh. (2026). *The StatQuest Illustrated Guide to Statistics*. StatQuest. Primary reading: the locally supplied edition, including Chapters 1–11 and Appendices A–F. [Official author and purchase page](https://statquest.org/statquest-store/).

The repository follows this subject order, but uses its own prose, examples, illustrations, and code. It is an independent learning companion and is not affiliated with or endorsed by StatQuest or Josh Starmer. The local reading PDFs are excluded from the distributed course.

| Repository chapter | Reading connection | Additional development in these notes |
|---|---|---|
| 00 | Front matter and Chapter 1 | Estimands, measurement design, random sampling versus assignment |
| 01 | Fundamental statistical concepts | Unbiased-variance derivation, Monte Carlo comparison, finite populations |
| 02 | Histograms and probabilities | Unequal-width density bins, ECDF, unobserved-event uncertainty |
| 03 | Distributions and models | PMF/PDF/CDF distinctions, joint log-likelihood, discrete and continuous examples |
| 04 | Hypothesis testing and null hypotheses | Exact randomization under a sharp null and exchangeability |
| 05 | P-values | Exact discrete calibration, direction selection, confidence-interval coverage |
| 06 | Linear regression | Explicit assumptions, confidence versus prediction intervals, residual diagnostics |
| 07 | Multiple regression | Matrix rank, interactions, collinearity, held-out prediction error |
| 08 | t-tests | Welch and paired designs, intervals, pooled-regression equivalence |
| 09 | Power and power analysis | Noncentral-t verification, sensitivity analysis, simulated power |
| 10 | P-value pitfalls | FWER versus FDR, Holm and BH, repeated-look simulation |
| 11 | ANOVA and ANCOVA | Simultaneous intervals, partial model comparisons, interactions and overlap |
| AA | Appendices A–F | Bayes' rule, covariance, CLT, matrix notation, reproducible Python |

The reference sequence is a study aid, not a claim that every extension appears in the book. Where simplified intuitions require qualifications, the notes state the formal conditions directly—for example, likelihood products, the interpretation of p-values, and common-variance versus Welch tests.

## Definitions, estimation, and linear models

NIST/SEMATECH. *e-Handbook of Statistical Methods*. National Institute of Standards and Technology. Relevant sections:

- [Measures of scale](https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm): variance, standard deviation, and other measures of spread; Chapter 01.
- [Histogram](https://www.itl.nist.gov/div898/handbook/eda/section3/histogra.htm): distributional exploration; Chapter 02.
- [Maximum likelihood](https://www.itl.nist.gov/div898/handbook/apr/section4/apr412.htm): likelihood construction and estimation; Chapter 03.
- [Confidence limits for the mean](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm): t-based intervals; Chapters 01, 05, and 08.
- [Linear least squares regression](https://www.itl.nist.gov/div898/handbook/pmd/section1/pmd141.htm): fitting and regression interpretation; Chapters 06, 07, and AA.
- [Assumptions for statistical tests](https://www.itl.nist.gov/div898/handbook/pri/section2/pri245.htm): distributional conditions and residual checks; Chapters 06–11.
- [Two-sample t-test](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm): pooled and unequal-variance formulas; Chapter 08.
- [One-way analysis of variance](https://www.itl.nist.gov/div898/handbook/eda/section3/eda354.htm): sums of squares, degrees of freedom, and the F-test; Chapter 11.

## P-values and interpretation

Wasserstein, R. L., & Lazar, N. A. (2016). The ASA's statement on p-values: Context, process, and purpose. *The American Statistician, 70*(2), 129–133. [DOI: 10.1080/00031305.2016.1154108](https://doi.org/10.1080/00031305.2016.1154108). The American Statistical Association also provides an accessible [statement and summary of its principles](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf).

This informs Chapters 04, 05, and 10: interpretation depends on the model and analysis process; statistical significance does not measure effect magnitude; conclusions should not rest on a threshold alone.

## Multiple testing

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics, 6*(2), 65–70. [Original publication](https://www.jstor.org/stable/4615733). Chapter 10 implements the ordered step-down adjustment and checks it against statsmodels.

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B (Methodological), 57*(1), 289–300. [DOI: 10.1111/j.2517-6161.1995.tb02031.x](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x). Chapter 10 develops the false discovery rate and the independent-test BH procedure, with a simulation that records the realized false-discovery proportion in each family.

The notes distinguish the independence setting of the original BH result from extensions requiring specific dependence conditions. Correlation alone is not a sufficient justification for applying an independence-based guarantee.

## Software documentation

These are the primary documentation pages for the functions used in the notebooks. Stable documentation can evolve independently of the pinned environment; the executable labs are the record of the calls actually validated here.

| Package and documentation | Used for |
|---|---|
| [NumPy histogram](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html) | Bin-edge conventions and density normalization |
| [NumPy least squares](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html) | Matrix fitting, rank, and coefficient checks |
| [SciPy statistical functions](https://docs.scipy.org/doc/scipy/reference/stats.html) | Distributions, densities, quantiles, and survival functions |
| [SciPy binomtest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html) | Exact two-sided binomial convention |
| [SciPy permutation_test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html) | Resampling nulls and conventions |
| [SciPy ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html) | Welch and pooled independent-sample tests |
| [SciPy ttest_rel](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html) | Paired comparisons |
| [SciPy noncentral t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nct.html) | Power under a nonzero standardized effect |
| [statsmodels TTestIndPower](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.html) | Sample-size and power calculations |
| [statsmodels multipletests](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html) | Bonferroni, Holm, BH, and related adjustments |
| [statsmodels compare_f_test](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.compare_f_test.html) | Nested regression comparisons |
| [statsmodels ANOVA](https://www.statsmodels.org/stable/generated/statsmodels.stats.anova.anova_lm.html) | Linear-model ANOVA tables |
| [statsmodels Tukey HSD](https://www.statsmodels.org/stable/generated/statsmodels.stats.multicomp.pairwise_tukeyhsd.html) | All-pairs simultaneous comparisons |

## Source handling and publication

U.S. Copyright Office. [Fair-use and permission questions](https://www.copyright.gov/help/faq/faq-fairuse.html). This is a general reference for the distinction between attribution and permission; it does not provide clearance for this repository or determine which country's law applies. See [Publication notes](PUBLICATION.md) for the concrete source-handling decisions in this project.

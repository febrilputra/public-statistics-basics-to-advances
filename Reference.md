# References and reading connections

This course uses the sources below for its learning sequence, statistical definitions, inference conventions, and software APIs. It has two primary sources:

| Part | Primary source | Section below |
|---|---|---|
| Chapters 1–13 (basics) | The Organic Chemistry Tutor, *Statistics* video course | [OCT](#oct-the-organic-chemistry-tutor) |
| Chapters 14–18 (advanced) and the archived chapters in `old_chapters/` | Josh Starmer, *The StatQuest Illustrated Guide to Statistics* | [SQ](#sq-statquest) |

All prose is written in my own words. In Chapters 1–13 the worked examples follow the examples solved in each video, with every calculation re-checked. In Chapters 14–18 the examples, made-up datasets, exercises and figure code were written for this repository. Videos, source books and their artwork are not part of the course distribution. StatQuest-related website references were consulted on 4 October 2026; software is pinned separately in [requirements.txt](requirements.txt).

## OCT: The Organic Chemistry Tutor

The Organic Chemistry Tutor. *Statistics* (video course). [video-tutor.net/statistic.html](https://www.video-tutor.net/statistic.html); videos hosted on YouTube.

Chapters 1–13 are personal study notes on this course: one Markdown note per video (87 lessons), named `chapter-lesson-title.md`. The header of every note links to its original video and to the chapter page below. The notes explain the concepts, formulas and worked examples in my own words, re-check every calculation, and say so where a video contains a slip, giving the corrected value. Figures, `pdf_version/` exports and `handwritten_note/` PDFs were made for these notes.

The videos and the website belong to The Organic Chemistry Tutor. These notes are an independent study companion and are not affiliated with or endorsed by The Organic Chemistry Tutor. Watch the original videos for the full explanations.

| Repository chapter | Course chapter page | Lessons |
|---|---|---:|
| 01 | [Introduction to Statistics](https://www.video-tutor.net/introduction-to-statistics.html) | 5 |
| 02 | [Graphs and Tables](https://www.video-tutor.net/graphs-and-tables.html) | 9 |
| 03 | [Central Tendency and Variation](https://www.video-tutor.net/central-tendency-and-variation.html) | 19 |
| 04 | [Measures of Position](https://www.video-tutor.net/measures-of-position.html) | 5 |
| 05 | [Introduction to Probability](https://www.video-tutor.net/introduction-to-probability.html) | 11 |
| 06 | [Discrete Probability Distributions](https://www.video-tutor.net/discrete-probability-distributions.html) | 5 |
| 07 | [Continuous Probability Distributions](https://www.video-tutor.net/continuous-probability-distributions.html) | 4 |
| 08 | [Normal Probability Distributions](https://www.video-tutor.net/normal-probability-distributions.html) | 5 |
| 09 | [Confidence Intervals](https://www.video-tutor.net/confidence-intervals.html) | 6 |
| 10 | [Hypothesis Testing with One Sample](https://www.video-tutor.net/hypothesis-testing-with-one-sample.html) | 7 |
| 11 | [Hypothesis Testing with Two Samples](https://www.video-tutor.net/hypothesis-testing-with-two-samples.html) | 4 |
| 12 | [Chi-Square Distributions](https://www.video-tutor.net/chi-square-distributions.html) | 3 |
| 13 | [Linear Regression and Correlation](https://www.video-tutor.net/linear-regression.html) | 4 |

## SQ: StatQuest

Starmer, Josh. (2026). *The StatQuest Illustrated Guide to Statistics*. StatQuest. Primary reading: the locally supplied edition, including Chapters 1–11 and Appendices A–F. [Official author and purchase page](https://statquest.org/statquest-store/).

Chapters 14–18 and the archived chapters follow this subject order, but use their own prose, examples, illustrations, and code. They are an independent learning companion and are not affiliated with or endorsed by StatQuest or Josh Starmer. The local reading PDFs are excluded from the distributed course.

| Repository chapter | Reading connection | Additional development in these notes |
|---|---|---|
| archived 00 | Front matter and Chapter 1 | Estimands, measurement design, random sampling versus assignment |
| archived 01 | Fundamental statistical concepts | Unbiased-variance derivation, Monte Carlo comparison, finite populations |
| archived 02 | Histograms and probabilities | Unequal-width density bins, ECDF, unobserved-event uncertainty |
| archived 03 | Distributions and models | PMF/PDF/CDF distinctions, joint log-likelihood, discrete and continuous examples |
| archived 04 | Hypothesis testing and null hypotheses | Exact randomization under a sharp null and exchangeability |
| archived 05 | P-values | Exact discrete calibration, direction selection, confidence-interval coverage |
| archived 06 | Linear regression | Explicit assumptions, confidence versus prediction intervals, residual diagnostics |
| 14 | Chapter 7: Multiple regression | Dummy variables, interactions, nested F-tests, overfitting, collinearity and VIF |
| archived 08 | t-tests | Welch and paired designs, intervals, pooled-regression equivalence |
| 15 | Chapter 9: Power and power analysis | Effect size, exact t-test sample size, sensitivity, simulated power |
| 16 | Chapter 10: P-value pitfalls | FWER versus FDR, Bonferroni, Holm and BH, optional stopping, winner's curse |
| 17 | Chapter 11: ANOVA and ANCOVA | Effect sizes, Tukey and Holm comparisons, partial model comparisons, interactions and overlap |
| 18 | Appendices A–F | Bayes' rule, covariance, CLT, derivatives, matrix notation, reproducible Python |

The reference sequence is a study aid, not a claim that every extension appears in the book. Where simplified intuitions require qualifications, the notes state the formal conditions directly—for example, likelihood products, the interpretation of p-values, and common-variance versus Welch tests.

## Definitions, estimation, and linear models

NIST/SEMATECH. *e-Handbook of Statistical Methods*. National Institute of Standards and Technology. Relevant sections:

- [Measures of scale](https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm): variance, standard deviation, and other measures of spread; archived Chapter 01.
- [Histogram](https://www.itl.nist.gov/div898/handbook/eda/section3/histogra.htm): distributional exploration; archived Chapter 02.
- [Maximum likelihood](https://www.itl.nist.gov/div898/handbook/apr/section4/apr412.htm): likelihood construction and estimation; archived Chapter 03.
- [Confidence limits for the mean](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm): t-based intervals; archived Chapters 01, 05, and 08.
- [Linear least squares regression](https://www.itl.nist.gov/div898/handbook/pmd/section1/pmd141.htm): fitting and regression interpretation; archived Chapter 06, Chapters 14 and 18.
- [Assumptions for statistical tests](https://www.itl.nist.gov/div898/handbook/pri/section2/pri245.htm): distributional conditions and residual checks; Chapters 14–17.
- [Two-sample t-test](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm): pooled and unequal-variance formulas; archived Chapter 08.
- [One-way analysis of variance](https://www.itl.nist.gov/div898/handbook/eda/section3/eda354.htm): sums of squares, degrees of freedom, and the F-test; Chapter 17.

## P-values and interpretation

Wasserstein, R. L., & Lazar, N. A. (2016). The ASA's statement on p-values: Context, process, and purpose. *The American Statistician, 70*(2), 129–133. [DOI: 10.1080/00031305.2016.1154108](https://doi.org/10.1080/00031305.2016.1154108). The American Statistical Association also provides an accessible [statement and summary of its principles](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf).

This informs archived Chapters 04 and 05 and Chapter 16: interpretation depends on the model and analysis process; statistical significance does not measure effect magnitude; conclusions should not rest on a threshold alone.

## Multiple testing

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics, 6*(2), 65–70. [Original publication](https://www.jstor.org/stable/4615733). Lesson 16.3 works through the ordered step-down adjustment.

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B (Methodological), 57*(1), 289–300. [DOI: 10.1111/j.2517-6161.1995.tb02031.x](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x). Lessons 16.2 and 16.4 develop the false discovery rate and the independent-test BH procedure, with a simulation that records the realized false-discovery proportion in each family.

The notes distinguish the independence setting of the original BH result from extensions requiring specific dependence conditions. Correlation alone is not a sufficient justification for applying an independence-based guarantee.

## Software documentation

These are the primary documentation pages for the functions used in the figure scripts (`figures/make_figures.py` in Chapters 14–18) and in the archived notebooks. Stable documentation can evolve independently of the pinned environment.

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

# 08 · t-tests for means and differences

A t-test compares an estimated mean or mean difference with a hypothesized value, measured in estimated standard errors. The right version depends on the design: one sample, two independent samples, or paired observations.

```mermaid
flowchart TD
    A[Identify independent units] --> B{What comparison?}
    B --> C[One sample against a target]
    B --> D[Two independent groups]
    B --> E[Paired measurements]
    D --> F[Welch or justified pooled variance]
    C --> G[Effect, SE, t, df, interval]
    E --> G
    F --> G
    G --> H[Interpret with assumptions]
```

**Learning route:** t distribution → choose design → calculate → connect to regression → report. Prerequisites: [p-values and intervals](../05_P-Values_for_Confidence_Quantification/05_P-Values_for_Confidence_Quantification.md); the regression connection uses Chapters 6–7.

## 1. Why use a t distribution?

For iid normal observations, if $\sigma$ were known, $(\bar X-\mu)/(\sigma/\sqrt n)$ would be standard normal. Usually $\sigma$ is unknown, so we substitute $S$. That estimated denominator introduces additional uncertainty:

$$T=\frac{\bar X-\mu}{S/\sqrt n}\sim t_{n-1}.$$

A t distribution is symmetric with heavier tails than a standard normal. Its shape depends on degrees of freedom. As degrees of freedom increase, it approaches normal gradually; there is no magic sample size at which they become identical. Heavy tails reflect uncertainty in standardizing the statistic, not a claim that every raw dataset is t distributed.

![Normal and t densities](figure/t_distributions.png)

<!-- lab: t_distributions -->

## 2. One-sample t-test

To test $H_0:\mu=\mu_0$, calculate

$$t=\frac{\bar x-\mu_0}{s/\sqrt n},\qquad df=n-1.$$

For a two-sided alternative, $p=2P(t_{df}\ge|t|)$. The corresponding interval is $\bar x\pm t_{1-\alpha/2,df}s/\sqrt n$. A one-sided test uses the appropriate tail chosen beforehand.

For invented filling volumes 48, 49, 50, 51, 52 mL, the mean is 50 and sample variance is 2.5. Testing a target of 49 mL gives $t=(50-49)/\sqrt{2.5/5}=\sqrt2$, with four degrees of freedom. The notebook computes its p-value and interval. The mean differs descriptively from the target; whether it is well distinguished from the target depends on uncertainty.

<!-- lab: one_sample -->

## 3. Independent groups: Welch's t-test

For independent samples A and B, define $\Delta=\mu_B-\mu_A$. With possibly different population variances, the estimated standard error is

$$SE=\sqrt{\frac{s_B^2}{n_B}+\frac{s_A^2}{n_A}},\qquad
t=\frac{(\bar x_B-\bar x_A)-\Delta_0}{SE}.$$

Welch's approximate degrees of freedom are

$$\nu=\frac{(s_B^2/n_B+s_A^2/n_A)^2}
{(s_B^2/n_B)^2/(n_B-1)+(s_A^2/n_A)^2/(n_A-1)}.$$

Fractional degrees of freedom are normal here. The Welch–Satterthwaite approximation accounts for uncertainty from estimating two variances. Welch's method does not require equal variances and is a sensible starting choice for two independent means when equal variance is not justified. It still requires appropriate independent sampling and is not immune to severe skewness or influential observations in small samples.

### Worked example: two preparation processes

Use independent invented times, in minutes:

| Process | Times | $n$ | Mean | Sample variance |
|---|---|---:|---:|---:|
| A | 15, 17, 18, 19, 21 | 5 | 18 | 5 |
| B | 12, 13, 14, 16, 20, 21 | 6 | 16 | 14 |

For $H_0:\Delta=0$, the effect estimate is $16-18=-2$ minutes. The SE is $\sqrt{14/6+5/5}=\sqrt{10/3}\approx1.826$, and $t\approx-1.095$. Welch degrees of freedom are approximately 8.299. The two-sided p-value is about 0.30; the interval includes zero and potentially meaningful effects in either direction. This is insufficient precision to claim equality or an established improvement.

![Independent process times and an interval for the mean difference](figure/welch_comparison.png)

<!-- lab: welch -->

Report the effect and interval even when the p-value is large. Reporting only “not significant” discards useful information about magnitude and precision.

## 4. Equal-variance Student test and its regression connection

If a common population variance is justified, pool the within-group information:

$$s_p^2=\frac{(n_A-1)s_A^2+(n_B-1)s_B^2}{n_A+n_B-2},$$

$$t=\frac{(\bar x_B-\bar x_A)-\Delta_0}
{s_p\sqrt{1/n_A+1/n_B}},\qquad df=n_A+n_B-2.$$

For our example, $s_p^2=10$. This is a weighted average of variances, not an unweighted average of SDs. Equal sample sizes do not establish equal population variances. Choosing between pooled and Welch tests solely by first testing variance equality can make the overall procedure harder to interpret; state the variance model directly.

Regress all observations on an intercept and indicator $z=1$ for B, $z=0$ for A. The intercept estimates A's mean and the indicator coefficient estimates B minus A. Under ordinary homoscedastic OLS, the indicator's t-test equals the **pooled** two-sample t-test, and the one-degree-of-freedom F-test equals $t^2$.

This equivalence does not generally turn the ordinary OLS F-test into Welch's test. Welch uses a different variance estimate and degrees-of-freedom approximation. In both cases, the direction of a contrast is lost when squaring its t statistic; retain the signed effect in the report.

<!-- lab: regression_equivalence -->

## 5. Paired observations: analyze differences within pairs

When the same device is measured before and after a setting change, the measurements are paired. Let $d_i=\text{after}_i-\text{before}_i$. Test the mean difference with a one-sample t-test:

$$t=\frac{\bar d-\Delta_0}{s_d/\sqrt n},\qquad df=n-1,$$

where $n$ is the number of independent pairs. The relevant normality assumption for an exact small-sample test concerns the **differences**, not the separate before and after distributions.

Consider before times $(40,50,60,70,80)$ and after times $(38,47,59,66,78)$ seconds for five devices. Differences are $(-2,-3,-1,-4,-2)$, with mean $-2.4$ and sample variance 1.3. Their SE is $\sqrt{1.3/5}\approx0.510$, much smaller than the spread of the raw device times.

![Paired observations preserve the within-device comparison](figure/paired_times.png)

<!-- lab: paired -->

Pairing works because $\operatorname{Var}(A-B)=\operatorname{Var}(A)+\operatorname{Var}(B)-2\operatorname{Cov}(A,B)$. Positive within-pair association can reduce difference variability. Arbitrary pairing after seeing the data is not a valid way to obtain this advantage. Pairing must come from the design, and missing one measurement can remove an entire pair from a complete-pair analysis.

## 6. Assumptions, alternatives, and effect sizes

Independence cannot be established by a normality test. Repeated observations, matched observations, and cluster assignments require their respective designs to be represented in the analysis. Large independent samples can make mean-based inference approximately valid under suitable moment conditions, but severe heavy tails or influential points can still matter.

If assumptions are implausible, consider a justified transformation, robust estimation, a design-respecting randomization test, or a suitable distributional model. Rank tests are not automatic replacements for tests of mean differences: their hypotheses and interpretation differ.

An unstandardized mean difference keeps the measurement units. Cohen's $d$ divides a difference by a specified SD, often the pooled SD for independent groups. For paired designs, different standardized effect definitions use different denominators; name the convention. Hedges' correction can reduce small-sample bias in standardized effects. None of these replaces an interval or a meaningful practical threshold.

## 7. Practice

1. Six independent pairs have differences 1, 2, 2, 3, 3, 1. Find the mean difference, its SE, t for zero difference, and degrees of freedom.
2. An unpaired study has $n_A=10,n_B=20,s_A^2=9,s_B^2=16$. Find the Welch SE. Can you use $df=28$ automatically?
3. A student passes paired before and after data to `ttest_ind`. Why might the result be inefficient or inappropriate?
4. When does $F=t^2$ give the same two-sided inference for a group difference?
5. Why should a mean difference and interval be reported even if $p>0.05$?

## 8. Worked answers

1. $\bar d=2$, squared deviations sum to 4, so $s_d^2=4/5=0.8$, $SE=\sqrt{0.8/6}\approx0.3651$, $t=\sqrt{30}\approx5.477$, and $df=5$.
2. $SE=\sqrt{9/10+16/20}=\sqrt{1.7}\approx1.3038$. No: Welch uses its approximate df formula, here about 23.37.
3. The independent-sample formula discards the paired covariance and does not represent the actual sampling structure. Use differences or an appropriate paired model.
4. For the same one-degree-of-freedom contrast and variance model, such as a pooled two-sample t-test and ordinary two-group homoscedastic regression.
5. They show which effect magnitudes remain plausible under the model; a threshold label alone does not.

<!-- lab: practice -->

## References and next step

Reading connection: Starmer (2026), Chapter 8, [SQ](../Reference.md#sq-statquest). Welch and paired extensions: [NIST two-sample t-test](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm). API choices: [SciPy ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html) and [ttest_rel](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html).

Next: [09 · Power and sample size](../09_Power_and_Power_Analysis/09_Power_and_Power_Analysis.md).

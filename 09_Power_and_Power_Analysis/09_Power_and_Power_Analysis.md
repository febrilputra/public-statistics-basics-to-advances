# 09 · Power and planning sample size

Power is the probability that a specified test will detect a specified effect under a specified design. Planning sample size means choosing the precision and detection capability needed before collecting data, while acknowledging uncertainty in the planning assumptions.

```mermaid
flowchart LR
    A[Choose meaningful effect] --> B[Specify variability and design]
    B --> C[Set alpha and desired power]
    C --> D[Solve for sample size]
    D --> E[Round and allow for losses]
    E --> F[Check sensitivity and simulate]
```

**Learning route:** error rates → sampling separation → effect size → power calculation → sensitivity. Prerequisites: [t-tests](../08_T-test_for_Testing_the_Differences/08_T-test_for_Testing_the_Differences.md).

## 1. Power is conditional, not a guarantee

For a rejection rule $R$ and true effect $\Delta$, define

$$\operatorname{Power}(\Delta)=P_{\Delta}(R),\qquad
\beta(\Delta)=1-\operatorname{Power}(\Delta).$$

At a nonzero alternative, rejection is a correct detection, also called a true positive. At the null, the rejection probability is the test's size, bounded by its level $\alpha$ when the test is valid. Thus a power curve can be defined at zero too, but that point represents false-positive probability, not useful detection.

An 80%-power design at an effect of two minutes means that, under that effect and the other assumptions, about 80% of repeated studies reject. It does not mean an 80% chance that the treatment works, that the observed result will be correct, or that every nonzero effect will be detected.

## 2. Why more independent observations help

For independent groups with common SD $\sigma$ and equal size $n$ per group, the difference in sample means has

$$E[\bar X_B-\bar X_A]=\Delta,\qquad
SE=\sigma\sqrt{2/n}.$$

The null sampling distribution is centered at zero. Under a positive alternative it is centered at $\Delta$. Increasing $n$ narrows both distributions while their centers stay the same. More of the alternative distribution then lies beyond a preplanned null cutoff.

For a known-SD normal test, let $\lambda=\Delta/[\sigma\sqrt{2/n}]$. The standardized statistic has distribution $N(\lambda,1)$ under the alternative, while the two-sided rejection region is $|Z|>z_{1-\alpha/2}$. Power is

$$\Phi(-z_{1-\alpha/2}-\lambda)
+1-\Phi(z_{1-\alpha/2}-\lambda).$$

![Null and alternative sampling distributions with rejection regions](figure/power_geometry.png)

<!-- lab: power_geometry -->

The graph uses the **distribution of a mean difference**, not the overlap of individual observations. Individual distributions may overlap extensively while a large study estimates their means precisely. More dependent repetitions do not necessarily provide the same gain as more independent units.

## 3. Choose an effect worth detecting

Suppose a workshop considers a process change worthwhile if it saves at least **two minutes** on average. Prior process knowledge suggests a common SD of **four minutes**. For equal-variance independent groups, the standardized effect magnitude is

$$d=\frac{|\Delta|}{\sigma}=\frac24=0.5.$$

This is a planning value, not an effect discovered in the current study. Use the smallest effect of practical interest, informed by the decision and credible prior data. Choosing an optimistic pilot estimate can badly underpower a later study. Generic labels such as “small” and “large” do not decide what matters for a particular workshop.

A signed Cohen's $d$ is useful when reporting direction. The magnitude is sufficient for a two-sided power calculation. Specify the denominator convention; paired standardized changes and independent-group pooled-SD effects are not interchangeable.

## 4. Calculate sample size for the planned test

An approximate known-SD, balanced, two-sided design uses

$$n\approx\frac{2(z_{1-\alpha/2}+z_{1-\beta})^2}{d^2}.$$

At $\alpha=0.05$, power 0.80, and $d=0.5$, this is about 62.79 observations **per group**, before rounding. The expression approximates power by emphasizing the main rejection tail under a directional effect; it is useful for intuition and initial planning, not a replacement for the appropriate test calculation.

For the pooled two-sample t-test, use the noncentral t distribution. With equal group sizes,

$$df=2n-2,\qquad \lambda=d\sqrt{n/2},\qquad
c=t_{1-\alpha/2,df},$$

$$\operatorname{Power}=P(t_{df,\lambda}<-c)+P(t_{df,\lambda}>c).$$

The cutoff comes from the **central** null t distribution, while rejection probability under the alternative comes from the **noncentral** distribution. The notebook solves this numerically with statsmodels and independently checks the result with SciPy's noncentral t CDF and survival function.

The result is about **63.77 per group**. Round up to **64 per group, 128 total**, and recompute the achieved power, about 0.8015. Rounding down would miss the target. If 20% of recruited units are expected to be unusable for a reason accounted for in the design, start with $\lceil64/(1-0.20)\rceil=80$ per group. This numerical allowance does not solve bias from outcome-dependent missingness.

<!-- lab: sample_size -->

This calculation assumes independent observations, common normal error variance, equal allocation, a two-sided pooled test, and one planned comparison. A Welch design with unequal variances, a paired design, a cluster trial, or a multiple-testing procedure needs a matching power calculation or simulation.

## 5. A sensitivity analysis is part of the answer

Planning inputs are uncertain. Calculate several plausible effect sizes and SDs, not just one convenient number. The notebook displays sample sizes for several $d$ values and compares 80% with 90% desired power.

![Power curves for several standardized effects](figure/power_curves.png)

<!-- lab: sensitivity -->

For the same test and allocation, larger effects and lower variability generally improve power. Larger sample size improves precision. A smaller $\alpha$ makes rejection harder and reduces power at fixed $n$; maintaining power then needs more information. These are design tradeoffs, not reasons to relax the significance threshold after seeing a result.

The approximate formula shows why detecting half the effect requires about four times the sample size when SD is unchanged. Improving measurement reliability or using justified pairing/blocking can be valuable because reducing noise also reduces the information required. If cluster sizes are $m$ and within-cluster correlation is $\rho$, the rough design effect $1+(m-1)\rho$ illustrates why many measurements from few clusters can be inefficient; actual cluster designs need more careful planning.

## 6. Verify power by simulating the full procedure

The notebook simulates 10,000 independent studies under $\Delta=2$, $\sigma=4$, and $n=64$ per group. It performs the same two-sided pooled t-test that the planning calculation assumes. The rejection fraction should be near the theoretical power, within simulation error.

For $B$ repetitions and estimated power $\hat\pi$, the Monte Carlo SE is $\sqrt{\hat\pi(1-\hat\pi)/B}$. At 0.80 with 10,000 repetitions, this is about 0.004. Deviations of a few thousandths are ordinary simulation noise. This check does not validate the realism of the normal or common-variance assumptions.

<!-- lab: simulated_power -->

Simulation becomes especially useful when the real analysis includes unequal variances, clustering, missing values, or complicated decision rules. Generate data from explicit plausible scenarios and run the **entire planned analysis**, including any stopping or selection procedure.

## 7. Avoid observed-power reasoning

After a study, substituting the observed effect into the planning formula and calling the resulting number “observed power” adds little beyond the p-value and can be misleading. The observed effect is noisy, especially in small studies. Report its estimate and interval; discuss which scientifically meaningful effects the data constrain.

For a new study, revisit power using a defensible effect range and variability assumptions. A previous nonsignificant result is neither proof of zero effect nor a license to add observations until significance appears. A valid sequential design can allow repeated looks, but it must calibrate the stopping rule.

## 8. Practice

1. A meaningful change is 3 units and the common SD is 6. What standardized effect should a balanced independent-group planner use?
2. Approximately how does required $n$ change if the target effect halves while SD, power, and $\alpha$ stay fixed?
3. A calculator returns 87.2 observations per group. What is the minimum rounded total? With 15% expected loss, how many should initially be recruited per group?
4. Does 90% power mean that a significant result has a 90% chance of being true?
5. Why should a paired study not simply use an independent-group sample-size result?

## 9. Worked answers

1. $d=3/6=0.5$. Keep the 3-unit practical meaning in the report as well.
2. About four times as many per group, because the approximation is proportional to $1/d^2$.
3. Round to 88 per group, 176 total. Inflate to $\lceil88/0.85\rceil=104$ per group, or 208 initially, subject to the missingness assumptions.
4. No. Power conditions on a specified alternative being true. It is not a posterior probability for a discovered result.
5. Its information comes from within-pair differences and their SD, including covariance. Its independent unit is a pair; its test and degrees of freedom differ.

<!-- lab: practice -->

## References and next step

Reading connection: Starmer (2026), Chapter 9, [SQ](../Reference.md#sq-statquest). Power implementation: [statsmodels TTestIndPower](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.html); noncentral reference: [SciPy nct](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nct.html). The planning scenario and sensitivity analysis are original.

Next: [10 · P-value pitfalls](../10_P-Values_Pitfalls/10_P-Values_Pitfalls.md).

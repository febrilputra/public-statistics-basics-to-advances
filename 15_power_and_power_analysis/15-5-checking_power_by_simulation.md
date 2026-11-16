# Lesson 15.5 - Checking Power by Simulation (and Power Mistakes)

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 9 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 15 - Power and Power Analysis

## The big picture: if you can describe the study, you can simulate it

**1. Power is a long-run fraction, so count it.** Power = the fraction of repeated studies that reject ${\color{#0072B2}H_0}$ when the effect is real. A computer can **run the study** thousands of times with made-up data that has the planned effect, apply the real analysis each time, and count the rejections:

1. Generate data for both groups from the assumed model ($\Delta = 2$, $\sigma = 4$, $n = 64$ per group).
2. Run the planned test (pooled two-sample t-test, $\alpha = 0.05$).
3. Record whether $p < 0.05$.
4. Repeat $B = 10{,}000$ times. **Estimated power** = fraction of rejections.

![Left: a histogram of 10,000 simulated t statistics, centred near 2.8; the 80.3% beyond the cutoff 1.979 are green (significant) and the 19.7% below are light orange. Right: the running estimate of power against the number of simulated studies on a log scale, wandering at first and then settling inside a narrowing ±2 Monte Carlo SE band around the theoretical 0.8015](figures/simulated_power.png)

Left: in 80.3% of the 10,000 simulated studies the t statistic passed the cutoff. Right: the estimate jumps around for the first few hundred studies, then settles near the theoretical 0.80.

**2. A simulation has its own error.** The estimate $\hat p$ is a sample proportion (Lesson 9.4), so its standard error is

$$\text{MC SE} = \sqrt{\frac{\hat p(1 - \hat p)}{B}}$$

With $B = 10{,}000$ and $\hat p \approx 0.80$, MC SE ≈ 0.004. Our 0.803 is well within ±0.008 of the exact 0.8015.

**3. Why bother, when there's a formula?** Formulas exist only for simple designs. Simulation handles anything you can write down: unequal SDs, skewed data, clusters, missing values, several outcomes, interim looks. **Simulate the whole planned procedure**, including every rule for stopping, excluding or choosing results. The simulation is only as realistic as the model you feed it, though.

**4. Mistake 1: "observed power".** After a study, some people plug the **observed** effect back into the power formula and report the result. This adds nothing. It is just the p-value in disguise (a non-significant result always gives low "observed power"), and the observed effect is noisy. Report the **estimate and its confidence interval** instead.

**5. Mistake 2: "not significant, so no effect".** A non-significant result from a low-power study is **inconclusive**, not proof of no effect. Look at the confidence interval: does it exclude the differences that would matter?

**6. Mistake 3: "add data until it's significant".** Checking the p-value again and again while adding observations inflates false positives (Lesson 16.5). Repeated looks are fine only with a **pre-planned sequential design** that adjusts the cutoffs.

---

## Goal

Estimate power by simulation, judge the simulation's accuracy with the Monte Carlo SE, and avoid the common power mistakes.

## Formulas

$$\widehat{\text{Power}} = \frac{\#\text{ simulated studies with } p < \alpha}{B}, \qquad \text{MC SE} = \sqrt{\frac{\hat p(1 - \hat p)}{B}}$$

---

## Example

Simulate the workshop plan: $n = 64$ per group, $\sigma = 4$, $\Delta = 2$, pooled t-test at $\alpha = 0.05$.

**Step 1: run it.** In 10,000 simulated studies, 8,029 had $p < 0.05$:
$$\widehat{\text{Power}} = \frac{8029}{10000} = 0.803$$

**Step 2: simulation accuracy.**
$$\text{MC SE} = \sqrt{\frac{0.803(0.197)}{10000}} = \sqrt{0.0000158} = 0.004$$

**Step 3: compare with theory.** Exact power = 0.8015. The difference is $0.803 - 0.8015 = 0.0015$, less than half an MC SE. The simulation agrees with the calculation in Lesson 15.4.

**Step 4: the t cutoff.** With $df = 2(64) - 2 = 126$, the two-sided cutoff is $t_{0.025,126} = 1.979$ (a little more than 1.96).

**A Python sketch:**

```python
import numpy as np
from scipy import stats
rng = np.random.default_rng(2024)
a = rng.normal(0, 4, (10_000, 64))          # 10,000 studies, old process
b = rng.normal(2, 4, (10_000, 64))          # new process: true difference of 2 minutes
p = stats.ttest_ind(b, a, axis=1).pvalue
print((p < 0.05).mean())                    # about 0.80
```

---

## Doing it in Excel

`=SQRT(0.803*(1-0.803)/10000)` → 0.004 (the MC SE). Excel can simulate too, using `=NORM.INV(RAND(), 2, 4)` and *Data Table*, but it's slow for 10,000 studies.

---

## Your turn

1. Does 90% power mean that a significant result has a 90% chance of being true?
2. Why shouldn't a paired study (before/after on the same 30 machines) just use the independent-groups sample size?

**Answers:**
1. No. Power assumes the effect is real and asks how often we detect it. The probability that a significant finding is true also depends on how plausible the effect was to begin with. Power alone can't give it.
2. A paired test works with the **differences** within each pair, and their SD (which depends on how strongly before and after are correlated). The unit is the pair, so the degrees of freedom are $n_\text{pairs} - 1$. The calculation uses $d$ = mean difference / SD of differences.

---

## Key takeaways

- Power by simulation: generate data under the assumed effect, run the real analysis, count rejections.
- MC SE $= \sqrt{\hat p(1 - \hat p)/B}$, about 0.004 for $B = 10{,}000$ and $\hat p = 0.8$.
- Simulate the **entire** procedure, including any stopping or selection rules.
- "Observed power" after the fact adds nothing. Report the estimate and its confidence interval.
- A non-significant result from a low-power study is inconclusive, not evidence of no effect.

# Lesson 15.4 - Sample Size for Comparing Two Means

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 9 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 15 - Power and Power Analysis

## The big picture: from "what power do I have?" to "how many do I need?"

Lesson 9.5 found the sample size for a **confidence interval** of a given width. This lesson finds the sample size for a **test** with a given power.

**1. Turn the power formula around.** Power is 80% when the effect curve's centre sits $z_{\beta}$ standard errors beyond the cutoff (here $z_\beta = z_{0.20} = 0.842$). So we need

$$d\sqrt{\frac{n}{2}} = z_{\alpha/2} + z_{\beta}$$

Solve for $n$:

$$n \approx \frac{2\,(z_{\alpha/2} + z_{\beta})^2}{d^2} \quad \text{per group}$$

**2. Quick formula vs exact answer.** The formula above uses the normal curve. The real analysis is a **t-test**, with slightly fatter tails (Lesson 9.3). The exact answer comes from the **noncentral t distribution**, the shape of the t statistic when the effect is real. Software (G\*Power, R, Python `statsmodels`) does this calculation. For moderate effects the two answers differ by about one person per group.

**3. Always round UP.** 63.77 people means 64. Rounding down drops the power below the target.

**4. Plan for losses.** If you expect a fraction $L$ of units to drop out or be unusable, recruit

$$n_\text{recruit} = \left\lceil \frac{n}{1 - L} \right\rceil$$

This only fixes the **number**. If the people who drop out differ from those who stay, the results can still be biased.

![Left: power against n per group for d = 0.5; power reaches 0.80 at exactly 63.77, n = 63 gives 0.795 (too low) and n = 64 gives 0.801. Right: four boxes: 1, approximate formula gives 62.79; 2, exact t-test calculation gives 63.77; 3, round up to 64 per group, 128 in total, power 0.8015; 4, allow for 20% dropout, 64/0.8 = 80 per group to recruit](figures/sample_size_steps.png)

Left: the exact power curve crosses 80% between 63 and 64 per group, so 64 is the answer. Right: the planning steps, from the quick formula to the number to recruit.

**5. Check the assumptions.** This calculation assumes independent observations, the same SD in both groups, equal group sizes, a two-sided pooled t-test and **one** planned comparison. Unequal variances (Welch), paired data, clusters, or several tests (Chapter 16) each need their own calculation, often done by simulation (Lesson 15.5).

---

## Goal

Calculate the sample size per group for a two-sample t-test with a chosen power, and adjust it for dropout.

## Formulas

$$n \approx \frac{2\,(z_{\alpha/2} + z_{\beta})^2}{d^2} \quad \text{per group}, \qquad n_\text{recruit} = \left\lceil \frac{n}{1 - L}\right\rceil$$

| Power | $\beta$ | $z_\beta$ |
|---:|---:|---:|
| 80% | 0.20 | 0.842 |
| 90% | 0.10 | 1.282 |
| 95% | 0.05 | 1.645 |

Two-sided $\alpha = 0.05$: $z_{\alpha/2} = 1.960$.

---

## Example

Workshop study: detect $\Delta = 2$ minutes with $\sigma = 4$ ($d = 0.5$), two-sided $\alpha = 0.05$, power 80%. Expect 20% of batches to be unusable.

**Step 1: approximate formula.**
$$n \approx \frac{2(1.9600 + 0.8416)^2}{0.5^2} = \frac{2(2.8016)^2}{0.25} = \frac{2(7.8489)}{0.25} = 62.79$$

**Step 2: exact t-test calculation** (software): $n = 63.77$ per group.

**Step 3: round up.** **64 per group, 128 in total.** Check: power at 64 per group is 0.8015 (at 63 it would be 0.795).

**Step 4: dropout.**
$$n_\text{recruit} = \left\lceil \frac{64}{1 - 0.20} \right\rceil = \lceil 80 \rceil = 80 \text{ per group}$$

**Conclusion:** recruit 80 batches per group (160 in total), expecting about 64 usable per group. That gives about 80% power to detect a 2-minute difference.

---

## Doing it in Excel

| Want | Formula | Result |
|---|---|---|
| $z_{\alpha/2}$ | `=NORM.S.INV(0.975)` | 1.960 |
| $z_\beta$ (80% power) | `=NORM.S.INV(0.80)` | 0.842 |
| approximate $n$ | `=2*(NORM.S.INV(0.975)+NORM.S.INV(0.8))^2/0.5^2` | 62.79 |
| round up | `=CEILING.MATH(62.79)` | 63 (exact t answer: 64) |

Excel has no noncentral t function. For the exact value use G\*Power or Python: `TTestIndPower().solve_power(0.5, alpha=0.05, power=0.8)` in `statsmodels`.

---

## Your turn

A calculator says 87.2 per group. What is the minimum total sample? With 15% expected loss, how many should you recruit per group?

**Answer:** Round up to 88 per group, **176 in total**. Recruit $\lceil 88/0.85 \rceil = \lceil 103.5\rceil = 104$ per group, **208 in total**.

---

## Key takeaways

- $n \approx 2(z_{\alpha/2} + z_\beta)^2/d^2$ per group gives a quick first answer. Use the exact t-test calculation for the final plan.
- For $d = 0.5$, $\alpha = 0.05$, power 80%: **64 per group**.
- Always round **up**, then inflate for expected dropout: $\lceil n/(1 - L)\rceil$.
- Paired, clustered, unequal-variance and multiple-test designs need their own calculations.

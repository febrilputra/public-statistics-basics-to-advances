# Lesson 15.1 - What Is Statistical Power?

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 9 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 15 - Power and Power Analysis

## The big picture: planning a study that can find what it is looking for

Lesson 10.2 introduced the two ways a hypothesis test can be wrong. This chapter turns that around: **before** collecting data, how do we make sure a study has a good chance of detecting an effect that really matters?

| Question | Tool | Lesson |
|---|---|---|
| What is power, and how is it different from α? | the two-curve picture | 15.1 (this one) |
| How big an effect should I plan for? | Cohen's $d$ | 15.2 |
| What makes power go up or down? | $n$, $d$, $\sigma$, $\alpha$ | 15.3 |
| How many people do I need? | sample size formulas | 15.4 |
| How do I check a plan? What mistakes should I avoid? | simulation, observed power | 15.5 |

**1. Four possible outcomes.** A test either rejects ${\color{#0072B2}H_0}$ or fails to reject it, and ${\color{#0072B2}H_0}$ is either true or false:

| | ${\color{#0072B2}H_0}$ true (no effect) | ${\color{#D55E00}H_a}$ true (real effect) |
|---|---|---|
| **Reject ${\color{#0072B2}H_0}$** | Type I error, probability $\alpha$ | correct, probability = **power** |
| **Fail to reject ${\color{#0072B2}H_0}$** | correct, probability $1 - \alpha$ | Type II error, probability $\beta$ |

$$\text{Power} = P(\text{reject } {\color{#0072B2}H_0} \mid \text{the effect is real}) = 1 - \beta$$

**2. α and power live in different worlds.** $\alpha$ is about the world where there is **no effect**: how often we raise a false alarm. Power is about a world where a **specific effect** exists: how often we detect it. You choose $\alpha$ (usually 0.05). Power has to be **calculated**, and it depends on the design.

**3. Two curves.** Imagine running the same study many times. The difference in sample means, $\bar x_B - \bar x_A$, bounces around:

- If ${\color{#0072B2}H_0}$ is true, it is centred at 0 (blue curve).
- If the true difference is $\Delta = \mu_B - \mu_A$, it is centred at $\Delta$ (orange curve).

Both curves have the same spread, the **standard error** $\text{SE} = \sigma\sqrt{2/n}$ for two groups of size $n$ (Lesson 11.1). The test rejects when the observed difference lands beyond the cutoffs $\pm 1.96\,\text{SE}$. Power is the part of the **orange** curve beyond the cutoffs.

![Left: a 2-by-2 table of decisions against truth, with Type I error (α) in red, power in green, Type II error (β) in light orange. Right: two normal curves for the difference in sample means, blue centred at 0 if H0 is true and orange centred at 2 if the true difference is 2 minutes; dashed cutoffs at ±1.39; red tails of the blue curve are α, the light-orange part of the orange curve inside the cutoffs is β ≈ 0.19, and the green part beyond the cutoff is power ≈ 0.81](figures/power_two_curves.png)

With 64 per group, SD 4 and a true difference of 2 minutes, about 81% of the orange curve lies beyond the cutoff. Such a study would detect the effect about 81% of the time and miss it about 19% of the time.

**4. What "80% power" does and doesn't mean.** It means: **if** the true difference is $\Delta$ and the other assumptions hold, about 80% of repeated studies like this one would reject ${\color{#0072B2}H_0}$. It does **not** mean an 80% chance that the treatment works, or that a significant result is 80% likely to be right. Every power number is attached to one assumed effect size.

---

## Goal

Define power, relate it to $\alpha$ and $\beta$, and calculate it for a two-group comparison of means (normal approximation).

## Formulas

$$\text{SE} = \sigma\sqrt{\frac{2}{n}} \quad (n \text{ per group}), \qquad \text{cutoff} = z_{\alpha/2}\,\text{SE}$$

$$\text{Power} \approx P\!\left(Z > \frac{\text{cutoff} - \Delta}{\text{SE}}\right) = P\!\left(Z > z_{\alpha/2} - \frac{\Delta}{\text{SE}}\right)$$

$z_{\alpha/2}$ is the two-tailed critical value from the z-table (Lesson 9.2): $z_{\alpha/2} = 1.96$ for $\alpha = 0.05$. $\Delta = \mu_B - \mu_A$ is the true difference in means we want to detect. (The other tail, on the far side of $-\text{cutoff}$, adds a tiny amount and is usually ignored.)

---

## Example

A workshop compares an old and a new process. They want to detect a true saving of $\Delta = 2$ minutes. The SD of times is $\sigma = 4$ minutes. They plan $n = 64$ per group and a two-sided test at $\alpha = 0.05$.

**Step 1: standard error.**
$$\text{SE} = 4\sqrt{\frac{2}{64}} = 4(0.17678) = 0.7071 \text{ minutes}$$

**Step 2: cutoff.** Reject if the observed difference is beyond
$$1.96 \times 0.7071 = 1.386 \text{ minutes}$$

**Step 3: power.** If the true difference is 2, the observed difference is centred at 2:
$$\text{Power} \approx P\!\left(Z > \frac{1.386 - 2}{0.7071}\right) = P(Z > -0.868) = 0.807$$

**Step 4: β.**
$$\beta = 1 - 0.807 = 0.193$$

**Conclusion:** with 64 per group, the study detects a 2-minute difference about 81% of the time. (The exact t-test calculation in Lesson 15.4 gives 0.80.)

---

## Doing it in Excel

`=1-NORM.S.DIST(1.96-2/(4*SQRT(2/64)), TRUE)` → 0.807

---

## Your turn

Same workshop, but only $n = 20$ per group. What is the power?

**Answer:**
$$\text{SE} = 4\sqrt{2/20} = 1.265, \qquad \text{cutoff} = 1.96(1.265) = 2.479$$
$$\text{Power} \approx P\!\left(Z > \frac{2.479 - 2}{1.265}\right) = P(Z > 0.379) = 0.352$$

That is only about a 35% chance of detecting a real 2-minute saving. (The exact t-test value is 0.34.) This study would usually miss the effect, so a non-significant result from it would say very little.

---

## Key takeaways

- Power = $P(\text{reject } {\color{#0072B2}H_0} \mid \text{a specified effect is real}) = 1 - \beta$.
- $\alpha$ is the false alarm rate when there is no effect. Power is the detection rate when there is one.
- Picture two curves with the same SE: power is the part of the "effect" curve beyond the cutoff.
- Power always refers to an assumed effect size and design. It is not the chance that the hypothesis is true.
- A common target is 80% power (β = 0.20).

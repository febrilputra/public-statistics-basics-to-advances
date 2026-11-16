# Lesson 17.5 - ANCOVA Assumptions and Interactions

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 11 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 17 - ANOVA and ANCOVA

## The big picture: when is an "adjusted difference" meaningful?

An ANCOVA result like "B is 3 minutes faster at the same moisture" relies on three things that the F-test does not check for you.

**1. Parallel slopes (no interaction).** The additive model gives both groups the same slope, so the gap $\tau$ is the same at every covariate value. If the slopes really differ, add an interaction (Lesson 14.3):

$$\hat y = b_0 + b_1x + \tau z + \gamma\,xz$$

Then the B − A difference **depends on $x$**:

$$\text{difference at } x = \tau + \gamma x$$

There is no single "adjusted effect" any more. Report the difference at several sensible covariate values. A non-significant interaction in a small study does **not** prove the slopes are parallel. It may just be low power.

**2. Overlap.** Comparing groups "at the same moisture" only makes sense if both groups actually **have** batches at that moisture. If all A batches are dry and all B batches are wet, the comparison at a middle value comes entirely from **extrapolating** both lines into a region with no data. The model fills the gap with assumptions, not evidence.

**3. The right covariate: measured before treatment.** Adjust for things fixed **before** the groups were treated (baseline moisture, age at entry, a pre-test score). Don't adjust for something the treatment itself changes, such as moisture after one hour of drying. That variable is part of **how** the method works, so adjusting for it removes part of the effect you want to measure, and can add bias.

![Three panels. A: two non-parallel lines, A: 12 + 0.5x and B: 10 + 0.8x; the B − A gap is −2.0 at x = 0, 0 at x = 6.67 and +1.0 at x = 10. B: method A batches all at low moisture and method B batches all at high moisture, with a shaded empty band around 20% labelled "no data here: comparison at x = 20 is extrapolation". C: a diagram where method and baseline moisture both point to drying time (green: adjust for baseline moisture), and method points to moisture after 1 hour which points to drying time (red: don't adjust for it)](figures/ancova_assumptions.png)

A: with an interaction, method B is slower at low x, the same at $x = 6.67$, and faster at high x. B: with no overlap, an "adjusted" comparison is pure extrapolation. C: adjust for baseline variables, not for variables on the path from treatment to outcome.

**4. Other checks, as in any regression or ANOVA.** Independent observations, roughly constant residual spread (Welch-type methods if not), a straight-line relationship with the covariate, no single point driving the result. In **observational** data (groups not randomly assigned), adjusting for covariates helps but does not by itself prove cause and effect (Lesson 14.3).

---

## Goal

Check the main ANCOVA assumptions and interpret a model in which the group difference depends on the covariate.

## Formulas

$$\hat y = b_0 + b_1x + \tau z + \gamma xz$$

| Group | Line |
|---|---|
| A ($z = 0$) | $b_0 + b_1x$ |
| B ($z = 1$) | $(b_0 + \tau) + (b_1 + \gamma)x$ |
| B − A | $\tau + \gamma x$, equal to 0 at $x = -\tau/\gamma$ |

---

## Example

A fitted interaction model is

$$\hat y = 12 + 0.5x - 2z + 0.3xz$$

**Step 1: the two lines.**
- A: $\hat y = 12 + 0.5x$
- B: $\hat y = 12 + 0.5x - 2 + 0.3x = 10 + 0.8x$

**Step 2: the difference B − A.**
$$-2 + 0.3x$$

| $x$ | B − A |
|---:|---:|
| 0 | −2.0 |
| 5 | −0.5 |
| 6.67 | 0 |
| 10 | +1.0 |

**Step 3: interpretation.** B is lower than A at small $x$ and higher at large $x$. The lines cross at $x = 2/0.3 = 6.67$. Saying "the effect of B is −2" would be true only at $x = 0$. Report the difference across the range of $x$ that the data actually cover, and only where both groups have data.

**The drying data of Lesson 17.4** have exactly equal slopes in both groups (2 and 2), so the interaction coefficient is 0 and the additive model is appropriate there.

---

## Doing it in Excel

Add a column `=B2*C2` (covariate × group dummy) and include it in *Data Analysis → Regression*. Its coefficient is $\gamma$. Its p-value tests whether the slopes differ, but remember the low-power caveat.

---

## Your turn

Why is adjusting for a measurement taken **after** treatment different from adjusting for baseline moisture?

**Answer:** A post-treatment measurement can be affected by the treatment, so it may sit on the path from treatment to outcome or reflect who stayed in the study. Holding it fixed removes part of the treatment's effect and can introduce bias. Baseline moisture is fixed before treatment, so adjusting for it only removes noise and pre-existing differences.

---

## Key takeaways

- Check parallel slopes: with an interaction, the group difference is $\tau + \gamma x$ and must be reported at chosen $x$ values.
- A non-significant interaction in a small sample doesn't prove parallel slopes.
- Make sure the groups overlap on the covariate. Otherwise the adjusted comparison is extrapolation.
- Adjust only for covariates measured before treatment, never for variables the treatment can change.
- Adjustment improves comparisons but does not turn observational data into proof of causation.

# Lesson 17.1 - One-Way ANOVA and Sums of Squares

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 11 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 17 - ANOVA and ANCOVA

## The big picture: comparing more than two means at once

Lesson 11.1 compared **two** means with a t-test. With three or more groups, we could run a t-test for every pair, but Chapter 16 showed that many tests mean many chances for a false positive. **ANOVA** (ANalysis Of VAriance) asks one joint question first.

| Question | Tool | Lesson |
|---|---|---|
| Are all the group means equal? | sums of squares and the F statistic | 17.1 (this one) |
| How do I fill in and read the ANOVA table? | ANOVA table, η², ω² | 17.2 |
| Which groups differ? | pairwise comparisons, Tukey, Holm | 17.3 |
| How do I compare groups fairly when a measured variable differs? | ANCOVA | 17.4 |
| When can I trust an adjusted comparison? | interaction, overlap, covariate choice | 17.5 |

**1. One joint null hypothesis.** For $g$ groups with population means $\mu_1, \dots, \mu_g$:

$${\color{#0072B2}H_0}: \mu_1 = \mu_2 = \dots = \mu_g \qquad {\color{#D55E00}H_a}: \text{at least one mean is different}$$

${\color{#D55E00}H_a}$ does **not** say that every mean differs, or which one is biggest.

**2. Why "analysis of variance" compares means.** Split the variation of all observations into two parts:

- **Between groups**: how far the group means are from the overall (grand) mean. If the population means really differ, this part is big.
- **Within groups**: how far observations are from their own group's mean. This is just noise, and it's there whether or not ${\color{#0072B2}H_0}$ is true.

$$\underbrace{\sum\sum (y_{ij} - \bar y)^2}_{SS_T \text{ (total)}} = \underbrace{\sum n_j(\bar y_j - \bar y)^2}_{SS_B \text{ (between)}} + \underbrace{\sum\sum (y_{ij} - \bar y_j)^2}_{SS_W \text{ (within)}}$$

![Three panels of the same 12 completion times for layouts A, B and C. Left: red sticks from each point to the grand mean 7, SS_T = 38. Middle: red bars from each group mean (5, 7, 9) to the grand mean, SS_B = 32. Right: red sticks from each point to its own group mean, SS_W = 6. An equals sign and a plus sign between the panels show 38 = 32 + 6](figures/anova_sum_of_squares.png)

The total scatter around the grand mean (left) splits exactly into the scatter **of the group means** (middle) plus the scatter **inside the groups** (right). Here most of the variation, 32 of 38, comes from differences between the layouts.

**3. The F statistic.** Turn each sum of squares into a variance estimate (a **mean square**) by dividing by its degrees of freedom:

$$MS_B = \frac{SS_B}{g - 1}, \qquad MS_W = \frac{SS_W}{n_T - g}, \qquad F = \frac{MS_B}{MS_W}$$

If ${\color{#0072B2}H_0}$ is true, both mean squares estimate the same noise variance, so $F \approx 1$. If the means differ, $MS_B$ grows and $F$ gets large. Compare with the **F distribution** with $(g - 1, n_T - g)$ degrees of freedom, right tail only.

**4. ANOVA is regression in disguise.** One-way ANOVA is the nested-model F-test of Lesson 14.4 with $g - 1$ dummy variables (Lesson 14.2). The reduced model is "one common mean" and the full model is "one mean per group". $SS_W$ is the full model's SSE and $SS_T$ is the reduced model's SSE. With $g = 2$ groups, $F = t^2$ from the pooled two-sample t-test.

**5. Assumptions.** Independent observations, roughly normal errors, and **equal variances** in all groups (like the pooled t-test). With clearly unequal variances, especially with unequal group sizes, use Welch's ANOVA instead.

---

## Goal

Split the total variation into between-group and within-group sums of squares, and compute the ANOVA F statistic.

## Formulas

| Quantity | Formula | df |
|---|---|---|
| $SS_B$ | $\sum_j n_j(\bar y_j - \bar y)^2$ | $g - 1$ |
| $SS_W$ | $\sum_j\sum_i (y_{ij} - \bar y_j)^2$ | $n_T - g$ |
| $SS_T$ | $\sum_j\sum_i (y_{ij} - \bar y)^2 = SS_B + SS_W$ | $n_T - 1$ |
| $F$ | $\dfrac{SS_B/(g - 1)}{SS_W/(n_T - g)}$ | $(g - 1, n_T - g)$ |

$g$ = number of groups, $n_j$ = size of group $j$, $n_T = \sum n_j$ = total number of observations, $\bar y$ = grand mean of all $n_T$ observations. (We write $n_T$, not $N$, because $N$ already means a population size in Lessons 1.4 and 13.2.)

---

## Example

Three packing layouts are each timed 4 times (minutes):

| Layout | Times | Mean $\bar y_j$ | Within: $\sum(y - \bar y_j)^2$ |
|---|---|---:|---:|
| A | 4, 5, 6, 5 | 5 | $1 + 0 + 1 + 0 = 2$ |
| B | 6, 7, 8, 7 | 7 | $1 + 0 + 1 + 0 = 2$ |
| C | 8, 9, 10, 9 | 9 | $1 + 0 + 1 + 0 = 2$ |

$g = 3$, $n_T = 12$, grand mean $\bar y = 84/12 = 7$.

**Step 1: within.**
$$SS_W = 2 + 2 + 2 = 6$$

**Step 2: between.**
$$SS_B = 4(5 - 7)^2 + 4(7 - 7)^2 + 4(9 - 7)^2 = 16 + 0 + 16 = 32$$

**Step 3: total (check).** Deviations from 7: A gives $9 + 4 + 1 + 4 = 18$, B gives $1 + 0 + 1 + 0 = 2$, C gives $1 + 4 + 9 + 4 = 18$.
$$SS_T = 18 + 2 + 18 = 38 = 32 + 6 \checkmark$$

**Step 4: F.**
$$MS_B = \frac{32}{2} = 16, \qquad MS_W = \frac{6}{9} = 0.667, \qquad F = \frac{16}{0.667} = 24$$

The variation between layouts is 24 times larger than what noise alone would produce. Lesson 17.2 turns this into a p-value.

---

## Doing it in Excel

*Data → Data Analysis → Anova: Single Factor*, with the three layouts in three columns, prints SS, df, MS, F, the p-value and the critical F.

---

## Your turn

Four groups have five observations each. The within-group SS is 80 and the between-group SS is 60. Find $F$ and its degrees of freedom.

**Answer:** $g = 4$, $n_T = 20$.
$$F = \frac{60/3}{80/16} = \frac{20}{5} = 4, \qquad \text{df} = (3, 16)$$

---

## Key takeaways

- ANOVA tests ${\color{#0072B2}H_0}$: all group means are equal, in one test instead of many t-tests.
- $SS_T = SS_B + SS_W$: total = between groups + within groups.
- $F = MS_B/MS_W$, with df $(g - 1, n_T - g)$. $F \approx 1$ under ${\color{#0072B2}H_0}$, and a large $F$ is evidence against it.
- One-way ANOVA is a nested-model F-test using dummy variables. With 2 groups, $F = t^2$.
- It assumes independence, normal errors and equal group variances (use Welch's ANOVA if the variances clearly differ).

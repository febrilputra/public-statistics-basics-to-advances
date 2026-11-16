# Lesson 17.2 - The ANOVA Table and Effect Size

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 11 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 17 - ANOVA and ANCOVA

## The big picture: one table holds the whole test

**1. The ANOVA table.** Every ANOVA output, by hand or by software, has the same layout:

| Source | SS | df | MS = SS/df | F |
|---|---|---|---|---|
| Between groups | $SS_B$ | $g - 1$ | $MS_B$ | $MS_B/MS_W$ |
| Within groups (error) | $SS_W$ | $n_T - g$ | $MS_W$ | |
| Total | $SS_T$ | $n_T - 1$ | | |

Both columns add up: $SS_B + SS_W = SS_T$, and $(g - 1) + (n_T - g) = n_T - 1$. These make handy checks.

**2. The F-test is always right-tailed.** Only a **large** F is evidence that the means differ (like the chi-square tests of Chapter 12). Reject ${\color{#0072B2}H_0}$ when $F > F_\alpha(g - 1, n_T - g)$, or when the p-value $< \alpha$.

![Left: the ANOVA table for the three layouts: between SS 32, df 2, MS 16; within SS 6, df 9, MS 0.667; total SS 38, df 11; F = 16/0.667 = 24; below it η² = 32/38 = 0.842 and ω² = 0.793. Right: the F distribution with 2 and 9 degrees of freedom, the critical value 4.26 dashed, and the observed F = 24 far to the right with p = 0.000247](figures/anova_f_test.png)

The observed F = 24 lies far beyond the critical value 4.26, deep in the right tail of F(2, 9). The p-value is about 0.00025.

**3. Significance is not size: report an effect size.** A tiny difference can be significant with huge samples. Two common effect sizes for ANOVA:

- **Eta squared**, the share of the observed variation explained by group membership (the same as $R^2$ in Lesson 14.5):

$$\eta^2 = \frac{SS_B}{SS_T}$$

- **Omega squared**, a less biased estimate of the share in the **population**. $\eta^2$ tends to overestimate, especially in small samples:

$$\omega^2 = \frac{SS_B - (g - 1)MS_W}{SS_T + MS_W}$$

$\omega^2$ can come out negative when $F < 1$. It is usually reported as 0 then, and you should say so if you do that.

**4. Always give the means in real units too.** "Layout C takes 4 minutes longer than A on average" means more to a reader than "$\eta^2 = 0.84$".

**5. A significant F says "some means differ", not which.** Lesson 17.3 finds out which.

---

## Goal

Complete an ANOVA table, carry out the F-test with a critical value or p-value, and report $\eta^2$ and $\omega^2$.

## Formulas

$$F = \frac{MS_B}{MS_W}, \qquad \text{p-value} = P(F_{g - 1,\, n_T - g} > F_\text{obs})$$

$$\eta^2 = \frac{SS_B}{SS_T}, \qquad \omega^2 = \frac{SS_B - (g - 1)MS_W}{SS_T + MS_W}$$

---

## Example

Continue the three layouts of Lesson 17.1 at $\alpha = 0.05$.

**Step 1: hypotheses.** ${\color{#0072B2}H_0}: \mu_A = \mu_B = \mu_C$. ${\color{#D55E00}H_a}$: at least one mean differs.

**Step 2: ANOVA table.**

| Source | SS | df | MS | F |
|---|---:|---:|---:|---:|
| Between layouts | 32 | 2 | 16 | **24** |
| Within layouts | 6 | 9 | 0.667 | |
| Total | 38 | 11 | | |

**Step 3: critical value.** $F_{0.05}(2, 9) = 4.26$. Since $24 > 4.26$, **reject ${\color{#0072B2}H_0}$**.

**Step 4: p-value.** $P(F_{2,9} > 24) = 0.000247$, far below 0.05.

**Step 5: effect sizes.**
$$\eta^2 = \frac{32}{38} = 0.842$$
$$\omega^2 = \frac{32 - 2(0.667)}{38 + 0.667} = \frac{30.67}{38.67} = 0.793$$

**Conclusion:** the layouts do not all have the same mean completion time ($F(2, 9) = 24$, $p < 0.001$). Layout explains about 84% of the observed variation (about 79% after correcting for small-sample bias). The means are 5, 7 and 9 minutes. "Explains" here is statistical. It doesn't prove that the layout **causes** the difference unless layouts were assigned at random.

---

## Doing it in Excel

| Want | Formula | Result |
|---|---|---|
| p-value | `=F.DIST.RT(24, 2, 9)` | 0.000247 |
| critical value | `=F.INV.RT(0.05, 2, 9)` | 4.256 |

---

## Your turn

With $F = 4$ and df $= (3, 16)$ from Lesson 17.1's exercise, what is the p-value? If $SS_B = 60$ and $SS_W = 80$, what is $\eta^2$?

**Answer:** p $=$ `F.DIST.RT(4, 3, 16)` $\approx 0.027$, so reject ${\color{#0072B2}H_0}$ at $\alpha = 0.05$. $\eta^2 = 60/(60 + 80) = 0.429$.

---

## Key takeaways

- ANOVA table: SS, df, MS = SS/df, and F = $MS_B/MS_W$. The SS column and the df column each add up to their totals.
- The test is right-tailed: reject when $F > F_\alpha(g - 1, n_T - g)$.
- Report an effect size: $\eta^2 = SS_B/SS_T$, or the less biased $\omega^2$.
- Also report the group means in real units.
- A significant F means at least one mean differs. Follow-up comparisons find which.

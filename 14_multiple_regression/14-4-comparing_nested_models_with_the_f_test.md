# Lesson 14.4 - Comparing Nested Models with the F-Test

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 7 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 14 - Multiple Regression

## The big picture: is the extra predictor worth it?

**1. Adding a predictor always lowers SSE.** The bigger model can always set the new coefficient to 0 and get back the smaller model, so its SSE can only go down or stay the same. Even a column of random numbers lowers SSE a little. The question is whether the drop is **bigger than chance**.

**2. Nested models.** A **reduced** model is *nested* in a **full** model when you get it by setting some of the full model's coefficients to 0:

- reduced: $\hat y = b_0 + b_1x$ ($K_R = 2$ coefficients)
- full: $\hat y = b_0 + b_1x + b_2z$ ($K_F = 3$ coefficients)

Fit **both** models separately, on exactly the same rows. Don't just delete a term from the fitted full equation, because the other coefficients can change when you refit.

**3. The F statistic compares "improvement" with "noise".**

$$F = \frac{\text{drop in SSE per added coefficient}}{\text{leftover noise variance}} = \frac{(\text{SSE}_R - \text{SSE}_F)/(K_F - K_R)}{\text{SSE}_F/(n - K_F)}$$

If the new predictors are useless, the top and bottom both estimate the same noise variance, so $F \approx 1$. A large $F$ means the SSE dropped much more than noise alone would explain.

**4. Use the right tail of the F distribution.** Under ${\color{#0072B2}H_0}$ (all added coefficients are 0) and the usual regression assumptions (independent, normal errors with constant variance), $F$ follows an **F distribution** with

$$\text{df} = (K_F - K_R,\; n - K_F)$$

Like the chi-square test in Lesson 12.1, only **large** values are evidence against ${\color{#0072B2}H_0}$, so the test is always right-tailed.

![Left: bars of SSE falling from 58 for the mean-only model to 26 after adding batch size and to 8 after adding coating, with drops of 32 and 18 marked. Right: the F distribution with 1 and 5 degrees of freedom, the critical value 6.61 dashed, and the observed F = 11.25 in the far right tail; an inset zooms in on the tail, where the red area beyond 11.25 is the p-value 0.020](figures/nested_models_f_test.png)

Left: each added term lowers SSE. Adding coating removes another 18. Right: compared with the F(1, 5) distribution, an F of 11.25 is far out in the right tail. Only 2% of the area lies beyond it, so p = 0.020.

**5. Two special cases.**

- **One added coefficient:** $F = t^2$, where $t$ is that coefficient's t statistic. The F-test and the t-test give the same p-value.
- **Overall F-test:** compare the full model with the **mean-only** model $\hat y = \bar y$, whose SSE is the total sum of squares $\text{TSS} = \sum(y - \bar y)^2$. It tests whether **any** predictor helps.

---

## Goal

Test whether one or more added predictors significantly improve a regression model.

## Formulas

$${\color{#0072B2}H_0}: \text{all added coefficients} = 0 \qquad {\color{#D55E00}H_a}: \text{at least one} \ne 0$$

$$F = \frac{(\text{SSE}_R - \text{SSE}_F)/(K_F - K_R)}{\text{SSE}_F/(n - K_F)}, \qquad \text{df} = (K_F - K_R,\; n - K_F)$$

Reject ${\color{#0072B2}H_0}$ if $F > F_{\alpha}$, or equivalently if p-value $< \alpha$.

---

## Example

Same 8 batches as Lesson 14.2. Does coating add anything beyond batch size? Use $\alpha = 0.05$.

**Step 1: fit both models.**

| Model | Fitted equation | SSE | $K$ |
|---|---|---:|---:|
| mean only | $\hat y = 11.5$ | 58 | 1 |
| reduced (size) | $\hat y = 11.5 + 2x$ | 26 | 2 |
| full (size + coating) | $\hat y = 10 + 2x + 3z$ | 8 | 3 |

The reduced model's SSE, row by row: at $x = -1$ it predicts 9.5, and the times 7, 9, 10, 12 give residuals −2.5, −0.5, 0.5, 2.5. Their squares add to 13. The same happens at $x = +1$, so $\text{SSE}_R = 26$.

**Step 2: F statistic.** $n = 8$, $K_F - K_R = 1$, $n - K_F = 5$.

$$F = \frac{(26 - 8)/1}{8/5} = \frac{18}{1.6} = 11.25$$

**Step 3: decision.** Critical value $F_{0.05}(1, 5) = 6.61$. Since $11.25 > 6.61$, reject ${\color{#0072B2}H_0}$. The p-value is $P(F_{1,5} > 11.25) \approx 0.020 < 0.05$.

**Conclusion:** at the same batch size, coating changes the average preparation time. The estimate is +3 minutes.

**Check with $t$:** the t statistic for the coating coefficient is $3.354$, and $3.354^2 = 11.25 = F$.

**Overall F-test** (full model vs mean only):

$$F = \frac{(58 - 8)/(3 - 1)}{8/5} = \frac{25}{1.6} = 15.625, \qquad \text{df} = (2, 5), \quad p \approx 0.007$$

---

## Doing it in Excel

| Want | Formula | Result |
|---|---|---|
| p-value | `=F.DIST.RT(11.25, 1, 5)` | 0.0202 |
| Critical value | `=F.INV.RT(0.05, 1, 5)` | 6.608 |

---

## Your turn

A reduced model has SSE = 120 with $K_R = 2$. A full model, fitted to the same 30 rows, has SSE = 90 with $K_F = 4$. Find $F$, its df and the p-value.

**Answer:**
$$F = \frac{(120 - 90)/2}{90/26} = \frac{15}{3.4615} \approx 4.333, \qquad \text{df} = (2, 26), \qquad p = \texttt{F.DIST.RT(4.333, 2, 26)} \approx 0.024$$

At $\alpha = 0.05$ the two added predictors improve the model.

---

## Key takeaways

- Adding predictors never raises SSE, so test whether the drop is bigger than chance.
- Partial F $= \dfrac{(\text{SSE}_R - \text{SSE}_F)/(K_F - K_R)}{\text{SSE}_F/(n - K_F)}$, with df $= (K_F - K_R, n - K_F)$. It is always right-tailed.
- Fit both models separately, on exactly the same rows.
- With one added coefficient, $F = t^2$.
- The overall F-test compares the full model with the mean-only model.

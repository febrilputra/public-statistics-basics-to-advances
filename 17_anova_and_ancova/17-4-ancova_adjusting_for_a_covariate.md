# Lesson 17.4 - ANCOVA: Adjusting for a Covariate

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 11 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 17 - ANOVA and ANCOVA

## The big picture: compare groups "at the same starting point"

**1. Some of the noise can be explained.** Two drying methods are compared. Drying time also depends strongly on how wet each batch was at the start (its **initial moisture**). In a plain comparison of the methods, that moisture effect looks like random scatter, so the comparison is noisy.

**2. ANCOVA = ANOVA + a numerical covariate.** **AN**alysis of **CO**-**VA**riance adds the covariate to the model:

$$\hat y = b_0 + b_1x + \tau z$$

- $x$ = covariate (moisture − 20, centred as in Lesson 14.1)
- $z$ = 1 for method B, 0 for method A (a dummy, Lesson 14.2)
- $\tau$ = the B − A difference **at the same moisture**

It is exactly the "parallel lines" model of Lesson 14.2, with a different story.

**3. Two benefits.**

- **Precision:** the covariate explains part of the noise, so the residual variance and the standard error of $\tau$ shrink. That gives a narrower interval and more power.
- **Fairness:** if the groups happen to start with different moisture, ANCOVA compares them at the **same** moisture.

![Three panels. A: drying times for methods A and B ignoring moisture, means 10 and 7, with lots of scatter; B − A = −3, p = 0.19, 95% CI [−7.84, 1.84]. B: drying time against initial moisture with two parallel fitted lines, A: ŷ = 10 + 2x and B: ŷ = 7 + 2x, a gap τ = −3, residuals small; B − A = −3, p = 0.003, 95% CI [−4.60, −1.40]. C: sum of squared errors 88 for a method-only model, 30.5 for moisture only, and 8 for moisture plus method](figures/ancova_adjustment.png)

A: ignoring moisture, the scatter within each method hides the difference (p = 0.19). B: plotted against moisture, the points sit close to two parallel lines 3 minutes apart (p = 0.003). C: the leftover noise drops from 88 to 8 once moisture is in the model.

**4. Test the method with a partial F-test** (Lesson 14.4). Compare:

- reduced: $\hat y = b_0 + b_1x$ (moisture only)
- full: $\hat y = b_0 + b_1x + \tau z$ (moisture + method)

This asks whether method matters **after** accounting for moisture.

**5. Partial $R^2$.** The share of the reduced model's leftover variation that the method removes:

$$R^2_\text{partial} = \frac{\text{SSE}_R - \text{SSE}_F}{\text{SSE}_R}$$

---

## Goal

Fit and interpret an ANCOVA model, test the group effect with a partial F-test, and see how adjustment changes precision.

## Formulas

$$\hat y = b_0 + b_1x + \tau z$$

$$F = \frac{(\text{SSE}_R - \text{SSE}_F)/(K_F - K_R)}{\text{SSE}_F/(n_T - K_F)}, \qquad R^2_\text{partial} = \frac{\text{SSE}_R - \text{SSE}_F}{\text{SSE}_R}$$

---

## Example

Five batches per method. Moisture 18, 19, 20, 21, 22% in **each** group ($x = -2, -1, 0, 1, 2$).

| $x$ | −2 | −1 | 0 | 1 | 2 | Mean |
|---|---:|---:|---:|---:|---:|---:|
| Method A time | 7 | 7 | 10 | 11 | 15 | 10 |
| Method B time | 2 | 6 | 7 | 10 | 10 | 7 |

**Step 1: common slope.** Within each group, $S_{xx} = 4 + 1 + 0 + 1 + 4 = 10$.

- A: $S_{xy} = (-2)(-3) + (-1)(-3) + 0 + (1)(1) + (2)(5) = 20$
- B: $S_{xy} = (-2)(-5) + (-1)(-1) + 0 + (1)(3) + (2)(3) = 20$

$$b_1 = \frac{20 + 20}{10 + 10} = 2 \text{ minutes per \% moisture}$$

**Step 2: intercepts and $\tau$.** Both groups have $\bar x = 0$, so each line passes through its group mean at $x = 0$: A at 10, B at 7.
$$\boxed{\hat y = 10 + 2x - 3z}, \qquad \tau = -3$$

**Step 3: SSE of the full model.** A's fitted values are 6, 8, 10, 12, 14, giving residuals 1, −1, 0, −1, 1. B's fitted values are 3, 5, 7, 9, 11, giving residuals −1, 1, 0, 1, −1.
$$\text{SSE}_F = 4 + 4 = 8$$

**Step 4: SSE of the reduced model** (moisture only). It fits one line through the overall mean 8.5 with slope 2. Its residuals are ±2.5, ±0.5, ±1.5, ±0.5, ±2.5, so
$$\text{SSE}_R = 2(6.25 + 0.25 + 2.25 + 0.25 + 6.25) = 30.5$$

**Step 5: partial F.** $n_T = 10$, $K_F = 3$, $K_R = 2$.
$$F = \frac{(30.5 - 8)/1}{8/7} = \frac{22.5}{1.143} = 19.69, \qquad \text{df} = (1, 7), \qquad p = 0.0030$$

**Step 6: partial $R^2$.**
$$R^2_\text{partial} = \frac{22.5}{30.5} = 0.738$$

**Step 7: compare with no adjustment.**

| Analysis | Estimate B − A | 95% CI | p |
|---|---:|---|---:|
| two-sample t-test (ignore moisture) | −3 | [−7.84, 1.84] | 0.19 |
| ANCOVA (adjust for moisture) | −3 | [−4.60, −1.40] | 0.003 |

**Conclusion:** at the same initial moisture, method B dries about 3 minutes faster (95% CI 1.4 to 4.6 minutes faster). The estimate didn't change, because moisture was perfectly balanced between the groups. What changed is the **precision**: moisture explained most of the scatter.

---

## Doing it in Excel

Put time in A, moisture − 20 in B, and the method dummy in C. Use *Data Analysis → Regression* with B:C as the X range. The coefficient on C is $\tau$, with its SE, t, p-value and CI. Fit B alone too to get $\text{SSE}_R$ (the "Residual SS" line).

---

## Your turn

A reduced ANCOVA model has SSE = 50. Adding two group dummies (three groups) gives SSE = 30. There are 24 observations and 4 coefficients in the full model. Find the partial F and the partial $R^2$.

**Answer:**
$$F = \frac{(50 - 30)/2}{30/(24 - 4)} = \frac{10}{1.5} = 6.667, \qquad \text{df} = (2, 20), \qquad p \approx 0.006$$
$$R^2_\text{partial} = \frac{50 - 30}{50} = 0.40$$

---

## Key takeaways

- ANCOVA adds a numerical covariate to a group comparison: $\hat y = b_0 + b_1x + \tau z$.
- $\tau$ is the group difference **at the same covariate value** (parallel lines).
- A covariate that predicts the outcome reduces the noise, so you get a smaller SE, a narrower CI and more power.
- Test the group with a partial F-test (moisture-only vs moisture + group). Report partial $R^2$.
- Use covariates measured **before** treatment (Lesson 17.5).

# Lesson 14.6 - Multicollinearity and the VIF

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 7 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 14 - Multiple Regression

## The big picture: two predictors telling the same story

**1. Separate slopes need separate information.** To estimate the slope of $x_1$ "with $x_2$ held fixed", the data must contain cases where $x_1$ changes **while $x_2$ doesn't**. If two predictors almost always move together, there are very few such cases. This is called **multicollinearity**.

**2. The total is stable, the split is not.** With two nearly identical predictors the model can still predict $y$ well, because their **combined** effect is clear. But it can't tell how to divide that effect between them. One sample might give $b_1 = 3$, $b_2 = -1$ and the next $b_1 = -1$, $b_2 = 3$. Both add up to about 2.

**3. Perfect collinearity is the extreme case.** If one column is an exact combination of the others (Celsius and Fahrenheit, kilograms and grams, all $g$ dummies plus an intercept), the coefficients can't be found at all (Lessons 14.1 and 14.2).

![Three panels. A: a scatter of x1 against x2 with r = 0.98. B: estimated slopes b1 and b2 from 400 repeated samples; with unrelated predictors the estimates form a tight green cluster around the true values (1, 1), but with r = 0.98 they form a long red streak along b1 + b2 ≈ 2. C: the VIF curve 1/(1 − R²j) rising steeply, with points at R²j = 0.5, 0.8, 0.9 giving VIF = 2, 5, 10](figures/multicollinearity_vif.png)

A: two predictors with correlation 0.98. B: when the same experiment is repeated 400 times, unrelated predictors give slope estimates that cluster tightly around the truth (green). Nearly duplicate predictors give estimates that swing wildly, though always along the line $b_1 + b_2 \approx 2$ (red). C: the variance inflation factor rises steeply as $R^2_j$ approaches 1.

**4. Measuring it: the VIF.** For each predictor $x_j$, regress it on **all the other predictors** and take that regression's $R^2_j$. Then

$$\text{VIF}_j = \frac{1}{1 - R^2_j}$$

The variance of $b_j$ is multiplied by $\text{VIF}_j$ compared with predictors that are unrelated to each other. Its **standard error** is multiplied by $\sqrt{\text{VIF}_j}$.

**5. What to do about it.** A high VIF is a reason to think, not an automatic order to delete a predictor:

- If you only care about **prediction**, collinearity may not matter much.
- If two columns really measure the same thing, keep one or combine them (e.g. average them).
- If you need the separate effects, you need data where the predictors vary separately.
- Centring helps with interpretation, but it can't separate two predictors that carry the same information.

---

## Goal

Recognise multicollinearity, compute and interpret the VIF, and know what it does to coefficient estimates.

## Formulas

$$\text{VIF}_j = \frac{1}{1 - R^2_j}, \qquad \text{SE}(b_j) \text{ is inflated by } \sqrt{\text{VIF}_j}$$

$R^2_j$ = the $R^2$ from regressing $x_j$ on the other predictors (with an intercept).

---

## Example

How does the VIF grow as $x_j$ becomes more predictable from the other predictors?

| $R^2_j$ | $\text{VIF}_j = 1/(1 - R^2_j)$ | SE multiplied by $\sqrt{\text{VIF}}$ |
|---:|---:|---:|
| 0 | 1 | 1.00 (no inflation) |
| 0.5 | $1/0.5 = 2$ | 1.41 |
| 0.8 | $1/0.2 = 5$ | 2.24 |
| 0.9 | $1/0.1 = 10$ | 3.16 |
| 0.99 | $1/0.01 = 100$ | 10.0 |

Read the last row: if the other predictors explain 99% of $x_j$, its slope's standard error is **10 times** larger than it would be with unrelated predictors. Its confidence interval is 10 times wider.

**Two predictors only.** Then $R^2_j$ is just the squared correlation between them (Lesson 13.3). With $r = 0.98$:

$$R^2_j = 0.98^2 = 0.9604, \qquad \text{VIF} = \frac{1}{1 - 0.9604} = \frac{1}{0.0396} \approx 25.3, \qquad \sqrt{25.3} \approx 5.0$$

Each slope's SE is about 5 times bigger than with unrelated predictors. That is why the red estimates in panel B are spread so widely.

---

## Doing it in Excel

For two predictors: `=1/(1-RSQ(B2:B31, C2:C31))`. For more, regress each predictor on the others with *Data Analysis → Regression* and use its "R Square".

---

## Your turn

A model of house price uses floor area in m² and floor area in ft² ($1\text{ m}^2 = 10.764\text{ ft}^2$) together with an intercept. What will happen?

**Answer:** The ft² column equals 10.764 × the m² column exactly, so $R^2_j = 1$ and the VIF is infinite. The software can't separate the two slopes. It will either refuse, drop one column, or return arbitrary values. Keep only one area column.

---

## Key takeaways

- Multicollinearity: predictors that move together leave little information about their separate effects.
- The combined prediction can be fine while the individual slopes are unstable, with large SEs and sometimes surprising signs.
- $\text{VIF}_j = 1/(1 - R^2_j)$. The SE of $b_j$ is multiplied by $\sqrt{\text{VIF}_j}$.
- Exact duplicates (VIF = ∞) make the coefficients impossible to estimate.
- A high VIF calls for thought (combine, drop, or collect better data), not automatic deletion.

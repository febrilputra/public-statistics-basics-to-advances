# Lesson 14.5 - R², Adjusted R², and Overfitting

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 7 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 14 - Multiple Regression

## The big picture: a good fit is not the same as a good prediction

**1. $R^2$: the share of variation explained.** Lesson 13.3 met $r^2$ for one predictor. In general,

$$R^2 = 1 - \frac{\text{SSE}}{\text{TSS}}, \qquad \text{TSS} = \sum (y - \bar y)^2$$

TSS is the total scatter of $y$ around its mean (the SSE of the mean-only model). SSE is the scatter left over after the model. $R^2 = 0.86$ means the model accounts for 86% of the squared variation in $y$.

**2. $R^2$ never goes down when you add a predictor.** SSE can't increase (Lesson 14.4), so $R^2$ can't decrease, even if the new predictor is pure noise. A higher $R^2$ alone doesn't prove the bigger model is better.

**3. Adjusted $R^2$ charges for each coefficient.** It replaces both sums of squares with their **variances**, i.e. divides by the degrees of freedom:

$$\bar R^2 = 1 - \frac{\text{SSE}/(n - K)}{\text{TSS}/(n - 1)}$$

An extra coefficient makes $n - K$ smaller. If it doesn't lower SSE enough to make up for that, $\bar R^2$ goes **down**. It can even be negative.

**4. Overfitting.** A model with too many coefficients starts fitting the random noise in **this** data set. It looks great on the data it was fitted to (the *training* data) and does worse on new data. The only honest check of prediction is data the model hasn't seen: a held-out **test** set.

![Left: a bar of TSS = 58 split into 50 explained and 8 SSE, with R² = 1 − 8/58 = 0.862 and adjusted R² = 0.807. Right: a simulation where only 2 of 30 predictors are real; as predictors are added, error on the 40 training rows falls from 0.94 to 0.50 while error on 3,000 new rows rises from 1.01 to 1.82](figures/r_squared_and_overfitting.png)

Left: the batch model explains 50 of the 58 units of squared variation. Right: a simulation with 40 training rows where only the first 2 predictors matter. Adding the 28 noise predictors keeps lowering the training error, while the error on new data climbs.

**5. What the simulation shows.**

| Predictors in model | Training error | Error on new data | $R^2$ | Adjusted $R^2$ |
|---:|---:|---:|---:|---:|
| 2 (the real ones) | 0.94 | 1.01 | 0.827 | 0.817 |
| 10 | 0.85 | 1.10 | 0.857 | 0.807 |
| 20 | 0.75 | 1.24 | 0.890 | 0.774 |
| 30 | 0.50 | 1.82 | 0.950 | 0.785 |

(Error = root mean squared error.) $R^2$ climbs all the way to 0.95, while the predictions for new data get almost twice as bad. Adjusted $R^2$ drops away from 0.817, but it is still only a training-data summary. It doesn't replace testing on new data.

---

## Goal

Calculate and interpret $R^2$ and adjusted $R^2$, and recognise overfitting.

## Formulas

$$R^2 = 1 - \frac{\text{SSE}}{\text{TSS}} \qquad \bar R^2 = 1 - \frac{\text{SSE}/(n - K)}{\text{TSS}/(n - 1)} = 1 - (1 - R^2)\frac{n - 1}{n - K}$$

---

## Example

The batch model $\hat y = 10 + 2x + 3z$ from Lesson 14.2: $n = 8$, $K = 3$, SSE = 8.

**Step 1: TSS.** $\bar y = 11.5$. The deviations of 7, 9, 10, 12, 11, 13, 14, 16 from 11.5 are −4.5, −2.5, −1.5, 0.5, −0.5, 1.5, 2.5, 4.5.

$$\text{TSS} = 20.25 + 6.25 + 2.25 + 0.25 + 0.25 + 2.25 + 6.25 + 20.25 = 58$$

**Step 2: $R^2$.**
$$R^2 = 1 - \frac{8}{58} = 0.862$$

**Step 3: adjusted $R^2$.**
$$\bar R^2 = 1 - \frac{8/5}{58/7} = 1 - \frac{1.6}{8.286} = 0.807$$

The model explains about 86% of the variation in preparation time. After allowing for its 3 coefficients, adjusted $R^2$ is 0.81.

**Compare with the size-only model** (SSE = 26, $K = 2$): $R^2 = 1 - 26/58 = 0.552$ and $\bar R^2 = 1 - (26/6)/(58/7) = 0.477$. Adding coating raises both, which agrees with the F-test in Lesson 14.4.

---

## Doing it in Excel

`=RSQ(y, x)` works only for one predictor. For several, `=INDEX(LINEST(y, xs, TRUE, TRUE), 3, 1)` returns $R^2$. *Data Analysis → Regression* prints both "R Square" and "Adjusted R Square".

---

## Your turn

An analyst adds 10 columns of random numbers to a model and sees the training $R^2$ rise from 0.60 to 0.66. Is the new model better?

**Answer:** Not necessarily. $R^2$ is guaranteed not to fall when columns are added, so the rise is expected even from pure noise. Check adjusted $R^2$, ask whether the variables make sense, and above all test the model on new data.

---

## Key takeaways

- $R^2 = 1 - \text{SSE}/\text{TSS}$ is the share of the squared variation in $y$ that the model explains.
- $R^2$ never goes down when you add predictors, even useless ones.
- Adjusted $R^2$ divides by degrees of freedom, so it can fall when a predictor isn't worth its coefficient.
- Overfitting: training error keeps falling while error on new data rises.
- To judge prediction, test on data the model hasn't seen.

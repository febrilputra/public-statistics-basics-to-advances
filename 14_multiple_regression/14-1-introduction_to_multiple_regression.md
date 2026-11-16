# Lesson 14.1 - Introduction to Multiple Regression

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 7 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 14 - Multiple Regression

## The big picture: one line is rarely enough

Chapter 13 predicted $y$ from **one** variable $x$ with the line $\hat y = mx + b$. Real outcomes usually depend on several things at once. A workshop's preparation time depends on the batch size, but also on whether the batch is coated and on who does the work. **Multiple regression** puts all of these predictors into one equation.

| Question | Tool | Lesson |
|---|---|---|
| How do I write and read a model with several predictors? | $\hat y = b_0 + b_1x_1 + \dots + b_px_p$ | 14.1 (this one) |
| How do I put a **category** (coated / uncoated) into the model? | 0/1 dummy variables | 14.2 |
| What does "holding the others fixed" mean? What if a slope differs by group? | adjustment and interaction terms | 14.3 |
| Does an extra predictor really help? | the partial F-test | 14.4 |
| How well does the model fit, and will it predict new data? | $R^2$, adjusted $R^2$, overfitting | 14.5 |
| What if two predictors say the same thing? | multicollinearity and VIF | 14.6 |

**1. One equation, several slopes.** With $p$ predictors the model is

$$\hat y = b_0 + b_1x_1 + b_2x_2 + \dots + b_px_p$$

$b_0$ is the intercept and each $b_j$ is a slope.

**2. Each slope is an "all else equal" change.** $b_1$ is how much $\hat y$ changes when $x_1$ goes up by 1 **while every other predictor stays the same**. This is the big difference from Chapter 13. A slope in a multiple regression is a comparison *inside* the model, between cases that differ only in that one predictor.

**3. Same fitting rule as Lesson 13.1.** The coefficients are again chosen by **least squares**: make the sum of squared residuals as small as possible.

$$\text{SSE} = \sum (y - \hat y)^2$$

This is the same SSE (sum of squared errors) as in Lesson 13.1. With one predictor the best fit is a line. With two numerical predictors it is a flat **plane**. With more it is a "hyperplane" that we can't draw, but the rule doesn't change.

![Three panels. Left: preparation time against batch size with one fitted line. Middle: a 3-D scatter of time against batch size and staff experience, with a fitted orange plane and red residual sticks. Right: the design matrix, a table with a y column and columns 1, x1, x2, boxed as K = 3 columns for 3 coefficients](figures/multiple_regression_idea.png)

Left: with one predictor, least squares fits a line. Middle: with two numerical predictors it fits a plane. The red sticks are the residuals, and least squares makes their squares add up to as little as possible. Right: what the software works with. A column of 1s (for the intercept) plus one column per predictor.

**4. Count the coefficients: $K$.** $K$ is the number of coefficients **including the intercept**, so $K = p + 1$. Two things are needed:

- **No redundant columns.** No predictor may be an exact combination of the others. Mass in kilograms and mass in grams together carry the same information twice, and the software can't split the effect between them (Lesson 14.6).
- **More rows than coefficients**, $n > K$. The leftover variation is measured with $n - K$ degrees of freedom, just like the $n - 1$ of the sample variance (Lesson 3.13). In practice you want many more rows than coefficients.

**5. Software does the arithmetic.** For one predictor you can fill in Lesson 13.1's table by hand. For several predictors the formulas are matrix algebra (Lesson 18.7), so we let Excel or Python do it. The important skill is **reading** the result.

---

## Goal

Write a model with several predictors, read what each coefficient means, and use the fitted equation to make predictions.

## The model

| Symbol | Meaning |
|---|---|
| $y$ | the response (what we predict) |
| $x_1, \dots, x_p$ | the $p$ predictors |
| $b_0$ | intercept: $\hat y$ when every predictor is 0 |
| $b_j$ | slope of $x_j$: change in $\hat y$ when $x_j$ rises by 1 and the other predictors stay fixed |
| $K = p + 1$ | number of coefficients |
| $s^2 = \dfrac{\text{SSE}}{n - K}$ | estimate of the noise variance around the fitted plane |

---

## Example

A workshop fits a model for preparation time (minutes) using two predictors:

- $x$ = batch size **minus 5** (so $x = 0$ means a batch of 5 items, $x = 1$ means 6 items)
- $z$ = 1 if the batch is coated, 0 if not

The fitted equation (Lesson 14.2 shows where it comes from) is

$$\hat y = 10 + 2x + 3z$$

**Reading the coefficients:**

- $b_0 = 10$: an **uncoated** batch of **5 items** ($x = 0$, $z = 0$) is predicted to take 10 minutes.
- $b_1 = 2$: for batches with the **same coating**, one extra item adds 2 minutes.
- $b_2 = 3$: for batches of the **same size**, coating adds 3 minutes.

**Why subtract 5?** This is called **centring**. Without it the intercept would describe a batch of 0 items, which doesn't exist. After centring, $b_0$ describes a typical batch. The slopes don't change.

**Predictions:**

| Batch | $x$ | $z$ | $\hat y = 10 + 2x + 3z$ |
|---|---:|---:|---:|
| 6 items, uncoated | 1 | 0 | $10 + 2(1) + 3(0) = 12$ |
| 4 items, coated | −1 | 1 | $10 + 2(-1) + 3(1) = 11$ |
| 8 items, coated | 3 | 1 | $10 + 2(3) + 3(1) = 19$ |

The last row is a warning sign. If the data only had batches of 4 to 6 items, predicting a batch of 8 is **extrapolation** (Lesson 13.1). The model can't show that the straight-line pattern continues.

---

## Doing it in Excel

Put $y$ in column A and the predictors side by side in columns B and C (rows 2 to 9).

| Want | How | Result |
|---|---|---|
| All coefficients at once | `=LINEST(A2:A9, B2:C9)` | returns $b_2, b_1, b_0$ (**right to left!**) |
| Full output (SEs, $R^2$, F) | `=LINEST(A2:A9, B2:C9, TRUE, TRUE)` or *Data → Data Analysis → Regression* | a table |

---

## Your turn

A data set has temperature in Celsius ($C$) as one predictor. Someone also adds temperature in Fahrenheit, $F = 32 + 1.8C$, as a second predictor, and the model has an intercept. Why can't the software find unique coefficients?

**Answer:** The Fahrenheit column is an exact combination of the intercept column (all 1s, times 32) and the Celsius column (times 1.8). The columns are redundant, so infinitely many coefficient combinations give the same predictions. Keep only one temperature column.

---

## Key takeaways

- Multiple regression: $\hat y = b_0 + b_1x_1 + \dots + b_px_p$, fitted by least squares, the same rule as Lesson 13.1.
- Each slope is the change in $\hat y$ when that predictor rises by 1 **and the others stay fixed**.
- $K$ = number of coefficients including the intercept. You need $n > K$ and no redundant predictor columns.
- Centring a predictor (subtracting a typical value) makes the intercept meaningful without changing the slopes.
- Predict only inside the range of the data.

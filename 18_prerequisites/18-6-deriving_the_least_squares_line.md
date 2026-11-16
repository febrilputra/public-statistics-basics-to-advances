# Lesson 18.6 - Deriving the Least Squares Line

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Appendices A–F (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 18 - Mathematical and Python Prerequisites

## The big picture: where Lesson 13.1's formulas come from

Lesson 13.1 gave formulas for the slope and intercept of the best line. This lesson **derives** them with the tools of Lesson 18.5.

**1. The quantity to minimise.** For a line $\hat y = mx + b$,

$$\text{SSE}(m, b) = \sum_{i=1}^n (y_i - mx_i - b)^2$$

SSE depends on **two** numbers, $m$ and $b$. Picture it as a bowl over the $(m, b)$ plane. We want the bottom of the bowl.

**2. Partial derivatives.** With two unknowns, differentiate with respect to one while holding the other fixed. That's a **partial derivative**, written $\partial$. Using the chain rule on each squared term:

$$\frac{\partial\,\text{SSE}}{\partial b} = -2\sum (y_i - mx_i - b), \qquad \frac{\partial\,\text{SSE}}{\partial m} = -2\sum x_i(y_i - mx_i - b)$$

**3. Set both to 0** (the bottom of the bowl is flat in every direction). These are the **normal equations**:

$$\sum (y_i - mx_i - b) = 0, \qquad \sum x_i(y_i - mx_i - b) = 0$$

**4. Solve.** The first equation gives $\sum y_i = m\sum x_i + nb$, so

$$\hat b = \bar y - \hat m\,\bar x$$

(the line passes through $(\bar x, \bar y)$). Substitute this into the second equation and rearrange using deviations from the means:

$$\hat m = \frac{S_{xy}}{S_{xx}} = \frac{\sum (x_i - \bar x)(y_i - \bar y)}{\sum (x_i - \bar x)^2}$$

This is the same as Lesson 13.1's $m = \dfrac{n\sum xy - \sum x\sum y}{n\sum x^2 - (\sum x)^2}$. Multiply the top and bottom of $S_{xy}/S_{xx}$ by $n$ and you get exactly that.

![Left: four points (0, 1), (1, 2), (2, 2), (3, 4) with the line ŷ = 0.9 + 0.9x, residuals +0.1, +0.2, −0.7, +0.4, and the point of means (1.5, 2.25) on the line. Right: contour lines of SSE over slope m and intercept b, forming nested ellipses around a star at m = 0.9, b = 0.9 where the minimum SSE is 0.7](figures/least_squares_derivation.png)

Left: the fitted line and its residuals. They add to 0, and their squares add to 0.7. Right: SSE as a contour map over all possible $(b, m)$. It is a bowl with a single lowest point at $b = 0.9$, $m = 0.9$.

**5. What the normal equations also tell us.** With an intercept in the model, the residuals $e_i = y_i - \hat y_i$ satisfy

$$\sum e_i = 0 \quad \text{and} \quad \sum x_i e_i = 0$$

The residuals add to 0, and they are unrelated to $x$ in the training data. These are **algebraic facts** of least squares, not evidence that the model's assumptions are right.

**6. When it fails.** If every $x_i$ is the same, $S_{xx} = 0$ and the slope can't be estimated, because you can't learn how $y$ changes with $x$ if $x$ never changes.

---

## Goal

Derive the least squares slope and intercept, and use the deviation formulas to fit a line by hand.

## Formulas

$$\hat m = \frac{S_{xy}}{S_{xx}}, \qquad \hat b = \bar y - \hat m\,\bar x, \qquad S_{xy} = \sum(x - \bar x)(y - \bar y), \quad S_{xx} = \sum (x - \bar x)^2$$

---

## Example

$x = (0, 1, 2, 3)$, $y = (1, 2, 2, 4)$.

**Step 1: means.** $\bar x = 6/4 = 1.5$, $\bar y = 9/4 = 2.25$.

**Step 2: deviations.**

| $x$ | $y$ | $x - \bar x$ | $y - \bar y$ | $(x - \bar x)(y - \bar y)$ | $(x - \bar x)^2$ |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | −1.5 | −1.25 | 1.875 | 2.25 |
| 1 | 2 | −0.5 | −0.25 | 0.125 | 0.25 |
| 2 | 2 | 0.5 | −0.25 | −0.125 | 0.25 |
| 3 | 4 | 1.5 | 1.75 | 2.625 | 2.25 |
| | | | **Sum** | **4.5** | **5** |

**Step 3: slope and intercept.**
$$\hat m = \frac{4.5}{5} = 0.9, \qquad \hat b = 2.25 - 0.9(1.5) = 0.9$$
$$\boxed{\hat y = 0.9 + 0.9x}$$

**Step 4: residuals and SSE.** Fitted values: 0.9, 1.8, 2.7, 3.6. Residuals: 0.1, 0.2, −0.7, 0.4.
$$\text{SSE} = 0.01 + 0.04 + 0.49 + 0.16 = 0.7$$

**Step 5: check the normal equations.** $\sum e = 0.1 + 0.2 - 0.7 + 0.4 = 0$ ✓ and $\sum xe = 0 + 0.2 - 1.4 + 1.2 = 0$ ✓.

---

## Doing it in Excel

`=SLOPE(B2:B5, A2:A5)` → 0.9, `=INTERCEPT(B2:B5, A2:A5)` → 0.9, and `=DEVSQ(A2:A5)` gives $S_{xx}$ = 5.

---

## Your turn

For $x = (0, 1, 2)$ and $y = (2, 3, 5)$, find the least squares intercept, slope, SSE and $R^2$.

**Answer:** $\bar x = 1$, $\bar y = 10/3$, $S_{xx} = 2$, $S_{xy} = (-1)(-4/3) + 0 + (1)(5/3) = 3$.
$\hat m = 3/2 = 1.5$ and $\hat b = 10/3 - 1.5 = 11/6 \approx 1.833$.
Residuals: $1/6, -1/3, 1/6$, so $\text{SSE} = 1/36 + 1/9 + 1/36 = 1/6$.
$\text{TSS} = 14/3$, so $R^2 = 1 - (1/6)/(14/3) = 27/28 \approx 0.964$.

---

## Key takeaways

- Least squares minimises $\text{SSE}(m, b) = \sum (y - mx - b)^2$, a bowl with one lowest point.
- Setting both partial derivatives to 0 gives the normal equations.
- $\hat m = S_{xy}/S_{xx}$ and $\hat b = \bar y - \hat m\bar x$: the line passes through $(\bar x, \bar y)$.
- With an intercept, residuals sum to 0 and are uncorrelated with $x$ in the training data.
- If $x$ never varies ($S_{xx} = 0$), the slope can't be estimated.

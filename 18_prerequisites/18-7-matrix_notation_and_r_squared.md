# Lesson 18.7 - Matrix Notation and R²

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Appendices A–F (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 18 - Mathematical and Python Prerequisites

## The big picture: one formula for every linear model

**1. Stack the data into matrices.** Any linear regression (one predictor, many predictors, dummies, interactions) can be written as

$$\mathbf y = X\boldsymbol\beta + \boldsymbol\varepsilon$$

- $\mathbf y$: the column of $n$ responses
- $X$: the **design matrix**, $n$ rows and $K$ columns. The first column is all 1s (for the intercept), then one column per predictor (Lesson 14.1).
- $\boldsymbol\beta$: the $K$ coefficients
- $\boldsymbol\varepsilon$: the $n$ errors

**2. The least squares solution.** The normal equations of Lesson 18.6, written for all coefficients at once, are

$$X^\top X\,\hat{\boldsymbol\beta} = X^\top\mathbf y \quad\Rightarrow\quad \hat{\boldsymbol\beta} = (X^\top X)^{-1}X^\top\mathbf y$$

($X^\top$ is the **transpose**: rows become columns.) The formula is great for understanding. In practice software uses a numerically stable least squares solver (e.g. `np.linalg.lstsq`) instead of computing the inverse.

**3. Identifiability: full rank.** Unique coefficients need $X$ to have **full column rank**: no column can be built from the others. Exact duplicates (kg and g, Celsius and Fahrenheit), or an intercept plus a dummy for **every** category (Lesson 14.2), break this. Estimating the noise variance also needs $n > K$.

![Left: the matrix equation for the four-point example: y = (1, 2, 2, 4) equals X with rows (1, 0), (1, 1), (1, 2), (1, 3) times β̂ = (0.9, 0.9) plus residuals e = (0.1, 0.2, −0.7, 0.4); a side note gives XᵀX = [4 6; 6 14], Xᵀy = [9; 18] and β̂ = (XᵀX)⁻¹Xᵀy. Right: two bars, R² = 1 − 0.7/4.75 = 0.853 and adjusted R² = 1 − (0.7/2)/(4.75/3) = 0.779](figures/matrix_notation.png)

Left: the whole regression of Lesson 18.6 in matrix form. Right: $R^2$ and adjusted $R^2$ differ only in what SSE and TSS are divided by.

**4. $R^2$ and the denominator trap.** With $\text{TSS} = \sum(y - \bar y)^2$:

$$R^2 = 1 - \frac{\text{SSE}}{\text{TSS}}$$

Dividing **both** SSE and TSS by the same $n$ (turning them into mean squared errors) leaves $R^2$ unchanged. Dividing each by its own **degrees of freedom** turns them into variance estimates, and gives **adjusted** $R^2$ (Lesson 14.5):

$$\bar R^2 = 1 - \frac{\text{SSE}/(n - K)}{\text{TSS}/(n - 1)}$$

So whenever you see "MSE", ask what it was divided by and why.

---

## Goal

Write a regression in matrix form, solve the normal equations for a small example, and compute $R^2$ and adjusted $R^2$.

## Formulas

$$\hat{\boldsymbol\beta} = (X^\top X)^{-1}X^\top\mathbf y, \qquad R^2 = 1 - \frac{\text{SSE}}{\text{TSS}}, \qquad \bar R^2 = 1 - \frac{\text{SSE}/(n - K)}{\text{TSS}/(n - 1)}$$

For a 2×2 matrix: $\begin{bmatrix}p & q\\ r & s\end{bmatrix}^{-1} = \dfrac{1}{ps - qr}\begin{bmatrix}s & -q\\ -r & p\end{bmatrix}$.

---

## Example

The four points of Lesson 18.6: $x = (0, 1, 2, 3)$, $y = (1, 2, 2, 4)$, so $n = 4$, $K = 2$.

**Step 1: design matrix.**
$$X = \begin{bmatrix}1 & 0\\1 & 1\\1 & 2\\1 & 3\end{bmatrix}, \qquad \mathbf y = \begin{bmatrix}1\\2\\2\\4\end{bmatrix}$$

**Step 2: $X^\top X$ and $X^\top\mathbf y$.**
$$X^\top X = \begin{bmatrix} n & \sum x\\ \sum x & \sum x^2\end{bmatrix} = \begin{bmatrix}4 & 6\\6 & 14\end{bmatrix}, \qquad X^\top\mathbf y = \begin{bmatrix}\sum y\\ \sum xy\end{bmatrix} = \begin{bmatrix}9\\18\end{bmatrix}$$

**Step 3: invert and multiply.** $\det = 4(14) - 6(6) = 20$.
$$\hat{\boldsymbol\beta} = \frac{1}{20}\begin{bmatrix}14 & -6\\-6 & 4\end{bmatrix}\begin{bmatrix}9\\18\end{bmatrix} = \frac{1}{20}\begin{bmatrix}126 - 108\\-54 + 72\end{bmatrix} = \begin{bmatrix}0.9\\0.9\end{bmatrix}$$

The same line as Lesson 18.6: $\hat y = 0.9 + 0.9x$.

**Step 4: $R^2$.** $\text{SSE} = 0.7$. $\bar y = 2.25$, so
$$\text{TSS} = 1.5625 + 0.0625 + 0.0625 + 3.0625 = 4.75$$
$$R^2 = 1 - \frac{0.7}{4.75} = 0.853$$

**Step 5: adjusted $R^2$.**
$$\bar R^2 = 1 - \frac{0.7/2}{4.75/3} = 1 - \frac{0.35}{1.583} = 0.779$$

---

## Doing it in Excel

`=MMULT(MINVERSE(MMULT(TRANSPOSE(X),X)), MMULT(TRANSPOSE(X),y))` with X = the two columns (1s and x) returns $\hat{\boldsymbol\beta}$. `=LINEST(y, x)` gives the same coefficients directly.

---

## Your turn

A model has an intercept and dummies for **all three** colours (red, green, blue). Why does $X^\top X$ have no inverse?

**Answer:** In every row the three dummies add up to 1, which is exactly the intercept column. The columns are linearly dependent, so $X$ doesn't have full rank, $\det(X^\top X) = 0$, and the coefficients aren't unique. Drop one dummy (use a reference colour).

---

## Key takeaways

- Every linear model is $\mathbf y = X\boldsymbol\beta + \boldsymbol\varepsilon$, with a column of 1s for the intercept.
- $\hat{\boldsymbol\beta} = (X^\top X)^{-1}X^\top\mathbf y$ solves the normal equations. Software uses a stable solver.
- Unique coefficients need full column rank (no redundant columns), and variance estimation needs $n > K$.
- $R^2 = 1 - \text{SSE}/\text{TSS}$. Dividing by degrees of freedom instead gives adjusted $R^2$.

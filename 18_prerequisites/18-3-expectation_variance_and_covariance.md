# Lesson 18.3 - Expectation, Variance, and Covariance

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Appendices A–F (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 18 - Mathematical and Python Prerequisites

## The big picture: the rules behind every standard error

**1. Expectation is a probability-weighted average** (Lesson 5.9):

$$E(X) = \sum x\,P(X = x) \quad \text{(discrete)}, \qquad E(X) = \int x f(x)\,dx \quad \text{(continuous)}$$

It is the long-run average, not necessarily a value $X$ can take. The expected value of a die roll, 3.5, never comes up.

**2. Variance and covariance:**

$$\text{Var}(X) = E\big((X - E(X))^2\big) = E(X^2) - (E(X))^2$$

$$\text{Cov}(X, Y) = E\big((X - E(X))(Y - E(Y))\big)$$

Covariance is positive when $X$ and $Y$ tend to be above (or below) their means together (Lesson 13.2).

**3. Expectation is always simple.** For any constants $a, b, c$, **whether or not $X$ and $Y$ are related**:

$$E(aX + bY + c) = aE(X) + bE(Y) + c$$

**4. Variance needs the covariance.**

$$\text{Var}(aX + bY) = a^2\,\text{Var}(X) + b^2\,\text{Var}(Y) + 2ab\,\text{Cov}(X, Y)$$

Constants come out **squared**. Adding a constant doesn't change the variance. Dropping the covariance term is only allowed when $\text{Cov}(X, Y) = 0$.

![Three panels. A: a scatter of 600 (X, Y) pairs with positive covariance, correlation 0.5. B: a histogram of X − Y with the correct normal curve of variance 4 + 9 − 2·3 = 7 and a wider dashed curve of variance 13 that ignores the covariance; the simulated variance is 7.03. C: points on the parabola Y = X² for X from −1 to 1, labelled Cov(X, Y) = 0 but Y is completely determined by X](figures/variance_rules.png)

A: $X$ and $Y$ move together. B: because of that, $X - Y$ varies **less** than you'd guess by adding the variances (7, not 13). C: zero covariance does **not** mean independence. $Y = X^2$ is fully determined by $X$, but the left and right halves cancel, so the covariance is 0.

**5. The most important consequence: the standard error of a mean.** For $n$ **independent** observations, each with variance $\sigma^2$:

$$\text{Var}(\bar X) = \text{Var}\!\left(\frac1n\sum X_i\right) = \frac{1}{n^2}\sum \text{Var}(X_i) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}, \qquad \text{SE}(\bar X) = \frac{\sigma}{\sqrt n}$$

This is the $\sigma/\sqrt n$ of Lesson 8.5. If the observations are **correlated** (repeated measurements of the same unit, clusters), the covariance terms don't vanish, and treating the rows as independent understates the uncertainty. That's why paired and clustered designs need their own methods.

---

## Goal

Use the rules for expectation and variance of combinations, and derive the standard error of a mean.

## Formulas

| Rule | Formula |
|---|---|
| linearity of expectation | $E(aX + bY + c) = aE(X) + bE(Y) + c$ |
| variance of a combination | $\text{Var}(aX + bY) = a^2\text{Var}X + b^2\text{Var}Y + 2ab\,\text{Cov}(X, Y)$ |
| independent ⇒ | $\text{Cov}(X, Y) = 0$ (not the other way round) |
| mean of $n$ independent | $\text{Var}(\bar X) = \sigma^2/n$ |

---

## Example

$\text{Var}(X) = 4$, $\text{Var}(Y) = 9$, $\text{Cov}(X, Y) = 3$.

**Step 1: variance of the difference.** $a = 1$, $b = -1$:
$$\text{Var}(X - Y) = 4 + 9 + 2(1)(-1)(3) = 13 - 6 = 7$$

**Step 2: what if we wrongly assume independence?** $4 + 9 = 13$, which is almost twice too big.

**Step 3: variance of the sum.**
$$\text{Var}(X + Y) = 4 + 9 + 2(3) = 19$$

**Step 4: scaling.**
$$\text{Var}(3X) = 9 \times 4 = 36, \qquad \text{Var}(X + 10) = 4$$

**Step 5: correlation.**
$$r = \frac{\text{Cov}}{\sigma_X\sigma_Y} = \frac{3}{2 \times 3} = 0.5$$

**Why this matters for paired data** (Lesson 11.4): before/after measurements on the same unit are positively correlated. The variance of the difference is smaller than the sum of the variances, which is why a paired test can be much more powerful than an independent-groups test.

---

## Doing it in Excel

For data columns: `=VAR.S(A:A)`, `=COVARIANCE.S(A:A,B:B)`. Check the rule: `=VAR.S(C:C)` where `C = A − B` equals `VAR.S(A) + VAR.S(B) − 2*COVARIANCE.S(A,B)`.

---

## Your turn

Two variables have variances 4 and 9 and covariance 3. Find the variance of their difference. What would an independence assumption change?

**Answer:** $4 + 9 - 2(3) = 7$. Assuming independence removes the covariance term and gives 13, overstating the variance of the difference. Use the actual dependence structure.

---

## Key takeaways

- Expectation is linear, always: $E(aX + bY) = aE(X) + bE(Y)$.
- $\text{Var}(aX + bY) = a^2\text{Var}X + b^2\text{Var}Y + 2ab\,\text{Cov}(X, Y)$. Constants come out squared.
- Independence ⇒ zero covariance, but zero covariance does not imply independence.
- For $n$ independent observations, $\text{Var}(\bar X) = \sigma^2/n$, so $\text{SE} = \sigma/\sqrt n$.
- Correlated observations (pairs, clusters) need the covariance terms.

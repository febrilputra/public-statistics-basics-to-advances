# Lesson 18.1 - Sums, Products, and Logarithms

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Appendices A–F (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 18 - Mathematical and Python Prerequisites

## The big picture: the notation behind every formula

This chapter is a toolbox. It collects the maths and Python ideas used in Chapters 13–17, so you can come back to it whenever a symbol or step looks unfamiliar.

| Tool | Used in | Lesson |
|---|---|---|
| $\sum$, $\prod$, factorials, logs | every formula, likelihood | 18.1 (this one) |
| conditional probability, Bayes | p-values, power, screening | 18.2 |
| expectation, variance, covariance | standard errors, paired data | 18.3 |
| law of large numbers, CLT | sampling distributions, simulation | 18.4 |
| derivatives, chain rule | least squares | 18.5 |
| deriving the least squares line | Lesson 13.1, Chapter 14 | 18.6 |
| matrix notation, $R^2$ | multiple regression | 18.7 |
| arrays and reproducible code | simulations | 18.8 |

**1. $\sum$ means "add up", $\prod$ means "multiply".** For observations $x_1, \dots, x_n$:

$$\sum_{i=1}^n x_i = x_1 + x_2 + \dots + x_n, \qquad \prod_{i=1}^n x_i = x_1 \times x_2 \times \dots \times x_n$$

**2. Where the square goes matters.** $\sum x_i^2$ squares **each** value and then adds. $\left(\sum x_i\right)^2$ adds first and then squares. They are different numbers, and Lesson 13.1's formulas use both.

**3. Deviations from the mean always add to 0.** $\sum (x_i - \bar x) = 0$, because the positives and negatives cancel exactly. That's why variance **squares** the deviations before adding (Lesson 3.13).

![Three panels. Left: three small squares of areas 1, 4 and 16 adding to Σx² = 21, next to one big 7-by-7 square for (Σx)² = 49. Middle: bars of the deviations of 1, 2, 4 from their mean 2.33: −1.33, −0.33 and +1.67, which add to 0; their squares add to 4.67. Right: a bar split into log 0.1 = −2.30, log 0.2 = −1.61 and log 0.5 = −0.69, which add to log 0.01 = −4.61](figures/sums_squares_and_logs.png)

Left: for $x = (1, 2, 4)$, squaring first gives 21, and adding first gives 49. Middle: the deviations add to exactly 0, so we square them. Right: the log of a product is the sum of the logs.

**4. Factorials and combinations.** $n! = n(n - 1)\cdots 1$, with $0! = 1$. The number of ways to choose $k$ items from $n$, ignoring order, is

$$\binom{n}{k} = \frac{n!}{k!\,(n - k)!}$$

used in the binomial distribution (Lesson 6.2) and for counting pairs, $\binom{g}{2}$, in Lesson 17.3.

**5. Logarithms turn products into sums.** The natural log $\ln$ (written $\log$ in statistics) undoes $e^x$. For positive $a$ and $b$:

$$\log(ab) = \log a + \log b, \qquad \log(a/b) = \log a - \log b, \qquad \log(a^k) = k\log a$$

But $\log(a + b) \ne \log a + \log b$. **Why statisticians love logs:** the likelihood of independent data is a **product** of many small probabilities. That product can become too small for a computer to store. The **log-likelihood** is a **sum**, which is easy to handle, and the value that maximises it is the same, because log only ever increases.

---

## Goal

Read and evaluate sums, products, factorials, combinations and logarithms correctly.

## Formulas

$$\sum x_i^2 \ne \left(\sum x_i\right)^2, \qquad \sum (x_i - \bar x) = 0, \qquad \binom nk = \frac{n!}{k!(n - k)!}$$

$$\log(ab) = \log a + \log b, \qquad \log\prod p_i = \sum \log p_i$$

---

## Example

Let $x = (1, 2, 4)$.

**Step 1: $\sum x_i^2$.** $1 + 4 + 16 = 21$

**Step 2: $(\sum x_i)^2$.** $(1 + 2 + 4)^2 = 7^2 = 49$

**Step 3: deviations.** $\bar x = 7/3 = 2.333$. Deviations: $-1.333$, $-0.333$, $+1.667$. Sum: $0$. Sum of squares:
$$1.778 + 0.111 + 2.778 = 4.667$$

**Step 4: a combination.** Choosing 2 of 5 objects: $\binom52 = \dfrac{5!}{2!\,3!} = \dfrac{120}{2 \times 6} = 10$.

**Step 5: a log-likelihood.** Three independent events with probabilities 0.5, 0.2, 0.1:

$$\text{likelihood} = 0.5 \times 0.2 \times 0.1 = 0.01$$
$$\text{log-likelihood} = \log 0.5 + \log 0.2 + \log 0.1 = -0.693 - 1.609 - 2.303 = -4.605 = \log 0.01 \checkmark$$

**In Python:** `x**2` squares (elementwise for arrays). `x^2` does **not**: in Python `^` is a bitwise operation. `x.sum()**2` squares the sum.

---

## Doing it in Excel

| Want | Formula |
|---|---|
| $\sum x^2$ | `=SUMSQ(A2:A4)` → 21 |
| $(\sum x)^2$ | `=SUM(A2:A4)^2` → 49 |
| $\binom52$ | `=COMBIN(5,2)` → 10 |
| natural log | `=LN(0.01)` → −4.605 |

---

## Your turn

For $x = (2, 3, 5)$, find $\sum x_i^2$, $(\sum x_i)^2$ and $\sum (x_i - \bar x)$.

**Answer:** $4 + 9 + 25 = 38$. $(2 + 3 + 5)^2 = 100$. $\sum(x_i - \bar x) = 0$, as always (in code it may show as a tiny number like $10^{-16}$ because of rounding).

---

## Key takeaways

- $\sum$ adds, $\prod$ multiplies. Parentheses decide whether you square before or after adding.
- Deviations from the mean always add to 0, so variance squares them.
- $\binom nk$ counts unordered choices.
- $\log(ab) = \log a + \log b$, which turns likelihood products into sums. But $\log(a + b) \ne \log a + \log b$.
- Python: `**` is a power, `^` is not.

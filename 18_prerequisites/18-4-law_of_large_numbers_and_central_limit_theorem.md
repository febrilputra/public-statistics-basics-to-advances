# Lesson 18.4 - The Law of Large Numbers and the Central Limit Theorem

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Appendices A–F (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 18 - Mathematical and Python Prerequisites

## The big picture: two different promises about the sample mean

Lessons 8.3 and 8.4 introduced these two theorems. This lesson puts them side by side, because they are often mixed up.

**1. Law of large numbers (LLN): where the mean goes.** For independent observations from the same distribution with mean $\mu$, the sample mean $\bar x_n$ gets closer and closer to $\mu$ as $n$ grows. It is the reason a long-run average, a simulation estimate (Lesson 15.5) or a casino's profit is predictable.

**2. Central limit theorem (CLT): the shape of the error.** For independent observations with mean $\mu$ and a finite, non-zero SD $\sigma$:

$$\frac{\bar X - \mu}{\sigma/\sqrt n} \;\approx\; N(0, 1) \quad \text{for large } n$$

The **distribution of the sample mean** becomes approximately normal, centred at $\mu$, with standard deviation $\sigma/\sqrt n$ (Lesson 18.3). This is what justifies z- and t-based intervals and tests for means even when the raw data aren't normal.

![Four panels for exponential waiting times with mean 2. LLN: three running means that wander at first and then settle on the dashed line at 2. CLT n = 1: a histogram that is strongly right-skewed. CLT n = 5: the histogram of means is less skewed, with a normal curve of SD 0.89 overlaid. CLT n = 30: the histogram of means is close to the normal curve with SD 0.37](figures/lln_and_clt.png)

Left: three running means start far apart and settle on 2 (the LLN). Right three panels: averaging 1, 5 and 30 skewed waiting times. The distribution of the **mean** narrows like $2/\sqrt n$ and looks more normal as $n$ grows (the CLT).

**3. What the theorems do NOT say.**

- They say nothing about the **raw data** becoming normal. Individual waiting times stay skewed forever.
- There is **no magic $n = 30$**. How large $n$ must be depends on how skewed or heavy-tailed the data are. Mild skew may need 10, extreme skew or outliers may need hundreds.
- They need **independence** (or limited dependence). Clustered or time-series data need more care.
- The simulation in the figure uses the **known** $\sigma = 2$. Replacing $\sigma$ with the sample SD $s$ is what leads to the t distribution (Lesson 9.3).

---

## Goal

State the LLN and the CLT, tell them apart, and compute the SD of a sample mean.

## Formulas

$$\bar X_n \to \mu \quad \text{(LLN)}, \qquad \bar X \approx N\!\left(\mu,\ \frac{\sigma}{\sqrt n}\right) \quad \text{(CLT, large } n)$$

---

## Example

Waiting times follow an exponential distribution with mean $\mu = 2$ minutes and SD $\sigma = 2$ minutes. The distribution is strongly right-skewed (skewness 2).

**Step 1: the SD of the mean for several $n$.**

| $n$ | SD of $\bar x$ = $2/\sqrt n$ | Skewness of $\bar x$ = $2/\sqrt n$ |
|---:|---:|---:|
| 1 | 2.00 | 2.00 (very skewed) |
| 5 | 0.89 | 0.89 |
| 30 | 0.37 | 0.37 (mild) |
| 100 | 0.20 | 0.20 |

(For exponential data the skewness of the mean also shrinks like $2/\sqrt n$.)

**Step 2: a probability using the CLT.** For $n = 30$, what is $P(\bar x > 2.5)$?
$$z = \frac{2.5 - 2}{0.365} = 1.37, \qquad P(Z > 1.37) = 0.085$$

So about 8.5% of samples of 30 waiting times would average more than 2.5 minutes. Because a little skew remains at $n = 30$, the exact value is slightly different (about 0.09). That's the "approximately" in the CLT.

**Step 3: the LLN in action.** Each running mean in the left panel wanders a lot for the first 10–20 observations, then stays within a few tenths of 2 after about 1,000.

---

## Doing it in Excel

`=2/SQRT(30)` → 0.365. `=1-NORM.DIST(2.5, 2, 2/SQRT(30), TRUE)` → 0.085. To see the CLT, fill 30 columns with `=-2*LN(RAND())` (exponential, mean 2), average each row, and make a histogram of the averages.

---

## Your turn

For the same waiting times, what is the SD of the mean of $n = 100$ observations? Roughly what range covers the middle 95% of such means?

**Answer:** $2/\sqrt{100} = 0.2$. By the CLT, about 95% of means fall within $2 \pm 1.96(0.2)$, i.e. between **1.61 and 2.39** minutes.

---

## Key takeaways

- LLN: the sample mean settles at $\mu$ as $n$ grows.
- CLT: the sample mean's distribution is approximately normal with SD $\sigma/\sqrt n$.
- Neither makes the raw data normal, and there is no universal "$n = 30$" rule.
- Both need independent observations. Skewed or heavy-tailed data need larger $n$.
- Replacing the unknown $\sigma$ with $s$ leads to the t distribution.

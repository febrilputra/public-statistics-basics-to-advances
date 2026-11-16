# Lesson 13.2 - How to Calculate the Covariance

> **Video:** [How To Calculate The Covariance Between X and Y](https://www.youtube.com/watch?v=rb2nU7YZV_I) by The Organic Chemistry Tutor
> **Chapter:** [13 - Regression & Correlation](https://www.video-tutor.net/linear-regression.html)

## The big picture: do $x$ and $y$ move together?

Covariance answers one question: **when $x$ is above its average, is $y$ usually above its average too?**

**1. Start from variance.** The variance (Lesson 3.13) averages the squared deviations of **one** variable:

$$s_x^2 = \frac{\sum (x - \bar x)(x - \bar x)}{n - 1}$$

Covariance swaps the second factor for the deviation of the **other** variable:

$$\text{cov}(x, y) = \frac{\sum (x - \bar x)(y - \bar y)}{n - 1}$$

So covariance is "variance for two variables". In fact, $\text{cov}(x, x) = s_x^2$.

**2. Each point gives a signed rectangle.** The product $(x - \bar x)(y - \bar y)$ is the area of the rectangle between the point and the point of means $(\bar x, \bar y)$, with a sign:

| Where the point is | $x - \bar x$ | $y - \bar y$ | Product |
|---|---|---|---|
| up and right of the means | $+$ | $+$ | $+$ |
| down and left | $-$ | $-$ | $+$ |
| up and left, or down and right | opposite signs | | $-$ |

**3. Add them up.** If most points are up-right or down-left, the positive rectangles win and the covariance is **positive**. If most are up-left or down-right, it is **negative**. If they balance, it is **close to 0**.

![Two scatter plots. Left: Example 1, where every point makes a green (positive) rectangle with the point of means (6, 10.2); the products add up to 70, so cov = 70/4 = 17.5. Right: a set with no clear pattern, where green and red rectangles cancel; the products add up to −2, so cov = −0.5, about 0. A box notes that cov(x, x) = var(x) and that the size of the covariance depends on the units](figures/covariance_as_rectangles.png)

Left: in Example 1 every rectangle is positive, so they add up to a big positive total. Right: when there's no pattern, positive and negative rectangles cancel and the covariance is near 0.

**4. Why divide by $n - 1$?** For the same reason as the sample variance: the deviations are measured from the sample means, which uses up one degree of freedom.

**5. The catch: units.** Covariance has units of (units of $x$) × (units of $y$). Measure $y$ in centimetres instead of metres and the covariance becomes 100 times bigger, even though the pattern hasn't changed. So the **sign** is meaningful, but the **size** is hard to judge. Lessons 13.3 and 13.4 fix this with the correlation coefficient $r$, which divides the covariance by both standard deviations.

---

## Formula

$$\text{cov}(x, y) = \frac{\sum (x - \bar x)(y - \bar y)}{n - 1} \quad\text{(sample)}$$

For a **population**, divide by $N$ instead of $n - 1$.

## Steps (table method)

1. Columns: $x$, $y$, $x - \bar x$, $y - \bar y$, $(x - \bar x)(y - \bar y)$.
2. Find $\bar x$ and $\bar y$.
3. Fill in the deviation columns. Each one sums to 0, which is a useful check.
4. Multiply the deviations row by row and add the products.
5. Divide by $n - 1$.

---

## Example 1 - positive covariance

| $x$ | $y$ | $x - \bar x$ | $y - \bar y$ | product |
|---:|---:|---:|---:|---:|
| 2 | 3 | −4 | −7.2 | 28.8 |
| 4 | 7 | −2 | −3.2 | 6.4 |
| 6 | 10 | 0 | −0.2 | 0 |
| 8 | 14 | 2 | 3.8 | 7.6 |
| 10 | 17 | 4 | 6.8 | 27.2 |
| **Sum 30** | **Sum 51** | 0 | 0 | **70** |

$\bar x = \sum x / n = 30/5 = 6$, $\;\bar y = \sum y / n = 51/5 = 10.2$

$$\text{cov}(x, y) = \frac{\sum (x - \bar x)(y - \bar y)}{n - 1} = \frac{70}{5 - 1} = 17.5$$

---

## Example 2 - negative covariance

| $x$ | $y$ | $x - \bar x$ | $y - \bar y$ | product |
|---:|---:|---:|---:|---:|
| 3 | 20 | −6 | 7.4 | −44.4 |
| 6 | 17 | −3 | 4.4 | −13.2 |
| 9 | 13 | 0 | 0.4 | 0 |
| 12 | 9 | 3 | −3.6 | −10.8 |
| 15 | 4 | 6 | −8.6 | −51.6 |
| **Sum 45** | **Sum 63** | 0 | 0 | **−120** |

$\bar x = \sum x / n = 45/5 = 9$, $\;\bar y = \sum y / n = 63/5 = 12.6$

$$\text{cov}(x, y) = \frac{\sum (x - \bar x)(y - \bar y)}{n - 1} = \frac{-120}{5 - 1} = -30$$

(The video has a few slips while adding up this column, such as "−1.8" and "−20", but its final answer, −30, is correct.)

---

## What the sign means

On a scatter plot:

- Example 1: as $x$ increases, $y$ increases (an upward trend) → covariance **positive** (+17.5).
- Example 2: as $x$ increases, $y$ decreases (a downward trend) → covariance **negative** (−30).

| Covariance | Relationship |
|---|---|
| $> 0$ | Positive: the variables move **together** |
| $< 0$ | Negative: when one goes up, the other goes **down** |
| $\approx 0$ | No linear relationship |

> The **size** of the covariance depends on the units of $x$ and $y$, so it is hard to say whether 17.5 is "big". The **correlation coefficient** (Lessons 13.3 and 13.4) rescales it to the range −1 to +1.

![Two scatter plots split into quadrants at the means, with each point's product of deviations](figures/covariance_quadrants.png)

Points up-right or down-left of the means (green) add positive products. Points up-left or down-right (red) add negative products. Example 1 is all green, so the covariance is positive. Example 2 is all red, so it is negative.

---

## Key takeaways

- Covariance is variance for two variables: $\text{cov}(x, x) = s_x^2$. Each point adds a signed rectangle $(x - \bar x)(y - \bar y)$.
- Sample covariance $= \sum (x - \bar x)(y - \bar y)/(n - 1)$.
- The **sign** gives the direction of the relationship. The size is unit-dependent.
- The deviation columns always add to 0, which is a good check on your arithmetic.

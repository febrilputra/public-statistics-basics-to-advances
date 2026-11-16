# Lesson 14.2 - Dummy Variables for Categories

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 7 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 14 - Multiple Regression

## The big picture: turning a category into a number

Regression needs numbers, but many useful predictors are **categories**: coated or uncoated, method A or B, morning or evening shift. The trick is a **dummy variable** (also called an *indicator*): a column that is 1 if the row is in the category and 0 if it isn't.

**1. One dummy shifts the line up or down.** With $z = 1$ for coated and $z = 0$ for uncoated, the model $\hat y = b_0 + b_1x + b_2z$ is really **two lines**:

- uncoated ($z = 0$): $\hat y = b_0 + b_1x$
- coated ($z = 1$): $\hat y = (b_0 + b_2) + b_1x$

Same slope $b_1$, different heights. $b_2$ is the vertical gap between them: the coated-minus-uncoated difference **at the same batch size**.

**2. The 0 group is the reference.** Every dummy coefficient is a comparison with the group that gets 0, called the **reference group**. Switching which group is 0 flips the sign and changes the intercept, but all the predictions stay exactly the same.

**3. $g$ categories need $g - 1$ dummies.** A finish with three levels (none, matte, gloss) needs two dummies, `d_matte` and `d_gloss`. "None" is the row where both are 0. A third dummy for "none" would equal $1 - d_\text{matte} - d_\text{gloss}$. It repeats the intercept column, so the software can't separate the coefficients. This is the **dummy variable trap**.

![Left: eight batches plotted as preparation time against batch size, blue circles uncoated and orange squares coated, with two parallel fitted lines. A black arrow shows the 3-minute gap, a green step shows +1 item gives +2 minutes, and dotted red residuals are all 1 minute. Right: a table coding uncoated as z = 0 and coated as z = 1, and a second table coding three finishes with two dummies, with a warning about the dummy variable trap](figures/dummy_variable_parallel_lines.png)

The two fitted lines are parallel because the model gives both groups the same slope. The gap between them is $b_2 = 3$ minutes everywhere. Every data point misses its line by exactly 1 minute.

**4. Where the numbers come from.** For one predictor we had formulas (Lesson 13.1). With several, software solves the least squares problem. This data set is **balanced** (every size has the same number of coated and uncoated batches), so here the coefficients can also be found from simple averages, as the example shows.

---

## Goal

Code a category as 0/1, fit and read a model with one numerical predictor and one dummy, and compute its residuals, SSE and $s^2$.

## Formulas

$$\hat y = b_0 + b_1x + b_2z, \qquad z = \begin{cases}1 & \text{in the category}\\ 0 & \text{reference group}\end{cases}$$

$$\text{SSE} = \sum (y - \hat y)^2, \qquad s^2 = \frac{\text{SSE}}{n - K}$$

For $g$ categories, use $g - 1$ dummies.

---

## Example

A workshop times 8 batches. $x$ = batch size − 5, and $z$ = 1 for coated.

| Batch size | $x$ | Coated $z$ | Times (minutes) |
|---:|---:|---:|---|
| 4 | −1 | 0 | 7, 9 |
| 4 | −1 | 1 | 10, 12 |
| 6 | +1 | 0 | 11, 13 |
| 6 | +1 | 1 | 14, 16 |

**Step 1: the size slope $b_1$.** Average time at 6 items: $(11 + 13 + 14 + 16)/4 = 13.5$. At 4 items: $(7 + 9 + 10 + 12)/4 = 9.5$. Two extra items add $13.5 - 9.5 = 4$ minutes, so

$$b_1 = \frac{4}{2} = 2 \text{ minutes per item}$$

**Step 2: the coating gap $b_2$.** Average coated time: $(10 + 12 + 14 + 16)/4 = 13$. Average uncoated time: $(7 + 9 + 11 + 13)/4 = 10$. Both groups have the same mix of sizes, so

$$b_2 = 13 - 10 = 3 \text{ minutes}$$

**Step 3: the intercept $b_0$.** The overall mean is $\bar y = 92/8 = 11.5$, at $\bar x = 0$ and $\bar z = 0.5$. The fitted plane passes through the point of means (like Lesson 13.1's line), so

$$b_0 = \bar y - b_1\bar x - b_2\bar z = 11.5 - 2(0) - 3(0.5) = 10$$

**Fitted model:**
$$\boxed{\hat y = 10 + 2x + 3z}$$

**Step 4: residuals.**

| $x$ | $z$ | $\hat y$ | Actual $y$ | Residuals $y - \hat y$ |
|---:|---:|---:|---|---|
| −1 | 0 | 8 | 7, 9 | −1, +1 |
| −1 | 1 | 11 | 10, 12 | −1, +1 |
| +1 | 0 | 12 | 11, 13 | −1, +1 |
| +1 | 1 | 15 | 14, 16 | −1, +1 |

$$\text{SSE} = 8 \times 1^2 = 8, \qquad s^2 = \frac{8}{8 - 3} = 1.6, \qquad s = \sqrt{1.6} \approx 1.26 \text{ minutes}$$

$n = 8$ batches and $K = 3$ coefficients, so 5 degrees of freedom are left for the noise.

**Changing the reference group.** Let $w = 1 - z$ (1 = uncoated). Substitute $z = 1 - w$:

$$\hat y = 10 + 2x + 3(1 - w) = 13 + 2x - 3w$$

Now the intercept describes a coated batch of 5, and the dummy coefficient is −3 (uncoated minus coated). The predictions haven't changed.

---

## Doing it in Excel

Type the dummy column yourself (`=IF(B2="coated",1,0)`), then use `=LINEST(y_range, x_and_z_range)` or *Data Analysis → Regression*. Excel doesn't create dummies automatically.

---

## Your turn

A three-level predictor "shift" (morning, afternoon, night) goes into a regression with an intercept. How many dummy columns do you need, and what does each coefficient compare?

**Answer:** Two. If morning is the reference, the coefficients are afternoon − morning and night − morning, each at the same values of the other predictors.

---

## Key takeaways

- A dummy variable is 1 for "in the category" and 0 for the reference group.
- One dummy in an additive model gives **parallel lines**. Its coefficient is the gap between them, at equal values of the other predictors.
- $g$ categories → $g - 1$ dummies. Using $g$ dummies plus an intercept is the dummy variable trap.
- Changing the reference group changes the labels and signs, not the predictions.
- $s^2 = \text{SSE}/(n - K)$ estimates the noise variance.

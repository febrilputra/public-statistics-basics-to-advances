# Lesson 17.3 - Post-Hoc Comparisons: Which Groups Differ?

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 11 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 17 - ANOVA and ANCOVA

## The big picture: following up a significant F

**1. Pairwise comparisons are a family of tests.** With $g$ groups there are

$$\binom{g}{2} = \frac{g(g - 1)}{2}$$

pairs: 3 pairs for 3 groups, 10 pairs for 5 groups, 45 pairs for 10 groups. Testing each pair at 0.05 brings back the multiple testing problem of Lesson 16.1. A significant ANOVA does **not** license unadjusted tests of every pair.

**2. Use the ANOVA's noise estimate.** ANOVA assumes all groups share one noise variance, estimated by $MS_W$ with $n_T - g$ degrees of freedom. A pairwise comparison uses that same estimate:

$$\text{SE}(\bar y_j - \bar y_k) = \sqrt{MS_W\left(\frac{1}{n_j} + \frac{1}{n_k}\right)}, \qquad t = \frac{\bar y_j - \bar y_k}{\text{SE}}, \qquad \text{df} = n_T - g$$

This borrows information from **all** groups, so it's more precise than a separate two-sample t-test that uses only the two groups involved.

**3. Two standard ways to control the error rate.**

- **Tukey's HSD** ("honestly significant difference") is built for **all pairs**. It uses the *studentized range* distribution $q$, and gives simultaneous 95% intervals: all of them together cover the true differences 95% of the time.

$$(\bar y_j - \bar y_k) \pm q_{0.05}(g, n_T - g)\sqrt{\frac{MS_W}{n}} \quad \text{(equal group sizes } n)$$

- **Holm** (Lesson 16.3) applied to the pairwise p-values. It works for any chosen set of comparisons.

![Left: dot plot of the three layouts with group means 5, 7 and 9. Right: for B − A, C − A and C − B, a blue Tukey 95% interval and a grey unadjusted interval; Tukey intervals [0.39, 3.61], [2.39, 5.61] and [0.39, 3.61] are wider than the unadjusted [0.69, 3.31], [2.69, 5.31] and [0.69, 3.31]; all intervals lie to the right of the red zero line](figures/pairwise_comparisons.png)

Tukey's intervals (blue) are wider than unadjusted ones (grey), because they hold **together** with 95% confidence. Every interval still misses 0, so all three layouts differ from each other.

**4. Planned contrasts can be sharper.** If, **before** seeing the data, you planned one specific question, such as "new layout C vs the average of A and B", test just that one contrast. The coefficients of a contrast add to zero, e.g. $\bar y_C - \tfrac12\bar y_A - \tfrac12\bar y_B$. One planned test needs no multiple-testing correction, and it doesn't require a significant overall F first.

---

## Goal

Carry out pairwise comparisons after ANOVA with the pooled SE, and control the error rate with Tukey's HSD or Holm.

## Formulas

$$\text{SE} = \sqrt{MS_W\left(\tfrac{1}{n_j} + \tfrac{1}{n_k}\right)}, \qquad t = \frac{\bar y_j - \bar y_k}{\text{SE}}, \qquad \text{df} = n_T - g$$

$$\text{Tukey HSD half-width} = q_{0.05}(g, n_T - g)\sqrt{\frac{MS_W}{n}}$$

---

## Example

Layouts A, B, C (Lesson 17.1): means 5, 7, 9, $n = 4$ each, $MS_W = 0.667$, df $= 9$.

**Step 1: pooled SE** (the same for every pair, since all $n = 4$).
$$\text{SE} = \sqrt{0.667\left(\tfrac14 + \tfrac14\right)} = \sqrt{0.333} = 0.577$$

**Step 2: t statistics and raw p-values (df = 9).**

| Pair | Difference | $t$ = diff / 0.577 | Raw p | Holm-adjusted p |
|---|---:|---:|---:|---:|
| C − A | 4 | 6.93 | 0.00007 | $3 \times 0.00007 = 0.0002$ |
| B − A | 2 | 3.46 | 0.0071 | $2 \times 0.0071 = 0.0142$ |
| C − B | 2 | 3.46 | 0.0071 | $1 \times 0.0071 \to$ running max $= 0.0142$ |

All three Holm-adjusted p-values are below 0.05.

**Step 3: Tukey HSD.** $q_{0.05}(3, 9) = 3.948$, so
$$\text{HSD} = 3.948\sqrt{\frac{0.667}{4}} = 3.948(0.408) = 1.61$$

| Pair | Difference | Tukey 95% interval | Contains 0? |
|---|---:|---|---|
| B − A | 2 | $2 \pm 1.61 = [0.39,\ 3.61]$ | no |
| C − A | 4 | $4 \pm 1.61 = [2.39,\ 5.61]$ | no |
| C − B | 2 | $2 \pm 1.61 = [0.39,\ 3.61]$ | no |

**Conclusion:** all three layouts differ. C is slowest, A fastest, and each step is about 2 minutes, though with only 4 runs per layout the gaps could be anywhere from about 0.4 to 3.6 minutes.

For comparison, an unadjusted 95% interval uses $t_{0.025, 9} = 2.262$: $2 \pm 2.262(0.577) = 2 \pm 1.31 = [0.69, 3.31]$. It is narrower, but it doesn't protect the family.

---

## Doing it in Excel

Excel has no Tukey function. Compute $t$ by hand and get the p-values with `=T.DIST.2T(3.46, 9)` → 0.0071, then apply Holm (Lesson 16.3). In Python: `statsmodels.stats.multicomp.pairwise_tukeyhsd`.

---

## Your turn

A significant omnibus F test is followed by a statement: "The group with the largest sample mean is higher than every other group." Is that justified by the F test alone?

**Answer:** No. The F test only says that **at least one** mean differs. Claims about particular pairs need pairwise comparisons with suitable error control (Tukey, Holm) or pre-planned contrasts.

---

## Key takeaways

- $g$ groups give $g(g - 1)/2$ pairs, a family of tests that needs error control.
- Pairwise SE uses the ANOVA's $MS_W$ and df $= n_T - g$.
- Tukey's HSD gives simultaneous intervals for all pairs. Holm works on any set of p-values.
- Adjusted intervals are wider than unadjusted ones. That's the price of protecting the whole family.
- A single pre-planned contrast needs no adjustment and doesn't require a significant F first.

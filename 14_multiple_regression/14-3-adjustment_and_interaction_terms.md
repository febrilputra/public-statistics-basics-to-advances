# Lesson 14.3 - Adjustment and Interaction Terms

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 7 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 14 - Multiple Regression

## The big picture: what "holding the others fixed" really means

**1. A slope can change when you add a predictor.** Suppose the big batches in a data set happen to be mostly coated. If you regress time on batch size **alone**, the size slope also picks up the extra coating time, because size and coating travel together. Put coating in the model and the size slope becomes the change **within** a coating group. That is called **adjusting** for coating.

**2. Adjusting is not the same as proving cause.** A multiple regression slope is an "all else **in the model** equal" comparison. A variable left out of the model can still bias it (**confounding**). Adding the wrong variable can also hurt, for example one that is itself caused by the thing you're studying. Choose predictors from your understanding of the process, not by the rule "more is always better".

**3. An interaction lets a slope depend on a group.** The model $\hat y = b_0 + b_1x + b_2z$ forces both groups to share the slope $b_1$, which gives parallel lines. Adding the product $xz$,

$$\hat y = b_0 + b_1x + b_2z + b_3\,xz$$

gives each group its own slope:

- $z = 0$: $\hat y = b_0 + b_1x$, slope $b_1$
- $z = 1$: $\hat y = (b_0 + b_2) + (b_1 + b_3)x$, slope $b_1 + b_3$

**4. With an interaction, the group gap changes along $x$.** Gap = coated − uncoated $= b_2 + b_3x$. There is no longer one single "coating effect", so you report the gap at chosen values of $x$.

![Three panels. A: six batches where big batches are coated; ignoring coating gives a dashed line with slope 2.9, while each group has slope 2. B: two parallel lines, uncoated and coated, with green arrows showing a gap of 3 at x = -1, 0 and 1. C: with an interaction the coated line is steeper and the gaps are 2, 3 and 4](figures/confounding_and_interaction.png)

A: leaving coating out bends the size slope from 2 up to 2.9, because the larger batches here are mostly coated. B: without an interaction the gap is the same everywhere. C: with an interaction the lines spread apart, so the gap depends on batch size.

**5. Keep the lower-order terms.** If you include $xz$, also keep $x$ and $z$ in the model. Otherwise the model forces the gap or a slope to be 0 at $x = 0$ for no good reason.

---

## Goal

Explain what an adjusted slope means, and write, read and evaluate a model with an interaction term.

## Formulas

| Model | Slope of $x$ | Gap (group 1 − group 0) at a given $x$ |
|---|---|---|
| Additive: $b_0 + b_1x + b_2z$ | $b_1$ in both groups | $b_2$ (constant) |
| Interaction: $b_0 + b_1x + b_2z + b_3xz$ | $b_1$ ($z = 0$), $b_1 + b_3$ ($z = 1$) | $b_2 + b_3x$ |

---

## Example 1: a slope that is bent by a missing predictor

| Group | Centred size $x$ | Time $y$ |
|---|---|---|
| uncoated | −2, −1, 0 | 6, 8, 10 |
| coated | 0, 1, 2 | 13, 15, 17 |

Within each group, time rises by exactly **2 minutes per item**, and coated batches are 3 minutes higher.

**Ignoring coating** (Lesson 13.1 on all six points): $\bar x = 0$, $\bar y = 11.5$.

$$S_{xy} = \sum (x - \bar x)(y - \bar y) = (-2)(-5.5) + (-1)(-3.5) + 0 + 0 + (1)(3.5) + (2)(5.5) = 29$$

$$S_{xx} = \sum (x - \bar x)^2 = 4 + 1 + 0 + 0 + 1 + 4 = 10, \qquad \text{slope} = \frac{29}{10} = 2.9$$

**With coating in the model**, the slope is **2**. The extra 0.9 came from the fact that the big batches were coated, not from batch size.

## Example 2: reading an interaction

$$\hat y = 5 + 2x - 3z + 4xz$$

- $z = 0$: $\hat y = 5 + 2x$
- $z = 1$: $\hat y = 5 + 2x - 3 + 4x = 2 + 6x$
- Gap ($z = 1$ minus $z = 0$): $-3 + 4x$

| $x$ | Gap $-3 + 4x$ |
|---:|---:|
| 0 | −3 |
| 0.75 | 0 |
| 1 | +1 |
| 2 | +5 |

Saying "the effect of $z$ is −3" is only correct at $x = 0$. The lines cross at $x = 0.75$, and after that group 1 is **higher**.

---

## Doing it in Excel

Make the interaction column yourself, e.g. `=B2*C2` for $x \times z$, and include it with $x$ and $z$ in `LINEST` or *Data Analysis → Regression*.

---

## Your turn

The fitted model is $\hat y = 10 + 2x + 3z + 1\cdot xz$. Find the coated-minus-uncoated gap at $x = -1$, $0$ and $1$.

**Answer:** Gap $= 3 + 1\cdot x$, which gives 2, 3 and 4 minutes (panel C of the figure).

---

## Key takeaways

- A multiple regression slope compares cases that differ in that predictor only, with the other **included** predictors held fixed.
- Leaving out a predictor that is related to both $x$ and $y$ can bend a slope (2 became 2.9 in the example).
- Adjusting for variables in a regression does not by itself prove cause and effect.
- An interaction term $xz$ lets the slope of $x$ differ between groups. The group gap becomes $b_2 + b_3x$.
- When you include an interaction, keep the main terms $x$ and $z$ too.

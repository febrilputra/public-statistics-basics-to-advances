# Lesson 16.1 - The Multiple Testing Problem

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 10 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 16 - P-Value Pitfalls

## The big picture: a valid p-value can still mislead

Lesson 10.6 built the p-value method for **one** planned test. This chapter is about what goes wrong when there are **many** chances to get a small p-value, and how to fix it.

| Question | Tool | Lesson |
|---|---|---|
| Why do many tests produce false "discoveries"? | $1 - (1 - \alpha)^m$ | 16.1 (this one) |
| Which error rate should I control? | FWER vs FDR | 16.2 |
| How do I keep the chance of **any** false claim ≤ 5%? | Bonferroni, Holm | 16.3 |
| How do I keep the **share** of false claims low? | Benjamini–Hochberg | 16.4 |
| What about hidden multiple testing? | selection, optional stopping, winner's curse | 16.5 |

**1. Every test is a lottery ticket for a false positive.** When ${\color{#0072B2}H_0}$ is true, a valid test at $\alpha = 0.05$ still rejects 5% of the time (a Type I error, Lesson 10.2). One test → 5% risk. Twenty tests → twenty tickets.

**2. The chance of at least one false positive.** If $m$ tests are **independent** and all their nulls are true, each one is "not rejected" with probability $0.95$. All of them are not rejected with probability $0.95^m$ (multiplication rule, Lesson 5.7). So

$$P(\text{at least one false positive}) = 1 - (1 - \alpha)^m$$

For $m = 20$: $1 - 0.95^{20} = 0.642$. Nearly a two-in-three chance that something looks "significant" when nothing is going on.

**3. The expected number of false positives** is simply $m \times \alpha$, here $20 \times 0.05 = 1$. This works even if the tests are dependent, because averages add up regardless (Lesson 18.3).

![Left: twenty circles, one per null test, each with its p-value; one circle, test 10 with p = 0.028, is red, the others are light blue. Right: the curve 1 − 0.95^m rising with the number of tests, with points m = 1: 0.050, m = 5: 0.226, m = 10: 0.401, m = 20: 0.642 and m = 50: 0.923](figures/multiple_testing_problem.png)

Left: one run of 20 tests in which every null is true. Test 10 still came out "significant" (p = 0.028), purely by chance. Right: the more tests, the more likely at least one false alarm. With 50 tests it is 92%.

**4. Three different numbers, don't mix them up.**

| Quantity | $m = 20$, $\alpha = 0.05$ |
|---|---|
| P(a **given** test is a false positive) | 0.05 |
| P(**at least one** false positive) | 0.642 |
| **Expected number** of false positives | 1 |

**5. Where many tests come from.** Several outcomes, several subgroups (men, women, under 40...), several time points, all pairs of groups (Lesson 17.3), several ways to analyse the data. The **family** of tests is everything that could have produced the claim, not only what ended up in the report.

---

## Goal

Calculate the chance of at least one false positive and the expected number of false positives among $m$ tests.

## Formulas

$$P(\text{at least one false positive}) = 1 - (1 - \alpha)^m \quad \text{(independent tests, all nulls true)}$$

$$E(\text{number of false positives}) = m\,\alpha \quad \text{(any dependence, all nulls true)}$$

---

## Example

A sensor team tests 20 independent settings. None of them truly changes accuracy. Each test uses $\alpha = 0.05$.

**Step 1: no false positives at all.**
$$P(\text{none}) = 0.95^{20} = 0.3585$$

**Step 2: at least one.**
$$P(\text{at least one}) = 1 - 0.3585 = 0.6415$$

**Step 3: expected number.**
$$E = 20 \times 0.05 = 1$$

**Interpretation:** if the team reports "setting 10 significantly improves accuracy (p = 0.028)" without mentioning the other 19 tests, the claim is misleading. With 20 tries, a p-value below 0.05 is the **usual** result, not a surprise.

**When tests are dependent** (e.g. all compared with the same control group), $1 - 0.95^m$ is no longer exact, but $m\alpha$ still gives the expected count, and the risk still grows with $m$.

---

## Doing it in Excel

`=1-0.95^20` → 0.6415 · `=20*0.05` → 1

---

## Your turn

What is the chance of at least one false positive in 10 independent true-null tests at 0.05? What is the expected number?

**Answer:** $1 - 0.95^{10} = 1 - 0.5987 = 0.4013$. Expected number $= 10 \times 0.05 = 0.5$.

---

## Key takeaways

- Each true-null test has a 5% false positive risk. Many tests multiply the opportunities.
- $P(\text{at least one}) = 1 - (1 - \alpha)^m$ for independent tests: 0.401 for 10 tests, 0.642 for 20.
- The expected number of false positives is $m\alpha$, whether or not the tests are independent.
- The family of tests includes every analysis that could have produced the claim.

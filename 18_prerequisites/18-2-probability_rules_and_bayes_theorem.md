# Lesson 18.2 - Probability Rules and Bayes' Theorem

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Appendices A–F (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 18 - Mathematical and Python Prerequisites

## The big picture: which way round is the condition?

Chapter 5 introduced the probability rules. This lesson collects the ones the later chapters rely on, and stresses the most common trap: confusing $P(A \mid B)$ with $P(B \mid A)$.

**1. The basic rules** (Lessons 5.2–5.7):

- complement: $P(A^c) = 1 - P(A)$
- addition: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ (subtract the overlap so it isn't counted twice)
- conditional: $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$ (restrict attention to the cases where $B$ happened)
- multiplication: $P(A \cap B) = P(A \mid B)\,P(B)$

**2. Independence is a property, not a default.** $A$ and $B$ are independent if $P(A \cap B) = P(A)P(B)$, i.e. knowing one doesn't change the chance of the other. **Mutually exclusive** events (they can't both happen) are the opposite: they are **dependent**. If one happens, the other can't.

**3. Conditional probability is not symmetric.** $P(\text{flag} \mid \text{flawed})$ and $P(\text{flawed} \mid \text{flag})$ answer different questions and can be very different. **Bayes' theorem** connects them:

$$P(D \mid F) = \frac{P(F \mid D)\,P(D)}{P(F)}, \qquad P(F) = P(F \mid D)P(D) + P(F \mid D^c)P(D^c)$$

The second formula is the **law of total probability**: add up the ways $F$ can happen.

![Three panels. Left: 1,000 small squares: 90 red (flawed and flagged), 10 light red (flawed, missed), 180 orange (good but flagged), 720 light blue (good, not flagged). Middle: a tree from 1,000 to flawed 100 (0.10) and good 900 (0.90), then flag 90 / no flag 10 and flag 180 / no flag 720. Right: among flagged parts, 90 of 270 are flawed (0.333) when 10% are flawed, but only 9 of 207 (0.043) when 1% are flawed](figures/bayes_sensor.png)

Left and middle: out of 1,000 parts, 270 get flagged, and only 90 of those are really flawed. Right: the rarer the flaw, the smaller the share of flags that are real. The sensor itself hasn't changed.

**4. Counting is the easiest way.** Imagine 1,000 cases and fill in the tree with counts. This "natural frequency" method avoids most mistakes.

**5. Why it matters for p-values.** A p-value is $P(\text{data this extreme} \mid {\color{#0072B2}H_0})$. It is **not** $P({\color{#0072B2}H_0} \mid \text{data})$. Reversing the condition needs prior probabilities, just as the sensor example needed the 10% flaw rate. That is why a p-value alone can't tell you how likely a hypothesis is (Lesson 15.5).

---

## Goal

Apply the probability rules and use Bayes' theorem (or a frequency tree) to reverse a conditional probability.

## Formulas

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(D \mid F) = \frac{P(F \mid D)P(D)}{P(F \mid D)P(D) + P(F \mid D^c)P(D^c)}$$

---

## Example

10% of manufactured parts have a surface flaw. A sensor flags 90% of flawed parts and also (wrongly) flags 20% of good parts. A part is flagged. What is the chance it is really flawed?

**Step 1: count (1,000 parts).**

| | Flagged | Not flagged | Total |
|---|---:|---:|---:|
| Flawed | $100 \times 0.9 = 90$ | 10 | 100 |
| Good | $900 \times 0.2 = 180$ | 720 | 900 |
| **Total** | **270** | 730 | 1,000 |

**Step 2: answer from the table.**
$$P(\text{flawed} \mid \text{flagged}) = \frac{90}{270} = \frac13 = 0.333$$

**Step 3: the same with Bayes' formula.**
$$P(F) = 0.9(0.1) + 0.2(0.9) = 0.09 + 0.18 = 0.27$$
$$P(D \mid F) = \frac{0.9 \times 0.1}{0.27} = \frac{0.09}{0.27} = 0.333$$

**Interpretation:** the sensor catches 90% of flaws, yet **two out of three** flagged parts are fine. Good parts are so common that their 20% false-flag rate produces more flags than the real flaws do.

---

## Doing it in Excel

`=0.9*0.1/(0.9*0.1+0.2*0.9)` → 0.333

---

## Your turn

Keep the same sensor, but suppose only **1%** of parts are flawed. Find $P(\text{flawed} \mid \text{flagged})$.

**Answer:**
$$\frac{0.9(0.01)}{0.9(0.01) + 0.2(0.99)} = \frac{0.009}{0.009 + 0.198} = \frac{0.009}{0.207} = 0.043$$

Only about 4% of flags are real. (In counts: 9 real flags among 207.)

---

## Key takeaways

- $P(A \mid B) = P(A \cap B)/P(B)$, the probability within the cases where $B$ happened.
- $P(A \mid B) \ne P(B \mid A)$ in general. Bayes' theorem converts one into the other, using the base rate.
- Independent means the joint probability equals the product. Mutually exclusive events are dependent.
- Filling in a table or tree of counts for 1,000 cases is the most reliable method.
- A p-value is $P(\text{data} \mid {\color{#0072B2}H_0})$, not $P({\color{#0072B2}H_0} \mid \text{data})$.

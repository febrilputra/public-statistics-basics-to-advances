# Lesson 16.5 - Selection, Optional Stopping, and the Winner's Curse

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 10 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 16 - P-Value Pitfalls

## The big picture: multiple testing you can't see in the report

Lessons 16.1–16.4 dealt with tests you **know** you ran. Often the multiple testing is hidden in how the analysis was chosen.

**1. Selection: many paths, one reported.** Trying several outcomes, transformations, subgroups, covariates, exclusion rules or time windows, and then reporting only the best-looking one, is multiple testing even if only **one** p-value is printed. Looking at 20 plots and then formally testing the most striking one is the same thing: the data chose the test.

**What to do:**
- Write down the main analysis **before** seeing the data (pre-registration).
- Report every analysis you tried, and label exploratory results as exploratory.
- Confirm a surprising finding on **new data**.

**2. Optional stopping: peeking until $p < 0.05$.** Collect 20 observations and test. Not significant? Add 20 more and test again... and stop as soon as $p \le 0.05$. Each individual test is valid, but the **procedure** gives you up to 10 chances to cross the line.

**3. Winner's curse: the biggest estimate is too big.** Among many noisy estimates of similar effects, the largest one is likely to be one where the noise happened to push it **up**. Selecting it by size (or by significance) then **overstates** the effect. This is worst when power is low (Chapter 15). Adjusting the p-value doesn't fix this bias in the estimate.

![Three panels. A: p-value paths over 10 looks (every 20 observations) for null studies; red paths cross below p = 0.05 and stop with a star, light-blue paths never cross. B: false positive rate 5.1% for one planned test at n = 200 versus 19.3% for 10 looks with stopping at the first p ≤ 0.05, from 20,000 simulated studies. C: 20 noisy estimates of the same true effect 0.2 with 95% intervals; the largest, the "winner", is 0.44, more than double the truth](figures/optional_stopping_and_winners_curse.png)

A: with no real effect, some studies dip below 0.05 at some look just by chance, and peeking catches them. B: one planned test keeps the false positive rate at 5%. Peeking 10 times nearly quadruples it, to 19%. C: the "winning" estimate (0.44) is more than twice the true effect (0.2), only because it was chosen for being the largest.

**4. How to look at data more than once, correctly.** Interim looks are not forbidden. A **group-sequential design** fixes the number of looks in advance and uses stricter cutoffs at each look, so that the overall false positive rate stays at 5%. The rule must be planned before the data arrive, and then followed.

---

## Goal

Recognise hidden multiple testing (selection and optional stopping) and the winner's curse, and know the remedies.

## Formulas

There's no new formula. The key idea is that **the false positive rate belongs to the whole procedure**, not to the final test:

$$P(\text{false positive}) = P(\text{the procedure ever declares } p \le \alpha \mid {\color{#0072B2}H_0})$$

---

## Example

**Optional stopping simulation.** 20,000 studies with **no** real effect (true mean 0, SD 1). Two plans:

| Plan | What happens | False positive rate |
|---|---|---:|
| A: fixed | collect 200 observations, test once | 5.1% |
| B: peek | test after 20, 40, 60, ..., 200; stop at the first $p \le 0.05$ | 19.3% |

**Step 1.** Under plan A, the false positive rate matches $\alpha = 0.05$ (5.1% is within simulation error).

**Step 2.** Under plan B, each look is a valid z-test, but there are 10 looks. 19.3% of null studies cross the line at some look.

**Step 3.** If the 10 looks were independent, the rate would be $1 - 0.95^{10} = 40\%$. It's "only" 19% because successive looks share most of their data. Dependence reduces the inflation but doesn't remove it.

**Conclusion:** a result from plan B reported as "p = 0.04" is far weaker evidence than it sounds. Its real false positive rate is almost 4 times the advertised 5%.

**Winner's curse.** Twenty studies each estimate the same true effect, 0.2, with SE 0.15. The estimates scatter from about 0.0 to 0.44. A news story about "the study that found the biggest effect" reports 0.44, more than double the truth. The average of all 20 is close to 0.2.

---

## Doing it in Excel

Simulate one peeking study: 200 rows of `=NORM.S.INV(RAND())`. At each look $n$, `z = SUM(first n)/SQRT(n)` and `p = 2*(1-NORM.S.DIST(ABS(z),TRUE))`. Press F9 many times and count how often any look gives $p \le 0.05$.

---

## Your turn

An analyst checks 50 scatter plots, picks the one with the clearest pattern, and reports a single p-value of 0.01 for it. Is this a single test?

**Answer:** No. The visual inspection used the same data to choose among 50 possibilities, so the selection acts like 50 tests. The p-value of 0.01 doesn't account for it. The finding needs confirmation on new data, or an analysis that accounts for the whole search.

---

## Key takeaways

- Choosing the analysis after seeing the data is hidden multiple testing, even if only one p-value is reported.
- Peeking and stopping at the first $p \le 0.05$ inflates false positives: 19% instead of 5% with 10 looks.
- Pre-plan the analysis, report everything you tried, and confirm surprising findings on new data.
- Interim looks are fine with a planned group-sequential design that uses stricter cutoffs.
- Winner's curse: the largest or most significant estimate tends to overstate the true effect.

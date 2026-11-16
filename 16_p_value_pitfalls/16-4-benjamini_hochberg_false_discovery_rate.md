# Lesson 16.4 - The Benjamini–Hochberg Procedure (FDR)

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 10 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 16 - P-Value Pitfalls

## The big picture: accept a few false leads to find many more real ones

**1. A rising line instead of a flat cutoff.** Benjamini–Hochberg (BH) compares the $k$-th smallest p-value with a threshold that grows with $k$:

$$p_{(k)} \le \frac{k}{m}\,q$$

where $q$ is the FDR you're willing to accept (e.g. 0.05). The smallest p-value must beat $q/m$ (the Bonferroni cutoff). The largest only needs to beat $q$ itself.

**2. Step-UP: look for the LARGEST $k$ under the line.** Find the **largest** $k$ for which $p_{(k)} \le (k/m)q$, then reject the $k$ smallest p-values, **even if some of them were above their own threshold**. This is the opposite of Holm, which steps *down* and stops at the first failure.

**3. What it guarantees.** BH keeps the false discovery rate (Lesson 16.2) at or below $q$ when the tests are independent, or positively dependent in certain ways. Under arbitrary dependence, a more conservative variant (Benjamini–Yekutieli) is needed.

![Left: the five sorted example p-values on a log scale against the BH line 0.01, 0.02, 0.03, 0.04, 0.05 and the flat Bonferroni line at 0.01; the first four points are blue and on or under the BH line, and an arrow marks k = 4 as the largest k under the line. Right: a simulation of 3,000 studies with 80 true nulls and 20 real effects; estimated FWER is 0.041 for Bonferroni, 0.044 for Holm and 0.410 for BH, while estimated FDR is 0.006, 0.006 and 0.040; Bonferroni and Holm make 6.4 and 6.5 discoveries per study, BH 12.8](figures/benjamini_hochberg.png)

Left: four p-values are at or below the BH line, so BH rejects 4. Holm rejected 2 and Bonferroni 1. Right: over 3,000 simulated screening studies, BH keeps its false discovery rate at 0.040 (just under $q = 0.05$) and finds about twice as many effects. In exchange, 41% of its studies contain at least one false discovery.

**4. The simulation in numbers** (each study: 100 tests, 80 with no effect, 20 with a real effect; 3,000 studies):

| Method | FWER | FDR | Discoveries per study |
|---|---:|---:|---:|
| Bonferroni | 0.041 | 0.006 | 6.4 |
| Holm | 0.044 | 0.006 | 6.5 |
| BH ($q = 0.05$) | 0.410 | 0.040 | 12.8 |

Each method does exactly what it promises. Bonferroni and Holm keep FWER under 0.05. BH keeps FDR under 0.05. BH isn't "better", it controls a different error rate.

**5. BH adjusted p-values** use a running minimum from the top:

$$p_{(k)}^\text{BH} = \min\!\Big(1,\; \min_{j \ge k}\, \frac{m}{j}\,p_{(j)}\Big)$$

Reject when the adjusted value is ≤ $q$.

---

## Goal

Apply the Benjamini–Hochberg procedure and compare its results with Bonferroni and Holm.

## Formulas

$$\text{Find the largest } k \text{ with } p_{(k)} \le \frac{k}{m}q; \text{ reject } H_{(1)}, \dots, H_{(k)}$$

$$p_{(k)}^\text{BH} = \min\!\Big(1, \min_{j \ge k} \tfrac{m}{j}p_{(j)}\Big)$$

---

## Example

Same five p-values as Lesson 16.3: 0.001, 0.012, 0.021, 0.040, 0.200. $m = 5$, $q = 0.05$.

**Step 1: BH thresholds $(k/5)(0.05)$.**

| $k$ | $p_{(k)}$ | Threshold $k \times 0.01$ | $p_{(k)} \le$ threshold? |
|---:|---:|---:|---|
| 1 | 0.001 | 0.01 | yes |
| 2 | 0.012 | 0.02 | yes |
| 3 | 0.021 | 0.03 | yes |
| 4 | 0.040 | 0.04 | yes (equal) |
| 5 | 0.200 | 0.05 | no |

**Step 2: largest $k$ that passes.** $k = 4$. **Reject the four smallest.**

**Step 3: adjusted p-values.** Compute $(m/k)\,p_{(k)}$, then take the running minimum from the bottom up:

| $p_{(k)}$ | $(5/k)\,p_{(k)}$ | Running min from bottom | Reject at 0.05? |
|---:|---:|---:|---|
| 0.001 | $5(0.001) = 0.005$ | 0.005 | yes |
| 0.012 | $2.5(0.012) = 0.030$ | 0.030 | yes |
| 0.021 | $1.667(0.021) = 0.035$ | 0.035 | yes |
| 0.040 | $1.25(0.040) = 0.050$ | 0.050 | yes |
| 0.200 | $1(0.200) = 0.200$ | 0.200 | no |

**Comparison:** Bonferroni rejects 1, Holm 2, BH 4. BH's extra discoveries come from controlling a different, more lenient error rate. Use BH only when an average of about 5% false leads is acceptable.

---

## Doing it in Excel

Sorted p-values in `B2:B6`, rank $k$ in `A2:A6`: raw `C2 = MIN(1, 5/A2*B2)`. Running min from the bottom: `D6 = C6`, then `D5 = MIN(C5, D6)` and fill upwards.

---

## Your turn

Apply BH at $q = 0.10$ to the p-values 0.008, 0.030, 0.045, 0.300 ($m = 4$).

**Answer:** Thresholds $(k/4)(0.10)$ = 0.025, 0.050, 0.075, 0.100. The checks: $0.008 \le 0.025$ ✓, $0.030 \le 0.050$ ✓, $0.045 \le 0.075$ ✓, $0.300 > 0.100$ ✗. The largest passing $k$ is 3, so reject the three smallest.

---

## Key takeaways

- BH compares $p_{(k)}$ with the rising line $(k/m)q$.
- It steps **up**: find the largest $k$ under the line and reject the $k$ smallest p-values.
- It controls FDR (the average share of false discoveries), not FWER.
- It usually finds many more effects than Bonferroni or Holm, but often includes at least one false discovery.
- It is valid for independent or positively dependent tests. Use Benjamini–Yekutieli for arbitrary dependence.

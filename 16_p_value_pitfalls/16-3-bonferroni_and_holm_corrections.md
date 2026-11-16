# Lesson 16.3 - Bonferroni and Holm Corrections

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 10 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 16 - P-Value Pitfalls

## The big picture: share the 5% among the tests

**1. Bonferroni: split α equally.** To keep the chance of **any** false positive (FWER) at most $\alpha$, test each of the $m$ hypotheses at level $\alpha/m$:

$$\text{reject } H_i \text{ if } p_i \le \frac{\alpha}{m}$$

**Why it works.** The chance that at least one of several events happens is never more than the sum of their chances (the "union bound"). With $m$ true nulls each tested at $\alpha/m$: $P(V \ge 1) \le m \times \alpha/m = \alpha$. This holds whatever the dependence between the tests.

**2. Adjusted p-values say the same thing.** Instead of shrinking the cutoff, inflate the p-values and compare with the usual $\alpha$:

$$p_i^\text{Bonf} = \min(1,\; m\,p_i), \quad \text{reject if } p_i^\text{Bonf} \le \alpha$$

"$p \le \alpha/m$" and "$mp \le \alpha$" are the same rule, written two ways.

**3. Holm: a smarter step-down.** Bonferroni treats all tests as if all $m$ were still "in play". Holm uses the fact that once a hypothesis is rejected, fewer remain:

1. Sort the p-values: $p_{(1)} \le p_{(2)} \le \dots \le p_{(m)}$.
2. Compare $p_{(1)}$ with $\alpha/m$, $p_{(2)}$ with $\alpha/(m - 1)$, $p_{(3)}$ with $\alpha/(m - 2)$, ... and the last one with $\alpha/1$.
3. Reject one by one while the comparison succeeds. **Stop at the first failure.** We fail to reject that hypothesis and all larger ones.

Holm also controls FWER under any dependence, and it always rejects **at least as many** hypotheses as Bonferroni. There's no reason to prefer plain Bonferroni except simplicity.

![Left: five sorted p-values (0.001, 0.012, 0.021, 0.040, 0.200) on a log scale with Bonferroni's flat threshold 0.01 and Holm's rising staircase 0.01, 0.0125, 0.0167, 0.025, 0.05; the first two points are green (rejected by Holm) and an arrow marks the stop at 0.021 > 0.0167. Right: bars of raw, Bonferroni and Holm adjusted p-values for each test with a dashed line at 0.05; Bonferroni rejects only the first test, Holm the first two](figures/bonferroni_vs_holm.png)

Left: Bonferroni's cutoff stays at 0.01 for every test. Holm's cutoff rises step by step, so 0.012 passes (≤ 0.0125). Holm stops at 0.021, which is above 0.0167. Right: the same decisions as adjusted p-values. A test is rejected if its bar is at or below the 0.05 line.

**4. Holm's adjusted p-values** need a running maximum, so the adjusted values never go down as the raw p-values go up:

$$p_{(k)}^\text{Holm} = \min\!\Big(1,\; \max_{j \le k}\, (m - j + 1)\,p_{(j)}\Big)$$

Then put them back in the original test order.

---

## Goal

Apply the Bonferroni and Holm procedures, by thresholds and by adjusted p-values.

## Formulas

| Method | Compare | Adjusted p-value |
|---|---|---|
| Bonferroni | every $p_i$ with $\alpha/m$ | $\min(1, m\,p_i)$ |
| Holm | $p_{(k)}$ with $\alpha/(m - k + 1)$; stop at first failure | $\min\big(1, \max_{j \le k}(m - j + 1)p_{(j)}\big)$ |

---

## Example

Five planned comparisons give p-values 0.001, 0.012, 0.021, 0.040 and 0.200. Use $\alpha = 0.05$, so $m = 5$.

**Bonferroni:** cutoff $0.05/5 = 0.01$. Only $0.001 \le 0.01$. **1 rejection.**

**Holm (thresholds):**

| $k$ | $p_{(k)}$ | Threshold $\alpha/(m - k + 1)$ | Decision |
|---:|---:|---:|---|
| 1 | 0.001 | $0.05/5 = 0.0100$ | $0.001 \le 0.0100$ → reject |
| 2 | 0.012 | $0.05/4 = 0.0125$ | $0.012 \le 0.0125$ → reject |
| 3 | 0.021 | $0.05/3 = 0.0167$ | $0.021 > 0.0167$ → **stop** |
| 4 | 0.040 | $0.05/2 = 0.0250$ | fail to reject (already stopped) |
| 5 | 0.200 | $0.05/1 = 0.0500$ | fail to reject |

**2 rejections.** Note that 0.040 ≤ 0.05 doesn't matter, because Holm already stopped at $k = 3$.

**Adjusted p-values:**

| Raw $p$ | Bonferroni $5p$ | Holm: $(m - k + 1)p$ | Holm after running max |
|---:|---:|---:|---:|
| 0.001 | 0.005 | $5(0.001) = 0.005$ | **0.005** |
| 0.012 | 0.060 | $4(0.012) = 0.048$ | **0.048** |
| 0.021 | 0.105 | $3(0.021) = 0.063$ | 0.063 |
| 0.040 | 0.200 | $2(0.040) = 0.080$ | 0.080 |
| 0.200 | 1.000 | $1(0.200) = 0.200$ | 0.200 |

Values ≤ 0.05 are rejected. The same answers: Bonferroni 1, Holm 2.

---

## Doing it in Excel

With p-values sorted ascending in `B2:B6`: Bonferroni `=MIN(1,5*B2)`. Holm, raw: `C2 = (5-ROW()+2)*B2`, then running max: `D2 = MIN(1, MAX($C$2:C2))`.

---

## Your turn

1. For raw p-values 0.004, 0.020 and 0.030, find the Holm-adjusted values and the rejections at 0.05.
2. Is "multiply each p by $m$" more powerful than "compare each p with $\alpha/m$"?

**Answers:**
1. Multiply the sorted values by 3, 2, 1: 0.012, 0.040, 0.030. Running max: **0.012, 0.040, 0.040**. All three ≤ 0.05, so all three are rejected. (Forgetting the running max gives the wrong value, 0.030, for the last one.)
2. No. They are the same rule written two ways.

---

## Key takeaways

- Bonferroni: reject if $p \le \alpha/m$ (or $mp \le \alpha$). It controls FWER under any dependence.
- Holm: sort, compare $p_{(k)}$ with $\alpha/(m - k + 1)$, stop at the first failure. It also controls FWER, and always rejects at least as many as Bonferroni.
- Holm adjusted p-values need a running maximum.
- Both are conservative with many correlated tests. That's the price of controlling the chance of **any** false claim.

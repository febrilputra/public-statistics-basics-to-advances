# Lesson 16.2 - FWER and FDR: Two Ways to Count Mistakes

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 10 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 16 - P-Value Pitfalls

## The big picture: what exactly do we want to keep small?

**1. Name the counts.** In a family of $m$ tests, after the decisions are made:

- $R$ = number of rejections (all **discoveries**)
- $V$ = number of **false** discoveries (rejections where ${\color{#0072B2}H_0}$ was actually true)

We never see $V$ in real data, because we don't know which nulls are true. But we can choose a procedure that keeps it under control **on average over repeated studies**.

**2. Family-wise error rate (FWER).**

$$\text{FWER} = P(V \ge 1)$$

the chance of making **one or more** false discoveries. Controlling FWER at 0.05 means that in at most 5% of studies does even one false claim get through. Use it when a single false claim is costly: confirming a drug, a safety claim, a short list of planned comparisons.

**3. False discovery rate (FDR).**

$$\text{FDR} = E\!\left(\frac{V}{\max(R, 1)}\right)$$

the **average fraction** of discoveries that are false. ($\max(R, 1)$ just avoids dividing by 0. A study with no discoveries counts as fraction 0.) Controlling FDR at 0.05 means that, on average, about 5% of the discoveries are false leads. Use it for **screening**: thousands of genes, hundreds of product features, where you'll check the hits again later.

![Ten rows, one per repeated study, each made of green squares for true discoveries and red squares for false ones; three rows contain a red square. For each row V/R is shown: 1/8 = 0.125, 1/9 = 0.111 and 2/9 = 0.222, and 0 for the rest. Bottom: FWER = 3/10 = 0.30 and FDR = average of the V/R values = 0.046. Right: boxes defining FWER = P(V ≥ 1) and FDR = E(V/max(R, 1))](figures/fwer_vs_fdr.png)

The same 10 studies scored two ways. 3 of the 10 studies contain a false discovery, so the FWER is 0.30. But false discoveries are only a small part of each list, so the FDR is just 0.046.

**4. The two can be very different.** In the figure, a method with FDR ≈ 0.05 still lets at least one false claim through in 30% of studies. FDR control makes more discoveries in exchange for accepting a few false ones.

**5. When all nulls are true, they're equal.** Then every discovery is false. $V/R$ is 1 whenever there is a discovery and 0 otherwise, so $\text{FDR} = P(V \ge 1) = \text{FWER}$. The difference appears only when some effects are real.

**6. FDR is about the long run, not one list.** "FDR = 0.05" does **not** guarantee that at most 5% of **this** list is false, and it doesn't give each discovery a 95% chance of being real.

---

## Goal

Define FWER and FDR, compute them from a set of studies, and choose which one to control.

## Formulas

$$\text{FWER} = P(V \ge 1), \qquad \text{FDR} = E\!\left(\frac{V}{\max(R, 1)}\right)$$

| Situation | Control | Typical method |
|---|---|---|
| few planned, confirmatory claims; one false claim is costly | FWER | Bonferroni, Holm (16.3) |
| many exploratory tests; hits will be checked again | FDR | Benjamini–Hochberg (16.4) |

---

## Example

A screening study is repeated 10 times. Each time it reports a list of discoveries. Because this is a teaching example, we know which are true:

| Study | Discoveries $R$ | False $V$ | Any false? | $V/R$ |
|---:|---:|---:|---|---:|
| 1 | 8 | 0 | no | 0 |
| 2 | 8 | 1 | **yes** | 0.125 |
| 3 | 9 | 0 | no | 0 |
| 4 | 6 | 0 | no | 0 |
| 5 | 9 | 1 | **yes** | 0.111 |
| 6 | 7 | 0 | no | 0 |
| 7 | 9 | 0 | no | 0 |
| 8 | 8 | 0 | no | 0 |
| 9 | 9 | 2 | **yes** | 0.222 |
| 10 | 8 | 0 | no | 0 |

**FWER estimate:** 3 of 10 studies had at least one false discovery.
$$\widehat{\text{FWER}} = \frac{3}{10} = 0.30$$

**FDR estimate:** average of the $V/R$ column.
$$\widehat{\text{FDR}} = \frac{0.125 + 0.111 + 0.222}{10} = \frac{0.458}{10} = 0.046$$

This procedure controls FDR at about 5% but not FWER. If even one false claim would be a disaster, it is the wrong tool.

---

## Doing it in Excel

With $V$ in column B and $R$ in column C: FWER `=COUNTIF(B2:B11,">0")/10`, FDR `=AVERAGE(D2:D11)` where `D2 = B2/MAX(C2,1)`.

---

## Your turn

A Benjamini–Hochberg procedure at $q = 0.05$ produces 20 discoveries. Does that guarantee at most one of them is false?

**Answer:** No. FDR control is a promise about the **average** false fraction over many repeated studies, under the procedure's conditions. A particular list of 20 could contain 0, 1, 3 or more false discoveries.

---

## Key takeaways

- $V$ = false discoveries, $R$ = all discoveries.
- FWER = $P(V \ge 1)$: the chance of any false claim. Strict, for confirmatory work.
- FDR = average of $V/R$: the expected share of false claims. Lenient, for screening.
- With all nulls true, FDR = FWER. With real effects present, FDR can be far below FWER.
- Neither tells you which particular discoveries are false.

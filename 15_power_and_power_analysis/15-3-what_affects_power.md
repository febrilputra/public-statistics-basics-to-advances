# Lesson 15.3 - What Affects Power?

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Chapter 9 (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 15 - Power and Power Analysis

## The big picture: four dials

Power depends on how far apart the two curves of Lesson 15.1 are, measured in standard errors:

$$\frac{\Delta}{\text{SE}} = \frac{\Delta}{\sigma\sqrt{2/n}} = d\sqrt{\frac{n}{2}}$$

The bigger this number, the less the curves overlap and the higher the power. That gives four dials:

| Dial | Turn it... | Power... | Why |
|---|---|---|---|
| sample size $n$ | up | **up** | SE shrinks like $1/\sqrt n$, so the curves get narrower |
| effect $\Delta$ (or $d$) | up | **up** | the curves move further apart |
| noise $\sigma$ | down | **up** | smaller $\sigma$ means bigger $d$ and smaller SE |
| significance level $\alpha$ | up (e.g. 0.10) | **up** | the cutoff moves in, but there are more false alarms |

A one-sided test also has more power in the predicted direction, but only if the direction was fixed **before** seeing the data (Lesson 10.3).

![Three panels. Left: with 16 per group the null and alternative curves are wide and overlap a lot, so power ≈ 0.29. Middle: with 64 per group the curves are narrow, so power ≈ 0.81. Right: power curves against n per group for d = 0.8, 0.5, 0.3 and 0.2, crossing 80% at 26, 64, 176 and 394 per group](figures/what_affects_power.png)

Left and middle: the same 2-minute effect. Quadrupling the sample halves the SE, and power jumps from 0.29 to 0.81. Right: the smaller the effect, the more people you need. Halving $d$ from 0.5 to about 0.25 needs roughly four times the sample.

**1. More data helps, but with diminishing returns.** The SE goes down like $1/\sqrt n$. To halve the SE you need **four times** as many observations.

**2. Small effects are expensive.** The sample size needed is roughly proportional to $1/d^2$ (Lesson 15.4). Halving the effect you want to detect means about **four times** the sample.

**3. Reducing noise is often the cheapest dial.** Better measurement, more uniform conditions, or a **paired design** (Lesson 11.4: each unit is its own control) all shrink $\sigma$. That raises power without more units.

**4. Independent units count, repeats don't.** Ten measurements of the same batch are not ten independent batches. For clustered data (e.g. $m$ batches from each of several machines), a rough "design effect" $1 + (m - 1)\rho$ shows how much the effective sample shrinks when observations in a cluster are correlated with correlation $\rho$.

**5. Don't change α after seeing the data.** Raising $\alpha$ buys power at the cost of more false alarms. It's a choice for the planning stage, never a rescue for a result that just missed.

---

## Goal

Predict how power changes with sample size, effect size, noise and α, and use a table of required sample sizes.

## Formulas

$$\text{Power} \approx P\!\left(Z > z_{\alpha/2} - d\sqrt{\tfrac{n}{2}}\right)$$

---

## Example

Same workshop: $\Delta = 2$, $\sigma = 4$ ($d = 0.5$), $\alpha = 0.05$.

**With $n = 16$ per group:**
$$d\sqrt{n/2} = 0.5\sqrt{8} = 1.414, \qquad \text{Power} \approx P(Z > 1.96 - 1.414) = P(Z > 0.546) = 0.29$$

**With $n = 64$ per group:**
$$d\sqrt{n/2} = 0.5\sqrt{32} = 2.828, \qquad \text{Power} \approx P(Z > 1.96 - 2.828) = P(Z > -0.868) = 0.81$$

Four times the sample doubles $d\sqrt{n/2}$, and power goes from about 29% to 81%.

**Sample size per group needed** (exact two-sample t-test, two-sided $\alpha = 0.05$), always rounded **up**:

| $d$ | 80% power | 90% power |
|---:|---:|---:|
| 0.2 | 394 | 527 |
| 0.3 | 176 | 235 |
| 0.5 | 64 | 86 |
| 0.8 | 26 | 34 |

Going from 80% to 90% power costs about a third more people. With $d = 0.5$, a stricter $\alpha = 0.01$ needs **96** per group instead of 64.

---

## Doing it in Excel

`=1-NORM.S.DIST(1.96-0.5*SQRT(16/2), TRUE)` → 0.29 (change 16 to try other sample sizes)

---

## Your turn

Approximately how does the required sample size change if the target effect is halved, with SD, power and α unchanged?

**Answer:** It goes up about **four times**, because $n$ is proportional to $1/d^2$ and $(1/0.5)^2 = 4$. The table agrees: $d = 0.5$ needs 64 per group, and $d = 0.25$ needs about 253 per group.

---

## Key takeaways

- Power grows with $d\sqrt{n/2}$: bigger effects, bigger samples and less noise all help.
- Halving SE or halving the detectable effect each needs about four times the sample.
- Reducing noise (better measurement, pairing, blocking) is often the cheapest way to gain power.
- Count independent units, not repeated measurements of the same unit.
- Choose α during planning, never after seeing the result.

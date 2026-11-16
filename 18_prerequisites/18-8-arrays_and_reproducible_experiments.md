# Lesson 18.8 - Arrays and Reproducible Experiments in Python

> **Reading:** *The StatQuest Illustrated Guide to Statistics*, Appendices A–F (Starmer, 2026) · [references](../Reference.md#sq-statquest)
> **Chapter:** 18 - Mathematical and Python Prerequisites

## The big picture: small coding slips change the statistical question

The simulations and figures in Chapters 14–18 are made with Python (NumPy, SciPy, Matplotlib). A few habits prevent most mistakes.

**1. Know the shape, and which axis you average over.** A simulation often stores results in a 2-D array with shape `(experiments, observations)`, e.g. 1,000 experiments of 20 observations each: shape `(1000, 20)`.

- `samples.mean(axis=1)` gives **one mean per experiment**: 1,000 numbers. Usually this is what you want.
- `samples.mean(axis=0)` gives one mean per column: 20 numbers.
- `samples.mean()` (no axis) gives one number: the mean of all 20,000 values.

**2. Variance: NumPy divides by $n$ unless told otherwise.** `np.var(x)` and `np.std(x)` use `ddof=0` and divide by $n$, which is the **population** formula. The usual **sample** variance divides by $n - 1$ (Lesson 3.13): use `np.var(x, ddof=1)`. pandas' `.var()` and Excel's `VAR.S` already use $n - 1$. Always check which one you're getting.

![Left: a 6-by-5 grid of numbers (6 experiments, 5 observations each) with one orange mean per row from mean(axis=1) and one green mean per column from mean(axis=0). Right: bars of the average variance estimate over 20,000 samples of size 5 from a population with σ² = 4: np.var(x) with ddof=0 gives 3.19, too small, while np.var(x, ddof=1) gives 3.99, matching the true value](figures/arrays_axes_and_ddof.png)

Left: `axis=1` collapses each row (one mean per experiment). `axis=0` collapses each column. Right: dividing by $n$ underestimates the variance by the factor $(n - 1)/n$, which is 0.8 for $n = 5$. Dividing by $n - 1$ is right on target.

**3. Missing values are not zeros.** A `NaN` (not a number) means "unknown". `np.mean` returns `nan` if any value is missing, and `np.nanmean` skips them. Silently dropping rows can also make two models use **different** observations, and then comparisons like the F-test of Lesson 14.4 are invalid.

**4. Reproducibility.**

- Use a **seeded** random generator: `rng = np.random.default_rng(123)`. The same seed gives the same "random" numbers, so the results can be repeated and checked. A seed makes a calculation repeatable. It doesn't make the model correct.
- **Restart and run everything from top to bottom** before trusting a notebook or script. Leftover variables from an earlier run can make broken code look like it works.
- Record package versions (e.g. a `requirements.txt` file). Tiny numerical differences across computers are normal.

---

## Goal

Choose the right axis and `ddof`, handle missing values deliberately, and make simulations reproducible.

## Formulas

$$\text{np.var}(x) = \frac{1}{n}\sum (x - \bar x)^2, \qquad \text{np.var}(x, \text{ddof}=1) = \frac{1}{n - 1}\sum (x - \bar x)^2 = s^2$$

$$E\big(\text{np.var}(x)\big) = \frac{n - 1}{n}\,\sigma^2$$

---

## Example

**Step 1: the shape of a simulation.**

```python
import numpy as np
rng = np.random.default_rng(123)              # seeded: same numbers every run
samples = rng.normal(loc=50, scale=10, size=(1000, 20))
print(samples.shape)                          # (1000, 20)
means = samples.mean(axis=1)                  # one mean per experiment
print(means.shape)                            # (1000,)
print(means.std(ddof=1))                      # about 10/sqrt(20) = 2.24
print(samples.std(ddof=1))                    # about 10: spread of single values
```

**Step 2: why the two SDs differ.** `samples.std` measures the spread of **individual** observations ($\sigma = 10$). `means.std` measures the spread of **means of 20** ($\sigma/\sqrt{20} = 2.24$, Lesson 18.3). Mixing them up is the SD vs SE confusion.

**Step 3: the ddof bias.** Draw 20,000 samples of size 5 from a population with $\sigma^2 = 4$:

| Formula | Average estimate | Expected |
|---|---:|---:|
| `np.var(x)` (÷ n) | 3.19 | $\tfrac{4}{5} \times 4 = 3.2$ |
| `np.var(x, ddof=1)` (÷ n − 1) | 3.99 | 4 |

---

## Doing it in Excel

`=VAR.S(range)` divides by $n - 1$ (sample) and `=VAR.P(range)` divides by $n$ (population). In Excel, `AVERAGE` and `VAR.S` skip empty cells, but a cell containing 0 is a real zero.

---

## Your turn

What does `samples.mean(axis=1)` return if `samples.shape == (1000, 20)`? Why is the SD of those values different from the SD of all 20,000 values?

**Answer:** It returns 1,000 means, one per experiment, each from 20 observations. With independent sampling, their SD is about the original SD divided by $\sqrt{20}$. It describes how much a **mean** varies, not how much a single observation varies.

---

## Key takeaways

- Check `.shape` and choose `axis` deliberately: `axis=1` gives one result per row (experiment).
- `np.var`/`np.std` divide by $n$ by default. Use `ddof=1` for the sample variance and SD.
- `NaN` is not 0. Handle missing values on purpose, and make compared models use the same rows.
- Seed the random generator and rerun everything from a fresh start. Record package versions.

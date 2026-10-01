# Chapter 01 notes: Data, populations, and summaries

Reading companion for chapter 1, original PDF pages 11-38. These notes use independently written explanations and invented examples. [Source and sharing information](README.md#source-and-sharing).

## The question to ask first

What population do I want to describe, and how did these observations enter my dataset? Calculating a mean is easy; deciding what that mean represents is the harder part.

A **population** is the complete set relevant to a question, such as all parcels processed at one depot during September. A **sample** contains some of those parcels. A population parameter describes the target population; a sample statistic estimates it. A new sample will usually produce a different estimate.

A complete dataset for September does not automatically describe December. Even a census can contain measurement errors or omissions.

## What kind of variable is this?

| Variable | Example | Useful distinction |
|---|---|---|
| Categorical | Delivery service | Labels have no numerical distance. |
| Ordered categorical | Standard, priority, urgent | The order matters; equal spacing is not implied. |
| Discrete numeric | Number of damaged items | Values occur in separate, countable steps. |
| Continuous numeric | Processing duration | The underlying quantity can vary continuously, even if recorded to whole seconds. |

Do not calculate a meaningful numerical average of arbitrary category codes. A mean service code of 1.8 has no inherent operational interpretation.

## Center and spread

For observations $x_1,\ldots,x_n$, the sample mean and variance are

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i,
\qquad
s^2=\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}.
$$

The sample standard deviation is $s=\sqrt{s^2}$. Variance has squared units; standard deviation has the original units. For a complete finite population, its descriptive variance uses the population size $N$ as the denominator.

Why $n-1$ for a sample variance? Estimating the mean uses one degree of freedom: the deviations from that fitted mean sum to zero. Under independent, identically distributed sampling with finite variance, dividing by $n-1$ makes $s^2$ unbiased for population variance. The square root $s$ is not itself exactly unbiased for population standard deviation.

## Worked example: Parcel processing

Five sampled processing times, in minutes, are **6, 8, 9, 11, 16**.

- Mean: $50/5=10$ minutes.
- Median: 9 minutes.
- Sum of squared deviations: $16+4+1+1+36=58$.
- Sample variance: $58/4=14.5$ square minutes.
- Sample standard deviation: $\sqrt{14.5}\approx3.81$ minutes.

The unusually long final time pulls the mean above the median. Keep both summaries and inspect the individual observations before deciding what is typical.

```python
from statistics import mean, median, variance, stdev

times = [6, 8, 9, 11, 16]
print(round(mean(times), 2), median(times))
print(round(variance(times), 2), round(stdev(times), 2))
# 10 9
# 14.5 3.81
```

## Interpretation checks

A large sample does not repair a biased selection process. Sampling only the easiest parcels can underestimate processing time, however precisely their average is measured. Standard deviation describes variation among observations; it is not the uncertainty of the estimated mean. That distinction returns in chapter 9.

## Practice

1. If these five parcels were the entire population of interest, what variance would describe it?
2. If every duration increased by 3 minutes, what would happen to the mean and standard deviation?

**Answers:** (1) $58/5=11.6$. (2) The mean becomes 13 minutes; the standard deviation stays the same.

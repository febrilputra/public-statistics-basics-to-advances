# Chapter 03 notes: Probability models and likelihood

Reading companion for chapter 3, original PDF pages 48-79. These notes use independently written explanations and invented examples. [Source and sharing information](README.md#source-and-sharing).

## Move from observations to a model

A probability model describes possible outcomes and their relative frequency under stated assumptions. Its parameters summarize features such as location, spread, or event rate. A fitted model can estimate probabilities between or beyond observed values, but those estimates inherit its assumptions.

A smooth curve does not make a model correct. Check whether the variable's possible values, the data-generating process, and the model's shape agree.

## Match the model to the question

| Model | Typical quantity | Important condition |
|---|---|---|
| Binomial | Number of successes in $n$ trials | Independent trials with a common success probability $p$. |
| Poisson | Number of events in a fixed exposure | A stable rate and independent increments in a Poisson-process interpretation. |
| Normal | A continuous measurement near a central value | Symmetric, bell-shaped variation is a reasonable approximation. |
| Exponential | Time until the next event | A constant event rate; the waiting-time model is memoryless. |
| Uniform | A value inside fixed bounds | Equal-length intervals have equal probability. |

For Poisson counts, expected count and variance both equal $\lambda$. Substantially greater observed variability can be a warning that this model misses clustering or varying rates.

## Mass, density, and cumulative probability

A discrete probability mass function gives probabilities of individual outcomes. For a continuous variable, a probability density function gives density; probabilities come from areas:

$$
P(a\le X\le b)=\int_a^b f(x)\,dx=F(b)-F(a),
$$

where $F$ is the cumulative distribution function. A continuous model assigns zero probability to one exact point. A rounded measurement represents an interval, not an infinitely precise point. Density can exceed 1 without violating probability rules because area, not height, must total 1.

## Two worked calculations

**Failed uploads.** Suppose eight uploads fail independently with probability 0.10 each. The probability of exactly two failures is

$$
P(X=2)=\binom{8}{2}(0.10)^2(0.90)^6\approx0.1488.
$$

**Sensor readings.** Suppose a sensor measurement is modeled as normal with mean 100 and standard deviation 5. The probability of a reading between 95 and 105 is approximately 0.6827. This is an implication of the model, not a guarantee that the next batch will have exactly that proportion.

```python
from math import comb
from statistics import NormalDist

p_two = comb(8, 2) * 0.1**2 * 0.9**6
sensor = NormalDist(mu=100, sigma=5)
p_interval = sensor.cdf(105) - sensor.cdf(95)
print(round(p_two, 4), round(p_interval, 4))
# 0.1488 0.6827
```

## Likelihood changes what is held fixed

For probability calculations, fix the parameters and consider possible data. For likelihood, hold the observed data fixed and compare parameter values. For independent observations,

$$
L(\theta;x_1,\ldots,x_n)=\prod_{i=1}^{n}f(x_i\mid\theta),
\qquad
\ell(\theta)=\sum_{i=1}^{n}\log f(x_i\mid\theta).
$$

The joint likelihood uses a **product** of masses or densities; the log-likelihood uses a sum of their logarithms. Maximizing likelihood chooses the best-fitting parameter value within the selected model. It does not produce a probability distribution over parameters without additional assumptions. See [NIST's likelihood reference](https://www.itl.nist.gov/div898/handbook/apr/section4/apr412.htm).

## Practice

1. For $X\sim\mathrm{Uniform}(0,12)$, calculate $P(3\le X\le6)$.
2. If failures occur in correlated bursts, which binomial assumption is questionable?

**Answers:** (1) $3/12=0.25$. (2) Independence; a single shared outage can affect several uploads.

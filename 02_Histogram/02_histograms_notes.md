# Chapter 02 notes: Histograms and empirical probabilities

Reading companion for chapter 2, original PDF pages 39-47. These notes use independently written explanations and invented examples. [Source and sharing information](README.md#source-and-sharing).

## What a histogram answers

A histogram shows how numerical observations are distributed across intervals. It can reveal concentration, asymmetry, unusual values, and multiple clusters that a single mean hides.

Choose interval boundaries, count the observations within each interval, then decide whether the vertical axis shows counts, proportions, or density. Record that choice in the axis label. A bar chart of named categories serves a different purpose: the positions and widths of histogram bins have numerical meaning.

## Worked example: Job completion times

Ten simulated job durations, in seconds, are **2, 3, 5, 6, 7, 9, 11, 12, 14, 18**. Use left-inclusive, right-exclusive intervals:

| Interval, seconds | Count | Proportion | Density per second |
|---|---:|---:|---:|
| $[0,5)$ | 2 | 0.20 | 0.04 |
| $[5,10)$ | 4 | 0.40 | 0.08 |
| $[10,15)$ | 3 | 0.30 | 0.06 |
| $[15,20)$ | 1 | 0.10 | 0.02 |

A duration of exactly 5 belongs in the second bin. Giving boundaries an explicit convention prevents double counting.

The observed proportion of jobs taking at least 5 but less than 15 seconds is

$$
\widehat{P}(5\le X<15)=\frac{4+3}{10}=0.70.
$$

This describes the sample. Interpreting it as a future-job probability requires the sample to represent the process that will generate future jobs.

## Why area matters

For bin $j$, with count $c_j$ and width $w_j$, a density histogram uses

$$
h_j=\frac{c_j}{n w_j}.
$$

Its bar area is $h_jw_j=c_j/n$, so the total area is 1. With unequal bin widths, heights alone do not represent relative probabilities. A wide interval can contain more observations while having lower density.

For example, 20 observations in a 10-second interval and 20 in a 2-second interval have the same probability mass. The second interval has five times the density.

```python
durations = [2, 3, 5, 6, 7, 9, 11, 12, 14, 18]
edges = [0, 5, 10, 15, 20]
counts = [sum(lo <= x < hi for x in durations)
          for lo, hi in zip(edges, edges[1:])]
probability = sum(5 <= x < 15 for x in durations) / len(durations)
print(counts)
print(probability)
# [2, 4, 3, 1]
# 0.7
```

## What can go wrong?

Very wide bins can hide structure; very narrow bins can turn sampling noise into apparent patterns. Try several reasonable choices and keep the scale consistent when comparing datasets. If the groups contain different numbers of observations, proportions or densities usually make comparison easier than raw counts.

A histogram discards exact positions within bins. If a requested probability interval cuts through a bin, use the original observations when available. Taking a fraction of that bar's area otherwise assumes something about how values are distributed inside it.

## Practice

1. What is the observed proportion of jobs taking at least 10 seconds?
2. Does an empty sample bin establish that the corresponding event is impossible?

**Answers:** (1) $4/10=0.40$. (2) No. An empty bin can result from limited sampling; impossibility requires information beyond that absence.

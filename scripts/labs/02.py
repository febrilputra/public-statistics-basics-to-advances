# %% histogram_scales
waits = np.array([2,3,4,4,5,6,6,7,8,8,9,10,11,12,12,13,14,16,18,22])
edges = np.arange(0, 26, 5)
counts, _ = np.histogram(waits, bins=edges)
assert np.array_equal(counts, [4,7,6,2,1])
display(pd.DataFrame({"left_edge": edges[:-1], "right_edge": edges[1:],
                      "count": counts, "proportion": counts/len(waits),
                      "density": counts/(len(waits)*np.diff(edges))}))
fig, axes = plt.subplots(1, 3, figsize=(12, 4), layout="constrained")
for ax, heights, label in zip(axes, [counts, counts/20, counts/100],
                            ["Count", "Relative frequency", "Density (per minute)"]):
    ax.bar(edges[:-1], heights, width=5, align="edge", color=TEAL, edgecolor="white")
    ax.set(xlabel="Queue time (minutes)", ylabel=label, title=label, xticks=edges)
save_figure(fig, "three_scales")

# %% unequal_bins
unequal = np.array([0,5,15,25])
c, _ = np.histogram(waits, bins=unequal)
widths = np.diff(unequal)
density = c / (len(waits) * widths)
assert np.isclose(np.sum(density * widths), 1)
fig, ax = plt.subplots(layout="constrained")
ax.bar(unequal[:-1], density, width=widths, align="edge", edgecolor="white", color=TEAL)
for left, width, height, count in zip(unequal[:-1], widths, density, c):
    ax.text(left+width/2, height+.003, f"area = {count/20:.2f}", ha="center")
ax.set(xlabel="Queue time (minutes)", ylabel="Density (per minute)", ylim=(0,.08),
       xticks=unequal, title="With unequal widths, probability is rectangle area")
save_figure(fig, "unequal_bins")

# %% bin_sensitivity
rng = np.random.default_rng(202)
mixture = np.r_[rng.normal(8, 1.3, 230), rng.normal(14, 1.8, 170)]
fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True, layout="constrained")
for ax, bins in zip(axes, [4, 16, 70]):
    ax.hist(mixture, bins=np.linspace(2,22,bins+1), density=True, color=TEAL, edgecolor="white")
    ax.set(xlabel="Synthetic time (minutes)", title=f"Same 400 observations, {bins} bins")
axes[0].set_ylabel("Density (per minute)")
save_figure(fig, "bin_choices")
print("Freedman-Diaconis suggested number of bins:", len(np.histogram_bin_edges(mixture, bins="fd"))-1)

# %% empirical_cdf
sorted_waits = np.sort(waits)
fig, ax = plt.subplots(layout="constrained")
ax.step(np.r_[0, sorted_waits, 25], np.r_[0, np.arange(1,21)/20, 1], where="post", color=TEAL)
ax.scatter([12], [(waits<=12).mean()], color=ORANGE, s=90, zorder=3)
ax.axvline(12, color=ORANGE, ls="--", alpha=.6)
ax.set(xlabel="Queue time t (minutes)", ylabel="Fraction at or below t", ylim=(-.03,1.05),
       title="The empirical CDF uses every observation without bins")
save_figure(fig, "ecdf")
print("P-hat(X > 12) =", (waits>12).mean())
print("95% upper bound after zero events in 20 trials:", 1-.05**(1/20))

# %% practice
distance = np.array([1,2,2,3,5,6,7,9])
counts, edges = np.histogram(distance, [0,3,6,10])
display(pd.DataFrame({"count": counts, "proportion": counts/8,
                      "density_per_km": counts/(8*np.diff(edges))}))
assert np.array_equal(counts, [3,2,3])
assert (distance>=6).mean() == 3/8
print("F-hat(6) =", (distance<=6).mean())
print("Upper bound for zero failures in 100 tests:", 1-.05**.01)

# %% summaries
x = np.array([96, 98, 100, 102, 104], dtype=float)
deviations = x - x.mean()
display(pd.DataFrame({"mass_g": x, "deviation_g": deviations, "squared_g2": deviations**2}))
print(f"Mean={x.mean():.3f}; population descriptive variance={x.var(ddof=0):.3f}")
print(f"Sample variance={x.var(ddof=1):.3f}; sample SD={x.std(ddof=1):.3f}")
assert np.isclose(np.sum(deviations**2), 40)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), layout="constrained")
axes[0].vlines(np.arange(1, 6), 0, deviations, color=TEAL, lw=3)
axes[0].scatter(np.arange(1, 6), deviations, color=TEAL, s=65)
axes[0].axhline(0, color="black", lw=1)
axes[0].set(xlabel="Notebook number", ylabel="Deviation from mean (g)", title="Signed deviations cancel", xticks=np.arange(1, 6))
for row, values in enumerate([x, np.array([96, 98, 100, 102, 144])]):
    axes[1].scatter(values, np.full(5, row), s=60, color=TEAL)
    axes[1].plot(values.mean(), row, "|", ms=28, mew=3, color=ORANGE, label="Mean" if row == 0 else None)
    axes[1].plot(np.median(values), row, "x", ms=10, mew=2, color=PURPLE, label="Median" if row == 0 else None)
axes[1].set(xlabel="Mass (g)", yticks=[0, 1], yticklabels=["Original", "One unusual mass"], ylim=(-.6, 1.7), title="The mean responds to magnitude")
axes[1].legend(loc="upper right")
save_figure(fig, "center_spread")

# %% variance_bias
rng = np.random.default_rng(101)
n, repetitions, sigma = 5, 20000, 4
samples = rng.normal(100, sigma, size=(repetitions, n))
v_n = samples.var(axis=1, ddof=0)
v_corrected = samples.var(axis=1, ddof=1)
print(f"Average with n: {v_n.mean():.3f}; target {(n-1)/n*sigma**2:.3f}")
print(f"Average with n-1: {v_corrected.mean():.3f}; target {sigma**2:.3f}")
fig, ax = plt.subplots(layout="constrained")
ax.hist(v_n, bins=70, range=(0, 65), density=True, alpha=.5, label="Divide by n")
ax.hist(v_corrected, bins=70, range=(0, 65), density=True, alpha=.5, label="Divide by n - 1")
ax.axvline(sigma**2, color="black", ls="--", label="True variance = 16")
ax.set(xlabel="Estimated variance (g²)", ylabel="Density", title="Unbiased on average does not mean exact in one sample")
ax.legend()
save_figure(fig, "variance_estimators")

# %% sampling_means
rng = np.random.default_rng(102)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), layout="constrained")
individuals = rng.normal(100, 4, 30000)
axes[0].hist(individuals, bins=65, density=True, color=TEAL, alpha=.7)
axes[0].set(title="Individual masses: SD = 4 g", xlabel="Mass (g)", ylabel="Density (per g)")
for size in [5, 50]:
    means = rng.normal(100, 4, (8000, size)).mean(axis=1)
    axes[1].hist(means, bins=50, density=True, alpha=.55, label=f"n={size}, SE={4/np.sqrt(size):.2f} g")
axes[1].set(title="Sample means have smaller spread", xlabel="Mean mass (g)", ylabel="Density (per g)")
axes[1].legend()
for ax in axes:
    ax.set_xlim(86, 114)
save_figure(fig, "sd_vs_se")

# %% practice
cables = np.array([8, 10, 10, 12], dtype=float)
assert np.isclose(cables.var(ddof=1), 8/3)
assert np.isclose((10*cables).var(ddof=1), 100*cables.var(ddof=1))
print({"mean": cables.mean(), "median": np.median(cables),
       "sample_variance": cables.var(ddof=1), "sample_sd": cables.std(ddof=1),
       "estimated_se": stats.sem(cables)})

# %% first_comparison
desk = np.array([6, 8, 7, 9, 10], dtype=float)
kiosk = np.array([5, 7, 6, 8, 9], dtype=float)
print(f"Desk mean: {desk.mean():.1f}; kiosk mean: {kiosk.mean():.1f}")
print(f"Kiosk - desk: {kiosk.mean() - desk.mean():.1f} minutes")
fig, ax = plt.subplots(layout="constrained")
for i, (name, values, color) in enumerate([("Desk", desk, TEAL), ("Kiosk", kiosk, ORANGE)]):
    ax.scatter(values, np.full(len(values), i), s=80, color=color, label=f"{name}: observations")
    ax.plot(values.mean(), i, marker="|", ms=30, mew=3, color="black")
ax.set(yticks=[0, 1], yticklabels=["Desk", "Kiosk"], ylim=(-.6, 1.6),
       xlabel="Return time (minutes)", title="Different means, overlapping observations")
ax.text(.02, .95, "Black marks: sample means", transform=ax.transAxes, va="top")
save_figure(fig, "return_times")
changed = kiosk.copy()
changed[-1] = 20
print(f"After replacing 9 by 20: mean={changed.mean():.1f}, median={np.median(changed):.1f}")

# %% repeated_samples
rng = np.random.default_rng(100)
fig, ax = plt.subplots(layout="constrained")
for n in [5, 50]:
    differences = (rng.normal(7, 2, (8000, n)).mean(axis=1)
                   - rng.normal(8, 2, (8000, n)).mean(axis=1))
    ax.hist(differences, bins=55, density=True, alpha=.55, label=f"n = {n} per group")
    print(f"n={n}: mean estimate {differences.mean():.3f}, SD of estimates {differences.std():.3f}")
ax.axvline(-1, color="black", ls="--", label="True difference = -1")
ax.set(xlabel="Estimated kiosk - desk time (minutes)", ylabel="Density (per minute)",
       title="Larger independent samples stabilize an estimate")
ax.legend()
save_figure(fig, "sampling_difference")

# %% practice
locker = np.array([3, 4, 5, 8])
other_desk = np.array([5, 6, 7, 10])
assert locker.mean() - other_desk.mean() == -2
print("Practice 2: locker - desk =", locker.mean() - other_desk.mean(), "minutes")

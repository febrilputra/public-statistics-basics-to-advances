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
from matplotlib.ticker import FuncFormatter, PercentFormatter

distance = np.array([1,2,2,3,5,6,7,9])
counts, edges = np.histogram(distance, [0,3,6,10])
sample_size = len(distance)
widths = np.diff(edges)
probabilities = counts / sample_size
density_heights = probabilities / widths
display(pd.DataFrame({"bin": ["[0,3)", "[3,6)", "[6,10]"],
                      "count": counts, "width_km": widths,
                      "proportion": probabilities, "density_per_km": density_heights}))
assert np.array_equal(counts, [3,2,3])
assert (distance>=6).mean() == 3/8
print("F-hat(6) =", (distance<=6).mean())
print("Upper bound for zero failures in 100 tests:", 1-.05**.01)

exercise_labels = {
    "en": {
        "name": "travel_distance_exercise",
        "title": "Travel distances: one dataset, three histogram scales",
        "data": "Data: 1, 2, 2, 3, 5, 6, 7, 9 km   |   n = 8   |   Bins: [0, 3), [3, 6), [6, 10]",
        "titles": [r"Counts: $c_j$", r"Probabilities: $\hat p_j=c_j/n$",
                   r"Density: $h_j=c_j/(n w_j)$"],
        "ylabels": ["Number of observations", "Empirical probability", "Density (per km)"],
        "xlabel": "Travel distance (km)",
        "area": "area",
        "footer": "Bin widths: 3, 3, 4 km. Probability is bar height in the middle panel and bar area in the density panel.",
    },
    "id": {
        "name": "travel_distance_exercise_indonesian",
        "title": "Jarak perjalanan: satu kumpulan data, tiga skala histogram",
        "data": "Data: 1, 2, 2, 3, 5, 6, 7, 9 km   |   n = 8   |   Kelas: [0, 3), [3, 6), [6, 10]",
        "titles": [r"Frekuensi: $c_j$", r"Probabilitas: $\hat p_j=c_j/n$",
                   r"Kepadatan: $h_j=c_j/(n w_j)$"],
        "ylabels": ["Jumlah pengamatan", "Probabilitas empiris", "Kepadatan (per km)"],
        "xlabel": "Jarak perjalanan (km)",
        "area": "luas",
        "footer": "Lebar kelas: 3, 3, 4 km. Probabilitas adalah tinggi batang di panel tengah dan luas batang di panel kepadatan.",
    },
}

for language, labels in exercise_labels.items():
    fig, axes = plt.subplots(1, 3, figsize=(13.2, 5.7))
    fig.subplots_adjust(left=0.065, right=0.98, bottom=0.22, top=0.74, wspace=0.32)
    fig.suptitle(labels["title"], fontsize=17, y=0.98)
    fig.text(0.5, 0.87, labels["data"], ha="center", fontsize=11, color="#475569")

    for index, (ax, heights, ymax) in enumerate(zip(
            axes, [counts, probabilities, density_heights], [4, 0.5, 0.16])):
        bars = ax.bar(edges[:-1], heights, width=widths, align="edge",
                       color=[TEAL, ORANGE, PURPLE], edgecolor="white", linewidth=1.4)
        ax.set(xlim=(0, 10), xticks=edges, ylim=(0, ymax),
               xlabel=labels["xlabel"], ylabel=labels["ylabels"][index])
        ax.set_title(labels["titles"][index], fontsize=12, pad=14)
        ax.grid(axis="y", color="#DCE2E8", linewidth=0.7)
        ax.set_axisbelow(True)
        for bar, value in zip(bars, heights):
            if index == 0:
                value_label = str(int(value))
            elif index == 1:
                value_label = f"{100 * value:g}%"
            else:
                value_label = f"{value:.5f}".rstrip("0")
            if language == "id":
                value_label = value_label.replace(".", ",")
            ax.text(bar.get_x() + bar.get_width()/2, value + 0.025*ymax,
                     value_label, ha="center", va="bottom", fontsize=11, fontweight="bold")
        if index == 0:
            ax.set_yticks(np.arange(5))
        elif index == 1:
            ax.yaxis.set_major_formatter(PercentFormatter(1, decimals=0))
        else:
            ax.set_yticks(np.arange(0, 0.161, 0.04))
            if language == "id":
                ax.yaxis.set_major_formatter(FuncFormatter(
                    lambda value, position: f"{value:.2f}".replace(".", ",")))
            for bar, probability in zip(bars, probabilities):
                area_label = f"{100 * probability:g}%"
                if language == "id":
                    area_label = area_label.replace(".", ",")
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
                         f"{labels['area']}\n{area_label}", ha="center", va="center",
                         fontsize=10, color="white", fontweight="bold")
    fig.text(0.065, 0.04, labels["footer"], fontsize=10, color="#475569")
    save_figure(fig, labels["name"])

# Worked answer 5: what the one-sided 95% upper bound means.
n_tests, alpha = 100, 0.05
p_upper = 1 - alpha**(1/n_tests)
assert np.isclose(p_upper, 0.02951, atol=5e-6)
assert np.isclose((1 - p_upper)**n_tests, alpha)
p_grid = np.linspace(0, 0.10, 501)
prob_all_pass = (1 - p_grid)**n_tests
fig, ax = plt.subplots(figsize=(10, 5.6), layout="constrained")
ax.axvspan(0, p_upper, color=TEAL, alpha=0.12)
ax.axvspan(p_upper, 0.10, color="#94A3B8", alpha=0.15)
ax.plot(p_grid, prob_all_pass, color=TEAL, lw=2.6)
ax.axhline(alpha, color=ORANGE, lw=1.5, ls="--")
ax.text(0.099, alpha + 0.015, "5% line", ha="right", color=ORANGE, fontsize=10)
ax.plot([p_upper, p_upper], [0, alpha], color=PURPLE, lw=1.3, ls=":")
ax.plot(p_upper, alpha, "o", color=PURPLE, ms=9, zorder=4)
ax.annotate("If p = 2.95%, P(all 100 pass) ≈ 5%\n→ upper bound $p_U$ ≈ 2.95%",
            xy=(p_upper, alpha), xytext=(0.036, 0.30), color=PURPLE, fontsize=11,
            arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.3))
ax.plot(0, 1, "o", color=TEAL, ms=9, clip_on=False, zorder=4)
ax.annotate("Observed failure rate: 0/100 = 0%", xy=(0, 1), xytext=(0.012, 0.93),
            fontsize=10, color="#334155", arrowprops=dict(arrowstyle="->", color="#334155"))
ax.plot(0.05, (1 - 0.05)**n_tests, "o", color="#475569", ms=7)
ax.annotate(f"If p = 5%: P(all pass) ≈ {100*(1-0.05)**n_tests:.1f}%\n(even less likely)",
            xy=(0.05, (1 - 0.05)**n_tests), xytext=(0.058, 0.17), fontsize=10, color="#475569",
            arrowprops=dict(arrowstyle="->", color="#475569"))
ax.text(p_upper/2, 0.62, "One-sided 95%\nconfidence interval\n0% to 2.95%", ha="center",
        fontsize=10, color=TEAL, fontweight="bold")
ax.text(0.068, 0.62, "Failure probabilities here make\n100 passes in a row less than 5% likely",
        ha="center", fontsize=10, color="#475569")
ax.xaxis.set_major_formatter(PercentFormatter(1, decimals=0))
ax.yaxis.set_major_formatter(PercentFormatter(1, decimals=0))
ax.set(xlim=(0, 0.10), ylim=(0, 1.03), xlabel="True failure probability per test, p",
       ylabel="P(zero failures in 100 tests) = $(1-p)^{100}$",
       title="Zero failures in 100 tests: where the 95% upper bound comes from")
ax.grid(color="#DCE2E8", linewidth=0.7)
ax.set_axisbelow(True)
save_figure(fig, "zero_failure_upper_bound")

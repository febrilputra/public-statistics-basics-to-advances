"""Draw every figure for Chapter 15 - Power and Power Analysis.

Run with Python, NumPy, SciPy and Matplotlib installed:
    python 15_power_and_power_analysis/figures/make_figures.py
Each figure is written beside this script as a PNG (for the notes) and an SVG.
The planning example: smallest useful difference 2 minutes, SD 4 minutes, alpha = 0.05.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
from scipy import stats

OUT = Path(__file__).resolve().parent
BLUE, ORANGE, GREEN, YELLOW = "#0072B2", "#D55E00", "#009E73", "#E69F00"
INK, MUTED, RED, LIGHTRED, GRID, LIGHTBLUE = "#222222", "#555555", "#C0392B", "#E8B4B4", "#E6E6E6", "#BFD3E6"
LIGHTGREEN, LIGHTORANGE = "#BFE6D8", "#F6D3BC"

plt.rcParams.update({
    "font.family": ["Arial", "DejaVu Sans"], "font.size": 12, "text.color": INK,
    "axes.labelcolor": INK, "axes.edgecolor": MUTED, "xtick.color": INK, "ytick.color": INK,
    "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none",
    "mathtext.fontset": "dejavusans", "figure.facecolor": "white", "axes.facecolor": "white",
})


def figure(title, subtitle, ncols, size=(15, 7.4), top=0.76, bottom=0.25, wspace=0.32, **kw):
    fig, axes = plt.subplots(1, ncols, figsize=size, **kw)
    fig.subplots_adjust(left=0.06, right=0.98, top=top, bottom=bottom, wspace=wspace)
    fig.text(0.5, 0.955, title, ha="center", va="center", fontsize=22, fontweight="bold")
    fig.text(0.5, 0.905, subtitle, ha="center", va="center", fontsize=13.5, color=MUTED)
    return fig, axes


def panel(ax, title, subtitle):
    ax.text(0.5, 1.13, title, transform=ax.transAxes, ha="center", va="bottom", fontsize=15, fontweight="bold")
    ax.text(0.5, 1.05, subtitle, transform=ax.transAxes, ha="center", va="bottom", fontsize=12, color=MUTED)


def note(fig, bold, rest, y=0.03, h=0.115):
    fig.add_artist(FancyBboxPatch((0.07, y), 0.86, h, boxstyle="round,pad=0,rounding_size=0.012",
                                  transform=fig.transFigure, fill=False, ec=INK, lw=1.5))
    fig.text(0.5, y + h * 0.68, bold, ha="center", va="center", fontsize=13, fontweight="bold")
    fig.text(0.5, y + h * 0.3, rest, ha="center", va="center", fontsize=12.5, color=MUTED)


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=140)
    fig.savefig(OUT / f"{name}.svg")
    plt.close(fig)
    print("wrote", name)


def t_power(d, n, alpha=0.05):
    """Exact power of the two-sided pooled two-sample t-test, n per group."""
    df = 2 * n - 2
    nc = d * np.sqrt(n / 2)
    c = stats.t.isf(alpha / 2, df)
    return stats.nct.sf(c, df, nc) + stats.nct.cdf(-c, df, nc)


DELTA, SIGMA = 2.0, 4.0


def sampling_curves(ax, n, show_labels=True, ymax=None):
    """Null and alternative sampling distributions of the mean difference (known-SD z picture)."""
    se = SIGMA * np.sqrt(2 / n)
    cut = 1.96 * se
    x = np.linspace(-4.2 * se, DELTA + 4.2 * se, 800)
    h0, ha = stats.norm.pdf(x, 0, se), stats.norm.pdf(x, DELTA, se)
    ax.plot(x, h0, color=BLUE, lw=2.4)
    ax.plot(x, ha, color=ORANGE, lw=2.4)
    ax.fill_between(x, ha, where=x >= cut, color=LIGHTGREEN, alpha=0.95)
    ax.fill_between(x, ha, where=(x < cut) & (x > -cut), color=LIGHTORANGE, alpha=0.9)
    ax.fill_between(x, h0, where=np.abs(x) >= cut, color=RED, alpha=0.75)
    for c in (-cut, cut):
        ax.axvline(c, color=MUTED, lw=1.2, ls="--")
    power = stats.norm.sf(cut, DELTA, se) + stats.norm.cdf(-cut, DELTA, se)
    ax.set_xlabel("difference in sample means, x̄_B − x̄_A (minutes)")
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    if ymax:
        ax.set_ylim(0, ymax)
    return se, cut, power


# ---------------------------------------------------------------- 15.1
def power_two_curves():
    fig, (ax0, ax) = figure("Power: the chance a study detects an effect that is really there",
                            "Two groups of n = 64, SD σ = 4 minutes, true difference Δ = 2 minutes, two-sided α = 0.05",
                            2, wspace=0.12)
    ax0.set_position([0.04, 0.27, 0.33, 0.45])
    ax.set_position([0.43, 0.25, 0.55, 0.5])
    ax0.axis("off")
    cells = [[("", None), ("H₀ true\n(no effect)", None), ("Hₐ true\n(real effect)", None)],
             [("reject H₀", None), ("Type I error\nprob. α", LIGHTRED), ("correct!\nprob. = POWER", LIGHTGREEN)],
             [("fail to\nreject H₀", None), ("correct\nprob. 1 − α", "#EEF2F6"), ("Type II error\nprob. β", LIGHTORANGE)]]
    for i, row in enumerate(cells):
        for j, (txt, col) in enumerate(row):
            x0, y0, w, h = 0.02 + j * 0.33, 0.72 - i * 0.33, 0.31, 0.3
            if col:
                ax0.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=0.02",
                                             transform=ax0.transAxes, fc=col, ec="white"))
            ax0.text(x0 + w / 2, y0 + h / 2, txt, transform=ax0.transAxes, ha="center", va="center",
                     fontsize=12.5, fontweight="bold" if (i == 0 or j == 0) else "normal",
                     color=BLUE if i == 0 else INK)
    ax0.text(0.5, 1.13, "The four outcomes of a test", transform=ax0.transAxes, ha="center", fontsize=15, fontweight="bold")
    ax0.text(0.5, 1.05, "power = 1 − β", transform=ax0.transAxes, ha="center", fontsize=12, color=MUTED)

    se, cut, power = sampling_curves(ax, 64)
    ax.text(0, stats.norm.pdf(0, 0, se) + 0.02, "if H₀ is true\n(centre 0)", ha="center", color=BLUE, fontsize=12, fontweight="bold")
    ax.text(DELTA, stats.norm.pdf(0, 0, se) + 0.02, "if Δ = 2 is true\n(centre 2)", ha="center", color=ORANGE, fontsize=12, fontweight="bold")
    ax.text(2.7, 0.13, f"POWER\n≈ {power:.2f}", color=GREEN, fontsize=15, fontweight="bold", ha="center")
    ax.text(0.85, 0.07, f"β ≈ {1 - power:.2f}", color=ORANGE, fontsize=13, fontweight="bold", ha="center")
    ax.annotate("α/2 = 0.025\nin each tail", xy=(-cut - 0.25, 0.012), xytext=(-2.6, 0.2), color=RED, fontsize=11.5,
                arrowprops=dict(arrowstyle="->", color=RED))
    ax.text(0.99, 0.97, f"dashed lines = cutoffs\n±1.96·SE = ±{cut:.2f} minutes", transform=ax.transAxes,
            ha="right", va="top", color=MUTED, fontsize=11.5)
    ax.set_ylim(0, 0.75)
    panel(ax, "Two possible worlds for the observed difference", f"SE = σ√(2/n) = 4√(2/64) = {se:.3f} minutes")
    note(fig, "Red: false alarms when there is no effect (α). Green: detections when the effect is real (power).",
         "Power belongs to a planned design AND an assumed effect. It is not the chance that the treatment works.")
    save(fig, "power_two_curves")
    return se, cut, power


# ---------------------------------------------------------------- 15.2
def effect_size_overlap():
    fig, axes = figure("Cohen's d: the difference measured in standard deviations",
                       "Individual measurements of two groups, d = (μ_B − μ_A)/σ. Bigger d → less overlap → easier to detect.", 3)
    x = np.linspace(-4, 5, 600)
    for ax, d, lab in zip(axes, [0.2, 0.5, 0.8], ["'small'", "'medium'", "'large'"]):
        ax.plot(x, stats.norm.pdf(x), color=BLUE, lw=2.4, label="group A")
        ax.plot(x, stats.norm.pdf(x, d), color=ORANGE, lw=2.4, label="group B")
        ax.fill_between(x, np.minimum(stats.norm.pdf(x), stats.norm.pdf(x, d)), color=MUTED, alpha=0.18)
        ovl = 2 * stats.norm.cdf(-d / 2)
        for m, c in [(0, BLUE), (d, ORANGE)]:
            ax.plot([m, m], [0, 0.43], color=c, ls=":", lw=1.3)
        ax.plot([0, d], [0.43, 0.43], color=GREEN, lw=2.5)
        ax.text(d / 2, 0.445, f"gap = {d} σ", ha="center", color=GREEN, fontsize=13, fontweight="bold")
        ax.text(0.5, 0.06, f"overlap {ovl:.0%}", transform=ax.transAxes, ha="center", fontsize=12.5, color=MUTED, fontweight="bold")
        ax.set_ylim(0, 0.5)
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.set_xticks(range(-3, 5), [f"{v}σ" if v else "μ_A" for v in range(-3, 5)])
        extra = " · our example: d = 2/4" if d == 0.5 else ""
        panel(ax, f"d = {d}", f"Cohen's rough label: {lab}{extra}")
    axes[0].legend(loc="upper left", frameon=False)
    note(fig, "Choose d from the smallest difference that would matter in practice, not from an optimistic pilot study.",
         "Even with heavy overlap of individuals, a big enough study can estimate the difference in MEANS precisely.")
    save(fig, "effect_size_overlap")


# ---------------------------------------------------------------- 15.3
def what_affects_power():
    fig, axes = figure("What raises power?", "Bigger samples narrow the curves; bigger effects pull them apart.", 3)
    ymax = 0.62
    se16, _, p16 = sampling_curves(axes[0], 16, ymax=ymax)
    se64, _, p64 = sampling_curves(axes[1], 64, ymax=ymax)
    for ax, n, se, p in [(axes[0], 16, se16, p16), (axes[1], 64, se64, p64)]:
        ax.set_xlim(-4.5, 6.5)
        ax.text(0.97, 0.88, f"power ≈ {p:.2f}", transform=ax.transAxes, ha="right", color=GREEN, fontsize=15, fontweight="bold")
        panel(ax, f"n = {n} per group", f"SE = 4√(2/{n}) = {se:.2f}")
    ns = np.arange(5, 451)
    ax = axes[2]
    for d, c in zip([0.8, 0.5, 0.3, 0.2], [GREEN, BLUE, ORANGE, RED]):
        pw = np.array([t_power(d, n) for n in ns])
        ax.plot(ns, pw, color=c, lw=2.3, label=f"d = {d}")
        need = int(np.ceil(next(n for n in np.arange(4, 1000, 0.01) if t_power(d, n) >= 0.8)))
        ax.plot(need, t_power(d, need), "o", color=c, ms=7)
        dx, dy = (-6, 0.05) if d == 0.8 else (8, -0.08)
        ax.text(need + dx, t_power(d, need) + dy, str(need), color=c, fontsize=12, fontweight="bold",
                ha="right" if d == 0.8 else "left")
    ax.axhline(0.8, color=MUTED, ls="--", lw=1.2)
    ax.text(445, 0.82, "80%", ha="right", color=MUTED)
    ax.set_xlabel("n per group")
    ax.set_ylabel("power")
    ax.set_ylim(0, 1.02)
    ax.legend(loc="lower right", frameon=False)
    panel(ax, "Power curves (two-sample t-test)", "dots: smallest n per group with power ≥ 80%")
    note(fig, "Power rises with n, with the effect size d, and with α; it falls when the noise σ grows.",
         "Halving the effect you want to detect needs about 4 times the sample, because n is proportional to 1/d².")
    save(fig, "what_affects_power")
    return p16, p64


# ---------------------------------------------------------------- 15.4
def sample_size_steps():
    fig, (ax, ax2) = figure("Finding the sample size for 80% power",
                            "Two-sample t-test, d = 0.5, two-sided α = 0.05", 2, wspace=0.2)
    ns = np.linspace(40, 90, 400)
    pw = [t_power(0.5, n) for n in ns]
    ax.plot(ns, pw, color=BLUE, lw=2.5)
    ax.axhline(0.8, color=MUTED, ls="--", lw=1.2)
    for n, c, lab in [(63, RED, "63 → 0.795 (too low)"), (64, GREEN, "64 → 0.801 ✓")]:
        p = t_power(0.5, n)
        ax.plot(n, p, "o", color=c, ms=9, zorder=5)
        ax.text(n + (1.2 if n == 64 else -1.2), p + (0.012 if n == 64 else 0.025), lab, color=c, fontsize=12.5,
                fontweight="bold", ha="left" if n == 64 else "right")
    ax.axvline(63.77, color=ORANGE, lw=1.2, ls=":")
    ax.text(63.9, 0.6, "exact answer\n63.77", color=ORANGE, fontsize=11.5)
    ax.set_xlabel("n per group")
    ax.set_ylabel("power")
    ax.set_ylim(0.55, 0.95)
    panel(ax, "Read off where power reaches 0.80", "always round UP")

    ax2.axis("off")
    steps = [("1  Approximate formula", "n ≈ 2(1.960 + 0.842)² / 0.5² = 62.79", BLUE),
             ("2  Exact t-test calculation", "n = 63.77 per group", ORANGE),
             ("3  Round up", "64 per group · 128 in total (power 0.8015)", GREEN),
             ("4  Allow for 20% dropout", "64 / (1 − 0.20) = 80 per group to recruit", INK)]
    for i, (h, t, c) in enumerate(steps):
        y = 0.86 - i * 0.25
        ax2.add_patch(FancyBboxPatch((0.03, y - 0.09), 0.94, 0.18, boxstyle="round,pad=0,rounding_size=0.03",
                                     transform=ax2.transAxes, fc="white", ec=c, lw=1.8))
        ax2.text(0.07, y + 0.03, h, transform=ax2.transAxes, fontsize=13.5, fontweight="bold", color=c, va="center")
        ax2.text(0.07, y - 0.045, t, transform=ax2.transAxes, fontsize=13, va="center")
        if i < 3:
            ax2.annotate("", xy=(0.5, y - 0.16), xytext=(0.5, y - 0.09), xycoords="axes fraction",
                         arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.5))
    panel(ax2, "From formula to recruitment plan", "")
    note(fig, "The z-formula is a quick first guess; the t-test calculation is the one to report.",
         "Inflating for dropout assumes the people who drop out are like the ones who stay.")
    save(fig, "sample_size_steps")


# ---------------------------------------------------------------- 15.5
def simulated_power():
    fig, (ax, ax2) = figure("Checking power by simulation: run the study 10,000 times on the computer",
                            "Each study: 64 per group, σ = 4, true Δ = 2, pooled two-sample t-test at α = 0.05", 2, wspace=0.25)
    rng = np.random.default_rng(2024)
    B, n = 10_000, 64
    a = rng.normal(0, SIGMA, (B, n))
    b = rng.normal(DELTA, SIGMA, (B, n))
    t, p = stats.ttest_ind(b, a, axis=1)
    rej = p < 0.05
    crit = stats.t.isf(0.025, 2 * n - 2)
    bins = np.linspace(-2, 7, 61)
    ax.hist(t[~rej], bins=bins, color=LIGHTORANGE, ec="white", label=f"not significant ({(~rej).mean():.1%})")
    ax.hist(t[rej], bins=bins, color=GREEN, ec="white", alpha=0.85, label=f"significant ({rej.mean():.1%})")
    ax.axvline(crit, color=MUTED, ls="--")
    ax.text(crit - 0.15, ax.get_ylim()[1] * 0.75, f"t cutoff\n= {crit:.3f}", color=MUTED, fontsize=11.5, ha="right")
    ax.set_xlabel("t statistic of each simulated study")
    ax.set_ylabel("number of studies")
    ax.legend(loc="upper right", frameon=False)
    panel(ax, "10,000 simulated t statistics", "fraction beyond the cutoff = estimated power")

    run = np.cumsum(rej) / np.arange(1, B + 1)
    k = np.arange(1, B + 1)
    true = t_power(0.5, 64)
    band = 2 * np.sqrt(true * (1 - true) / k)
    ax2.fill_between(k, true - band, true + band, color=LIGHTBLUE, alpha=0.6, label="±2 Monte Carlo SE")
    ax2.plot(k, run, color=ORANGE, lw=1.8, label="running estimate")
    ax2.axhline(true, color=BLUE, lw=1.5, ls="--", label=f"theory {true:.4f}")
    ax2.set_xscale("log")
    ax2.set_ylim(0.6, 1.0)
    ax2.set_xlabel("number of simulated studies (log scale)")
    ax2.set_ylabel("estimated power")
    ax2.legend(loc="upper right", frameon=False)
    panel(ax2, "The estimate settles down", "MC SE = √(p̂(1 − p̂)/B) ≈ 0.004 at B = 10,000")
    note(fig, "A simulation checks the whole plan: data, test, and decision rule together.",
         "It is most useful when the real design is messy (unequal variances, clusters, dropouts, stopping rules).")
    save(fig, "simulated_power")
    return rej.mean(), crit


if __name__ == "__main__":
    print("15.1 se, cutoff, z-power:", power_two_curves())
    effect_size_overlap()
    print("15.3 z-power n=16, n=64:", what_affects_power())
    sample_size_steps()
    print("15.5 simulated power, t cutoff:", simulated_power())
    print("exact t power n=20:", t_power(0.5, 20), " n=63:", t_power(0.5, 63), " n=64:", t_power(0.5, 64))

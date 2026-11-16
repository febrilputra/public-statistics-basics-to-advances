"""Draw every figure for Chapter 17 - ANOVA and ANCOVA.

Run with Python, NumPy, SciPy and Matplotlib installed:
    python 17_anova_and_ancova/figures/make_figures.py
Each figure is written beside this script as a PNG (for the notes) and an SVG.
Data: three packing layouts (ANOVA) and two drying methods with initial moisture (ANCOVA).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
from scipy import stats

OUT = Path(__file__).resolve().parent
BLUE, ORANGE, GREEN, YELLOW, PINK = "#0072B2", "#D55E00", "#009E73", "#E69F00", "#CC79A7"
INK, MUTED, RED, LIGHTRED, GRID, LIGHTBLUE = "#222222", "#555555", "#C0392B", "#E8B4B4", "#E6E6E6", "#BFD3E6"

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


GROUPS = {"A": [4, 5, 6, 5], "B": [6, 7, 8, 7], "C": [8, 9, 10, 9]}
COLORS = {"A": BLUE, "B": ORANGE, "C": GREEN}
GRAND = 7.0
MOIST = np.array([18, 19, 20, 21, 22])
DRY_A = np.array([7, 7, 10, 11, 15])
DRY_B = np.array([2, 6, 7, 10, 10])


def layout_points(ax, sticks, title, sub):
    i = 0
    for g, vals in GROUPS.items():
        m = np.mean(vals)
        for j, v in enumerate(vals):
            x = i
            ax.plot(x, v, "o", color=COLORS[g], ms=10, zorder=4, mec="white")
            if sticks == "total":
                ax.plot([x, x], [GRAND, v], color=RED, lw=1.6)
            elif sticks == "within":
                ax.plot([x, x], [m, v], color=RED, lw=1.6)
            i += 1
        lo, hi = i - 4 - 0.3, i - 1 + 0.3
        if sticks in ("within", "between"):
            ax.plot([lo, hi], [m, m], color=COLORS[g], lw=2.5)
        if sticks == "between":
            ax.plot([i - 2.5, i - 2.5], [GRAND, m], color=RED, lw=3)
            lab = f"{m - GRAND:+.0f}" if m != GRAND else "0"
            ax.text(i - 1 + 0.4, m + (0.35 if m == GRAND else 0), lab, color=RED, fontsize=12.5, fontweight="bold", va="center")
        ax.text(i - 2.5, 3.3, f"layout {g}", ha="center", color=COLORS[g], fontsize=12.5, fontweight="bold")
        i += 1
    ax.axhline(GRAND, color=MUTED, ls="--", lw=1.4)
    ax.text(-0.6, GRAND + 0.15, "grand mean 7", color=MUTED, ha="left", fontsize=11)
    ax.set_xlim(-0.8, 14.3)
    ax.set_ylim(3, 10.8)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.set_ylabel("completion time (minutes)")
    panel(ax, title, sub)


# ---------------------------------------------------------------- 17.1
def anova_sum_of_squares():
    fig, axes = figure("ANOVA splits the total variation into 'between groups' + 'within groups'",
                       "Three packing layouts, 4 times each. Red sticks are the deviations that get squared and added.", 3)
    layout_points(axes[0], "total", "Total: SS_T = 38", "each point vs the grand mean")
    layout_points(axes[1], "between", "Between: SS_B = 32", "4 × (group mean − grand mean)²")
    layout_points(axes[2], "within", "Within: SS_W = 6", "each point vs its own group mean")
    for ax in axes[1:]:
        ax.set_ylabel("")
    for sym, left, right in [("=", axes[0], axes[1]), ("+", axes[1], axes[2])]:
        x = (left.get_position().x1 + right.get_position().x0) / 2
        fig.text(x, 0.5, sym, fontsize=34, fontweight="bold", ha="center", va="center", color=INK)
    note(fig, "SS_T = SS_B + SS_W:  38 = 32 + 6.  F = [SS_B/(g − 1)] ÷ [SS_W/(n_T − g)] = (32/2) ÷ (6/9) = 16 ÷ 0.667 = 24",
         "If the population means were equal, the between part would be about as big as the noise. Here it is 24 times bigger.")
    save(fig, "anova_sum_of_squares")


# ---------------------------------------------------------------- 17.2
def anova_f_test():
    fig, (ax, ax2) = figure("The ANOVA table and the F-test", "g = 3 layouts, n_T = 12 observations in total, α = 0.05", 2, wspace=0.15)
    ax.set_position([0.04, 0.27, 0.42, 0.45])
    ax.axis("off")
    rows = [["source", "SS", "df", "MS = SS/df", "F"],
            ["between layouts", "32", "g − 1 = 2", "16", "16 / 0.667 = 24"],
            ["within layouts", "6", "n_T − g = 9", "0.667", ""],
            ["total", "38", "n_T − 1 = 11", "", ""]]
    widths = [0.27, 0.1, 0.2, 0.18, 0.25]
    for i, row in enumerate(rows):
        x = 0
        for cell, w in zip(row, widths):
            ax.text(x + w / 2, 0.85 - i * 0.2, cell, ha="center", va="center", fontsize=13,
                    fontweight="bold" if i == 0 or (i == 1 and cell.endswith("24")) else "normal",
                    color=BLUE if i == 0 else (RED if cell.endswith("24") else INK), transform=ax.transAxes)
            x += w
        if i in (0, 2):
            ax.plot([0, 1], [0.85 - i * 0.2 - 0.1] * 2, color=MUTED, lw=1, transform=ax.transAxes)
    ax.text(0.5, 1.06, "One-way ANOVA table", transform=ax.transAxes, ha="center", fontsize=15, fontweight="bold")
    ax.text(0.0, 0.0, "η² = SS_B / SS_T = 32/38 = 0.842\nω² = (SS_B − (g − 1)·MS_W) / (SS_T + MS_W) = 0.793",
            transform=ax.transAxes, fontsize=12.5, color=GREEN, fontweight="bold", va="top")

    f = np.linspace(0.01, 27, 800)
    dens = stats.f.pdf(f, 2, 9)
    crit = stats.f.isf(0.05, 2, 9)
    ax2.plot(f, dens, color=BLUE, lw=2.5)
    ax2.fill_between(f, dens, where=f >= crit, color=LIGHTRED)
    ax2.axvline(crit, color=MUTED, ls="--")
    ax2.text(crit + 0.3, 0.6, f"critical value\nF(0.05; 2, 9) = {crit:.2f}", color=MUTED, fontsize=11.5)
    ax2.annotate(f"observed F = 24\np = {stats.f.sf(24, 2, 9):.6f}", xy=(24, 0.003), xytext=(17.5, 0.35), color=RED,
                 fontsize=13, fontweight="bold", arrowprops=dict(arrowstyle="->", color=RED, lw=1.6))
    ax2.set_xlim(0, 27)
    ax2.set_ylim(0, 1.02)
    ax2.set_xlabel("F")
    ax2.set_ylabel("density of F(2, 9)")
    ax2.set_position([0.54, 0.25, 0.44, 0.5])
    panel(ax2, "Compare F with the F(2, 9) distribution", "right-tailed: big F → reject 'all means equal'")
    note(fig, "F = 24 ≫ 4.26, p ≈ 0.00025: reject H₀. At least one layout's mean time differs from the others.",
         "ANOVA says SOME means differ, not which ones. Lesson 17.3 finds out which.")
    save(fig, "anova_f_test")
    return crit


# ---------------------------------------------------------------- 17.3
def pairwise_comparisons():
    fig, (ax, ax2) = figure("After ANOVA: which layouts differ?", "Pairwise differences with 95% intervals; an interval that misses 0 → a real difference",
                            2, wspace=0.28)
    for i, (g, vals) in enumerate(GROUPS.items()):
        ax.plot(np.full(4, i) + np.array([-0.08, -0.03, 0.03, 0.08]), vals, "o", color=COLORS[g], ms=10, mec="white")
        ax.plot([i - 0.25, i + 0.25], [np.mean(vals)] * 2, color=COLORS[g], lw=3)
        ax.text(i + 0.3, np.mean(vals), f"mean {np.mean(vals):.0f}", va="center", color=COLORS[g], fontweight="bold")
    ax.set_xticks([0, 1, 2], ["layout A", "layout B", "layout C"])
    ax.set_xlim(-0.5, 2.8)
    ax.set_ylabel("completion time (minutes)")
    panel(ax, "Group means", "MS_W = 0.667 is the shared noise variance")

    msw, n, df = 2 / 3, 4, 9
    se = np.sqrt(msw * (1 / n + 1 / n))
    q = stats.studentized_range.ppf(0.95, 3, df)
    hsd = q * np.sqrt(msw / n)
    tcrit = stats.t.ppf(0.975, df)
    pairs = [("B − A", 2), ("C − A", 4), ("C − B", 2)]
    for i, (lab, d) in enumerate(pairs):
        y = 2 - i
        ax2.plot([d - hsd, d + hsd], [y + 0.12] * 2, color=BLUE, lw=4, solid_capstyle="butt")
        ax2.plot([d - tcrit * se, d + tcrit * se], [y - 0.12] * 2, color=MUTED, lw=4, solid_capstyle="butt", alpha=0.6)
        ax2.plot(d, y, "D", color=INK, ms=8)
        ax2.text(d + hsd + 0.15, y + 0.12, f"Tukey [{d - hsd:.2f}, {d + hsd:.2f}]", va="center", color=BLUE, fontsize=11.5)
        ax2.text(d + hsd + 0.15, y - 0.16, f"unadjusted [{d - tcrit * se:.2f}, {d + tcrit * se:.2f}]", va="center", color=MUTED, fontsize=11)
    ax2.axvline(0, color=RED, lw=1.5)
    ax2.text(0.05, 2.55, "0 = no difference", color=RED, fontsize=11.5)
    ax2.set_yticks([2, 1, 0], [p[0] for p in pairs], fontsize=13)
    ax2.set_xlim(-0.8, 9.2)
    ax2.set_ylim(-0.6, 2.8)
    ax2.set_xlabel("difference in mean time (minutes)")
    panel(ax2, "Tukey HSD vs unadjusted intervals", f"Tukey half-width = q·√(MS_W/n) = {q:.3f} × {np.sqrt(msw / n):.3f} = {hsd:.2f}")
    note(fig, "Tukey's intervals are wider so that ALL three hold together with 95% confidence. Here every interval misses 0.",
         f"Pairwise SE = √(MS_W(1/4 + 1/4)) = {se:.3f}, using the full-ANOVA df = 9 rather than each pair's own variance.")
    save(fig, "pairwise_comparisons")
    return se, q, hsd, tcrit


# ---------------------------------------------------------------- 17.4
def ancova_adjustment():
    fig, axes = figure("ANCOVA: compare the methods at the same starting moisture",
                       "Drying time for two methods, 5 batches each, initial moisture 18–22%", 3)
    ax = axes[0]
    for i, (vals, c, lab) in enumerate([(DRY_A, BLUE, "method A"), (DRY_B, ORANGE, "method B")]):
        ax.plot(np.full(5, i) + np.linspace(-0.12, 0.12, 5), vals, "o", color=c, ms=10, mec="white")
        ax.plot([i - 0.25, i + 0.25], [vals.mean()] * 2, color=c, lw=3)
        ax.text(i + 0.3, vals.mean(), f"mean {vals.mean():.0f}", va="center", color=c, fontweight="bold")
    ax.set_xticks([0, 1], ["method A", "method B"])
    ax.set_xlim(-0.5, 1.8)
    ax.set_ylim(0, 17)
    ax.set_ylabel("drying time (minutes)")
    ax.text(0.5, 0.97, "B − A = −3, p = 0.19\n95% CI [−7.84, 1.84]", transform=ax.transAxes, ha="center", va="top",
            color=RED, fontsize=12.5, fontweight="bold")
    panel(ax, "A  |  Ignoring moisture", "lots of scatter within each method")

    ax = axes[1]
    xs = np.linspace(17.6, 22.4, 2)
    for vals, c, b0, lab in [(DRY_A, BLUE, 10, "A: ŷ = 10 + 2x"), (DRY_B, ORANGE, 7, "B: ŷ = 7 + 2x")]:
        ax.plot(MOIST, vals, "o", color=c, ms=10, mec="white", zorder=4)
        ax.plot(xs, b0 + 2 * (xs - 20), color=c, lw=2.5, label=lab)
        for m, v in zip(MOIST, vals):
            ax.plot([m, m], [v, b0 + 2 * (m - 20)], color=RED, lw=1.2, ls=":")
    ax.annotate("", xy=(20, 7), xytext=(20, 10), arrowprops=dict(arrowstyle="<->", color=GREEN, lw=2))
    ax.text(20.1, 8.5, "τ = −3", color=GREEN, fontsize=14, fontweight="bold", va="center")
    ax.set_xlabel("initial moisture (%), centred at 20: x = moisture − 20")
    ax.set_ylim(0, 17)
    ax.legend(loc="upper left", frameon=False)
    ax.text(0.97, 0.04, "B − A = −3, p = 0.003\n95% CI [−4.60, −1.40]", transform=ax.transAxes, ha="right", color=GREEN,
            fontsize=12.5, fontweight="bold")
    panel(ax, "B  |  Adjusting for moisture", "parallel lines, common slope 2 min per %")

    ax = axes[2]
    vals = [88, 30.5, 8]
    labs = ["method only", "moisture only", "moisture +\nmethod"]
    ax.bar(range(3), vals, color=[MUTED, BLUE, GREEN], width=0.6)
    for i, v in enumerate(vals):
        ax.text(i, v + 2, f"{v:g}", ha="center", fontsize=14, fontweight="bold")
    ax.set_xticks(range(3), labs)
    ax.set_ylabel("sum of squared errors (SSE)")
    ax.set_ylim(0, 100)
    panel(ax, "C  |  Leftover noise (SSE)", "the covariate soaks up most of the scatter")
    note(fig, "The estimated difference is −3 minutes both ways, but adjusting for moisture shrinks the noise, so the SE and interval shrink.",
         "Partial F for method = [(30.5 − 8)/1] ÷ (8/7) = 19.69, df (1, 7), p = 0.003. Partial R² = 22.5/30.5 = 0.74.")
    save(fig, "ancova_adjustment")


# ---------------------------------------------------------------- 17.5
def ancova_assumptions():
    fig, axes = figure("ANCOVA checks: parallel slopes, overlap, and the right covariate",
                       "The adjusted comparison is only as good as these three things", 3)
    ax = axes[0]
    x = np.linspace(0, 10, 2)
    ax.plot(x, 12 + 0.5 * x, color=BLUE, lw=2.5, label="A: 12 + 0.5x")
    ax.plot(x, 10 + 0.8 * x, color=ORANGE, lw=2.5, label="B: 10 + 0.8x")
    for xv in [0, 20 / 3, 10]:
        a, b = 12 + 0.5 * xv, 10 + 0.8 * xv
        if abs(a - b) > 0.05:
            ax.annotate("", xy=(xv, b), xytext=(xv, a), arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.6))
        ax.text(xv + 0.15, (a + b) / 2 + (0.6 if abs(a - b) < 0.05 else 0), f"{b - a:+.1f}" if abs(a - b) > 0.05 else "0 at x = 6.67",
                color=GREEN, fontsize=12.5, fontweight="bold", va="center")
    ax.set_xlabel("covariate x")
    ax.set_ylabel("ŷ")
    ax.legend(loc="upper left", frameon=False)
    panel(ax, "A  |  Interaction: slopes differ", "B − A = −2 + 0.3x changes sign")

    ax = axes[1]
    rng = np.random.default_rng(5)
    xa, xb = rng.uniform(14, 18, 8), rng.uniform(22, 26, 8)
    ya, yb = 10 + 2 * (xa - 20) + rng.normal(0, 0.8, 8), 7 + 2 * (xb - 20) + rng.normal(0, 0.8, 8)
    ax.axvspan(18.2, 21.8, color=YELLOW, alpha=0.18)
    ax.text(20, 22, "no data here:\ncomparison at\nx = 20 is\nextrapolation", ha="center", va="top", fontsize=11.5, color=INK)
    ax.plot(xa, ya, "o", color=BLUE, ms=9, mec="white")
    ax.plot(xb, yb, "s", color=ORANGE, ms=9, mec="white")
    xs = np.linspace(13.5, 26.5, 2)
    ax.plot(xs, 10 + 2 * (xs - 20), color=BLUE, lw=2, ls="--")
    ax.plot(xs, 7 + 2 * (xs - 20), color=ORANGE, lw=2, ls="--")
    ax.set_xlabel("initial moisture (%)")
    ax.set_ylabel("drying time")
    panel(ax, "B  |  No overlap", "all A batches dry, all B batches wet")

    ax = axes[2]
    ax.axis("off")
    boxes = {"method": (0.18, 0.92), "baseline\nmoisture": (0.18, 0.5), "drying\ntime": (0.82, 0.7),
             "moisture after\n1 hour": (0.5, 0.3)}
    for lab, (bx, by) in boxes.items():
        col = RED if "after" in lab else (GREEN if "baseline" in lab else INK)
        ax.text(bx, by, lab, ha="center", va="center", fontsize=12.5, fontweight="bold", transform=ax.transAxes,
                bbox=dict(boxstyle="round,pad=0.5", fc="white", ec=col, lw=1.8))
    arrows = [((0.3, 0.9), (0.7, 0.75), INK), ((0.3, 0.53), (0.7, 0.66), GREEN), ((0.2, 0.84), (0.42, 0.37), RED),
              ((0.6, 0.36), (0.78, 0.6), RED)]
    for (x0, y0), (x1, y1), c in arrows:
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0), xycoords="axes fraction", arrowprops=dict(arrowstyle="->", color=c, lw=2))
    ax.text(0.0, 0.14, "✓ adjust for baseline moisture (before treatment)\n✗ don't adjust for moisture AFTER treatment:\n    it is part of how the method works",
            transform=ax.transAxes, ha="left", va="top", fontsize=11.5)
    panel(ax, "C  |  Pick the right covariate", "measured before the treatment starts")
    note(fig, "Check that slopes are (roughly) parallel, that the groups overlap on the covariate, and that the covariate isn't caused by the treatment.",
         "If slopes differ, report the group difference at several covariate values instead of one 'adjusted effect'.")
    save(fig, "ancova_assumptions")


if __name__ == "__main__":
    anova_sum_of_squares()
    print("F critical (2, 9):", anova_f_test())
    print("pairwise se, q, hsd, tcrit:", pairwise_comparisons())
    ancova_adjustment()
    ancova_assumptions()

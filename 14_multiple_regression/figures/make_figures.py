"""Draw every figure for Chapter 14 - Multiple Regression.

Run with Python, NumPy, SciPy and Matplotlib installed:
    python 14_multiple_regression/figures/make_figures.py
Each figure is written beside this script as a PNG (for the notes) and an SVG.
All data are small, made-up teaching examples; random ones use fixed seeds.
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


def text_table(ax, rows, x0, y0, widths, dy=0.085, header_color=BLUE, size=12.5, colors=None):
    """Draw a small table as text in axes coordinates; the first row is the header."""
    for i, row in enumerate(rows):
        x = x0
        for j, (cell, w) in enumerate(zip(row, widths)):
            c = colors[i][j] if colors else (header_color if i == 0 else INK)
            ax.text(x + w / 2, y0 - i * dy, cell, transform=ax.transAxes, ha="center", va="center",
                    fontsize=size, color=c, fontweight="bold" if i == 0 else "normal")
            x += w
        if i == 0:
            ax.plot([x0, x], [y0 - dy / 2] * 2, transform=ax.transAxes, color=MUTED, lw=1)


# The workshop batches used throughout the chapter.
SIZE = np.array([4, 4, 4, 4, 6, 6, 6, 6])
X = SIZE - 5                       # batch size centred at 5 items
Z = np.array([0, 0, 1, 1, 0, 0, 1, 1])  # 1 = coated
Y = np.array([7, 9, 10, 12, 11, 13, 14, 16])


# ---------------------------------------------------------------- 14.1
def multiple_regression_idea():
    fig = plt.figure(figsize=(15, 7.4))
    fig.text(0.5, 0.955, "From one predictor to several", ha="center", va="center", fontsize=22, fontweight="bold")
    fig.text(0.5, 0.905, "Multiple regression uses the same least squares idea as Lesson 13.1, with more columns of x.",
             ha="center", va="center", fontsize=13.5, color=MUTED)
    rng = np.random.default_rng(14)

    ax = fig.add_axes([0.05, 0.27, 0.26, 0.47])
    size = rng.integers(2, 9, 30)
    exp_years = rng.uniform(0, 10, 30)
    time = 14 + 2 * (size - 5) - 0.5 * exp_years + rng.normal(0, 1.2, 30)
    b, a = np.polyfit(size, time, 1)
    ax.scatter(size, time, color=BLUE, s=40, zorder=3, edgecolor="white", lw=0.8)
    xs = np.linspace(1.5, 8.5, 2)
    ax.plot(xs, a + b * xs, color=ORANGE, lw=2.5)
    ax.set_xlabel("batch size (items)")
    ax.set_ylabel("preparation time (minutes)")
    ax.text(0.04, 0.93, f"ŷ = {a:.1f} + {b:.2f}·size", transform=ax.transAxes, color=ORANGE,
            fontsize=12.5, fontweight="bold")
    panel(ax, "1 predictor: a line", "Chapter 13: ŷ = mx + b")

    ax = fig.add_axes([0.35, 0.22, 0.3, 0.56], projection="3d")
    gx, gy = np.meshgrid(np.linspace(2, 8, 12), np.linspace(0, 10, 12))
    coef, *_ = np.linalg.lstsq(np.c_[np.ones(30), size, exp_years], time, rcond=None)
    plane = coef[0] + coef[1] * gx + coef[2] * gy
    ax.plot_surface(gx, gy, plane, color=ORANGE, alpha=0.25, edgecolor=ORANGE, lw=0.3)
    fitted = coef[0] + coef[1] * size + coef[2] * exp_years
    for s, e, t, f in zip(size, exp_years, time, fitted):
        ax.plot([s, s], [e, e], [t, f], color=RED, lw=0.9)
    ax.scatter(size, exp_years, time, color=BLUE, s=28, depthshade=False)
    ax.set_xlabel("batch size", labelpad=6)
    ax.set_ylabel("staff experience (years)", labelpad=8)
    ax.set_zlabel("time", labelpad=4)
    ax.view_init(elev=18, azim=-58)
    ax.set_box_aspect(None, zoom=0.88)
    fig.text(0.5, 0.86, "2 predictors: a plane", ha="center", fontsize=15, fontweight="bold")
    fig.text(0.5, 0.815, f"ŷ = {coef[0]:.1f} + {coef[1]:.2f}·size − {-coef[2]:.2f}·experience",
             ha="center", fontsize=12, color=MUTED)

    ax = fig.add_axes([0.68, 0.27, 0.3, 0.47])
    ax.axis("off")
    rows = [["y", "1", "x₁", "x₂"]] + [[f"{t:.1f}", "1", f"{s}", f"{e:.1f}"] for t, s, e in zip(time[:6], size[:6], exp_years[:6])] + [["⋮", "⋮", "⋮", "⋮"]]
    text_table(ax, rows, 0.05, 0.93, [0.24, 0.16, 0.2, 0.24], dy=0.105)
    ax.add_patch(FancyBboxPatch((0.29, 0.0), 0.6, 0.99, boxstyle="round,pad=0,rounding_size=0.02",
                                transform=ax.transAxes, fill=False, ec=ORANGE, lw=1.6, ls="--"))
    ax.text(0.59, -0.08, "design matrix X: K = 3 columns → 3 coefficients", transform=ax.transAxes,
            ha="center", color=ORANGE, fontsize=12, fontweight="bold")
    fig.text(0.83, 0.86, "What the computer sees", ha="center", fontsize=15, fontweight="bold")
    fig.text(0.83, 0.815, "a column of 1s for the intercept + one column per predictor", ha="center", fontsize=12, color=MUTED)

    note(fig, "Each slope is the change in ŷ when that predictor goes up by 1 and the others stay fixed.",
         "Least squares picks b₀, b₁, b₂ to make SSE = Σ(y − ŷ)² as small as possible. The red sticks are the residuals.")
    save(fig, "multiple_regression_idea")


# ---------------------------------------------------------------- 14.2
def dummy_variables():
    fig, (ax, ax2) = figure("A 0/1 dummy variable gives two parallel lines",
                            "Workshop data: time = 10 + 2·(size − 5) + 3·coated. Same slope, different heights.",
                            2, size=(15, 7.4), wspace=0.18)
    fig.axes[1].set_position([0.58, 0.25, 0.4, 0.51])
    for z, c, m, lab in [(0, BLUE, "o", "uncoated (z = 0)"), (1, ORANGE, "s", "coated (z = 1)")]:
        sel = Z == z
        ax.scatter(SIZE[sel] + (0.06 if z else -0.06), Y[sel], color=c, marker=m, s=70, zorder=4,
                   edgecolor="white", lw=1, label=lab)
        xs = np.array([3.6, 6.4])
        ax.plot(xs, 10 + 2 * (xs - 5) + 3 * z, color=c, lw=2.5)
        for s, y in zip(SIZE[sel], Y[sel]):
            f = 10 + 2 * (s - 5) + 3 * z
            ax.plot([s + (0.06 if z else -0.06)] * 2, [y, f], color=RED, lw=1.2, ls=":")
    ax.annotate("", xy=(5, 13), xytext=(5, 10), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.6))
    ax.text(5.1, 11.5, "b₂ = 3 minutes\n(coated − uncoated,\nsame size)", va="center", fontsize=11.5,
            bbox=dict(fc="white", ec="none", alpha=0.9, pad=1), zorder=6)
    ax.plot([4.2, 5.2, 5.2], [8.4, 8.4, 10.4], color=GREEN, lw=1.8)
    ax.text(4.7, 7.5, "+1 item → +2 min (b₁ = 2)", color=GREEN, ha="center", fontsize=11.5, fontweight="bold")
    ax.plot(5, 10, "o", color=INK, ms=6)
    ax.text(5.06, 9.3, "b₀ = 10", ha="left", fontsize=11.5,
            bbox=dict(fc="white", ec="none", alpha=0.9, pad=1), zorder=6)
    ax.set_xlim(3.5, 6.5)
    ax.set_ylim(5, 17.5)
    ax.set_xticks([4, 5, 6])
    ax.set_xlabel("batch size (items); centred x = size − 5")
    ax.set_ylabel("preparation time (minutes)")
    ax.legend(loc="upper left", frameon=False)
    panel(ax, "The fitted model", "dotted red = residuals, all ±1 minute")

    ax2.axis("off")
    ax2.text(0.0, 0.97, "Put a category into a model", fontsize=15, fontweight="bold", transform=ax2.transAxes)
    rows = [["coating", "z", "the equation becomes"], ["uncoated", "0", "ŷ = 10 + 2x"], ["coated", "1", "ŷ = 10 + 2x + 3 = 13 + 2x"]]
    text_table(ax2, rows, 0.0, 0.84, [0.25, 0.12, 0.6], dy=0.09)
    ax2.text(0.0, 0.48, "3 categories → 2 dummies (the reference gets 0, 0)", fontsize=15, fontweight="bold", transform=ax2.transAxes)
    rows = [["finish", "d_matte", "d_gloss"], ["none (reference)", "0", "0"], ["matte", "1", "0"], ["gloss", "0", "1"]]
    text_table(ax2, rows, 0.0, 0.36, [0.35, 0.22, 0.22], dy=0.085)
    ax2.text(0.0, -0.02, "A 3rd dummy for 'none' would equal 1 − d_matte − d_gloss:\nthe dummy variable trap.",
             fontsize=12, color=RED, transform=ax2.transAxes)
    note(fig, "Residuals: 7 − 8 = −1, 9 − 8 = +1, ... every miss is ±1, so SSE = 8 and s² = SSE/(n − K) = 8/(8 − 3) = 1.6.",
         "With g categories use g − 1 dummies. Changing the reference group changes the labels, not the predictions.")
    save(fig, "dummy_variable_parallel_lines")


# ---------------------------------------------------------------- 14.3
def confounding_and_interaction():
    fig, axes = figure("“Holding the others fixed” and interactions",
                       "Leaving out a related predictor can bend a slope; an interaction lets a slope differ by group.", 3)
    ax = axes[0]
    xu, yu = np.array([-2, -1, 0]), np.array([6, 8, 10])
    xc, yc = np.array([0, 1, 2]), np.array([13, 15, 17])
    allx, ally = np.r_[xu, xc], np.r_[yu, yc]
    m, b = np.polyfit(allx, ally, 1)
    xs = np.linspace(-2.4, 2.4, 2)
    ax.plot(xs, b + m * xs, color=MUTED, lw=2.2, ls="--")
    ax.plot(xs, 10 + 2 * xs, color=BLUE, lw=2.2)
    ax.plot(xs, 13 + 2 * xs, color=ORANGE, lw=2.2)
    ax.scatter(xu, yu, color=BLUE, s=70, zorder=4, edgecolor="white")
    ax.scatter(xc, yc, color=ORANGE, marker="s", s=70, zorder=4, edgecolor="white")
    ax.text(-2.3, 17.5, f"ignore coating: slope {m:.1f}", color=MUTED, fontsize=12, fontweight="bold")
    ax.text(-2.3, 16.3, "within each group: slope 2", color=INK, fontsize=12, fontweight="bold")
    ax.set_xlabel("centred batch size x")
    ax.set_ylabel("time (minutes)")
    ax.set_ylim(4, 19)
    panel(ax, "A  |  Leaving out coating", "big batches here are mostly coated")

    for ax, inter, title, sub in [(axes[1], 0, "B  |  No interaction", "ŷ = 10 + 2x + 3z: parallel lines"),
                                  (axes[2], 1, "C  |  Interaction", "ŷ = 10 + 2x + 3z + 1·xz: slopes 2 and 3")]:
        xs = np.linspace(-1.3, 1.3, 2)
        ax.plot(xs, 10 + 2 * xs, color=BLUE, lw=2.5, label="uncoated, z = 0")
        ax.plot(xs, 13 + (2 + inter) * xs, color=ORANGE, lw=2.5, label="coated, z = 1")
        for x in [-1, 0, 1]:
            lo, hi = 10 + 2 * x, 13 + (2 + inter) * x
            ax.annotate("", xy=(x, hi), xytext=(x, lo), arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.5))
            ax.text(x + 0.06, (lo + hi) / 2, f"{hi - lo:g}", color=GREEN, fontsize=13, fontweight="bold", va="center")
        ax.set_ylim(6, 18)
        ax.set_xticks([-1, 0, 1])
        ax.set_xlabel("centred batch size x")
        ax.legend(loc="upper left", frameon=False, fontsize=11)
        panel(ax, title, sub)
    axes[1].text(0.97, 0.06, "gap = 3 everywhere", transform=axes[1].transAxes, ha="right", color=GREEN, fontweight="bold")
    axes[2].text(0.97, 0.06, "gap = 3 + 1·x  (2, 3, 4)", transform=axes[2].transAxes, ha="right", color=GREEN, fontweight="bold")
    note(fig, "A coefficient is a comparison inside the model: change one predictor, keep the others where they are.",
         "With an interaction there is no single 'coating effect'. The gap depends on x, so report it at chosen x values.")
    save(fig, "confounding_and_interaction")
    return m


# ---------------------------------------------------------------- 14.4
def nested_models():
    fig, (ax, ax2) = figure("Does adding coating really help? The partial F-test",
                            "Compare the SSE of two nested models fitted to the same 8 batches.", 2, wspace=0.25)
    rss = [58, 26, 8]
    labels = ["mean only\nŷ = 11.5", "+ batch size\nŷ = 11.5 + 2x", "+ coating\nŷ = 10 + 2x + 3z"]
    colors = [MUTED, BLUE, ORANGE]
    ax.bar(range(3), rss, color=colors, width=0.6)
    for i, r in enumerate(rss):
        ax.text(i, r + 1.2, f"SSE = {r}", ha="center", fontsize=13, fontweight="bold")
    for i, drop in [(0.5, 32), (1.5, 18)]:
        ax.annotate("", xy=(i + 0.5 - 0.32, rss[int(i + 0.5)] + 0.3), xytext=(i - 0.5 + 0.32, rss[int(i - 0.5)] - 0.3),
                    arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.8))
        ax.text(i + 0.02, (rss[int(i - 0.5)] + rss[int(i + 0.5)]) / 2 + 3, f"−{drop}", color=GREEN, fontsize=14,
                fontweight="bold", ha="center")
    ax.set_xticks(range(3), labels, fontsize=11.5)
    ax.set_ylabel("sum of squared errors (SSE)")
    ax.set_ylim(0, 66)
    panel(ax, "Each added term lowers SSE", "reduced model: K = 2 · full model: K = 3")

    f = np.linspace(0.01, 14, 600)
    dens = stats.f.pdf(f, 1, 5)
    crit = stats.f.isf(0.05, 1, 5)
    p = stats.f.sf(11.25, 1, 5)
    ax2.plot(f, dens, color=BLUE, lw=2.5)
    ax2.fill_between(f, dens, where=f >= crit, color=LIGHTRED, alpha=0.8)
    ax2.fill_between(f, dens, where=f >= 11.25, color=RED, alpha=0.9)
    ax2.axvline(crit, color=MUTED, lw=1.2, ls="--")
    ax2.text(crit - 0.15, 0.7, f"critical F = {crit:.2f}\n(α = 0.05)", color=MUTED, fontsize=11.5, ha="right")
    ax2.annotate(f"observed F = 11.25\np-value = {p:.3f}", xy=(11.25, 0.004), xytext=(9.3, 0.13),
                 arrowprops=dict(arrowstyle="->", color=RED, lw=1.5), color=RED, fontsize=12.5, fontweight="bold")
    ax2.set_ylim(0, 0.8)
    ax2.set_xlim(0, 14)
    ins = ax2.inset_axes([0.45, 0.45, 0.5, 0.32])
    ins.plot(f, dens, color=BLUE, lw=2)
    ins.fill_between(f, dens, where=f >= crit, color=LIGHTRED)
    ins.fill_between(f, dens, where=f >= 11.25, color=RED)
    ins.set_xlim(5, 14)
    ins.set_ylim(0, 0.03)
    ins.set_yticks([0, 0.01, 0.02, 0.03])
    ins.tick_params(labelsize=9)
    ins.set_title("zoom on the right tail", fontsize=10.5, color=MUTED)
    ins.text(12.6, 0.009, "p = 0.020", color=RED, fontsize=10.5, fontweight="bold", ha="center")
    ins.text(7.8, 0.018, "pink + red = 5%", color=MUTED, fontsize=10, ha="center")
    ax2.set_xlabel("F")
    ax2.set_ylabel("density")
    panel(ax2, "Compare F with F(1, 5)", "df = (K_F − K_R, n − K_F) = (1, 5); right tail only")
    note(fig, "F = [(SSE_R − SSE_F)/(K_F − K_R)] ÷ [SSE_F/(n − K_F)] = (18/1) ÷ (8/5) = 11.25",
         "Numerator: improvement per added coefficient. Denominator: leftover noise. F far above 1 → the new term helps.")
    save(fig, "nested_models_f_test")
    return crit, p


# ---------------------------------------------------------------- 14.5
def r_squared_and_overfitting():
    fig, (ax, ax2) = figure("R² always goes up when you add predictors, but predictions may get worse",
                            "Left: the batch model. Right: a simulation where only 2 of 30 predictors are real.", 2, wspace=0.25)
    ax.barh([1], [50], color=ORANGE, height=0.5)
    ax.barh([1], [8], left=[50], color=LIGHTRED, height=0.5)
    ax.barh([0], [58], color=MUTED, height=0.5)
    ax.text(29, 0, "TSS = Σ(y − ȳ)² = 58", color="white", ha="center", va="center", fontsize=13, fontweight="bold")
    ax.text(25, 1, "explained: 58 − 8 = 50", color="white", ha="center", va="center", fontsize=13, fontweight="bold")
    ax.text(54, 1, "SSE\n8", ha="center", va="center", fontsize=12, fontweight="bold", color=RED)
    ax.set_yticks([0, 1], ["total", "model"])
    ax.set_xlim(0, 60)
    ax.set_xlabel("sum of squares")
    ax.text(0, -0.75, "R² = 1 − 8/58 = 0.862", fontsize=14, fontweight="bold", color=ORANGE)
    ax.text(0, -1.15, "adjusted R² = 1 − (8/5)/(58/7) = 0.807", fontsize=14, fontweight="bold", color=BLUE)
    ax.set_ylim(-1.35, 1.5)
    panel(ax, "R² = share of variation explained", "n = 8 batches, K = 3 coefficients")

    rng = np.random.default_rng(707)
    train_x, test_x = rng.normal(size=(40, 30)), rng.normal(size=(3000, 30))
    train_y = 4 + 2 * train_x[:, 0] - train_x[:, 1] + rng.normal(size=40)
    test_y = 4 + 2 * test_x[:, 0] - test_x[:, 1] + rng.normal(size=3000)
    ks = np.arange(2, 31)
    tr, te, r2, ar2 = [], [], [], []
    for k in ks:
        A = np.c_[np.ones(40), train_x[:, :k]]
        coef, *_ = np.linalg.lstsq(A, train_y, rcond=None)
        res = train_y - A @ coef
        tr.append(np.sqrt(np.mean(res ** 2)))
        te.append(np.sqrt(np.mean((test_y - np.c_[np.ones(3000), test_x[:, :k]] @ coef) ** 2)))
        tss = np.sum((train_y - train_y.mean()) ** 2)
        r2.append(1 - res @ res / tss)
        ar2.append(1 - (res @ res / (40 - k - 1)) / (tss / 39))
    ax2.plot(ks, tr, "o-", color=BLUE, ms=4, lw=2.2, label="error on the 40 training rows")
    ax2.plot(ks, te, "s-", color=ORANGE, ms=4, lw=2.2, label="error on 3,000 new rows")
    ax2.axvline(2, color=GREEN, ls="--", lw=1.5)
    ax2.text(2.5, 0.35, "the 2 real\npredictors", color=GREEN, fontsize=11.5)
    ax2.set_xlabel("number of predictors in the model (28 of them pure noise)")
    ax2.set_ylabel("root mean squared error (minutes)")
    ax2.set_ylim(0, 2.0)
    ax2.legend(loc="upper left", frameon=False)
    panel(ax2, "Overfitting", "training error falls, error on new data rises")
    note(fig, "R² can never go down when a predictor is added, even pure noise. Adjusted R² charges for each extra coefficient.",
         "To know how well a model predicts, test it on data it has not seen.")
    save(fig, "r_squared_and_overfitting")
    return [(k, a, b, c, d) for k, a, b, c, d in zip(ks, tr, te, r2, ar2) if k in (2, 5, 10, 20, 30)]


# ---------------------------------------------------------------- 14.6
def multicollinearity():
    fig, axes = figure("Multicollinearity: when two predictors carry the same information",
                       "The fit can be good while the separate slopes are very unstable.", 3)
    rng = np.random.default_rng(66)
    n = 30
    x1 = rng.normal(size=n)
    x2 = 0.98 * x1 + np.sqrt(1 - 0.98 ** 2) * rng.normal(size=n)
    ax = axes[0]
    ax.scatter(x1, x2, color=BLUE, s=40, edgecolor="white")
    r = np.corrcoef(x1, x2)[0, 1]
    ax.text(0.04, 0.92, f"r = {r:.2f}", transform=ax.transAxes, fontsize=14, fontweight="bold", color=BLUE)
    ax.set_xlabel("x₁ (e.g. weight in kg)")
    ax.set_ylabel("x₂ (e.g. a second weight measurement)")
    panel(ax, "A  |  Two predictors move together", "few points where one changes and the other doesn't")

    ax = axes[1]
    for rho, c, lab in [(0.98, RED, "x₁, x₂ with r = 0.98"), (0.0, GREEN, "x₁, x₂ unrelated")]:
        est = []
        for _ in range(400):
            a = rng.normal(size=n)
            bb = rho * a + np.sqrt(1 - rho ** 2) * rng.normal(size=n)
            y = 1 * a + 1 * bb + rng.normal(size=n)
            coef, *_ = np.linalg.lstsq(np.c_[np.ones(n), a, bb], y, rcond=None)
            est.append(coef[1:])
        est = np.array(est)
        ax.scatter(est[:, 0], est[:, 1], s=8, color=c, alpha=0.5, label=lab)
    ax.plot(1, 1, "*", color=INK, ms=16, zorder=5)
    ax.text(1.4, 1.7, "true slopes (1, 1)", fontsize=11.5, bbox=dict(fc="white", ec="none", alpha=0.85, pad=1))
    ax.set_xlabel("estimated slope b₁")
    ax.set_ylabel("estimated slope b₂")
    ax.legend(loc="lower left", frameon=False, fontsize=11, markerscale=2.5)
    panel(ax, "B  |  400 repeated samples", "red: b₁ + b₂ stays ≈ 2, but each slope swings")

    ax = axes[2]
    r2 = np.linspace(0, 0.97, 300)
    ax.plot(r2, 1 / (1 - r2), color=BLUE, lw=2.5)
    for v in [0.5, 0.8, 0.9]:
        vif = 1 / (1 - v)
        ax.plot(v, vif, "o", color=ORANGE, ms=8)
        ax.text(v - 0.03, vif + 2, f"R²ⱼ = {v} → VIF = {vif:.0f}", ha="right", fontsize=11.5)
    ax.set_xlabel("R²ⱼ: how well the other predictors predict xⱼ")
    ax.set_ylabel("VIF = 1 / (1 − R²ⱼ)")
    ax.set_ylim(0, 35)
    panel(ax, "C  |  Variance inflation factor", "SE of bⱼ is multiplied by √VIF")
    note(fig, "Perfect duplicates (Celsius and Fahrenheit, kg and g) make the coefficients impossible to separate.",
         "Near duplicates make them unstable. A high VIF is a warning to think, not an automatic order to delete a predictor.")
    save(fig, "multicollinearity_vif")


if __name__ == "__main__":
    multiple_regression_idea()
    dummy_variables()
    print("pooled slope when coating is left out:", confounding_and_interaction())
    print("critical F and p:", nested_models())
    for row in r_squared_and_overfitting():
        print("k=%d train RMSE %.3f test RMSE %.3f R2 %.3f adjR2 %.3f" % row)
    multicollinearity()

"""Draw every figure for Chapter 18 - Mathematical and Python Prerequisites.

Run with Python, NumPy, SciPy and Matplotlib installed:
    python 18_prerequisites/figures/make_figures.py
Each figure is written beside this script as a PNG (for the notes) and an SVG.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle
from scipy import stats

OUT = Path(__file__).resolve().parent
BLUE, ORANGE, GREEN, YELLOW, PINK = "#0072B2", "#D55E00", "#009E73", "#E69F00", "#CC79A7"
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


# ---------------------------------------------------------------- 18.1
def sums_and_logs():
    fig, axes = figure("Reading Σ, squares and logs correctly", "x = (1, 2, 4): where the parentheses go changes the answer", 3)
    ax = axes[0]
    x0 = 0
    for v, c in zip([1, 2, 4], [BLUE, ORANGE, GREEN]):
        ax.add_patch(Rectangle((x0, 0), v, v, fc=c, alpha=0.75, ec="white"))
        if v == 1:
            ax.text(x0 + v / 2, -0.7, "1² = 1", ha="center", va="center", color=c, fontweight="bold", fontsize=11.5)
        else:
            ax.text(x0 + v / 2, v / 2, f"{v}² = {v * v}", ha="center", va="center", color="white", fontweight="bold", fontsize=11.5)
        x0 += v + 0.4
    ax.text(3.5, 4.6, "Σx² = 1 + 4 + 16 = 21", ha="center", fontsize=13.5, fontweight="bold")
    ax.add_patch(Rectangle((8.2, 0), 7, 7, fc="none", ec=RED, lw=2))
    for i in range(1, 7):
        ax.plot([8.2 + i, 8.2 + i], [0, 7], color=LIGHTRED, lw=0.8)
        ax.plot([8.2, 15.2], [i, i], color=LIGHTRED, lw=0.8)
    ax.text(11.7, 7.5, "(Σx)² = 7² = 49", ha="center", fontsize=13.5, fontweight="bold", color=RED)
    ax.set_xlim(-0.3, 15.6)
    ax.set_ylim(-1.2, 8.2)
    ax.set_aspect("equal")
    ax.axis("off")
    panel(ax, "Σx² ≠ (Σx)²", "square first, then add  vs  add first, then square")

    ax = axes[1]
    x = np.array([1, 2, 4])
    dev = x - x.mean()
    ax.bar(range(3), dev, color=[RED if d < 0 else GREEN for d in dev], width=0.55)
    for i, d in enumerate(dev):
        ax.text(i, d + (0.12 if d > 0 else -0.25), f"{d:+.2f}", ha="center", fontsize=13, fontweight="bold")
    ax.axhline(0, color=INK, lw=1.2)
    ax.set_xticks(range(3), ["x = 1", "x = 2", "x = 4"])
    ax.set_ylabel("deviation x − x̄  (x̄ = 7/3 = 2.33)")
    ax.set_ylim(-2, 2.2)
    ax.text(-0.35, 1.55, "sum = 0 always\n→ square before adding:\nΣ(x − x̄)² = 1.78 + 0.11 + 2.78\n= 4.67",
            ha="left", va="center", fontsize=11.5, color=INK)
    panel(ax, "Deviations always add to 0", "that is why variance squares them")

    ax = axes[2]
    probs = [0.5, 0.2, 0.1]
    logs = np.log(probs)
    left = 0
    for p, lg, c in zip(probs, logs, [BLUE, ORANGE, GREEN]):
        ax.barh(0, lg, left=left, color=c, height=0.45)
        ax.text(left + lg / 2, 0, f"log {p}\n= {lg:.2f}", ha="center", va="center", color="white", fontweight="bold",
                fontsize=11 if p != 0.5 else 9.5)
        left += lg
    ax.text(left / 2, 0.55, f"log(0.5 × 0.2 × 0.1) = log 0.01 = {np.log(0.01):.2f}", ha="center", fontsize=12.5, fontweight="bold")
    ax.text(left / 2, -0.62, "a product of probabilities becomes a SUM of logs", ha="center", fontsize=12, color=MUTED)
    ax.set_xlim(left - 0.3, 0.3)
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("natural log")
    panel(ax, "log(ab) = log a + log b", "used for likelihoods (log-likelihood)")
    note(fig, "Order matters: Σx² squares each value then adds; (Σx)² adds then squares. In Python, x**2 squares; x^2 does NOT.",
         "Logs turn products into sums, and log(a + b) is NOT log a + log b.")
    save(fig, "sums_squares_and_logs")


# ---------------------------------------------------------------- 18.2
def bayes_sensor():
    fig, axes = figure("Reversing a conditional probability: the flaw sensor",
                       "10% of parts are flawed. The sensor flags 90% of flawed parts and 20% of good parts.", 3)
    ax = axes[0]
    cols, rows = 40, 25
    k = 0
    cats = [(90, RED, "flawed, flagged (90)"), (10, LIGHTRED, "flawed, missed (10)"),
            (180, ORANGE, "good, flagged (180)"), (720, LIGHTBLUE, "good, not flagged (720)")]
    for n, c, _ in cats:
        for _ in range(n):
            r, cc = divmod(k, cols)
            ax.add_patch(Rectangle((cc, rows - 1 - r), 0.85, 0.85, color=c))
            k += 1
    ax.set_xlim(0, cols)
    ax.set_ylim(-7.5, rows)
    ax.set_aspect("equal")
    ax.axis("off")
    for i, (_, c, lab) in enumerate(cats):
        ax.add_patch(Rectangle((0 + (i % 2) * 20, -2.5 - (i // 2) * 2.8), 1.2, 1.2, color=c))
        ax.text(1.8 + (i % 2) * 20, -1.9 - (i // 2) * 2.8, lab, va="center", fontsize=11)
    panel(ax, "Imagine 1,000 parts", "each square = 1 part")

    ax = axes[1]
    ax.axis("off")
    nodes = {"root": (0.05, 0.5), "D": (0.42, 0.78), "Dc": (0.42, 0.22),
             "DF": (0.85, 0.92), "DN": (0.85, 0.64), "GF": (0.85, 0.36), "GN": (0.85, 0.08)}
    labels = {"root": "1,000", "D": "flawed\n100", "Dc": "good\n900", "DF": "flag 90", "DN": "no flag 10",
              "GF": "flag 180", "GN": "no flag 720"}
    colors = {"DF": RED, "GF": ORANGE, "D": INK, "Dc": INK, "root": INK, "DN": MUTED, "GN": MUTED}
    edges = [("root", "D", "0.10"), ("root", "Dc", "0.90"), ("D", "DF", "0.90"), ("D", "DN", "0.10"),
             ("Dc", "GF", "0.20"), ("Dc", "GN", "0.80")]
    for a, b, p in edges:
        (x0, y0), (x1, y1) = nodes[a], nodes[b]
        ax.plot([x0 + 0.06, x1 - 0.08], [y0, y1], color=MUTED, lw=1.5, transform=ax.transAxes)
        ax.text((x0 + x1) / 2, (y0 + y1) / 2 + 0.03, p, transform=ax.transAxes, ha="center", fontsize=12, color=BLUE,
                fontweight="bold", bbox=dict(fc="white", ec="none", pad=1))
    for n, (x, y) in nodes.items():
        ax.text(x, y, labels[n], transform=ax.transAxes, ha="center", va="center", fontsize=12.5, fontweight="bold",
                color=colors[n], bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=colors[n]))
    panel(ax, "Tree diagram (Lesson 5.10)", "multiply along branches")

    ax = axes[2]
    for prev, y in [(0.10, 1), (0.01, 0)]:
        tp, fp = 0.9 * prev * 1000, 0.2 * (1 - prev) * 1000
        ax.barh(y, tp, color=RED, height=0.5)
        ax.barh(y, fp, left=tp, color=ORANGE, height=0.5)
        ax.text(tp + fp + 5, y, f"P(flawed | flag)\n= {tp:.0f}/{tp + fp:.0f}\n= {tp / (tp + fp):.3f}", va="center", fontsize=11.5,
                fontweight="bold")
    ax.set_yticks([1, 0], ["10% flawed", "1% flawed"], fontsize=12.5)
    ax.set_xlabel("flagged parts out of 1,000 (red = really flawed)")
    ax.set_xlim(0, 400)
    panel(ax, "Among FLAGGED parts", "the base rate matters a lot")
    note(fig, "P(flag | flawed) = 0.90 but P(flawed | flag) = 90/270 = 1/3. Conditional probabilities are not symmetric.",
         "Bayes: P(D|F) = P(F|D)P(D) / P(F), with P(F) = 0.9(0.1) + 0.2(0.9) = 0.27. With only 1% flawed it drops to 0.043.")
    save(fig, "bayes_sensor")


# ---------------------------------------------------------------- 18.3
def variance_rules():
    fig, axes = figure("Expectation adds simply; variance needs the covariance",
                       "Var(X) = 4, Var(Y) = 9, Cov(X, Y) = 3", 3)
    rng = np.random.default_rng(18)
    cov = np.array([[4, 3], [3, 9]])
    xy = rng.multivariate_normal([0, 0], cov, 3000)
    ax = axes[0]
    ax.scatter(xy[:600, 0], xy[:600, 1], s=8, color=BLUE, alpha=0.5)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.text(0.03, 0.93, "positive covariance:\nX and Y tend to move together", transform=ax.transAxes, fontsize=11.5)
    panel(ax, "A  |  X and Y are related", f"correlation = 3/(2·3) = 0.5")

    ax = axes[1]
    d = xy[:, 0] - xy[:, 1]
    ax.hist(d, bins=50, density=True, color=LIGHTGREEN, ec="white")
    g = np.linspace(-12, 12, 400)
    ax.plot(g, stats.norm.pdf(g, 0, np.sqrt(7)), color=GREEN, lw=2.5, label="correct: Var = 4 + 9 − 2·3 = 7")
    ax.plot(g, stats.norm.pdf(g, 0, np.sqrt(13)), color=RED, lw=2.2, ls="--", label="wrong (ignores Cov): 13")
    ax.set_xlabel("X − Y")
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_ylim(0, 0.24)
    ax.legend(loc="upper left", frameon=False, fontsize=11)
    ax.text(0.99, 0.5, f"simulated\nVar(X − Y)\n= {d.var():.2f}", transform=ax.transAxes, ha="right", fontsize=12, color=GREEN,
            fontweight="bold", bbox=dict(fc="white", ec="none", alpha=0.85))
    panel(ax, "B  |  Var(X − Y)", "Var(aX + bY) = a²Var X + b²Var Y + 2ab Cov")

    ax = axes[2]
    xs = np.linspace(-1, 1, 41)
    ax.plot(xs, xs ** 2, color=MUTED, lw=1.2)
    ax.scatter(xs, xs ** 2, color=ORANGE, s=22, zorder=3)
    ax.axvline(0, color=GRID)
    ax.set_xlabel("X  (uniform on −1 to 1)")
    ax.set_ylabel("Y = X²")
    ax.text(0, 0.82, "Cov(X, Y) = 0\nbut Y is completely\ndetermined by X", ha="center", fontsize=12, fontweight="bold", color=ORANGE)
    panel(ax, "C  |  Zero covariance ≠ independence", "left and right halves cancel")
    note(fig, "E(aX + bY) = aE(X) + bE(Y) always. Var(aX + bY) adds 2ab·Cov(X, Y), which is 0 only without a linear link.",
         "For n independent observations, Var(x̄) = σ²/n, so SE = σ/√n. Correlated data (pairs, clusters) need the Cov terms.")
    save(fig, "variance_rules")


# ---------------------------------------------------------------- 18.4
def lln_and_clt():
    fig, axes = figure("Law of large numbers and central limit theorem",
                       "Waiting times from an exponential distribution with mean 2 and SD 2 (very skewed)", 4,
                       size=(16, 7.4), wspace=0.3)
    rng = np.random.default_rng(4)
    ax = axes[0]
    for c in [BLUE, ORANGE, GREEN]:
        s = rng.exponential(2, 2000)
        ax.plot(np.arange(1, 2001), np.cumsum(s) / np.arange(1, 2001), color=c, lw=1.6)
    ax.axhline(2, color=INK, ls="--")
    ax.set_xscale("log")
    ax.set_ylim(0, 5)
    ax.set_xlabel("n (log scale)")
    ax.set_ylabel("running mean x̄ₙ")
    panel(ax, "LLN", "x̄ settles at μ = 2")
    for ax, n in zip(axes[1:], [1, 5, 30]):
        m = rng.exponential(2, (20000, n)).mean(1)
        ax.hist(m, bins=60, density=True, color=LIGHTBLUE, ec="white")
        g = np.linspace(max(0, 2 - 4 * 2 / np.sqrt(n)), 2 + 5 * 2 / np.sqrt(n), 300)
        if n > 1:
            ax.plot(g, stats.norm.pdf(g, 2, 2 / np.sqrt(n)), color=ORANGE, lw=2.2, label="normal curve")
            ax.legend(loc="upper right", frameon=False, fontsize=10.5)
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.set_xlabel(f"mean of n = {n}")
        ax.set_xlim(0, 2 + 5 * 2 / np.sqrt(n) if n > 1 else 10)
        panel(ax, f"CLT: n = {n}", f"SD of x̄ = 2/√{n} = {2 / np.sqrt(n):.2f}")
    note(fig, "LLN: the sample mean gets close to μ. CLT: its random error looks more and more like a normal curve with SD σ/√n.",
         "The raw data stay skewed. There is no magic n = 30: the more skewed the data, the larger n must be.")
    save(fig, "lln_and_clt")


# ---------------------------------------------------------------- 18.5
def derivatives():
    fig, (ax, ax2) = figure("A derivative is the slope of the tangent; the minimum is where it hits 0",
                            "Loss L(m) = (5 − 2m)²; chain rule: L′(m) = 2(5 − 2m)·(−2) = 8m − 20", 2, wspace=0.25)
    b = np.linspace(0, 5, 300)
    L = (5 - 2 * b) ** 2
    ax.plot(b, L, color=BLUE, lw=2.6)
    for b0, c in [(1, RED), (2.5, GREEN), (4, ORANGE)]:
        L0, s = (5 - 2 * b0) ** 2, 8 * b0 - 20
        t = np.linspace(b0 - 0.8, b0 + 0.8, 2)
        ax.plot(t, L0 + s * (t - b0), color=c, lw=2)
        ax.plot(b0, L0, "o", color=c, ms=9)
        ax.text(b0 + (0.15 if b0 != 2.5 else 0), L0 + (2.2 if b0 != 2.5 else 1.6), f"slope {s:+.0f}" if s else "slope 0",
                color=c, fontsize=12.5, fontweight="bold", ha="left" if b0 != 2.5 else "center")
    ax.set_xlabel("m")
    ax.set_ylabel("L(m)")
    ax.set_ylim(-2, 27)
    panel(ax, "Tangent lines on L(m)", "downhill (−), flat (0), uphill (+)")

    ax2.plot(b, 8 * b - 20, color=ORANGE, lw=2.6)
    ax2.axhline(0, color=INK, lw=1)
    ax2.plot(2.5, 0, "o", color=GREEN, ms=11)
    ax2.annotate("L′(m) = 0 at m = 2.5\n→ the minimum", xy=(2.5, 0), xytext=(2.9, -12), color=GREEN, fontsize=13,
                 fontweight="bold", arrowprops=dict(arrowstyle="->", color=GREEN))
    ax2.text(0.3, 12, "L″(m) = 8 > 0:\ncurves upward → minimum", fontsize=12.5, color=INK)
    ax2.set_xlabel("m")
    ax2.set_ylabel("L′(m) = 8m − 20")
    panel(ax2, "The derivative L′(m)", "negative left of 2.5, positive right of it")
    note(fig, "To minimise a smooth loss: differentiate, set the derivative to 0, solve, and check the second derivative is positive.",
         "That is exactly how least squares finds the best line (Lesson 18.6).")
    save(fig, "derivative_and_minimum")


# ---------------------------------------------------------------- 18.6
def least_squares_derivation():
    fig, (ax, ax2) = figure("Deriving the least squares line", "x = (0, 1, 2, 3), y = (1, 2, 2, 4)", 2, wspace=0.25)
    x, y = np.array([0, 1, 2, 3.]), np.array([1, 2, 2, 4.])
    a, b = 0.9, 0.9
    xs = np.linspace(-0.3, 3.3, 2)
    ax.plot(xs, a + b * xs, color=ORANGE, lw=2.6)
    for xi, yi in zip(x, y):
        f = a + b * xi
        ax.plot([xi, xi], [yi, f], color=RED, lw=1.6, ls=":")
        ax.text(xi + 0.07, (yi + f) / 2, f"{yi - f:+.1f}", color=RED, fontsize=12, fontweight="bold", va="center")
    ax.scatter(x, y, color=BLUE, s=80, zorder=4, ec="white")
    ax.plot(1.5, 2.25, "s", color=INK, ms=9)
    ax.annotate("(x̄, ȳ) = (1.5, 2.25)\nthe line passes through it", xy=(1.5, 2.25), xytext=(0.3, 3.3), fontsize=11.5,
                arrowprops=dict(arrowstyle="->", color=INK))
    ax.text(0.03, 0.93, "ŷ = 0.9 + 0.9x", transform=ax.transAxes, color=ORANGE, fontsize=14, fontweight="bold")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    panel(ax, "Best line and its residuals", "residuals add to 0; SSE = 0.01 + 0.04 + 0.49 + 0.16 = 0.7")

    A, B = np.meshgrid(np.linspace(-0.6, 2.4, 200), np.linspace(0.2, 1.6, 200))
    SSE = ((y[None, None, :] - A[..., None] - B[..., None] * x[None, None, :]) ** 2).sum(-1)
    cs = ax2.contour(A, B, SSE, levels=[0.8, 1, 1.5, 2.5, 4, 6, 9, 13], colors=BLUE, linewidths=1.2)
    ax2.clabel(cs, fontsize=9.5, fmt="%g")
    ax2.plot(0.9, 0.9, "*", color=ORANGE, ms=18)
    ax2.text(1.15, 1.08, "minimum SSE = 0.7\nat m = 0.9, b = 0.9", fontsize=12.5, color=ORANGE, fontweight="bold",
             bbox=dict(fc="white", ec="none", alpha=0.9))
    ax2.set_xlabel("intercept b")
    ax2.set_ylabel("slope m")
    panel(ax2, "SSE(m, b) as a contour map", "a bowl with one lowest point")
    note(fig, "Set ∂SSE/∂m = 0 and ∂SSE/∂b = 0  →  m = Sxy/Sxx = 4.5/5 = 0.9,  b = ȳ − m·x̄ = 2.25 − 0.9(1.5) = 0.9",
         "The same formulas as Lesson 13.1, written with deviations from the means.")
    save(fig, "least_squares_derivation")


# ---------------------------------------------------------------- 18.7
def matrix_notation():
    fig, (ax, ax2) = figure("Regression in matrix form, and R² vs adjusted R²", "the four-point example: ŷ = 0.9 + 0.9x", 2,
                            wspace=0.15)
    ax.set_position([0.03, 0.25, 0.55, 0.5])
    ax2.set_position([0.66, 0.25, 0.32, 0.5])
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)

    def mat(x0, vals, title, color, w=1.1):
        rows, cols = len(vals), len(vals[0])
        ax.add_patch(FancyBboxPatch((x0, 0.8), cols * w, rows * 1.0 + 0.2, boxstyle="round,pad=0.05,rounding_size=0.15",
                                    fc="white", ec=color, lw=2))
        for i, row in enumerate(vals):
            for j, v in enumerate(row):
                ax.text(x0 + (j + 0.5) * w, 0.9 + (rows - i - 0.5) * 1.0, v, ha="center", va="center", fontsize=13.5)
        ax.text(x0 + cols * w / 2, 5.4, title, ha="center", fontsize=14, fontweight="bold", color=color)

    mat(0.2, [["1"], ["2"], ["2"], ["4"]], "y", BLUE)
    ax.text(1.75, 2.9, "=", fontsize=22, ha="center", va="center")
    mat(2.3, [["1", "0"], ["1", "1"], ["1", "2"], ["1", "3"]], "X", ORANGE)
    ax.text(5.15, 2.9, "×", fontsize=20, ha="center", va="center")
    ax.add_patch(FancyBboxPatch((5.7, 1.85), 1.1, 2.2, boxstyle="round,pad=0.05,rounding_size=0.15", fc="white", ec=GREEN, lw=2))
    ax.text(6.25, 3.5, "0.9", ha="center", va="center", fontsize=13.5)
    ax.text(6.25, 2.4, "0.9", ha="center", va="center", fontsize=13.5)
    ax.text(6.25, 5.4, "β̂", ha="center", fontsize=14, fontweight="bold", color=GREEN)
    ax.text(7.35, 2.9, "+", fontsize=22, ha="center", va="center")
    mat(7.9, [["0.1"], ["0.2"], ["−0.7"], ["0.4"]], "e (residuals)", RED, w=1.4)
    ax.text(10.0, 3.6, "column of 1s\n→ intercept", fontsize=11, color=ORANGE)
    ax.text(10.0, 1.6, "XᵀX = [4 6; 6 14]\nXᵀy = [9; 18]\nβ̂ = (XᵀX)⁻¹Xᵀy", fontsize=11.5, color=INK)
    ax.text(6, 0.2, "n = 4 rows, K = 2 columns (full rank: no column copies another)", ha="center", fontsize=12, color=MUTED)

    ax2.bar([0, 1], [0.8526, 0.7789], color=[ORANGE, BLUE], width=0.55)
    ax2.text(0, 0.87, "R² = 1 − 0.7/4.75\n= 0.853", ha="center", fontsize=12.5, fontweight="bold", color=ORANGE)
    ax2.text(1, 0.80, "adj R² = 1 − (0.7/2)/(4.75/3)\n= 0.779", ha="center", fontsize=12.5, fontweight="bold", color=BLUE)
    ax2.set_xticks([0, 1], ["same denominators\n(SSE/n ÷ TSS/n)", "variance estimates\n(SSE/(n−K) ÷ TSS/(n−1))"])
    ax2.set_ylim(0, 1.05)
    ax2.set_ylabel("share of variation explained")
    panel(ax2, "Denominators matter", "")
    note(fig, "y = Xβ + ε puts every regression in one form. Solve the normal equations XᵀX β̂ = Xᵀy (software uses a stable solver).",
         "Dividing SSE and TSS by the same n keeps R²; dividing by their degrees of freedom gives adjusted R².")
    save(fig, "matrix_notation")


# ---------------------------------------------------------------- 18.8
def arrays_and_axes():
    fig, (ax, ax2) = figure("Arrays: which axis you average over changes the question",
                            "samples has shape (experiments, observations) = (6, 5) here; (1000, 20) in the exercise", 2, wspace=0.25)
    rng = np.random.default_rng(8)
    data = rng.integers(1, 10, (6, 5))
    ax.axis("off")
    ax.set_xlim(-0.5, 8.2)
    ax.set_ylim(-2.2, 7)
    for i in range(6):
        for j in range(5):
            ax.add_patch(Rectangle((j, 5 - i), 0.95, 0.95, fc=LIGHTBLUE, ec="white"))
            ax.text(j + 0.47, 5 - i + 0.47, str(data[i, j]), ha="center", va="center", fontsize=12)
        ax.add_patch(Rectangle((5.6, 5 - i), 1.3, 0.95, fc=LIGHTORANGE, ec="white"))
        ax.text(6.25, 5 - i + 0.47, f"{data[i].mean():.1f}", ha="center", va="center", fontsize=12, color=ORANGE, fontweight="bold")
    for j in range(5):
        ax.add_patch(Rectangle((j, -1.2), 0.95, 0.95, fc=LIGHTGREEN, ec="white"))
        ax.text(j + 0.47, -0.73, f"{data[:, j].mean():.1f}", ha="center", va="center", fontsize=11, color=GREEN, fontweight="bold")
    ax.annotate("", xy=(5.5, 3.5), xytext=(4.95, 3.5), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2))
    ax.text(6.25, 6.4, "mean(axis=1)\none mean per\nexperiment", ha="center", fontsize=11.5, color=ORANGE, fontweight="bold")
    ax.text(2.5, -1.9, "mean(axis=0): one mean per column (usually NOT what you want here)", ha="center", fontsize=11, color=GREEN)
    ax.text(-0.3, 6.6, "← 5 observations →", fontsize=11.5, color=MUTED)
    panel(ax, "axis=1 averages across a row", "")

    reps, n = 20000, 5
    s = rng.normal(0, 2, (reps, n))
    v0, v1 = s.var(axis=1, ddof=0), s.var(axis=1, ddof=1)
    ax2.bar([0, 1], [v0.mean(), v1.mean()], color=[RED, GREEN], width=0.55)
    ax2.axhline(4, color=INK, ls="--")
    ax2.text(0.5, 4.1, "true σ² = 4", ha="center", fontsize=12)
    ax2.text(0, v0.mean() + 0.1, f"{v0.mean():.2f}", ha="center", fontsize=14, fontweight="bold", color=RED)
    ax2.text(1, v1.mean() + 0.1, f"{v1.mean():.2f}", ha="center", fontsize=14, fontweight="bold", color=GREEN)
    ax2.set_xticks([0, 1], ["np.var(x)\n(ddof=0, divide by n)", "np.var(x, ddof=1)\n(divide by n − 1)"])
    ax2.set_ylabel("average estimate of σ² (20,000 samples of n = 5)")
    ax2.set_ylim(0, 5)
    panel(ax2, "NumPy's default divides by n", "too small on average by the factor (n − 1)/n = 0.8")
    note(fig, "Check shapes and axes before averaging. Use ddof=1 for the usual sample variance and SD (Lesson 3.13).",
         "Seeded generators like np.random.default_rng(123) make a run repeatable; restart and run all cells top to bottom.")
    save(fig, "arrays_axes_and_ddof")
    return data, v0.mean(), v1.mean()


if __name__ == "__main__":
    sums_and_logs()
    bayes_sensor()
    variance_rules()
    lln_and_clt()
    derivatives()
    least_squares_derivation()
    matrix_notation()
    print("18.8:", arrays_and_axes()[1:])

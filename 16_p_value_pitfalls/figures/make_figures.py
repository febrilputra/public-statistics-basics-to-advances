"""Draw every figure for Chapter 16 - P-Value Pitfalls (multiple testing, selection, stopping).

Run with Python, NumPy, SciPy and Matplotlib installed:
    python 16_p_value_pitfalls/figures/make_figures.py
Each figure is written beside this script as a PNG (for the notes) and an SVG.
Simulations use fixed seeds; the numbers they print are quoted in the lessons.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle
from scipy import stats

OUT = Path(__file__).resolve().parent
BLUE, ORANGE, GREEN, YELLOW = "#0072B2", "#D55E00", "#009E73", "#E69F00"
INK, MUTED, RED, LIGHTRED, GRID, LIGHTBLUE = "#222222", "#555555", "#C0392B", "#E8B4B4", "#E6E6E6", "#BFD3E6"
LIGHTGREEN = "#BFE6D8"

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


P = np.array([0.001, 0.012, 0.021, 0.040, 0.200])   # the worked example, already sorted


def holm(p):
    m = len(p)
    o = np.argsort(p)
    adj = np.minimum(1, np.maximum.accumulate((m - np.arange(m)) * p[o]))
    out = np.empty(m)
    out[o] = adj
    return out


def bh(p):
    m = len(p)
    o = np.argsort(p)
    adj = np.minimum(1, np.minimum.accumulate((m * p[o] / np.arange(1, m + 1))[::-1])[::-1])
    out = np.empty(m)
    out[o] = adj
    return out


# ---------------------------------------------------------------- 16.1
def multiple_testing_problem():
    fig, (ax, ax2) = figure("Test enough things and something will look 'significant'",
                            "20 independent tests where NOTHING is going on, each at α = 0.05", 2, wspace=0.22)
    rng = np.random.default_rng(1)  # seed chosen so that this run shows exactly one false positive
    p = rng.uniform(size=20)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 4)
    ax.axis("off")
    for i, pv in enumerate(p):
        r, c = divmod(i, 5)
        hit = pv < 0.05
        ax.add_patch(plt.Circle((c + 0.5, 3.5 - r), 0.42, color=RED if hit else LIGHTBLUE, ec="white"))
        ax.text(c + 0.5, 3.5 - r + 0.08, f"test {i + 1}", ha="center", va="center", fontsize=9.5,
                color="white" if hit else INK)
        ax.text(c + 0.5, 3.5 - r - 0.15, f"p = {pv:.3f}", ha="center", va="center", fontsize=10.5,
                color="white" if hit else INK, fontweight="bold" if hit else "normal")
    panel(ax, "One run of 20 null tests", f"{(p < 0.05).sum()} red 'discovery' even though every null is true")

    m = np.arange(1, 61)
    fw = 1 - 0.95 ** m
    ax2.plot(m, fw, color=BLUE, lw=2.6)
    for k in [1, 5, 10, 20, 50]:
        v = 1 - 0.95 ** k
        ax2.plot(k, v, "o", color=ORANGE, ms=8)
        ax2.text(k + 1.2, v - 0.045, f"m = {k}: {v:.3f}", fontsize=12, color=ORANGE, fontweight="bold")
    ax2.set_xlabel("number of independent tests m (all nulls true)")
    ax2.set_ylabel("P(at least one false positive)")
    ax2.set_ylim(0, 1.05)
    panel(ax2, "P(at least one false positive) = 1 − 0.95ᵐ", "the expected number of false positives is m × 0.05")
    note(fig, "With 20 tests: P(at least one false positive) = 1 − 0.95²⁰ = 0.642, and on average 20 × 0.05 = 1 false positive.",
         "Each test is fine on its own. The problem is reporting whichever one happens to come out small.")
    save(fig, "multiple_testing_problem")
    return (p < 0.05).sum()


# ---------------------------------------------------------------- 16.2
FAMILIES = [(8, 0), (7, 1), (9, 0), (6, 0), (8, 1), (7, 0), (9, 0), (8, 0), (7, 2), (8, 0)]


def fwer_vs_fdr():
    fig, (ax, ax2) = figure("Two ways to count mistakes: FWER and FDR",
                            "Imagine repeating the same screening study 10 times. Each row = the discoveries of one study.",
                            2, wspace=0.12)
    ax.set_position([0.04, 0.25, 0.56, 0.5])
    ax2.set_position([0.64, 0.25, 0.34, 0.5])
    ax.set_xlim(-0.5, 14)
    ax.set_ylim(-2.0, len(FAMILIES) - 0.3)
    ax.axis("off")
    fdps = []
    for row, (t, f) in enumerate(FAMILIES):
        y = len(FAMILIES) - 1 - row
        ax.text(-0.3, y, f"study {row + 1}", ha="right", va="center", fontsize=11)
        for k in range(t):
            ax.add_patch(Rectangle((k * 0.8, y - 0.32), 0.65, 0.64, color=GREEN))
        for k in range(f):
            ax.add_patch(Rectangle(((t + k) * 0.8, y - 0.32), 0.65, 0.64, color=RED))
        fdp = f / (t + f)
        fdps.append(fdp)
        ax.text(9.2, y, "any false? " + ("YES" if f else "no"), va="center", fontsize=11.5,
                color=RED if f else MUTED, fontweight="bold" if f else "normal")
        ax.text(12.0, y, f"V/R = {f}/{t + f} = {fdp:.3f}", va="center", fontsize=11.5, color=RED if f else MUTED)
    fwer = np.mean([f > 0 for _, f in FAMILIES])
    fdr = np.mean(fdps)
    ax.text(9.2, -1.05, f"FWER = {sum(f > 0 for _, f in FAMILIES)}/10 studies with a false one = {fwer:.2f}",
            fontsize=13, fontweight="bold", color=ORANGE)
    ax.text(9.2, -1.7, f"FDR = average of the 10 V/R values = {fdr:.3f}", fontsize=13, fontweight="bold", color=BLUE)
    ax.text(0, -1.05, "■ true discovery   ", color=GREEN, fontsize=12.5, fontweight="bold")
    ax.text(3.6, -1.05, "■ false discovery", color=RED, fontsize=12.5, fontweight="bold")
    ax.text(0.5, 1.06, "Discoveries in 10 repeated studies", transform=ax.transAxes, ha="center", fontsize=15, fontweight="bold")

    ax2.axis("off")
    blocks = [("FWER  family-wise error rate", "P(V ≥ 1)", "chance of ONE OR MORE false\ndiscoveries in the family", ORANGE),
              ("FDR  false discovery rate", "E( V / max(R, 1) )", "average FRACTION of false\ndiscoveries among the discoveries", BLUE)]
    for i, (h, f, t, c) in enumerate(blocks):
        y = 0.75 - i * 0.48
        ax2.add_patch(FancyBboxPatch((0.0, y - 0.2), 1.0, 0.4, boxstyle="round,pad=0,rounding_size=0.03",
                                     transform=ax2.transAxes, fc="white", ec=c, lw=1.8))
        ax2.text(0.05, y + 0.12, h, transform=ax2.transAxes, fontsize=13.5, fontweight="bold", color=c)
        ax2.text(0.05, y + 0.02, f, transform=ax2.transAxes, fontsize=14)
        ax2.text(0.05, y - 0.11, t, transform=ax2.transAxes, fontsize=12, color=MUTED, va="center")
    ax2.text(0.5, -0.12, "V = false discoveries, R = all discoveries", transform=ax2.transAxes, ha="center", fontsize=12, color=MUTED)
    note(fig, "FWER asks 'did we make ANY false claim?'. FDR asks 'what share of our claims are false, on average?'",
         "Control FWER when one false claim is costly; control FDR when screening many leads that will be checked again.")
    save(fig, "fwer_vs_fdr")
    return fwer, fdr


# ---------------------------------------------------------------- 16.3
def bonferroni_and_holm():
    fig, (ax, ax2) = figure("Bonferroni and Holm: two ways to keep FWER ≤ 0.05",
                            "Five planned comparisons, p-values sorted from smallest to largest", 2, wspace=0.25)
    m = len(P)
    k = np.arange(1, m + 1)
    bonf = np.full(m, 0.05 / m)
    holm_thr = 0.05 / (m - k + 1)
    ax.step(np.r_[0.5, k + 0.5], np.r_[holm_thr[0], holm_thr], where="pre", color=GREEN, lw=2.4, label="Holm: α/(m − k + 1)")
    ax.plot([0.5, 5.5], [0.01, 0.01], color=ORANGE, lw=2.4, ls="--", label="Bonferroni: α/m = 0.01")
    hrej = np.zeros(m, bool)
    for i in range(m):
        if P[i] <= holm_thr[i]:
            hrej[i] = True
        else:
            break
    for i in range(m):
        c = GREEN if hrej[i] else MUTED
        ax.plot(k[i], P[i], "o", ms=12, color=c, zorder=5, mec="white")
        ax.text(k[i] + 0.12, P[i] * 1.12, f"{P[i]:.3f}", fontsize=12, color=c, fontweight="bold")
    for i, t in enumerate(holm_thr):
        ax.text(k[i] - 0.28, t * 1.1, f"{t:.4f}".rstrip("0"), ha="center", fontsize=10, color=GREEN)
    ax.annotate("stop here:\n0.021 > 0.0167", xy=(3, 0.021), xytext=(3.4, 0.0035), color=RED, fontsize=11.5,
                arrowprops=dict(arrowstyle="->", color=RED))
    ax.set_yscale("log")
    ax.set_ylim(0.0007, 0.35)
    ax.set_xticks(k, [f"k = {i}" for i in k])
    ax.set_ylabel("p-value (log scale)")
    ax.legend(loc="upper left", frameon=False)
    panel(ax, "Holm steps up the threshold", "Bonferroni rejects 1 (only 0.001); Holm rejects 2")

    adj = {"raw p": P, "Bonferroni": np.minimum(1, m * P), "Holm": holm(P)}
    x = np.arange(m)
    for j, (name, vals) in enumerate(adj.items()):
        c = [MUTED, ORANGE, GREEN][j]
        ax2.bar(x + (j - 1) * 0.26, np.minimum(vals, 0.22), width=0.25, color=c, label=name)
        for xi, v in zip(x, vals):
            if v <= 0.05 and name != "raw p":
                ax2.text(xi + (j - 1) * 0.26, min(v, 0.22) + 0.004, "✓", ha="center", color=c, fontsize=13, fontweight="bold")
    ax2.axhline(0.05, color=RED, ls="--", lw=1.3)
    ax2.text(4.6, 0.054, "0.05", color=RED, ha="right")
    ax2.set_xticks(x, [f"{v:.3f}" for v in P])
    ax2.set_xlabel("raw p-value of each test")
    ax2.set_ylabel("adjusted p-value (bars cut at 0.22)")
    ax2.legend(loc="upper left", frameon=False)
    panel(ax2, "Adjusted p-values: reject if ≤ 0.05", "✓ = rejected after adjustment")
    note(fig, "Bonferroni: compare every p with α/m. Holm: compare the k-th smallest with α/(m − k + 1) and stop at the first failure.",
         "Both control FWER for any dependence between tests. Holm always rejects at least as many as Bonferroni.")
    save(fig, "bonferroni_vs_holm")


# ---------------------------------------------------------------- 16.4
def benjamini_hochberg():
    fig, (ax, ax2) = figure("Benjamini–Hochberg: controlling the false discovery rate",
                            "Find the LARGEST k with p₍ₖ₎ ≤ (k/m)·q, then reject the k smallest p-values", 2, wspace=0.25)
    m = len(P)
    k = np.arange(1, m + 1)
    q = 0.05
    line = k / m * q
    ax.plot(k, line, color=BLUE, lw=2.4, marker="s", ms=6, label="BH line (k/m)·q")
    ax.plot([0.5, 5.5], [0.01, 0.01], color=ORANGE, lw=2, ls="--", label="Bonferroni α/m")
    kmax = max(i for i in k if P[i - 1] <= line[i - 1])
    for i in k:
        c = BLUE if i <= kmax else MUTED
        ax.plot(i, P[i - 1], "o", ms=12, color=c, mec="white", zorder=5)
        ax.text(i + 0.12, P[i - 1] * 1.12, f"{P[i - 1]:.3f}", color=c, fontsize=12, fontweight="bold")
        ax.text(i - 0.15, line[i - 1] * 1.13, f"{line[i - 1]:.2f}", ha="right", color=BLUE, fontsize=10)
    ax.annotate(f"largest k under the line: k = {kmax}\n→ reject tests 1–{kmax}", xy=(kmax, P[kmax - 1]), xytext=(2.2, 0.0018),
                fontsize=12, color=BLUE, fontweight="bold", arrowprops=dict(arrowstyle="->", color=BLUE))
    ax.set_xticks(k, [f"k = {i}" for i in k])
    ax.set_ylabel("sorted p-value (log scale)")
    ax.set_yscale("log")
    ax.set_ylim(0.0007, 0.4)
    ax.legend(loc="upper left", frameon=False)
    panel(ax, "BH on the five example p-values", f"q = 0.05: BH rejects {kmax}, Holm 2, Bonferroni 1")

    rng = np.random.default_rng(1010)
    F, M, NULLS = 3000, 100, 80
    z = rng.normal(size=(F, M))
    z[:, NULLS:] += 3
    pm = 2 * stats.norm.sf(np.abs(z))
    res = {}
    for name, fn in [("Bonferroni", lambda p: np.minimum(1, M * p)), ("Holm", holm), ("BH", bh)]:
        rej = np.array([fn(row) for row in pm]) <= 0.05
        false = rej[:, :NULLS].sum(1)
        tot = rej.sum(1)
        res[name] = (np.mean(false > 0), np.mean(false / np.maximum(tot, 1)), tot.mean())
    names = list(res)
    x = np.arange(3)
    ax2.bar(x - 0.2, [res[n][0] for n in names], 0.38, color=ORANGE, label="estimated FWER")
    ax2.bar(x + 0.2, [res[n][1] for n in names], 0.38, color=BLUE, label="estimated FDR")
    for i, n in enumerate(names):
        ax2.text(i - 0.2, res[n][0] + 0.012, f"{res[n][0]:.3f}", ha="center", fontsize=11.5, color=ORANGE, fontweight="bold")
        ax2.text(i + 0.2, res[n][1] + 0.012, f"{res[n][1]:.3f}", ha="center", fontsize=11.5, color=BLUE, fontweight="bold")
    ax2.axhline(0.05, color=RED, ls="--", lw=1.2)
    ax2.text(2.55, 0.056, "0.05", color=RED, ha="right")
    ax2.set_xticks(x, [f"{n}\n{res[n][2]:.1f} discoveries / study" for n in names], fontsize=12)
    ax2.set_ylim(0, 0.5)
    ax2.legend(loc="upper left", frameon=False)
    panel(ax2, "3,000 simulated studies, 100 tests each", "80 true nulls + 20 real effects")
    note(fig, "BH keeps the AVERAGE share of false discoveries near q, and in return finds about twice as many real effects.",
         "It often makes at least one false discovery (high FWER). That is the trade-off FDR control accepts.")
    save(fig, "benjamini_hochberg")
    return res


# ---------------------------------------------------------------- 16.5
def optional_stopping_and_winners_curse():
    fig, axes = figure("Hidden multiple testing: peeking, and picking the winner",
                       "Both inflate false positives or effect sizes even though every single test is 'valid'", 3)
    rng = np.random.default_rng(7)
    R = 20000
    data = rng.normal(0, 1, (R, 200))
    looks = np.arange(20, 201, 20)
    zs = np.cumsum(data, 1)[:, looks - 1] / np.sqrt(looks)
    ps = 2 * stats.norm.sf(np.abs(zs))
    fixed = np.mean(ps[:, -1] <= 0.05)
    peek = np.mean((ps <= 0.05).any(1))

    ax = axes[0]
    shown = 0
    for i in range(R):
        crossed = (ps[i] <= 0.05).any()
        if (crossed and shown < 4) or (not crossed and shown < 9 and i % 3 == 0):
            stop = np.argmax(ps[i] <= 0.05) if crossed else len(looks) - 1
            ax.plot(looks[:stop + 1], ps[i, :stop + 1], "-o", ms=3.5, lw=1.4, color=RED if crossed else LIGHTBLUE, alpha=0.95)
            if crossed:
                ax.plot(looks[stop], ps[i, stop], "*", ms=14, color=RED)
            shown += 1
        if shown >= 13:
            break
    ax.axhline(0.05, color=RED, ls="--", lw=1.3)
    ax.text(200, 0.07, "p = 0.05", color=RED, ha="right")
    ax.set_yscale("log")
    ax.set_ylim(0.005, 1.1)
    ax.set_xticks(looks[::2])
    ax.set_xlabel("observations so far (a look every 20)")
    ax.set_ylabel("p-value at each look (log scale)")
    panel(ax, "A  |  Peeking until p < 0.05", "true effect = 0; red studies stop at ★ and claim success")

    ax = axes[1]
    ax.bar([0, 1], [fixed, peek], color=[BLUE, RED], width=0.55)
    ax.text(0, fixed + 0.006, f"{fixed:.1%}", ha="center", fontsize=15, fontweight="bold", color=BLUE)
    ax.text(1, peek + 0.006, f"{peek:.1%}", ha="center", fontsize=15, fontweight="bold", color=RED)
    ax.axhline(0.05, color=MUTED, ls="--")
    ax.set_xticks([0, 1], ["one test at n = 200\n(planned)", "10 looks, stop at\nfirst p ≤ 0.05"])
    ax.set_ylabel("false positive rate (no real effect)")
    ax.set_ylim(0, 0.25)
    panel(ax, "B  |  Optional stopping", f"{R:,} simulated studies")

    ax = axes[2]
    true = 0.2
    est = true + rng.normal(0, 0.15, 20)
    order = np.argsort(est)
    ax.errorbar(est[order], np.arange(20), xerr=1.96 * 0.15, fmt="o", color=LIGHTBLUE, ecolor=LIGHTBLUE, ms=6)
    ax.errorbar(est[order][-1], 19, xerr=1.96 * 0.15, fmt="o", color=RED, ecolor=RED, ms=9)
    ax.axvline(true, color=GREEN, lw=2)
    ax.set_ylim(-1, 21.5)
    ax.text(true - 0.02, 20.5, f"true effect {true}", color=GREEN, ha="right", fontweight="bold")
    ax.text(est[order][-1], 20.5, f"'winner' {est[order][-1]:.2f}", color=RED, ha="center", fontweight="bold")
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("estimated effect (± 95% CI)")
    panel(ax, "C  |  Winner's curse", "20 noisy estimates of the same effect")
    note(fig, f"Peeking 10 times turns a 5% false positive rate into about {peek:.0%}. Picking the biggest estimate overstates the effect.",
         "Fix the stopping rule (or use a planned sequential design) and report every analysis you ran.")
    save(fig, "optional_stopping_and_winners_curse")
    return fixed, peek, est.max()


if __name__ == "__main__":
    print("16.1 red tests:", multiple_testing_problem())
    print("16.2 FWER, FDR:", fwer_vs_fdr())
    bonferroni_and_holm()
    print("holm", holm(P), "bh", bh(P))
    print("16.4 simulation:", benjamini_hochberg())
    print("16.5 fixed, peek, winner:", optional_stopping_and_winners_curse())

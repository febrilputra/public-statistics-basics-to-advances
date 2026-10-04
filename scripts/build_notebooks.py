"""Build the teaching notebooks from Markdown and named Python lab cells.

Edit <folder_name>.md and scripts/labs/NN.py, then rebuild. This intentionally does
not execute code; use validate_course.py --execute for a fresh-kernel check.
"""
from pathlib import Path
import argparse
import re
import hashlib
import nbformat

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = sorted(p for p in ROOT.iterdir() if p.is_dir() and
                  re.match(r"^(\d\d|AA)_", p.name))
LAB_MARKER = re.compile(r"<!-- lab: ([a-z_]+) -->")

SETUP = '''from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from IPython.display import display

# Works when Jupyter starts in either this chapter or the repository root.
ROOT = next((p for p in [Path.cwd(), *Path.cwd().parents]
             if (p / "scripts" / "build_notebooks.py").is_file()), None)
if ROOT is None:
    raise RuntimeError("Open this notebook inside the cloned course repository.")
FIGURE_DIR = ROOT / __CHAPTER__ / "figure"
FIGURE_DIR.mkdir(exist_ok=True)
plt.rcParams.update({
    "figure.figsize": (9, 4.8), "figure.dpi": 110,
    "font.size": 11, "axes.titlesize": 14, "axes.labelsize": 11,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.prop_cycle": plt.cycler(color=["#087E8B", "#D55E00", "#7251A2", "#4477AA"]),
    "savefig.facecolor": "white", "axes.facecolor": "#FAFBFC",
})
TEAL, ORANGE, PURPLE = "#087E8B", "#D55E00", "#7251A2"

def save_figure(fig, name):
    """Save the exact figure used by Markdown and display it in the notebook."""
    fig.savefig(FIGURE_DIR / f"{name}.png", dpi=180, bbox_inches="tight")
    fig.savefig(FIGURE_DIR / f"{name}.svg", bbox_inches="tight")
    display(fig)
    plt.close(fig)

print("All datasets in this notebook are synthetic teaching examples.")
'''


def lab_cells(path):
    pieces = re.split(r"^# %% ([a-z_]+)\s*$", path.read_text(encoding="utf-8"), flags=re.M)
    if pieces[0].strip():
        raise ValueError(f"Unexpected text before first lab cell in {path}")
    cells = dict(zip(pieces[1::2], (s.strip() for s in pieces[2::2])))
    if len(cells) != len(pieces[1::2]):
        raise ValueError(f"Duplicate lab names: {path}")
    return cells


def build():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapter", help="Only build chapter prefix, e.g. 06 or AA")
    args = parser.parse_args()
    folders = CHAPTERS
    if args.chapter:
        folders = [p for p in folders if p.name.startswith(args.chapter + "_")]
        if not folders:
            parser.error("No chapter matches the requested prefix")
    for folder in folders:
        source = folder / f"{folder.name}.md"
        labs = lab_cells(ROOT / "scripts" / "labs" / f"{folder.name[:2]}.py")
        parts = LAB_MARKER.split(source.read_text(encoding="utf-8"))
        used = parts[1::2]
        if set(used) != set(labs) or len(used) != len(set(used)):
            raise ValueError(f"Lab markers do not match code: {folder.name}")
        cells = [nbformat.v4.new_markdown_cell(parts[0].strip()),
                 nbformat.v4.new_markdown_cell(
                     "**Notebook setup.** Run all cells from top to bottom. Figures are saved "
                     "in this chapter's `figure/` folder. Restart the kernel and run all "
                     "after changing a simulation. See the repository README for installation."),
                 nbformat.v4.new_code_cell(SETUP.replace("__CHAPTER__", repr(folder.name)))]
        for name, prose in zip(parts[1::2], parts[2::2]):
            cells.append(nbformat.v4.new_code_cell(labs[name]))
            if prose.strip():
                cells.append(nbformat.v4.new_markdown_cell(prose.strip()))
        for i, cell in enumerate(cells):
            cell.id = hashlib.sha256(f"{folder.name}:{i}".encode()).hexdigest()[:12]
        nb = nbformat.v4.new_notebook(cells=cells, metadata={
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.12"},
        })
        nbformat.write(nb, folder / f"{folder.name}.ipynb")
        print(f"Built {folder.name}: {len(cells)} cells")


if __name__ == "__main__":
    build()

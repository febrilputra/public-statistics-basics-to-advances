# Statistics: from intuition to reproducible analysis

An original, executable course in statistical foundations, estimation, hypothesis testing, and linear models. Each chapter develops a question in plain language, states the formal model, works through a small numerical example, and uses Python to investigate what happens over repeated samples.

The learning sequence follows the topics in Josh Starmer's *The StatQuest Illustrated Guide to Statistics*. These are independent study notes with new explanations, datasets, exercises, and programmatically generated figures. They are not an official StatQuest resource. See [References](Reference.md) for attribution and [Publication notes](PUBLICATION.md) for source-file and licensing considerations.

## Start here

Read [00 · Introduction](00_Intro/00_Intro.md), then proceed in chapter order. Use [AA · Prerequisites](AA_Prerequisite/AA_Prerequisite.md) whenever notation, calculus, probability, or Python arrays need a refresher. Basic arithmetic is enough to begin. Regression derivations use algebra; the appendix develops the calculus and matrix notation.

For each chapter:

1. Read the overview and follow the worked example by hand.
2. Open the notebook, restart its kernel, and run all cells from top to bottom.
3. Change an effect size, sample size, or assumption and predict the result before rerunning.
4. Attempt the practice problems before reading the worked answers.

The course reaches multiple regression, power planning, multiple testing, ANOVA, and ANCOVA. It builds foundations for further study; it does not attempt a full treatment of time series, Bayesian modeling, causal identification, multilevel models, or generalized linear models.

## Course map

| Chapter | Main questions and experiments | Notes | Executed notebook |
|---|---|---|---|
| 00 · Introduction | Questions, estimands, design, and sampling variation | [Read](00_Intro/00_Intro.md) | [Run](00_Intro/00_Intro.ipynb) |
| 01 · Fundamentals | Population vs sample, variance, SD vs SE, unbiasedness | [Read](01_Fundamental_Concepts_in_Statistics/01_Fundamental_Concepts_in_Statistics.md) | [Run](01_Fundamental_Concepts_in_Statistics/01_Fundamental_Concepts_in_Statistics.ipynb) |
| 02 · Histograms | Counts, probability, density, bin widths, ECDFs | [Read](02_Histogram/02_Histogram.md) | [Run](02_Histogram/02_Histogram.ipynb) |
| 03 · Probability models | PMFs, PDFs, CDFs, common distributions, likelihood | [Read](03_Probability_Models/03_Probability_Models.md) | [Run](03_Probability_Models/03_Probability_Models.ipynb) |
| 04 · Hypothesis testing | Null models, exact randomization, errors, decision rules | [Read](04_Hypothesis_Testing/04_Hypothesis_Testing.md) | [Run](04_Hypothesis_Testing/04_Hypothesis_Testing.ipynb) |
| 05 · P-values and intervals | Tail conventions, calibration, confidence coverage | [Read](05_P-Values_for_Confidence_Quantification/05_P-Values_for_Confidence_Quantification.md) | [Run](05_P-Values_for_Confidence_Quantification/05_P-Values_for_Confidence_Quantification.ipynb) |
| 06 · Linear regression | Least squares, inference, prediction intervals, diagnostics | [Read](06_Linear_Regression/06_Linear_Regression.md) | [Run](06_Linear_Regression/06_Linear_Regression.ipynb) |
| 07 · Multiple regression | Conditional effects, indicators, interactions, overfitting | [Read](07_Multiple_Regression/07_Multiple_Regression.md) | [Run](07_Multiple_Regression/07_Multiple_Regression.ipynb) |
| 08 · t-tests | One-sample, Welch, pooled, paired, regression equivalence | [Read](08_T-test_for_Testing_the_Differences/08_T-test_for_Testing_the_Differences.md) | [Run](08_T-test_for_Testing_the_Differences/08_T-test_for_Testing_the_Differences.ipynb) |
| 09 · Power | Noncentral t, sample size, sensitivity, simulation | [Read](09_Power_and_Power_Analysis/09_Power_and_Power_Analysis.md) | [Run](09_Power_and_Power_Analysis/09_Power_and_Power_Analysis.ipynb) |
| 10 · P-value pitfalls | FWER vs FDR, Holm, BH, selection, optional stopping | [Read](10_P-Values_Pitfalls/10_P-Values_Pitfalls.md) | [Run](10_P-Values_Pitfalls/10_P-Values_Pitfalls.ipynb) |
| 11 · ANOVA and ANCOVA | Decomposition, contrasts, adjusted comparisons, interaction | [Read](11_Anova_and_Ancova/11_Anova_and_Ancova.md) | [Run](11_Anova_and_Ancova/11_Anova_and_Ancova.ipynb) |
| AA · Prerequisites | Probability, Bayes, CLT, derivatives, OLS, arrays | [Read](AA_Prerequisite/AA_Prerequisite.md) | [Run](AA_Prerequisite/AA_Prerequisite.ipynb) |

Every chapter includes a Mermaid overview, original examples, explicit assumptions, exercises, and worked answers. Notebooks contain the complete chapter prose with interleaved code. The same code saves each figure as a PNG for the notes and an SVG for sharp scaling. No book PDF, external dataset, account, API key, or network access is needed to run the course after dependencies are installed.

## Run locally

The validated environment uses Python 3.12.14; install Python 3.12 and the pinned dependencies in [requirements.txt](requirements.txt). From the repository root on Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name statistics-course --display-name "Statistics course (.venv)"
.\.venv\Scripts\python.exe -m jupyterlab
```

On macOS or Linux:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name statistics-course --display-name "Statistics course (.venv)"
.venv/bin/python -m jupyterlab
```

Open a chapter's `<folder_name>.ipynb` and select **Statistics course (.venv)** as its kernel. Jupyter can start in the repository root or a chapter directory; the setup cell finds the root automatically. Keep the directory structure intact. The already executed notebooks and PNGs can also be read without installing Python.

GitHub renders Mermaid diagrams in Markdown. Some notebook viewers display their source instead; each chapter also describes the route in prose. LaTeX equations use standard Markdown math delimiters. Figure links are relative to the chapter folder.

All data are synthetic and chosen for learning. Simulation estimates fluctuate around theoretical values; seeded generators make each experiment reproducible in the specified environment. Small floating-point and rendering differences across platforms are expected.

## Rebuild and verify

The authored files are each chapter's `<folder_name>.md` and its corresponding [Python lab source](scripts/labs). A marker such as `<!-- lab: least_squares -->` places a named code cell from `scripts/labs/06.py` after the relevant explanation. This keeps the notes and notebook synchronized.

After changing prose or a lab, rebuild and execute:

```powershell
.\.venv\Scripts\python.exe scripts/build_notebooks.py
.\.venv\Scripts\python.exe scripts/validate_course.py --execute
```

Replace the Python path with `.venv/bin/python` on macOS or Linux. For a focused edit, both scripts accept a chapter prefix:

```powershell
.\.venv\Scripts\python.exe scripts/build_notebooks.py --chapter 06
.\.venv\Scripts\python.exe scripts/validate_course.py --execute --chapter 06
```

Building overwrites generated notebooks and clears their previous outputs. Execute afterward to restore outputs and regenerate figures. Make persistent changes in the Markdown and lab source, rather than editing only the generated notebook. Running a notebook interactively also regenerates that chapter's figures.

The validator checks notebook structure, executed cells, errors, synchronization with notes, local links, and figure files. The lab cells additionally check important scientific results: exact probabilities, variance formulas, regression identities, library agreement, sample-size calculations, and simulation agreement where appropriate. `--execute` runs each notebook in a separate fresh kernel using the invoking Python environment. Without it, validation checks saved outputs and files. CI rebuilds and executes the same course on Python 3.12.

## Statistical conventions

- A p-value is a tail probability under a specified null model, not the probability that the null hypothesis is true.
- Confidence levels describe repeated-sampling coverage; effect sizes and intervals accompany decisions.
- SD describes variation in observations; SE describes variation in an estimator.
- A density height is not a probability; probability is mass or area.
- Independent-observation likelihood contributions multiply, and log-likelihood contributions add.
- Inference, prediction, and causality ask different questions. Assumptions and study design matter for each.
- Model comparisons use the same observations, explicit parameter counts, and appropriate variance assumptions.

The notes identify where finite-sample formulas are exact, where approximations are used, and where the analysis extends the primary reading. Treat the deliberately small examples as opportunities to understand the calculation, not as evidence for decisions about real systems.

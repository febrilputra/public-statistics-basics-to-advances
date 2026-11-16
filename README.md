# Statistics: From Basics to Advanced

My statistics notes in one place, from the first definitions to multiple regression, power analysis, multiple testing and ANOVA. Every lesson is its own Markdown note, named `chapter-lesson-title.md`, written in my own words with worked examples, re-checked calculations and illustrated figures.

- **Chapters 1–13 (basics)** follow [The Organic Chemistry Tutor's statistics course](https://www.video-tutor.net/statistic.html). Each note covers one video and links to it. Where a video contains a slip, the note says so and gives the corrected value. Each chapter also has a `pdf_version/` folder and, from Chapter 5, a `handwritten_note/` folder.
- **Chapters 14–18 (advanced)** cover topics the course above does not: multiple regression, power and sample size, p-value pitfalls and multiple testing, ANOVA and ANCOVA, and a mathematical and Python prerequisites toolbox. They follow the topic order of Josh Starmer's *The StatQuest Illustrated Guide to Statistics*, with new explanations, made-up teaching data, and figures drawn by each chapter's `figures/make_figures.py`.

The videos and website belong to The Organic Chemistry Tutor, and *The StatQuest Illustrated Guide to Statistics* belongs to Josh Starmer. These notes are a personal study companion, not affiliated with or endorsed by either. See [References](Reference.md) for attribution and [Publication notes](PUBLICATION.md) for licensing considerations.

## How each lesson is laid out

1. **The big picture**: why the topic matters and how it connects to earlier lessons, with a large illustrated figure.
2. **Goal** and **Formulas**: what you'll be able to do and the formulas you need.
3. **Example**: a worked example, step by step, with every calculation shown.
4. **Doing it in Excel**: the matching spreadsheet functions.
5. **Your turn** (Chapters 14–18): a practice problem with its answer.
6. **Key takeaways**.

Lesson numbers in the text (e.g. "Lesson 13.1") point to other notes, so you can jump back to a tool when you need it. Chapter 18 is a reference chapter for the maths and code behind Chapters 13–17.

## Lessons

### Chapter 1 - Introduction to Statistics

- [Lesson 1.1 - Introduction to Statistics](01_introduction_to_statistics/1-1-introduction_to_statistics.md)
- [Lesson 1.2 - Descriptive Statistics vs Inferential Statistics](01_introduction_to_statistics/1-2-descriptive_statistics_vs_inferential_statistics.md)
- [Lesson 1.3 - Quantitative vs Qualitative Data](01_introduction_to_statistics/1-3-quantitative_vs_qualitative_data.md)
- [Lesson 1.4 - Statistic Vs Parameter and Population vs Sample](01_introduction_to_statistics/1-4-statistic_vs_parameter_and_population_vs_sample.md)
- [Lesson 1.5 - Scales of Measurement](01_introduction_to_statistics/1-5-scales_of_measurement.md)

### Chapter 2 - Graphs and Tables

- [Lesson 2.1 - How to Make a Simple Frequency Table](02_graphs_and_tables/2-1-how_to_make_a_simple_frequency_table.md)
- [Lesson 2.2 - Relative Frequency Distribution Table](02_graphs_and_tables/2-2-relative_frequency_distribution_table.md)
- [Lesson 2.3 - Cumulative Relative Frequency Table](02_graphs_and_tables/2-3-cumulative_relative_frequency_table.md)
- [Lesson 2.4 - Dot Plots and Frequency Tables](02_graphs_and_tables/2-4-dot_plots_and_frequency_tables.md)
- [Lesson 2.5 - Line Plots](02_graphs_and_tables/2-5-line_plots.md)
- [Lesson 2.6 - Stem and Leaf Plots](02_graphs_and_tables/2-6-stem_and_leaf_plots.md)
- [Lesson 2.7 - Side by Side Stem and Leaf Plots](02_graphs_and_tables/2-7-side_by_side_stem_and_leaf_plots.md)
- [Lesson 2.8 - How to Make a Histogram Using a Frequency Distribution Table](02_graphs_and_tables/2-8-how_to_make_a_histogram_using_a_frequency_distribution_table.md)
- [Lesson 2.9 - How to Make a Frequency Polygon](02_graphs_and_tables/2-9-how_to_make_a_frequency_polygon.md)

### Chapter 3 - Central Tendency

- [Lesson 3.1 - Statistics Formulas and Equations](03_central_tendency/3-1-statistics_formulas_and_equations.md)
- [Lesson 3.2 - Mean, Median, Mode, and Range](03_central_tendency/3-2-mean_median_mode_and_range.md)
- [Lesson 3.3 - How to Calculate the Median Using a Formula](03_central_tendency/3-3-how_to_calculate_the_median_using_a_formula.md)
- [Lesson 3.4 - How to Calculate the Range, Midrange, and Coefficient of Range](03_central_tendency/3-4-how_to_calculate_the_range_midrange_and_coefficient_of_range.md)
- [Lesson 3.5 - How to Find the Missing Value Given the Mean](03_central_tendency/3-5-how_to_find_the_missing_value_given_the_mean.md)
- [Lesson 3.6 - How to Find the Weighted Mean](03_central_tendency/3-6-how_to_find_the_weighted_mean.md)
- [Lesson 3.7 - The Mean Formulas](03_central_tendency/3-7-the_mean_formulas.md)
- [Lesson 3.8 - Formulas of Statistics in Excel](03_central_tendency/3-8-formulas_of_statistics_in_excel.md)
- [Lesson 3.9 - Sample Mean and Population Mean](03_central_tendency/3-9-sample_mean_and_population_mean.md)
- [Lesson 3.10 - Averages and Uncertainty Calculations](03_central_tendency/3-10-averages_and_uncertainty_calculations.md)
- [Lesson 3.11 - How to Calculate the Standard Deviation](03_central_tendency/3-11-how_to_calculate_the_standard_deviation.md)
- [Lesson 3.12 - Standard Deviation and Coefficient of Variation](03_central_tendency/3-12-standard_deviation_and_coefficient_of_variation.md)
- [Lesson 3.13 - How to Calculate Variance](03_central_tendency/3-13-how_to_calculate_variance.md)
- [Lesson 3.14 - Mean, Median, and Mode of Grouped Data](03_central_tendency/3-14-mean_median_and_mode_of_grouped_data.md)
- [Lesson 3.15 - Standard Deviation of Grouped Data](03_central_tendency/3-15-standard_deviation_of_grouped_data.md)
- [Lesson 3.16 - How to Calculate the Median of Grouped Data](03_central_tendency/3-16-how_to_calculate_the_median_of_grouped_data.md)
- [Lesson 3.17 - How to Calculate the Mode of Grouped Data](03_central_tendency/3-17-how_to_calculate_the_mode_of_grouped_data.md)
- [Lesson 3.18 - Mean Absolute Deviation](03_central_tendency/3-18-mean_absolute_deviation.md)
- [Lesson 3.19 - How to Calculate the Average Deviation](03_central_tendency/3-19-how_to_calculate_the_average_deviation.md)

### Chapter 4 - Measures of Position

- [Lesson 4.1 - Quartiles, Deciles, and Percentiles](04_measures_of_position/4-1-quartiles_deciles_and_percentiles.md)
- [Lesson 4.2 - How to Find the Interquartile Range](04_measures_of_position/4-2-how_to_find_the_interquartile_range.md)
- [Lesson 4.3 - The Coefficient of Quartile Deviation](04_measures_of_position/4-3-the_coefficient_of_quartile_deviation.md)
- [Lesson 4.4 - How to Make Box and Whisker Plots](04_measures_of_position/4-4-how_to_make_box_and_whisker_plots.md)
- [Lesson 4.5 - Skewness with Box Plots](04_measures_of_position/4-5-skewness_with_box_plots.md)

### Chapter 5 - Introduction to Probability

- [Lesson 5.1 - Introduction to Probability](05_introduction_to_probability/5-1-introduction_to_probability.md)
- [Lesson 5.2 - Probability Formulas](05_introduction_to_probability/5-2-probability_formulas.md)
- [Lesson 5.3 - Probability of Complementary Events](05_introduction_to_probability/5-3-probability_of_complementary_events.md)
- [Lesson 5.4 - Conditional Probability with Venn Diagrams and Contingency Tables](05_introduction_to_probability/5-4-conditional_probability_with_venn_diagrams_and_contingency_tables.md)
- [Lesson 5.5 - Probability of Independent and Dependent Events](05_introduction_to_probability/5-5-probability_of_independent_and_dependent_events.md)
- [Lesson 5.6 - Probability of Mutually Exclusive Events with Venn Diagrams](05_introduction_to_probability/5-6-probability_of_mutually_exclusive_events_with_venn_diagrams.md)
- [Lesson 5.7 - Addition Rule and Multiplication Rule](05_introduction_to_probability/5-7-addition_rule_and_multiplication_rule.md)
- [Lesson 5.8 - Compound Probability of Independent Events](05_introduction_to_probability/5-8-compound_probability_of_independent_events.md)
- [Lesson 5.9 - How to Calculate the Expected Value](05_introduction_to_probability/5-9-how_to_calculate_the_expected_value.md)
- [Lesson 5.10 - Probability Tree Diagrams](05_introduction_to_probability/5-10-probability_tree_diagrams.md)
- [Lesson 5.11 - Bayes Theorem of Probability with Tree Diagrams](05_introduction_to_probability/5-11-bayes_theorem_of_probability_with_tree_diagrams.md)

### Chapter 6 - Discrete Probability Distributions

- [Lesson 6.1 - Probability Distribution Formulas](06_discrete_probability_distributions/6-1-probability_distribution_formulas.md)
- [Lesson 6.2 - Finding the Probability of a Binomial Distribution](06_discrete_probability_distributions/6-2-finding_the_probability_of_a_binomial_distribution.md)
- [Lesson 6.3 - The Geometric Distribution](06_discrete_probability_distributions/6-3-the_geometric_distribution.md)
- [Lesson 6.4 - The Poisson Distribution](06_discrete_probability_distributions/6-4-the_poisson_distribution.md)
- [Lesson 6.5 - Continuous vs Discrete Data](06_discrete_probability_distributions/6-5-continuous_vs_discrete_data.md)

### Chapter 7 - Continuous Distributions

- [Lesson 7.1 - Continuous Probability Distributions](07_continuous_distributions/7-1-continuous_probability_distributions.md)
- [Lesson 7.2 - Cumulative Distribution Functions and Probability Density Functions](07_continuous_distributions/7-2-cumulative_distribution_functions_and_probability_density_functions.md)
- [Lesson 7.3 - Probability of a Uniform Distribution](07_continuous_distributions/7-3-probability_of_a_uniform_distribution.md)
- [Lesson 7.4 - Probability of an Exponential Distribution](07_continuous_distributions/7-4-probability_of_an_exponential_distribution.md)

### Chapter 8 - Normal Probability Distributions

- [Lesson 8.1 - Standard Normal Distributions](08_normal_probability_distributions/8-1-standard_normal_distributions.md)
- [Lesson 8.2 - Standard Normal Distribution with Calculus](08_normal_probability_distributions/8-2-standard_normal_distribution_with_calculus.md)
- [Lesson 8.3 - Law of Large Numbers](08_normal_probability_distributions/8-3-law_of_large_numbers.md)
- [Lesson 8.4 - The Central Limit Theorem](08_normal_probability_distributions/8-4-the_central_limit_theorem.md)
- [Lesson 8.5 - The Standard Error of the Mean](08_normal_probability_distributions/8-5-the_standard_error_of_the_mean.md)

### Chapter 9 - Confidence Intervals

- [Lesson 9.1 - Z-Scores, Confidence Intervals, and Margin of Error](09_confidence_intervals/9-1-z_scores_confidence_intervals_and_margin_of_error.md)
- [Lesson 9.2 - How to Find the Z-score Given the Confidence Intervals](09_confidence_intervals/9-2-how_to_find_the_z_score_given_the_confidence_intervals.md)
- [Lesson 9.3 - Student's T-Distribution](09_confidence_intervals/9-3-students_t_distribution.md)
- [Lesson 9.4 - Finding a Confidence Interval of a Population Proportion](09_confidence_intervals/9-4-finding_a_confidence_interval_of_a_population_proportion.md)
- [Lesson 9.5 - How to Calculate the Sample Size](09_confidence_intervals/9-5-how_to_calculate_the_sample_size.md)
- [Lesson 9.6 - Chebyshev's Theorem](09_confidence_intervals/9-6-chebyshevs_theorem.md)

### Chapter 10 - Hypothesis Testing - 1 Sample

- [Lesson 10.1 - Hypothesis Testing - Null and Alternative Hypotheses](10_hypothesis_testing-1_sample/10-1-hypothesis_testing_null_and_alternative_hypotheses.md)
- [Lesson 10.2 - How to Identify Type I and Type II Errors](10_hypothesis_testing-1_sample/10-2-how_to_identify_type_i_and_type_ii_errors.md)
- [Lesson 10.3 - One Tailed and Two Tailed Tests](10_hypothesis_testing-1_sample/10-3-one_tailed_and_two_tailed_tests.md)
- [Lesson 10.4 - Test Statistic for Means and Population Proportions](10_hypothesis_testing-1_sample/10-4-test_statistic_for_means_and_population_proportions.md)
- [Lesson 10.5 - Hypothesis Testing Problems - Z Test and T Statistics](10_hypothesis_testing-1_sample/10-5-hypothesis_testing_problems_z_test_and_t_statistics.md)
- [Lesson 10.6 - P-Value Method for Hypothesis Testing](10_hypothesis_testing-1_sample/10-6-p_value_method_for_hypothesis_testing.md)
- [Lesson 10.7 - Hypothesis Testing - Solving Problems with Proportions](10_hypothesis_testing-1_sample/10-7-hypothesis_testing_solving_problems_with_proportions.md)

### Chapter 11 - Hypothesis Testing - 2 Samples

- [Lesson 11.1 - Hypothesis Testing - Difference of Two Means](11_hypothesis_testing-2_samples/11-1-hypothesis_testing_difference_of_two_means.md)
- [Lesson 11.2 - How to Find Cohen's D to Determine the Effect Size](11_hypothesis_testing-2_samples/11-2-how_to_find_cohens_d_to_determine_the_effect_size.md)
- [Lesson 11.3 - Hypothesis Testing with Two Proportions](11_hypothesis_testing-2_samples/11-3-hypothesis_testing_with_two_proportions.md)
- [Lesson 11.4 - Matched or Paired Samples](11_hypothesis_testing-2_samples/11-4-matched_or_paired_samples.md)

### Chapter 12 - The Chi-Square Distribution

- [Lesson 12.1 - The Chi Square Test](12_the_chi-square_distribution/12-1-the_chi_square_test.md)
- [Lesson 12.2 - The Chi Square Distribution Test of a Single Standard Deviation](12_the_chi-square_distribution/12-2-the_chi_square_distribution_test_of_a_single_standard_deviation.md)
- [Lesson 12.3 - Tests of Independence Using Chi-Square Distribution](12_the_chi-square_distribution/12-3-tests_of_independence_using_chi_square_distribution.md)

### Chapter 13 - Regression & Correlation

- [Lesson 13.1 - The Least Squares Method](13_regression_and_correlation/13-1-the_least_squares_method.md)
- [Lesson 13.2 - How to Calculate the Covariance](13_regression_and_correlation/13-2-how_to_calculate_the_covariance.md)
- [Lesson 13.3 - Correlation Coefficient](13_regression_and_correlation/13-3-correlation_coefficient.md)
- [Lesson 13.4 - Calculating the Correlation Coefficient Using the Covariance Formula](13_regression_and_correlation/13-4-calculating_the_correlation_coefficient_using_the_covariance_formula.md)

### Chapter 14 - Multiple Regression

- [Lesson 14.1 - Introduction to Multiple Regression](14_multiple_regression/14-1-introduction_to_multiple_regression.md)
- [Lesson 14.2 - Dummy Variables for Categories](14_multiple_regression/14-2-dummy_variables_for_categories.md)
- [Lesson 14.3 - Adjustment and Interaction Terms](14_multiple_regression/14-3-adjustment_and_interaction_terms.md)
- [Lesson 14.4 - Comparing Nested Models with the F-Test](14_multiple_regression/14-4-comparing_nested_models_with_the_f_test.md)
- [Lesson 14.5 - R², Adjusted R², and Overfitting](14_multiple_regression/14-5-r_squared_adjusted_r_squared_and_overfitting.md)
- [Lesson 14.6 - Multicollinearity and the VIF](14_multiple_regression/14-6-multicollinearity_and_vif.md)

### Chapter 15 - Power and Power Analysis

- [Lesson 15.1 - What Is Statistical Power?](15_power_and_power_analysis/15-1-what_is_statistical_power.md)
- [Lesson 15.2 - Effect Size for Planning](15_power_and_power_analysis/15-2-effect_size_for_planning.md)
- [Lesson 15.3 - What Affects Power?](15_power_and_power_analysis/15-3-what_affects_power.md)
- [Lesson 15.4 - Sample Size for Comparing Two Means](15_power_and_power_analysis/15-4-sample_size_for_comparing_two_means.md)
- [Lesson 15.5 - Checking Power by Simulation (and Power Mistakes)](15_power_and_power_analysis/15-5-checking_power_by_simulation.md)

### Chapter 16 - P-Value Pitfalls and Multiple Testing

- [Lesson 16.1 - The Multiple Testing Problem](16_p_value_pitfalls/16-1-the_multiple_testing_problem.md)
- [Lesson 16.2 - FWER and FDR: Two Ways to Count Mistakes](16_p_value_pitfalls/16-2-fwer_and_fdr.md)
- [Lesson 16.3 - Bonferroni and Holm Corrections](16_p_value_pitfalls/16-3-bonferroni_and_holm_corrections.md)
- [Lesson 16.4 - The Benjamini–Hochberg Procedure (FDR)](16_p_value_pitfalls/16-4-benjamini_hochberg_false_discovery_rate.md)
- [Lesson 16.5 - Selection, Optional Stopping, and the Winner's Curse](16_p_value_pitfalls/16-5-selection_optional_stopping_and_the_winners_curse.md)

### Chapter 17 - ANOVA and ANCOVA

- [Lesson 17.1 - One-Way ANOVA and Sums of Squares](17_anova_and_ancova/17-1-one_way_anova_and_sums_of_squares.md)
- [Lesson 17.2 - The ANOVA Table and Effect Size](17_anova_and_ancova/17-2-the_anova_table_and_effect_size.md)
- [Lesson 17.3 - Post-Hoc Comparisons: Which Groups Differ?](17_anova_and_ancova/17-3-post_hoc_comparisons.md)
- [Lesson 17.4 - ANCOVA: Adjusting for a Covariate](17_anova_and_ancova/17-4-ancova_adjusting_for_a_covariate.md)
- [Lesson 17.5 - ANCOVA Assumptions and Interactions](17_anova_and_ancova/17-5-ancova_assumptions_and_interactions.md)

### Chapter 18 - Mathematical and Python Prerequisites

- [Lesson 18.1 - Sums, Products, and Logarithms](18_prerequisites/18-1-sums_products_and_logarithms.md)
- [Lesson 18.2 - Probability Rules and Bayes' Theorem](18_prerequisites/18-2-probability_rules_and_bayes_theorem.md)
- [Lesson 18.3 - Expectation, Variance, and Covariance](18_prerequisites/18-3-expectation_variance_and_covariance.md)
- [Lesson 18.4 - The Law of Large Numbers and the Central Limit Theorem](18_prerequisites/18-4-law_of_large_numbers_and_central_limit_theorem.md)
- [Lesson 18.5 - Derivatives and the Chain Rule](18_prerequisites/18-5-derivatives_and_the_chain_rule.md)
- [Lesson 18.6 - Deriving the Least Squares Line](18_prerequisites/18-6-deriving_the_least_squares_line.md)
- [Lesson 18.7 - Matrix Notation and R²](18_prerequisites/18-7-matrix_notation_and_r_squared.md)
- [Lesson 18.8 - Arrays and Reproducible Experiments in Python](18_prerequisites/18-8-arrays_and_reproducible_experiments.md)

## Formula sheet

- [Formula sheet (PDF)](formula_sheet/00_febril/formula_sheet.pdf) · [HTML](formula_sheet/00_febril/formula_sheet.html): every formula from Chapters 1–18, each with a small sketch of what it means, plus a "Which formula do I need?" table.

## Rebuilding figures and PDFs

The figures for Chapters 14–18 are drawn by one script per chapter. With Python 3.12 and the packages in [requirements.txt](requirements.txt):

```bash
python -m pip install -r requirements.txt
python 14_multiple_regression/figures/make_figures.py
```

Each script writes PNG files (used in the notes) and SVG files (for sharp scaling) next to itself. Random examples use fixed seeds, so the numbers quoted in the lessons come out the same.

Other tools (they need Perl and Google Chrome, and an internet connection for the maths fonts):

- `perl formula_sheet/00_febril/make_formula_sheet.pl` rebuilds the formula sheet HTML and PDF.
- `perl scripts/export_markdown.pl` exports every lesson to its chapter's `pdf_version/` folder. Add a folder name, e.g. `perl scripts/export_markdown.pl 14_multiple_regression`, for one chapter.
- `python scripts/check_links.py` checks that every local link and image in the notes exists. GitHub Actions runs it, together with the figure scripts, on every push.

## Archived chapters

An earlier version of this repository was a set of single-file chapters with Jupyter notebooks. The chapters whose topics are now covered by Chapters 1–13 (introduction, fundamentals, histograms, probability models, hypothesis testing, p-values and intervals, simple regression, t-tests) are kept unchanged in [old_chapters/](old_chapters/README.md) for reference.

## Statistical conventions used throughout

- A p-value is a tail probability under a specified null model, not the probability that the null hypothesis is true.
- Confidence levels describe repeated-sampling coverage. Report effect sizes and intervals, not only decisions.
- SD describes variation in observations. SE describes variation in an estimate.
- A density height is not a probability. Probability is area.
- Inference, prediction and causality ask different questions. Assumptions and study design matter for each.
- Model comparisons use the same observations, explicit parameter counts and appropriate variance assumptions.

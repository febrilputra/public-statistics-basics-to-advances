# 07 · Multiple regression and conditional comparisons

Multiple regression estimates a response using several predictors together. Its coefficients describe conditional relationships within the specified model. Adding predictors improves or preserves training fit, but it can make estimates unstable and future predictions worse.

```mermaid
flowchart TD
    A[Build a design matrix] --> B[Estimate coefficients jointly]
    B --> C[Interpret conditional effects]
    C --> D[Compare nested models]
    D --> E[Check collinearity and residuals]
    E --> F[Evaluate new-data prediction]
```

**Learning route:** model → coding → fitting → nested tests → stability → validation. Prerequisites: [simple regression](../06_Linear_Regression/06_Linear_Regression.md). Matrix notation is introduced in [AA](../AA_Prerequisite/AA_Prerequisite.md).

## 1. From a line to a plane and beyond

With $p$ predictor columns and an intercept,

$$Y_i=\beta_0+\beta_1x_{i1}+\cdots+\beta_px_{ip}+\varepsilon_i.$$

Two numerical predictors define a plane for the conditional mean. More predictors require no new fitting principle: minimize the squared residuals. In matrix notation, $\mathbf y=X\boldsymbol\beta+\boldsymbol\varepsilon$, where the first column of $X$ is ones. Let $K=p+1$ count **all** coefficients, including the intercept.

If $X$ has full column rank, the OLS solution is theoretically $(X^TX)^{-1}X^T\mathbf y$. In numerical work, use a least-squares solver based on QR or singular-value decomposition rather than explicitly computing an inverse. Full column rank means no predictor column can be exactly reconstructed from the others.

Counting observations is not enough. Even with 1,000 rows, including both mass in kilograms and mass in grams creates exact dependence. Unique coefficients require rank $K$; estimating classical residual variance also requires $n>K$. Adequate practical sample size usually requires considerably more than the minimum.

## 2. An original worked example with a categorical predictor

A workshop records preparation time for batches. Let $x$ be batch size centered at five items, and $z$ indicate a protective coating: 0 for uncoated and 1 for coated. Use this deliberately balanced teaching dataset:

| Batch size | Centered $x$ | Coating $z$ | Times, minutes |
|---:|---:|---:|---|
| 4 | -1 | 0 | 7, 9 |
| 4 | -1 | 1 | 10, 12 |
| 6 | 1 | 0 | 11, 13 |
| 6 | 1 | 1 | 14, 16 |

Fit $Y=\beta_0+\beta_1x+\beta_2z+\varepsilon$. The fitted equation is

$$\hat y=10+2x+3z.$$

For batches of the same size, coated batches have a fitted mean three minutes higher. Within either coating category, an extra item is associated with two additional minutes. The intercept is ten minutes for an uncoated batch of five items. Centering makes this a meaningful reference rather than a hypothetical batch of zero items.

Residuals are $-1,+1$ in each row of the table, so $RSS_F=8$. There are $n=8$ observations and $K_F=3$ coefficients, giving residual variance estimate $8/(8-3)=1.6$.

![Conditional fitted lines for coated and uncoated batches](figure/conditional_fit.png)

<!-- lab: conditional_fit -->

For a three-category predictor, use two indicator columns plus the intercept. Including all three indicators and an intercept creates the identity “intercept = sum of indicators” and loses rank. Changing the reference category changes coefficient labels and meanings, but not the fitted values of the same model.

## 3. “Holding other variables fixed” needs a model

In the additive model above, changing $x$ by one with $z$ fixed changes the fitted mean by $\beta_1$. This is a conditional association. It differs from a one-predictor regression when the omitted predictor is associated with both the included predictor and the response.

Adjustment is not automatically causal. An omitted common cause can leave confounding; conditioning on variables caused by treatment or on selection mechanisms can introduce other biases. Choose variables using the question and data-generating process, not just a rule that more adjustment is always better.

An **interaction** allows one relationship to vary with another predictor:

$$E[Y\mid x,z]=\beta_0+\beta_1x+\beta_2z+\beta_3xz.$$

Now the slope is $\beta_1$ for $z=0$ and $\beta_1+\beta_3$ for $z=1$. The group difference at a specified $x$ is $\beta_2+\beta_3x$. There is no single constant group effect. Keep the lower-order terms when adding an interaction unless the scientific model specifically justifies a constraint.

The notebook evaluates an example equation $10+2x+3z+xz$ to show how the group difference changes from 2 to 3 to 4 minutes as centered $x$ changes from $-1$ to 0 to 1. This is a specified illustration, not an interaction inferred from the eight-row additive dataset.

<!-- lab: interaction -->

## 4. Compare nested models on identical observations

A reduced model is **nested** in a full model when setting selected full-model coefficients to zero produces the reduced model. Refit both models separately. Do not delete a term from a fitted full-model equation while retaining all its other coefficients; the remaining optimum can change.

For nested OLS models fit to the same response and rows, with $K_R<K_F$,

$$F=\frac{(RSS_R-RSS_F)/(K_F-K_R)}{RSS_F/(n-K_F)}.$$

Under the classical independent, homoscedastic normal-error model and the null that all added coefficients are zero, this has an $F_{K_F-K_R,n-K_F}$ distribution. The numerator measures improvement per added coefficient. The denominator estimates unexplained error variance from the full model.

In our example, the reduced model excludes coating. Its RSS is 26, compared with 8 for the full model. Therefore,

$$F=\frac{(26-8)/(3-2)}{8/(8-3)}=11.25,$$

with degrees of freedom $(1,5)$ and p-value about 0.020. This tests the coating coefficient conditional on batch size. With a single added coefficient, $F=t^2$ under the same variance assumptions.

<!-- lab: nested_models -->

The **overall** F-test compares all predictor coefficients to zero against an intercept-only model. It can reject even when some individual coefficients are imprecise. Non-nested formulas, different response transformations, or different rows due to missing data do not meet the conditions for this simple RSS comparison.

## 5. $R^2$ and adjusted $R^2$

Because the full model can set extra coefficients to zero, its minimized training RSS cannot increase. Consequently training $R^2$ cannot decrease. Random noise predictors can absorb chance features of the training data even when they have no real predictive relationship.

For an intercept model, adjusted $R^2$ is

$$\bar R^2=1-\frac{RSS/(n-K)}{TSS/(n-1)}.$$

It compares residual variation per remaining degree of freedom with the mean-only estimate. In our example, $TSS=58$, $R^2=1-8/58\approx0.8621$, and adjusted $R^2\approx0.8069$. It may decrease when unnecessary predictors are added and may be negative. It is a penalized training summary, not a substitute for evaluating new data or a guarantee of selecting the true model.

![Training and test error after adding irrelevant predictors](figure/overfitting.png)

<!-- lab: overfitting -->

The simulation has two true predictors. Extra columns are independent noise, and the test sample is generated separately. Training error decreases as noise variables are added, while test error can worsen. A particular test curve can wobble; the lesson is to measure generalization rather than infer it from training fit. If model choices use a validation set, keep a final test set untouched or use an appropriate nested validation design.

## 6. Collinearity and coefficient uncertainty

If two predictors move almost together, the data contain few comparisons where one changes while the other stays fixed. Their separate slopes become hard to identify even if their combined prediction is accurate. Coefficients may be large, uncertain, or sensitive to small data changes.

The **variance inflation factor** for predictor $j$ is $VIF_j=1/(1-R_j^2)$, where $R_j^2$ comes from regressing that predictor on the other predictors with an intercept. It describes variance inflation relative to an orthogonal design under the homoscedastic model. A high VIF is a diagnostic, not a universal instruction to delete a predictor.

The notebook contrasts an ordinary design with one containing a nearly duplicated predictor, then checks the exact rank deficiency created by a perfect duplicate. Centering can aid interpretation and reduce some numerical issues; it does not separate truly redundant measurements. Ridge regression is one possible predictive extension, but changes the estimation method and is beyond this chapter.

<!-- lab: collinearity -->

Continue checking residuals, leverage, influence, and collection-order dependence as in Chapter 6. A two-dimensional residual plot is still useful when a high-dimensional fitted surface cannot be shown directly.

## 7. Practice

1. A reduced model has RSS 120 and $K_R=2$. A full model on the same 30 rows has RSS 90 and $K_F=4$. Calculate the partial F statistic and its degrees of freedom.
2. Interpret $\hat y=5+2x-3z+4xz$ at $z=0$ and $z=1$.
3. An analyst adds ten independent random columns and sees training $R^2$ increase. Does that establish a better model?
4. Why can including Celsius and Fahrenheit temperatures together with an intercept make coefficients nonunique?
5. What changes in the eight-row example if the reference group changes from uncoated to coated?

## 8. Worked answers

1. $F=[(120-90)/2]/[90/26]=13/3\approx4.333$, with $(2,26)$ degrees of freedom. The upper-tail probability is calculated in the notebook.
2. At $z=0$, $\hat y=5+2x$. At $z=1$, $\hat y=2+6x$. The group difference is $-3+4x$, so “the effect of $z$ is -3” is only correct at $x=0$.
3. No. This is expected from greater fitting flexibility. Examine model purpose, uncertainty, assumptions, and independent validation.
4. $F=32+1.8C$ is an exact linear combination of the intercept and Celsius column. The design matrix cannot have full column rank.
5. With $w=1-z$, the equation becomes $\hat y=13+2x-3w$. Predictions remain identical; the intercept and group contrast now use coated batches as reference.

<!-- lab: practice -->

## References and next step

Reading connection: Starmer (2026), Chapter 7, [SQ](../Reference.md#sq-statquest). Matrix fitting: [NumPy least squares](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html). Model comparisons: [statsmodels compare_f_test](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.compare_f_test.html). Conditional interpretation, interactions, and held-out experiments extend the reading.

Next: [08 · t-tests](../08_T-test_for_Testing_the_Differences/08_T-test_for_Testing_the_Differences.md).

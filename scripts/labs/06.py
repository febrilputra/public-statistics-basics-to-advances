# %% least_squares
import statsmodels.api as sm
x = np.array([1,2,3,4,5],dtype=float)
y = np.array([2,4,5,4,5],dtype=float)
sxx = np.sum((x-x.mean())**2)
sxy = np.sum((x-x.mean())*(y-y.mean()))
slope = sxy/sxx
intercept = y.mean()-slope*x.mean()
fitted = intercept+slope*x
residuals = y-fitted
rss = np.sum(residuals**2)
tss = np.sum((y-y.mean())**2)
fit = sm.OLS(y,sm.add_constant(x)).fit()
assert np.allclose(fit.params,[2.2,.6]) and np.isclose(rss,2.4)
display(pd.DataFrame({"mass_kg":x,"time_min":y,"fitted":fitted,"residual":residuals,"squared":residuals**2}))
print(f"RSS={rss:.3f}, TSS={tss:.3f}, R-squared={1-rss/tss:.3f}")
fig, ax = plt.subplots(layout="constrained")
ax.scatter(x,y,s=75,label="Observed packages")
ax.plot(x,fitted,label="OLS: 2.2 + 0.6 × mass")
ax.vlines(x,fitted,y,color=ORANGE,lw=2,label="Vertical residuals")
ax.set(xlabel="Package mass (kg)",ylabel="Packing time (minutes)",title="Least squares fits all five observations together")
ax.legend()
save_figure(fig,"least_squares")

# %% inference
df = len(x)-2
sigma_hat = np.sqrt(rss/df)
slope_se = sigma_hat/np.sqrt(sxx)
t_stat = slope/slope_se
f_stat = ((tss-rss)/1)/(rss/df)
p_t = 2*stats.t.sf(abs(t_stat),df)
p_f = stats.f.sf(f_stat,1,df)
assert np.isclose(f_stat,t_stat**2)
assert np.isclose(p_t,p_f) and np.isclose(p_t,fit.pvalues[1])
print(f"Slope SE={slope_se:.4f}; t={t_stat:.4f}; F={f_stat:.4f}; p={p_t:.4f}")
print("95% coefficient intervals:",fit.conf_int())

# %% prediction
grid = np.linspace(1,5,120)
pred = fit.get_prediction(sm.add_constant(grid)).summary_frame(alpha=.05)
fig, ax = plt.subplots(layout="constrained")
ax.fill_between(grid,pred["obs_ci_lower"],pred["obs_ci_upper"],color=TEAL,alpha=.14,label="95% individual prediction interval")
ax.fill_between(grid,pred["mean_ci_lower"],pred["mean_ci_upper"],color=TEAL,alpha=.4,label="95% mean confidence interval")
ax.plot(grid,pred["mean"],color=TEAL)
ax.scatter(x,y,color=ORANGE,s=60)
ax.set(xlabel="Package mass (kg)",ylabel="Packing time (minutes)",title="Uncertainty about a mean is smaller than individual uncertainty")
ax.legend(fontsize=9)
save_figure(fig,"prediction_intervals")
display(fit.get_prediction(np.array([[1.,3.]])).summary_frame())

# %% diagnostics
rng = np.random.default_rng(606)
dx = np.linspace(0,10,90)
fig, axes = plt.subplots(1,3,figsize=(12,4),layout="constrained")
examples = [
    ("Suitable linear mean",10+.5*dx+rng.normal(0,1,len(dx))),
    ("Missing curvature",10+.5*dx+.25*(dx-5)**2+rng.normal(0,.65,len(dx))),
    ("Increasing variance",10+.5*dx+rng.normal(0,.2+.3*dx,len(dx))),
]
for ax,(label,response) in zip(axes,examples):
    diagnostic_fit = sm.OLS(response,sm.add_constant(dx)).fit()
    ax.scatter(dx,diagnostic_fit.resid,s=18,alpha=.75)
    ax.axhline(0,color="black",ls="--")
    ax.set(xlabel="Predictor x",ylabel="Residual",title=label)
save_figure(fig,"residual_patterns")

# %% practice
exercise_fit = sm.OLS([1.,2.,2.],sm.add_constant([0.,1.,2.])).fit()
assert np.allclose(exercise_fit.params,[7/6,.5])
assert np.isclose(exercise_fit.ssr,1/6) and np.isclose(exercise_fit.rsquared,.75)
print("Practice coefficients:",exercise_fit.params,"RSS:",exercise_fit.ssr,"R²:",exercise_fit.rsquared)

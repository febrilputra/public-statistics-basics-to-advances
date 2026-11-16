# %% t_distributions
grid = np.linspace(-5,5,600)
fig, ax = plt.subplots(layout="constrained")
ax.plot(grid,stats.norm.pdf(grid),color="black",ls="--",label="Standard normal")
for df in [2,5,30]: ax.plot(grid,stats.t.pdf(grid,df),label=f"t, df={df}")
ax.set(xlabel="Standardized statistic",ylabel="Density",title="Estimating SD gives heavier reference tails")
ax.legend()
save_figure(fig,"t_distributions")

# %% one_sample
volumes = np.array([48,49,50,51,52],dtype=float)
one = stats.ttest_1samp(volumes,49)
assert np.isclose(one.statistic,np.sqrt(2))
print("One-sample test:",one)
print("95% interval for the mean:",one.confidence_interval())

# %% welch
a = np.array([15,17,18,19,21],dtype=float)
b = np.array([12,13,14,16,20,21],dtype=float)
delta = b.mean()-a.mean()
va,vb = a.var(ddof=1)/len(a),b.var(ddof=1)/len(b)
se = np.sqrt(va+vb)
df_w = (va+vb)**2/(va**2/(len(a)-1)+vb**2/(len(b)-1))
t_w = delta/se
welch = stats.ttest_ind(b,a,equal_var=False)
ci = delta+np.array([-1,1])*stats.t.ppf(.975,df_w)*se
assert np.isclose(welch.statistic,t_w) and np.isclose(welch.df,df_w)
assert np.allclose(ci,welch.confidence_interval())
print(f"B-A={delta:.3f}, SE={se:.4f}, df={df_w:.4f}, t={t_w:.4f}, p={welch.pvalue:.4f}")
print("95% Welch CI:",ci)
fig, axes = plt.subplots(1,2,figsize=(11,4.5),layout="constrained")
axes[0].scatter(np.zeros(len(a)),a,s=70,label="A")
axes[0].scatter(np.ones(len(b)),b,s=70,label="B")
axes[0].set(xticks=[0,1],xticklabels=["Process A","Process B"],ylabel="Time (minutes)",title="Independent observations")
axes[1].errorbar(delta,0,xerr=[[delta-ci[0]],[ci[1]-delta]],fmt="o",capsize=6,color=TEAL)
axes[1].axvline(0,color="black",ls="--")
axes[1].set(xlabel="B - A mean time (minutes)",yticks=[],ylim=(-1,1),title="Difference with 95% Welch interval")
save_figure(fig,"welch_comparison")

# %% regression_equivalence
import statsmodels.api as sm
all_y = np.r_[a,b]
indicator = np.r_[np.zeros(len(a)),np.ones(len(b))]
regression = sm.OLS(all_y,sm.add_constant(indicator)).fit()
pooled = stats.ttest_ind(b,a,equal_var=True)
assert np.isclose(pooled.statistic,regression.tvalues[1])
assert np.isclose(pooled.pvalue,regression.f_pvalue)
assert np.isclose(regression.fvalue,pooled.statistic**2)
print("Pooled t p-value:",pooled.pvalue,"OLS F p-value:",regression.f_pvalue)
print("Welch p-value differs because it uses another variance model:",welch.pvalue)

# %% paired
before = np.array([40,50,60,70,80],dtype=float)
after = np.array([38,47,59,66,78],dtype=float)
d = after-before
paired = stats.ttest_rel(after,before)
assert np.isclose(paired.statistic,stats.ttest_1samp(d,0).statistic)
print("Paired mean difference:",d.mean(),"sample variance:",d.var(ddof=1))
print("Paired test:",paired,"95% CI:",paired.confidence_interval())
fig, axes = plt.subplots(1,2,figsize=(11,4.5),layout="constrained")
for i,(v_before,v_after) in enumerate(zip(before,after)):
    axes[0].plot([0,1],[v_before,v_after],"o-",label=f"Device {i+1}")
axes[0].set(xticks=[0,1],xticklabels=["Before","After"],ylabel="Time (seconds)",title="Preserve each device's pair")
axes[1].scatter(np.arange(1,6),d,s=70,color=TEAL)
axes[1].axhline(d.mean(),color=ORANGE,ls="--",label="Mean change = -2.4 s")
axes[1].axhline(0,color="black",lw=1)
axes[1].set(xlabel="Device",ylabel="After - before (seconds)",xticks=np.arange(1,6),title="The paired test analyzes changes")
axes[1].legend()
save_figure(fig,"paired_times")

# %% practice
differences = np.array([1,2,2,3,3,1],dtype=float)
assert np.isclose(stats.ttest_1samp(differences,0).statistic,np.sqrt(30))
nu = (9/10+16/20)**2/((9/10)**2/9+(16/20)**2/19)
print("Practice 1:",stats.ttest_1samp(differences,0))
print("Practice 2 Welch SE:",np.sqrt(1.7),"df:",nu)

# %% exact_binomial
k = np.arange(13)
masses = stats.binom.pmf(k,12,.5)
extreme = (k<=2)|(k>=10)
p_manual = masses[extreme].sum()
result = stats.binomtest(10,12,p=.5,alternative="two-sided")
assert np.isclose(p_manual,158/4096) and np.isclose(p_manual,result.pvalue)
print(f"Observed-count probability = {masses[10]:.6f}; two-sided p = {p_manual:.6f}")
print("One-sided p:",stats.binomtest(10,12,p=.5,alternative="greater").pvalue)
fig, ax = plt.subplots(layout="constrained")
ax.bar(k,masses,color=np.where(extreme,ORANGE,TEAL))
ax.set(xlabel="Number assigned to A out of 12",ylabel="Probability under q = 0.5",
       xticks=k,title=f"Orange bars contribute to the p-value: {p_manual:.4f}")
ax.annotate("Observed: 10",xy=(10,masses[10]),xytext=(9,.12),arrowprops={"arrowstyle":"->"})
save_figure(fig,"binomial_tails")

# %% direction_selection
rng = np.random.default_rng(505)
z = rng.standard_normal(100000)
p_two = 2*stats.norm.sf(np.abs(z))
p_fixed = stats.norm.sf(z)
p_selected = np.minimum(stats.norm.cdf(z),stats.norm.sf(z))
rates = [np.mean(p<=.05) for p in [p_two,p_fixed,p_selected]]
fig, ax = plt.subplots(layout="constrained")
ax.bar(["Two-sided", "Fixed upper tail", "Choose tail after seeing z"],rates,color=[TEAL,TEAL,ORANGE])
ax.axhline(.05,color="black",ls="--",label="Intended Type I error rate")
ax.set(ylabel="Rejection fraction under H0",ylim=(0,.13),title="Selecting a direction changes the procedure's error rate")
for i,r in enumerate(rates): ax.text(i,r+.003,f"{r:.3f}",ha="center")
ax.legend()
save_figure(fig,"direction_selection")

# %% confidence_interval
setup_times = np.array([18,20,22,24,26],dtype=float)
se = stats.sem(setup_times)
critical = stats.t.ppf(.975,len(setup_times)-1)
ci = setup_times.mean()+np.array([-1,1])*critical*se
test = stats.ttest_1samp(setup_times,popmean=20)
print("Mean:",setup_times.mean(),"SE:",se,"95% CI:",ci)
print(f"Test of mean=20: t={test.statistic:.4f}, p={test.pvalue:.4f}")
assert ci[0]<20<ci[1] and test.pvalue>.05

# %% coverage
rng = np.random.default_rng(506)
true_mean, n, repetitions = 50, 12, 10000
samples = rng.normal(true_mean,8,(repetitions,n))
means = samples.mean(axis=1)
margin = stats.t.ppf(.975,n-1)*samples.std(axis=1,ddof=1)/np.sqrt(n)
low, high = means-margin,means+margin
covers = (low<=true_mean)&(high>=true_mean)
coverage = covers.mean()
print(f"Coverage across {repetitions} samples: {coverage:.4f}; Monte Carlo SE {np.sqrt(coverage*(1-coverage)/repetitions):.4f}")
fig, ax = plt.subplots(figsize=(9,6),layout="constrained")
for i in range(80):
    ax.plot([low[i],high[i]],[i,i],color=TEAL if covers[i] else ORANGE,lw=1.4)
ax.axvline(true_mean,color="black",ls="--",label="True mean = 50")
ax.set(xlabel="Mean parameter (measurement units)",ylabel="Repeated sample",
       title="95% is a property of the interval-building procedure")
ax.legend()
save_figure(fig,"interval_coverage")

# %% practice
all_p = np.array([stats.binomtest(int(i),12,.5).pvalue for i in range(13)])
exact_size = stats.binom.pmf(np.arange(13),12,.5)[all_p<=.05].sum()
assert np.isclose(exact_size,158/4096)
assert np.isclose(stats.binomtest(8,8,.5).pvalue,2/256)
print("Exact size for n=12:",exact_size)
print("Known-SD approximate interval:",40+np.array([-1,1])*1.96*2)

# %% power_geometry
alpha,n,sigma,delta = .05,64,4,2
se = sigma*np.sqrt(2/n)
critical = stats.norm.ppf(1-alpha/2)*se
grid = np.linspace(-3.5,5,800)
null_density = stats.norm.pdf(grid,0,se)
alt_density = stats.norm.pdf(grid,delta,se)
reject = np.abs(grid)>critical
fig, ax = plt.subplots(layout="constrained")
ax.plot(grid,null_density,label="Null: true difference = 0")
ax.plot(grid,alt_density,label="Alternative: true difference = 2")
ax.fill_between(grid,alt_density,where=reject,color=ORANGE,alpha=.25,label="Power: alternative area in rejection region")
for boundary in [-critical,critical]: ax.axvline(boundary,color="black",ls="--",alpha=.5)
ax.set(xlabel="Estimated mean difference (minutes)",ylabel="Density (per minute)",title="Known-SD illustration: judge the estimate against null cutoffs")
ax.legend(fontsize=9)
save_figure(fig,"power_geometry")

# %% sample_size
from statsmodels.stats.power import TTestIndPower
from math import ceil
planner = TTestIndPower()
d,target_power,alpha = .5,.8,.05
n_approx = 2*(stats.norm.ppf(1-alpha/2)+stats.norm.ppf(target_power))**2/d**2
n_continuous = planner.solve_power(effect_size=d,alpha=alpha,power=target_power,ratio=1,alternative="two-sided")
n_per_group = ceil(n_continuous)
achieved = planner.power(effect_size=d,nobs1=n_per_group,alpha=alpha,ratio=1,alternative="two-sided")
df = 2*n_per_group-2
noncentrality = d*np.sqrt(n_per_group/2)
cutoff = stats.t.ppf(1-alpha/2,df)
independent_power = stats.nct.cdf(-cutoff,df,noncentrality)+stats.nct.sf(cutoff,df,noncentrality)
assert n_per_group==64 and np.isclose(achieved,independent_power)
assert achieved>=target_power and planner.power(d,n_per_group-1,alpha,ratio=1)<target_power
print(f"Normal approximation: {n_approx:.3f}; t-based solution: {n_continuous:.3f}")
print(f"Round up: {n_per_group} per group, {2*n_per_group} total; power={achieved:.5f}")
print("Recruitment with 20% loss:",ceil(n_per_group/.8),"per group")

# %% sensitivity
rows = []
for effect in [.3,.4,.5,.6,.8]:
    for desired in [.8,.9]:
        needed = ceil(planner.solve_power(effect_size=effect,power=desired,alpha=.05,ratio=1))
        rows.append([effect,desired,needed,2*needed])
display(pd.DataFrame(rows,columns=["d","desired_power","n_per_group","total_n"]))
sizes = np.arange(5,201)
fig, ax = plt.subplots(layout="constrained")
for effect in [.3,.5,.8]:
    ax.plot(sizes,planner.power(effect_size=effect,nobs1=sizes,alpha=.05,ratio=1),label=f"d = {effect}")
ax.axhline(.8,ls="--",color="black",label="Target power = 0.80")
ax.axvline(64,ls=":",color="black",alpha=.5)
ax.set(xlabel="Independent observations per group",ylabel="Power",ylim=(0,1.02),title="Sample size is meaningful only with a specified effect")
ax.legend()
save_figure(fig,"power_curves")

# %% simulated_power
rng = np.random.default_rng(909)
repetitions = 10000
group_a = rng.normal(20,4,(repetitions,64))
group_b = rng.normal(22,4,(repetitions,64))
tests = stats.ttest_ind(group_b,group_a,axis=1,equal_var=True)
estimated_power = np.mean(tests.pvalue<=.05)
mc_se = np.sqrt(estimated_power*(1-estimated_power)/repetitions)
print(f"Monte Carlo power={estimated_power:.4f}, SE={mc_se:.4f}, theoretical={achieved:.4f}")
assert abs(estimated_power-achieved)<5*mc_se

# %% practice
assert 3/6==.5
print("Rounded study total:",2*ceil(87.2))
print("Initial recruitment per group:",ceil(ceil(87.2)/.85))

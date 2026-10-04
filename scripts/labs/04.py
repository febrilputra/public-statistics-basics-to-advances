# %% exact_randomization
from itertools import combinations
standard = np.array([7,8,9])
new = np.array([4,5,6])
pooled = np.r_[new,standard]
observed = new.mean()-standard.mean()
null_differences = []
for chosen in combinations(range(6),3):
    mask = np.zeros(6,dtype=bool)
    mask[list(chosen)] = True
    null_differences.append(pooled[mask].mean()-pooled[~mask].mean())
null_differences = np.array(null_differences)
extreme = np.abs(null_differences)>=abs(observed)-1e-12
p_exact = extreme.mean()
assert len(null_differences)==20 and np.isclose(p_exact,.1)
values, counts = np.unique(np.round(null_differences,8),return_counts=True)
fig, ax = plt.subplots(layout="constrained")
ax.bar(values,counts/20,width=.48,color=np.where(abs(values)>=3-1e-7,ORANGE,TEAL))
ax.axvline(observed,ls="--",color="black",label=f"Observed difference = {observed:g}")
ax.set(xlabel="New - standard mean time (minutes)",ylabel="Probability under sharp null",
       title="Only 20 possible assignments: two equally extreme allocations")
ax.legend()
save_figure(fig,"randomization")
print(f"Exact two-sided p = {extreme.sum()}/20 = {p_exact:.2f}")

# %% repeated_tests
rng = np.random.default_rng(404)
alpha, n, sigma, reps = .05, 25, 5, 12000
shifts = np.array([0,.5,1,2,3])
rejection_rates = []
for shift in shifts:
    # Equivalent to simulating n iid normal measurements and taking their mean.
    means = rng.normal(shift,sigma/np.sqrt(n),reps)
    p_values = 2*stats.norm.sf(np.abs(means/(sigma/np.sqrt(n))))
    rejection_rates.append(np.mean(p_values<=alpha))
fig, ax = plt.subplots(layout="constrained")
ax.plot(shifts,rejection_rates,"o-",lw=2)
ax.axhline(alpha,ls="--",color=ORANGE,label="Nominal alpha = 0.05")
ax.set(xlabel="True mean shift (measurement units)",ylabel="Fraction of studies rejecting H0",
       ylim=(0,1),title="Rejection depends on the true effect and the study design")
ax.legend()
save_figure(fig,"decision_rates")
display(pd.DataFrame({"true_shift":shifts,"rejection_fraction":rejection_rates}))

# %% practice
from math import comb
assert comb(4,2)==6
print("Smallest two-sided p-value in practice 2:",2/comb(4,2))

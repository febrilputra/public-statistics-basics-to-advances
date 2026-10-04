# %% discrete_models
from math import comb
manual = comb(4,3) * .8**3 * .2
assert np.isclose(manual, stats.binom.pmf(3,4,.8))
print(f"P(K=3)={manual:.4f}; Poisson P(K=0)={stats.poisson.pmf(0,6):.6f}")
fig, axes = plt.subplots(1,2,figsize=(11,4.5),layout="constrained")
for ax, values, masses, title in [
    (axes[0], np.arange(5), stats.binom.pmf(np.arange(5),4,.8), "Binomial: 4 trials, p = 0.8"),
    (axes[1], np.arange(17), stats.poisson.pmf(np.arange(17),6), "Poisson: expected count = 6")]:
    ax.bar(values,masses,color=TEAL)
    ax.set(xlabel="Count",ylabel="Probability mass",title=title)
    ax.set_xticks(values[::1 if len(values)<=5 else 2])
save_figure(fig,"discrete_models")

# %% continuous_models
fig, axes = plt.subplots(1,3,figsize=(12,4),layout="constrained")
z = np.linspace(-7,7,700)
axes[0].plot(z,stats.norm.pdf(z,0,2))
axes[0].fill_between(z,stats.norm.pdf(z,0,2),where=(abs(z)<=2),color=TEAL,alpha=.4)
axes[0].set(title="Normal: central area = 0.6827",xlabel="Sensor error (mm)",ylabel="Density (per mm)")
t = np.linspace(0,20,700)
axes[1].plot(t,stats.expon.pdf(t,scale=4))
axes[1].fill_between(t,stats.expon.pdf(t,scale=4),where=t>6,color=TEAL,alpha=.4)
axes[1].set(title="Exponential: P(T > 6) = 0.2231",xlabel="Waiting time (minutes)",ylabel="Density (per minute)")
u = np.linspace(0,8,700)
axes[2].plot(u,stats.uniform.pdf(u,loc=2,scale=4))
axes[2].fill_between(u,stats.uniform.pdf(u,loc=2,scale=4),where=(u>=3)&(u<=4.5),color=TEAL,alpha=.4)
axes[2].set(title="Uniform: interval area = 0.375",xlabel="Delay (seconds)",ylabel="Density (per second)")
save_figure(fig,"continuous_models")
print("Normal central probability:",stats.norm.cdf(2,0,2)-stats.norm.cdf(-2,0,2))
print("P(recorded 0.0 mm):",stats.norm.cdf(.05,0,2)-stats.norm.cdf(-.05,0,2))

# %% likelihood
readings = np.array([9,10,14])
mu_grid = np.linspace(6,17,1101)
log_likelihood = stats.norm.logpdf(readings[:,None],loc=mu_grid,scale=2).sum(axis=0)
mu_hat = mu_grid[log_likelihood.argmax()]
assert np.isclose(mu_hat,11)
ll_at_11 = stats.norm.logpdf(readings,loc=11,scale=2).sum()
ll_at_10 = stats.norm.logpdf(readings,loc=10,scale=2).sum()
assert np.isclose(ll_at_11-ll_at_10,3/8)
fig, ax = plt.subplots(layout="constrained")
ax.plot(mu_grid,log_likelihood-log_likelihood.max(),label="Log likelihood minus its maximum")
ax.axvline(readings.mean(),ls="--",color=ORANGE,label="MLE = sample mean = 11")
ax.set(xlabel="Candidate mean (sensor units)",ylabel="Relative log likelihood",title="Keep the data fixed; vary the model's mean")
ax.legend()
save_figure(fig,"likelihood")
print("Likelihood ratio L(11)/L(10):",np.exp(ll_at_11-ll_at_10))
print("Normal variance MLE:",readings.var(ddof=0),"; unbiased estimate:",readings.var(ddof=1))

# %% practice
answers = {"binomial_exactly_two":stats.binom.pmf(2,6,.3),
           "binomial_at_least_one":stats.binom.sf(0,6,.3),
           "poisson_zero":stats.poisson.pmf(0,6),
           "normal_interval":stats.norm.cdf(15,12,1.5)-stats.norm.cdf(10.5,12,1.5),
           "likelihood":.2*.4,"log_likelihood":np.log(.2)+np.log(.4)}
display(pd.Series(answers,name="Answer"))
assert np.isclose(answers["binomial_exactly_two"],.324135)

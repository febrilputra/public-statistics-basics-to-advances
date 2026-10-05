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

# %% distribution_catalog
from scipy.special import gamma as gamma_function

# Check the relationships listed in Section 6.
assert np.allclose(stats.bernoulli.pmf([0, 1], 0.3), stats.binom.pmf([0, 1], 1, 0.3))
assert np.allclose(stats.multinomial.pmf(np.eye(3), 1, [0.5, 0.3, 0.2]), [0.5, 0.3, 0.2])
failures = np.arange(0, 8)
# SciPy's geom counts trials (1, 2, ...); nbinom counts failures (0, 1, ...).
assert np.allclose(stats.geom.pmf(failures + 1, 0.4), stats.nbinom.pmf(failures, 1, 0.4))
t_grid = np.linspace(0.01, 12, 300)
assert np.allclose(stats.expon.pdf(t_grid, scale=2), stats.gamma.pdf(t_grid, a=1, scale=2))
assert np.allclose(stats.chi2.pdf(t_grid, 4), stats.gamma.pdf(t_grid, a=4/2, scale=2))
assert np.allclose(stats.weibull_min.pdf(t_grid, c=1, scale=2), stats.expon.pdf(t_grid, scale=2))
z = np.linspace(-4, 4, 161)
t_gap = {nu: np.abs(stats.t.pdf(z, nu) - stats.norm.pdf(z)).max() for nu in [2, 10, 100]}
assert t_gap[2] > t_gap[10] > t_gap[100]
print("Largest |t density - normal density|:", {nu: round(float(g), 4) for nu, g in t_gap.items()})

# Check the mean formulas with example parameter values.
catalog = {
    "Geometric(p=0.4), trials":            (stats.geom(0.4), 1/0.4),
    "Negative binomial(r=3, p=0.4)":       (stats.nbinom(3, 0.4), 3*0.6/0.4),
    "Hypergeometric(N=20, M=5, n=4)":      (stats.hypergeom(M=20, n=5, N=4), 4*5/20),
    "Discrete uniform(1, ..., 6)":         (stats.randint(1, 7), 3.5),
    "Beta(2, 5)":                          (stats.beta(2, 5), 2/7),
    "Gamma(shape 3, scale 2)":             (stats.gamma(a=3, scale=2), 6),
    "Chi-squared(4)":                      (stats.chi2(4), 4),
    "Student t(5)":                        (stats.t(5), 0),
    "F(5, 10)":                            (stats.f(5, 10), 10/8),
    "Log-normal(mu=0, sigma=0.5)":         (stats.lognorm(s=0.5, scale=np.exp(0)), np.exp(0.5**2/2)),
    "Weibull(k=2, lambda=3)":              (stats.weibull_min(c=2, scale=3), 3*gamma_function(1 + 1/2)),
}
table = pd.DataFrame({name: {"formula mean": formula, "SciPy mean": dist.mean(), "SciPy variance": dist.var()}
                      for name, (dist, formula) in catalog.items()}).T
assert np.allclose(table["formula mean"], table["SciPy mean"])
display(table.round(4))

# Gallery of the additional distributions.
fig, axes = plt.subplots(4, 4, figsize=(14, 12.5), layout="constrained")
axes = axes.ravel()
def stems(ax, x, p, title):
    ax.bar(x, p, width=0.7, color=TEAL)
    ax.set(title=title, ylabel="Probability")
def curves(ax, x, specs, title, loc="best"):
    for (y, label), color in zip(specs, [PURPLE, ORANGE, TEAL]):
        ax.plot(x, y, color=color, lw=2, label=label)
    ax.set(title=title, ylabel="Density")
    if len(specs) > 1:
        ax.legend(fontsize=8, frameon=False, loc=loc)

stems(axes[0], [0, 1], stats.bernoulli.pmf([0, 1], 0.3), "Bernoulli(p = 0.3)")
axes[0].set_xticks([0, 1], ["0: fail", "1: success"])
axes[1].bar(["red", "green", "blue"], [0.5, 0.3, 0.2], color=TEAL, width=0.7)
axes[1].set(title="Categorical(0.5, 0.3, 0.2)", ylabel="Probability")
grid = np.array([[stats.multinomial.pmf([a, b, 4 - a - b], 4, [0.5, 0.3, 0.2]) if a + b <= 4 else np.nan
                  for b in range(5)] for a in range(5)])
axes[2].imshow(grid, origin="lower", cmap="Blues")
axes[2].set(title="Multinomial(n=4; 0.5, 0.3, 0.2)", xlabel="count of green", ylabel="count of red")
for a in range(5):
    for b in range(5 - a):
        axes[2].text(b, a, f"{grid[a, b]:.2f}", ha="center", va="center", fontsize=8,
                     color="white" if grid[a, b] > 0.09 else "#1E293B")
k = np.arange(1, 13)
stems(axes[3], k, stats.geom.pmf(k, 0.4), "Geometric(p = 0.4): trials")
k = np.arange(0, 16)
stems(axes[4], k, stats.nbinom.pmf(k, 3, 0.4), "Neg. binomial(r=3, p=0.4): failures")
k = np.arange(0, 5)
stems(axes[5], k, stats.hypergeom.pmf(k, 20, 5, 4), "Hypergeometric(N=20, M=5, n=4)")
k = np.arange(1, 7)
stems(axes[6], k, stats.randint.pmf(k, 1, 7), "Discrete uniform(1, ..., 6)")
x01 = np.linspace(0.001, 0.999, 400)
curves(axes[7], x01, [(stats.beta.pdf(x01, 2, 5), "α=2, β=5"), (stats.beta.pdf(x01, 2, 2), "α=2, β=2"),
                      (stats.beta.pdf(x01, 0.5, 0.5), "α=β=0.5")], "Beta")
axes[7].set_ylim(0, 4)
xpos = np.linspace(0.001, 20, 500)
curves(axes[8], xpos, [(stats.gamma.pdf(xpos, a=1, scale=2), "shape 1 (exponential)"),
                       (stats.gamma.pdf(xpos, a=3, scale=2), "shape 3")], "Gamma (scale 2)")
curves(axes[9], xpos, [(stats.chi2.pdf(xpos, nu), f"ν = {nu}") for nu in [2, 4, 8]], "Chi-squared")
axes[9].set_ylim(0, 0.5)
zz = np.linspace(-5, 5, 400)
curves(axes[10], zz, [(stats.t.pdf(zz, 2), "t, ν = 2"), (stats.t.pdf(zz, 10), "t, ν = 10"),
                      (stats.norm.pdf(zz), "standard normal")], "Student's t", loc="upper left")
xf = np.linspace(0.001, 5, 400)
curves(axes[11], xf, [(stats.f.pdf(xf, 5, 10), "d1 = 5, d2 = 10"), (stats.f.pdf(xf, 2, 20), "d1 = 2, d2 = 20")], "F")
xl = np.linspace(0.001, 5, 400)
curves(axes[12], xl, [(stats.lognorm.pdf(xl, s=0.5), "μ = 0, σ = 0.5"), (stats.lognorm.pdf(xl, s=1), "μ = 0, σ = 1")],
       "Log-normal")
xw = np.linspace(0.001, 8, 400)
curves(axes[13], xw, [(stats.weibull_min.pdf(xw, c=0.8, scale=3), "k = 0.8"),
                      (stats.weibull_min.pdf(xw, c=1, scale=3), "k = 1 (exponential)"),
                      (stats.weibull_min.pdf(xw, c=2.5, scale=3), "k = 2.5")], "Weibull (λ = 3)")
axes[13].set_ylim(0, 0.6)
for ax in axes[14:]:
    ax.axis("off")
axes[14].text(0, 0.75, "Teal bars: discrete masses\n(add them for probabilities)\n\n"
              "Curves: continuous densities\n(probability = area under the curve)",
              fontsize=11, va="top", transform=axes[14].transAxes)
fig.suptitle("Additional probability distributions: typical shapes", fontsize=16)
save_figure(fig, "distribution_gallery")

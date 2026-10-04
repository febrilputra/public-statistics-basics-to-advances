# %% arithmetic
from math import comb
x = np.array([1,2,4.])
assert np.isclose(np.sum(x**2),21) and np.isclose(x.sum()**2,49)
assert np.isclose(np.sum(x-x.mean()),0)
print("Sum of squares:",np.sum(x**2),"; square of sum:",x.sum()**2)
print("Choose two of five:",comb(5,2))
contributions = np.array([.2,.4,.1])
assert np.isclose(np.log(contributions.prod()),np.log(contributions).sum())
print("Product:",contributions.prod(),"; log product:",np.log(contributions).sum())

# %% conditional_probability
prevalence, detection, false_flag = .1,.9,.2
p_flag = detection*prevalence+false_flag*(1-prevalence)
posterior = detection*prevalence/p_flag
assert np.isclose(posterior,1/3)
print("P(flag):",p_flag,"; P(flaw | flag):",posterior)
fig, axes = plt.subplots(1,2,figsize=(11,4.7),layout="constrained")
axes[0].bar(["Flawed", "Unflawed"],[90,180],color=[ORANGE,TEAL])
axes[0].set(ylabel="Expected flagged parts per 1,000 screened",title="Who contributes to the flags?")
for i,count in enumerate([90,180]):
    axes[0].text(i,count+3,str(count),ha="center")
axes[0].set_ylim(0,205)
prior = np.linspace(.001,.5,300)
updated = detection*prior/(detection*prior+false_flag*(1-prior))
axes[1].plot(prior,updated,color=TEAL)
axes[1].scatter([prevalence],[posterior],color=ORANGE,zorder=3)
axes[1].set(xlabel="Flaw prevalence",ylabel="P(flaw | flag)",title="Same sensor, different base rates",ylim=(0,1))
save_figure(fig,"conditional_probability")

# %% clt
rng = np.random.default_rng(1201)
B, mu, sigma = 12000,2,2
fig, axes = plt.subplots(1,3,figsize=(12,4.2),layout="constrained",sharex=True,sharey=True)
grid = np.linspace(-4,5,400)
for ax,n in zip(axes,[1,5,40]):
    draws = rng.exponential(scale=mu,size=(B,n))
    standardized = np.sqrt(n)*(draws.mean(axis=1)-mu)/sigma
    ax.hist(standardized,bins=np.linspace(-4,5,65),density=True,color=TEAL,alpha=.6)
    ax.plot(grid,stats.norm.pdf(grid),color=ORANGE,label="Standard normal")
    ax.set(xlabel="Standardized sample mean",title=f"n = {n}",xlim=(-4,5))
    print(f"n={n}: mean={standardized.mean():.3f}, SD={standardized.std(ddof=1):.3f}")
axes[0].set_ylabel("Density")
axes[-1].legend()
save_figure(fig,"central_limit_theorem")

# %% derivatives
b = np.linspace(0,5,300)
loss = (5-2*b)**2
derivative = 8*b-20
step = 1e-5
finite_difference = ((5-2*(b+step))**2-(5-2*(b-step))**2)/(2*step)
assert np.allclose(finite_difference,derivative,atol=1e-7)
fig, axes = plt.subplots(1,2,figsize=(11,4.5),layout="constrained")
axes[0].plot(b,loss,color=TEAL)
axes[0].scatter([2.5],[0],color=ORANGE,zorder=3)
axes[0].set(xlabel="b",ylabel="Loss",title="L(b) = (5 − 2b)²")
axes[1].plot(b,derivative,color=ORANGE,label="Analytic derivative")
axes[1].plot(b[::15],finite_difference[::15],"o",ms=3,color=TEAL,label="Finite difference")
axes[1].axhline(0,color="black",lw=1)
axes[1].set(xlabel="b",ylabel="Derivative",title="L′(b) = 8b − 20")
axes[1].legend()
save_figure(fig,"derivative_and_loss")

# %% least_squares
x = np.arange(4,dtype=float)
y = np.array([1,2,2,4.])
sxx = np.sum((x-x.mean())**2)
sxy = np.sum((x-x.mean())*(y-y.mean()))
slope = sxy/sxx
intercept = y.mean()-slope*x.mean()
X = np.column_stack([np.ones(len(x)),x])
beta,residual_sum,rank,singular_values = np.linalg.lstsq(X,y,rcond=None)
residuals = y-X@beta
rss = residuals@residuals
tss = np.sum((y-y.mean())**2)
assert np.allclose(beta,[intercept,slope]) and np.allclose(beta,[.9,.9])
assert np.isclose(rss,.7) and np.isclose(tss,4.75)
assert np.allclose(X.T@residuals,0,atol=1e-12) and rank==2
print("Coefficients:",beta,"; residuals:",residuals)
print("RSS:",rss,"; R²:",1-rss/tss,"; adjusted R²:",1-(rss/2)/(tss/3))
a_grid,b_grid = np.meshgrid(np.linspace(-1,3,140),np.linspace(-.2,2,140))
surface = np.sum((y[:,None,None]-a_grid[None,:,:]-x[:,None,None]*b_grid[None,:,:])**2,axis=0)
fig, ax = plt.subplots(figsize=(8,5.5),layout="constrained")
contours = ax.contour(a_grid,b_grid,surface,levels=[.8,1,2,4,8,16,32],colors=TEAL,linewidths=1)
ax.clabel(contours,inline=True,fontsize=9,colors="#273444")
ax.scatter([intercept],[slope],color=ORANGE,s=65,label="Minimum: (0.9, 0.9)",zorder=3)
ax.set(xlabel="Intercept a",ylabel="Slope b",title="RSS contours for four observations")
ax.legend()
save_figure(fig,"least_squares_surface")

# %% practice
rare_prior = .01
print("Practice 2:",.9*rare_prior/(.9*rare_prior+.2*(1-rare_prior)))
px = np.array([0,1,2.])
py = np.array([2,3,5.])
pX = np.column_stack([np.ones(3),px])
pbeta = np.linalg.lstsq(pX,py,rcond=None)[0]
prss = np.sum((py-pX@pbeta)**2)
ptss = np.sum((py-py.mean())**2)
assert np.allclose(pbeta,[11/6,1.5]) and np.isclose(prss,1/6)
assert np.isclose(1-prss/ptss,27/28)
print("Practice 4 coefficients:",pbeta,"; RSS:",prss,"; R²:",1-prss/ptss)
assert np.isclose(4+9-2*3,7)

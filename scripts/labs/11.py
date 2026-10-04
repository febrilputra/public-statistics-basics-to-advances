# %% anova
import statsmodels.api as sm
import statsmodels.formula.api as smf
from itertools import combinations
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.multicomp import pairwise_tukeyhsd
groups = {"A":np.array([4,5,6,5.]),"B":np.array([6,7,8,7.]),"C":np.array([8,9,10,9.])}
data = pd.DataFrame([(g,v) for g,values in groups.items() for v in values],columns=["layout","time"])
grand = data.time.mean()
ssw = sum(np.sum((v-v.mean())**2) for v in groups.values())
ssb = sum(len(v)*(v.mean()-grand)**2 for v in groups.values())
sst = np.sum((data.time-grand)**2)
N,g = len(data),len(groups)
mse = ssw/(N-g)
f_stat = (ssb/(g-1))/mse
model = smf.ols("time ~ C(layout)",data=data).fit()
assert np.isclose(ssw,6) and np.isclose(ssb,32) and np.isclose(sst,ssw+ssb)
assert np.isclose(f_stat,24) and np.isclose(f_stat,stats.f_oneway(*groups.values()).statistic)
assert np.isclose(f_stat,model.fvalue)
display(sm.stats.anova_lm(model,typ=2))
print("eta squared:",ssb/sst,"omega squared:",(ssb-(g-1)*mse)/(sst+mse))
fig, ax = plt.subplots(layout="constrained")
for i,(name,values) in enumerate(groups.items()):
    ax.scatter(i+np.array([-.06,-.02,.02,.06]),values,s=65,color=TEAL)
    ax.hlines(values.mean(),i-.23,i+.23,color=ORANGE,lw=3)
ax.axhline(grand,color="black",ls="--",label="Grand mean = 7")
ax.set(xticks=np.arange(g),xticklabels=list(groups),xlabel="Packing layout",ylabel="Time (minutes)",title="Group means reduce residual variation")
ax.legend()
save_figure(fig,"anova_groups")

# %% posthoc
contrasts = []
for left,right in combinations(groups,2):
    difference = groups[right].mean()-groups[left].mean()
    se_diff = np.sqrt(mse*(1/len(groups[left])+1/len(groups[right])))
    p = 2*stats.t.sf(abs(difference/se_diff),N-g)
    contrasts.append([f"{right} - {left}",difference,se_diff,p])
comparisons = pd.DataFrame(contrasts,columns=["contrast","difference","SE","raw_p"])
comparisons["Holm_p"] = multipletests(comparisons.raw_p,method="holm")[1]
display(comparisons)
tukey = pairwise_tukeyhsd(data.time,data.layout,alpha=.05)
print(tukey)
fig, ax = plt.subplots(layout="constrained")
differences = np.array(tukey.meandiffs)
intervals = np.array(tukey.confint)
ax.errorbar(differences,np.arange(len(differences)),
            xerr=[differences-intervals[:,0],intervals[:,1]-differences],fmt="o",capsize=5,color=TEAL)
ax.axvline(0,color="black",ls="--")
ax.set(yticks=np.arange(3),yticklabels=comparisons.contrast,xlabel="Mean time difference (minutes)",
       title="Tukey 95% simultaneous intervals for all three pairs",ylim=(-.6,2.6))
save_figure(fig,"pairwise_intervals")

# %% ancova
moisture = np.tile(np.arange(18,23,dtype=float),2)
method = np.repeat(["A","B"],5)
dry_time = np.array([7,7,10,11,15,2,6,7,10,10],dtype=float)
dry = pd.DataFrame({"moisture":moisture,"x":moisture-20,"method":method,"time":dry_time})
adjusted = smf.ols("time ~ x + C(method)",data=dry).fit()
unadjusted = smf.ols("time ~ C(method)",data=dry).fit()
covariate_only = smf.ols("time ~ x",data=dry).fit()
assert np.isclose(adjusted.params["C(method)[T.B]"],-3)
assert np.isclose(adjusted.params["x"],2) and np.isclose(adjusted.ssr,8)
display(pd.DataFrame({"estimate":adjusted.params,"SE":adjusted.bse,"p":adjusted.pvalues}))
print("Unadjusted group p:",unadjusted.pvalues["C(method)[T.B]"])
fig, ax = plt.subplots(layout="constrained")
for label,color in [("A",TEAL),("B",ORANGE)]:
    observed = dry[dry.method==label]
    ax.scatter(observed.moisture,observed.time,color=color,s=65)
    grid = np.linspace(18,22,60)
    prediction = adjusted.predict(pd.DataFrame({"x":grid-20,"method":label}))
    ax.plot(grid,prediction,color=color,label=f"Method {label}")
ax.set(xlabel="Initial moisture (%)",ylabel="Drying time (minutes)",title="ANCOVA: group comparisons conditional on moisture")
ax.legend()
save_figure(fig,"ancova")

# %% ancova_comparison
f_partial,p_partial,df_added = adjusted.compare_f_test(covariate_only)
partial_r2 = (covariate_only.ssr-adjusted.ssr)/covariate_only.ssr
assert np.isclose(covariate_only.ssr,30.5) and np.isclose(f_partial,19.6875)
print(f"Group after moisture: F={f_partial:.4f}, p={p_partial:.6f}, df=({df_added:g},7)")
print("Partial R²:",partial_r2,"; ordinary full-model R²:",adjusted.rsquared)
display(adjusted.conf_int().rename(columns={0:"95% lower",1:"95% upper"}))

# %% interaction
interaction_fit = smf.ols("time ~ x * C(method)",data=dry).fit()
print("Comparison allowing separate slopes:",interaction_fit.compare_f_test(adjusted))
print("Do not interpret nonrejection as proof of equal population slopes.")
illustrative_x = np.array([-2,0,2])
display(pd.DataFrame({"centered_moisture":illustrative_x,
                      "specified_interaction_contrast":-3+.8*illustrative_x}))

# %% practice
assert np.isclose((60/3)/(80/16),4)
assert np.isclose(((50-30)/2)/(30/20),20/3)
print("Practice 1 p:",stats.f.sf(4,3,16))
print("Practice 4 partial R²:",(50-30)/50)

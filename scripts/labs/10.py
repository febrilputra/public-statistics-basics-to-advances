# %% multiple_opportunities
m = np.arange(1,101)
fig, ax = plt.subplots(layout="constrained")
ax.plot(m,1-.95**m,lw=2)
ax.scatter([20],[1-.95**20],color=ORANGE,s=70)
ax.axhline(.05,color="black",ls="--",label="One-test error rate = 0.05")
ax.set(xlabel="Number of independent true-null tests",ylabel="Probability of at least one false rejection",
       ylim=(0,1.02),title="A family of tests has more chances to produce a false lead")
ax.legend()
save_figure(fig,"multiple_opportunities")
print("20-test FWER:",1-.95**20,"expected false rejections:",20*.05)

# %% corrections
from statsmodels.stats.multitest import multipletests
raw = np.array([.001,.012,.021,.04,.2])
m = len(raw)
bonf = np.minimum(1,m*raw)
holm = np.minimum(1,np.maximum.accumulate((m-np.arange(m))*raw))
bh = np.minimum(1,np.minimum.accumulate((m*raw/np.arange(1,m+1))[::-1])[::-1])
for method,manual in [("bonferroni",bonf),("holm",holm),("fdr_bh",bh)]:
    assert np.allclose(manual,multipletests(raw,method=method)[1])
display(pd.DataFrame({"raw":raw,"Bonferroni":bonf,"Holm":holm,"BH":bh}))
assert np.allclose(holm,[.005,.048,.063,.08,.2])

# %% family_simulation
rng = np.random.default_rng(1010)
families,tests_per_family,true_nulls = 3000,100,80
z = rng.normal(size=(families,tests_per_family))
z[:,true_nulls:] += 3
p_matrix = 2*stats.norm.sf(np.abs(z))
# Apply the preceding formulas to all families at once. Each row is one family.
# The row-wise sort retains the identity of each test so false rejections can
# still be counted against the known simulation truth after adjustment.
order = np.argsort(p_matrix,axis=1)
sorted_p = np.take_along_axis(p_matrix,order,axis=1)
ranks = np.arange(1,tests_per_family+1)
adjusted_sorted = {
    "bonferroni": np.minimum(1,tests_per_family*sorted_p),
    "holm": np.minimum(1,np.maximum.accumulate((tests_per_family-ranks+1)*sorted_p,axis=1)),
    "fdr_bh": np.minimum(1,np.minimum.accumulate(
        (tests_per_family*sorted_p/ranks)[:,::-1],axis=1)[:,::-1]),
}
inverse_order = np.argsort(order,axis=1)
rows = []
for method,sorted_adjustment in adjusted_sorted.items():
    adjusted = np.take_along_axis(sorted_adjustment,inverse_order,axis=1)
    # Independent library checks also verify restoration to original test order.
    for i in [0,1,17,2999]:
        assert np.allclose(adjusted[i],multipletests(p_matrix[i],method=method)[1])
    rejection = adjusted<=.05
    false = rejection[:,:true_nulls].sum(axis=1)
    total = rejection.sum(axis=1)
    rows.append([method,np.mean(false>0),np.mean(false/np.maximum(total,1)),np.mean(total)])
display(pd.DataFrame(rows,columns=["method","estimated_FWER","estimated_FDR","mean_discoveries"]))
print("These are Monte Carlo estimates, not guarantees for one realized family.")

# %% optional_stopping
rng = np.random.default_rng(1011)
repetitions,max_n = 12000,200
observations = rng.normal(size=(repetitions,max_n))
cumulative = observations.cumsum(axis=1)
looks = np.arange(20,201,20)
z_at_looks = cumulative[:,looks-1]/np.sqrt(looks)
p_at_looks = 2*stats.norm.sf(np.abs(z_at_looks))
fixed_rate = np.mean(p_at_looks[:,-1]<=.05)
any_rate = np.mean(np.any(p_at_looks<=.05,axis=1))
fig, ax = plt.subplots(layout="constrained")
ax.bar(["One planned look at 200","Stop at any of 10 looks"],[fixed_rate,any_rate],color=[TEAL,ORANGE])
ax.axhline(.05,color="black",ls="--")
ax.set(ylabel="False-positive fraction under zero mean",ylim=(0,max(.25,any_rate+.04)),title="The stopping rule belongs in the test calibration")
for i,rate in enumerate([fixed_rate,any_rate]): ax.text(i,rate+.005,f"{rate:.3f}",ha="center")
save_figure(fig,"optional_stopping")
print("Fixed:",fixed_rate,"Repeated looks:",any_rate)

# %% practice
exercise_adjusted = multipletests([.004,.020,.030],method="holm")[1]
assert np.allclose(exercise_adjusted,[.012,.040,.040])
print("Practice 1 FWER:",1-.95**10)
print("Practice 2 Holm:",exercise_adjusted)

# %% conditional_fit
import statsmodels.api as sm
x = np.repeat([-1.,1.],4)
z = np.tile(np.repeat([0.,1.],2),2)
y = 10+2*x+3*z+np.tile([-1.,1.],4)
design = np.column_stack([np.ones(8),x,z])
full = sm.OLS(y,design).fit()
reduced = sm.OLS(y,design[:,:2]).fit()
manual_coefficients = np.linalg.lstsq(design,y,rcond=None)[0]
assert np.allclose(manual_coefficients,[10,2,3])
assert np.isclose(full.ssr,8) and np.isclose(reduced.ssr,26)
display(pd.DataFrame({"term":["Intercept at size 5","Centered size","Coated"],
                      "estimate":full.params,"SE":full.bse,"p":full.pvalues}))
fig, ax = plt.subplots(layout="constrained")
for group,color in [(0,TEAL),(1,ORANGE)]:
    mask = z==group
    ax.scatter(x[mask]+5,y[mask],color=color,s=65)
    grid = np.linspace(-1,1,60)
    ax.plot(grid+5,full.predict(np.column_stack([np.ones(60),grid,np.full(60,group)])),
            color=color,label="Coated" if group else "Uncoated")
ax.set(xlabel="Batch size (items)",ylabel="Preparation time (minutes)",title="Compare groups at the same batch size")
ax.legend()
save_figure(fig,"conditional_fit")

# %% interaction
rows = []
for centered_size in [-1,0,1]:
    base = 10+2*centered_size
    coated = base+3+centered_size
    rows.append([centered_size,base,coated,coated-base])
display(pd.DataFrame(rows,columns=["centered_size","uncoated_mean","coated_mean","group_difference"]))

# %% nested_models
partial_f = ((reduced.ssr-full.ssr)/1)/(full.ssr/full.df_resid)
partial_p = stats.f.sf(partial_f,1,full.df_resid)
library_f,library_p,df_difference = full.compare_f_test(reduced)
assert np.isclose(partial_f,11.25) and np.isclose(partial_f,full.tvalues[2]**2)
assert np.isclose(partial_p,library_p)
print(f"Partial F={partial_f:.4f}, df=(1,5), p={partial_p:.5f}")
print(f"R²={full.rsquared:.5f}, adjusted R²={full.rsquared_adj:.5f}")

# %% overfitting
rng = np.random.default_rng(707)
train_x = rng.normal(size=(40,30))
test_x = rng.normal(size=(3000,30))
train_y = 4+2*train_x[:,0]-train_x[:,1]+rng.normal(size=40)
test_y = 4+2*test_x[:,0]-test_x[:,1]+rng.normal(size=3000)
rows = []
for predictors in [2,5,10,20,30]:
    fit = sm.OLS(train_y,sm.add_constant(train_x[:,:predictors])).fit()
    test_prediction = fit.predict(sm.add_constant(test_x[:,:predictors]))
    rows.append([predictors,np.sqrt(np.mean(fit.resid**2)),
                 np.sqrt(np.mean((test_y-test_prediction)**2)),fit.rsquared,fit.rsquared_adj])
scores = pd.DataFrame(rows,columns=["predictors","train_RMSE","test_RMSE","R2","adjusted_R2"])
assert np.all(np.diff(scores.train_RMSE)<=1e-10)
display(scores)
fig, ax = plt.subplots(layout="constrained")
ax.plot(scores.predictors,scores.train_RMSE,"o-",label="Training RMSE")
ax.plot(scores.predictors,scores.test_RMSE,"s-",label="Independent test RMSE")
ax.axvline(2,color="black",ls="--",alpha=.4)
ax.set(xlabel="Predictor columns (only the first two carry signal)",ylabel="RMSE (response units)",title="Fitting more noise can make future predictions worse")
ax.legend()
save_figure(fig,"overfitting")

# %% collinearity
from statsmodels.stats.outliers_influence import variance_inflation_factor
rng = np.random.default_rng(708)
a = rng.normal(size=100)
b = a+rng.normal(0,.03,100)
X_near = sm.add_constant(np.column_stack([a,b]))
X_exact = sm.add_constant(np.column_stack([a,1000*a]))
print("VIFs for nearly duplicated predictors:",[variance_inflation_factor(X_near,j) for j in [1,2]])
print("Exact duplicate design: columns =",X_exact.shape[1],"rank =",np.linalg.matrix_rank(X_exact))
assert np.linalg.matrix_rank(X_exact)==2

# %% practice
exercise_f = ((120-90)/(4-2))/(90/(30-4))
assert np.isclose(exercise_f,13/3)
print("Practice 1: F =",exercise_f,"p =",stats.f.sf(exercise_f,2,26))
assert np.allclose(10+2*x+3*z,13+2*x-3*(1-z))

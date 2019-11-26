import pprint, inspect
import pandas as pd
from sklearn import linear_model as lm, datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics

import statsmodels.api as sm

print(dir(sm))
diab = datasets.load_diabetes()
X = pd.DataFrame(diab.data, columns = diab.feature_names)
Y = diab.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

# training with OLS Regression
# we need to assess the performance of the model
reg = lm.LinearRegression(copy_X = True, normalize=True)

lm_fit = reg.fit(X_train, Y_train)
# Y_pred = reg.predict(X_test)
print("R-square is {} \n List of model weights are: \n {}".format( 1 - lm_fit.score(X_train, Y_train), lm_fit.coef_))

print(reg.get_params(deep=True))

# we don't have the p-values for the Linear Regression??

# print(lm_fit.score(X_train,Y_train))
# print("Accuracy: ", metrics.accuracy_score(Y_test, Y_pred))

# WARNING : WE NEED TO GET THE P-VALUES OF THE LINEAR REGRESSION
# SOLUTION : Use statsmodels library
# LIKE THE RESULTS THAT WE ARE GETTING IN R

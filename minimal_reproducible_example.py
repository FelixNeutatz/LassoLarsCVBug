import numpy as np
import sklearn.linear_model as lm

eps = 1e-08
X = np.load('data/X_error.npy')
target = np.load('data/target_error.npy')

reg = lm.LassoLarsCV(eps=eps)
reg.fit(X, target)
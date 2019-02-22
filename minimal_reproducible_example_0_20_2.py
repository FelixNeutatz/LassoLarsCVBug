import numpy as np
import sklearn.linear_model as lm

import platform; print(platform.platform())
import sys; print("Python", sys.version)
import numpy; print("NumPy", numpy.__version__)
import scipy; print("SciPy", scipy.__version__)
import sklearn; print("Scikit-Learn", sklearn.__version__)


eps = 1e-08
X = np.load('data/0.20.2/X_error.npy')
target = np.load('data/0.20.2/target_error.npy')

reg = lm.LassoLarsCV(eps=eps)
reg.fit(X, target)
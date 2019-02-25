import numpy as np
import sklearn.linear_model as lm

import platform; print(platform.platform())
import sys; print("Python", sys.version)
import numpy; print("NumPy", numpy.__version__)
import scipy; print("SciPy", scipy.__version__)
import sklearn; print("Scikit-Learn", sklearn.__version__)


import numpy; print("NumPy", numpy.__version__)
np.__config__.show()


eps = 1e-08
X = np.load('data/last/X_error.npy')
target = np.load('data/last/target_error.npy')

reg = lm.LassoLarsCV(eps=eps)
reg.fit(X, target)
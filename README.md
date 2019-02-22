# LassoLarsCVBug

Minimal reproducible example for https://github.com/scikit-learn/scikit-learn/issues/9603

We provide two examples. One example makes scikit fail for commit https://github.com/scikit-learn/scikit-learn/tree/09bc27630fb8feea2f10627dce25e93cd6ff258a

Another example makes scikit fail for version 0.20.2.

If you use scikit-learn at commit https://github.com/scikit-learn/scikit-learn/tree/09bc27630fb8feea2f10627dce25e93cd6ff258a
run:
```
python minimal_reproducible_example_0_21_dev0.py
```
This will cause the following exception:
```
Linux-4.15.0-45-generic-x86_64-with-Ubuntu-16.04-xenial
Python 3.6.7 (default, Oct 25 2018, 09:16:13) 
[GCC 5.4.0 20160609]
NumPy 1.16.1
SciPy 1.1.0
Scikit-Learn 0.21.dev0
/home/felix/Software/scikit-learn/sklearn/model_selection/_split.py:2061: FutureWarning: You should specify a value for 'cv' instead of relying on the default value. The default value will change from 3 to 5 in version 0.22.
  warnings.warn(CV_WARNING, FutureWarning)
/home/felix/Software/scikit-learn/sklearn/linear_model/least_angle.py:307: ConvergenceWarning: Regressors in active set degenerate. Dropping a regressor, after 19 iterations, i.e. alpha=3.087e-03, with an active set of 19 regressors, and the smallest cholesky pivot element being 1.000e-08. Reduce max_iter or increase eps parameters.
  ConvergenceWarning)
/home/felix/Software/scikit-learn/sklearn/linear_model/least_angle.py:333: ConvergenceWarning: Early stopping the lars path, as the residues are small and the current value of alpha is no longer well controlled. 32 iterations, alpha=1.558e-03, previous alpha=1.544e-03, with an active set of 31 regressors.
  ConvergenceWarning)
/home/felix/Software/scikit-learn/sklearn/linear_model/least_angle.py:307: ConvergenceWarning: Regressors in active set degenerate. Dropping a regressor, after 55 iterations, i.e. alpha=4.045e-05, with an active set of 37 regressors, and the smallest cholesky pivot element being 1.000e-08. Reduce max_iter or increase eps parameters.
  ConvergenceWarning)
/home/felix/Software/scikit-learn/sklearn/linear_model/least_angle.py:307: ConvergenceWarning: Regressors in active set degenerate. Dropping a regressor, after 56 iterations, i.e. alpha=4.045e-05, with an active set of 38 regressors, and the smallest cholesky pivot element being 1.000e-08. Reduce max_iter or increase eps parameters.
  ConvergenceWarning)
/home/felix/Software/scikit-learn/sklearn/linear_model/least_angle.py:307: ConvergenceWarning: Regressors in active set degenerate. Dropping a regressor, after 57 iterations, i.e. alpha=4.044e-05, with an active set of 39 regressors, and the smallest cholesky pivot element being 1.000e-08. Reduce max_iter or increase eps parameters.
  ConvergenceWarning)
/home/felix/Software/scikit-learn/sklearn/linear_model/least_angle.py:333: ConvergenceWarning: Early stopping the lars path, as the residues are small and the current value of alpha is no longer well controlled. 61 iterations, alpha=3.474e-05, previous alpha=3.473e-05, with an active set of 40 regressors.
  ConvergenceWarning)
Traceback (most recent call last):
  File "/home/felix/Software/LassoLarsCVBug/minimal_reproducible_example.py", line 16, in <module>
    reg.fit(X, target)
  File "/home/felix/Software/scikit-learn/sklearn/linear_model/least_angle.py", line 1142, in fit
    for train, test in cv.split(X, y))
  File "/home/felix/Software/scikit-learn/sklearn/externals/joblib/parallel.py", line 920, in __call__
    while self.dispatch_one_batch(iterator):
  File "/home/felix/Software/scikit-learn/sklearn/externals/joblib/parallel.py", line 759, in dispatch_one_batch
    self._dispatch(tasks)
  File "/home/felix/Software/scikit-learn/sklearn/externals/joblib/parallel.py", line 716, in _dispatch
    job = self._backend.apply_async(batch, callback=cb)
  File "/home/felix/Software/scikit-learn/sklearn/externals/joblib/_parallel_backends.py", line 182, in apply_async
    result = ImmediateResult(func)
  File "/home/felix/Software/scikit-learn/sklearn/externals/joblib/_parallel_backends.py", line 549, in __init__
    self.results = batch()
  File "/home/felix/Software/scikit-learn/sklearn/externals/joblib/parallel.py", line 225, in __call__
    for func, args, kwargs in self.items]
  File "/home/felix/Software/scikit-learn/sklearn/externals/joblib/parallel.py", line 225, in <listcomp>
    for func, args, kwargs in self.items]
  File "/home/felix/Software/scikit-learn/sklearn/linear_model/least_angle.py", line 960, in _lars_path_residues
    positive=positive)
  File "/home/felix/Software/scikit-learn/sklearn/linear_model/least_angle.py", line 376, in lars_path
    g1 = arrayfuncs.min_pos((C - Cov) / (AA - corr_eq_dir + tiny32))
ValueError: operands could not be broadcast together with shapes (28,) (27,) 

Process finished with exit code 1

```




If you use scikit-learn in version 0.20.2. 
```
python minimal_reproducible_example_0_20_2.py 
```
This will cause the following exception:
```
Linux-4.15.0-45-generic-x86_64-with-Ubuntu-16.04-xenial
Python 3.6.7 (default, Oct 25 2018, 09:16:13) 
[GCC 5.4.0 20160609]
NumPy 1.16.1
SciPy 1.1.0
Scikit-Learn 0.20.2
/home/felix/FastFeatures/new_project/venv/lib/python3.6/site-packages/sklearn/model_selection/_split.py:2053: FutureWarning: You should specify a value for 'cv' instead of relying on the default value. The default value will change from 3 to 5 in version 0.22.
  warnings.warn(CV_WARNING, FutureWarning)
Traceback (most recent call last):
  File "/home/felix/Software/LassoLarsCVBug/minimal_reproducible_example_0_20_2.py", line 16, in <module>
    reg.fit(X, target)
  File "/home/felix/FastFeatures/new_project/venv/lib/python3.6/site-packages/sklearn/linear_model/least_angle.py", line 1147, in fit
    for train, test in cv.split(X, y))
  File "/home/felix/FastFeatures/new_project/venv/lib/python3.6/site-packages/sklearn/externals/joblib/parallel.py", line 917, in __call__
    if self.dispatch_one_batch(iterator):
  File "/home/felix/FastFeatures/new_project/venv/lib/python3.6/site-packages/sklearn/externals/joblib/parallel.py", line 759, in dispatch_one_batch
    self._dispatch(tasks)
  File "/home/felix/FastFeatures/new_project/venv/lib/python3.6/site-packages/sklearn/externals/joblib/parallel.py", line 716, in _dispatch
    job = self._backend.apply_async(batch, callback=cb)
  File "/home/felix/FastFeatures/new_project/venv/lib/python3.6/site-packages/sklearn/externals/joblib/_parallel_backends.py", line 182, in apply_async
    result = ImmediateResult(func)
  File "/home/felix/FastFeatures/new_project/venv/lib/python3.6/site-packages/sklearn/externals/joblib/_parallel_backends.py", line 549, in __init__
    self.results = batch()
  File "/home/felix/FastFeatures/new_project/venv/lib/python3.6/site-packages/sklearn/externals/joblib/parallel.py", line 225, in __call__
    for func, args, kwargs in self.items]
  File "/home/felix/FastFeatures/new_project/venv/lib/python3.6/site-packages/sklearn/externals/joblib/parallel.py", line 225, in <listcomp>
    for func, args, kwargs in self.items]
  File "/home/felix/FastFeatures/new_project/venv/lib/python3.6/site-packages/sklearn/linear_model/least_angle.py", line 965, in _lars_path_residues
    positive=positive)
  File "/home/felix/FastFeatures/new_project/venv/lib/python3.6/site-packages/sklearn/linear_model/least_angle.py", line 380, in lars_path
    g1 = arrayfuncs.min_pos((C - Cov) / (AA - corr_eq_dir + tiny32))
ValueError: operands could not be broadcast together with shapes (45,) (44,) 
```

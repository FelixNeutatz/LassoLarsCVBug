# LassoLarsCVBug

Minimal reproducible example for https://github.com/scikit-learn/scikit-learn/issues/9603

scikit-learn version: 0.20.2
numpy version: 1.16.1

Output of the corresponding program:
```
/usr/local/lib/python3.6/dist-packages/sklearn/model_selection/_split.py:2053: FutureWarning: You should specify a value for 'cv' instead of relying on the default value. The default value will change from 3 to 5 in version 0.22.
  warnings.warn(CV_WARNING, FutureWarning)
Traceback (most recent call last):
  File "/home/felix/Software/LassoLarsCVBug/minimal_reproducible_example.py", line 9, in <module>
    reg.fit(X, target)
  File "/usr/local/lib/python3.6/dist-packages/sklearn/linear_model/least_angle.py", line 1147, in fit
    for train, test in cv.split(X, y))
  File "/usr/local/lib/python3.6/dist-packages/sklearn/externals/joblib/parallel.py", line 917, in __call__
    if self.dispatch_one_batch(iterator):
  File "/usr/local/lib/python3.6/dist-packages/sklearn/externals/joblib/parallel.py", line 759, in dispatch_one_batch
    self._dispatch(tasks)
  File "/usr/local/lib/python3.6/dist-packages/sklearn/externals/joblib/parallel.py", line 716, in _dispatch
    job = self._backend.apply_async(batch, callback=cb)
  File "/usr/local/lib/python3.6/dist-packages/sklearn/externals/joblib/_parallel_backends.py", line 182, in apply_async
    result = ImmediateResult(func)
  File "/usr/local/lib/python3.6/dist-packages/sklearn/externals/joblib/_parallel_backends.py", line 549, in __init__
    self.results = batch()
  File "/usr/local/lib/python3.6/dist-packages/sklearn/externals/joblib/parallel.py", line 225, in __call__
    for func, args, kwargs in self.items]
  File "/usr/local/lib/python3.6/dist-packages/sklearn/externals/joblib/parallel.py", line 225, in <listcomp>
    for func, args, kwargs in self.items]
  File "/usr/local/lib/python3.6/dist-packages/sklearn/linear_model/least_angle.py", line 965, in _lars_path_residues
    positive=positive)
  File "/usr/local/lib/python3.6/dist-packages/sklearn/linear_model/least_angle.py", line 380, in lars_path
    g1 = arrayfuncs.min_pos((C - Cov) / (AA - corr_eq_dir + tiny32))
ValueError: operands could not be broadcast together with shapes (45,) (44,) 
```

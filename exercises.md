# Exercises for Day 4
Testing and documentation of code, plotting with matplotlib


## 1. Testing code with py.test

#### a. Install pytest using e.g.
```
pip install pytest --user
```

#### b. Write a module ```test_simple_math.py``` which tests the correctness of the math operations inside ```simple_math.py```.
You can run the tests using the ```py.test``` command. Note that the name of your test functions should start with ```test_```.

## 2. Documenting code

#### a. Write some meaningful docstrings for the ```simple_math.py``` module, e.g. following the [numpy_doc](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) standard.

#### b. Create a documenation html page for the ```simple_math.py``` module using Sphinx.
Follow the instructions from the lecture notes.

## 3. Plotting with matplotlib

#### a. Download the jupyter notebook [customized_plotting.ipynb](customized_plotting.ipynb) and try to understand the individual steps in creating a plot and customizing it

#### b. Produce your own data (curves, images, point clouds, etc...) and create a nice plot. Get inspired by the [matplotlib gallery](https://matplotlib.org/gallery/index.html) and use the extensive documentation of the [pyplot API](https://matplotlib.org/api/pyplot_summary.html)


## 4. Optimization with SciPy

#### Fitting Datasets
In the repository there's a file, `I_q_IPA_exp.npy`, with an experimental set of points giving the scattering strength of a sample as a function of the scattering vector. You also have, `I_q_IPA_model.npy`, a set of points produced by a theoretical model that also give the scattering strength as a function of the scattering vector. You would like to scale the points from the theoretical model to give the best possible fit to the experimental dataset. Use [`numpy.load()`](https://numpy.org/doc/stable/reference/generated/numpy.load.html) to load the arrays. For both arrays `[:,0]` correspond to the scattering vector and [:,1] corresponds to the scattering strength. A few useful SciPy functions might be [`scipy.optimize.minimize_scalar()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize_scalar.html#scipy.optimize.minimize_scalar) and [`scipy.interpolate.interp1d()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html#scipy.interpolate.interp1d). Matplotlib might be helpful to visualize the result, e.g. with [`plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html) or [`scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html). 



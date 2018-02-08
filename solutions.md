## 1. Speed optimization using Cython

### a. As a simple start, try to reproduce the ```primes.py``` Cythonize example from the lecture notes and familiarize yourself on how to use Cython
See lecture notes

### b. Take a look at the example ```rbf.py```<sup>[1](#myfootnote1)</sup> which uses Gaussian Radial Basis Functions (RBFs) as an approximation scheme some given data. 
How much speed up do you gain by using existing Python packages like Scipy? (Feel free to use your knowledge about performance testing 
and improve the current way of timing the different implementations)

There is about a 20-fold increase in speed when using Scipy. (compare to rbf_solution.py)

### c. In the above example, why is Scipy faster than the naive Python implementation? 
Which part of the Python code is slowing things down? (Again, use the profiling skills you learned yesterday)

It is mostly the for loops which are slowing down regular Python code.

### d. How much can you improve the performance of ```rbf.py``` using Cython? 
Use the lecture notes and follow the instructions from the comments

There is about a 80-fold increase in speed when using Cython. The performance can be even further improved by playing around with some C tricks (compare to ```rbf_solution.py```, ```fastloop.pyx``` and ```setup.py```). 

The procedure for using Cython is to first compile 
```
python setup.py build_ext --inplace
```

and then import the C-compiled module 
```
from fastloop import rbf_network_cython 
```

## 2. MPI parallelization

### a. Write a simple MPI script ```mpi_ranks.py``` that prints the rank of the different processes when running 
```mpirun python mpi_ranks.py```

see the file ```mpi_ranks.py```

### b. Write a small script ```mpi_sum.py``` which calculates the sum over all ranks and prints the result from the process with rank 0.
Hint: Have a look at the tutorials from the mpi4py documentation page: [https://mpi4py.scipy.org/docs/usrman/tutorial.html](https://mpi4py.scipy.org/docs/usrman/tutorial.html)

see the file ```mpi_sum.py```

## 3. Plotting with matplotlib

#### a. Download the jupyter notebook [customized_plotting.ipynb](customized_plotting.ipynb) and try to understand the individual steps in creating a plot and customizing it

#### b. Produce your own data (curves, images, point clouds, etc...) and create a nice plot. Get inspired by the [matplotlib gallery](https://matplotlib.org/gallery/index.html) and use the extensive documentation of the [pyplot API](https://matplotlib.org/api/pyplot_summary.html)


## 4. Testing code with py.test

#### a. Install pytest using e.g.
```
pip install --user pytest

```

#### b. Write a module ```test_simple_math.py``` which tests the correctness of the math operations inside ```simple_math.py```.
You can run the tests using the ```py.test``` command. Note that the name of your test functions should start with ```test_```.

See the file ```test_simple_math.py```

## 5. Documenting code

#### a. Write some meaningful docstrings for the ```simple_math.py``` module, e.g. following the [numpy_doc](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt) standard.

#### b. Create a documenation html page for the ```simple_math.py``` module using Sphinx.
Follow the instructions from the lecture notes.

Note: If you want to use the automodule feature (as shown in the lecture notes), you need to answer with "yes" to the automodule question in the configuration procedure.

********************************************************************************************************
<a name="myfootnote1">1</a>: Taken from [http://nealhughes.net/cython1/](http://nealhughes.net/cython1/)

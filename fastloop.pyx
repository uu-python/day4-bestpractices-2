from math import exp
import numpy as np
cimport numpy as np

def rbf_network_cython(np.ndarray[np.float64_t, ndim=2] X, np.ndarray[np.float64_t] beta, int theta):
    
    cdef int i, j, d
    cdef double r
    cdef int N = X.shape[0]
    cdef int D = X.shape[1]
    cdef np.ndarray[np.float64_t] Y = np.zeros(N, dtype=np.float64)

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y

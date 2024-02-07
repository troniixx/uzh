import math
import numpy as np

def transformer(M, x, tol):
    Q = np.zeros(M.shape)
    i, j = M.shape
    
    for k in range(i):
        for l in range(j):
            if abs(M[k, l] - x) < tol:
                Q[k, l] = x
            else:
                Q[k, l] = M[k, l]
                
    return Q


def calc(f, a):
    pass

def sequence(a, tol):
    pass
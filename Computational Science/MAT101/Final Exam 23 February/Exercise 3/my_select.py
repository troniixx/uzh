import numpy as np
import math

def my_select(d, w, y):
    out = []

    for element in w:
        if abs(element - y) > d:
            out.append(element)

    return out

def my_columns(A, y):
    # checks if y is present in any column of A
    l = []
    
    for i in range(A.shape[1]):
        if y in A[:, i]:
            l.append(True)
        else:
            l.append(False)

    return l


if __name__ == "__main__":
    A = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])
    
    w = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    d = 2
    y = 5
    
    print(my_select(d, w, y))
    print(my_columns(A, y))
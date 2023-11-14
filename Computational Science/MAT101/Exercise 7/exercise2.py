import numpy as np

def fibonacciMatrix(n: int) -> np.array:
    if not isinstance(n, int) or n < 0: return -1
    
    A = np.array([[1, 1], [1, 0]])
    
    return (np.linalg.matrix_power(A, n)@np.array([0, 1]))[0]


if __name__ == '__main__':
    print(fibonacciMatrix(0))
    print(fibonacciMatrix(1))
    print(fibonacciMatrix(11))
    print(fibonacciMatrix(12))
    print(fibonacciMatrix(13))
    print(fibonacciMatrix(101))
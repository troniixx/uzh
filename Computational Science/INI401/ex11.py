import numpy as np

def is_feasible(X):
    #return (X[0, 1] + X[0, 2] - X[0, 3] <= 0 and
    #        -X[1, 0] + X[1, 2] - X[1, 3] >= 0 and
    #        -X[2, 0] + X[2, 1] - X[2, 3] >= 0 and
    #        -X[3, 0] + X[3, 1] + X[3, 2] <= 0)
    
    return (X[0, 1] - X[0, 2] + X[0, 3] > 0 and
            -X[1, 0] - X[1, 2] + X[1, 3] <= 0 and
            -X[2, 0] + X[2, 1] + X[2, 3] > 0 and
            -X[3, 0] + X[3, 1] - X[3, 2] <= 0)

def generate_symmetric_matrix(n, min_val=-20, max_val=20):
    A = np.random.randint(min_val, max_val, size=(n, n))
    A_symmetric = (A + A.T) / 2
    np.fill_diagonal(A_symmetric, 0)  # Setting the diagonal elements to 0
    return A_symmetric

num_trials = 10000  # Number of matrices to try
for _ in range(num_trials):
    X = generate_symmetric_matrix(4)
    if is_feasible(X):
        print("A feasible matrix is found:")
        print(X)
        break
else:
    print("No feasible matrix found in {} trials.".format(num_trials))

import math
import matplotlib.pyplot as plt
import numpy as np

def partial_sum(q, n):
    if abs(q) < 1:
        return (1 - q**(n+1)) / (1 - q)
    else:
        raise ValueError("The series does not converge for |q| >= 1")

def convergence_vector(v):
    """Check if the geometric series converges for each q in v."""
    l = []
    for q in v:
        l.append(abs(q) < 1)
    return l

def convergence_limit(N):
    """
    This function calculates the limit S(q) of the series for N+1 equispaced values of q in the range [-0.5, 0.5].
    
    :param N: The number of intervals (N+1 points will be calculated)
    :return: A list of the limit values of the series
    """
    q_values = np.linspace(-0.5, 0.5, N+1)
    S_values = [1 / (1 - q) if q != 1 else None for q in q_values] 
    return q_values, S_values

def plot_convergence_limit(N):
    q_values, S_values = convergence_limit(N)
    
    plt.plot(q_values, S_values, label="S(q)", linestyle="-", marker="")
    plt.title("Convergence Limit of S(q)")
    plt.xlabel("q")
    plt.ylabel("S(q)")
    plt.grid(True)
    plt.savefig("Computational Science/MAT101/Final Exam 23 February/Exercise 1/plot_convergence.pdf")
    plt.show()

def convergence_even_odd(q, m, s):
    pass

def convergene_up_to_tolerance(q, t, m):
    pass

if __name__ == "__main__":
    v = [0.5, -0.5, 2, -2, 0, 1, -1]
    print(convergence_vector(v))
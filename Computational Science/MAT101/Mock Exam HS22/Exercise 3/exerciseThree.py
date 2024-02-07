import math
import numpy as np
import matplotlib.pyplot as plt

def plotter():
    N = 5
    _, ax = plt.subplots()
    Q = 100
    x = np.linspace(0, 1, Q)
    function_values = np.zeros((Q, N))

    for j in range(1, N+1):
        y = x**j
        ax.plot(x, y, label=f"x^{j}")
        function_values[:, j-1] = y

    ax.set_title("Functions x^j for j=1,...,N")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()
    plt.savefig("Computational Science/MAT101/Mock Exam HS22/Exercise 3/xj.png")
    plt.show()

    header = ",".join([f"x^{j}" for j in range(1, N+1)])
    np.savetxt("Computational Science/MAT101/Mock Exam HS22/Exercise 3/my_columns.dat", function_values, delimiter = ",", header = header, comments = "")

    print("Plot and data saved.")
    
def reproduce(N):
    data = np.loadtxt("Computational Science/MAT101/Mock Exam HS22/Exercise 3/my_columns.dat", delimiter=",", skiprows=1)  # skip the header row
    _, ax = plt.subplots()
    Q = 100
    x = np.linspace(0, 1, Q)
    
    for j in range(1, N+1):
        ax.plot(x, data[:, j-1], label=f"x^{j}")

    ax.set_title("Functions x^j for j=1,...,N")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()
    plt.savefig("Computational Science/MAT101/Mock Exam HS22/Exercise 3/xj_replot.png")
    plt.show()

    
if __name__ == "__main__":
    #plotter()
    reproduce(5)
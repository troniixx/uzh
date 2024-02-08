import numpy as np
import matplotlib.pyplot as plt


#TODO: Implement without using loop and using some numpy array function
def a_sequence(n):
    sol = []
    sol.append(1.33)
    for i in range(2, n+1):
        sol.append(sol[i-1] + ((2*i)**2 / (((2*i)**2)-1)))

def partial_wallis(n):
    sol = 1
    
    for i in range(1, n+1):
        sol *= ((2*i)**2 / (((2*i)**2)-1))
        
    return sol

def plotter(n):
    
    x = [i for i in range(n+1)]
    # y are the partial sums of the wallis sequence
    y = [partial_wallis(i) for i in range(n+1)]
    
    plt.plot(x, y, "x", color = "red", label="W_n", linestyle = "solid")
    plt.axhline(np.pi/2, color="blue", label="pi/2", linestyle="dashed")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.xlabel("n")
    plt.ylabel("Partial product")
    plt.show()

def convergence_up_to_tolerance(e, m):
    n  = 1
    
    while n <= m:
        ps1 = partial_wallis(n)
        ps2 = partial_wallis(n-1)
        
        if abs(ps1 - ps2) <= e:
            return n
    
    return "No convergence up to tolerance"

if __name__ == "__main__":
    #plotter(15)
    print(convergence_up_to_tolerance(0.0001, 1000))
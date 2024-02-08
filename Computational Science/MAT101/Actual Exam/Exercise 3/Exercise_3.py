import numpy as np
import matplotlib.pyplot as plt

# The wallis sequence is defined as the product of the following sequence:
def a_sequence(n):
    return np.array([(2*k/(2*k-1)) * (2*k/(2*k+1)) for k in range(1, n+1)])

def partial_wallis(n):
    # Calculate the sequence
    seq = a_sequence(n)
    # Return the product of the sequence
    return np.prod(seq)

def plotter(n):
    # Create the values of n
    xrange = np.arange(1, n+1)
    x_1 = 2**xrange
    
    # Calculate the partial products
    pp = [partial_wallis(n) for n in x_1]
    
    # Plot the partial products
    plt.plot(x_1, pp, "|", color = "red", label="W_n", linestyle = "solid")
    # Plot the pi/2 line
    plt.axhline((np.pi)/2, color="blue", label="pi/2", linestyle="dashed")
    
    # Addinf ruther information to the plot as documented in Figure 1
    plt.ylim(1.4, 1.6)
    plt.legend(loc = "lower right")
    plt.grid(True)
    plt.xscale("log")
    plt.xlabel("n")
    plt.ylabel("Partial product")
    plt.show()

def convergence_up_to_tolerance(e, m):
    n = 1
    while n <= m:
        # Calculate the partial products
        ps1 = partial_wallis(n)
        ps2 = partial_wallis(n-1)
        
        # check if the difference is less than the tolerance
        if abs(ps1 - ps2) <= e:
            return n # if yes, return value of n
        n += 1 # if no, increment m and continue
    
    # if no convergence is found, return the following message
    return "No convergence up to tolerance"

if __name__ == "__main__":
    plotter(15)
    #print(convergence_up_to_tolerance(0.1, 100))
    #print(a_sequence(15))
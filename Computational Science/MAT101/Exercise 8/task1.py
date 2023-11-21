import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial as f
#a
def approx_e_limit(x, n):
    return (1+x/n)**n

#b
def approx_e_sum(x, n):
    total = 0

    for k in range(n):
        term = (x**k)/f(k)
        total += term

    return total

#c
def plot_e_aproxximations(x, k):
    #title. axis labels, legend
    x_values = np.arange(1, k+1)
    limit = [approx_e_limit(x, k) for k in x_values]
    sum = [approx_e_sum(x, k) for k in x_values]

    plt.title("Approximate e^x")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline((np.exp(1))**2, color="black", label="e (np.exp(1))")
    plt.plot(x_values, limit, color = "orange", label="Limit")
    plt.plot(x_values, sum, color = "green", label="Sum")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    plot_e_aproxximations(2, 11)


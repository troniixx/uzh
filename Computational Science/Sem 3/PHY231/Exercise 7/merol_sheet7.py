import numpy as np
import scipy.optimize as opt
from scipy.stats import poisson
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

### ----- Exercise 1 ----- ###

def nll_ex1(alpha, data):
    return -np.sum(np.log(0.5 * (1 + alpha * data)))

def ex_1():
    print("Exercise 1:")
    data = np.loadtxt("MLE.txt")
    
    # Plot the negative-log-likelihood function for 0 <= alpha <= 1
    alpha = np.linspace(0, 1, 100)
    nll_values = [nll_ex1(a, data) for a in alpha]
    plt.figure(figsize=(8, 6))
    plt.plot(alpha, nll_values)
    plt.xlabel("Alpha")
    plt.ylabel("Negative Log-Likelihood")
    plt.title("Negative Log-Likelihood Function")
    plt.grid(True)
    plt.savefig("ex1.png")

    # (b) Determine the maximum likelihood estimator alpha_hat
    alpha_hat = alpha[np.argmin(nll_values)]
    print(f"The maximum likelihood estimator alpha_hat is: {alpha_hat:.2f}")


### ----- Exercise 2 ----- ###

exp_data = np.loadtxt("exponential_data.txt")

# Constants
tau_true = 2
t_min, t_max = 0, 5

# Part (a): Unbinned 2*NLL Calculation
def unbinned_nll(tau, data):
    """
    Calculate the negative log-likelihood for unbinned data given tau.
    """
    pdf = (1 / tau) * (1 - np.exp(-5/tau)) * np.exp(-data / tau)
    nll = -np.sum(np.log(pdf))
    return 2 * nll

# Part (b): Binned 2*NLL Calculation
def binned_nll(tau, data, n_bins=40, t_min=0, t_max=5):
    """
    Calculate the negative log-likelihood for binned data given tau.
    """
    bin_edges = np.linspace(t_min, t_max, n_bins + 1)
    counts, _ = np.histogram(data, bins=bin_edges)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    bin_width = bin_edges[1] - bin_edges[0]
    expected_counts = np.zeros_like(counts, dtype=float)
    
    for i, center in enumerate(bin_centers):
        expected_counts[i] = (1 / tau) * (1 - np.exp(-5/tau)) * np.exp(-center / tau) * bin_width * len(data)
    
    nll = -2 * np.sum(counts * np.log(expected_counts) - expected_counts)
    return nll

# Part (c): Chi-Square Calculation
def chi_squared_2(tau, data, n_bins=40, t_min=0, t_max=5):
    """
    Calculate the chi-squared for binned data given tau.
    """
    bin_edges = np.linspace(t_min, t_max, n_bins + 1)
    counts, _ = np.histogram(data, bins=bin_edges)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    bin_width = bin_edges[1] - bin_edges[0]
    expected_counts = np.zeros_like(counts, dtype=float)
    
    for i, center in enumerate(bin_centers):
        expected_counts[i] = (1 / tau) * (1 - np.exp(-5/tau)) * np.exp(-center / tau) * bin_width * len(data)
    
    chi2 = np.sum((counts - expected_counts) ** 2 / expected_counts)
    return chi2

def wider_binned_nll_and_chi_squared(tau, data):
    """
    Calculate the binned NLL and Chi-squared for just 2 bins.
    """
    return binned_nll(tau, data, n_bins=2), chi_squared_2(tau, data, n_bins=2)

def ex_2():
    print("\nExercise 2:")
    tau_values = np.linspace(1.8, 2.2, 100)

    unbinned_nll_values = np.array([unbinned_nll(tau, exp_data) for tau in tau_values])

    binned_nll_values = np.array([binned_nll(tau, exp_data) for tau in tau_values])

    chi_squared_values = np.array([chi_squared_2(tau, exp_data) for tau in tau_values])

    unbinned_nll_values -= np.min(unbinned_nll_values)
    binned_nll_values -= np.min(binned_nll_values)
    chi_squared_values -= np.min(chi_squared_values)

    plt.figure(figsize=(10, 6))

    plt.plot(tau_values, unbinned_nll_values, label="Unbinned 2*NLL", color="blue")
    plt.plot(tau_values, binned_nll_values, label="Binned 2*NLL (40 bins)", color="green")
    plt.plot(tau_values, chi_squared_values, label="Chi-Squared", color="red")

    plt.xlabel(r"$\tau$ [μs]")
    plt.ylabel(r"$\Delta$ 2*NLL / $\Delta \chi^2$")
    plt.legend()
    plt.title("Comparison of Unbinned NLL, Binned NLL, and Chi-Squared")
    plt.grid(True)
    plt.savefig("ex2.png")

    wider_binned_nll_value, wider_chi2_value = wider_binned_nll_and_chi_squared(tau_true, exp_data)
    print(f"Wider binned 2*NLL: {wider_binned_nll_value:.4f}")
    print(f"Wider binned Chi-Squared: {wider_chi2_value:.4f}")
    
### ----- Exercise 3 ----- ###

poly_data = np.loadtxt("polynomial_data.txt")

def poly_func(x, *params):
    degree = len(params) - 1
    return sum(p * x**(degree - i) for i, p in enumerate(params))

def chi_squared(y_observed, y_fit, uncertainties):
    return np.sum(((y_observed - y_fit) / uncertainties) ** 2)

def ex_3():
    print("\nExercise 3:")
    n_bins = 20
    bin_edges = np.linspace(-1, 1, n_bins + 1)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    hist, _ = np.histogram(poly_data, bins=bin_edges)

    uncertainties = np.sqrt(hist)

    plt.figure(figsize=(10, 6))
    plt.errorbar(bin_centers, hist, yerr=uncertainties, fmt="o", label="Data", color="black", capsize=3)
    plt.xlabel("x")
    plt.ylabel("Counts")
    plt.title("Histogram of x with Poisson Uncertainty")
    plt.grid(True)
    plt.legend()
    plt.savefig("ex3_0.png")

    degree_list = [1, 2, 3, 4]
    fits = []
    popt_list = []
    pcov_list = []

    for degree in degree_list:
        popt, pcov = curve_fit(poly_func, bin_centers, hist, p0=np.ones(degree + 1), sigma=uncertainties)
        fits.append(poly_func(bin_centers, *popt))
        popt_list.append(popt)
        pcov_list.append(pcov)

        plt.plot(bin_centers, fits[-1], label=f"Poly Degree {degree}")

    plt.errorbar(bin_centers, hist, yerr=uncertainties, fmt="o", label="Data", color="black", capsize=3)
    plt.xlabel("x")
    plt.ylabel("Counts")
    plt.title("Polynomial Fits of Different Degrees")
    plt.legend()
    plt.grid(True)
    plt.savefig("ex3_1.png")

    for degree, popt, pcov in zip(degree_list, popt_list, pcov_list):
        print(f"Polynomial Degree {degree}:")
        print("Optimal Parameters:", popt)
        print("Uncertainties:", np.sqrt(np.diag(pcov)))
        print()

    chi2_list = []
    ndf_list = []

    for degree, fit, popt, pcov in zip(degree_list, fits, popt_list, pcov_list):
        chi2 = chi_squared(hist, fit, uncertainties)
        ndf = len(hist) - (degree + 1)
        chi2_ndf = chi2 / ndf
        chi2_list.append(chi2_ndf)
        ndf_list.append(ndf)

    plt.figure(figsize=(8, 5))
    plt.plot(degree_list, chi2_list, marker="o", linestyle="-", color="blue")
    plt.xlabel("Degree of Polynomial")
    plt.ylabel(r"$\chi^2 / \text{ndf}$")
    plt.title("Chi-Squared per Degree of Freedom vs Polynomial Degree")
    plt.grid(True)
    plt.savefig("ex3_2.png")

    # Part (e):
    # From the chi2/ndf plot, the optimal degree should be the one with the lowest chi2/ndf.
    # Typically, a lower degree will have a lower chi-squared if its a good fit to the data.

    for degree, chi2_ndf in zip(degree_list, chi2_list):
        print(f"Degree {degree}: Chi-Squared / ndf = {chi2_ndf:.4f}")


if __name__ == "__main__":
    ex_1()
    ex_2()
    ex_3()
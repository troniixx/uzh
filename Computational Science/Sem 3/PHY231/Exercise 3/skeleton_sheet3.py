"""Skeleton sheet 3 Datenanalyse University of Zurich"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.stats as stats
from matplotlib.backends.backend_pdf import PdfPages



def integrate(dist, lower, upper):
    """Integrate the pdf of a distribution between lower and upper.

    Parameters
    ----------
    dist : scipy.stats.rv_continuous
        A scipy.stats distribution object.
    lower : float
        Lower limit of the integration.
    upper : float
        Upper limit of the integration.

    Returns
    -------
    integral : float
        The integral of the pdf between lower and upper.
    """

    integral, error = integrate.quad(dist.pdf, lower, upper)

    return integral #: add your code here


# THIS FUNCTION IS NOT NEEDED, JUST DEMONSTRATION PURPOSE
def example_integrate_shifted_norm(x):
    # to get a "norm distribution" with mean 5 and std 3, we can use
    norm_dist_shifted = stats.norm(loc=5, scale=3)
    # we can then use different methods of the norm_dist_shifted object to calculate
    # the probability density function (pdf) and the cumulative distribution function (cdf)
    # and more.
    # using the cdf we can also calculate the integral of the pdf:
    integrate_4to7 = norm_dist_shifted.cdf(7)- norm_dist_shifted.cdf(4)  # integral form 4 to 7
    # or just write a function that does it for us
    integral_1to10 = integrate(norm_dist_shifted, 1, 10)



def ex1(pdf):
    print("Exercise 1")

    print("\nPart a)")

    n = 4 # detectors
    p_signal = 0.85

    x = range(n+1)
    probs = [stats.binom.pmf(k, n, p_signal) for k in x]

    plt.figure()
    plt.bar(x, probs)
    plt.xlabel("Number of signals")
    plt.ylabel("Probability")
    plt.title("Porb Dist. for number of signals")
    pdf.savefig()
    plt.close()

    print("\nPart b)")

    p_signal_b = 0.85
    required = 0.99
    efficiency = 0
    n_detec = 1

    while efficiency < required:
        n_detec += 1
        efficiency = 1 - stats.binom.cdf(2, n_detec, p_signal_b)

    print("Minimum number of detectors: ", n_detec)


    print("\nPart c)")
    n_part = 1000
    n_detec_c = 4
    p_signal_c = 0.85
    res = np.random.binomial(n_detec_c, p_signal_c, n_part)

    detected = np.sum(res >= 3)
    print(f"Detected particles with 3 or more: {detected:.3f}")

    plt.figure()
    plt.hist(res, bins = np.arange(6)-0.5, density = True, alpha = 0.7, color = "green")
    plt.xlabel("Number of signals")
    plt.ylabel("Frequency")
    plt.title("Histogram of detected signals (1000 particles)")
    pdf.savefig()
    plt.close()


def ex3():
    print("\nExercise 3")
    mu = 1
    sigma = 0.01
    print("Probabilities:")

    p_a = stats.norm.cdf(1.03, mu, sigma) - stats.norm.cdf(0.97, mu, sigma)
    print(f"(a) Probability of height within [0.97, 1.03]: {p_a:.3f}")

    p_b = stats.norm.cdf(1.00, mu, sigma) - stats.norm.cdf(0.99, mu, sigma)
    print(f"(b) Probability of height within [0.99, 1.00]: {p_b:.3f}")

    p_c = stats.norm.cdf(1.05, mu, sigma) - stats.norm.cdf(0.95, mu, sigma)
    print(f"(c) Probability of height within [0.95, 1.05]: {p_c:.3f}")

    p_d = stats.norm.cdf(1.015, mu, sigma)
    print(f"(d) Probability of height less than 1.015: {p_d:.3f}")
    
def ex4():
    print("Exercise 4")


if __name__ == '__main__':
    #with PdfPages("Exercise 1.pdf") as pdf:
    #    ex1(pdf)

    ex3()  # uncomment to run ex3
    # ex4()  # uncomment to run ex4

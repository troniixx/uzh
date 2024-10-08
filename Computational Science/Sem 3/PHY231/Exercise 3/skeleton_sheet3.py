"""Skeleton sheet 3 Datenanalyse University of Zurich"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats



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
    return # TODO: add your code here


# THIS FUNCTION IS NOT NEEDED, JUST DEMONSTRATION PURPOSE
def example_integrate_shifted_norm(x):
    # to get a "norm distribution" with mean 5 and std 3, we can use
    norm_dist_shifted = scipy.stats.norm(loc=5, scale=3)
    # we can then use different methods of the norm_dist_shifted object to calculate
    # the probability density function (pdf) and the cumulative distribution function (cdf)
    # and more.
    # using the cdf we can also calculate the integral of the pdf:
    integrate_4to7 = norm_dist_shifted.cdf(7)- norm_dist_shifted.cdf(4)  # integral form 4 to 7
    # or just write a function that does it for us
    integral_1to10 = integrate(norm_dist_shifted, 1, 10)



def ex1():
    print("Exercise 1")
    print("... and the result is")

def ex3():
    print("Exercise 3")
    prob_a = 42  # TODO: calculate the probability of a
    print("Probabilities:")
    print(f"3a) {prob_a:.3f} to be within...")
    # 3f means that the number is printed with three decimals. Check if that makes sense!
    
def ex4():
    print("Exercise 4")


if __name__ == '__main__':
    ex1()
    # ex3()  # uncomment to run ex3
    # ex4()  # uncomment to run ex4

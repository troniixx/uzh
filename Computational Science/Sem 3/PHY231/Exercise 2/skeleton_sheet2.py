import numpy as np
from math import sqrt
import matplotlib.pyplot as plt


def mean(x):
    """Calculate the mean for an array-like object x.

    Parameters
    ----------
    x : array-like
        Array-like object containing the data.

    Returns
    -------
    mean : float
        The mean of the data.
    """
    # here goes your code

    return sum(x) / len(x)


def std(x):
    """Calculate the standard deviation for an array-like object x."""
    # here goes your code
    print("Calculating")  # replace this with your code
    return sqrt(variance(x))  # replace this with your code


def variance(x):
    """Calculate the variance for an array-like object x."""
    # here goes your code
    m = mean(x)
    var = sum((i - m) ** 2 for i in x) / (len(x) - 1)  # replace this with your code
    return var  # replace this with your code


def mean_uncertainty(x):
    """Calculate the uncertainty in the mean for an array-like object x."""
    # here goes your code
    s = std(x)
    # replace this with your code
    return s / sqrt(len(x))  # replace this with your code


def ex1():
    data = np.loadtxt("/Users/merterol/Desktop/VSCode/uzh/Computational Science/Sem 3/PHY231/Exercise 1/ironman.txt")
    age = 2010 - data[:, 1]
    total_time = data[:, 2]

    # a)
    mean_age = mean(age)
    mean_age_uncertainty = mean_uncertainty(age)
    # .2f means that the number is printed with two decimals. Check if that makes sense
    print("Using my own functions:")
    print(f"The mean age of the participants is {mean_age:.2f} +/- {mean_age_uncertainty:.2f} years.")
    print("Using numpy functions:")
    print(f"The mean age of the participants is {np.mean(age):.2f} +/- {np.std(age) / sqrt(len(age)):.2f} years.")

    mean_total_time = mean(total_time)
    mean_total_time_uncertainty = mean_uncertainty(total_time)
    print("Using my own functions:")
    print(f"The mean total time of the participants is {mean_total_time:.2f} +/- {mean_total_time_uncertainty:.2f} hours.")
    print("Using numpy functions:")
    print(f"The mean total time of the participants is {np.mean(total_time):.2f} +/- {np.std(total_time) / sqrt(len(total_time)):.2f} hours.")

    # b)
    younger_group = [time for a, time in zip(age, total_time) if a < 35]
    older_group = [time for a, time in zip(age, total_time) if a >= 35]

    younger_mean = mean(younger_group)
    older_mean = mean(older_group)
    younger_uncertainty = mean_uncertainty(younger_group)
    older_uncertainty = mean_uncertainty(older_group)

    print(f"The mean time of the younger group is {younger_mean:.2f} +/- {younger_uncertainty:.2f} hours.")
    print(f"The mean time of the older group is {older_mean:.2f} +/- {older_uncertainty:.2f} hours.")

    # Range younger = [675.57, 682.87] / range older = [701.99, 706.87]
    # Ranges do not overlap!
    # The younger group is significantly faster than the older group, with a mean time difference of about 25.21 hours.

    # c)

    # d)

    # e)

def ex2():
    radiation = np.loadtxt("/Users/merterol/Desktop/VSCode/uzh/Computational Science/Sem 3/PHY231/Exercise 2/radiation.txt")

    # a)
    m = radiation[:, 0]
    u = radiation[:, 1]

    print(f"The mean radiation (including mean uncertainty) is {mean(m):.6f} +/- {mean_uncertainty(u):.7f} mSv.")



if __name__ == '__main__':
    #ex1()
    ex2()  # uncomment to run ex2

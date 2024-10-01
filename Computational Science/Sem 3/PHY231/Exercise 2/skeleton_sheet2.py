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

    return sum(x) / len(x)


def std(x):
    """Calculate the standard deviation for an array-like object x."""
    return sqrt(variance(x))


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

def covariance(x, y):
    m_x = mean(x)
    m_y = mean(y)
    cov = sum((i - m_x) * (j - m_y) for i, j in zip(x, y)) / (len(x) - 1)
    
    return cov

def correlation(x, y):
    cov = covariance(x, y)
    std_x = std(x)
    std_y = std(y)
    
    return cov / (std_x * std_y)


def ex1():
    data = np.loadtxt("/Users/merterol/Desktop/iMac27_github/uzh/Computational Science/Sem 3/PHY231/Exercise 1/ironman.txt")
    age = 2010 - data[:, 1]
    total_time = data[:, 2]
    total_rank = data[:, 0]
    swimming_time = data[:, 3]
    swimming_rank = data[:, 4]
    cycling_time = data[:, 5]
    cycling_rank = data[:, 6]
    running_time = data[:, 7]
    running_rank = data[:, 8]

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
    
    print("\n")
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

    print("\n")
    print(f"The mean time of the younger group is {younger_mean:.2f} +/- {younger_uncertainty:.2f} hours.")
    print(f"The mean time of the older group is {older_mean:.2f} +/- {older_uncertainty:.2f} hours.")

    # Range younger = [675.57, 682.87] / range older = [701.99, 706.87]
    # Ranges do not overlap!
    # The younger group is significantly faster than the older group, with a mean time difference of about 25.21 hours.

    # c)
    

    # d)

    # e)
    
    
    print("\n")
    print(f"The covariance between total rank and total time is {covariance(total_rank, total_time):.4f}")
    print(f"The covariance between age and total time is {covariance(age, total_time):.4f}")
    print(f"The covariance between swimming time and total time is {covariance(swimming_time, total_time):.4f}")
    print(f"The covariance between cycling time and running time is {covariance(cycling_time, running_time):.4f}")

    print("\n")
    print(f"The correlation between total rank and total time is {correlation(total_rank, total_time):.4f}")
    print(f"The correlation between age and total time is {correlation(age, total_time):.4f}")
    print(f"The correlation between swimming time and total time is {correlation(swimming_time, total_time):.4f}")
    print(f"The correlation between cycling time and running time is {correlation(cycling_time, running_time):.4f}")
    
def ex2():
    DESKTOP = np.loadtxt("/Users/merterol/Desktop/iMac27_github/uzh/Computational Science/Sem 3/PHY231/Exercise 2/radiation.txt")
    LAPTOP = np.loadtxt("/Users/merterol/uzh/Computational Science/Sem 3/PHY231/Exercise 2/radiation.txt")
    
    # a)
    m = LAPTOP[:, 0]
    u = LAPTOP[:, 1]

    weights = 1 / (u ** 2)
    w_avg = np.sum(m * weights)/np.sum(weights)

    w_avg_uncertain = np.sqrt(1 / np.sum(weights))

    yearly = w_avg * 8760
    yearly_uncertain = w_avg_uncertain * 8760

    print(f"Weighted average radiation level: {yearly:.3f} mSv/year")
    print(f"Uncertainty in the weighted average radiation level: {yearly_uncertain:.4f} mSv/year")
    print(f"This leads to: {yearly:.3f} +/- {yearly_uncertain:.4f} mSv/year")

    """
    b)
    Natural Background radiation = 2.4 mSv/year
    My range = [2.5261, 2.6559] mSv/year

    --> higher than the Natural backgroud radiation
    --> also difference between natural and mine (0.191) is more than the uncertainty (0.0649) 
    --> so the two values are not compatible
    """

if __name__ == '__main__':
    ex1()
    #ex2()  # uncomment to run ex2

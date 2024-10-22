# author: Mert Erol, 20-915-245, merol
import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

SAND = "/Users/merterol/uzh/Computational Science/Sem 3/PHY231/Exercise 4/sand.txt"
DF = np.loadtxt(SAND)

def a():
    granules = DF[:, 0]
    slope = DF[:, 1]
    y_err = DF[:, 2]

    m = 16.1
    q = -2.61

    granules_fit = np.linspace(min(granules), max(granules), 100)
    slope_fit = m * granules_fit + q

    plt.errorbar(granules, slope, yerr = y_err, fmt = "o", label = "Data")
    plt.plot(granules_fit, slope_fit, label = "Fit")

    plt.xlabel("Granules")
    plt.ylabel("Slope")
    plt.title("Granules vs Slope")
    plt.legend()

    #plt.show()
    plt.savefig("plots_task_a.pdf")
    
    print("Part a: Plots have been successfully saved as plots_task_a.pdf\n")

def b():
    print("Part b: ")
    x = 1.5
    m_uncert = ufloat(16.1, 1.0)
    q_uncert = ufloat(-2.61, 0.34)
    
    y = m_uncert * x + q_uncert
    
    print(f"Slope of the beach for a sand grain diameter of {x} mm is {y}\n")

    
def c():
    print("Part c: ")
    
    x = 1.5
    m_uncert = ufloat(16.1, 1.0)
    q_uncert = ufloat(-2.61, 0.34)
    
    y = m_uncert * x + q_uncert

    sigma_m_squared = 1.068
    sigma_q_squared = 0.118
    cov_mq = -0.302
    
    sigma_y_with_correlation = np.sqrt((x ** 2) * sigma_m_squared + sigma_q_squared + 2 * x * cov_mq)
    sigma_y_without_correlation = np.sqrt((x ** 2) * sigma_m_squared + sigma_q_squared)

    print(f"Slope of the beach for a sand grain diameter of {x} mm is {y:.2f}")
    print(f"Uncertainty without correlation: {sigma_y_without_correlation:.2f}")
    print(f"Uncertainty with correlation: {sigma_y_with_correlation:.2f}")


    
if __name__ == "__main__":
    a()
    b()
    c()

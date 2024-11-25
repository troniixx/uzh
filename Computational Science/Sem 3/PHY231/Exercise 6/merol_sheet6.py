import numpy as np
from scipy import optimize
import scipy.optimize as opt
from scipy.stats import chi2
from matplotlib import pyplot as plt


def current_ohmslaw(U, R):
    r"""Calculate the current according to Ohm"s Law given the voltage U and resistance R.

    Ohm"s Law states that the current is given by:

    .. math::

        I = \frac{U}{R}

    Args:
        U (float, array): The measured voltage.
        R (float, array): The resistance.

    Returns:
        float or array: Value of the linear function. Shape is the broadcast shape of
            the inputs.
    """
    return U / R  # Implemented Ohm"s Law: I = U / R


def current_ohmslaw_bias(U, R, bias=None):
    """Calculate the current according to Ohm"s Law given the voltage U and resistance R with a bias.

    Ohm"s Law states that the current is given by:

    .. math::

        I = \frac{U}{R}

    We can add a bias to the current by adding a constant to the voltage:

    .. math::

        I = \frac{U + bias}{R}

    Args:
        U (float, array): The measured voltage.
        R (float, array): The resistance.
        bias (float, array): The bias to add to the voltage. If None, no bias is added.

    Returns:
        float or array: Value of the linear function. Shape is the broadcast shape of
            the inputs.
    """
    if bias is None:
        bias = 0  # with this, we can also use the function without bias.
    return current_ohmslaw(U, R + bias)  # Reuse code from above by calling the function


def chi2(x, y, err):
    """Calculate the chi2 statistic for a dataset and its predictions.

    Args:
        x (array): The first data set.
        y (array): Predicted values for the first data set.
        err (array): The error on the measurements of the first data set.

    Returns:
        float: The chi2 statistic.
    """
    return np.sum(((x - y) / err) ** 2)  # Implemented chi2 calculation

def chi2_2b(R):
    """Calculate chi2 in dependence of the resistance considering uncertainties."""
    # Calculate the predicted current using Ohm"s Law
    current_pred = current_ohmslaw(voltage, R)
    
    # Calculate chi2, including the uncertainties
    chi2val = np.sum(((current - current_pred) ** 2) / (uncertainties ** 2))
    
    return chi2val

DATA = np.loadtxt("/Users/merterol/uzh/Computational Science/Sem 3/PHY231/Exercise 6/current_measurements.txt")  # Load the data from the file
DATA_UNCERT = np.loadtxt("/Users/merterol/uzh/Computational Science/Sem 3/PHY231/Exercise 6/current_measurements_uncertainties.txt")  # Load the uncertainties from the file

# Used in exericse 1
voltage = DATA[:, 0]
current = DATA[:, 1]

# Used in exercise 2
voltage_two = DATA_UNCERT[:, 0]
current_two = DATA_UNCERT[:, 1]
uncertainties = DATA_UNCERT[:, 2]

def ex_1a():
    """Run exercise 1a."""

    # Plot the current as a function of voltage (without the trendline)
    plt.scatter(voltage, current, color="blue", label="Measured data", marker="o")

    # Add labels and title
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (I)")
    plt.title("Current vs Voltage")
    plt.grid(True)

    # Display a legend
    plt.legend()
    plt.savefig("/Users/merterol/uzh/Computational Science/Sem 3/PHY231/Exercise 6/current_vs_voltage.pdf", dpi=300)

    plt.close()
    print("ex1a executed and plot saved.")


# This is an example of creating 1b composing different functions together.
def chi2_1b(R):
    """Calculate chi2 in dependence of the resistance."""

    # Here is your code for exercise 1b.
    current_pred = current_ohmslaw(voltage, R)
    chi2val = chi2(current, current_pred, 0.2)
    return chi2val


def ex_1c():
    """Run exercise 1c."""

    # Define the range of resistances
    resistances = np.linspace(1, 100, 500)

    # Calculate chi2 for each resistance value
    chi2_values = [chi2_1b(R) for R in resistances]  # List of chi2 values for each resistance

    # Plot the chi2 value as a function of the resistance
    plt.figure()
    plt.plot(resistances, chi2_values, label=r"$\chi^2$ vs. Resistance")

    # Highlight the minimum chi2 value and corresponding resistance
    min_chi2 = min(chi2_values)
    best_R = resistances[np.argmin(chi2_values)]
    plt.scatter(best_R, min_chi2, color="red", label=f"Minimum $\\chi^2$ at R = {best_R:.2f} Ohms")

    plt.xlabel("Resistance (Ohms)")
    plt.ylabel(r"$\chi^2$")
    plt.title(r"$\chi^2$ vs. Resistance")
    plt.grid(True)
    plt.legend()

    plt.savefig("ex1c.png")
    plt.close()

    print(f"Best fit resistance: {best_R:.2f} Ohms with chi^2 = {min_chi2:.2f}")
    
def ex_1():
    ex_1a()
    ex_1c()

### ---- Exercise 2 ---- ###

def current_ohmslaw(U, R, bias=0):
    """Calculate the current with potential bias according to Ohm"s law."""
    return (U + bias) / R

def chi_squared(R, bias, voltage, current, uncertainty):
    """Calculate the chi-squared value for given resistance R and bias."""
    predicted_current = current_ohmslaw(voltage, R, bias)
    return np.sum(((current - predicted_current) / uncertainty) ** 2)

def fit_func(data, R, bias):
    """Function to be fitted, combining voltage, resistance, and bias."""
    return current_ohmslaw(data, R, bias)

initial_guess = [2.0, 0.0]

# Task (g): Fit using curve_fit
def ex2_g():
    params, cov = opt.curve_fit(fit_func, voltage_two, current_two, p0=initial_guess, sigma=uncertainties, absolute_sigma=True)
    best_R, best_bias = params
    std_dev_R, std_dev_bias = np.sqrt(np.diag(cov))
    
    return best_R, best_bias, cov, std_dev_R, std_dev_bias

# Task (a, b, c): Plot chi-squared as a function of R and overlay best fit
def ex2_abc():
    best_R, best_bias, cov, std_dev_R, std_dev_bias = ex2_g()
    
    R_values = np.linspace(0.5, 5, 400)
    chi2_values = [chi_squared(R, best_bias, voltage_two, current_two, uncertainties) for R in R_values]

    plt.figure(figsize=(10, 5))
    plt.plot(R_values, chi2_values, label="Chi-squared")
    plt.axvline(x=best_R, color="r", linestyle="--", label=f"Best R = {best_R:.2f} Ohms, Bias = {best_bias:.2f}")
    plt.xlabel("Resistance R (ohms)")
    plt.ylabel("Chi-squared")
    plt.title("Chi-squared vs. Resistance")
    plt.legend()
    plt.grid(True)
    plt.savefig("ex2.png")

# Task (d): Estimate uncertainty using Delta(chi^2) = 1 rule
def ex2_d():
    best_R, best_bias, cov, std_dev_R, std_dev_bias = ex2_g()
    R_values = np.linspace(0.5, 5, 400)
    chi2_values = [chi_squared(R, best_bias, voltage_two, current_two, uncertainties) for R in R_values]
    
    min_chi2 = chi_squared(best_R, best_bias, voltage_two, current_two, uncertainties)
    chi2_plus_1 = min_chi2 + 1
    confidence_band = [R for R, chi2 in zip(R_values, chi2_values) if chi2 <= chi2_plus_1]

    if confidence_band:
        R_uncertainty = (max(confidence_band) - min(confidence_band)) / 2
    else:
        R_uncertainty = None

    print(f"Estimated R = {best_R:.4f} ± {R_uncertainty:.4f} Ohms")

# Task (e): Chi-squared calculation with fixed bias
def ex2_e():
    best_R, best_bias, cov, std_dev_R, std_dev_bias = ex2_g()
    
    fixed_bias = 0.7
    chi2_fixed = chi_squared(best_R, fixed_bias, voltage_two, current_two, uncertainties)
    print(f"Chi-squared with fixed bias ({fixed_bias:.4f} A): {chi2_fixed:.4f}")

# Task (f): Goodness-of-fit comparison
def ex2_f():
    fixed_bias = 0.7
    best_R, best_bias, cov, std_dev_R, std_dev_bias = ex2_g()
    min_chi2 = chi_squared(best_R, best_bias, voltage_two, current_two, uncertainties)
    chi2_fixed = chi_squared(best_R, fixed_bias, voltage_two, current_two, uncertainties)
    
    print(f"Chi-squared per degree of freedom without bias: {(min_chi2 / (len(current_two) - 2)):.4f}")
    print(f"Chi-squared per degree of freedom with fixed bias: {(chi2_fixed / (len(current_two) - 2)):.4f}")

# Task (h): Analyzing covariance matrix
def ex2_h():
    best_R, best_bias, cov, std_dev_R, std_dev_bias = ex2_g()
    
    print("Covariance matrix:")
    print(cov)
    print(f"Standard deviation of R: {std_dev_R:.4f}")
    print(f"Standard deviation of bias: {std_dev_bias:.4f}")
    print(f"Correlation coefficient between R and bias: {cov[0, 1] / (std_dev_R * std_dev_bias):.4f}")
    
def ex_2():
    ex2_g()
    ex2_abc()
    ex2_d()
    ex2_e()
    ex2_f()
    ex2_h()

if __name__ == "__main__":
    # You can uncomment the exercises that you don"t want to run. Here we have just one,
    # but in general you can have more.
    
    ex_1()
    ex_2()
    #plt.show()  # comment out when submitting

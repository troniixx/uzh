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
    
def ex_2():
    """Run exercise 2."""
    
    #b
    # Define the range of resistances to test (you can adjust the range based on your data)
    resistances = np.linspace(1, 100, 500)
    
    # Calculate chi2 for each resistance value using chi2_2b
    chi2_values = [chi2_2b(R) for R in resistances]
    
    # Plot the chi2 value as a function of resistance
    plt.figure()
    plt.plot(resistances, chi2_values, label=r"$\chi^2$ vs. Resistance")
    
    # Highlight the minimum chi2 value and corresponding resistance
    min_chi2 = min(chi2_values)
    best_R = resistances[np.argmin(chi2_values)]
    plt.scatter(best_R, min_chi2, color="red", label=f"Minimum $\\chi^2$ at R = {best_R:.2f} Ohms")
    
    # Add labels and title
    plt.xlabel("Resistance (Ohms)")
    plt.ylabel(r"$\chi^2$")
    plt.title(r"$\chi^2$ vs. Resistance")
    plt.grid(True)
    plt.legend()
    
    # Save the chi2 vs resistance plot
    plt.savefig("ex2_chi2_vs_R.png")
    plt.close()

    # Print the best fit resistance and corresponding chi2 value
    print(f"Best fit resistance: {best_R:.2f} Ohms with chi^2 = {min_chi2:.2f}")
    
    
    #c
    # Now overlay the best fit function on the original data (current vs voltage)
    current_pred = current_ohmslaw(voltage, best_R)  # Predicted current using best fit resistance

    # Plot the original data
    plt.scatter(voltage, current, color="blue", label="Measured data", marker="o")
    
    # Plot the best fit function
    plt.plot(voltage, current_pred, color="red", label=f"Best fit: R = {best_R:.2f} Ohms")

    # Add labels and title
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (I)")
    plt.title("Current vs Voltage with Best Fit Overlay")
    plt.grid(True)
    plt.legend()

    # Save the plot with the best fit function
    plt.savefig("ex2_best_fit_overlay.png")
    plt.close()

    print("ex_2 executed with best fit overlay plot saved.")

    
def ex_2d():
    """Run exercise 2 with uncertainty on resistance."""

    # Define the range of resistances to test (you can adjust the range based on your data)
    resistances = np.linspace(1, 100, 500)
    
    # Calculate chi2 for each resistance value using chi2_2b
    chi2_values = [chi2_2b(R) for R in resistances]
    
    # Plot the chi2 value as a function of resistance
    plt.figure()
    plt.plot(resistances, chi2_values, label=r"$\chi^2$ vs. Resistance")
    
    # Highlight the minimum chi2 value and corresponding resistance
    min_chi2 = min(chi2_values)
    best_R = resistances[np.argmin(chi2_values)]
    plt.scatter(best_R, min_chi2, color="red", label=f"Minimum $\\chi^2$ at R = {best_R:.2f} Ohms")
    
    # Add labels and title
    plt.xlabel("Resistance (Ohms)")
    plt.ylabel(r"$\chi^2$")
    plt.title(r"$\chi^2$ vs. Resistance")
    plt.grid(True)
    plt.legend()
    
    # Save the chi2 vs resistance plot
    plt.savefig("ex2_chi2_vs_R_with_uncertainty.png")
    plt.close()

    # Print the best fit resistance and corresponding chi2 value
    print(f"Best fit resistance: {best_R:.2f} Ohms with chi^2 = {min_chi2:.2f}")

    # Now, apply the Δχ² = 1 rule to find the uncertainty on R
    tolerance = 1
    chi2_tolerance = min_chi2 + tolerance

    # Find the range of R where chi2 is within tolerance
    lower_R = np.min(resistances[chi2_values <= chi2_tolerance])
    upper_R = np.max(resistances[chi2_values <= chi2_tolerance])

    # Calculate the uncertainty on R
    delta_R = (upper_R - lower_R) / 2

    # Print the uncertainty on R
    print(f"Uncertainty on R: ±{delta_R:.2f} Ohms")

    # Check compatibility with the known value of R = 2 Ohms
    known_R = 2
    if lower_R <= known_R <= upper_R:
        print(f"The known value R = {known_R} Ohms is compatible with the uncertainty range.")
    else:
        print(f"The known value R = {known_R} Ohms is NOT compatible with the uncertainty range.")

    # Now overlay the best fit function on the original data (current vs voltage)
    current_pred = current_ohmslaw(voltage, best_R)  # Predicted current using best fit resistance

    # Plot the original data
    plt.scatter(voltage, current, color="blue", label="Measured data", marker="o")
    
    # Plot the best fit function
    plt.plot(voltage, current_pred, color="red", label=f"Best fit: R = {best_R:.2f} Ohms")

    # Add labels and title
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (I)")
    plt.title("Current vs Voltage with Best Fit Overlay")
    plt.grid(True)
    plt.legend()

    # Save the plot with the best fit function
    plt.savefig("ex2_best_fit_overlay_with_uncertainty.png")
    plt.close()

    print("ex_2 executed with best fit overlay plot and uncertainty range.")

# e)
def current_ohmslaw_with_bias(U, R, epsilon_bias=0.7):
    """Calculate the current according to Ohm's Law with a bias term."""
    return U / R + epsilon_bias  # Ohm's law with a fixed bias

def chi2_with_bias(R, epsilon_bias=0.7):
    """Calculate chi2 in dependence of the resistance considering uncertainties and bias."""
    # Calculate the predicted current using Ohm's Law with bias
    current_pred = current_ohmslaw_with_bias(voltage, R, epsilon_bias)
    
    # Calculate chi2, including the uncertainties
    chi2val = np.sum(((current - current_pred) ** 2) / (uncertainties ** 2))
    
    return chi2val

def ex_2_with_bias():
    """Run exercise 2 with bias and uncertainty on resistance."""
    
    # Define the range of resistances to test
    resistances = np.linspace(1, 100, 500)
    
    # Calculate chi2 for each resistance value using chi2_with_bias
    chi2_values = [chi2_with_bias(R, epsilon_bias=0.7) for R in resistances]
    
    # Plot the chi2 value as a function of resistance
    plt.figure()
    plt.plot(resistances, chi2_values, label=r"$\chi^2$ vs. Resistance")
    
    # Highlight the minimum chi2 value and corresponding resistance
    min_chi2 = min(chi2_values)
    best_R = resistances[np.argmin(chi2_values)]
    plt.scatter(best_R, min_chi2, color="red", label=f"Minimum $\\chi^2$ at R = {best_R:.2f} Ohms")
    
    # Add labels and title
    plt.xlabel("Resistance (Ohms)")
    plt.ylabel(r"$\chi^2$")
    plt.title(r"$\chi^2$ vs. Resistance with Bias")
    plt.grid(True)
    plt.legend()
    
    # Save the chi2 vs resistance plot
    plt.savefig("ex2_chi2_vs_R_with_bias.png")
    plt.close()

    # Print the best fit resistance and corresponding chi2 value
    print(f"Best fit resistance: {best_R:.2f} Ohms with chi^2 = {min_chi2:.2f}")

    # Now, apply the Δχ² = 1 rule to find the uncertainty on R
    tolerance = 1
    chi2_tolerance = min_chi2 + tolerance

    # Find the range of R where chi2 is within tolerance
    lower_R = np.min(resistances[chi2_values <= chi2_tolerance])
    upper_R = np.max(resistances[chi2_values <= chi2_tolerance])

    # Calculate the uncertainty on R
    delta_R = (upper_R - lower_R) / 2

    # Print the uncertainty on R
    print(f"Uncertainty on R: ±{delta_R:.2f} Ohms")

    # Check compatibility with the known value of R = 2 Ohms
    known_R = 2
    if lower_R <= known_R <= upper_R:
        print(f"The known value R = {known_R} Ohms is compatible with the uncertainty range.")
    else:
        print(f"The known value R = {known_R} Ohms is NOT compatible with the uncertainty range.")

    # Now overlay the best fit function on the original data (current vs voltage)
    current_pred = current_ohmslaw_with_bias(voltage, best_R, epsilon_bias=0.7)  # Predicted current using best fit resistance

    # Plot the original data
    plt.scatter(voltage, current, color="blue", label="Measured data", marker="o")
    
    # Plot the best fit function
    plt.plot(voltage, current_pred, color="red", label=f"Best fit: R = {best_R:.2f} Ohms with bias")

    # Add labels and title
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (I)")
    plt.title("Current vs Voltage with Best Fit Overlay (with Bias)")
    plt.grid(True)
    plt.legend()

    # Save the plot with the best fit function
    plt.savefig("ex2_best_fit_overlay_with_bias.png")
    plt.close()

    print("ex_2 with bias executed and best fit overlay plot saved.")
    

def reduced_chi2(chi2_value, ndf):
    """Calculate the reduced chi2 value."""
    return chi2_value / ndf

def goodness_of_fit_probability(chi2_value, ndf):
    """Calculate the goodness-of-fit probability (p-value)."""
    # Using the survival function (1 - CDF) to get the p-value
    return 1 - chi2.cdf(chi2_value, ndf)

def ex_2_compare_bias():
    """Compare chi2/ndf with and without the bias offset and calculate GoF probability."""
    
    # Case 1: Without bias (using chi2_1b)
    resistances_no_bias = np.linspace(1, 100, 500)
    chi2_values_no_bias = [chi2_1b(R) for R in resistances_no_bias]
    min_chi2_no_bias = min(chi2_values_no_bias)
    best_R_no_bias = resistances_no_bias[np.argmin(chi2_values_no_bias)]
    
    # Calculate reduced chi2 and GoF probability for no bias
    ndf_no_bias = len(voltage) - 1  # 1 parameter (R) fitted
    reduced_chi2_no_bias = reduced_chi2(min_chi2_no_bias, ndf_no_bias)
    p_value_no_bias = goodness_of_fit_probability(min_chi2_no_bias, ndf_no_bias)
    
    # Case 2: With bias (using chi2_with_bias)
    chi2_values_with_bias = [chi2_with_bias(R, epsilon_bias=0.7) for R in resistances_no_bias]
    min_chi2_with_bias = min(chi2_values_with_bias)
    best_R_with_bias = resistances_no_bias[np.argmin(chi2_values_with_bias)]
    
    # Calculate reduced chi2 and GoF probability for with bias
    ndf_with_bias = len(voltage) - 2  # 2 parameters (R and bias) fitted
    reduced_chi2_with_bias = reduced_chi2(min_chi2_with_bias, ndf_with_bias)
    p_value_with_bias = goodness_of_fit_probability(min_chi2_with_bias, ndf_with_bias)
    
    # Print results
    print(f"Without bias:")
    print(f"  Best fit resistance: {best_R_no_bias:.2f} Ohms")
    print(f"  Minimum chi2: {min_chi2_no_bias:.2f}")
    print(f"  Reduced chi2: {reduced_chi2_no_bias:.2f}")
    print(f"  Goodness-of-fit probability: {p_value_no_bias:.4f}")
    
    print(f"\nWith bias:")
    print(f"  Best fit resistance: {best_R_with_bias:.2f} Ohms")
    print(f"  Minimum chi2: {min_chi2_with_bias:.2f}")
    print(f"  Reduced chi2: {reduced_chi2_with_bias:.2f}")
    print(f"  Goodness-of-fit probability: {p_value_with_bias:.4f}")
    
    # Plot the chi2 vs resistance for both cases
    plt.figure(figsize=(10, 6))
    plt.plot(resistances_no_bias, chi2_values_no_bias, label=r"$\chi^2$ vs. Resistance (without bias)", color='blue')
    plt.plot(resistances_no_bias, chi2_values_with_bias, label=r"$\chi^2$ vs. Resistance (with bias)", color='red')
    
    plt.xlabel("Resistance (Ohms)")
    plt.ylabel(r"$\chi^2$")
    plt.title("Chi-squared vs Resistance for with and without bias")
    plt.grid(True)
    plt.legend()
    plt.savefig("chi2_comparison_with_without_bias.png")
    plt.close()

    print("Comparison plot saved as chi2_comparison_with_without_bias.png")




def ex_2g():
    """Run exercise 2g."""
    # Here we need to use scipy.optimize.curve_fit to fit the data.
    # make sure to first read the documentation for curve_fit
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

    # NOTE: curve_fit already calculates the chi2 value (including error) for us!
    # hint: maybe look for simple examples around or play around if it is not clear on how to use curve_fit.

    popt, pcov = opt.curve_fit(...)
    print("ex2g executed.")

def ex2_main():
    pass

if __name__ == "__main__":
    # You can uncomment the exercises that you don"t want to run. Here we have just one,
    # but in general you can have more.
    #ex_1a()
    #ex_1c()
    ex_2()
    #ex_2g()
    #plt.show()  # comment out when submitting

import numpy as np
import scipy.optimize as opt
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

DATA = np.loadtxt("/Users/merterol/uzh/Computational Science/Sem 3/PHY231/Exercise 6/current_measurements.txt")  # Load the data from the file
DATA_UNCERT = np.loadtxt("/Users/merterol/uzh/Computational Science/Sem 3/PHY231/Exercise 6/current_measurements_uncertainties.txt")  # Load the uncertainties from the file

voltage = DATA[:, 0]  # Extract the voltage from the data
current = DATA[:, 1]  # Extract the current from the data
uncertanties = DATA_UNCERT[:, 2]  # Extract the uncertainties from the data

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
    chi2val = chi2(current, current_pred, uncertanties)
    return chi2val


def ex_1c():
    """Run exercise 1c."""

    # Define the range of resistances
    resistances = np.linspace(1, 100, 500)  # You can adjust start, stop, and number of steps

    # Calculate chi2 for each resistance value
    chi2_values = [chi2_1b(R) for R in resistances]  # List of chi2 values for each resistance

    # Plot the chi2 value as a function of the resistance
    plt.figure()  # Create a new figure

    plt.plot(resistances, chi2_values, label=r"$\chi^2$ vs. Resistance")

    # Highlight the minimum chi2 value and corresponding resistance
    min_chi2 = min(chi2_values)
    best_R = resistances[np.argmin(chi2_values)]
    plt.scatter(best_R, min_chi2, color="red", label=f"Minimum $\\chi^2$ at R = {best_R:.2f} Ohms")

    # Add labels, title, and legend
    plt.xlabel("Resistance (Ohms)")
    plt.ylabel(r"$\chi^2$")
    plt.title(r"$\chi^2$ vs. Resistance")
    plt.grid(True)
    plt.legend()

    # Save the plot as a PNG file
    plt.savefig("ex1c.png")

    # Close the figure
    plt.close()

    # Print the best fit resistance value and chi^2
    print(f"Best fit resistance: {best_R:.2f} Ohms with chi^2 = {min_chi2:.2f}")


def ex_2g():
    """Run exercise 2g."""
    # Here we need to use scipy.optimize.curve_fit to fit the data.
    # make sure to first read the documentation for curve_fit
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

    # NOTE: curve_fit already calculates the chi2 value (including error) for us!
    # hint: maybe look for simple examples around or play around if it is not clear on how to use curve_fit.

    popt, pcov = opt.curve_fit(...)
    print("ex2g executed.")


if __name__ == "__main__":
    # You can uncomment the exercises that you don"t want to run. Here we have just one,
    # but in general you can have more.
    #ex_1a()
    ex_1c()
    #ex_2g()
    #plt.show()  # comment out when submitting

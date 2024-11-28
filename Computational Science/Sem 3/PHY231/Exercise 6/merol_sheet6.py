import numpy as np
import matplotlib.pyplot as plt

# ---- Exercise 1 ---- #

def load_data(filename="current_measurements.txt"):
    """Load voltage and current measurements from file"""
    data = np.loadtxt(filename)
    voltage = data[:, 0]
    current = data[:, 1]
    return voltage, current

def calculate_chi_square(func, x_data, y_data, uncertainty, params):
    """Calculate chi-square value for a given function and data"""
    y_predicted = func(x_data, *params)
    chi_square = np.sum(((y_data - y_predicted) / uncertainty) ** 2)
    return chi_square

def ohms_law(voltage, resistance):
    """Define Ohm"s law: I = V/R"""
    return voltage / resistance

def analyze_resistance_range(voltage, current, uncertainty, r_range):
    """Calculate chi-square values for a range of resistance values"""
    chi_squares = []
    for r in r_range:
        chi_sq = calculate_chi_square(ohms_law, voltage, current, uncertainty, (r,))
        chi_squares.append(chi_sq)
    return np.array(chi_squares)

def plot_measurements(voltage, current, uncertainty, best_fit_r):
    """Plot current vs voltage with error bars and best-fit line"""
    plt.figure(figsize=(10, 6))
    
    # Plot data points with error bars
    plt.errorbar(voltage, current, yerr=uncertainty, fmt="o", label="Measurements")
    
    # Add best-fit line
    v_line = np.linspace(0, max(voltage)*1.1, 100)
    i_line = ohms_law(v_line, best_fit_r)
    plt.plot(v_line, i_line, "r-", label=f"Best Fit (R = {best_fit_r:.2f} Ω)")
    
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (A)")
    plt.title("Current vs Voltage Measurements with Best Fit Line")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_chi_square(r_range, chi_squares, best_fit_r, uncertainty_range=None):
    """Plot chi-square vs resistance with best-fit line and uncertainty range"""
    plt.figure(figsize=(10, 6))
    
    plt.plot(r_range, chi_squares, "b-", label="chi^2 values")
    
    min_chi = np.min(chi_squares)
    plt.axvline(x=best_fit_r, color="r", linestyle="--", 
                label=f"Best Fit R = {best_fit_r:.2f} Ω")
    
    if uncertainty_range is not None:
        r_lower, r_upper = uncertainty_range
        plt.axhline(y=min_chi + 1, color="g", linestyle=":",label="Δchi^2 = 1")
        plt.axvline(x=r_lower, color="g", linestyle=":")
        plt.axvline(x=r_upper, color="g", linestyle=":")
        
    plt.xlabel("Resistance (Ω)")
    plt.ylabel("chi^2")
    plt.title("chi^2 vs Resistance")
    plt.grid(True)
    plt.legend()
    plt.show()

def linear_regression(x, y, uncertainty):
    w = 1 / (uncertainty ** 2)
    delta = np.sum(w) * np.sum(w * x * x) - (np.sum(w * x)) ** 2
    m = (np.sum(w) * np.sum(w * x * y) - np.sum(w * x) * np.sum(w * y)) / delta
    return m

def find_uncertainty_range(r_range, chi_squares, min_chi_square):
    delta_chi_square = chi_squares - min_chi_square
    indices = np.where(delta_chi_square <= 1)[0]
    return r_range[indices[0]], r_range[indices[-1]]

def ex1_main():
    voltage, current = load_data()
    uncertainty = 0.2
    
    r_range = np.linspace(1, 10, 1000)
    chi_squares = analyze_resistance_range(voltage, current, uncertainty, r_range)

    best_fit_index = np.argmin(chi_squares)
    best_fit_r = r_range[best_fit_index]
    min_chi_square = chi_squares[best_fit_index]
    
    plot_measurements(voltage, current, uncertainty, best_fit_r)

    r_lower, r_upper = find_uncertainty_range(r_range, chi_squares, min_chi_square)
    uncertainty_range = (r_lower, r_upper)
    
    plot_chi_square(r_range, chi_squares, best_fit_r, uncertainty_range)
    
    analytical_r = linear_regression(voltage, current, uncertainty)
    uncertainty_r = (r_upper - r_lower) / 2
    
    return best_fit_r, analytical_r, uncertainty_r, min_chi_square

def ex1():
    best_fit_r, analytical_r, uncertainty_r, min_chi_square = ex1_main()
    print(f"Best fit resistance: {best_fit_r:.3f} Ω")
    print(f"Analytical resistance: {analytical_r:.3f} Ω")
    print(f"Resistance uncertainty: ±{uncertainty_r:.3f} Ω")
    print(f"Minimum chi^2: {min_chi_square:.3f}")
    
# ---- Exercise 2 ---- #

from scipy.optimize import curve_fit

data = np.loadtxt("current_measurements_uncertainties.txt")
voltage = data[:, 0]
current = data[:, 1]
current_uncertainty = data[:, 2]

def ohms_law_two(voltage, resistance, bias=0):
    return voltage / resistance + bias

def chi_squared_two(resistance, bias=0):
    model = ohms_law_two(voltage, resistance, bias)
    return np.sum(((current - model) / current_uncertainty)**2)

R_range = np.linspace(0, 3, 100)
chi2_values = [chi_squared_two(R) for R in R_range]

# (b) Plot chi-squared as a function of resistance
def ex2_b():
    R_best_fit = ex2_c()
    
    min_chi2_index = np.argmin(chi2_values)
    min_chi2 = chi2_values[min_chi2_index]
    R_min_chi2 = R_range[min_chi2_index]

    plt.plot(R_range, chi2_values, label="chi^2")

    plt.axvline(x=R_min_chi2, color="red", linestyle="--", label=f"Min chi^2 at R = {R_min_chi2:.2f}")
    plt.axvline(x=R_best_fit, color="green", linestyle="--", label=f"Best-fit R = {R_best_fit:.2f}")
    plt.legend()

    plt.xlabel("Resistance (Ohm)")
    plt.ylabel("chi^2")
    plt.title("Chi-Squared as a Function of Resistance")
    plt.grid(True)
    plt.savefig("ex2.png")


# (c) Find minimum chi-squared and best-fit R
def ex2_c():
    R_best_fit = R_range[np.argmin(chi2_values)]
    print(f"Best-fit resistance: {R_best_fit:.4f}")
    
    return R_best_fit

# (d) Uncertainty on R using Δ(chi^2) = 1 rule
def ex2_d():
    R_best_fit = ex2_c()
    
    delta_chi2 = 1
    R_uncertainty = np.interp(chi2_values[np.argmin(chi2_values)] + delta_chi2, chi2_values[::-1], R_range[::-1]) - R_best_fit
    print(f"Uncertainty on R: {R_uncertainty:.4f}")

# (e) Add bias offset and recalculate
def ex2_e():
    bias = 0.7
    R_range_bias = np.linspace(0, 3, 100)
    chi2_values_bias = [chi_squared_two(R, bias) for R in R_range_bias]
    R_best_fit_bias = R_range_bias[np.argmin(chi2_values_bias)]
    print(f"Best-fit resistance with bias: {R_best_fit_bias:.4f}")
    
    return R_range_bias, R_best_fit_bias, chi2_values, chi2_values_bias

# (f) Compare chi-squared/ndof and calculate goodness-of-fit probability
def ex2_f():
    R_range_bias, R_best_fit_bias, chi2_values, chi2_values_bias = ex2_e()
    
    ndof = len(voltage) - 2  # Degrees of freedom
    chi2_ndof = chi2_values[np.argmin(chi2_values)] / ndof
    chi2_ndof_bias = chi2_values_bias[np.argmin(chi2_values_bias)] / ndof
    print(f"chi^2/ndof without bias: {chi2_ndof:.4f}")
    print(f"chi^2/ndof with bias: {chi2_ndof_bias:.4f}")

# (g) Use curve_fit for simultaneous optimization
def ex2_g():
    R_best_fit = ex2_c()
    bias = 0.7
    
    popt, pcov = curve_fit(ohms_law_two, voltage, current, sigma=current_uncertainty, absolute_sigma=True, p0=[R_best_fit, bias])
    R_fit, bias_fit = popt
    print(f"Curve_fit resistance: {R_fit:.4f}")
    print(f"Curve_fit bias: {bias_fit:.4f}")
    
    return pcov

# (h) Calculate uncertainties and correlation coefficient
def ex2_h():
    pcov = ex2_g()
    
    perr = np.sqrt(np.diag(pcov))
    R_fit_uncertainty, bias_fit_uncertainty = perr
    corr_coeff = pcov[0, 1] / (perr[0] * perr[1])
    print(f"Uncertainty on R from curve_fit: {R_fit_uncertainty:.4f}")
    print(f"Correlation coefficient: {corr_coeff:.4f}")
    
def ex2():
    ex2_b()
    ex2_c()
    ex2_d()
    ex2_e()
    ex2_f()
    ex2_h()

# ---- Runner ---- #

if __name__ == "__main__":
    ex1()
    ex2()

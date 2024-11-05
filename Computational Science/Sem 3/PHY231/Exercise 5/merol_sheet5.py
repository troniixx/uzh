# author: Mert Erol, 20-915-245, merol

from math import sqrt
from scipy.stats import norm

def ex_1():
    print("Exercise 1:")
    
    print("Part a:")
    
    print("Part b:")
    
    print("Part c:")
    
    print("Part d:")
    
    print("Part e:")
    
    print("Part f:")

def ex_2():
    print("Exercise 2:")
    print("Part a:")
    
    counts = 240  # seconds
    usv_per_hour = 0.1  # corresponding to 0.1 μSv per hour

    # Mean and standard deviation
    mean_usv_per_hour = usv_per_hour
    std_dev_usv_per_hour = usv_per_hour * sqrt(counts) / counts

    # 68% interval is mean +/- 1 standard deviation
    lower_68_interval = mean_usv_per_hour - std_dev_usv_per_hour
    upper_68_interval = mean_usv_per_hour + std_dev_usv_per_hour

    print("68% Confidence Interval:")
    print(f"Lower limit: {lower_68_interval:.4f} μSv per hour")
    print(f"Upper limit: {upper_68_interval:.4f} μSv per hour")
    
    print("Part b:")
    # z-score for 90% confidence
    z_90 = norm.ppf(0.9)

    # 90% upper confidence limit
    upper_90_limit = mean_usv_per_hour + z_90 * std_dev_usv_per_hour

    print("90% Upper Confidence Limit:")
    print(f"Upper limit: {upper_90_limit:.4f} μSv per hour")
    
    print("Part c:")
    # Convert 1000 μSv per year to μSv per hour (assuming 8760 hours in a year)
    annual_limit_usv_per_hour = 1000 / 8760
    is_below_annual_limit = upper_90_limit < annual_limit_usv_per_hour

    print("Comparison with Annual Radiation Requirement:")
    print(f"90% confidence limit ({upper_90_limit:.4f} μSv per hour) "
    f"{'is below' if is_below_annual_limit else 'exceeds'} the annual limit "
    f"({annual_limit_usv_per_hour:.4f} μSv per hour)")
    

def ex_3():
    print("Exercise 3:")
    m_measured = 90e24  # kg
    d_measured = 5.2e7  # m
    sigma_m = 5e24      # kg
    sigma_d = 0.2e7     # m
    rho = -0.6          # correlation coefficient
    
    m_uranus = 86.8e24  # kg
    d_uranus = 51.1e6   # m
    
    m_neptune = 102.0e24  # kg
    d_neptune = 49.5e6    # m
    
    sigma_combined = combined_uncertainty(sigma_m, sigma_d, rho)
    print("Combined Uncertainty (sigma_combined):", sigma_combined)
    
    diff_uranus_m = abs(m_measured - m_uranus)
    diff_uranus_d = abs(d_measured - d_uranus)
    
    sigma_uranus = sqrt((diff_uranus_m / sigma_m)**2 + (diff_uranus_d / sigma_d)**2)
    print("Standard Deviations from Uranus:", sigma_uranus)
    
    diff_neptune_m = abs(m_measured - m_neptune)
    diff_neptune_d = abs(d_measured - d_neptune)

    sigma_neptune = sqrt((diff_neptune_m / sigma_m)**2 + (diff_neptune_d / sigma_d)**2)
    print("Standard Deviations from Neptune:", sigma_neptune)

# Support function for ex_3
def combined_uncertainty(sigma_m, sigma_d, rho):
    return sqrt(sigma_m**2 + sigma_d**2 + 2 * rho * sigma_m * sigma_d)


if __name__ == "__main__":
    ex_1()
    ex_2()
    ex_3()
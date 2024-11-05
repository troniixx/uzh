# author: Mert Erol, 20-915-245, merol

from math import sqrt
from scipy.stats import norm
from scipy.stats import poisson
from scipy.stats import ttest_ind
from statsmodels.stats.proportion import proportions_ztest

def ex_1():
    print("Exercise 1:")
    
    print("Part a:")
    predicted_rk = 1.0
    measured_rk = 0.83
    sigma_rk = 0.06

    z_score_a = (measured_rk - predicted_rk) / sigma_rk

    # Calculate two-tailed p-value
    p_value_a = 2 * norm.cdf(-abs(z_score_a))
    print("P-value for (a):", p_value_a)

    print("Part b:")
    
    predicted_g = 9.70
    measured_g = 9.90
    sigma_predicted_g = 0.10
    sigma_measured_g = 0.09

    sigma_combined_b = (sigma_predicted_g**2 + sigma_measured_g**2)**0.5
    z_score_b = (measured_g - predicted_g) / sigma_combined_b

    # Calculate two-tailed p-value
    p_value_b = 2 * norm.cdf(-abs(z_score_b))
    print("P-value for (b):", p_value_b)
    
    print("Part c:")
    expected_events = 1.5
    observed_events = 6

    # Calculate one-tailed p-value
    p_value_c = 1 - poisson.cdf(observed_events - 1, expected_events)
    print("P-value for (c):", p_value_c)
    
    print("Part d:")
    count_2019 = 50
    count_2020 = 60
    n_2019 = n_2020 = 50 + 60

    counts = [count_2019, count_2020]
    nobs = [n_2019, n_2020]

    # Perform two-sample proportion z-test
    _, p_value_d = proportions_ztest(counts, nobs)
    print("P-value for (d):", p_value_d)
    
    print("Part e:")
    expected_infection_rate = 3000 / 1e6
    trial_population = 8924
    observed_infections = 3

    observed_infection_rate = observed_infections / trial_population

    z_score_e = (observed_infection_rate - expected_infection_rate) / sqrt((expected_infection_rate * (1 - expected_infection_rate)) / trial_population)

    # Calculate one-tailed p-value
    p_value_e = norm.cdf(-abs(z_score_e))
    print("P-value for (e):", p_value_e)
    
    print("Part f:")
    hockey_heights = [187, 185, 183, 176, 190]
    soccer_heights = [170, 174, 186, 178, 185, 176, 182, 184, 179, 189, 177]

    # Independent two-sample t-test (unknown standard deviation)
    _, p_value_f_ttest = ttest_ind(hockey_heights, soccer_heights, equal_var=False)
    print("P-value for (f) using t-test:", p_value_f_ttest)

    # Z-test if standard deviation is known (sigma = 5 cm)
    sigma_known = 5
    mean_diff = abs(sum(hockey_heights)/len(hockey_heights) - sum(soccer_heights)/len(soccer_heights))
    n_hockey = len(hockey_heights)
    n_soccer = len(soccer_heights)
    sigma_combined_f = sigma_known * sqrt(1/n_hockey + 1/n_soccer)
    z_score_f = mean_diff / sigma_combined_f
    p_value_f_ztest = 2 * norm.cdf(-abs(z_score_f))
    print("P-value for (f) using z-test:", p_value_f_ztest)
    
    print("\n")

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
    
    print("\n")
    
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
    
    sigma_combined = sqrt(sigma_m**2 + sigma_d**2 + 2 * rho * sigma_m * sigma_d)
    print("Combined Uncertainty (sigma_combined):", sigma_combined)
    
    diff_uranus_m = abs(m_measured - m_uranus)
    diff_uranus_d = abs(d_measured - d_uranus)
    
    sigma_uranus = sqrt((diff_uranus_m / sigma_m)**2 + (diff_uranus_d / sigma_d)**2)
    print("Standard Deviations from Uranus:", sigma_uranus)
    
    diff_neptune_m = abs(m_measured - m_neptune)
    diff_neptune_d = abs(d_measured - d_neptune)

    sigma_neptune = sqrt((diff_neptune_m / sigma_m)**2 + (diff_neptune_d / sigma_d)**2)
    print("Standard Deviations from Neptune:", sigma_neptune)

if __name__ == "__main__":
    ex_1()
    ex_2()
    ex_3()
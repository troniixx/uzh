import numpy as np
from math import sqrt, ceil
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
    s = 0
    for i in range(len(x)):
        s += x[i]
    mean = s / len(x)
    return mean


def std(x):
    """Calculate the standard deviation for an array-like object x."""
    s = 0
    for i in range(len(x)):
        s += (x[i] - mean(x))**2
    std = np.sqrt(s / (len(x) - 1))
    return std


def variance(x):
    """Calculate the variance for an array-like object x."""
    # here goes your code
    s = 0
    for i in range(len(x)):
        s += (x[i] - mean(x))**2
    variance = s / (len(x) - 1)
    return variance


def mean_uncertainty(x):
    """Calculate the uncertainty in the mean for an array-like object x."""
    # here goes your code
    s = std(x)
    # replace this with your code
    return s / sqrt(len(x))  # replace this with your code

def covariance(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    cov = sum((x_i - mean_x) * (y_i - mean_y) for x_i, y_i in zip(x, y)) / len(x)
    
    return cov

def correlation(x, y):
    cov = covariance(x, y)
    std_x = std(x)
    std_y = std(y)
    
    return cov / (std_x * std_y)


def ex1():
    data = np.loadtxt("data/ironman.txt")
    total_rank = data[:, 0]
    age = 2010 - data[:, 1]
    total_time = data[:, 2]
    swimming_time = data[:, 3]
    cycling_time = data[:, 5]
    running_time = data[:, 7]


    print("\na\n")
    mean_age = mean(age)
    mean_age_uncertainty = mean_uncertainty(age)
    print("Using my own functions:")
    print(f"The mean age of the participants is {mean_age:.4f} +/- {mean_age_uncertainty:.4f} years.")
    print("Using numpy functions:")
    print(f"The mean age of the participants is {np.mean(age):.4f} +/- {np.std(age) / sqrt(len(age)):.4f} years.")

    mean_total_time = mean(total_time)
    mean_total_time_uncertainty = mean_uncertainty(total_time)
    
    print("\n")
    print("Using my own functions:")
    print(f"The mean total time of the participants is {mean_total_time:.4f} +/- {mean_total_time_uncertainty:.4f} hours.")
    print("Using numpy functions:")
    print(f"The mean total time of the participants is {np.mean(total_time):.4f} +/- {np.std(total_time) / sqrt(len(total_time)):.4f} hours.")

    print("\nb\n")
    younger_group = [time for a, time in zip(age, total_time) if a < 35]
    older_group = [time for a, time in zip(age, total_time) if a >= 35]

    younger_mean = mean(younger_group)
    older_mean = mean(older_group)
    younger_uncertainty = mean_uncertainty(younger_group)
    older_uncertainty = mean_uncertainty(older_group)

    print("\n")
    print(f"The mean time of the younger group is {younger_mean:.4f} +/- {younger_uncertainty:.4f} hours.")
    print(f"The mean time of the older group is {older_mean:.4f} +/- {older_uncertainty:.4f} hours.")

    print("Range younger = [675.57, 682.87] / range older = [701.99, 706.87]")
    print("Ranges do not overlap!")
    print("The younger group is significantly faster than the older group, with a mean time difference of about 25.21 hours.")

    print("\nc & d \n") #(chatgpt had to help me with this one)
    def histo(data, n_bins):
        bins = np.linspace(min(data), max(data), n_bins + 1)
        bin_centers = 0.5 * (bins[:-1] + bins[1:])
        bin_means = np.zeros(n_bins)
        bin_uncertainties = np.zeros(n_bins)
        bin_counts = np.zeros(n_bins)
        bin_indices = np.digitize(data, bins)
        
        for i in range(1, n_bins + 1):
            
            bin_data = data[bin_indices == i]
            
            if len(bin_data) > 0:
                
                bin_means[i - 1] = np.mean(bin_data)
                bin_uncertainties[i - 1] = np.std(bin_data) / np.sqrt(len(bin_data))
                bin_counts[i - 1] = len(bin_data)
        
        return bin_centers, bin_means, bin_uncertainties, bin_counts

    def stats_histo(centers, counts):
        mean = np.sum(centers * counts) / np.sum(counts)
        variance = np.sum(counts * (centers - mean) ** 2) / np.sum(counts)
        std_dev = np.sqrt(variance)
        
        return mean, variance, std_dev
    
    bins_age = int(np.ceil(np.log2(len(age)) + 1))
    bins_tot_tim = int(np.ceil(np.log2(len(total_time)) + 1))
    age_bin_width = (max(age) - min(age)) / bins_age
    total_time_bin_width = (max(total_time) - min(total_time)) / bins_tot_tim

    age_bin_centers, age_bin_means, age_bin_uncertainties, age_bin_counts = histo(age, bins_age)
    total_time_bin_centers, total_time_bin_means, total_time_bin_uncertainties, total_time_bin_counts = histo(total_time, bins_tot_tim)

    plt.figure(figsize=(10, 6))
    plt.bar(age_bin_centers, age_bin_means, width=(age_bin_centers[1] - age_bin_centers[0]), yerr=age_bin_uncertainties, capsize=5, color="green", label="Age Distribution")
    plt.xlabel("Age in years")
    plt.ylabel("Mean Age in years")
    plt.title("Mean Age with Uncertainty")
    plt.grid(True)
    plt.legend()
    plt.savefig("age_distribution.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.bar(total_time_bin_centers, total_time_bin_means, width=(total_time_bin_centers[1] - total_time_bin_centers[0]), yerr=total_time_bin_uncertainties, capsize=5, color="green", label="Total Time Distribution")
    plt.xlabel("Total Time in minutes")
    plt.ylabel("Mean Total Time in minutes")
    plt.title("Mean Total Time Distribution with Uncertainty")
    plt.grid(True)
    plt.legend()
    plt.savefig("total_time_distribution_sturge.png")
    plt.close()

    age_mean_hist, age_variance_hist, age_std_hist = stats_histo(age_bin_centers, age_bin_counts)
    total_time_mean_hist, total_time_variance_hist, total_time_std_hist = stats_histo(total_time_bin_centers, total_time_bin_counts)

    print(f"Age Stats Histo: Mean = {age_mean_hist:.4f}, Variance = {age_variance_hist:.4f}, Standard Deviation = {age_std_hist:.4f}")
    print(f"Total Time Histo: Mean = {total_time_mean_hist:.4f}, Variance = {total_time_variance_hist:.4f}, Standard Deviation = {total_time_std_hist:.4f}\n")

    
    print("\nConclusion:")
    print("The calculated values from the histogram are close to values calculated in a.")
    print("After trying different rules I got from Google, I would choose Sturges rule over the rest")
    print(f"Bin number is correlated with bin width, so we can assume that we found the optimal number of bins --> bin width ({age_bin_width:.4f}, for age and {total_time_bin_width:.4f} for tot. Time).\n")


    print("\ne)\n")
    print(f"The covariance between total rank and total time is {covariance(total_rank, total_time):.4f}")
    print(f"The covariance between age and total time is {covariance(age, total_time):.4f}")
    print(f"The covariance between swimming time and total time is {covariance(swimming_time, total_time):.4f}")
    print(f"The covariance between cycling time and running time is {covariance(cycling_time, running_time):.4f}")

    print("\n")
    print(f"The correlation between total rank and total time is {correlation(total_rank, total_time):.4f}")
    print(f"The correlation between age and total time is {correlation(age, total_time):.4f}")
    print(f"The correlation between swimming time and total time is {correlation(swimming_time, total_time):.4f}")
    print(f"The correlation between cycling time and running time is {correlation(cycling_time, running_time):.4f}")

    fig, axs = plt.subplots(2, 3, figsize=(16, 10))
    fig.tight_layout(pad=3.0)

    axs[0, 0].scatter(total_rank, total_time, color="green", edgecolors="w", linewidth=0.5)
    axs[0, 0].set_title("Total Rank vs Total Time")
    axs[0, 0].set_xlabel("Total Rank")
    axs[0, 0].set_ylabel("Total Time (minutes)")

    axs[0, 1].scatter(age, total_time, color="green", edgecolors="w", linewidth=0.5)
    axs[0, 1].set_title("Age of Participant vs Total Time")
    axs[0, 1].set_xlabel("Age in 2010 (years)")
    axs[0, 1].set_ylabel("Total Time (minutes)")

    axs[0, 2].scatter(swimming_time, running_time, color="green", linewidth=0.5)
    axs[0, 2].set_title("Running Time vs Swimming Time")
    axs[0, 2].set_xlabel("Swimming Time (minutes)")
    axs[0, 2].set_ylabel("Running Time (minutes)")

    axs[1, 0].scatter(swimming_time, total_time, color="green", linewidth=0.5)
    axs[1, 0].set_title("Swimming Time vs Total Time")
    axs[1, 0].set_xlabel("Swimming Time (minutes)")
    axs[1, 0].set_ylabel("Total Time (minutes)")

    axs[1, 1].scatter(cycling_time, total_time, color="green", linewidth=0.5)
    axs[1, 1].set_title("Cycling Time vs Total Time")
    axs[1, 1].set_xlabel("Cycling Time (minutes)")
    axs[1, 1].set_ylabel("Total Time (minutes)")

    axs[1, 2].scatter(running_time, total_time, color="green", linewidth=0.5)
    axs[1, 2].set_title("Running Time vs Total Time")
    axs[1, 2].set_xlabel("Running Time (minutes)")
    axs[1, 2].set_ylabel("Total Time (minutes)")

    plt.savefig("scatter_sheet2.png")
    
def ex2():
    PATH = np.loadtxt("data/radiation.txt")
    
    print("\n2a)\n")
    m = PATH[:, 0]
    u = PATH[:, 1]

    weights = 1 / (u ** 2)
    w_avg = np.sum(m * weights)/np.sum(weights)

    w_avg_uncertain = np.sqrt(1 / np.sum(weights))

    yearly = w_avg * 8760
    yearly_uncertain = w_avg_uncertain * 8760

    print(f"Weighted average radiation level: {yearly:.3f} mSv/year")
    print(f"Uncertainty in the weighted average radiation level: {yearly_uncertain:.4f} mSv/year")
    print(f"This leads to: {yearly:.3f} +/- {yearly_uncertain:.4f} mSv/year")

    
    print("\nb)\n")
    print("Natural Background radiation = 2.4 mSv/year")
    print("My range = [2.5261, 2.6559] mSv/year")
    print("--> higher than the Natural backgroud radiation")
    print("--> also difference between natural and mine (0.191) is more than the uncertainty (0.0649) ")
    print("--> so the two values are not compatible")
    

if __name__ == "__main__":
    ex1()
    ex2()  # uncomment to run ex2

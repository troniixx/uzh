# author: Mert Erol, 20-915-245

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

PATH = "/Users/merterol/Desktop/VSCode/uzh/Computational Science/Sem 3/PHY231/Exercise 1/ironman.txt"

data = np.loadtxt(PATH)

total_rank = data[:, 0]
year_of_birth = data[:, 1]
total_time = data[:, 2]
swimming_time = data[:, 3]
swimming_rank = data[:, 4]
cycling_time = data[:, 5]
cycling_rank = data[:, 6]
running_time = data[:, 7]
running_rank = data[:, 8]

age = 2010 - year_of_birth

# for task b)
min_val_total = np.min(total_time)
max_val_total = np.max(total_time)

min_age = np.min(age)
max_age = np.max(age)

with PdfPages("exercise_1_merterol.pdf") as pdf:
    plt.figure()
    plt.title("Task 1")
    plt.xlabel("Total Rank")
    plt.ylabel("Total Time")
    plt.scatter(total_rank, total_time, s = 25)
    pdf.savefig()
    plt.close()

    plt.figure()
    plt.title("Task 2")
    plt.xlabel("age")
    plt.ylabel("total time")
    plt.scatter(age, total_time, s = 25)
    pdf.savefig()
    plt.close()

    plt.figure()
    plt.title("Task 3")
    plt.xlabel("running time")
    plt.ylabel("swimming time")
    plt.scatter(running_time, swimming_time, s= 25)
    pdf.savefig()
    plt.close()

    plt.figure()
    plt.title("Task 4")
    plt.xlabel("swimming time")
    plt.ylabel("total time")
    plt.scatter(swimming_time, total_time, s = 25)
    pdf.savefig()
    plt.close()

    plt.figure()
    plt.title("Task 5")
    plt.xlabel("cycling time")
    plt.ylabel("total time")
    plt.scatter(cycling_time, total_time, s = 25)
    pdf.savefig()
    plt.close()

    plt.figure()
    plt.title("Task 6")
    plt.xlabel("running time")
    plt.ylabel("total time")
    plt.scatter(running_time, total_time, s = 25)
    pdf.savefig()
    plt.close()

    plt.figure()
    plt.title("Histogram Total Time")
    plt.xlabel("Total Time")
    plt.ylabel("Frequency")
    num_bins = int(np.sqrt(len(total_time)))
    plt.hist(total_time, bins=num_bins, label=f"Number of Bins: {num_bins}")
    plt.axvline(min_val_total, color="red", linestyle="dashed", linewidth=2, label=f"Min: {min_val_total:.2f}")
    plt.axvline(max_val_total, color="green", linestyle="dashed", linewidth=2, label=f"Max: {max_val_total:.2f}")
    plt.legend()
    pdf.savefig()
    plt.close()

    plt.figure()
    plt.title("Histogram Age")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    num_bins = int(np.sqrt(len(age)))
    plt.hist(age, bins=num_bins, label=f"Number of Bins: {num_bins}")
    plt.axvline(min_age, color="red", linestyle="dashed", linewidth=2, label=f"Min: {min_age:.2f}")
    plt.axvline(max_age, color="green", linestyle="dashed", linewidth=2, label=f"Max: {max_age:.2f}")
    plt.legend()
    pdf.savefig()
    plt.close()


print("Process finished")

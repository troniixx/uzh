import numpy as np
from sys import argv
import matplotlib.pyplot as plt

data = np.loadtxt(argv[1], dtype=int)

sums = data.sum(axis=1)
print("Total number of entries (from sums array):", len(sums))

plt.figure(figsize=(6,4))
plt.plot(range(1, 101), sums[:100], 'o', markersize=4)
plt.xlabel('Repetition (1–100)')
plt.ylabel('Sum of 3 dice')
plt.title('Sum for the first 100 repetitions')
plt.grid(True)
plt.tight_layout()
plt.savefig("sum_3_dice.png")

# Create bins from 2.5 to 18.5 (so integer sums 3..18 each get their own bin)
bins = np.arange(2.5, 19.5, 1.0)
counts, edges = np.histogram(sums, bins=bins)
centers = 0.5 * (edges[:-1] + edges[1:])  # bin midpoints
yerr = np.sqrt(counts)                    # error = sqrt(N)
xerr = 0.5                                # half-bin width

plt.figure(figsize=(7, 5))
# Plot the histogram (lightly colored bars)
plt.hist(sums, bins=bins, edgecolor='black', alpha=0.3, label='Histogram')

# Overlay the points with error bars
plt.errorbar(centers, counts, xerr=xerr, yerr=yerr, 
                fmt='o', color='red', ecolor='black', capsize=3,
                label='Bin counts with error')

plt.title('Distribution of sums of 3 dice (10,000 throws)')
plt.xlabel('Sum')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("dice_histogram.png")


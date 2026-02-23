import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 1/Testing/table_Mert.csv")

# summary of the data
print(data.describe())

# Check missing
print(data.isnull().sum())

# Visualize & Histogram
data.hist(bins=50, figsize=(20,15))
plt.show()

# Correlation matrix
matrix = data.corr()
sns.heatmap(matrix, annot=True)
plt.show()
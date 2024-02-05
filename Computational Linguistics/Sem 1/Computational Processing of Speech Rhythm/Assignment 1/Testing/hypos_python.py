import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 1/Testing/table_Mert.csv")

# Filter only "be," "ba," and "zh"
data_filtered = data[data['dialect'].isin(["be", "ba", "zh"])]

# Specified variables
# Just change variables depending on the hypothesis
variables_to_plot = ["rPVI_V_tier1", "rPVI_C_tier1", "nPVI_C_tier1", "nPVI_V_tier1"]

# Reshape the data for plotting with variable names
data_long = pd.melt(data_filtered, id_vars=['dialect'], value_vars=variables_to_plot, var_name='Variable', value_name='Value')

# Fancy colors for the boxplots
custom_colors = {"be": "#FF5733", "ba": "#FFB906", "zh": "#283BDA"}

# Create four separate box plots
plt.figure(figsize=(10, 6))
sns.boxplot(x='dialect', y='Value', hue='dialect', data=data_long, palette=custom_colors)
plt.title("Box Plots for Hypothesis 2")
plt.xlabel("Dialect")
plt.ylabel("Value")
plt.legend(title=None)
plt.show()

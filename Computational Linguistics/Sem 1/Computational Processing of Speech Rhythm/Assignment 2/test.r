library(tidyverse)

# ----- Analyze Intensity Variability Dataset -----
# Load the Intensity Variability data
intensityData <- read.csv("/path/to/intensityVariability_csv.csv")

# Visualization for Intensity Data - Standard Deviation and Variability Coefficient
ggplot(intensityData, aes(x = agegroup, y = stdev)) + 
    geom_boxplot() +
    labs(title = "Boxplot of Standard Deviation by Age Group", x = "Age Group", y = "Standard Deviation")

ggplot(intensityData, aes(x = agegroup, y = varco)) + 
    geom_boxplot() +
    labs(title = "Boxplot of Variability Coefficient by Age Group", x = "Age Group", y = "Variability Coefficient")

# Save the plot to a file
ggsave("intensity_boxplots.png", width = 10, height = 6)

# ----- Analyze CV Measures Dataset -----
# Load the CV Measures data
cvData <- read.csv("/path/to/CV_measures_2.csv", sep = ";") # Adjust the separator if needed

# Visualization for CV Data - Pairwise Variability Index
ggplot(cvData, aes(x = agegroup, y = rPVI)) + 
    geom_boxplot() +
    labs(title = "Boxplot of rPVI by Age Group", x = "Age Group", y = "rPVI")

ggplot(cvData, aes(x = agegroup, y = nPVI)) + 
    geom_boxplot() +
    labs(title = "Boxplot of nPVI by Age Group", x = "Age Group", y = "nPVI")

# Save the plot to a file
ggsave("cv_boxplots.pdf", width = 10, height = 6)

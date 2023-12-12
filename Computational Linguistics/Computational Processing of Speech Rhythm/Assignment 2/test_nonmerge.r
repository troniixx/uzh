# Load necessary library
library(tidyverse)

# ----- Analyze Intensity Variability Dataset -----
# Load the Intensity Variability data
intensityData <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 2/intensityVariability_csv.csv")

# Basic exploration of Intensity Data
summary(intensityData)
head(intensityData)

# Visualization for Intensity Data - Standard Deviation of Magnitude
ggplot(intensityData, aes(x = agegroup, y = stdevM)) + 
    geom_boxplot() +
    labs(title = "Standard Deviation of Magnitude by Age Group", x = "Age Group", y = "stdevM")

# Visualization for Intensity Data - Variability Coefficient of Magnitude
ggplot(intensityData, aes(x = agegroup, y = varcoM)) + 
    geom_boxplot() +
    labs(title = "Variability Coefficient of Magnitude by Age Group", x = "Age Group", y = "varcoM")

# ----- Analyze CV Measures Dataset -----
# Load the CV Measures data
cvData <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 2/CV_measures_2.csv", sep = ";") # Adjust the separator if needed

# Basic exploration of CV Data
summary(cvData)
head(cvData)

# Visualization for CV Data - Rate of CV
ggplot(cvData, aes(x = gender, y = rateCV_tier3)) + 
    geom_boxplot() +
    labs(title = "Rate of CV by Gender", x = "Gender", y = "Rate of CV")

# Visualization for CV Data - Variability Coefficient of CV
ggplot(cvData, aes(x = gender, y = varcoCV_tier3)) + 
    geom_boxplot() +
    labs(title = "Variability Coefficient of CV by Gender", x = "Gender", y = "varcoCV_tier3")

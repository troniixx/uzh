# Load necessary libraries
library(MASS)  # For lda function
library(tidyverse)  # For data manipulation

# Load the datasets
CV_data <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 2/CV_measures_2.csv", sep = ";")
intensity_data <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 2/intensityVariability_csv.csv")

# Handling missing values by removing rows with NA
CV_data <- na.omit(CV_data)
intensity_data <- na.omit(intensity_data)

# Performing LDA
# Replace 'class_column' with the actual name of your class/label column
lda_CV <- lda(speaker ~ ., data = CV_data)
lda_intensity <- lda(agegroup ~ ., data = intensity_data)

# Capture the output of LDA summaries
CV_measures_text <- capture.output(print(lda_CV))
intensityVariability_text <- capture.output(print(lda_intensity))

# Export LDA summaries to PDF files
sink("CV_measures_LDA_Summary.txt")
print(lda_CV)
sink()

# Redirect output to a PDF file for Intensity LDA Summary
sink("intensityVariability_LDA_Summary.txt")
print(lda_intensity)
sink()
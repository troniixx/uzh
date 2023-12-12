# Load necessary library
library(tidyverse)

# ----- Analyze Intensity Variability Dataset -----
# Load the Intensity Variability data
intensityData <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 2/intensityVariability_csv.csv")

# Basic exploration of Intensity Data
summary(intensityData)
head(intensityData)

# Visualization for Intensity Data
ggplot(intensityData, aes(x = agegroup, y = stdevM)) + 
    geom_boxplot() +
    labs(title = "Standard Deviation of Magnitude by Age Group", x = "Age Group", y = "stdevM")

# Statistical test for Intensity Data
t_test_intensity_stdevM <- t.test(stdevM ~ agegroup, data = intensityData)

# ----- Analyze CV Measures Dataset -----
# Load the CV Measures data
cvData <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 2/CV_measures_2.csv", sep = ";") # Adjust the separator if needed

# Ensure 'gender' is a factor with exactly two levels
cvData$gender <- factor(cvData$gender)
levels(cvData$gender)  # Check the levels of gender

# Visualization for CV Data
ggplot(cvData, aes(x = gender, y = rateCV_tier3)) + 
    geom_boxplot() +
    labs(title = "Rate of CV by Gender", x = "Gender", y = "rateCV_tier3")

# Perform t-test only if gender has exactly 2 levels
if (length(levels(cvData$gender)) == 2) {
    t_test_cv_rateCV <- t.test(rateCV_tier3 ~ gender, data = cvData)
    print(t_test_cv_rateCV)
} else {
    print("Gender does not have exactly two levels, t-test cannot be performed.")
}

# ----- Combine Insights Based on Common Features -----
# Merge key findings from both datasets based on 'subjectID' and 's'
combinedData <- merge(intensityData, cvData, by = c("subjectID", "s"))

# ----- Further Combined Analysis -----
# Exploratory analysis on the combined data
summary(combinedData)

# Visualization of the relationship between 'stdevM' and 'rateCV_tier3' across age groups
ggplot(combinedData, aes(x = stdevM, y = rateCV_tier3, color = agegroup)) + 
    geom_point() +
    labs(title = "Relationship between stdevM and rateCV_tier3 across Age Groups",
         x = "Standard Deviation of Magnitude (stdevM)",
         y = "Rate of CV (rateCV_tier3)")

# Statistical test on the combined data
# Example: correlation test between 'stdevM' and 'rateCV_tier3'
cor_test_result <- cor.test(combinedData$stdevM, combinedData$rateCV_tier3, method = "pearson")

# Print correlation test result
print(cor_test_result)

# Save the combined data to a new CSV file
write.csv(combinedData, "/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 2", row.names = FALSE)

# Note:
# - Replace "/path/to/yourfile.csv" with the actual file paths.
# - Replace 'stdevM' and 'rateCV_tier3' with actual metrics from your datasets if different.
# - Ensure 'subjectID' and 's' are the correct common columns for merging.

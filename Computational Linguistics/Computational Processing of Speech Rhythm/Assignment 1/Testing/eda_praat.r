library(dplyr)
library(tidyr)
library(ggplot2)

# Load data
data <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 1/Testing/table_Mert.csv") #nolint

# Filter the data to include only "be," "ba," and "zh"
data_filtered <- data %>% filter(dialect %in% c("be", "ba", "zh"))

# choose the specified variables
variables_to_plot <- c("rPVI_V_tier1", "rPVI_C_tier1", "nPVI_C_tier1", "nPVI_V_tier1") #nolint

# Gather the data for plotting with preserved variable names
data_long <- gather(data_filtered, key = "Variable", value = "Value", all_of(variables_to_plot)) #nolint

#Fancy colors for the boxplots
custom_colors <- c("be" = "#FF5733", "ba" = "#FFB906", "zh" = "#283BDA")

# Create four separate box plots for each of the chosen variables
ggplot(data_long, aes(x = dialect, y = Value, fill = dialect)) +
  geom_boxplot() +
  scale_fill_manual(values = custom_colors) +
  facet_wrap(~Variable, scales = "free") +
  labs(title = "Box Plots for Hypothesis 2", x = "dialect", y = "Value") +
  theme_minimal() +
  theme(legend.title = element_blank())
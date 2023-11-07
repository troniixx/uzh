library(dplyr)
library(tidyr)
library(ggplot2)

# Load your data
data <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 1/Testing/table_Mert.csv")

# Filter the data to include only "be," "ba," and "zh"
data_filtered <- data %>% filter(dialect %in% c("be", "ba", "zh"))

# Filter the data for the specified variables
variables_to_plot <- c("varcoC_tier1", "varcoV_tier1", "nPVI_C_tier1", "nPVI_V_tier1")

# Gather the data for plotting with preserved variable names
data_long <- gather(data_filtered, key = "Variable", value = "Value", all_of(variables_to_plot))

custom_colors <- c("be" = "#FF5733", "ba" = "#FFB906", "zh" = "#283BDA")

# Create separate box plots with custom colors
ggplot(data_long, aes(x = dialect, y = Value, fill = dialect)) +
  geom_boxplot() +
  scale_fill_manual(values = custom_colors) +  # Specify custom colors using hexadecimal codes
  facet_wrap(~Variable, scales = "free") +
  labs(title = "Box Plots for Hypothesis 1", x = "dialect", y = "Value") +
  theme_minimal() +
  theme(legend.title = element_blank())
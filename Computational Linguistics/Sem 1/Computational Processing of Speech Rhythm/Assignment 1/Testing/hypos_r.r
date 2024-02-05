library(dplyr)
library(tidyr)
library(ggplot2)

data <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 1/Testing/table_Mert.csv") #nolint

#Filter only "be," "ba," and "zh"
data_filtered <- data %>% filter(dialect %in% c("be", "ba", "zh"))

#specified variables
#just change variables depending on the hypothesis
variables <- c("rPVI_V_tier1", "rPVI_C_tier1", "nPVI_C_tier1", "nPVI_V_tier1") #nolint

# Gather the data for plotting with variable names
final <- gather(data_filtered, key = "Variable", value = "Value", all_of(variables)) #nolint

#Fancy colors for the boxplots
colors <- c("be" = "#FF5733", "ba" = "#FFB906", "zh" = "#283BDA")

# Create four separate box plots
ggplot(final, aes(x = dialect, y = Value, fill = dialect)) +
  geom_boxplot() +
  scale_fill_manual(values = colors) +
  facet_wrap(~Variable, scales = "free") +
  labs(title = "Box Plots for Hypothesis 2", x = "dialect", y = "Value") +
  theme_minimal() +
  theme(legend.title = element_blank())
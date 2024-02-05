# Load necessary libraries
library(tidyverse)
library(cluster)

# Load the data
data <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 2/CV_measures_2.csv", sep = ";")
data2 <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 2/intensityVariability_csv.csv")

summary(data)
summary(data2)

# Selecting relevant columns for clustering
clustering_data <- data %>%
  select(percentV_tier3, deltaConLn_tier2, deltaVLn_tier3, nPVI_Vof_tier2, rPVI_Con_tier2, varcoCV_tier3) %>%
  na.omit()

# Normalizing data
clustering_data <- scale(clustering_data)

# Applying k-means clustering with k=2
set.seed(123) # for reproducibility
km_result <- kmeans(clustering_data, centers = 2)

# Adding the cluster results to the original data
data$age_group <- as.factor(km_result$cluster)

# Defining the list of metrics for visualization
metrics <- c("percentV_tier3", "deltaConLn_tier2", "deltaVLn_tier3", "nPVI_Vof_tier2", "rPVI_Con_tier2", "varcoCV_tier3")

# Opening a new PDF device to save all plots
pdf("cluster_analysis_plots_final.pdf", width = 10, height = 6)

for (metric in metrics) {
  plot_title <- paste("Comparison of", metric, "between Clusters")
  p <- ggplot(data, aes_string(x = "age_group", y = metric, fill = "age_group")) +
    geom_boxplot() +
    theme_minimal() +
    labs(title = plot_title, x = "Cluster Group", y = metric)
  print(p)
}

# Closing the PDF device
dev.off()

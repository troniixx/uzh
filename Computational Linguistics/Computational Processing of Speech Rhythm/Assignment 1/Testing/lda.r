library(MASS)
library(caret)

data <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 1/Testing/table_Mert.csv")

#Variables incase we need them:
# "n", "rate", "mean", "meanLn", "delta", "deltaLn", "varco", "rPVI", "nPVI", "percentV"

set.seed(123)  # For reproducibility
train_index <- createDataPartition(data$Class, p = 0.7, list = FALSE)
training_data <- data[trainIndex, ]
testing_data <- data[-trainIndex, ]

lda_model <- lda(Class ~ Var1 + Var2, data = training_data)
lda_pred <- predict(lda_model, newdata = testing_data)

confusionMatrix(lda_pred$class, testing_data$Class)

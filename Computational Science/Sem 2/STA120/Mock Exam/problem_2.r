library(ggplot2)
set.seed(123)

# **** Task a) ****
X <- rbinom(1000, size = 50, prob = 0.4)

#plot histogram
hist(X, probability = TRUE, col = "blue",
        main = "Histogram of Binomial Samples with PMF",
        xlab = "Number of Successes", ylab = "Probability")

#plot pmf
X_values <- 0:50
pmf_values <- dbinom(X_values, size = 50, prob = 0.4)
points(X_values, pmf_values, col = "red", pch = 19)

ggplot() + geom_point(aes(x = X_values, y = pmf_values), col = "red", pch = 19) +
    geom_line(aes(x = X_values, y = pmf_values), col = "red")

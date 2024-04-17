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

ggplot() + geom_line(x = X_values, y = pmf_values, col = "red", linewidth = 1) +
    geom_point(x = X_values, y = pmf_values, col = "red", pch = 19)

# **** Task b) ****
#sample 50 trials
X_sample <- rbinom(50, size = 50, prob = 0.4)

#estimate parameter p
p_hat <- sum(X_sample) / (50 * 50)
print("P estimate = ")
print(p_hat)

#get wald confidence interval
z <- qnorm(0.975)
wald_ci <- c(p_hat - z * sqrt(p_hat * (1 - p_hat) / 50), p_hat + z * sqrt(p_hat * (1 - p_hat) / 50))
print("Wald Confidence interval = ")
print(wald_ci)

# **** Task c) ****
n <- 50
p_true <- 0.4
num_samples <- 1000

samples <- rbinom(num_samples, size = n, prob = p_true)

p_values <- sapply(samples, function(x) {
    res <- prop.test(x, n, p = 0.4)
    return(res$p.value)
})

percentage <- mean(p_values < 0.05) * 100
print("Percentage of p-values < 0.05 = ")
print(percentage)

# **** Task d) ****

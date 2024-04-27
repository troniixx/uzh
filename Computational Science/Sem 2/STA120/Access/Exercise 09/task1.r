# use the following code as a base:
set.seed(5)         ## for reproducible simulations 
beta0.true <- 1    ## true parameters, intercept
beta1.true <- 2     ## and slope
## observed x values:
x <- c(2.9, 6.7, 8.0, 3.1, 2.0, 4.1, 2.2, 8.9,
        8.1, 7.9, 5.7, 1.6, 6.6, 3.0, 6.3)

## simulation of y values:
y <- beta0.true + beta1.true * x + rnorm(length(x), mean = 0, sd = 2)

pearson_cor <- cor(x, y, method = "pearson")
spearman_cor <- cor(x, y, method = "spearman")


x.mean <- mean(x)
y.mean <- mean(y)

# Use formulas from the script
beta1.hat <- sum((x-x.mean)*(y-y.mean))/sum((x-x.mean)^2)
beta0.hat <- y.mean - beta1.hat*x.mean

sol <- list(Pearson_correlation_coefficients = pearson_cor,
        Spearman_correlation_coefficients = spearman_cor,
	    beta1_hat = beta1.hat, beta0_hat = beta0.hat)

print(sol)
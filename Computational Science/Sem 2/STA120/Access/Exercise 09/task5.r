# use the following code as a base:
set.seed(5)         ## for reproducible simulations 
beta0.true <- 1     ## true parameters, intercept
beta1.true <- 2     ## and slope
## observed x values:
x <- c(2.9, 6.7, 8.0, 3.1, 2.0, 4.1, 2.2, 8.9,
       8.1, 7.9, 5.7, 1.6, 6.6, 3.0, 6.3) 
## simulation of y values:
y <- beta0.true + beta1.true * x + rnorm(length(x), mean = 0, sd = 2)

data <- data.frame(x = x, y = y)

# start here to calculate your solution for the problem:
mod <- ... # Create a linear model.
smry <- ... # Show the summary.
fit <- ... # Calculate fitted values.
res <- ... # Calculate residuals.
ci <- ... # Calculate CIs of the model.

sol <- list(summary = smry, fitted = fit,  residuals = res, ci = ci)

set.seed(5)         ## for reproducible simulations 
beta0.true <- 1    ## true parameters, intercept
beta1.true <- 2     ## and slope

x <- c(2.9, 6.7, 8.0, 3.1, 2.0, 4.1, 2.2, 8.9,
       8.1, 7.9, 5.7, 1.6, 6.6, 3.0, 6.3) 

y <- beta0.true + beta1.true * x + rnorm(15, 0, 2)

data <- data.frame(x = x, y = y) #format as a table   

mod <- lm(y ~ x, data = data) # Create a linear model.
smry <- summary(mod) # Show the summary.
fit <- fitted(mod) # Calculate fitted values.
res <- residuals(mod) # Calculate residuals.
ci <- confint(mod) # Calculate CIs of the model.

sol <- list(summary = smry, fitted = fit,  residuals = res, ci = ci)

png(file="solution.png")
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
    mod <- lm(y ~ x, data = data) # Basic LM
    mod2 <- lm(y ~ x + 0, data = data) # b_0 = 0 LM
    par(mfrow = c(1, 1))
    plot(data)
    abline( mod , col = "red") # fit with intercept
    abline( mod2, lty = 2) # fit without intercept
dev.off()
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
    data_outlier <- rbind(data, data.frame(x = c(10, 11, 12), y = c(9, 7, 8)))
    par(mfrow = c(2, 3))

    # plot outliers and make sure outliers have different color
    plot(data_outlier, col = c(rep(1, length(x) ), rep(2, length(y) )), 
          main = "scatterplot of the data")

    model_outlier <- lm(y ~ x, data = data_outlier) # Build a LM with new data

    plot(model_outlier) # Plot the model assumptions (diagnostic plot)

dev.off()
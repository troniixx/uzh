png(file = "solution.png")
    require(mvtnorm)
    set.seed(14)
    mu <- c(1, 2)
    sigma <- matrix(1, 1, 1, 2, byrow = TRUE, nrow = 2)
    res <- ...
    
    # from (b)
    par(mai = c(0.8, 0.8, 0.1, 0.1)) # to have a proper aspect ratio
    plot(res, xlab = "y", ylab = "z", pch = 20,
            xlim = c(-3, 7), ylim = c(-3, 7))

    # exercise now
    # Make sure you choose a right operator instead of "%%%".
    points(... > ... "%%%" ... < ... , ... ], col = "red", pch = 20) #nolint
    z <- ...
    mu.constr <- ... # Use formula from the lecture.
    sigma.constr <- ... # Use formula from the lecture.
    y.constr <- ... # Generating 100 points with new mu and sigma
    points(y.constr, rep(z, 100), col = "blue", pch = 20)
dev.off()

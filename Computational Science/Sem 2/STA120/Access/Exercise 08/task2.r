png(file = "solution.png")
    mu <- c(1, 2)
    sigma <- matrix(c(1, 1, 1, 2), byrow = TRUE, nrow = 2)

    require(fields)
    require(mvtnorm)
    par(mai = c(0.8, 0.8, 0.1, 0.1))
    y <- seq(-2, 4, length = 100)
    z <- seq(-2, 6, length = 100)
    grid <- expand.grid(y = y, z = z)

    desngrid <- 

    jdensity <- array(densgrid, c(100, 100))
    image.plot(y, z, jdensity, col = tim.colors())
dev.off()
png(file="solution.png")
  require(mvtnorm)
  set.seed(14)
  mu <- c(1, 2)
  sigma <- matrix(c(1, 1, 1, 2), byrow = TRUE, nrow = 2)
  res <- rmvnorm(n = 500, mean = mu, sigma = sigma)
  
  # from (b)
  par(mai = c(0.8, 0.8, 0.1, 0.1)) # to have a proper aspect ratio
  plot(res, xlab = "y", ylab = "z", pch = 20,
       xlim = c(-3, 7), ylim = c(-3, 7))
  
  # exercise now
  # Make sure you choose a right operator instead of "%%%".
  points(res[res[, 2] > 3 & res[, 2] < 4, ], col = "red", pch = 20)
  z <- 3.5
  mu.constr <- mu[1] + sigma[1, 2] * (1/sigma[2, 2]) * sigma[2, 1] # Use formula from the lecture.
  sigma.constr <- sigma[1, 1] - sigma[1, 2] * (1/sigma[2, 2]) * sigma[2, 1] # Use formula from the lecture.
  y.constr <- rnorm(100, mu.constr, sqrt(sigma.constr)) # Generating 100 points with new mu and sigma
  points(y.constr, rep(z, 100), col = "blue", pch = 20)
dev.off()

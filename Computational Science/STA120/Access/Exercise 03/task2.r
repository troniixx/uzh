png(file="solution.png")
  lambda <- 5
  grid <- 0:12
  n <- c(10, 100, 1000)
  
  par(mfrow = c(1, 3))
  for (i in 1:length(n)) {
    plot(grid , dpois(grid, lambda) , main = paste("n =", n[i]), type = "h",
         ylim = c(0, 0.25), xlab = "", ylab = "", col = 1)

    points( grid, dpois(grid, lambda), col = 1, pch = 20)

    points( (grid) +0.1, dbinom(grid, size = n[i], p = lambda/n[i]) , type = "h", col = 2)

    points((grid)+0.1, dbinom(grid, size = n[i], p = lambda/n[i]) , col = 2, pch = 20)

    legend("topright", pch = 20, legend = c("Pois", "Binom"), col = c(1, 2))
  }
dev.off()

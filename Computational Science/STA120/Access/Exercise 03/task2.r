png(file="solution.png")
  lambda <- ...
  grid <- 0:12
  n <- ...
  
  par(mfrow = c(1, 3))
  for (i in 1:length(n)) {
    plot( ... , ... , main = paste("n =", n[i]), type = "h",
         ylim = c(0, 0.25), xlab = "", ylab = "", col = 1)
    points( ... , ..., col = 1, pch = 20)
    points( ... +0.1, ... , type = "h", col = 2)
    points((grid)+0.1, ... , col = 2, pch = 20)
    legend("topright", pch = 20, legend = c("Pois", "Binom"), col = c(1, 2))
  }
dev.off()
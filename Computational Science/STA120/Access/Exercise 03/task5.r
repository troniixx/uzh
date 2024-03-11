png(file="solution.png")
  lambda1 <- 0.2
  lambda2 <- 2
  grid <- 0:8
  
  par(mfrow = c(1, 2))
  plot(grid , dpois(grid , lambda1 ), main = "PMFs", type = "h",
       xlab = expression(x), ylab = expression(f(x)), col = "blue")
  points(grid, dpois( grid , lambda1 ), col = "blue", pch = 20)
  points( grid +0.1, dpois(grid, lambda2) , type = "h", col = "red")
  points( grid+0.1, dpois(grid, lambda2) , col = "red", pch = 20)
  legend("topright", pch = 20,
         legend = c(expression(lambda == 0.2), expression(lambda == 2)), 
         col = c("blue", "red"))
  
  probs1 <- c(0, ppois(grid, lambda1)) # Use ppois() here, and make sure to include an additional point at 0
  probs2 <- c(0, ppois(grid, lambda2)) # Use ppois() here
  
  plot(stepfun( grid, probs1 ), verticals = TRUE , pch = 20, 
       xlab = expression(x), ylab = expression(F(x)), 
       main = "CDFs", col = "blue")
  plot( stepfun(grid, probs2) , verticals = TRUE, add = TRUE, pch = 20, col = "red")
  legend("bottomright", pch = 20, 
         legend = c(expression(lambda == 0.2), expression(lambda == 2)),
         col = c("blue", "red"))
  
dev.off()

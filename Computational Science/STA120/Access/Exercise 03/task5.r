png(file="solution.png")
  lambda1 <- ...
  lambda2 <- ...
  grid <- 0:8
  
  par(mfrow = c(1, 2))
  plot( ... , dpois( ... , ... ), main = "PMFs", type = "h",
       xlab = expression(x), ylab = expression(f(x)), col = "blue")
  points( ... , dpois( ... , ... ), col = "blue", pch = 20)
  points( ... +0.1, ... , type = "h", col = "red")
  points( ... +0.1, ... , col = "red", pch = 20)
  legend("topright", pch = 20,
         legend = c(expression(lambda == 0.2), expression(lambda == 2)), 
         col = c("blue", "red"))
  
  probs1 <- ... # Use ppois() here, and make sure to include an additional point at 0
  probs2 <- ... # Use ppois() here
  
  plot(stepfun( ... ), verticals = ... , pch = 20, 
       xlab = expression(x), ylab = expression(F(x)), 
       main = "CDFs", col = "blue")
  plot( ... , verticals = ..., add = TRUE, pch = 20, col = "red")
  legend("bottomright", pch = 20, 
         legend = c(expression(lambda == 0.2), expression(lambda == 2)),
         col = c("blue", "red"))
  
dev.off()
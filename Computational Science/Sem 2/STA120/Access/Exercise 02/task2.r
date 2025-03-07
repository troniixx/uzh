png(file="solution.png")
P1 <- pnorm(4, mean = 2, sd = sqrt(16))
P2 <- pnorm(4, mean = 2, sd = sqrt(16)) - pnorm(0, mean = 2, sd = sqrt(16))
Q1 <- qnorm(0.95, 2, sqrt(16), lower.tail = FALSE)
Q2 <- -qnorm(0.05, 2, sqrt(16))

sol <- list("Results" = c(P1, P2, Q1, Q2))

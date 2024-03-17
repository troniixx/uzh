require(spam)
data(Oral)

smry <- summary(Oral)
maximum <- which.max(Oral$E)

mean_SMR <- mean(Oral$SMR)
n <- 544 
S2 <- 1/(n-1)*sum((Oral$SMR-mean_SMR)^2)
S <- sqrt(S2)
ci <- mean_SMR + c(-1, 1) * qt(0.975, n-1, lower = TRUE) * S/sqrt(n)


sol <- list(smry, maximum, mean_SMR, ci)
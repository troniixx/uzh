require( spam )
data( Oral )
str(Oral)

smry <- summary(Oral)
maximum <- max(Oral)

mean_SMR <- mean(Oral$SMR)
n <- 544 
S2 <- sum((Oral$SMR - mean_SMR)^2)/(n-1)
S <- sqrt(S2)
ci <- mean(Oral$SMR) + c(-1, 1) * qt(0.975, n-1, lower = TRUE) * S/sqrt(n)


sol <- list(smry, maximum, mean_SMR, ci)
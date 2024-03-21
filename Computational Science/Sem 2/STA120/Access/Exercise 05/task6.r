set.seed(5)
...
# t-distribution
...

typeI_t <-...

#chi-squared distribution
...
typeI_chi2 <- ...

par(mfrow = c(1, 2))
hist(..., main = "t-distribution", xlab = "p-values")
hist(..., main = "chi-square distribution", xlab = "p-values")


sol <- list(typeI_t = typeI_t, typeI_chi2=typeI_chi2)
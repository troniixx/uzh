set.seed(5)
pvals_t = c()
pvals_chi2 = c()

# t-distribution
for (i in 1:1000) {
    ttest = t.test(rnorm(10, mean = 0, sd = 1), conf.level = 0.95)
    pvals_t = c(pvals_t, ttest$p.value)
}
typeI_t <- sum(pvals_t < 0.05) / 1000

#chi-squared distribution
for(i in 1:1000){
    obs <- table(factor(sample(1:2, 10, replace = TRUE), levels = 1:2))
    exp <- c(5, 5)
    chi2test = chisq.test(obs, p = exp/sum(exp))
    pvals_chi2 = c(pvals_chi2, chi2test$p.value)
}
typeI_chi2 <- sum(pvals_chi2 < 0.05) / 1000

par(mfrow = c(1, 2))
hist(pvals_t, main = "t-distribution", xlab = "p-values")
hist(pvals_chi2, main = "chi-square distribution", xlab = "p-values")

sol <- list(typeI_t = typeI_t, typeI_chi2=typeI_chi2)
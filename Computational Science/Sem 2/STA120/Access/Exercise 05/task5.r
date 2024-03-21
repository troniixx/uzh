set.seed(5)

pvals = c()

for (i in 1:1000) {
    ttest = t.test(rnorm(10, mean = 0, sd = 1), conf.level = 0.95)
    pvals = c(pvals, ttest$p.value)
}

hist(pvals, main = "Histogram of p-values", xlab = "p-values")

err = sum(pvals < 0.05) / 1000

sol <- list(type_I_error = err)

print(sol)
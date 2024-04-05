n <- 95
x <- 8

ex_CI <- binom.test(x, n, conf.level = 0.95)$conf.int
app_CI <- prop.test(x, n, conf.level = 0.95)$conf.int

sol <- list(ex_CI = ex_CI, app_CI = app_CI)

print(sol)
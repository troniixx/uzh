# use the following code as a base:
set.seed(5)         ## for reproducible simulations 
beta0.true <- 1     ## true parameters, intercept
beta1.true <- 2     ## and slope
## observed x values:
x <- c(2.9, 6.7, 8.0, 3.1, 2.0, 4.1, 2.2, 8.9,
        8.1, 7.9, 5.7, 1.6, 6.6, 3.0, 6.3) 
## simulation of y values:
y <- beta0.true + beta1.true * x + rnorm(length(x), mean = 0, sd = 2)

# start here to calculate your solution for the problem:
x.mean <- mean(x)
y.mean <- mean(y)
beta1.hat <- sum((x-x.mean)*(y-y.mean))/sum((x-x.mean)^2)
beta0.hat <- y.mean - beta1.hat*x.mean
y.fitted <- beta0.hat + beta1.hat*x
residuals <- y - y.fitted
SS <- sum(residuals^2)

n <- length(x)
sigma.e <- sqrt(SS/(n-2))
beta0.se <- sigma.e * sqrt(1/n + x.mean^2/sum((x-x.mean)^2))
beta1.se <- sigma.e / sqrt(sum((x-x.mean)^2))


beta0.ci <- beta0.hat + c(-1, 1) * qt(0.975, df = n-2) * beta0.se
beta1.ci <- beta1.hat + c(-1, 1) * qt(0.975, df = n-2) * beta1.se

t0 <- (beta0.hat)/beta0.se
t1 <- (beta1.hat)/beta1.se
# Think about why abs() here:
p.value0 <- 2 * pt(abs(t0), df = n-2 , lower.tail = FALSE) 
p.value1 <- 2 * pt(abs(t1), df = n-2 , lower.tail = FALSE)

sol <- list(beta0_ci = beta0.ci, beta1_ci = beta1.ci,
t0 = t0, t1 = t1, pvalue0 = p.value0, pvalue1 = p.value1)
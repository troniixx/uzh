# Problem 1

# a)
set.seed <- 15
n <- 15
beta_0 <- 1
beta_1 <- 2
mu <- 4
sigma_x <- 4
sigma <- 2

x <- rnorm(n, mu, sigma_x)
y <- beta_0 + beta_1 * x + rnorm(n, 0, sigma)
plot(y ~ x)
(m1 <- lm(y ~ x))

abline(beta_0, beta_1)
abline(m1, lty = 2)
legend("topleft", legend = c("True", "Estimated"), lty = 1:2, bty = "n")


# b)
R <- 1000

# Problem 3
# Author: Mert Erol

require(mvtnorm)
set.seed(123)

mu <- c(2, 5)
Sigma <- matrix(c(1, 1/2, 1/2, 1), 2, 2)

# a)
print(eigen(Sigma))

# b)
n <- 100
par(pty = "s", lwd = 2)

X <- rmvnorm(n, mu, Sigma)
plot(X, xlab = "X", ylab = "Y", col = "blue", xlim = range(X), ylim = range(X))

# c)

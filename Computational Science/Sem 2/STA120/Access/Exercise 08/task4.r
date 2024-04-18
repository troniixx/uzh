set.seed(15)

c <- 0.5

X <- rnorm(1000)
Y <- ifelse(abs(X) >= c, X, -X)
N <- sum(X + Y == 0) / 1000 # What proportion of zero entries do we have?

X0 <- sum(X == 0)
Y0 <- sum(Y == 0)

par(mfrow = c(2, 2))
qqnorm(X, main = "QQ-plot of X")
qqnorm(Y, main = "QQ-plot of Y")

qqnorm(X + Y, main = "QQ-plot of X+Y")
hist(X + Y, breaks = 50, main = "Histogram of X+Y", prob = TRUE)

sol <- list(N = N, X0 = X0, Y0 = Y0)
print(sol)
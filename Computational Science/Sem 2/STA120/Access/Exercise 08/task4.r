set.seed(15)

c <- 0.5

X <- rnorm(1000)
Y <- if(abs(X) >= c) X else -X
N <- ... # What proportion of zero entries do we have?

X0 <- ...
Y0 <- ...

par(mfrow = c(2, 2))
qqnorm( ... , main = "QQ-plot of X")
qqnorm( ... , main = "QQ-plot of Y")

qqnorm( ... , main = "QQ-plot of X+Y")
hist( ... , breaks = 50, main = "Histogram of X+Y", prob = ...)

sol <- list(N = N, X0 = X0, Y0 = Y0)

png(file = "solution.png")
set.seed(1)
theta <- 8
n <- c(10, 50, 10000)
par(mfrow = c(3, 2))

for (i in n) {
    x <- runif(i, 0, theta)
    hist(x, prob = TRUE, col = "blue")
    # Add density Lines with color "red"
    lines(density(x), col = "red")
    # QQ-Plot using 500 probability points (ppoints)
    qqplot(ppoints(500), x)
}

dev.off()
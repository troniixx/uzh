png(file = "solution.png")
    n <- 95
    x <- 8
    p <- x / n

    #We compare the "exact" CDF with the one obtained from the CLT.
	grid <- seq(0, 0.25, length.out = 1000)

	plot(grid , pbinom(grid*n, size = n , prob = p ), type = "l",
		col = "red", xlab = "x", ylab = "P(X <= x)",
		ylim = c(0, 1), main = "Exact distribution vs. CLT approximation")

	lines(grid, pnorm(grid, mean = p , sd = sqrt(1/n * p * (1-p))), col = "blue")

	legend("bottomright", legend = c("exact", "approximation"),
		lty = 1, col = c("red", "blue"))
dev.off()

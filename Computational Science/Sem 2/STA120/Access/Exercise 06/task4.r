n <- 95
x <- 8

WilsonCI <- function(x, n, alpha = 0.05){
    p <- x/n
    z <- qnorm(1 - alpha/2)
    p_adj <- (p + z^2 / (2 * n)) / (1 + z^2 / n)
    adjustment <- z * sqrt((1/n) * p * (1 - p) + z^2 / (4 * n^2)) / (1 + z^2 / n)
    lower_bound <- p_adj - adjustment
    upper_bound <- p_adj + adjustment


    CI <- c(lower_bound, upper_bound)
    return(CI)
}

CI <- WilsonCI(x, n)
sol <- list(CI = CI)

print(sol)